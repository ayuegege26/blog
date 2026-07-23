# Changelog / 变更记录

This project records stable milestones with semantic versions. / 本项目使用语义化版本记录稳定成果。

## [Unreleased]

- Complete Server World S5 content, browser stability checks, and Gate 5 acceptance. / 完成 Server World S5 内容、浏览器稳定性检查与 Gate 5 验收。

## [0.2.2p] - 2026-07-23

Preview tag: `v0.2.2p`; package version: `0.2.2-preview.0`. / 预览标签：`v0.2.2p`；包版本：`0.2.2-preview.0`。

### Added / 新增

- Added VS–001 Archive Atlas, generated from seven public MDX Archive Objects with time, field, type, status, reading-length, and explicit-relation views. / 新增 VS–001 Archive Atlas，基于七个公开 MDX Archive Objects 生成时间、领域、类型、状态、阅读长度与显式关系视图。
- Added Web Worker filtering, URL-persisted view state, pointer exploration, and an equivalent accessible result list for Archive Atlas. / 为 Archive Atlas 新增 Web Worker 筛选、URL 视图状态、指针探索与等价无障碍结果列表。
- Added the VS–002 Server World preview with formal GLB assets, free-flight navigation, material and lighting passes, proximity reactions, and nine click nodes. / 新增 VS–002 Server World 预览，包含正式 GLB 资产、自由飞行、材质光照、靠近反应与九个点击节点。
- Added reduced-motion handling, input cleanup, occlusion-aware node interaction, a timed entry layer, and opt-in WebGPU support for VS–002. / 为 VS–002 新增低动态偏好、输入清理、遮挡感知节点、定时进入层和显式启用的 WebGPU 支持。
- Added read-only aggregate Backup Service status collection for NAS Constellation. / 为 NAS Constellation 新增只读聚合 Backup Service 状态采集。

### Changed / 变更

- Retired Temporal Field as a public project while keeping its renderer as an internal capability prototype. / 撤下 Temporal Field 的公开项目身份，同时保留其 renderer 作为内部能力原型。
- Set the public canonical base to `http://blog.ayuegege26.xyz`. / 将公开 canonical 基址设为 `http://blog.ayuegege26.xyz`。
- Updated Lab navigation, project manifests, engineering documents, and NAS deployment behavior for the preview. / 更新 Lab 导航、项目 manifest、工程文档与 NAS 部署行为。

### Preview limitations / 预览限制

- VS–002 nodes still use placeholder copy; final topic mapping and content belong to S5. / VS–002 节点仍使用占位文案；最终主题映射和内容属于 S5。
- Gate 5 release-candidate acceptance and extended WebGPU stability testing are not complete. / Gate 5 发布候选验收与 WebGPU 长时间稳定性测试尚未完成。
- The production bundle still reports a large Three.js client chunk warning. / Production 构建仍会报告 Three.js 客户端 chunk 偏大的警告。

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
