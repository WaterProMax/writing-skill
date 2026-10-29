# Codebase Knowledge-Base Generation Workflow (`codebase-knowledge-base-workflow.md`)

## Purpose & Role in the Unified Writing Skill

This workflow governs **Mode 1 (Knowledge-Base Generation)** and serves as the **Investigator's structured fact-indexing phase** for **Mode 4 (End-to-End Pipeline)**.

> **Governance Bridge Rule (Crucial)**:
> The `7 + 1` knowledge-base structure (`HOME.md` + `01` through `07`) is an **internal Investigator index** designed for fast fact lookup, cross-referencing, and code verification. Default `canonical_for` is **empty**.
> - **When the deliverable IS a local codebase knowledge base (Mode 1)**: Output the `HOME.md` + `01`..`07` files directly with full class names, **this-run** line counts, table fields, and issue statuses. If the target repository already has a Canonical Wiki, the index opening paragraph **must** link to that Wiki and declare that this index does **not** replace it.
> - **When the deliverable is a formal reader-facing document (Mode 2 / Mode 4, e.g., competition proposal, architecture whitepaper, research report)**: Treat the knowledge base as the canonical **Evidence Profile** index—never copy the `01`..`07` module catalog as the formal document's chapter outline (`Source gravity`), and never copy raw `ISSUE-xxx` defect logs into formal prose without passing the **Claim Necessity Test** (`references/decision-rules.md` §9).

### Mode 1 reading set (do not expand)

Mode 1 **must** read only:
1. This file (`codebase-knowledge-base-workflow.md`)
2. `references/core-model.md` — the five canonical objects (`Artifact Brief`, `Claim Record`, `Evidence Profile`, `Narrative Decision`, `Boundary Record`)
3. `references/decision-rules.md` — **§9 Claim Necessity Test** only

Do **not** load `examples.md`, `document-architecture.md`, or `audit-workflow.md` for Mode 1. Those belong to Mode 2/3. Do **not** treat Mode 1 as the Deep routing table.

### Conflict priority (always)

When sources disagree, apply this order and record the loser in `07` when relevant:

`running code > Flyway/entities > generated OpenAPI > Wiki non-canonical prose > test notes > experiment directories`

Example: if `API_ROUTE_MATRIX.md` says 404 but a Controller mapping exists, the Controller wins; note “手记状态未改，源码已变”.

### Red lines (Mode 1)

- Do **not** copy passwords, connection strings, test-account secrets, tokens, or full JDBC URLs into the knowledge base (name the config key / env var only).
- Do **not** paste template percentages or placeholder SLAs as measured metrics.
- Do **not** describe a CLI or batch job as a listening HTTP service until a bind is found (`ListenAndServe`, port listen, similar). Prefer “CLI / offline tool” when absent.
- Empty Controllers (class-level `@RequestMapping` only, **0** handler methods) are **not** APIs — list them as generator shells if needed.
- Keep **Java property names** separate from **physical column names**. Without `@TableField` / explicit DDL, do **not** invent snake_case columns; say “物理列名未在注解中声明”.
- `@Value` / code defaults are **not** the same as YAML placeholder defaults — record both when they differ.
- Directory ownership: treat third-party trees (e.g. upstream embedding kits), experiment-family directories (e.g. a `product-analysis/`-style tree), and full-chain notes (e.g. a `full-chain-testing/`-style tree) as **evidence / experiment**, not as live product specs or online services, unless running code proves otherwise. Those directory names are illustrative.
- **Controller 与入口扫描范围先全仓库再按目录所有权拆分**：扫描注解（如 `@RestController` / `@RequestMapping` / `go.mod`）时先扫全仓库，再按目录所有权拆分为「主产品进程」与「独立工具/采集进程（如 `tools/**`）」，既不漏扫工具进程，也不把工具进程的接口混入主产品 API 表。
- **前端请求字面量提取必须跟进本地包装函数**：提取 API 调用路径时，除了直接搜 `fetch(` / `axios`，必须先识别**本仓库自己的**本地封装函数（e.g., custom wrapper functions such as `apiClient` / `request` / `schoolFetch`），对包装函数调用一并提取；未跟进的包装调用只能记入「未覆盖」，严禁写出「前端无某模块 API」的否定结论。`apiClient` / `request` / `schoolFetch` 只是包装函数举例，不是每个仓库都必须存在的客户端。
- **符号表自带「非运行时行为契约」声明**：每张由注解/静态扫描生成的符号表（Controller 映射表、实体表、前端 API 路径表）表头或首段必须带一句固定提示：「本表仅证明符号/映射在源码中存在，不代表方法体分支、鉴权或运行时业务契约已验证」，防止下游 Mode 2 直接把符号表当成已验证的产品功能写进正式文档。

---

# 代码库知识库生成方法

## 适用场景

当你需要为大型多模块代码库生成一份详细的、可用于后续文档撰写的本地知识库（Investigator 索引）时，使用本方法。

## 方法概览

本方法的核心思想是**广度优先探索 → 并行深度挖掘 → 结构化输出 → 迭代补充**，而不是顺序地逐个文件阅读。

```
阶段 1: 全量结构探索（1 个 Agent）
    ↓
阶段 2: 并行模块分析（4+ 个后台 Agent，可覆盖声明）
    ↓
阶段 3: 同步读取关键文件（主对话，不等 Agent；含清单失效）
    ↓
阶段 4: 结构化文档输出（7 个专题文件 + 1 个索引）
    ↓
阶段 5: 迭代补充（Agent 延迟返回后定点 edit；或「阶段 5 增补」）
```

## 阶段 1: 全量结构探索

**目标**: 5 分钟内获得项目全貌

**使用单个 Explore Agent**，指令要点：
- 列出所有顶级目录和 2 级深度
- 识别所有主要模块（前后端、AI、工具、脚本）与**目录所有权**（实现 / 实验 / 上游第三方 / 测试手记 / 交付物）
- 找到所有配置文件（pom.xml、package.json、go.mod、requirements.txt、Dockerfile 等）
- 列出所有文档文件（*.md、*.txt、*.docx）及 Wiki / `AGENTS.md` 入口
- 统计代码行数（**必须来自本次 `wc` / 工具统计，不得沿用技能示例中的行数**）

**输出**: 项目结构树 + 模块分类 + 文件清单 + 目录所有权标注

## 阶段 2: 并行后台 Agent 分析

**关键技巧**: 使用 `run_in_background: true` 并行启动多个 Agent，同时深入分析不同模块。

### Agent 分工策略

```
Agent 1: 后端与独立工具进程源码结构
  - 先全仓库扫描 `@RestController` / `@RequestMapping` / `go.mod` 等入口，再按目录所有权拆分为「主产品进程」与「独立工具/采集进程（如 `tools/**`）」（既不漏扫 `tools/**` 等独立进程，也不混入主产品 API 表）
  - 列出所有包下的所有类名
  - 每个 Controller 的 URL 映射（跳过方法数为 0 的空壳；表头附非运行时契约声明）
  - 每个 Service 的职责
  - pom.xml 依赖分析

Agent 2: 前端源码结构
  - 先探测栈：有无 vue-router / Pinia / Vuex；无路由表时写「无路由表」，不要发明 routes
  - 组件 props/events/methods（按实际栈书写；可为 reactive() 组合式状态）
  - 每个 service 的 API 调用：除直接搜 `fetch(` / `axios` 外，必须先识别本仓库自己的本地包装函数（e.g., custom wrapper functions such as `apiClient` / `request` / `schoolFetch`）并一并提取；未跟进的包装调用只能记入「未覆盖」，严禁写出「前端无某模块 API」的否定结论。这些名字只是举例。
  - package.json 依赖分析

Agent 3: AI 服务 + 工具脚本 + SQL
  - Go / Python：先判定进程模型（监听 HTTP vs CLI/批处理）
  - 数据库迁移文件
  - 评测脚本；实验目录只索引家族名，不升格为在线能力

Agent 4: 数据库 Entity + Mapper + DTO
  - 实体与表：`@TableName` / Flyway 为准
  - 属性名与物理列名分列；无 `@TableField` 不臆造列名
  - MyBatis XML SQL 查询
  - DTO 字段和用途
```

### Agent 指令约束（可覆盖声明；禁止要求无差别通读全库）

每个探索 Agent **必须**在回报中输出三块清单：

1. **已列全的符号** — 类 / 路由 / 表 / 关键函数等枚举结果（允许来自目录扫描 + 注解提取）
2. **已通读的文件** — 真正打开并读完正文的路径
3. **明确未读的文件** — 已知存在但未通读的路径

硬约束：
- **未读文件不得出现在“行为”句子里**（不得写该文件“如何处理请求/如何落库”等）。未读只可出现在「未覆盖」清单。
- 要求 `document: purpose, parameters, return types` **仅针对已通读范围**。
- 标注后台运行: `run_in_background: true`。
- 若并行 Agent 无法在本回合返回：允许主会话做**结构化提取**（注解、映射、`fetch` 字面量），但提取逻辑必须处理「注解与 javadoc / 注释不相邻」等情况，避免漏掉 Controller。

## 阶段 3: 同步读取关键文件

在后台 Agent 运行时，主对话不闲置。**先读治理入口，再读技能示例清单。**

### 优先入口

1. `AGENTS.md` / 等价代理入口
2. Wiki repository map / `canonical_for` 索引（若存在）
3. 再按下方提示清单取材料

### 提示清单（示例文件名，非硬编码必读集）

| 类别 | 示例文件名 | 用途 |
|------|------------|------|
| 项目上下文 | `PROJECT_CONTEXT.md` / `AGENTS.md` / `QWEN.md` | 治理与模块边界 |
| 配置清单 | `功能模块.md`（若有） | 模块鸟瞰 |
| 技术配置 | `application.yml`、`pom.xml`、`package.json` | 端口、配置键（不含口令原文） |
| 测试体系 | `ISSUES.md`、`TEST_REQUIREMENTS.md`、`API_ROUTE_MATRIX.md` | 手记与矩阵（须再对源码） |
| AI 提示词 | `AI_PROMPTS.md` | 现行提示词索引 |
| 状态管理 | `store/app.js` 等 | 前端状态 |

### 清单失效（必做）

对上表**每一个**示例文件名：

- **若存在**：按路径读取，并用于合成。
- **若缺失**：立即查 `AGENTS.md` 与 Wiki repository map（或迁移说明），记录**新路径**或记为 **Boundary（已删除/未提供）**。
- **禁止**用归档目录或其他历史树中的**同名文件**充当现行实现或现行提示词（e.g. a `legacy-designs` archive）。目录名只是举例。
- 行数、矩阵结论、ISSUE「已修复」等：**必须以本次工具统计与源码抽查为准**；**不得沿用本技能文本里的示例行数或示例状态**（例如不得照抄技能或旧索引里的绝对行数）。

手记与矩阵冲突时，遵守全局 **Conflict priority**；Mode 1 抄录 ISSUE 状态时用**手记原词**（如「已修复 / 已确认 / 已作废」），不要擅自改成技能示例里的二元「已修复/未修复」。
- **手记状态抽查方式明确化**：抽查 `ISSUES.md` / 测试手记状态时，定义为「打开手记点名的源文件核对当前代码实现（并在文中注明未启动进程重跑）」；至少对每类状态抽查一条，抽查与原词不一致时**两个都写**。
- 若未打开对应源文件，必须写「未打开源码核对（仅保留手记原词）」，严禁把未打开写成“仍破损”或“已修复”。

## 阶段 4: 结构化文档输出

### 与 Canonical Wiki 共存

- 默认输出目录：`docs/knowledge-base/`（任务另有指定除外）。
- 产物是 Investigator 索引，`canonical_for` 为空。
- 若仓库已有 Wiki：在 `HOME.md`（及各文件如需要）**首段**放置 Wiki 入口链接，并声明「本目录不替代 Canonical Wiki」。

### 文件组织原则

不要把所有内容写入单个文件。按主题拆分为 7 个文件：

| # | 文件 | 受众 | 核心内容 |
|---|------|------|---------|
| 1 | `01-overview-architecture.md` | 所有人 | 项目定义、设计理念、技术栈、模块清单、仓库结构 |
| 2 | `02-frontend-analysis.md` | 前端开发 | View/Component/Service、实际状态方案、键名规范、UI 系统 |
| 3 | `03-backend-analysis.md` | 后端开发 | Controller/Service（排除空壳 API）、核心 Service 源码级分析 |
| 4 | `04-database-go-tools.md` | 数据工程 | 表与字段（属性/列分列）、迁移、Go CLI、向量库、评测 |
| 5 | `05-business-flows-testing.md` | QA/架构 | 核心业务链路、测试架构、设计规范 |
| 6 | `06-ai-prompts-analysis.md` | AI 工程 | 提示词体系、产品分析实验（标明实验非规格） |
| 7 | `07-issues-configuration.md` | 运维/PM | 问题追踪（原词+抽查）、环境变量名、构建命令、端口 |

另创建 `HOME.md` 作为总索引，包含按角色和按模块的快速导航表。

### 编写原则

1. **具体，不泛泛** — 列出已覆盖范围内的类名、表名、字段；未覆盖单独成节
2. **有数字，有行数** — 行数必须来自**本次** `wc`/工具统计，不得沿用技能示例
3. **标注状态用原词** — 抄录手记状态原词，并做每类至少一条抽查；不一致则双写
4. **交叉引用** — 前端 View → 后端 Controller → 数据表之间建立关联
5. **使用表格并附非运行时契约声明** — 大量信息用表格呈现；每张由注解/静态扫描生成的符号表（Controller 映射表、实体表、前端 API 路径表）表头或首段必须带固定提示：「本表仅证明符号/映射在源码中存在，不代表方法体分支、鉴权或运行时业务契约已验证」
6. **面向写文档的人** — 他们需要的是对接关系与字段事实，而不是把 `ISSUES.md` 整份搬进附录（先过 Claim Necessity）
7. **遵守红线** — 口令、空壳 API、臆造列名、把 CLI 写成 HTTP 服务、漏跟进前端包装函数而下否定结论等一律禁止

### HOME 模块导航（占位规则）

```
HOME.md (索引 + 快速导航)
  ├── 按角色导航: 新人/后端/前端/AI/测试/架构（按仓库实际角色裁剪）
  ├── 按模块导航: 从 workspace 视图名与 Controller 前缀归纳；
  │                 模块名必须在代码或 Wiki canonical 页出现
  │                 （不要写死其他项目的模块名；「用户系统/画像/简历」只是反例，不是本技能的默认模块）
  └── 7 个知识库文件（每个独立可读）
```

## 反模式（避免）

- ❌ 顺序读取几百个源文件 — 用 Agent 并行，并做可覆盖声明
- ❌ 单个大文件包含所有内容 — 拆分为 7 个专题
- ❌ 只写"见源码" — 必须写清楚具体类名、表名、字段（在已读范围内）
- ❌ 把知识库写成代码注释 — 受众是写文档的人，不是读代码的人
- ❌ 等所有 Agent 完成再开始写 — 边等边读，读够就开始写
- ❌ 清单缺失时回退 legacy 同名文件 — 记 Boundary 或查 Wiki 新路径
- ❌ 把实验目录 / 上游第三方 / 测试手记写成现行在线能力

## 阶段 5: 迭代补充（Agent 延迟返回）

### 为什么需要阶段 5

后台 Agent 的完成时间不可预测。部分 Agent 可能需要 2-5 分钟甚至更长。如果你在阶段 3 同步读取到足够的核心信息，不应等待所有 Agent 完成再开始写入——应该在读取到关键文件后立即开始结构化输出。

### 会话模型承认与固定占位句

若运行环境里后台 Agent **只能在回合结束后**把结果返回主会话：

1. 允许先提交「**主会话覆盖范围**」版本（写明已覆盖 / 未覆盖）。
2. 当后台探索尚未返回时，在固定标题 `## 阶段 5 增补` 下必须使用固定占位句：

```markdown
## 阶段 5 增补

占位：后台探索尚未回传，以下仅为主会话已核对范围。
```

3. 后台返回后删除该占位句并插入增量；**不要**要求边空等边改，也不要为了等 Agent 而阻塞首次提交。

**Agent 返回后的处理策略与二次核验门槛**：

1. **不重写整个文件** — 使用 `edit` 工具对已有文件进行定点插入/替换
2. **补充而非覆盖** — Agent 返回的信息应是"增量细节"而非"全新内容"
3. **合并到对应章节** — 后端 → `03`；数据库 → `04`；并再次对照 Conflict priority
4. **二次核验门槛（严禁盲信子 Agent）** — 子 Agent 自称“已通读”不等于主会话已核验。**后台返回稿中的默认主机/口令、注释列名、未经主会话打开源文件核对行号的方法体行为描述，严禁原样贴入**；调查稿若把无 `@TableField` 的属性自动写成物理列名，或把无品牌字面量的 URL 写成某向量库品牌，索引一律不得采纳

### 操作模式

```text
阶段 3 同步读取（治理入口 → 清单失效处理后的现行文件）
    ↓
立即开始阶段 4 写入（标注主会话覆盖范围）
    ↓
后台 Agent 陆续返回 → 阶段 5: 定点 edit，或统一写入「阶段 5 增补」
    ↓
最终 verify: 本次 wc/工具统计 + 未覆盖清单 + 红线自检
```

### 关键反模式避免

- ❌ 等待所有 Agent 再写 — 信息已经够用，等待是浪费
- ❌ Agent 返回后重写整个文件 — 会丢失之前的编辑结构
- ❌ 丢弃 Agent 的"非核心"细节 — 在已读前提下，字段与 Mapper 清单仍有价值
- ❌ 要求边等边改而无法交付 — 先交主会话版，再用「阶段 5 增补」

## 适用项目规模

- 全栈项目（前后端 + 数据库 + AI 工具/服务）
- 50+ Controller / 10+ 页面 / 100+ 表
- 有 `AGENTS.md` / Canonical Wiki / `PROJECT_CONTEXT.md` 更好（没有也可，但清单失效规则仍适用）

---

## 阶段 6: 与证据治理及代码核验的衔接（Unified Skill 协同规范）

当生成的知识库用于支撑后续正式文档撰写（Mode 2）或代码一致性核验（Mode 3）时，必须在各专题文件中确保以下可追溯锚点完备：

| 知识库文件 | 支撑的证据治理对象 (`core-model.md`) | 支撑的代码核验断言类型 (`code-verification-workflow.md`) |
|---|---|---|
| `01-overview-architecture.md` | `Artifact Brief`（技术栈、模块边界、主贡献定位） | 模块归属与系统职责边界核验（防偏差 1：跨系统归因错位） |
| `02-frontend-analysis.md` | `Engineering` / `Product` 证据（视图、交互状态、API 对接） | 前端状态流转、组件交互与接口调用核验 |
| `03-backend-analysis.md` | `Engineering` 证据（Controller/Service、同步/异步链路、状态枚举） | 状态机完整性（防偏差 2）、同步/异步返回值（防偏差 3）、工程门禁（防偏差 4） |
| `04-database-go-tools.md` | `Engineering` / `Research` 数据底座（Entity/表结构、向量库、评测工具） | 表名、字段名、持久化结构与离线/在线工具链路核验 |
| `05-business-flows-testing.md` | 端到端业务闭环链路与自动化测试证据（`Automated test` / `Runtime`） | 端到端数据流向、调用主链路 vs 辅助链路区分 |
| `06-ai-prompts-analysis.md` | `Research` / `Engineering` AI 能力边界与提示词策略 | AI 候选生成 vs 工程校验层（gate/validator/converter）边界核验（防偏差 4） |
| `07-issues-configuration.md` | `Boundary Record` 候选池与运行环境配置（`Appendix` / `Reproducibility`） | 手记原词状态 + 源码抽查（仅在通过 Claim Necessity Test 时进入正式正文） |
