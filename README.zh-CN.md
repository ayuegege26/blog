<div align="center">

# Ayue Observatory / 阿月觀測站

**一個長期運行、用於檔案、實驗、系統與信號的個人觀測站。**

[English](README.md) · [简体中文](README.zh-CN.md) · [v0.2.0 發布說明](RELEASE_NOTES_v0.2.0.md)

</div>

## 專案概述

Ayue Observatory 是一個使用 Astro 建立的個人發布與實驗站點。它刻意不採用普通博客、作品集、SaaS Dashboard 或 NAS 管理面板的形態。

主站以 **Archive Object（檔案對象）** 作為長期內容單位：每個對象都有編號、類型、日期與生命週期，可以被索引、修改並在未來建立關聯。獨立的 **Lab** 則承載技術密度更高的瀏覽器實驗，以及由基礎設施定期採集、只讀公開的觀測資料。

`v0.2.0` 建立了第一個完整 Lab 基礎，同時保持主站克制、安靜的觀測站審美。

## v0.2.0 主要內容

- 主導航加入低權重 Lab 入口，Observatory 首頁正文加入克制的 Lab 介紹區域。
- 建立與主站視覺、運行邊界相對隔離的 Lab Layout 與導航系統。
- 完成 **Temporal Field／時間景觀**：以 WebGL 為主、Canvas 為降級能力的瀏覽器生成視覺實驗。
- 完成 **NAS Constellation／NAS 星圖**：使用定期採集的真實 NAS 資料形成互動觀測視圖。
- 建立版本化 NAS JSON schema、前端驗證、脫敏 fixtures、資料狀態模擬、Collectors 與只讀 Data Gateway。
- 每小時採集一次 NAS 資料，保存 24 小時與 7 天降採樣歷史。
- 靜態站點、採集器與 Data Gateway 可分離部署。
- Windows 本機 QA 支援登入自啟，並以同源代理讀取 NAS Gateway。
- 建立 Lab 三步工程文件：全局架構、次級板塊主題、具體內容工程。

## 頁面結構

| 路徑 | 用途 |
| --- | --- |
| `/` | Observatory 入口與 Lab 概念介紹 |
| `/archive/` | 完整 Archive Object 索引 |
| `/archive/[slug]/` | 檔案對象詳情與長文頁 |
| `/projects/` | 專案類檔案視圖 |
| `/essays/` | 隨筆與日誌視圖 |
| `/about/` | 站點目標與邊界 |
| `/lab/` | Lab 入口與項目目錄 |
| `/lab/visual-systems/` | 生成視覺與高級前端系統 |
| `/lab/visual-systems/temporal-field/` | Temporal Field 實驗 |
| `/lab/nas-observatory/` | 基於 NAS 的觀測項目 |
| `/lab/nas-observatory/constellation/` | NAS Constellation 真實週期資料頁 |
| `/rss.xml` | Archive Object RSS |
| `/sitemap-index.xml` | 自動生成的 sitemap |

## 工程架構

專案分為三個運行層：

1. **靜態 Observatory 與 Lab 頁面**：由 Astro 構建到 `dist/`。
2. **Data Gateway**：運行在 NAS localhost 的輕量只讀 Python HTTP 服務。
3. **Collectors**：定期生成脫敏、聚合 JSON 快照的 Python 採集任務。

瀏覽器只讀取同源的 `/api/lab/v1/`。Nginx 將請求轉發給 Data Gateway。Collectors 不公開任意文件系統讀取、私人服務名稱、憑證、控制操作或寫入接口。

```text
瀏覽器
  ├── 靜態頁面與資源 ──> Nginx ──> dist/
  └── /api/lab/v1/* ───> Nginx ──> Data Gateway
                                           └── 公開聚合 JSON
                                                    ↑
                                               每小時採集器
```

## 環境需求

- Node.js 20 或更新版本
- npm
- Python 3.11 或更新版本（NAS 採集器與 Gateway）
- Nginx 與 systemd（文件中的 NAS 部署方式）

## 本機開發

```bash
npm install
npm run dev
```

即使沒有真實 NAS，也可以使用倉庫中的脫敏 fixtures 開發 NAS Constellation。

### 資料模式

- `fixture`：預設模式，使用倉庫內脫敏測試資料。
- `gateway`：請求 `/api/lab/v1/nas/snapshot` 和版本化歷史接口。

PowerShell 中構建 Gateway 模式：

```powershell
$env:PUBLIC_LAB_DATA_MODE = "gateway"
npm.cmd run build
```

資料狀態 QA 可以使用：

```text
?state=fresh|stale|partial|empty|unavailable|incompatible|offline
```

## Production 構建與本機 QA

```powershell
npm.cmd ci
$env:PUBLIC_LAB_DATA_MODE = "gateway"
npm.cmd run build
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\start-local.ps1
```

本機 QA 服務在 `http://127.0.0.1:4321/` 提供 `dist/`，並將 `/api/lab/v1/` 代理到指定 NAS。必要時可以覆蓋 NAS 地址：

```powershell
$env:NAS_LAB_ORIGIN = "http://your-nas-host:8818"
```

維護用 Windows 主機已配置 `Ayue Observatory Local` 計劃任務，在使用者登入後自動啟動。

## NAS 部署

目前參考部署如下：

- 專案根目錄：`/vol2/projects/ayue-observatory`
- 靜態站點端口：`8818`
- Data Gateway：`127.0.0.1:18101`
- 採集週期：每小時一次
- Gateway 服務：`ayue-lab-gateway.service`

| 文件 | 職責 |
| --- | --- |
| `lab-data/collector.py` | 採集公開系統指標並原子寫入 JSON |
| `lab-data/gateway.py` | 提供版本化、只讀 JSON 契約 |
| `lab-data/services.json` | 人工確認的公開別名與服務探測 |
| `lab-data/ayue-lab-gateway.service` | systemd 服務定義 |
| `lab-data/nginx-lab-api.conf` | Nginx 反向代理範例 |
| `lab-data/deploy-nas.sh` | 可重複執行的 NAS 部署腳本 |

部署前必須檢查 `services.json`。公開標籤應使用人工整理的別名，不得放入密碼、Token、私人主機名或敏感文件路徑。

## 資料契約與隱私

公開 API 使用 schema major version `1`：

- `/api/lab/v1/manifest`
- `/api/lab/v1/nas/snapshot`
- `/api/lab/v1/nas/history?range=24h`
- `/api/lab/v1/nas/history?range=7d`

首版公開 CPU、記憶體、溫度、儲存空間、uptime、備份結果，以及人工整理服務的聚合可用狀態。它不公開文件列表、使用者活動、精確私人網路結構、憑證、管理控制，也沒有任何服務端寫操作。

## Archive Object 內容模型

Archive 內容位於 `src/content/archive/`，使用 MDX 與 frontmatter：

```yaml
title: "對象標題"
type: "essay"
status: "active"
summary: "簡短觀測摘要。"
date: "2026-07-13"
tags:
  - "writing"
field: "essays"
```

類型包括 `essay`、`research`、`system`、`signal`、`project`、`failure`、`experiment`、`journal`、`unknown`。生命週期包括 `draft`、`active`、`ongoing`、`stable`、`archived`、`future`。

## 工程文件

- `CURRENT_STATE.md`：當前已交付能力與邊界。
- `CHANGELOG.md`：版本變更記錄。
- `LAB_MASTER_PLAN.md`：Lab 三步文件框架。
- `SITE_ARCHITECTURE_V2.md`：靜態主站與動態 Lab 全局架構。
- `LAB_SECTIONS.md`：Lab 次級板塊主題與邊界。
- `LAB_CONTENT_ENGINEERING.md`：項目規格、資料 schema、狀態與驗收標準。
- `CONTENT_MODEL.md`：Archive Object schema。
- `DESIGN_LANGUAGE.md`、`COMPONENT_BIBLE.md`：主站設計與元件規範。

## 驗證要求

每個階段性工程完成後至少執行：

```bash
npm run build
```

涉及 NAS 資料時，還需要驗證 snapshot 與 history 符合 schema、Nginx 配置、Gateway 服務狀態，以及頁面的 fresh、故障和不兼容狀態。

## License

本專案使用 [MIT License](LICENSE)。
