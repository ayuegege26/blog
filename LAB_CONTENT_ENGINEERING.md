# Ayue Observatory Lab Content Engineering

> 阶段：第三步／具体内容工程。
>
> 状态：v0.2.0 首版已实现。本文档同时作为 Lab 首发内容、项目关系、NAS 数据接入契约和开发验收边界的维护基线。

## 1. 首版内容目标

Lab 首版用两个独立项目证明两种核心能力：

1. `Temporal Field／时间景观`：完全在浏览器运行的高级动态前端。
2. `NAS Constellation／NAS 星图`：读取周期更新的真实 NAS 数据并形成可探索的动态观察。

二者不共享页面模板，也不要求视觉一致。它们只共享 Lab 导航、运行状态语义、可访问性底线和项目生命周期约定。

首版不实现：

- NAS 写操作或远程控制。
- 登录、账户和私人项目。
- 任意代码执行。
- 秒级公网实时监控。
- Lab 搜索、筛选和项目管理后台。
- 第三个正式项目。

## 2. 内容关系

```text
Lab
├── Visual Systems
│   └── Temporal Field
└── NAS Observatory
    └── NAS Constellation
```

首版 Lab 首页只展示已经存在的两个板块，不公开空的 `Interactive Works` 入口。

开源项目不是独立可见板块。第三方技术可以作为实现来源，但必须记录上游、许可证、修改和安全边界。

## 3. 共同项目责任

每个公开 Lab 项目必须提供：

- 项目名称和一句话目的。
- 进入后立即可理解的主舞台。
- 简短操作说明。
- 加载、运行、暂停、错误和降级状态。
- 重置或重新开始方式。
- 返回 Lab 与 Observatory 的路径。
- 桌面端和移动端行为。
- reduced-motion 行为。
- 技术或数据限制说明。

这些是信息责任，不形成统一视觉模板。

## 4. Temporal Field／时间景观

### 4.1 项目定位

Temporal Field 是一个随时间持续变化的浏览器生成环境。它不展示 NAS 数据，也不模拟监控状态。时间本身是输入，视觉系统是输出。

它用于证明 Lab 可以容纳纯粹、高完成度的动态前端，同时保持明确规则，而不是成为随机特效。

### 4.2 核心观察问题

> 如果页面不是播放一段固定动画，而是根据时间、停留和输入持续演化，它能否形成一种可被观察的数字环境？

### 4.3 时间输入

首版使用本地浏览器时间：

- 当前小时影响主色温与空间明暗。
- 分钟推进整体场的缓慢演化。
- 秒只用于局部细微变化，不承担快速闪烁。
- 页面停留时间影响系统复杂度或密度。
- 日期生成当天稳定 seed，使同一天具有可识别但不完全固定的状态。

不上传访问时间、设备信息或交互记录。

### 4.4 视觉构成

建议包含：

- 一个持续演化的场。
- 一组有规则的粒子、线、面或光点。
- 时间状态的低调文字层。
- 输入对局部空间的扰动。
- 可切换的观察强度或视角。

视觉不能包含：

- 高频闪烁。
- 无法停止的快速镜头移动。
- 伪装为 NAS 或实时系统数据的随机数值。
- 与实验规则无关的技术 Logo 和性能炫耀。

### 4.5 交互

首版支持：

- 鼠标或触控产生局部扰动。
- 暂停／继续。
- 重置为当前时间 seed。
- 切换低、中、高三档视觉密度。
- 显示或隐藏规则说明。

暂不支持：

- 用户账户和云端保存。
- 上传素材。
- 导出视频。
- 多人同步。

### 4.6 技术边界

- 首版以 WebGL 作为主要实现，并提供 Canvas 2D 降级。
- 不提供纯静态视觉降级；只有 WebGL 与 Canvas 都不可用时才进入 `unsupported` 说明状态。
- 动画循环在页面不可见时暂停或显著降频。
- 离开页面时释放 animation frame、事件监听和图形资源。
- reduced-motion 默认进入低密度、低速度模式，并提供完全暂停。

### 4.7 状态

项目状态至少包括：

- `loading`：资源初始化。
- `running`：正常演化。
- `paused`：用户暂停。
- `reduced`：低动态模式。
- `unsupported`：设备不支持主要渲染能力。
- `error`：初始化或运行失败。

### 4.8 首版验收

- 进入页面后无需说明即可看到系统正在演化。
- 时间变化与视觉变化存在可解释映射。
- 鼠标、触控、暂停、重置和密度切换可用。
- 后台标签页不会持续高负载渲染。
- reduced-motion 和不支持 WebGL 的设备有明确行为。
- 不依赖 NAS、Cloud 或在线 API。

## 5. NAS Constellation／NAS 星图

### 5.1 项目定位

NAS Constellation 把经过脱敏的 NAS 系统、服务和状态关系表现为可观察的星图。

它不是运维后台。它不提供管理按钮、告警确认和故障操作，而是回答：一个长期运行的个人系统由哪些部分组成，它们如何保持活跃，又如何随时间改变？

### 5.2 核心观察问题

> 能否把真实基础设施从指标面板重新表达为一个具有层级、关系和时间感的观察对象？

### 5.3 首版内容

首版展示：

- NAS 整体公开状态。
- 存储使用比例和近期变化。
- CPU、内存和温度的小时聚合。
- 人工设置别名后的服务节点。
- 服务所属类别和公开依赖关系。
- 最近备份结果。
- 数据生成时间、过期时间和来源状态。
- 最近 24 小时与 7 天的聚合历史。

首版不展示：

- 文件名、目录和个人文件活动。
- 内网地址、端口、容器真实名称和设备序列号。
- 原始日志、环境变量和挂载路径。
- 精确到秒的用户活动。
- NAS 管理操作。

### 5.4 星图映射

建议映射：

- 节点：公开服务或系统类别。
- 节点位置：类别和人工定义的关系，不由实时负载随机改变。
- 节点大小：服务相对权重或资源等级，使用稳定分级。
- 节点亮度：最近聚合状态或可用性。
- 呼吸速度：更新活跃度，必须保持低频。
- 连线：可选。只有存在明确、可验证且人工确认的公开依赖关系时才显示；首版不要求提供。
- 背景环境：存储、负载或温度的整体区间。
- 节点暗淡：离线、未知或数据过期，不使用强烈红色告警。

所有映射必须在项目说明中可查询，避免视觉含义随意变化。

### 5.5 交互

首版支持：

- 选择节点查看公开详情。
- 切换当前、24 小时和 7 天。
- 播放或拖动聚合历史。
- 显示节点类别、状态、最近更新时间和趋势摘要。
- 暂停动画和重置视图。
- 切换低密度模式。

不允许：

- 启停容器。
- 执行任务。
- 修改 NAS 配置。
- 查看原始日志。
- 通过浏览器访问内部管理接口。

### 5.6 数据更新

- 默认每小时生成一次公开快照。
- `staleAfterSeconds` 默认设置为 `7200`，即两小时未更新后标记过期。
- 如果整套项目部署在 NAS 本机，可以在独立工程评审后启用真正实时或高频更新。
- 实时模式必须使用相同公开 schema，不允许切换为直接读取管理接口。
- 24 小时历史建议使用 1 小时粒度。
- 7 天历史建议使用 3 小时或 6 小时粒度。
- 更长期数据不进入首版。

### 5.7 已确认的公开精度

- 允许公开精确的 `uptimeSeconds`。
- 允许公开精确的 `temperatureCelsius`。
- 允许公开精确的 `backup.lastCompletedAt` 和备份结果。
- 这些字段仍只能来自公开快照，浏览器不能为获得精确数据而直连 NAS 管理接口。

## 6. NAS 接入总体规范

### 6.1 接入方向

```text
NAS / Cloud Sources
        ↓
Collectors
        ↓
Sanitized Snapshots
        ↓
Lab Data Gateway
        ↓ HTTPS / JSON
NAS Constellation Frontend
```

Collectors 主动读取内部数据并输出公开快照。公开前端只访问 Data Gateway。

### 6.2 接入模式

首版采用匿名、只读、同源或明确允许来源的 HTTPS JSON 接口。

要求：

- `Content-Type: application/json; charset=utf-8`
- UTF-8 编码。
- 所有时间使用 ISO 8601 UTC，例如 `2026-07-13T01:00:00Z`。
- 所有数据结构包含 schema 版本。
- 数值单位固定，不由前端猜测。
- `null` 表示当前无有效值；不得用 `0` 代替未知。
- 字段名使用英文 `camelCase`。
- 公共 ID 使用稳定、非敏感的小写 kebab-case。
- 响应可以 gzip / Brotli 压缩。

### 6.3 端点

建议首版端点：

```text
GET /api/lab/v1/manifest
GET /api/lab/v1/nas/snapshot
GET /api/lab/v1/nas/history?range=24h
GET /api/lab/v1/nas/history?range=7d
```

端点职责：

- `manifest`：平台版本、可用项目、数据能力和更新时间。
- `snapshot`：最近一次公开 NAS 快照。
- `history`：指定允许范围的聚合历史。

首版只接受固定 `range=24h|7d`，不开放任意起止时间和任意粒度查询。

### 6.4 通用响应信封

所有成功响应使用：

```json
{
  "schemaVersion": "1.0",
  "generatedAt": "2026-07-13T01:00:00Z",
  "staleAfterSeconds": 7200,
  "sourceStatus": "ok",
  "data": {}
}
```

字段定义：

- `schemaVersion`：数据契约版本。
- `generatedAt`：该数据生成完成的 UTC 时间。
- `staleAfterSeconds`：从 `generatedAt` 开始计算的过期阈值。
- `sourceStatus`：`ok | partial | unavailable`。
- `data`：端点业务数据。

`partial` 表示部分数据源失败，但响应仍有可用数据；前端必须显示来源不完整。

### 6.5 Manifest 格式

```json
{
  "schemaVersion": "1.0",
  "generatedAt": "2026-07-13T01:00:00Z",
  "staleAfterSeconds": 7200,
  "sourceStatus": "ok",
  "data": {
    "labVersion": "0.1.0",
    "projects": [
      {
        "id": "temporal-field",
        "section": "visual-systems",
        "dataMode": "client-only",
        "status": "available"
      },
      {
        "id": "nas-constellation",
        "section": "nas-observatory",
        "dataMode": "periodic-snapshot",
        "status": "available"
      }
    ],
    "nasCapabilities": {
      "snapshot": true,
      "history24h": true,
      "history7d": true,
      "realtime": false
    }
  }
}
```

### 6.6 Snapshot 格式

```json
{
  "schemaVersion": "1.0",
  "generatedAt": "2026-07-13T01:00:00Z",
  "staleAfterSeconds": 7200,
  "sourceStatus": "ok",
  "data": {
    "system": {
      "id": "ayue-nas",
      "label": "Ayue NAS",
      "status": "online",
      "uptimeSeconds": 864000
    },
    "metrics": {
      "cpuUsageRatio": 0.18,
      "memoryUsageRatio": 0.63,
      "temperatureCelsius": 43.2
    },
    "storage": {
      "usedBytes": 8246337208320,
      "totalBytes": 13194139533312,
      "usageRatio": 0.625,
      "change24hBytes": 2147483648
    },
    "backup": {
      "lastCompletedAt": "2026-07-12T18:00:00Z",
      "lastResult": "success"
    },
    "services": [
      {
        "id": "knowledge-service",
        "label": "Knowledge Service",
        "category": "knowledge",
        "status": "online",
        "availabilityRatio24h": 0.998,
        "activityLevel": "medium",
        "dependsOn": ["storage-core"]
      },
      {
        "id": "storage-core",
        "label": "Storage Core",
        "category": "storage",
        "status": "online",
        "availabilityRatio24h": 1.0,
        "activityLevel": "low",
        "dependsOn": []
      }
    ]
  }
}
```

### 6.7 Snapshot 字段枚举

`system.status`：

- `online`
- `degraded`
- `offline`
- `unknown`

`services[].status`：

- `online`
- `degraded`
- `offline`
- `maintenance`
- `unknown`

`services[].category` 首版建议限制为：

- `storage`
- `knowledge`
- `automation`
- `media`
- `network`
- `development`
- `cloud`
- `other`

`activityLevel`：

- `idle`
- `low`
- `medium`
- `high`
- `unknown`

`backup.lastResult`：

- `success`
- `partial`
- `failed`
- `unknown`

### 6.8 History 格式

```json
{
  "schemaVersion": "1.0",
  "generatedAt": "2026-07-13T01:00:00Z",
  "staleAfterSeconds": 7200,
  "sourceStatus": "ok",
  "data": {
    "range": "24h",
    "resolutionSeconds": 3600,
    "points": [
      {
        "timestamp": "2026-07-13T00:00:00Z",
        "cpuUsageRatioAvg": 0.16,
        "memoryUsageRatioAvg": 0.62,
        "temperatureCelsiusAvg": 42.8,
        "storageUsageRatio": 0.625,
        "onlineServiceRatio": 1.0
      }
    ]
  }
}
```

规则：

- 点按 `timestamp` 升序。
- 缺失采样点不补零。
- 某字段无法计算时使用 `null`。
- `resolutionSeconds` 必须与实际聚合粒度一致。
- 24 小时最大 24–25 个点。
- 7 天首版最大 56 个点。

### 6.9 数值与单位

- 比例统一使用 `0–1` 浮点数，不使用 `0–100` 百分数。
- 存储和流量统一使用整数 bytes。
- 温度统一使用摄氏度。
- 时间长度统一使用整数 seconds。
- 时间戳统一使用 UTC。
- 前端负责将比例、bytes 和 UTC 转换为可读格式。

### 6.10 ID 与别名

- `id` 是稳定公开标识，不直接使用容器名、主机名或内部服务名。
- `label` 是人工确认可以公开的显示名称。
- ID 发布后尽量不变；需要变更时通过 schema 或迁移映射处理。
- `dependsOn` 是可选字段；存在时只能引用同一响应中存在的公开 ID。无法确认依赖关系时应省略，不能根据视觉需要猜测。
- 不通过 ID 暴露端口、IP、卷名、用户名和路径。

## 7. 缓存与传输

建议响应头：

```text
Cache-Control: public, max-age=300, stale-while-revalidate=3600
ETag: "<content-hash>"
Content-Type: application/json; charset=utf-8
```

说明：

- 数据每小时生成，但允许客户端在五分钟内复用缓存。
- `stale-while-revalidate` 允许接口短暂失败时继续使用旧数据。
- Data Gateway 应支持 `If-None-Match` 和 `304 Not Modified`。
- 前端仍必须根据 `generatedAt + staleAfterSeconds` 判断业务过期，不能只依赖 HTTP 缓存。

## 8. 错误格式

如果没有任何可返回的最后快照，接口使用合适 HTTP 状态码，并返回：

```json
{
  "schemaVersion": "1.0",
  "generatedAt": "2026-07-13T01:00:00Z",
  "error": {
    "code": "snapshot_unavailable",
    "message": "No public NAS snapshot is currently available.",
    "retryAfterSeconds": 3600
  }
}
```

公开错误不得包含堆栈、内部地址、路径、查询语句或服务端异常原文。

建议错误码：

- `snapshot_unavailable`
- `history_unavailable`
- `invalid_range`
- `schema_unavailable`
- `service_temporarily_unavailable`

## 9. 版本兼容

- URL 中的 `/v1/` 是接口主版本。
- `schemaVersion` 使用 `major.minor`。
- 新增可选字段只增加 minor。
- 删除字段、改变单位或改变字段语义必须增加 major。
- 前端忽略未知字段。
- 前端遇到不支持的 major 时停止数据映射并显示兼容性错误。
- Data Gateway 至少在一次正式 Lab 版本周期内保留旧主版本。

## 10. 脱敏与发布检查

Collectors 输出前必须执行允许列表，而不是只依赖禁止列表。

每次新增字段需确认：

- 是否为项目展示所必需。
- 是否可以推断内部地址、服务真实名称或个人活动。
- 是否需要聚合、区间化或延迟发布。
- 是否允许匿名公网访问。
- 是否需要历史保存。
- 是否需要从错误和日志中移除。

公开样本数据必须与真实 schema 一致，但不得包含真实敏感值。

## 11. 前端数据状态

NAS Constellation 必须区分：

- `loading`：首次请求尚未完成。
- `fresh`：数据仍在有效期内。
- `stale`：存在数据，但超过过期阈值。
- `partial`：部分来源失败。
- `empty`：接口正常但无公开节点。
- `unavailable`：没有快照可用。
- `incompatible`：schema 主版本不支持。
- `offline`：浏览器无法连接 Data Gateway。

状态不能只通过颜色表达。

## 12. 本地开发数据

项目必须提供：

```text
src/lab/fixtures/manifest.json
src/lab/fixtures/nas-snapshot.json
src/lab/fixtures/nas-history-24h.json
src/lab/fixtures/nas-history-7d.json
```

要求：

- fixtures 通过同一 schema 验证。
- 本地开发默认使用 fixtures。
- 连接真实接口必须显式启用。
- 测试覆盖 fresh、stale、partial、empty 和 unavailable。

fixtures 路径可以在实际工程阶段调整，但必须保留“无需真实 NAS 即可开发”的能力。

## 13. 实现顺序

### Phase 1：共同基础

- Lab 路由和专属导航。
- 项目运行状态语义。
- reduced-motion 与低性能检测。
- Lab 首页只展示两个首发项目。

### Phase 2：Temporal Field

- 先完成不依赖数据服务的动态项目。
- 验证 Lab 运行时、资源隔离和视觉自由度。

### Phase 3：数据契约与样本

- 将本文件中的接口格式转化为 schema。
- 建立 fixtures 和前端 Data Gateway 客户端。
- 在没有真实 NAS 接入时完成全部数据状态页面。

### Phase 4：Collectors 与 Data Gateway

- 在 NAS 建立允许列表采集。
- 输出 snapshot 和 history。
- 验证缓存、脱敏、过期和错误格式。

### Phase 5：NAS Constellation

- 实现星图映射、节点详情和历史回放。
- 接入真实小时快照。
- 完成降级、性能和隐私验收。

## 14. 首版完成标准

- Lab 首页只展示真实可访问项目。
- Temporal Field 可以独立运行、暂停、重置和降级。
- NAS Constellation 使用公开 Data Gateway，不直连 NAS 管理面。
- 接口、fixtures 和前端使用同一 schema。
- 快照每小时正常更新，并正确显示 stale。
- 24 小时和 7 天历史格式稳定。
- 响应中不存在禁止公开字段。
- 两个项目在桌面端和移动端可理解。
- Observatory 静态页面不加载 Lab 大型依赖。
- Lab 故障不影响 Observatory。
- build、数据 schema、路由、错误状态和资源释放通过验证。

## 15. 开发前决策状态

已确认：

- Temporal Field 以 WebGL 为主要实现，以 Canvas 2D 降级，不提供纯静态降级。
- 公开精确的 uptime、温度、备份完成时间和备份结果。
- Data Gateway 与静态站同域，使用 `/api/lab/v1/` 路径。
- NAS Constellation 使用本文列出的八个公开服务类别。
- 服务依赖连线是可选能力，首版不要求；只有关系明确、可验证且人工确认后才显示。

第三部分的内容与接入方向据此确认，可以继续拆分两个项目的正式实现文档。
