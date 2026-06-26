# Ayue Observatory Design Language

## 目的

`DESIGN_LANGUAGE.md` 是 Ayue Observatory 未来所有视觉实现的最高规范。

它不定义某一个页面的布局，也不描述某个 Hero 应该如何设计。它定义的是整个网站共同遵循的视觉语法：内容对象如何被识别，观测状态如何被表达，文字如何建立层级，页面如何组织节奏，颜色如何承载信息，动效如何保持克制。

Ayue Observatory 的视觉目标不是“漂亮”，而是形成一种可长期运行、可不断扩展、可被一眼识别的个人观测站语言。

---

## 1. Archive Object Language

Archive Object 是网站的核心视觉单位。它不是普通文章卡片，也不是作品集项目卡，而是一个被编号、归档、追踪和更新的内容对象。

### 核心原则

Object Card 必须表达三件事：

- 这是一个档案对象，不是普通链接。
- 它属于某个长期领域，而不是孤立文章。
- 它有状态、编号、时间和上下文。

Object Card 的视觉气质应接近“档案索引卡 + 研究记录条目”，而不是博客卡片、SaaS metric card 或作品展示封面。

### Object Number

Object Number 是 Archive Object 的身份锚点。

规则：

- 应优先显示 `objectId`，例如 `OBS-0001`。
- 如果没有 `objectId`，可以显示 slug 或系统生成 ID，但视觉上仍应被处理为编号。
- 编号使用 Mono 层级，字号小于标题，权重低于 Type Label。
- 编号不应被装饰成徽章，也不应喧宾夺主。
- 编号的位置应稳定，通常位于卡片顶部或详情页元信息区。

Object Number 的作用不是“酷”，而是建立档案系统的可信度和连续性。

### Type Label

Type Label 是对象的内容类型声明。

规则：

- Type Label 必须比普通 tag 更高一级。
- Type Label 可以包含英文与中文，例如 `Research / 研究`。
- Type Label 使用 Mono 或小号 UI Sans。
- Type Label 可以使用非常克制的分类 accent，但不能使用高饱和色块。
- Type Label 应出现在对象视觉读取路径的前段。

Type Label 解决的问题是：访问者不需要先读标题，就知道这个对象属于哪种内容。

### Status

Status 表示对象的生命周期状态。

允许状态：

- `draft`
- `active`
- `ongoing`
- `stable`
- `archived`

规则：

- Status 不应被设计成强提醒。
- Status 适合出现在卡片底部、元信息行或详情页 header。
- Status 使用低对比文字、细边线或微弱色彩差异。
- `active` 和 `ongoing` 可以稍微更亮；`archived` 应更安静。
- 不使用红绿灯式状态设计，避免 dashboard 感。

Status 的语义是“记录状态”，不是“系统告警”。

### Summary

Summary 是对象的最短解释。

规则：

- Summary 应承担内容判断，而不是营销描述。
- 卡片内 Summary 保持 1-2 行的阅读节奏。
- Summary 的颜色低于标题，高于元信息。
- Summary 不应被缩小到无法阅读。
- Summary 应避免模板化语气，例如“探索……的解决方案”。

Summary 让对象有内容密度，而不是只留下标题索引。

### Meta Information

Meta Information 包括日期、更新时间、field、tags、links、related、status 等。

规则：

- Meta 信息使用 Mono 层级或小号 UI Sans。
- Meta 信息应形成细线索引感，而不是标签墙。
- 日期应稳定出现，避免对象失去时间感。
- Tags 最多在卡片中显示 2-3 个，其余留给详情页。
- Meta 信息应以“定位对象”为目的，不以“填满卡片”为目的。

Meta 的视觉角色是建立秩序，而不是制造复杂度。

### Border

Border 是 Archive Object 的主要容器语言。

规则：

- Border 应细、低对比、稳定。
- Border 代表对象边界，而不是装饰框。
- 不使用厚边框、大面积发光边框或强玻璃拟态。
- Border 可以在 hover 或 selected 状态中略微变亮。
- Border radius 控制在 8px 以内。

Ayue Observatory 的卡片不依赖阴影建立层级，而依赖边界、间距、元信息和排版建立层级。

### Hover

Hover 表示“可进入”，不是表演。

规则：

- Hover 可以轻微提升边界亮度。
- Hover 可以有 1-2px 的位移。
- Hover 可以让 Type Label 或 Object Number 更清晰。
- Hover 不应改变布局尺寸。
- Hover 不应出现闪烁、扫描、强发光或复杂展开。

Hover 的语气是“这个对象可以被打开”，不是“这个卡片在炫技”。

### Selection

Selection 表示对象被当前页面、过滤器或阅读上下文选中。

规则：

- Selection 应比 hover 更稳定。
- Selection 可使用左侧细线、边框增强或背景轻微抬升。
- Selection 不应使用大面积高亮色。
- Selection 应适合列表、导航、筛选、related objects 等多种场景。

Selected Object 应像被放入观测焦点，而不是被按钮选中。

### Featured Object

Featured Object 是精选对象，不是广告位。

规则：

- Featured 状态可以增加空间、摘要长度或元信息完整度。
- Featured 不应依赖大图封面来制造重要性。
- Featured 可以使用更完整的 Object Number、Type、Status 和 Summary 组合。
- Featured 的层级提升应来自信息丰富度，而不是视觉噪音。

Featured Object 是“被当前阶段重点观察”，不是“被推荐购买”。

### Compact Object

Compact Object 用于列表、侧栏、related links、时间线和索引区。

规则：

- Compact Object 至少保留 Type 或 Object Number、标题、日期或状态。
- Compact Object 可以省略 Summary。
- Compact Object 应保留档案对象的语法，不退化成普通文字链接。
- Compact Object 适合使用横向条目，而不是完整卡片。

Compact Object 是网站未来扩展搜索、时间线、关系对象时的基础语言。

### Object Hierarchy

对象层级分为四级：

1. Featured Object：当前阶段重点对象。
2. Standard Object：常规档案卡片。
3. Compact Object：索引、列表、侧栏对象。
4. Inline Object Reference：正文中的对象引用。

所有层级都应共享相同语法：编号、类型、标题、状态、时间。区别只在信息密度和空间占用。

---

## 2. Observation Language

Observation 是 Ayue Observatory 区别于普通博客的关键语言。

首页右侧不应只是普通 panel。整个网站中，只要表达当前状态、近期关注、阶段性记录，都应使用 Observation Language。

### Observation 的基本语义

Observation 表示“正在被看见、记录、追踪或回顾的东西”。

它不是 dashboard，因为它不展示实时指标。
它不是 notification，因为它不制造即时压力。
它不是 card，因为它不是独立内容对象。

Observation 更接近研究日志、观测条目和档案快照。

### 推荐表达模式

#### Observation Log

用于记录当前阶段的观察状态。

适合内容：

- 当前研究方向
- 本周关注主题
- 最近整理的问题
- 阶段性站点状态

视觉规则：

- 应像一组简短日志，而不是三个独立指标块。
- 每条 log 可以包含时间、主题、短句。
- 使用纵向节奏和细 divider。
- 不使用大数字或实时状态灯。

#### Observation Entry

用于表达单条观察记录。

适合内容：

- 一条市场观察
- 一次系统记录
- 一段研究进展
- 一个临时问题

视觉规则：

- 应有轻微时间戳感。
- 文案可以短，但必须具体。
- 可与 Archive Object 建立引用关系。

#### Current Focus

用于表达当前注意力所在。

适合内容：

- 近期正在研究的领域
- 当前项目
- 正在积累的对象类型

视觉规则：

- 不应像任务列表。
- 不应像 OKR。
- 应像观测镜头当前指向的区域。

#### Archive Snapshot

用于表达档案系统的切片。

适合内容：

- 最近更新对象
- 某类型精选对象
- 某 field 的近期记录
- 某阶段产出的档案对象

视觉规则：

- 应保留 Archive Object 的编号和类型。
- 可以使用 Compact Object 形式。
- 不应变成普通“最新文章”列表。

#### Research Timeline

用于未来表达长期演进。

适合内容：

- 学习路径
- 项目阶段
- 系统迭代
- 月度回顾

视觉规则：

- 时间线应克制，不做复杂关系图谱。
- 应强调记录顺序，而不是动画路径。
- 节点应使用 Archive Object 或 Observation Entry 语法。

### Observation 与 Archive Object 的区别

Archive Object 是可被打开、长期保存的内容对象。

Observation 是某一时刻的观察状态、索引切片或上下文提示。

简单说：

- Object 是档案。
- Observation 是观测。
- Object 可进入详情。
- Observation 帮助理解当前站点正在看什么。

---

## 3. Typography Language

Ayue Observatory 的字体语言不是靠字体名称建立，而是靠角色关系建立。

整体原则：

- 标题负责建立空间和判断。
- 正文负责阅读。
- 编号负责系统性。
- Meta 负责秩序。
- Code 负责精确。
- Tag 负责分类。
- Caption 负责低声解释。

### Title

标题用于建立页面或对象的主判断。

规则：

- 页面级标题可以大，但必须冷静。
- 对象详情标题可以有文学性，但不应像营销标题。
- 卡片标题必须克制，避免过大造成 portfolio 感。
- 标题行高应紧，但不能压迫中文阅读。
- 不使用负字距。

标题的气质应是“档案索引中的主项”，不是海报口号。

### Body

正文用于长期阅读。

规则：

- 中文正文应有舒适行高。
- 阅读宽度应收敛，不铺满大屏。
- 段落之间要有清晰呼吸。
- 正文颜色不应纯白刺眼。
- 长文页面应优先保护阅读，而不是展示组件。

正文是网站可信度的核心，不应被界面感压过。

### Number

编号用于对象身份、序列、状态定位。

规则：

- 使用 Mono。
- 字号小，稳定，低声。
- 可出现在卡片、详情页、列表、时间线、引用中。
- 不应变成装饰性大号数字。

Number 让 Ayue Observatory 有档案连续性。

### Meta

Meta 用于日期、状态、field、type、更新时间等结构信息。

规则：

- 使用 Mono 或小号 UI Sans。
- 通常 uppercase 英文或短中文。
- 颜色低于正文。
- 字距可以略微增加，但不能影响可读性。
- Meta 应形成秩序线，而不是噪音。

Meta 是视觉系统里的骨架。

### Code

Code 用于真实代码、命令、路径、配置和技术标记。

规则：

- Code 应与 Meta 有亲缘关系，但更明确、更可复制。
- Inline code 不应过亮。
- Code block 应服务阅读，不做终端拟态表演。
- 不使用强扫描线或发光终端效果。

Code 的目的是真实、准确、可读。

### Tag

Tag 用于轻量分类。

规则：

- Tag 低对比、小字号。
- Tag 不应抢 Type Label 的层级。
- 普通 tag 不使用大面积填充。
- 标签数量应被控制。

Tag 是辅助检索语言，不是装饰系统。

### Caption

Caption 用于图片说明、图表说明、注释和附属解释。

规则：

- Caption 比正文更轻。
- 可以使用 Meta 语气，但不能过于机械。
- Caption 应靠近被解释对象。
- Caption 不应承担正文内容。

Caption 是旁注，不是第二正文。

---

## 4. Layout Language

Ayue Observatory 的布局语言应像一个有秩序的档案空间：可浏览、可停留、可深入，而不是信息堆满的 dashboard。

### Width

规则：

- 全站需要稳定的最大内容宽度。
- 长文阅读宽度应明显窄于索引页面。
- 对象卡片网格可以更宽，但正文不能跟随大屏无限扩张。
- 元信息区可以跨宽，但正文要保护可读性。

宽度的核心不是“占满”，而是“给内容正确的容器”。

### Grid

规则：

- Grid 用于对象索引、领域切片、精选区。
- Grid 应保持稳定间距。
- 不追求瀑布流。
- 不使用过度复杂的不规则拼贴。
- Featured Object 可以跨列，但必须仍然遵守对象语法。

Grid 应让对象之间形成档案索引，而不是作品墙。

### Section

规则：

- Section 是内容节奏单位，不是卡片容器。
- 页面大区块不应都被包进 card。
- Section 可以使用标题、eyebrow、divider、留白建立边界。
- Section 内部再放置对象、条目或正文。

Section 应像档案目录中的章节。

### Divider

规则：

- Divider 使用细线、低对比。
- Divider 用于分隔上下文，不用于装饰。
- Divider 可以配合 Meta 或 Section Title。
- 不使用厚重分割块。

Divider 是“索引线”，不是视觉阻断。

### Content Rhythm

规则：

- 页面从上到下应有稳定呼吸。
- 首屏、索引区、正文区、尾部区应有不同密度。
- 对象列表密度可以高，但不能拥挤。
- 详情页应比索引页更安静。

Ayue Observatory 的节奏应允许用户扫描，也允许用户停下来读。

### Vertical Spacing

规则：

- 页面级区块之间使用较大垂直间距。
- 卡片内部使用紧凑但清晰的垂直节奏。
- Meta 与标题之间可以紧，Summary 与 tags 之间应留出呼吸。
- 长文段落间距要明显高于普通界面文本。

垂直间距表达内容层级。

### Horizontal Rhythm

规则：

- 页面左右边距在移动端必须保留。
- 卡片间距不应过大，避免 portfolio 感。
- 面板、对象、正文之间应形成清晰列关系。
- 横向布局在窄屏应自然堆叠，而不是压缩文字。

横向节奏应保持“整理过的档案桌面”感。

---

## 5. Color Language

目前的白、灰、金可以作为基础气质，但不足以支撑长期扩展的 Archive Object 系统。

Ayue Observatory 应采用克制的分类色，但分类色必须服务信息结构，而不是装饰。

### 基础色角色

基础色继续保持：

- Background：近黑、炭灰、深海墨色。
- Surface：比背景略亮的深灰。
- Border：低对比灰。
- Text Primary：冷白或纸白。
- Text Secondary：银灰、雾灰。
- Global Accent：低饱和金色或旧铜色。

Global Accent 不应被滥用。它只用于全站身份、关键交互和少量重点信息。

### 分类色策略

建议采用 Object Type / Field 的低饱和分类色。

原因：

- Archive Object 类型较多，长期只靠文字会降低扫描效率。
- 分类色可以帮助用户建立空间记忆。
- 低饱和色可以强化对象系统，而不会破坏克制气质。
- 分类色可服务 Archive、Object Card、Timeline、Related Objects 等未来结构。

分类色不应作为大面积背景使用，只用于：

- Type Label
- 左侧细线
- 小型状态点
- Hover 或 selected 的边界增强
- 详情页元信息局部强调

### 建议色彩方向

分类色应使用低饱和、偏灰、偏暗的版本。

- Research：冷青灰，表达理性、抽象、学习。
- Systems：钢蓝灰，表达结构、基础设施、工具链。
- Signals：低饱和琥珀，表达观察、变化、市场信号。
- Essays：旧纸白或暗红灰，表达个人文字与观点。
- Projects：银紫灰，表达构建、实验性产品、可迭代对象。
- Experiments：酸性黄绿的极少量点缀，表达试验和不稳定性。
- Failure：锈红灰，表达复盘和错误路径，但不能像危险告警。
- Journal：雾灰，表达阶段记录和低强度状态。

### 分类色边界

规则：

- 单个页面不应被某一种分类色主导。
- 分类色不应用于大面积渐变。
- 分类色不应用于普通按钮。
- 分类色不应替代文字标签。
- 分类色必须在暗色背景上保持可读，但不能刺眼。

颜色在 Ayue Observatory 中是一种索引系统，不是情绪滤镜。

---

## 6. Motion Language

Ayue Observatory 的 motion language 不是动画语言，而是交互反馈语言。

Motion 的目标：

- 帮助用户理解对象可进入。
- 帮助页面层级轻微变化。
- 帮助焦点转移。
- 保持阅读安静。

### Hover

规则：

- Hover 轻、短、稳定。
- 主要变化来自 border、background、文字亮度或 1-2px 位移。
- Hover 不改变布局。
- Hover 不展开大段内容。
- Hover 不制造强光或闪烁。

Hover 应像手指划过档案索引卡。

### Transition

规则：

- Transition 时长短。
- 缓动自然，不弹跳。
- 所有基础交互应保持一致节奏。
- 不同组件不应拥有完全不同的动效性格。

Transition 是全站语气的一部分。

### Fade

规则：

- Fade 可用于页面进入、section 进入或内容加载。
- Fade 应低调，不能影响阅读。
- 不做大面积连续滚动动画。
- 不为了“高级感”让内容延迟出现。

Fade 的作用是降低突兀，而不是制造舞台效果。

### Elevation

规则：

- Elevation 不主要依赖阴影。
- 层级变化可以通过 border、surface、位移和信息密度表达。
- 不使用重阴影、浮夸玻璃层或强模糊背景。

Ayue Observatory 的层级是档案层级，不是悬浮界面层级。

### Focus

规则：

- Focus 必须清晰可见。
- Focus 风格应与 selected object 有亲缘关系。
- 键盘访问时不能只依赖 hover。
- Focus 不应破坏暗色视觉系统。

Focus 是可访问性的一部分，也是对象被观测的状态。

### Loading

规则：

- Loading 应尽量少出现，因为首版以静态生成优先。
- 如果出现，应使用文本、细线或轻量占位。
- 不使用复杂 spinner、实时终端流或假数据扫描。
- Loading 文案应克制，不模拟系统监控。

Loading 应表达“内容正在准备”，不是“系统正在运转”。

---

## 7. Design Philosophy

Ayue Observatory 的设计哲学是：

> 以档案对象组织长期记录，以观测语言表达当前注意力，以克制的暗色编辑系统承载个人研究和构建过程。

### 为什么它不像普通博客

普通博客通常围绕文章流、发布时间和分类目录展开。Ayue Observatory 围绕 Archive Object 展开。

在这里，一篇文章、一个项目、一条信号、一次失败复盘和一段阶段日志都不是“post”，而是同一个档案系统中的不同对象。

它不以“最新文章列表”作为核心体验，而以“对象索引、状态、编号、类型、长期领域”建立结构。

### 为什么它不像 Portfolio

Portfolio 通常强调作品展示、视觉冲击、项目成果和个人能力证明。Ayue Observatory 不以展示成果为中心。

它允许项目存在，但项目只是长期观察和构建的一部分。失败复盘、学习笔记、系统记录、市场信号和随笔拥有同等结构地位。

它不试图证明“我做过什么”，而是呈现“我长期在观察、研究、构建和记录什么”。

### 为什么它不像 Dashboard

Dashboard 强调实时数据、指标、监控、控制和效率。Ayue Observatory 不展示真实 NAS 状态、金融实时数据或 Agent 状态。

它可以有 Observation Log，但那不是监控面板。它可以有 Current Focus，但那不是任务系统。它可以有 Archive Snapshot，但那不是指标大屏。

它关心的是长期记录的可读性和可追踪性，而不是即时控制。

### 为什么它就是 Ayue Observatory

因为它有自己的核心语法：

- Archive Object：所有内容以对象存在。
- Observation Language：当前注意力以观测方式表达。
- Number / Type / Status / Meta：内容有档案秩序。
- Quiet Dark Editorial：视觉冷静、暗色、克制、有编辑感。
- Long-running Structure：页面不是一次性展示，而是为长期积累服务。

Ayue Observatory 的辨识度不来自 Logo，也不来自某一个首页 Hero。

它的辨识度来自：当用户看到编号、类型、状态、低声的元信息、克制的对象边界和观测式文案时，会意识到这里不是普通博客，不是作品集，不是 dashboard，而是一个持续运行的个人观测站。

