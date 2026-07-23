# Ayue Observatory v0.2.2p Preview

Release date: 2026-07-23

Git tag: `v0.2.2p`

Package version: `0.2.2-preview.0`

## Project introduction

Ayue Observatory is a long-running personal publishing and experimentation site built with Astro. Its quiet main site organizes durable writing as numbered Archive Objects; its separate Lab turns selected content, browser graphics, and sanitized infrastructure signals into focused interactive systems.

`v0.2.2p` is a preview rather than a stable release. It makes the current Visual Systems work available for review without claiming that VS–002 has passed its final production gate.

## What is new

### VS–001 Archive Atlas

- Generates an interactive map from seven real public MDX Archive Objects.
- Maps publication time, field, content type, lifecycle state, reading length, tags, and only explicitly authored `related` links.
- Excludes OBS-X, drafts, and future placeholders from the public map.
- Supports search and filtering in a Web Worker, URL-persisted state, zoom and pan, pointer selection, and an equivalent keyboard-accessible result list.

### VS–002 Server World preview

- Adds a formal low/mid-poly GLB world with a core tower, rings, vertical wells, bridges, and floating structures.
- Adds free-flight navigation, restrained blue-hour materials and lighting, fog, surface maps, and renderer fallback handling.
- Adds a shared reversible proximity registry and nine occlusion-aware click nodes.
- Adds pointer and keyboard interaction paths, `Esc`/outside-click reset, reduced-motion behavior, input cleanup, and a timed loading layer.
- Uses WebGL by default; WebGPU remains opt-in with `?renderer=webgpu` during stabilization.

### Archive and NAS integration

- Retires Temporal Field as a public Lab project while preserving its reusable renderer as an internal capability prototype.
- Updates NAS Constellation copy for real Gateway mode.
- Reads only the latest aggregate terminal Backup Service result through a read-only SQLite query; task names, paths, storage targets, credentials, and logs are not queried or published.
- Uses `http://blog.ayuegege26.xyz` as the default canonical site base.

## Preview limitations

- The nine VS–002 nodes still contain placeholder copy. Final mapping to NAS, tools, and Archive content is scheduled for S5.
- Gate 5 release-candidate acceptance is incomplete.
- Extended WebGPU, browser-session, device, and graphics-driver stability testing remains pending.
- The production build succeeds but reports a large client chunk warning caused mainly by the Three.js runtime.

## Verification baseline

- Gateway-mode Astro production build completes and generates 21 pages.
- Archive Atlas and Server World routes are present in the static output.
- Release deployment must additionally verify the NAS site, manifest, snapshot, 24-hour history, 7-day history, Gateway service, and invalid-route 404 behavior.

---

# Ayue Observatory v0.2.2p 預覽版

發布日期：2026-07-23

Git 標籤：`v0.2.2p`

Package 版本：`0.2.2-preview.0`

## 專案介紹

Ayue Observatory 是一個以 Astro 建立、長期運行的個人發布與實驗站。安靜的主站以編號 Archive Objects 組織可持續維護的內容；獨立 Lab 則把經過選擇的內容、瀏覽器圖形能力與脫敏基礎設施信號轉化為聚焦的互動系統。

`v0.2.2p` 是預覽版，而不是穩定版。它公開目前的 Visual Systems 成果供實際審閱，但不宣稱 VS–002 已通過最終發布門。

## 本次新增

### VS–001 Archive Atlas

- 從七個真實公開 MDX Archive Objects 生成互動地圖。
- 映射發布時間、領域、內容類型、生命週期、閱讀長度、標籤，以及作者明確寫入的 `related` 關係。
- 公開地圖排除 OBS-X、draft 和 future 占位內容。
- 支援 Web Worker 搜尋篩選、URL 狀態、縮放平移、指針選取和等價鍵盤結果列表。

### VS–002 Server World 預覽

- 加入包含核心塔、環體、垂直井、橋體和懸浮結構的正式低／中模 GLB 世界。
- 加入自由飛行、克制的藍調材質光照、霧、表面圖和 renderer 失敗處理。
- 加入共用、可逆的 proximity registry 與九個具遮擋判斷的點擊節點。
- 加入指針與鍵盤路徑、`Esc`／空白點擊重置、低動態偏好、輸入清理和定時載入層。
- 預設使用 WebGL；穩定期內 WebGPU 以 `?renderer=webgpu` 顯式啟用。

### Archive 與 NAS 整合

- 撤下 Temporal Field 的公開 Lab 項目身份，同時保留 renderer 作為內部可復用能力原型。
- 更新 NAS Constellation 在真實 Gateway 模式下的說明。
- 只以唯讀 SQLite 查詢最近一筆聚合終態 Backup Service 結果；不查詢或公開任務名稱、路徑、儲存目標、憑證和日誌。
- 預設 canonical 站點基址更新為 `http://blog.ayuegege26.xyz`。

## 預覽限制

- VS–002 九個節點仍是占位文案；與 NAS、工具和 Archive 的正式內容映射留待 S5。
- Gate 5 發布候選驗收尚未完成。
- WebGPU、瀏覽器會話、設備與顯卡驅動的長時間穩定性測試仍待完成。
- Production build 成功，但由 Three.js runtime 為主的客戶端 chunk 仍會觸發體積警告。

## 驗證基線

- Gateway 模式 Astro production build 成功並生成 21 個頁面。
- Archive Atlas 與 Server World 路由已進入靜態輸出。
- 正式部署還必須驗證 NAS 站點、manifest、snapshot、24 小時歷史、7 天歷史、Gateway 服務與非法路由 404。
