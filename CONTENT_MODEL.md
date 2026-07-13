# CONTENT_MODEL.md

# Ayue Observatory Content Model

## Archive Object 定义

Ayue Observatory 的核心内容单位不是传统意义上的 post，而是 **Archive Object**。

Archive Object 表示一个被长期记录、索引和展示的内容对象。它可以是一篇文章、一条研究笔记、一个系统记录、一次市场观察、一个项目、一份失败复盘、一次视觉实验或一段阶段性日志。

首版技术实现使用 Markdown / MDX + frontmatter，不引入复杂 CMS。视觉上将这些 Markdown / MDX 内容表现为 Object。

## Object 类型

首版支持以下类型，frontmatter 中统一使用小写枚举值：

- `essay`：随笔、观点、文学性表达、非技术长文
- `research`：数学、工程、计算机基础、长期学习笔记
- `system`：NAS、自托管、Agent、自动化、开发工作流、工具链
- `signal`：金融、市场观察、数据指标、趋势记录
- `project`：项目、工具、作品、产品化尝试
- `failure`：踩坑、复盘、调试记录、工程事故
- `experiment`：视觉实验、交互实验、模型/工具尝试
- `journal`：可选，短记录、阶段性状态、月度回顾
- `unknown`：尚未形成稳定分类的未来对象或保留位置

页面显示时再映射为首字母大写或中文标签，例如：

- `essay` -> Essay / 随笔
- `research` -> Research / 研究
- `system` -> System / 系统
- `signal` -> Signal / 信号

## frontmatter 字段

推荐字段：

```yaml
title: "对象标题"
type: "essay"
status: "active"
summary: "一句话摘要"
date: "2026-06-25"
updated: "2026-06-25"
tags:
  - "AI Agent"
  - "Self-hosted"
field: "systems"
featured: true
priority: 1
```

可选字段：

```yaml
slug: "custom-object-slug"
objectId: "OBS-0001"
cover: "/images/example.jpg"
related:
  - "another-object-slug"
links:
  demo: "https://example.com"
  repo: "https://github.com/example/repo"
  reference: "https://example.com/reference"
draft: false
```

## 必填字段

首版建议必填：

- `title`
- `type`
- `status`
- `summary`
- `date`
- `tags`
- `field`

其中：

- `updated` 如果缺失，可默认等于 `date`
- `featured` 如果缺失，可默认 `false`
- `priority` 如果缺失，可默认普通排序权重
- `slug` 不强制手写；如果技术栈支持基于文件名生成 slug，应优先使用文件名生成

## 可选字段

可选字段用于增强展示与关联：

- `slug`：自定义 URL，不强制
- `objectId`：视觉编号，例如 `OBS-0001`
- `cover`：封面图
- `related`：相关对象 slug 列表
- `links`：外部链接、仓库、演示地址、参考链接
- `draft`：草稿状态
- `updated`：最后更新日期
- `featured`：是否首页精选
- `priority`：精选排序权重

## 字段命名规则

规则：

- frontmatter key 使用小驼峰或全小写；首版优先全小写简单字段
- 枚举值统一小写
- 日期使用 ISO 格式：`YYYY-MM-DD`
- `type` 使用单数：`essay`、`project`
- `field` 使用站点栏目名，不强求单复数一致，但必须使用固定枚举
- URL slug 使用 kebab-case
- 标签保留自然写法，可包含大小写和空格，例如 `AI Agent`

枚举：

```yaml
type: essay | research | system | signal | project | failure | experiment | journal | unknown
status: draft | active | stable | archived | ongoing | future
field: research | systems | signals | essays | projects | experiments
```

## 类型与导航的关系

首版导航：

- Observatory
- Archive
- Projects
- Essays
- About

关系说明：

- `Observatory`：首页，展示精选对象与当前观测状态
- `Archive`：展示全部 Archive Object，可按 type / field / tag 过滤
- `Projects`：主要展示 `type: project`，也可关联 `experiment` 和 `system`
- `Essays`：展示 `type: essay`、`type: journal`，用于承载正式随笔、短记录和阶段性非技术内容
- `About`：站点说明与个人介绍

`Research`、`Systems`、`Signals` 首版不作为一级导航，而是在 Archive 中作为 field 和过滤维度存在。

## 示例对象数据

### Essay Object

```yaml
title: "关于长期数字空间的一些想法"
type: "essay"
status: "active"
summary: "记录个人网站为什么不应该只是文章列表。"
date: "2026-06-25"
updated: "2026-06-25"
tags:
  - "Writing"
  - "Personal Website"
field: "essays"
featured: true
priority: 1
```

### Research Object

```yaml
title: "线性代数复习笔记：向量空间与线性映射"
type: "research"
status: "ongoing"
summary: "整理线性代数核心概念，用于后续工程和模型理解。"
date: "2026-06-25"
tags:
  - "Math"
  - "Linear Algebra"
field: "research"
featured: false
```

### System Object

```yaml
title: "个人自托管服务的分层整理"
type: "system"
status: "stable"
summary: "梳理 NAS、自托管服务、Agent Runtime 与自动化任务之间的关系。"
date: "2026-06-25"
tags:
  - "Self-hosted"
  - "NAS"
  - "Automation"
field: "systems"
featured: true
priority: 2
```

### Signal Object

```yaml
title: "市场指标日报结构设计"
type: "signal"
status: "active"
summary: "为个人市场观察设计可长期维护的数据指标记录格式。"
date: "2026-06-25"
tags:
  - "Market"
  - "Data Pipeline"
field: "signals"
featured: true
priority: 3
```

### Project Object

```yaml
title: "Agent 管理 NAS 日常任务实验"
type: "project"
status: "ongoing"
summary: "探索多模型 Agent 如何辅助个人数字基础设施维护。"
date: "2026-06-25"
tags:
  - "AI Agent"
  - "Automation"
field: "projects"
featured: true
priority: 4
links:
  repo: ""
  demo: ""
```

### Failure Object

```yaml
title: "一次容器网络异常的排查记录"
type: "failure"
status: "archived"
summary: "记录容器网络策略调整中的错误路径和最终修正。"
date: "2026-06-25"
tags:
  - "Docker"
  - "Network"
field: "systems"
featured: false
```

### Experiment Object

```yaml
title: "Archive Object 卡片动效实验"
type: "experiment"
status: "active"
summary: "探索对象卡片在 hover、聚焦与滚动状态下的视觉反馈。"
date: "2026-06-25"
tags:
  - "Design"
  - "Interaction"
field: "experiments"
featured: false
```

### Journal Object

```yaml
title: "2026-06 观测记录"
type: "journal"
status: "active"
summary: "记录本月研究、项目和阅读状态。"
date: "2026-06-25"
tags:
  - "Journal"
  - "Monthly"
field: "essays"
featured: false
```
