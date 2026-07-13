#!/usr/bin/env python3
"""Generate the public, read-only Lab NAS snapshot and aggregate history."""

from __future__ import annotations

import json
import os
import socket
import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = ROOT.parent
OUTPUT_ROOT = PROJECT_ROOT / "dist" / "api" / "lab" / "v1"
NAS_ROOT = OUTPUT_ROOT / "nas"
HISTORY_STORE = ROOT / "history-hourly.json"
SERVICES_FILE = ROOT / "services.json"
SCHEMA_VERSION = "1.0"
STALE_AFTER_SECONDS = 7200


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def atomic_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, ensure_ascii=False, separators=(",", ":"))
            handle.write("\n")
        os.chmod(temp_name, 0o644)
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def read_cpu_totals() -> tuple[int, int]:
    fields = Path("/proc/stat").read_text(encoding="utf-8").splitlines()[0].split()[1:]
    values = [int(value) for value in fields]
    idle = values[3] + (values[4] if len(values) > 4 else 0)
    return sum(values), idle


def cpu_usage() -> float | None:
    try:
        total_a, idle_a = read_cpu_totals()
        time.sleep(0.2)
        total_b, idle_b = read_cpu_totals()
        total_delta = total_b - total_a
        if total_delta <= 0:
            return None
        return round(max(0.0, min(1.0, 1 - (idle_b - idle_a) / total_delta)), 4)
    except (OSError, ValueError, IndexError):
        return None


def memory_usage() -> float | None:
    try:
        values: dict[str, int] = {}
        for line in Path("/proc/meminfo").read_text(encoding="utf-8").splitlines():
            key, raw = line.split(":", 1)
            values[key] = int(raw.strip().split()[0])
        total = values["MemTotal"]
        available = values.get("MemAvailable", values.get("MemFree", 0))
        return round(max(0.0, min(1.0, 1 - available / total)), 4)
    except (OSError, ValueError, KeyError, ZeroDivisionError):
        return None


def temperature() -> float | None:
    readings: list[float] = []
    for path in Path("/sys/class/thermal").glob("thermal_zone*/temp"):
        try:
            value = float(path.read_text().strip())
            if value > 1000:
                value /= 1000
            if 5 <= value <= 110:
                readings.append(value)
        except (OSError, ValueError):
            continue
    return round(max(readings), 1) if readings else None


def storage() -> dict[str, int | float | None]:
    stats = os.statvfs("/vol2")
    total = stats.f_blocks * stats.f_frsize
    free = stats.f_bavail * stats.f_frsize
    used = total - free
    ratio = round(used / total, 6) if total else None
    previous_path = ROOT / "last-storage.json"
    previous_used = None
    try:
        previous_used = json.loads(previous_path.read_text(encoding="utf-8")).get("usedBytes")
    except (OSError, ValueError, AttributeError):
        pass
    atomic_json(previous_path, {"usedBytes": used, "recordedAt": iso(utc_now())})
    return {
        "usedBytes": used,
        "totalBytes": total,
        "usageRatio": ratio,
        "change24hBytes": used - previous_used if isinstance(previous_used, int) else None,
    }


def uptime_seconds() -> int | None:
    try:
        return int(float(Path("/proc/uptime").read_text().split()[0]))
    except (OSError, ValueError, IndexError):
        return None


def tcp_status(host: str, port: int) -> str:
    try:
        with socket.create_connection((host, port), timeout=1):
            return "online"
    except OSError:
        return "offline"


def services() -> list[dict[str, Any]]:
    configs = json.loads(SERVICES_FILE.read_text(encoding="utf-8"))
    result = []
    for config in configs:
        status = "online" if config.get("kind") == "storage" else tcp_status(config.get("host", "127.0.0.1"), int(config["port"]))
        result.append({
            "id": config["id"],
            "label": config["label"],
            "category": config["category"],
            "status": status,
            "availabilityRatio24h": None,
            "activityLevel": config.get("activityLevel", "unknown"),
        })
    return result


def envelope(now: datetime, data: Any, source_status: str = "ok") -> dict[str, Any]:
    return {
        "schemaVersion": SCHEMA_VERSION,
        "generatedAt": iso(now),
        "staleAfterSeconds": STALE_AFTER_SECONDS,
        "sourceStatus": source_status,
        "data": data,
    }


def load_history() -> list[dict[str, Any]]:
    try:
        value = json.loads(HISTORY_STORE.read_text(encoding="utf-8"))
        return value if isinstance(value, list) else []
    except (OSError, ValueError):
        return []


def aggregate(points: list[dict[str, Any]], hours: int, bucket_hours: int) -> list[dict[str, Any]]:
    cutoff = utc_now() - timedelta(hours=hours)
    recent = [point for point in points if datetime.fromisoformat(point["timestamp"].replace("Z", "+00:00")) >= cutoff]
    if bucket_hours == 1:
        return recent[-(hours + 1):]
    buckets: dict[str, list[dict[str, Any]]] = {}
    for point in recent:
        dt = datetime.fromisoformat(point["timestamp"].replace("Z", "+00:00"))
        bucket_hour = dt.hour - dt.hour % bucket_hours
        key = iso(dt.replace(hour=bucket_hour, minute=0, second=0, microsecond=0))
        buckets.setdefault(key, []).append(point)
    output = []
    keys = ["cpuUsageRatioAvg", "memoryUsageRatioAvg", "temperatureCelsiusAvg", "storageUsageRatio", "onlineServiceRatio"]
    for timestamp in sorted(buckets):
        row: dict[str, Any] = {"timestamp": timestamp}
        for key in keys:
            values = [item[key] for item in buckets[timestamp] if isinstance(item.get(key), (int, float))]
            row[key] = round(sum(values) / len(values), 4) if values else None
        output.append(row)
    return output


def main() -> None:
    now = utc_now()
    service_data = services()
    online = [item for item in service_data if item["status"] == "online"]
    metrics = {
        "cpuUsageRatio": cpu_usage(),
        "memoryUsageRatio": memory_usage(),
        "temperatureCelsius": temperature(),
    }
    storage_data = storage()
    snapshot_data = {
        "system": {"id": "ayue-nas", "label": "Ayue NAS", "status": "online", "uptimeSeconds": uptime_seconds()},
        "metrics": metrics,
        "storage": storage_data,
        "backup": {"lastCompletedAt": None, "lastResult": "unknown"},
        "services": service_data,
    }
    point = {
        "timestamp": iso(now.replace(minute=0, second=0, microsecond=0)),
        "cpuUsageRatioAvg": metrics["cpuUsageRatio"],
        "memoryUsageRatioAvg": metrics["memoryUsageRatio"],
        "temperatureCelsiusAvg": metrics["temperatureCelsius"],
        "storageUsageRatio": storage_data["usageRatio"],
        "onlineServiceRatio": round(len(online) / len(service_data), 4) if service_data else None,
    }
    history = load_history()
    history = [item for item in history if item.get("timestamp") != point["timestamp"]]
    history.append(point)
    history = history[-24 * 35:]
    atomic_json(HISTORY_STORE, history)

    history24 = aggregate(history, 24, 1)
    history7 = aggregate(history, 24 * 7, 6)
    atomic_json(NAS_ROOT / "snapshot", envelope(now, snapshot_data))
    atomic_json(NAS_ROOT / "history-24h", envelope(now, {"range": "24h", "resolutionSeconds": 3600, "points": history24}))
    atomic_json(NAS_ROOT / "history-7d", envelope(now, {"range": "7d", "resolutionSeconds": 21600, "points": history7}))
    atomic_json(OUTPUT_ROOT / "manifest", envelope(now, {
        "labVersion": "0.1.0",
        "projects": [
            {"id": "temporal-field", "section": "visual-systems", "dataMode": "client-only", "status": "available"},
            {"id": "nas-constellation", "section": "nas-observatory", "dataMode": "periodic-snapshot", "status": "available"},
        ],
        "nasCapabilities": {"snapshot": True, "history24h": True, "history7d": True, "realtime": False},
    }))


if __name__ == "__main__":
    main()
