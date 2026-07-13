#!/usr/bin/env python3
"""Minimal same-origin, read-only Data Gateway for Lab public JSON."""

from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent
DATA_ROOT = ROOT.parent / "dist" / "api" / "lab" / "v1"
HOST = "127.0.0.1"
PORT = 18101


class GatewayHandler(BaseHTTPRequestHandler):
    server_version = "AyueLabGateway/1.0"

    def log_message(self, format: str, *args: object) -> None:
        print(f"{self.address_string()} - {format % args}")

    def send_json_file(self, path: Path) -> None:
        if not path.is_file():
            self.send_error_json(HTTPStatus.SERVICE_UNAVAILABLE, "snapshot_unavailable", "No public Lab snapshot is currently available.")
            return
        content = path.read_bytes()
        etag = f'"{path.stat().st_mtime_ns:x}-{len(content):x}"'
        if self.headers.get("If-None-Match") == etag:
            self.send_response(HTTPStatus.NOT_MODIFIED)
            self.end_headers()
            return
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "public, max-age=300, stale-while-revalidate=3600")
        self.send_header("ETag", etag)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(content)

    def send_error_json(self, status: HTTPStatus, code: str, message: str) -> None:
        content = json.dumps({
            "schemaVersion": "1.0",
            "error": {"code": code, "message": message, "retryAfterSeconds": 3600},
        }, separators=(",", ":")).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path == "/api/lab/v1/manifest":
            self.send_json_file(DATA_ROOT / "manifest")
            return
        if parsed.path == "/api/lab/v1/nas/snapshot":
            self.send_json_file(DATA_ROOT / "nas" / "snapshot")
            return
        if parsed.path == "/api/lab/v1/nas/history":
            range_value = parse_qs(parsed.query).get("range", [""])[0]
            if range_value not in {"24h", "7d"}:
                self.send_error_json(HTTPStatus.BAD_REQUEST, "invalid_range", "Allowed ranges are 24h and 7d.")
                return
            self.send_json_file(DATA_ROOT / "nas" / f"history-{range_value}")
            return
        self.send_error_json(HTTPStatus.NOT_FOUND, "route_not_found", "This public Lab API route does not exist.")


if __name__ == "__main__":
    ThreadingHTTPServer((HOST, PORT), GatewayHandler).serve_forever()
