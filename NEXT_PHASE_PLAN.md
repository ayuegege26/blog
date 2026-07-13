# Ayue Observatory v0.1.3 Plan

## 版本主题

`v0.1.3 — Archive Maintenance`

本阶段不增加新页面，不扩展为 dashboard，也不引入搜索、复杂筛选、关系图谱或 CMS。目标是把已经完成的首版变成能够长期维护、稳定验证和安全发布的内容工程。

## Work Package A：Archive Object 模板

### 目标

建立新增对象时可直接复制的标准模板，降低 frontmatter 和正文结构漂移。

### 工作内容

- 提供标准 MDX 模板。
- 区分必填字段、可选字段和保留字段。
- 说明 `objectId`、slug、日期、状态、排序和 `related` 的写法。
- 明确 `unknown/future` 的适用边界。

### 验收标准

- 新对象可从单一模板开始创建。
- 模板内容能通过现有 Astro schema 和 production build。

## Work Package B：内容验证

### 目标

在 build 之前发现常见内容错误。

### 工作内容

- 检查重复 `objectId`。
- 检查重复或不规范 slug。
- 检查无效日期、空标签和不允许的枚举。
- 检查 `related` 是否指向存在的非草稿对象。
- 提供一个明确的内容验证命令。

### 验收标准

- 有错误时命令返回非零退出码，并指出文件与原因。
- 正常内容验证通过后，production build 继续成功。

## Work Package C：状态与展示规则

### 目标

让内容生命周期规则可预测，避免新增对象后各页面表现不一致。

### 工作内容

- 明确 `draft` 对象不进入公开页面、RSS 和 sitemap。
- 明确 `future` 对象的展示方式。
- 保持 `featured`、`priority`、`updated/date` 的排序规则一致。
- 保持 OBS-X 的隐藏彩蛋性质，不为它增加普通导航或公开说明。

### 验收标准

- 首页、Archive、栏目页和 RSS 使用一致的公开对象集合。
- 状态与排序规则有自动验证或可重复测试。

## Work Package D：发布流程

### 目标

形成稳定、可重复的小版本发布方式。

### 工作内容

- 建立统一的验证加 build 命令。
- 记录版本号更新位置。
- 定义发布前检查清单。
- 使用 `CHANGELOG.md` 记录稳定版本成果。
- 保持本地 production 服务从项目目录的 `dist/` 运行。

### 验收标准

- 一条命令可以完成内容验证与 production build。
- 发布检查清单覆盖版本、构建、路由、RSS、sitemap 和本地启动验证。
- `package.json`、`package-lock.json` 与 Changelog 的版本信息一致。

## 完成定义

`v0.1.3` 只有在以下条件全部满足时完成：

- Archive Object 模板可用。
- 内容验证能够阻止重复编号、失效关联和非法字段进入 build。
- 状态、排序和公开范围规则一致。
- production build 成功。
- 本地 production 服务验证成功。
- 工程文档与实际行为一致。

## 暂不进入范围

- 搜索和复杂筛选。
- 新一级栏目或新页面体系。
- 对象关系图谱。
- 实时 NAS、金融或 Agent 数据。
- CMS、账户、评论或后台管理。
- 为 OBS-X 增加公开入口或说明。
