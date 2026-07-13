# Ayue Observatory Current State

## 当前版本

当前发布版本为 `v0.2.0 — Lab Foundation`。

`v0.2.0` 在已经稳定的 Archive Object 主站之外，完成第一阶段动态 Lab：Temporal Field 证明浏览器高级生成视觉能力，NAS Constellation 证明周期真实数据、只读 Gateway 与动态前端可以在明确的隐私边界内共同运行。

## 已完成能力

### Observatory 主站

- Astro 静态站点与 MDX Archive Object 内容系统。
- Observatory、Archive、Projects、Essays、About、对象详情、RSS、sitemap 与 404 页面。
- Archive Object 编号、类型、状态、日期、领域、标签、精选顺序和可选关联对象。
- Canonical、Open Graph、RSS 与 sitemap 基础 SEO。
- 响应式布局、键盘 focus 与基础无障碍语义。

### Lab 平台

- Lab 主导航入口、主站正文介绍入口、独立 Layout 和板块导航。
- Visual Systems／Temporal Field：WebGL 生成视觉、Canvas 降级、暂停和密度控制。
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
- 备份状态在接入可信备份来源前保持 `unknown`。
- Blog 公网正式域名和 HTTPS 入口不属于 v0.2.0。
- 服务依赖连线仍为可选能力；没有明确、可验证关系时不显示。

## 验证基线

- 每个阶段性工程完成后必须执行 `npm run build`。
- NAS 数据改动必须验证 snapshot、24 小时和 7 天 history 均返回 schema 有效的 JSON。
- 部署改动必须验证 Nginx 配置、Gateway 服务状态、监听地址和定时采集任务。
- 前端必须保留 fresh、stale、partial、empty、unavailable、incompatible、offline 的可测试状态。

## 下一阶段

下一阶段不默认继续增加 Lab 项目。优先事项是积累并验证历史数据、接入可信备份状态、完成真实数据桌面与移动视觉 QA、完善公网 HTTPS 部署方案，并维护 v0.2.0 工程文件的一致性。
