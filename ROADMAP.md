# ROADMAP.md

# Ayue Observatory Roadmap

## 首版目标

首版目标是建立 **Ayue Observatory / 个人观测站** 的核心身份、视觉系统和内容结构。

首版不追求复杂功能，而是要让访问者在第一屏理解：

- 这是一个长期运行的个人数字空间
- 内容围绕观察、研究、构建和记录展开
- 网站不是普通博客、NAS 站、运维后台或作品集模板
- Archive Object 是内容组织的核心语言

首版关键词：

- 高完成度首页
- 暗色观测站气质
- 对象化档案索引
- Markdown / MDX 内容系统
- 清晰可扩展的导航与数据模型

## 首版页面范围

首版页面：

- `/`：Observatory 首页
- `/archive`：Archive Object 总索引
- `/projects`：项目聚合页
- `/essays`：随笔与非技术内容聚合页
- `/about`：站点与个人说明
- `/archive/[slug]` 或内容详情页：对象详情页

首版导航：

- Observatory
- Archive
- Projects
- Essays
- About

Logo / 站点名必须可点击回首页。

## 首版必须实现

### 视觉与体验

- `Ayue Observatory` 首页首屏
- 左侧站点身份与概念描述
- 右侧 3 个轻量观测块：
  - Now Observing
  - Latest Object
  - Active Project
- 首屏底部 Object Strip
- 第二屏 Archive Objects 精选区
- 暗色视觉系统
- 杂志式排版与终端感元信息
- 移动端完整适配

### 内容结构

- Markdown / MDX + frontmatter
- Archive Object 类型：
  - essay
  - research
  - system
  - signal
  - project
  - failure
  - experiment
  - journal
- Archive 页面支持基础对象展示
- Projects 页面展示项目对象
- Essays 页面允许 essay / journal 类非技术内容
- 对象详情页保证长文阅读体验

### 工程基础

- 清晰组件结构
- 全局设计 token 或 CSS variables
- 可维护的内容模型
- 基础 SEO 信息
- 可扩展的静态占位数据

## 首版禁止实现

首版禁止：

- 真实 NAS 状态
- 真实金融数据
- 真实 Agent 状态
- WebGL
- 复杂关系图谱
- 复杂 CMS
- 过度 dashboard
- 服务器监控台式首页
- 企业 SaaS 式首页
- 过度玻璃拟态
- 廉价赛博朋克
- 大量发光边框
- 具体内网 IP
- 首页强突出代理、脚本、内网配置细节
- 以 NAS / 基础设施作为网站主定位

## 第二版再做

第二版可以考虑：

- 命令面板搜索
- Archive 过滤、排序和标签页
- 对象关系图谱
- 时间线视图
- Market Signal 静态日报索引
- Agent Job 历史记录
- 项目状态自动更新
- 文章内交互组件
- 代码块增强
- 轻量 Canvas 背景
- 多主题模式
- 首页状态数据构建时生成
- 对象之间的 related links 展示

第二版重点不是添加炫技效果，而是让 Archive Object 之间产生关系，并提高长期检索与阅读效率。

## 开发顺序

建议顺序：

1. 固化文档
   - `DESIGN.md`
   - `CONTENT_MODEL.md`
   - `ROADMAP.md`

2. 初始化项目
   - 选择静态生成友好的技术栈
   - 配置 Markdown / MDX 内容系统
   - 建立基础目录结构

3. 建立设计系统
   - 全局样式
   - 色彩 token
   - 字体层级
   - 卡片、标签、按钮、导航基础组件

4. 实现内容模型
   - 定义 frontmatter schema
   - 创建示例 Archive Object
   - 建立对象查询与排序逻辑

5. 实现首页
   - Hero
   - Now Observing / Latest Object / Active Project
   - Object Strip
   - Archive Objects 第二屏

6. 实现核心页面
   - Archive
   - Projects
   - Essays
   - About
   - Object Detail

7. 打磨体验
   - 移动端
   - hover / focus 状态
   - 阅读页排版
   - 基础 SEO
   - 性能检查

## 验收标准

首版完成时应满足：

- 首页第一眼能明确传达 Ayue Observatory 的个人观测站定位
- 首页不等同于普通博客列表
- 首页不呈现为 SaaS dashboard 或服务器监控台
- 导航清晰，Logo / 站点名可返回首页
- Archive Object 的视觉语言统一
- 至少有 6-8 个示例对象，覆盖多种类型
- Projects 与 Essays 作为一级入口有独立价值
- 中文表达自然，不像英文模板直译
- 长文阅读体验舒适
- 移动端无明显布局压缩或文本溢出
- 首版没有引入真实 NAS / 金融 / Agent 状态
- 首版没有 WebGL、复杂关系图谱或复杂 CMS
- 代码结构方便后续迭代
