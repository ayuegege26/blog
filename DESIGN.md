# DESIGN.md

# Ayue Observatory Design Specification

## 站点定位

**Ayue Observatory** 是一个长期运行的个人观测站，用来沉淀研究、系统、信号、项目、实验、随笔与阶段性记录。

它不是 NAS 站、基础设施站、企业官网、简历站或普通技术博客。NAS、自托管、AI Agent、金融数据系统只是当前内容资产的一部分，不构成网站身份边界。

网站第一眼应该表达：

- 这是一个人的长期数字空间
- 这个人在持续观察、研究、构建和记录
- 内容以档案对象的方式被组织，而不是简单文章流
- 视觉上有终端感、档案感和编辑感，但不变成运维后台

概念描述：

> A personal observatory for research, systems, signals, essays and experiments.

中文表达应承担主要解释与内容表达；英文可以作为视觉符号、导航语言和界面气质的一部分，但不能让中文站点变成英文模板。

## 视觉关键词

- Personal Observatory
- Archive Index
- Research Terminal
- Editorial Dark
- Quiet System
- Object-based Content
- Long-running Notes
- Signal Recording
- Digital Archive

视觉气质：

- 暗色，但不是廉价赛博朋克
- 终端感，但不是服务器监控台
- 档案感，但不是复古报纸
- 杂志式排版，但不是作品集模板
- 技术感来自信息结构、层级和交互细节，而不是发光边框堆料

## 首页首屏结构

首页首屏承担第一印象任务，不做普通博客列表，也不做复杂 dashboard。

### 左侧：身份与概念

核心内容：

- 站点名：`Ayue Observatory`
- 概念描述：中文为主，英文辅助
- 2-3 个主入口：
  - Explore Archive
  - View Projects
  - Read Essays

推荐中文描述方向：

> 一个关于研究、系统、信号、随笔与实验的长期数字档案。

### 右侧：轻量观测面板

首版最多保留 3 个核心块：

- **Now Observing**：当前关注主题
- **Latest Object**：最近档案对象
- **Active Project**：当前项目或工具

这些块应表现为“观测记录”或“档案索引卡”，不要表现为 SaaS dashboard、服务器监控面板或指标大屏。

### 底部：Object Strip

首屏底部可以露出一排 Archive Object 卡片，暗示网站核心是对象化档案系统，而不是文章流。

Object Strip 可包含：

- 类型标签
- 编号
- 标题
- 一句话摘要
- 更新时间
- 状态

## 首页第二屏结构

第二屏承担“内容宇宙地图”的功能。

推荐结构：

1. **Archive Objects**
   - 展示 6-8 个精选对象
   - 覆盖 Essay、Research、System、Signal、Project、Failure、Experiment 等类型
   - Recent Signal 可以出现在这里，而不是首屏右侧面板

2. **Current Fields**
   - 展示长期方向：
     - Research
     - Systems
     - Signals
     - Essays
     - Projects
     - Experiments
   - 只做方向说明，不做复杂栏目堆叠

第二屏不应像普通博客列表。它更像一个有编号、有类型、有状态的档案索引。

## 导航规则

首版导航采用收敛方案：

- Observatory
- Archive
- Projects
- Essays
- About

规则：

- `Observatory` 是首页入口。
- Logo / 站点名必须可点击返回首页，避免用户不理解 Observatory 是首页。
- `Archive` 是全部 Archive Object 的主索引。
- `Projects` 是项目与工具的聚合入口。
- `Essays` 是随笔、观点、短记和非技术表达的聚合入口，不只承载长文。
- `About` 做克制个人说明，不做简历站。

后续内容丰富后，可考虑扩展为：

- Observatory
- Research
- Systems
- Signals
- Essays
- Projects
- Archive

但首版不采用完整导航，避免栏目过多、内容显空。

## 字体层级

字体系统应形成“编辑感 + 终端感”的组合。

建议层级：

- Display：用于首页大标题、章节标题，字形应冷静、有结构感
- UI Sans：用于导航、按钮、卡片标题、界面说明
- Mono：用于对象编号、状态、日期、元信息、代码与局部终端感元素
- Reading Font：用于长文正文，优先保证中文可读性

排版原则：

- 首页标题可以大，但卡片和面板内标题必须克制
- 中文正文需要足够行高和阅读宽度
- 英文元信息可小字号处理，作为视觉秩序的一部分
- 不使用负字距
- 不用视口宽度动态缩放字体

## 色彩角色

首版以暗色为主，但避免单一黑灰技术模板。

建议色彩角色：

- Background：近黑、炭灰、深海墨色
- Surface：比背景略亮的深灰，用于对象卡片或面板
- Border：低对比灰，用于分栏、卡片边界、索引线
- Text Primary：冷白或纸白
- Text Secondary：银灰、雾灰
- Accent：低饱和强调色，只用于状态、分类和交互反馈

对象类型可使用低饱和色区分：

- Essay：旧纸白 / 暗红
- Research：冷青灰
- System：钢蓝
- Signal：琥珀
- Project：银紫灰
- Failure：锈红
- Experiment：酸性黄绿少量点缀
- Journal：雾灰

色彩用于信息结构，不用于装饰堆料。

## 卡片样式

Archive Object 卡片是首版核心视觉组件。

卡片规则：

- 边界轻，不做厚重容器
- 圆角控制在 8px 以内
- 使用细线、编号、类型、状态构建档案感
- hover 时可以有轻微位移、边界变亮或元信息展开
- 不做强玻璃拟态
- 不做过度阴影
- 不把页面大区块都做成卡片

卡片信息优先级：

1. 类型 / 编号
2. 标题
3. 摘要
4. 标签
5. 更新时间 / 状态

## 标签样式

标签是信息结构的一部分，不是装饰贴纸。

规则：

- 标签小字号
- 低对比背景或纯文字加边线
- 不使用高饱和色块
- 类型标签和普通标签视觉上要区分
- 状态标签应克制，例如 active、ongoing、stable、archived

## 动效边界

首版动效少而准。

允许：

- 页面元素淡入
- 卡片 hover 层级变化
- 导航 hover 反馈
- 轻微的面板状态切换
- 滚动进入视口的低调位移

不允许：

- 大面积粒子动效
- WebGL
- 复杂关系图谱
- 频繁闪烁扫描线
- 过度视差
- 影响阅读的动画
- 为了炫技牺牲性能和维护性

## 禁止出现的视觉误区

首版禁止：

- 做成服务器监控台
- 做成企业 SaaS dashboard
- 做成普通 Hexo/Hugo 暗色博客
- 做成简历主页
- 做成 NAS / 自托管主题站
- 大量发光边框
- 过度玻璃拟态
- 廉价赛博朋克
- 首页强突出具体代理、脚本、内网细节
- 用英文模板腔取代中文内容表达
- 把所有内容都包装成技术教程
