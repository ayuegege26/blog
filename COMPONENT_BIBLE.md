# Ayue Observatory Component Bible

## 目的

`COMPONENT_BIBLE.md` 将 `DESIGN_LANGUAGE.md` 中的视觉语言转化为可实现的组件规范。

本文件不是页面设计稿，也不是审美说明。它是未来 Astro 组件实现时的规格书，用于保证所有页面共享同一套对象语法、观测语法、元信息层级、布局节奏和交互规则。

---

## 1. Archive Object Components

Archive Object Components 是网站最核心的组件组。它们用于展示可被归档、打开、引用和长期维护的内容对象。

所有 Archive Object 组件都必须共享以下基础字段语法：

- Object Number
- Type Label
- Title
- Summary
- Status
- Date / Updated
- Field
- Tags

不同组件的区别只在信息密度、空间占用和使用场景。

### Standard Object Card

#### 使用场景

Standard Object Card 是 Archive Object 的默认展示组件。

用于：

- Archive 总索引页
- 首页精选对象区
- Projects 聚合页
- Essays 聚合页
- Field 或 Type 的对象列表

#### 显示字段

必须显示：

- Type Label
- Object Number
- Title
- Summary
- Status
- Date 或 Updated

建议显示：

- 2-3 个 Tags
- Field Label

可选显示：

- Related count
- External link indicator

#### 信息优先级

1. Type Label + Object Number
2. Title
3. Summary
4. Tags / Field
5. Status + Date

用户扫描时应先知道“这是什么类型的对象”，再读标题，然后决定是否进入。

#### 布局结构

推荐结构：

- 顶部 Meta Row：左侧 Type Label，右侧 Object Number。
- 中部 Content：Title + Summary。
- 底部 Tag Row：最多 3 个 tags。
- 底部 Meta Row：Status + Date / Updated。

卡片内部垂直节奏应稳定。Title 与 Summary 之间距离小于 Summary 与 Tags 之间距离。

#### Hover 状态

Hover 应表示“可进入”。

允许：

- Border 轻微变亮。
- Background 轻微抬升。
- 1-2px translateY。
- Type Label 或 Object Number 变清晰。

禁止：

- 强阴影。
- 发光边框。
- 卡片尺寸变化。
- 大段内容展开。
- 图片或背景剧烈变化。

#### Selected 状态

Selected 用于当前对象、筛选结果焦点或键盘导航焦点。

表现方式：

- Border 比 hover 更稳定、更明确。
- 可增加左侧细线。
- Background 稍微更亮。
- Type Label 的分类 accent 可以更清晰。

Selected 不应像按钮按下状态，也不应使用大面积高亮。

#### 移动端表现

移动端：

- 单列展示。
- 卡片宽度占满内容容器。
- Summary 最多保持 2-3 行。
- Tags 可以换行，但不应超过两行。
- Meta Row 允许换行，但 Object Number 和 Type Label 应优先保持在顶部。

移动端点击区域应覆盖整张卡片。

#### 不应该出现的设计误区

- 像普通博客文章卡。
- 像作品集项目卡，使用大图封面作为主视觉。
- 像 SaaS dashboard metric card。
- 使用大面积分类色背景。
- 把所有 tag 做成同等强度的彩色胶囊。
- 卡片内塞入过多 metadata。

### Featured Object Card

#### 使用场景

Featured Object Card 用于当前阶段重点对象。

用于：

- 首页重点对象区
- Archive 页顶部精选对象
- Field 页中的阶段性重点对象
- 未来专题或观察集合页

#### 显示字段

必须显示：

- Type Label
- Object Number
- Title
- Summary
- Status
- Updated

建议显示：

- Field Label
- Tags
- Short note 或 featured reason

可选显示：

- Related objects preview
- Links indicator

#### 信息优先级

1. Type Label + Object Number
2. Title
3. Summary
4. Featured reason / Context note
5. Status + Updated
6. Tags / Field

Featured Object 的重点是“为什么它现在被观察”，不只是“它更大”。

#### 布局结构

Featured Object 可以比 Standard Object Card 更宽、更高，允许跨列。

推荐结构：

- 顶部细 Meta Line。
- 中部较大的 Title。
- Summary 可显示更完整。
- 侧边或底部放 Status、Updated、Field。
- 可以有一条短的 context note，例如“当前阶段重点整理”。

Featured Object 不依赖图片建立层级。空间、信息完整度和边界层级才是主要区分。

#### Hover 状态

Hover 与 Standard Object Card 保持同源，但幅度更克制。

允许：

- Border 变亮。
- 细线 accent 更明显。
- Title 颜色略微变亮。

不建议使用位移过大，因为 Featured Card 本身空间较大。

#### Selected 状态

Selected Featured Object 可以使用：

- 左侧或顶部 accent line。
- 更明确的 border。
- 更稳定的背景层。

不使用大面积分类色填充。

#### 移动端表现

移动端退化为单列大卡。

规则：

- Title 不应过大。
- Context note 可以保留。
- Tags 数量控制。
- 不使用复杂左右布局。

#### 不应该出现的设计误区

- 把 Featured 做成营销 Banner。
- 使用大图作为主导视觉。
- 通过大号数字或夸张标签表达重要性。
- 和 Standard Card 完全不同，破坏对象系统一致性。

### Compact Object Row

#### 使用场景

Compact Object Row 用于高密度对象索引。

用于：

- Observation 中的 Archive Snapshot。
- Related objects。
- 搜索结果。
- 时间线节点。
- 侧栏列表。
- Archive 页的紧凑视图。

#### 显示字段

必须显示：

- Object Number 或 Type Label
- Title
- Date 或 Status

建议显示：

- Type Label
- Updated
- Field

通常不显示：

- Summary
- Tags

#### 信息优先级

1. Object Number / Type Label
2. Title
3. Date / Status
4. Field

Compact Row 的目标是快速定位，不是完整解释。

#### 布局结构

推荐横向结构：

- 左侧：Object Number 或 Type Label。
- 中间：Title。
- 右侧：Date / Status。

在窄屏中，右侧 Meta 可换到下一行。

Compact Row 应看起来像档案索引条目，而不是普通链接列表。

#### Hover 状态

允许：

- 背景轻微出现。
- 左侧细线出现或变亮。
- Title 变亮。

禁止：

- 位移过大。
- 边框包裹成完整卡片。
- 出现多余装饰。

#### Selected 状态

Selected 可使用：

- 左侧细线。
- 背景轻微抬升。
- Object Number 变亮。

#### 移动端表现

移动端：

- Title 占满主行。
- Meta 信息换行显示。
- 点击区域应至少覆盖整行高度。
- 不压缩成难以点击的小链接。

#### 不应该出现的设计误区

- 退化成普通文章链接。
- 把每一行都做成厚重卡片。
- 显示太多 tags。
- 右侧 meta 挤压标题。

### Inline Object Reference

#### 使用场景

Inline Object Reference 用于正文中引用另一个 Archive Object。

用于：

- 文章正文内相关对象引用。
- 研究笔记中引用项目或系统记录。
- Failure 复盘中引用原始系统记录。
- Journal 中引用阶段性对象。

#### 显示字段

必须显示：

- Object Number 或 Type Label
- Title

建议显示：

- Status

通常不显示：

- Summary
- Tags
- Date

#### 信息优先级

1. Object Number / Type Label
2. Title
3. Status

Inline Reference 的目标是让读者知道“这不是普通链接，而是站内档案对象”。

#### 布局结构

可以有两种形式：

- Inline text form：嵌入段落中的对象引用。
- Block reference form：正文中独立一行的小型引用块。

Inline text form 应保持阅读流畅。
Block reference form 应接近 Compact Object Row，但更轻。

#### Hover 状态

允许：

- 下划线或底部细线变亮。
- Object Number 变亮。
- 背景轻微出现。

禁止：

- 弹窗预览。
- 复杂 tooltip。
- 强色块。

#### Selected 状态

正文中通常不需要 selected 状态。

如果用于当前阅读路径，可使用细线或背景弱提示。

#### 移动端表现

Inline text form 在移动端保持自然换行。

Block reference form 可占满宽度，保证点击区域。

#### 不应该出现的设计误区

- 和外部链接长得完全一样。
- 过度组件化，打断正文阅读。
- 放入完整卡片，破坏文章节奏。

---

## 2. Observation Components

Observation Components 表达当前关注、阶段性记录和档案切片。它们不是 Archive Object 本身。

区别原则：

- Archive Object 是可长期保存和打开的内容对象。
- Observation 是当前状态、上下文或切片。
- Archive Object 回答“这是什么内容”。
- Observation 回答“现在正在看什么”。

### Observation Log

#### 和 Archive Object 的区别

Observation Log 是一组观察记录，不是内容对象列表。

它不一定每条都对应详情页，也不一定可点击。

#### 使用场景

用于：

- 首页当前观测区域。
- About 页说明当前阶段。
- 未来 Journal 页顶部状态。
- Archive 页的阶段性说明。

#### 字段结构

推荐字段：

- Log Label，例如 `Observation Log`。
- Timestamp 或 period，例如 `2026-06`、`This Week`。
- 2-5 条 Observation Entry。
- 可选 footer note。

每条 entry 可包含：

- Entry label。
- Short text。
- Optional date。
- Optional linked object。

#### 文案语气

文案应像研究日志。

适合：

- “整理 Archive Object 的视觉层级。”
- “持续观察 Agent 与个人系统之间的边界。”
- “记录市场信号格式的长期可维护性。”

不适合：

- “3 个任务正在运行。”
- “系统正常。”
- “性能提升 35%。”

#### 是否可点击

Observation Log 本身通常不可点击。

其中某些 entry 可以引用 Archive Object，并通过 Compact Object 或 Inline Reference 可点击。

#### 如何避免 dashboard 感

- 不使用大数字。
- 不使用实时状态灯。
- 不使用成功/失败红绿状态。
- 不模拟监控面板。
- 不使用指标卡布局。

### Observation Entry

#### 和 Archive Object 的区别

Observation Entry 是一条短记录，不是完整档案对象。

它可以未来被整理成 Archive Object，但当前只是观察状态。

#### 使用场景

用于：

- Observation Log 内部。
- 页面侧栏。
- 当前状态区。
- 未来时间线中的轻量节点。

#### 字段结构

推荐字段：

- Entry Type，例如 `Focus`、`Note`、`Signal`。
- Short text。
- Optional date。
- Optional source object。

#### 文案语气

应具体、短、可记录。

避免营销、总结陈词和系统告警语气。

#### 是否可点击

默认不可点击。

只有当 entry 指向一个 Archive Object、外部链接或筛选结果时才可点击。

#### 如何避免 dashboard 感

- 不使用状态图标堆叠。
- 不使用进度条。
- 不使用“健康度”“完成率”等指标语言。

### Current Focus

#### 和 Archive Object 的区别

Current Focus 表示当前注意力方向，不是一个对象。

它可以引用多个对象，但本身是一个阶段性上下文。

#### 使用场景

用于：

- 首页当前关注区。
- Archive 顶部说明。
- Research / Systems 等未来 field 页。
- About 页当前阶段说明。

#### 字段结构

推荐字段：

- Label：`Current Focus`。
- 1 个主描述句。
- 2-4 个 focus terms。
- Optional linked objects。

#### 文案语气

应表达“当前在观察什么”，不是“当前要完成什么”。

适合：

- “把内容对象从文章流中剥离出来，形成可长期维护的档案系统。”

不适合：

- “完成首页改版。”
- “提升转化率。”

#### 是否可点击

Current Focus 容器通常不可点击。

Focus terms 可作为未来筛选入口，但首版不强制。

#### 如何避免 dashboard 感

- 不使用任务状态。
- 不使用 KPI。
- 不使用图表。
- 不使用 completed / pending 等项目管理语言。

### Archive Snapshot

#### 和 Archive Object 的区别

Archive Snapshot 是对 Archive Objects 的切片展示。

它本身不是对象，而是一组对象的当前视图。

#### 使用场景

用于：

- 首页 Object Strip。
- Observation 区中的 recent objects。
- Field 页顶部最近更新。
- 详情页底部 related objects。

#### 字段结构

推荐字段：

- Snapshot Label，例如 `Archive Snapshot`。
- Scope，例如 `Recent Objects`、`Systems / Updated`。
- 3-6 个 Compact Object Row。
- Optional View all link。

#### 文案语气

应像索引说明。

适合：

- “最近更新的档案对象。”
- “当前阶段相关的系统记录。”

不适合：

- “热门推荐。”
- “你可能喜欢。”

#### 是否可点击

Snapshot 容器不可点击。

内部对象必须可点击。

View all link 可点击。

#### 如何避免 dashboard 感

- 使用对象条目，不使用指标卡。
- 不展示总数作为主视觉。
- 不用图表。
- 不把更新时间做成实时动态。

---

## 3. Meta Components

Meta Components 是 Ayue Observatory 的视觉骨架。它们不能全部长得一样。

层级顺序：

1. Type Label：最高 meta 层级，定义对象类型。
2. Object Number：身份锚点，定义对象编号。
3. Status Label：生命周期状态。
4. Date / Updated：时间定位。
5. Field Label：长期领域。
6. Tag：辅助检索。
7. Meta Line：承载多个 meta 的组合结构。

### Object Number

用途：

- 标识 Archive Object。
- 建立档案连续性。

视觉规则：

- 使用 Mono。
- 小字号。
- 低对比，但可读。
- 不使用胶囊背景。
- 可与 Type Label 同行。

不应：

- 做成大号装饰数字。
- 使用强色块。
- 与 Tag 视觉混淆。

### Type Label

用途：

- 表达对象类型。
- 帮助快速扫描。

视觉规则：

- 比 Tag 更强。
- 可使用分类 accent。
- 可显示英文 / 中文组合。
- 通常位于对象顶部。

不应：

- 和普通 Tag 使用同一种样式。
- 过度彩色。
- 缺失于 Standard Object Card。

### Status Label

用途：

- 表达对象生命周期。

视觉规则：

- 低对比。
- 小字号。
- 可使用细边线或文字形式。
- `active` / `ongoing` 可略亮。
- `archived` 更安静。

不应：

- 像系统告警。
- 使用强红绿状态。
- 与 Type Label 抢层级。

### Date / Updated

用途：

- 表达对象时间定位。

视觉规则：

- 使用 Mono。
- 低对比。
- 日期格式保持统一。
- `updated` 优先用于对象卡和详情页；没有 updated 时使用 date。

不应：

- 被隐藏到无法扫描。
- 使用相对时间作为唯一显示，例如“3 days ago”。
- 作为强提醒。

### Field Label

用途：

- 表达长期领域，例如 Research、Systems、Signals。

视觉规则：

- 强度低于 Type Label。
- 可使用纯文字或轻边线。
- 通常出现在 meta line 或详情页 header。

不应：

- 和 Type Label 混用。
- 做成一级导航的视觉强度。

### Tag

用途：

- 辅助检索和语义补充。

视觉规则：

- 小字号。
- 低对比。
- 可使用细边线。
- 卡片中最多显示 2-3 个。

不应：

- 使用高饱和背景。
- 数量过多。
- 抢 Type Label 的层级。

### Meta Line

用途：

- 将多个 meta 信息组织成一行或一组。

常见组合：

- Type Label + Object Number
- Status + Updated
- Field + Date
- Object Number + Type + Status

视觉规则：

- 使用稳定间距。
- 可换行。
- 不强行塞满一行。
- 不同 meta 之间可用细点、斜线、间距或 divider 分隔。

不应：

- 将所有 meta 做成同样的胶囊标签。
- 在移动端挤压标题。
- 使用过多分隔符。

---

## 4. Layout Components

Layout Components 定义页面节奏、内容密度和空间关系。

### Page Header

#### 用途

Page Header 用于页面级入口说明。

用于：

- Archive 页。
- Projects 页。
- Essays 页。
- About 页。
- Object Detail 页。

#### 节奏

Page Header 应给用户足够上下文，但不应像营销 Hero。

推荐包含：

- Eyebrow。
- Page Title。
- Short description。
- Optional Meta Line。

#### 信息密度

中等密度。

Archive / Projects / Essays 可略紧凑。
Object Detail 可更安静、更宽松。

不应：

- 使用大面积背景图。
- 做成 landing page hero。
- 放入复杂 CTA。

### Section Header

#### 用途

Section Header 用于页面内部区块标题。

推荐包含：

- Eyebrow 或 Section Label。
- Section Title。
- Optional short note。

#### 节奏

Section Header 应比 Page Header 更紧凑。

它负责建立区块语义，不负责重新介绍整个页面。

#### 信息密度

低到中等。

不应：

- 每个 section 都使用大标题。
- 重复页面标题文案。

### Object Grid

#### 用途

Object Grid 用于多个 Standard Object Card 的索引展示。

#### 节奏

规则：

- 桌面端多列。
- 移动端单列。
- 卡片间距稳定。
- 不使用瀑布流。
- 不强制所有卡片等高，但同一区域应有稳定视觉节奏。

#### 信息密度

中等。

Object Grid 应适合扫描 6-12 个对象。

不应：

- 像作品集墙。
- 依赖图片裁切。
- 间距过大导致内容稀薄。

### Object Strip

#### 用途

Object Strip 用于横向或窄区域展示一组对象切片。

用于：

- 首页首屏底部。
- Archive Snapshot。
- Related Objects。

#### 节奏

Object Strip 比 Object Grid 更紧凑。

可以使用：

- Standard Object Card 的紧凑变体。
- Compact Object Row 的横向排列。

#### 信息密度

中高密度。

每个对象只显示必要信息。

不应：

- 变成轮播。
- 使用复杂横向滚动作为主要体验。
- 在移动端产生难以控制的横向溢出。

### Prose Layout

#### 用途

Prose Layout 用于对象详情页和长文阅读。

#### 节奏

规则：

- 正文宽度收敛。
- 行高舒适。
- 段落间距清晰。
- 标题层级明确。
- Code、quote、list 与正文有稳定距离。

#### 信息密度

低到中等。

阅读优先，不追求界面密度。

不应：

- 正文铺满大屏。
- 卡片化每个段落。
- 使用太强的终端拟态。

### Split Hero

#### 用途

Split Hero 仅用于需要同时表达站点身份和观测状态的页面入口。

首版主要用于首页。
未来可用于专题页，但不作为所有页面默认结构。

#### 节奏

左侧承载身份、概念或页面核心判断。
右侧承载 Observation Language，而不是普通 panel。

#### 信息密度

左侧低密度。
右侧中密度。

不应：

- 右侧做成 dashboard。
- 左侧堆多个 CTA。
- 每个页面都使用 Split Hero。

### Divider

#### 用途

Divider 用于分隔 section、meta group、object group。

#### 节奏

Divider 应轻，像索引线。

可以使用：

- 横向细线。
- 局部边框。
- 垂直细线。
- Meta 与线结合。

#### 信息密度

Divider 本身不承载主要信息。

不应：

- 使用厚重分割条。
- 使用高亮色大面积分隔。
- 让页面变成表格。

---

## 5. Interaction Rules

交互规则必须全站一致。交互反馈服务于对象可进入、焦点可见、状态可理解。

### Hover

适用：

- Object Card。
- Compact Object Row。
- Inline Object Reference。
- Navigation links。
- Buttons / links。

视觉变化原则：

- Border 或 underline 轻微变亮。
- Background 轻微变化。
- Text 或 Type Label 稍微提高对比。
- 可使用极小位移。

不应：

- 改变组件尺寸。
- 触发复杂动画。
- 使用强光效。
- 展开大量隐藏内容。

### Focus

适用：

- 所有可点击对象。
- 导航。
- 表单控件。
- 未来筛选项。

视觉变化原则：

- 必须清晰可见。
- 应与 selected 状态同源。
- 可使用 outline、border、左侧细线或背景轻微抬升。
- 不能只依赖颜色。

不应：

- 移除 focus。
- 使用浏览器默认但与设计语言冲突的强蓝色而不处理。
- 让 focus 被 hover 覆盖。

### Selected

适用：

- 当前导航项。
- 当前筛选项。
- 当前对象。
- 当前阅读路径。

视觉变化原则：

- 比 hover 更稳定。
- 可使用左侧细线、边框增强或背景抬升。
- 可使用分类 accent，但面积很小。

不应：

- 使用高饱和填充。
- 像按钮 pressed 状态。
- 和 active 混淆。

### Active

适用：

- 点击瞬间。
- 当前正在触发的控件。

视觉变化原则：

- 比 hover 更短暂。
- 可略微降低位移或压低背景。
- 不改变布局。

不应：

- 保持过久。
- 被误认为 selected。

### Disabled

适用：

- 未来不可用筛选项。
- 暂不可访问链接。
- 未启用功能入口。

视觉变化原则：

- 降低文字对比。
- 去除 hover 反馈。
- 保持布局位置。
- 可添加简短说明，但不模拟系统错误。

不应：

- 使用刺眼红色。
- 隐藏到无法理解。
- 仍然表现得可点击。

### Mobile Tap

适用：

- 所有移动端可点击组件。

视觉变化原则：

- 点击区域必须足够大。
- Tap feedback 可以使用轻微背景变化。
- 不依赖 hover 才能发现信息。
- 移动端不应隐藏关键 meta。

不应：

- 只有 hover 才显示重要字段。
- 横向滚动中出现难以点击的小对象。
- 将多个链接挤在同一小区域。

---

## 6. Implementation Priority

首版应优先实现能支撑全站对象语言和观测语言的组件，而不是先实现更多页面。

推荐顺序：

1. Meta Components
   - Object Number
   - Type Label
   - Status Label
   - Date / Updated
   - Field Label
   - Tag
   - Meta Line

2. Archive Object Components
   - Standard Object Card
   - Compact Object Row
   - Featured Object Card
   - Inline Object Reference

3. Layout Components
   - Page Header
   - Section Header
   - Object Grid
   - Object Strip
   - Prose Layout
   - Divider

4. Observation Components
   - Observation Entry
   - Observation Log
   - Current Focus
   - Archive Snapshot

5. Interaction Rules Across Components
   - hover
   - focus
   - selected
   - active
   - disabled
   - mobile tap

6. Split Hero Refinement
   - Only after Object, Meta and Observation components are stable.
   - Split Hero should consume existing components instead of inventing page-specific visuals.

首版组件实现的关键判断标准：

- 遮住 Logo 后，Archive Object 仍然能被识别为 Ayue Observatory 的对象。
- 所有 tag、status、type、number 不再长得一样。
- Observation 区域不再像普通 panel 或 dashboard。
- 页面布局依靠统一组件节奏，而不是单页手工排版。
- 移动端保留对象语法，不退化成普通文章列表。

