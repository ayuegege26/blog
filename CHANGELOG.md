# Changelog / 变更记录

This project records stable milestones with semantic versions. / 本项目使用语义化版本记录稳定成果。

## [Unreleased]

- Accumulate real NAS history and evaluate the next Lab project. / 累积真实 NAS 历史数据，并评估下一个 Lab 项目。

## [0.2.0] - 2026-07-13

### Added / 新增

- Added the Lab platform, independent layout, navigation, and homepage introduction portal. / 新增 Lab 平台、独立布局、导航与主站介绍入口。
- Added Temporal Field with WebGL rendering and Canvas fallback. / 新增带 WebGL 渲染和 Canvas 降级的 Temporal Field。
- Added NAS Constellation with current, 24-hour, and 7-day views. / 新增提供当前、24 小时和 7 天视图的 NAS Constellation。
- Added schema `1.0`, sanitized fixtures, runtime validation, and deterministic QA states. / 新增 schema `1.0`、脱敏 fixtures、运行时验证和确定性 QA 状态。
- Added NAS collectors, a localhost-only Data Gateway, Nginx proxying, systemd startup, and hourly collection. / 新增 NAS Collectors、本机 Data Gateway、Nginx 代理、systemd 自启动和每小时采集。
- Added Windows local QA hosting and NAS API proxying. / 新增 Windows 本地 QA 服务和 NAS API 代理。
- Added the three-step Lab architecture and content engineering documentation. / 新增 Lab 三步架构与内容工程文件。

### Fixed / 修复

- Corrected the NAS web service probe to port `8818`. / 修正 NAS Web 服务探测端口为 `8818`。
- Ensured the active Debian Nginx master reloads correctly when the NAS vendor Nginx shares PID management. / 处理 NAS 厂商 Nginx 共存时站点 Nginx 未正确重载的问题。
- Ensured local QA forwards versioned history endpoints instead of returning the static 404 page. / 确保本地 QA 正确转发版本化历史接口，而不是返回静态 404 页面。

### Verified / 已验证

- Astro production build generated 20 pages. / Astro production build 成功生成 20 个页面。
- Snapshot and 24-hour/7-day history endpoints returned HTTP 200 JSON. / Snapshot、24 小时和 7 天历史接口返回 HTTP 200 JSON。
- Data Gateway was enabled, active, and bound to localhost only. / Data Gateway 已启用、运行，并且仅监听 localhost。
- Main site and all first-release Lab routes returned HTTP 200. / 主站和首发 Lab 路由均返回 HTTP 200。

## [0.1.2] - 2026-07-10

### Added / 新增

- Completed the first Archive Object matrix from OBS-0001 to OBS-0008. / 完成 OBS-0001 至 OBS-0008 的首批 Archive Object 矩阵。
- Added the `unknown` type and `future` lifecycle state. / 加入 `unknown` 类型与 `future` 状态。
- Completed related-object presentation, RSS, sitemap, canonical, Open Graph, local production hosting, and Windows startup. / 完成相关对象、RSS、sitemap、canonical、Open Graph、本地 production 服务和 Windows 自启动。
