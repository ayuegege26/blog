# Ayue Observatory Content Replacement Plan

> 状态：已完成并归档。本文档保留为 `v0.1.2` 内容替换阶段的历史记录，不再作为当前待办清单。当前工程状态见 `CURRENT_STATE.md`，下一阶段见 `NEXT_PHASE_PLAN.md`。

## 目的

`CONTENT_REPLACEMENT.md` 用于第三阶段之后的具体内容替换工作。

当前站点框架、视觉语言、组件层级和页面结构已经完成。本阶段不再扩展页面、不重做设计、不新增复杂功能，而是把示例内容替换为真实内容，并校准全站语气。

本文件回答四个问题：

- 哪些内容需要替换。
- 替换点分布在哪些层级。
- 推荐按什么顺序执行。
- 哪些结构暂时不应该改动。

---

## 1. 当前阶段定义

当前阶段是 **内容替换与内容校准阶段**。

目标不是继续搭建系统，而是让既有系统承载真实表达：

- 保留 `Ayue Observatory / Personal Observatory` 的站点身份。
- 保留 `Archive Object` 作为核心内容单位。
- 保留 `Observatory / Archive / Projects / Essays / About` 的导航结构。
- 将占位对象、示例文案、说明文字替换为真实内容。
- 统一页面语气，避免重新滑向普通博客、作品集、dashboard 或 NAS 状态页。

---

## 2. 替换范围总览

按可执行替换点计算，目前约有 **51 个内容替换 / 校准点**。

按粗粒度文件块计算，目前有 **18 个内容块**。

分布如下：

| 层级 | 文件 / 区域 | 内容块 | 约替换点 |
| --- | --- | ---: | ---: |
| 内容对象层 | `src/content/archive/*.mdx` | 8 | 16 |
| 首页层 | `src/pages/index.astro` | 1 | 10 |
| 栏目页层 | Archive / Projects / Essays / About | 4 | 19 |
| 全站固定文案层 | Layout / Header / RSS / 404 / card defaults | 5 | 6 |
| 合计 |  | 18 | 51 |

---

## 3. 内容对象层

位置：

```text
src/content/archive/
```

这是最重要的替换层。首页、Archive、Projects、Essays 都会从这些 MDX 对象读取内容。

每个 Archive Object 至少包含两类替换：

- `frontmatter`：标题、类型、状态、摘要、日期、标签、领域、精选权重等。
- 正文内容：对象详情页实际阅读内容。

当前 8 个示例对象：

| 文件 | 当前标题 | 类型 | 建议动作 |
| --- | --- | --- | --- |
| `digital-space-essay.mdx` | 关于长期数字空间的一些想法 | `essay` | 替换为真实随笔或保留并改写为正式首篇 |
| `linear-algebra-notes.mdx` | 线性代数复习笔记：向量空间与线性映射 | `research` | 替换为真实学习 / 研究笔记 |
| `self-hosted-layers.mdx` | 个人自托管服务的分层整理 | `system` | 替换为真实系统记录，避免变成实时状态页 |
| `market-signal-format.mdx` | 市场指标日报结构设计 | `signal` | 替换为静态信号观察或数据记录格式 |
| `nas-agent-project.mdx` | Agent 管理 NAS 日常任务实验 | `project` | 替换为真实项目对象 |
| `container-network-failure.mdx` | 一次容器网络异常的排查记录 | `failure` | 替换为真实踩坑 / 复盘记录 |
| `object-card-motion.mdx` | Archive Object 卡片动效实验 | `experiment` | 替换为真实视觉、交互、模型或工具实验 |
| `june-observation-journal.mdx` | 2026-06 观测记录 | `journal` | 替换为真实阶段性记录 |

### frontmatter 替换要求

每个对象必须保持以下字段语义稳定：

```yaml
title: "对象标题"
type: "essay"
status: "active"
summary: "一句话摘要"
date: "2026-06-25"
tags:
  - "Tag"
field: "essays"
featured: true
priority: 1
objectId: "OBS-0001"
```

允许的枚举仍然遵循 `CONTENT_MODEL.md`：

- `type`: `essay | research | system | signal | project | failure | experiment | journal | unknown`
- `status`: `draft | active | ongoing | stable | archived | future`
- `field`: `research | systems | signals | essays | projects | experiments`

### 替换注意

- 不要把 `note` 作为首版新类型加入。
- 文件名建议使用 kebab-case，并作为 URL slug 的主要来源。
- `objectId` 可以继续使用 `OBS-0001` 这种稳定编号。
- `featured` 和 `priority` 会影响首页与 Archive 的展示顺序。
- `summary` 应是一句话，不要写成完整导语。

---

## 4. 首页层

位置：

```text
src/pages/index.astro
```

首页是 Observatory 的入口。这里要替换的是站点气质和当前状态，不是新增复杂模块。

需要校准的内容点：

1. `fields` 六个长期观察方向。
2. `Current Focus` 当前关注内容。
3. `Latest Object` 兜底文案。
4. `Active Project` 兜底文案。
5. 首页 `title` / `description`。
6. 首屏 kicker、eyebrow、主标题下说明。
7. 核心宣言段落。
8. 三个入口按钮文案。
9. `Archive Snapshot` 区块标题与说明。
10. `精选档案对象` / `长期观察方向` 两个 section 的说明。

### 首页替换原则

- 首页首屏必须仍然一眼是 `Ayue Observatory`。
- 首页文案应说明“这里是什么”，但不要像产品官网。
- 不要把首页改成文章 feed。
- 不要把首页改成 dashboard。
- 首页中出现的对象应来自真实 Archive Object，而不是额外手写列表。

---

## 5. 栏目页层

栏目页结构已经完成。当前只需要替换说明文案，使它们与真实内容匹配。

### Archive

位置：

```text
src/pages/archive/index.astro
```

约 4 个替换点：

- 页面 `title` / `description`。
- 主标题说明。
- `Featured Objects` 说明。
- `All Objects` 说明。

Archive 页应继续作为总索引，不要提前加入复杂筛选系统。

### Projects

位置：

```text
src/pages/projects.astro
```

约 5 个替换点：

- 页面 `title` / `description`。
- 主标题说明。
- 右侧 ledger 英文说明。
- `Active Project` 区块说明。
- `Related Experiments / Systems` 区块说明。

Projects 页应展示 `type: project`，并允许关联 `experiment` 和 `system`，但不要包装成传统作品集。

### Essays

位置：

```text
src/pages/essays.astro
```

约 5 个替换点：

- 页面 `title` / `description`。
- 主标题说明。
- 右侧 ledger 英文说明。
- `Reading Focus` 区块说明。
- `Journal Objects` 区块说明。

Essays 页应作为阅读入口，不要变成无限博客列表。

### About

位置：

```text
src/pages/about.astro
```

约 5 个替换点：

- 开头自我介绍。
- “它为什么存在”。
- “如何浏览”。
- 六个内容领域说明。
- “边界”说明。

About 页应该解释站点与人的关系，但不要写成简历页。

---

## 6. 全站固定文案层

这些文案不多，但会影响整体一致性。

### Base Layout

位置：

```text
src/layouts/BaseLayout.astro
```

替换点：

- 默认 `title`。
- 默认 `description`。
- `og:site_name`。
- RSS alternate title。

### RSS

位置：

```text
src/pages/rss.xml.ts
```

替换点：

- RSS feed title。
- RSS feed description。

### Site Header

位置：

```text
src/components/SiteHeader.astro
```

替换点：

- 顶部品牌文字。
- `aria-label`。
- 导航 label。

首版建议保持当前导航结构：

- Observatory
- Archive
- Projects
- Essays
- About

### Object Detail

位置：

```text
src/layouts/ObjectLayout.astro
```

替换点：

- `Back to Archive Index`。
- `Related Objects`。
- `相关档案对象`。
- `Related Objects will be added later.`

### Card Default Copy

位置：

```text
src/components/archive/FeaturedObjectCard.astro
```

替换点：

- `Featured object / 当前阶段重点对象` 默认提示。

### 404

位置：

```text
src/pages/404.astro
```

替换点：

- 页面标题。
- 页面说明。
- 两个返回入口文案。

---

## 7. 推荐执行顺序

### Step 1: 替换 Archive Object

先替换 `src/content/archive/*.mdx`。

原因：

- 首页精选对象来自这里。
- Archive 总索引来自这里。
- Projects / Essays 的对象列表来自这里。
- 详情页内容来自这里。

完成标准：

- 8 个示例对象都被真实对象替换，或明确保留为正式对象。
- 每个对象 frontmatter 合法。
- 每个对象正文不再是占位文本。
- `featured` 和 `priority` 能表达真实展示优先级。

### Step 2: 校准首页

替换 `src/pages/index.astro` 中的首页文案。

完成标准：

- 首屏表达准确。
- `Observation Log` 显示真实当前状态。
- `Archive Snapshot` 与真实对象列表一致。
- 长期观察方向不再像模板字段。

### Step 3: 校准栏目页

依次处理：

1. `src/pages/archive/index.astro`
2. `src/pages/projects.astro`
3. `src/pages/essays.astro`
4. `src/pages/about.astro`

完成标准：

- 每个页面说明都能解释当前真实内容。
- 页面没有模板腔。
- 页面没有扩展未实现功能的承诺。

### Step 4: 校准全站固定文案

处理 layout、header、RSS、404 和卡片默认提示。

完成标准：

- SEO 描述统一。
- RSS 描述统一。
- 导航与站点身份统一。
- 空状态与错误页语气一致。

### Step 5: Build 验证

内容替换完成后运行：

```bash
npm run build
```

如果 Windows + OneDrive 环境出现 npm 或 Astro 链接问题，可使用已验证过的直接 Astro CLI 路径：

```bash
node .\node_modules\astro\bin\astro.mjs build
```

---

## 8. 当前阶段不建议修改

本阶段暂时不改：

- `src/content.config.ts` 内容 schema。
- `src/lib/archive.ts` 排序和读取逻辑。
- Archive Object 组件层级。
- 页面布局结构。
- 全站 CSS 视觉语言。
- RSS / sitemap 集成方式。
- 导航信息架构。

除非真实内容明确要求，否则不要新增：

- 新一级页面。
- 新内容类型。
- 搜索或筛选系统。
- Dashboard 模块。
- 实时状态数据。
- 评论、订阅、登录等交互系统。

---

## 9. 内容替换检查清单

### Archive Object

- [ ] 每个对象都有真实 `title`。
- [ ] 每个对象都有准确 `type`。
- [ ] 每个对象都有准确 `status`。
- [ ] 每个对象都有一句话 `summary`。
- [ ] 每个对象日期为 `YYYY-MM-DD`。
- [ ] 每个对象 `tags` 不为空。
- [ ] 每个对象 `field` 属于固定枚举。
- [ ] `featured` 与 `priority` 反映真实展示顺序。
- [ ] 正文不再是示例占位内容。

### Homepage

- [ ] 首屏说明准确。
- [ ] `Current Focus` 是真实当前关注。
- [ ] `Active Project` 能指向真实项目对象。
- [ ] `fields` 是真实长期方向。
- [ ] 首页没有新增未实现功能承诺。

### Collection Pages

- [ ] Archive 页说明匹配真实对象范围。
- [ ] Projects 页说明匹配真实项目对象。
- [ ] Essays 页说明匹配真实随笔 / journal 对象。
- [ ] About 页说明匹配真实个人站点定位。

### Global Copy

- [ ] 默认 SEO 描述准确。
- [ ] RSS 描述准确。
- [ ] Header 品牌与导航准确。
- [ ] 详情页空状态自然。
- [ ] 404 页语气一致。

---

## 10. 完成标准

内容替换阶段完成时，站点应满足：

- 所有示例对象都被真实对象替换，或被明确确认保留为正式内容。
- 首页不再依赖模板感表达。
- 各栏目页说明与真实对象一致。
- About 页能解释这个站为什么存在。
- 全站文案仍然保持 `Personal Observatory` 的边界。
- `npm run build` 成功。

