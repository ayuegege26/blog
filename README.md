<div align="center">

# Ayue Observatory

**A long-running personal observatory for archives, experiments, systems, and signals.**

[English](README.md) · [简体中文](README.zh-CN.md) · [v0.2.2p Preview Notes](RELEASE_NOTES_v0.2.2p.md)

</div>

## Overview

Ayue Observatory is a personal publishing and experimentation site built with Astro. It is intentionally different from a conventional blog, portfolio, SaaS dashboard, or NAS administration panel.

The main site uses **Archive Objects** as its durable content unit: numbered, typed, dated records that can be indexed, revised, and related over time. The separate **Lab** area is reserved for technically ambitious browser experiments and read-only views of periodically collected infrastructure data.

Preview `v0.2.2p` expands that foundation into two content-led visual systems: the public-archive map **Archive Atlas** and the in-progress spatial experiment **Server World**. The preview label is intentional: Server World has a usable formal scene and interaction model, while final node content and Gate 5 release acceptance remain unfinished.

Production domain: [http://blog.ayuegege26.xyz](http://blog.ayuegege26.xyz). This personal site prioritizes direct access; HTTPS is optional and is not a release requirement.

## Highlights in v0.2.2p Preview

- A dedicated Lab entrance in the main navigation and a restrained introduction portal on the Observatory homepage.
- A Lab-specific layout and navigation system that remains visually and operationally isolated from the archive site.
- **Archive Atlas (VS–001)** maps seven public Archive Objects by publication time, field, type, lifecycle state, reading length, and explicit `related` links. Search and filtering run in a Web Worker with an equivalent keyboard-accessible result list.
- **Server World (VS–002 preview)** introduces a navigable 3D world, formal GLB assets, a restrained material and lighting system, reversible proximity reactions, and nine occlusion-aware click nodes.
- Server World defaults to WebGL, keeps WebGPU opt-in during stabilization, respects reduced-motion preferences, and includes loading and renderer-failure states.
- The former **Temporal Field** renderer has been retired as a public project and retained only as an internal visual capability prototype.
- **NAS Constellation**, an interactive visualization backed by periodically collected NAS data.
- The NAS collector can read the latest terminal result from the vendor Backup Service through a read-only, aggregate-only query without exposing task names, paths, targets, credentials, or logs.
- A versioned NAS JSON schema, validation layer, fixtures, data-state simulations, collectors, and a read-only Data Gateway.
- Hourly NAS collection with short-term 24-hour and 7-day aggregated history.
- Separate deployment paths for the static site, collectors, and Data Gateway.
- Windows local QA hosting with login-time startup and a same-origin proxy to the NAS data service.
- A three-step Lab engineering documentation set covering architecture, section design, and content implementation.

## Site Structure

| Path | Purpose |
| --- | --- |
| `/` | Observatory entrance and high-level Lab introduction |
| `/archive/` | Full Archive Object index |
| `/archive/[slug]/` | Long-form Archive Object page |
| `/projects/` | Project-oriented archive view |
| `/essays/` | Essay and journal archive view |
| `/about/` | Site intent and boundaries |
| `/lab/` | Lab entrance and project directory |
| `/lab/visual-systems/` | Visual Systems index and Archive Atlas entry |
| `/lab/visual-systems/archive-atlas/` | VS–001 interactive map generated from seven public Archive Objects |
| `/lab/visual-systems/vs002/` | VS–002 Server World preview |
| `/lab/nas-observatory/` | NAS-based observational projects |
| `/lab/nas-observatory/constellation/` | Live periodic NAS Constellation |
| `/rss.xml` | Archive Object RSS feed |
| `/sitemap-index.xml` | Generated sitemap index |

## Architecture

The project is split into three operational layers:

1. **Static Observatory and Lab pages** — built by Astro into `dist/`.
2. **Data Gateway** — a small read-only Python HTTP service bound to localhost on the NAS.
3. **Collectors** — scheduled Python jobs that generate public, aggregated JSON snapshots.

The browser only requests same-origin endpoints under `/api/lab/v1/`. Nginx forwards those requests to the local Data Gateway. Collectors never expose arbitrary filesystem access, private service names, credentials, control operations, or write endpoints.

```text
Browser
  ├── Static pages and assets ──> Nginx ──> dist/
  └── /api/lab/v1/* ───────────> Nginx ──> Data Gateway
                                               └── generated public JSON
                                                        ↑
                                                  hourly collectors
```

## Requirements

- Node.js 20 or later
- npm
- Python 3.11 or later for NAS collection and the Data Gateway
- Nginx and systemd for the documented NAS deployment

## Local Development

```bash
npm install
npm run dev
```

Astro serves the development site on its normal local port. The NAS project can be developed without a real NAS by using the committed fixtures.

### Data modes

NAS Constellation supports two build-time modes:

- `fixture` — default mode; uses sanitized repository fixtures.
- `gateway` — requests `/api/lab/v1/nas/snapshot` and the versioned history endpoints.

Build the gateway-enabled version in PowerShell:

```powershell
$env:PUBLIC_LAB_DATA_MODE = "gateway"
npm.cmd run build
```

The following query parameter is available for deterministic QA:

```text
?state=fresh|stale|partial|empty|unavailable|incompatible|offline
```

## Production Build and Local QA

```powershell
npm.cmd ci
$env:PUBLIC_LAB_DATA_MODE = "gateway"
npm.cmd run build
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\start-local.ps1
```

The local QA server serves `dist/` at `http://127.0.0.1:4321/` and proxies `/api/lab/v1/` to the configured NAS origin. Override the default origin when required:

```powershell
$env:NAS_LAB_ORIGIN = "http://your-nas-host:8818"
```

On the maintained Windows workstation, the scheduled task `Ayue Observatory Local` starts this server when the user signs in.

## NAS Deployment

The reference deployment uses:

- Project root: `/vol2/projects/ayue-observatory`
- Static site port: `8818`
- Data Gateway: `127.0.0.1:18101`
- Collector schedule: once per hour
- Gateway service: `ayue-lab-gateway.service`

Important files:

| File | Responsibility |
| --- | --- |
| `lab-data/collector.py` | Collects public system metrics and writes atomic JSON snapshots |
| `lab-data/gateway.py` | Serves the versioned, read-only JSON contract |
| `lab-data/services.json` | Curated public aliases and service probes |
| `lab-data/ayue-lab-gateway.service` | systemd service definition |
| `lab-data/nginx-lab-api.conf` | Nginx proxy example |
| `lab-data/deploy-nas.sh` | Repeatable NAS installation and update procedure |

Before deploying, review `services.json`. Public labels must remain curated aliases; do not place secrets, private hostnames, tokens, or sensitive filesystem paths in the public dataset.

## Data Contract and Privacy

The public API uses schema major version `1` and provides:

- `/api/lab/v1/manifest`
- `/api/lab/v1/nas/snapshot`
- `/api/lab/v1/nas/history?range=24h`
- `/api/lab/v1/nas/history?range=7d`

The first release exposes aggregate CPU, memory, temperature, storage, uptime, backup result, and curated service availability fields. It intentionally excludes file listings, user activity, precise private network structure, credentials, administration controls, and all server-side write operations.

## Archive Object Model

Archive content lives in `src/content/archive/` as MDX. Core fields include:

```yaml
title: "Object title"
type: "essay"
status: "active"
summary: "A concise observation."
date: "2026-07-13"
tags:
  - "writing"
field: "essays"
```

Supported types are `essay`, `research`, `system`, `signal`, `project`, `failure`, `experiment`, `journal`, and `unknown`. Supported lifecycle states are `draft`, `active`, `ongoing`, `stable`, `archived`, and `future`.

## Engineering Documentation

- `CURRENT_STATE.md` — shipped capabilities and current boundaries.
- `CHANGELOG.md` — version history.
- `LAB_MASTER_PLAN.md` — the three-step Lab documentation framework.
- `SITE_ARCHITECTURE_V2.md` — global static/dynamic architecture.
- `LAB_SECTIONS.md` — Lab section themes and boundaries.
- `LAB_CONTENT_ENGINEERING.md` — project specifications, schemas, states, and acceptance criteria.
- `CONTENT_MODEL.md` — Archive Object schema.
- `DESIGN_LANGUAGE.md` and `COMPONENT_BIBLE.md` — main-site visual and component rules.

## Verification

Every completed implementation stage should run, at minimum:

```bash
npm run build
```

Changes involving NAS data should also verify schema-valid snapshot and history responses, Nginx configuration, Gateway service health, and the rendered `fresh`, failure, and compatibility states.

## License

This project is released under the [MIT License](LICENSE).
