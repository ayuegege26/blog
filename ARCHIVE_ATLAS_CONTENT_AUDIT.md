# Archive Atlas 内容核查与 OpenPaw 询问记录

> 核查日期：2026-07-16
>
> 状态：第一轮内容核查与七个真实 Archive Object 接入均已完成。
> 用途：记录 VS–001 第二阶段的数据边界、点位语义、事实来源、未知项与候选内容。本文不是公开文章，也不把私人记忆直接发布到浏览器。

## 1. 核查原则

Archive Atlas 中一个点只代表一个真实、公开、可以独立阅读的 Archive Object。以下内容不能自动成为点：

- NAS 上的单个服务、设备、端口或配置项。
- 一条零散记忆、一次对话或模型推测。
- 尚未发生的计划，或只有标题而没有正文的未来位置。
- OpenPaw 能描述、但尚未经过作者确认并写成公开 MDX 的素材。

当前原型中的 12 个点只用于验证布局和交互，不是 12 个固定内容槽。正式节点数量必须由符合公开条件的 MDX 数量决定。

## 2. 拓扑字段的固定含义

| 视觉元素 | 数据来源 | 含义 |
| --- | --- | --- |
| 节点 | 一个公开 MDX | 一个 Archive Object |
| 时间位置 | `date` | 首次发布日期，不使用推测的事件日期 |
| 更新轨迹 | `updated` | 发布后的明确更新 |
| 轨道 | `field` | `research / systems / signals / essays / projects / experiments` |
| 颜色 | `type` | `essay / research / system / signal / project / failure / experiment / journal / unknown` |
| 边框或状态符号 | `status` | `draft / active / stable / archived / ongoing / future` |
| 节点大小 | 正文实际字数 | 自动计算的阅读时间，不由模型估造 |
| 关联线 | `related` | 作者明确填写的相关对象；不表示依赖或因果 |
| 详情和入口 | frontmatter 与生成路由 | 标题、摘要、标签、日期和公开文章 URL |

Canvas 中双向重复的 `related` 可以合并为一条视觉线，但详情中必须保留关系来源。主题相似、共同标签或同一基础设施背景不足以建立关系线。

## 3. 信息来源优先级

1. 公开 Archive MDX：正式标题、摘要、分类、状态、日期、标签、关系和正文。
2. 作者确认：解释含义、修正日期、决定公开边界和确认新对象。
3. OpenPaw 本地记忆：只提供候选事实、历史背景、未知项和隐私风险。
4. 模型建议：只能作为待审核分类或写作方向，不能覆盖 MDX 或作者决定。

当来源冲突时，OpenPaw 回答不能覆盖现有 MDX。完全不知道的内容必须保持未知，不能为了图谱完整而补写。

## 4. OpenPaw 询问方法

询问被拆为三批，避免一次性长回答超时：

- 第一批：`digital-space-essay`、`self-hosted-layers`、`nas-agent-project`。
- 第二批：`linear-algebra-notes`、`market-signal-format`、`container-network-failure`、`object-card-motion`。
- 第三批：寻找不与现有七项重复的新候选。

每项要求区分：

- `known_facts`：可核实的原子事实。
- `suggested_*`：分类建议及置信度。
- `unknowns`：无法确认的内容。
- `questions_for_owner`：写成可靠公开内容前必须询问作者的问题。
- `privacy_risks`：只说明风险类别，不返回敏感值。
- `explicit_related`：必须提供具体依据，否则为空。

询问明确禁止输出密码、令牌、身份信息、私人通信、地址、端口和私有路径。

## 5. 现有对象核查

OBS-X 是隐藏彩蛋，按作者决定排除。`june-observation-journal` 的内容和状态均为 future/unknown，也不作为真实事实节点。当前可接入七个对象。

### 5.1 `digital-space-essay`

- 正式来源：公开 MDX。
- OpenPaw 状态：`unknown`，没有找到可以补充的个人记忆事实。
- 处理：只使用 MDX，不从模型生成额外背景、日期或关系。

### 5.2 `linear-algebra-notes`

- 正式来源：公开 MDX，类型为 `research`，领域为 `research`，状态为 `ongoing`。
- 已知内容：正文实际讨论如何把学习过程组织为可复用研究笔记，而不是一篇线性代数课程笔记。
- 未知项：现有 slug 是否需要在未来调整；发布日期与文件创建时间是否完全一致。
- 处理：第二阶段保持现有 slug 和 MDX，不因标题语义重新命名。

### 5.3 `self-hosted-layers`

- 正式来源：公开 MDX。
- OpenPaw 状态：`partial`。
- 可用素材：确实存在网络接入、存储、知识服务、Agent 和站点等分层运行记录。
- 风险：基础设施细节可能包含不应公开的内部结构。
- 处理：Atlas 只使用现有 MDX。OpenPaw 素材必须经过作者确认后才能补入正文。

### 5.4 `market-signal-format`

- 正式来源：公开 MDX，类型为 `signal`，领域为 `signals`，状态为 `active`。
- 已知内容：正文记录每日三个市场指标和固定的手动记录格式。
- 未知项：一个月实验是否完成、指标是否调整、后续报告是否存在。
- 处理：保持现有 MDX；未知结果不由模型补写。

### 5.5 `nas-agent-project`

- 正式来源：公开 MDX，当前文章主题是“工具如何进入我的工作流”。
- OpenPaw 状态：`partial`，掌握大量 NAS Hardware Agent 的技术迭代与测试素材。
- 冲突：OpenPaw 容易把 Hardware Agent 项目史与现有方法论文章视为同一对象。
- 处理：不得使用 Hardware Agent 技术资料替换现有文章。若作者希望公开该项目，应另建独立 Project Object。
- 风险：基础设施结构和内部网络信息。

### 5.6 `container-network-failure`

- 正式来源：公开 MDX，类型为 `failure`，领域为 `systems`，状态为 `archived`。
- 已知内容：正文记录容器 DNS 配置读取权限导致网络异常的排查过程，以及由此形成的部署检查习惯。
- 未知项：frontmatter 日期是事件日还是文章发布日期。
- 处理：Atlas 一律把 `date` 解释为文章首次发布日期，不推测事件发生日。

### 5.7 `object-card-motion`

- 正式来源：公开 MDX，类型为 `experiment`，领域为 `experiments`，状态为 `active`。
- 已知内容：正文定义三种 Archive Object 展示密度，以及克制的 hover／focus 交互边界。
- 未知项：当前站点实现与文章规则是否完全一致、是否存在后续迭代。
- 处理：使用现有 MDX；实现一致性属于单独的工程审查，不由 OpenPaw判断。

## 6. 可采用的显式关系

以下关系直接来自当前 MDX 的 `related`，已排除 OBS-X 和 future 对象：

- `digital-space-essay` → `linear-algebra-notes`
- `digital-space-essay` → `market-signal-format`
- `market-signal-format` → `self-hosted-layers`
- `nas-agent-project` → `linear-algebra-notes`
- `nas-agent-project` ↔ `self-hosted-layers`
- `nas-agent-project` → `container-network-failure`
- `self-hosted-layers` → `container-network-failure`

OpenPaw 基于“同属排错”“共享基础设施”或“主题相似”补充的关系不进入 Atlas，除非以后写回 MDX 的 `related`。

## 7. 新内容候选

OpenPaw 找到两个有真实记录支撑、且有机会独立成文的候选。它们目前都不是 Atlas 节点。

### 7.1 Cloudflare Tunnel 故障排查方法

- 事实基础：存在完整的真实排查记录和修复结果。
- 独立价值：聚焦边缘隧道层，与容器内部网络故障属于不同层次。
- 建议 schema：`type: failure`、`field: systems`、`status: archived`。
- 公开前要求：删除域名、标识、地址、令牌和内部拓扑；由作者确认日期和最终结论。
- 状态：候选，尚未建立 MDX。

### 7.2 MCP Streamable HTTP 接入陷阱

- 事实基础：存在实际接入与排错记录。
- 独立价值：聚焦协议会话、请求头和传输行为，不等同于 NAS Agent 或自托管分层文章。
- 建议 schema：暂定 `type: failure`、`field: systems`、`status: stable`。
- 公开前要求：对照当时采用的官方 MCP 协议版本核验；协议版本变化必须明确标注。
- 状态：候选，尚未建立 MDX。

OpenPaw 为候选给出的 `pattern / note / devops / integration / evergreen` 不属于项目 schema，已拒绝。候选只有在作者确认并写成公开 MDX 后才会自动进入 Atlas。

## 8. 第二阶段执行边界

第二阶段已执行：

- 从七个现有公开 MDX 生成真实索引。
- 用六个 `field` 建立轨道，用 `type`、`status`、阅读时间和 `related` 生成视觉映射。
- 已删除 12 个占位节点和禁用的占位文章入口。
- 保持 OBS-X、draft、future/unknown 占位内容不进入 Atlas。

第二阶段不执行：

- 不改写现有文章正文。
- 不根据 OpenPaw 回答新增公开事实。
- 不自动创建两篇候选文章。
- 不根据文本相似度生成关系线。

## 9. 仍需作者决定的内容问题

1. `nas-agent-project` 保持“工具如何进入我的工作流”的方法论文章；NAS Hardware Agent 是否以后另建独立对象。
2. “每日三个数字”的一个月实验是否完成，以及是否需要新建后续报告。
3. 两个新增候选是否进入后续写作计划。

这些问题不会阻塞七个现有对象的 Atlas 接入。
