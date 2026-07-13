# Ayue Observatory v0.2.0 — Lab Foundation

[English](#english) · [中文](#中文)

## English

### Summary

Version `0.2.0` is the first release that treats Lab as a complete platform rather than an empty future section. It adds one advanced visual experiment and one real infrastructure observation project, together with the data, deployment, privacy, and failure-state foundations required to operate them safely.

### What changed

#### Lab platform

- Added Lab to the end of the main navigation with lower visual weight than the Archive.
- Added a homepage introduction portal that explains Lab without embedding individual experiments into the Observatory.
- Added a Lab-specific layout, header, section index, project metadata, and responsive styles.

#### Temporal Field

- Added a generative temporal landscape driven by local browser time.
- Added WebGL rendering, Canvas fallback, pause/resume, density control, and deterministic visual rules.
- Kept the experiment fully client-side; it does not require NAS or server data.

#### NAS Constellation

- Added a responsive, keyboard-accessible service constellation.
- Added current, 24-hour, and 7-day views.
- Added loading, fresh, stale, partial, empty, unavailable, incompatible, and offline states.
- Added deterministic query-driven state simulation for QA.

#### Data and deployment

- Added schema version `1.0`, runtime validation, sanitized fixtures, and a client data adapter.
- Added a dependency-free Python collector for aggregate NAS metrics and curated TCP probes.
- Added a localhost-only Python Data Gateway with caching, ETag, JSON errors, and fixed read-only routes.
- Added hourly collection, a systemd service, Nginx proxy configuration, a backup-aware deployment script, and a Windows local QA proxy.
- Accounted for the NAS environment running separate Debian and vendor Nginx masters.

### Security and privacy boundaries

- Public projects remain anonymous and read-only.
- No arbitrary filesystem, command execution, account, or administration endpoint is exposed.
- Public service labels are curated aliases.
- Historical data is aggregated and downsampled.
- The Gateway binds to localhost and is exposed only through the site reverse proxy.

### Known limitations

- Historical graphs need time to accumulate after first deployment.
- Backup status remains `unknown` until a verified backup source is integrated.
- Twenty-four-hour service availability is initially `null` until enough samples exist.
- A public production hostname and HTTPS ingress for the blog are outside this release.

### Verification

- Astro production build: 20 pages generated successfully.
- Snapshot and 24-hour/7-day history endpoints: HTTP 200 JSON.
- Nginx configuration: valid and reloaded on the correct site master.
- Data Gateway: enabled and active.
- Gateway listener: localhost only.
- Main site, Lab, Temporal Field, and NAS Constellation routes: HTTP 200.

---

## 中文

### 版本摘要

`v0.2.0` 是第一個將 Lab 視為完整平台、而不是未來空板塊的版本。它交付了一個高級生成視覺實驗和一個真實基礎設施觀測項目，也建立了安全運行所需的資料契約、部署拓撲、隱私邊界與故障狀態。

### 主要變更

#### Lab 平台

- Lab 進入主導航末位，視覺權重低於 Archive。
- Observatory 首頁正文新增 Lab 介紹入口，但不直接呈現具體實驗內容。
- 新增 Lab 專用 Layout、Header、板塊入口、項目資訊與響應式樣式。

#### Temporal Field／時間景觀

- 新增基於瀏覽器本機時間生成的時間景觀。
- 提供 WebGL 渲染、Canvas 降級、暫停／恢復、密度控制和確定性視覺規則。
- 完全在客戶端運行，不依賴 NAS 或服務端資料。

#### NAS Constellation／NAS 星圖

- 新增響應式、支援鍵盤操作的服務星圖。
- 提供當前、24 小時與 7 天視圖。
- 支援 loading、fresh、stale、partial、empty、unavailable、incompatible、offline 狀態。
- 支援 query 參數驅動的確定性 QA 模擬。

#### 資料與部署

- 新增 `1.0` schema、運行時驗證、脫敏 fixtures 與前端資料適配器。
- 新增無第三方依賴的 Python NAS 聚合指標與服務探測採集器。
- 新增只監聽 localhost 的 Python Data Gateway，提供快取、ETag、JSON 錯誤與固定只讀路由。
- 新增每小時採集、systemd 服務、Nginx 代理、帶備份的部署腳本與 Windows 本機 QA 代理。
- 對 NAS 同時運行 Debian Nginx 和廠商 Nginx master 的環境作了兼容。

### 安全與隱私邊界

- 公開項目保持匿名只讀。
- 不公開任意文件系統、命令執行、帳號或管理接口。
- 公開服務名稱使用人工整理別名。
- 歷史資料以聚合、降採樣方式保存。
- Gateway 只監聽 localhost，僅由站點反向代理對外提供。

### 已知限制

- 歷史圖需要在首次部署後隨每小時採集逐步累積。
- 在接入已驗證的備份來源前，備份狀態保持 `unknown`。
- 收集足夠樣本前，24 小時服務可用率初始為 `null`。
- Blog 正式公開域名與 HTTPS 入口不在本版本範圍內。

### 驗證結果

- Astro production build：成功生成 20 個頁面。
- Snapshot、24 小時與 7 天歷史接口：HTTP 200 JSON。
- Nginx 配置：語法有效，並已重載正確的站點 master。
- Data Gateway：已啟用且運行中。
- Gateway 監聽：僅 localhost。
- 主站、Lab、Temporal Field、NAS Constellation：HTTP 200。
