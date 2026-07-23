# Ayue Observatory Current State

## 当前版本

当前预览版本为 `v0.2.2p — Visual Systems Preview`；`package.json` 使用标准预发布版本 `0.2.2-preview.0`。

`v0.2.2p` 在已经稳定的 Archive Object 主站和动态 Lab 框架上，发布 VS–001 Archive Atlas，并开放 VS–002 Server World 的阶段性预览。后续内容评审确认 Temporal Field 只具备视觉原型价值，不足以作为独立博客内容，现已撤下公开入口；NAS Constellation 继续作为真实周期数据项目运行。

## 已完成能力

### Observatory 主站

- Astro 静态站点与 MDX Archive Object 内容系统。
- Observatory、Archive、Projects、Essays、About、对象详情、RSS、sitemap 与 404 页面。
- Archive Object 编号、类型、状态、日期、领域、标签、精选顺序和可选关联对象。
- Canonical、Open Graph、RSS 与 sitemap 基础 SEO。
- 响应式布局、键盘 focus 与基础无障碍语义。

### Lab 平台

- Lab 主导航入口、主站正文介绍入口、独立 Layout 和板块导航。
- Visual Systems：Temporal Field 渲染器转为未公开视觉能力原型；`VS–001 Archive Atlas` 已接入七个真实公开 Archive Objects，按发布日期、领域、类型、状态、阅读长度和显式关联生成地图。
- `VS–002 Server World` 预览：正式 GLB 资产、材质与光照、自由飞行、可逆 proximity 状态、九个遮挡感知点击节点和 reduced-motion 路径；节点正式内容与 Gate 5 仍待完成。
- NAS Observatory／NAS Constellation：当前、24 小时、7 天视图和八种数据状态。
- NAS schema `1.0`、前端运行时验证、脱敏 fixtures 与 QA 状态模拟。
- Python Collectors、只读 Data Gateway、Nginx 同源代理和每小时采集。
- Windows 本地 QA 服务、NAS API 代理与登录自启动。
- NAS systemd 开机自启和可重复执行部署脚本。

## 当前部署

- Windows QA：`127.0.0.1:4321`。
- NAS 项目目录：`/vol2/projects/ayue-observatory`。
- NAS 静态站点：端口 `8818`。
- Data Gateway：仅监听 `127.0.0.1:18101`。
- NAS Collector：每小时执行一次。

## 当前边界

- 所有公开 Lab 项目保持匿名、只读。
- 不提供 NAS 控制、服务端写操作、账号系统或私人项目入口。
- NAS 仅公开聚合指标和人工确认的服务别名。
- 24 小时和 7 天历史需要随部署时间逐步积累。
- 备份状态来自官方 Backup Service 的只读操作记录；当前尚无备份操作，所以真实结果为 `unknown`。
- Blog 正式入口为 `http://blog.ayuegege26.xyz`；个人站以直接访问为优先，HTTPS 不作为发布门槛。
- 服务依赖连线仍为可选能力；没有明确、可验证关系时不显示。

## 验证基线

- 每个阶段性工程完成后必须执行 `npm run build`。
- NAS 数据改动必须验证 snapshot、24 小时和 7 天 history 均返回 schema 有效的 JSON。
- 部署改动必须验证 Nginx 配置、Gateway 服务状态、监听地址和定时采集任务。
- 前端必须保留 fresh、stale、partial、empty、unavailable、incompatible、offline 的可测试状态。

## 下一阶段

下一阶段优先完成 VS–002 S5 节点内容、浏览器会话韧性与 Gate 5 发布候选验收；运行可靠性工作继续等待真实历史时间窗口。具体范围见 `NEXT_PHASE_PLAN.md` 与 `VS002_PRODUCTION_PLAN.md`。

备份接入只公开最近完成时间和聚合结果，不读取或公开任务名称、备份路径、存储目标、账号、凭证或日志内容。

2026-07-16 Archive Atlas 的内容核查和第二阶段真实资料接入已完成；OBS-X、draft 与 future 占位内容不会进入地图。OpenPaw 只作为事实核查和候选素材来源，正式公开资料仍以 MDX 与作者确认为准。NAS 运行验收仍需等待真实时间的 24 小时／7 天连续性。
