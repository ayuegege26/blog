# Ayue Observatory v0.2.1 Plan

## 版本主题

`v0.2.1 — Lab Reliability & Operations`

本阶段不扩展为 Dashboard，也不增加 NAS 控制能力。目标是让 NAS Constellation、Collectors 和 Data Gateway 经过真实时间、真实数据与真实设备验收；Temporal Field 已撤出正式项目，只保留其运行时能力供未来有内容价值的页面使用。

## 已确认基础

- `v0.2.0` 已合并到 `main`，并建立 Git Tag 与 GitHub Release。
- 正式 Blog 域名为 `blog.ayuegege26.xyz`。
- NAS Collector 每小时运行一次。
- Data Gateway 保持匿名、同源、只读，并且只监听 NAS localhost。
- 24 小时和 7 天连续性属于时间型验收，不能用短时样本代替。

## Work Package A：历史数据连续性

### 目标

验证 Collector 和聚合历史可以跨越真实的 24 小时与 7 天窗口稳定运行。

### 工作内容

- 检查每小时采集是否连续，记录缺口、重复点和异常时间戳。
- 验证 24 小时历史的排序、点数上限、stale 判断和存储变化量。
- 验证 7 天降采样的分辨率、点数上限和文件大小。
- 在采集服务重启、Gateway 重启和 Nginx reload 后确认历史不丢失。
- 形成可重复执行的历史数据验证命令。

### 时间门槛

- 24 小时验收必须等待至少 24 个真实采集周期。
- 7 天验收必须等待至少 7 天真实运行时间。

### 验收标准

- 没有无法解释的时间缺口或重复点。
- 历史时间戳严格递增，所有比例值符合 schema。
- 24 小时和 7 天接口持续返回 HTTP 200 JSON。
- 历史文件增长受控，不因长期运行无限膨胀。

## Work Package B：可信备份状态

### 目标

让 `backup.lastCompletedAt` 和 `backup.lastResult` 来自 NAS 上已经存在、可以验证的备份系统，而不是猜测进程或扫描私人文件内容。

### 工作内容

- 只读调查 NAS 上实际备份任务、日志或状态文件。
- 选择单一、稳定、权限最小的状态来源。
- 将来源映射为 `success | partial | failed | unknown`。
- 只公开完成时间和聚合结果，不公开文件名、目标地址、账号或路径细节。
- 来源缺失、过期或格式变化时安全回退为 `unknown`。

### 验收标准

- 状态来源和映射规则写入工程文件。
- Collector 无需管理员权限即可读取必要状态。
- 公开响应不包含备份目标、私人路径或凭证。
- fixtures 与真实接口使用同一 schema。

### 已确定的接入规范

- 唯一可信来源为 NAS 官方 Backup Service 的只读操作记录；Collector 不扫描备份目录，也不读取任务、存储配置或日志内容。
- 只查询最近一笔终态操作的 `finished_time`、`status`、`completed_count` 与 `actual_count`。
- 官方状态 `Successful (3)` 映射为 `success`；`Error (4)` 且存在已处理项目时映射为 `partial`，否则映射为 `failed`。
- 没有终态操作、数据库不可读、时间戳无效或格式变化时统一返回 `{ lastCompletedAt: null, lastResult: "unknown" }`。
- 当前 NAS 的官方服务正在运行，但尚无备份操作记录，因此 `unknown` 是预期且真实的公开状态。

## Work Package C：真实数据视觉 QA

### 目标

使用真实 NAS 数据，而不是仅用 fixtures，验证 NAS Constellation 在桌面端与移动端都可理解、可操作。

### 工作内容

- 验证正式域名、NAS 部署与 Windows QA 三个入口。
- 验证当前、24 小时与 7 天切换。
- 验证 fresh、stale、partial、empty、unavailable、incompatible、offline。
- 检查节点标签、指标单位、更新时间、空状态和错误说明。
- 检查键盘操作、触控、窄屏布局与文本溢出。

### 验收标准

- 桌面端和移动端没有阻断性布局或交互问题。
- 状态变化不需要打开开发者工具才能理解。
- 真实数据不会造成节点重叠、不可读数字或布局跳动。
- Lab 故障不影响 Observatory 主站。

## Work Package D：视觉运行时能力与退役处理

### 目标

确保已经验证的高成本动态能力可以安全复用，同时撤销 Temporal Field 的公开项目身份，避免视觉原型被误当作正式内容。

### 工作内容

- 保留暂停、Canvas、`prefers-reduced-motion`、后台降载和资源释放能力。
- 从公开路由、Lab 入口和 manifest 移除 Temporal Field。
- 将渲染组件标记为视觉原型，不再占用 VS–001。
- 只有当动态视觉服务真实内容或交互反馈时才允许复用。
- 以 `VS001_ARCHIVE_ATLAS.md` 作为首个正式 Visual Systems 项目设计基线。

### 验收标准

- Temporal Field 不再存在公开入口、路由或 manifest 项目。
- 原型能力保留在源代码中且不会被 Observatory 或公开 Lab 页面加载。
- VS–001 已接入真实 Archive Objects 并进入正式可用状态；后续新增节点必须先完成公开 MDX 和内容核查。

## Work Package E：正式域名与便捷访问

### 目标

让 `http://blog.ayuegege26.xyz` 成为 canonical、sitemap、RSS 与公开访问的统一来源，同时保持个人站部署简单、访问直接。

### 当前发现

- DNS 已解析到公开服务器。
- HTTP 可以返回 Observatory 页面。
- HTTP 已能直接返回 Observatory 页面，可作为本站正式入口。

### 工作内容

- 正式构建使用 `SITE_URL=http://blog.ayuegege26.xyz`。
- 验证 canonical、Open Graph、RSS 与 sitemap 不再出现本地占位域名。
- 明确公网静态站点与 NAS Data Gateway 的安全连接方式，不暴露 NAS 管理面。
- HTTPS 仅作为未来可选改善，不要求强制跳转，也不阻塞版本发布。

### 验收标准

- 浏览器和命令行可以直接通过正式 HTTP 域名访问。
- 所有公开绝对 URL 使用正式域名。
- 公网 Lab 数据接口仍保持匿名只读和最小暴露。

## 统一验证命令

本阶段应建立一个统一命令，至少执行：

- 内容与 schema 验证。
- Node 和 Python 语法检查。
- 敏感信息扫描。
- Gateway 模式 production build。
- 核心路由、RSS、sitemap 和 Lab API HTTP 验证。

每个阶段性工作完成后仍必须独立执行 `npm run build`，不能只依赖最终发布前检查。

## 完成定义

`v0.2.1` 只有在以下条件全部满足时完成：

- 24 小时与 7 天真实历史验收完成。
- 可信备份状态完成接入并通过隐私检查。
- 真实数据桌面端与移动端 QA 完成。
- Temporal Field 已完成退役处理，视觉运行时能力保留但不再作为项目发布。
- 正式 HTTP 域名和 canonical 配置正确。
- Gateway 模式 production build 成功。
- 工程文件与实际部署一致。

## 2026-07-13 执行记录

- Work Package B 已完成：Collector 以服务账户只读接入官方 Backup Service；当前没有备份操作记录，所以公开结果为 `unknown`。
- Work Package C 已完成：真实 NAS 数据的桌面端与 375px 移动端均无水平溢出；当前、24 小时、7 天、五个公开节点和键盘选择通过验证。
- Work Package D 已完成：运行时能力验证通过，Temporal Field 撤下公开入口并转为视觉原型，VS–001 Archive Atlas 已完成结构原型、内容核查与七个真实对象接入。
- Work Package A 仍在计时：真实小时点尚不足 24 小时，更不能替代 7 天连续性验收。
- Work Package E 已按个人站标准确认：正式 HTTP 域名可用，HTTPS 不作为发布门槛。

## 暂不进入范围

- 第三个正式 Lab 项目。
- NAS 写操作或远程管理。
- 登录、账号和私人项目。
- 任意查询时间范围或秒级公网监控。
- Lab 搜索、CMS 或项目管理后台。
- 没有明确关系证据的服务依赖连线。
