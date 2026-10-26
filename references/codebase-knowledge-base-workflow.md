# Codebase Knowledge-Base Generation Workflow (`codebase-knowledge-base-workflow.md`)

## Purpose & Role in the Unified Writing Skill

This workflow governs **Mode 1 (Knowledge-Base Generation)** and serves as the **Investigator's structured fact-indexing phase** for **Mode 4 (End-to-End Pipeline)**.

> **Governance Bridge Rule (Crucial)**:
> The `7 + 1` knowledge-base structure (`HOME.md` + `01` through `07`) is an **internal Investigator index** designed for fast fact lookup, cross-referencing, and code verification.
> - **When the deliverable IS a local codebase knowledge base (Mode 1)**: Output the `HOME.md` + `01`..`07` files directly with full class names, line counts, table fields, and issue statuses.
> - **When the deliverable is a formal reader-facing document (Mode 2 / Mode 4, e.g., competition proposal, architecture whitepaper, research report)**: Treat the knowledge base as the canonical **Evidence Profile** index—never copy the `01`..`07` module catalog as the formal document's chapter outline (`Source gravity`), and never copy raw `ISSUE-xxx` defect logs into formal prose without passing the **Claim Necessity Test** (`references/decision-rules.md`).

---

# 代码库知识库生成方法

## 适用场景

当你需要为大型多模块代码库生成一份详细的、可用于后续文档撰写的本地知识库时，使用本方法。

## 方法概览

本方法的核心思想是**广度优先探索 → 并行深度挖掘 → 结构化输出 → 迭代补充**，而不是顺序地逐个文件阅读。

```
阶段 1: 全量结构探索（1 个 Agent）
    ↓
阶段 2: 并行模块分析（4+ 个后台 Agent）
    ↓
阶段 3: 同步读取关键文件（主对话，不等 Agent）
    ↓
阶段 4: 结构化文档输出（7 个专题文件 + 1 个索引）
    ↓
阶段 5: 迭代补充（Agent 延迟返回后定点 edit 增量细节）
```

## 阶段 1: 全量结构探索

**目标**: 5 分钟内获得项目全貌

**使用单个 Explore Agent**，指令要点：
- 列出所有顶级目录和 2 级深度
- 识别所有主要模块（前后端、AI、工具、脚本）
- 找到所有配置文件（pom.xml、package.json、go.mod、requirements.txt、Dockerfile 等）
- 列出所有文档文件（*.md、*.txt、*.docx）
- 统计代码行数

**输出**: 项目结构树 + 模块分类 + 文件清单

## 阶段 2: 并行后台 Agent 分析

**关键技巧**: 使用 `run_in_background: true` 并行启动多个 Agent，同时深入分析不同模块。

### Agent 分工策略

```
Agent 1: 后端 Java 源码结构
  - 列出所有包下的所有类名
  - 每个 Controller 的 URL 映射
  - 每个 Service 的职责
  - pom.xml 依赖分析

Agent 2: 前端源码结构
  - 每个组件的 props/events/methods
  - 每个 service 的 API 调用
  - 状态管理 store 的 state/getters/actions
  - package.json 依赖分析

Agent 3: AI 服务 + 工具脚本 + SQL
  - Go 代码、Python 脚本
  - 数据库迁移文件
  - 评测脚本

Agent 4: 数据库 Entity + Mapper + DTO
  - 所有实体对应的表结构
  - MyBatis XML SQL 查询
  - DTO 字段和用途
```

### Agent 指令约束

- 要求 `read EVERY file` 而非抽样
- 要求 `document: purpose, parameters, return types`
- 强调 `this is for a comprehensive knowledge base`
- 标注后台运行: `run_in_background: true`

## 阶段 3: 同步读取关键文件

在后台 Agent 运行时，主对话不闲置，同步读取：

1. **项目上下文文档** — PROJECT_CONTEXT.md / AGENTS.md / QWEN.md
2. **配置清单文件** — 功能模块.md（如果有）
3. **技术配置** — application.yml、pom.xml、package.json
4. **测试体系** — ISSUES.md、TEST_REQUIREMENTS.md、API_ROUTE_MATRIX.md
5. **AI 提示词** — AI_PROMPTS.md
6. **状态管理** — store/app.js 等核心状态文件

这些文件提供业务背景、问题上下文和配置细节——是合成知识库的关键材料。

## 阶段 4: 结构化文档输出

### 文件组织原则

不要把所有内容写入单个文件。按主题拆分为 7 个文件：

| # | 文件 | 受众 | 核心内容 |
|---|------|------|---------|
| 1 | `01-overview-architecture.md` | 所有人 | 项目定义、设计理念、技术栈、模块清单、仓库结构 |
| 2 | `02-frontend-analysis.md` | 前端开发 | 所有 View/Component/Service、状态管理、键名规范、UI 系统 |
| 3 | `03-backend-analysis.md` | 后端开发 | 所有 Controller/Service、核心 Service 源码级分析 |
| 4 | `04-database-go-tools.md` | 数据工程 | 全部数据表（字段级说明）、迁移、Go CLI、向量库、评测 |
| 5 | `05-business-flows-testing.md` | QA/架构 | 核心业务链路（端到端数据流）、测试架构、设计规范 |
| 6 | `06-ai-prompts-analysis.md` | AI 工程 | 提示词体系版本演进、产品分析实验 |
| 7 | `07-issues-configuration.md` | 运维/PM | 问题追踪、环境变量、构建命令、端口 |

另创建 `HOME.md` 作为总索引，包含按角色和按模块的快速导航表。

### 编写原则

1. **具体，不泛泛** — 列出每个类名、每个表名、每个字段
2. **有数字，有行数** — "HxView.vue（7748 行）"而非"HxView.vue"
3. **标注修复状态** — ISSUE-003 已修复/未修复，附修复方案
4. **交叉引用** — 前端 View → 后端 Controller → 数据表之间建立关联
5. **使用表格** — 大量信息用表格呈现，可扫描、易查阅
6. **面向写文档的人** — 他们需要的是"这个组件对接哪个 API、这个表有哪些字段"，而不是代码实现细节

### 信息的层级组织

```
HOME.md (索引 + 快速导航)
  ├── 按角色导航: 新人/后端/前端/AI/测试/架构
  ├── 按模块导航: 用户系统/画像/简历/规划/...
  └── 7 个知识库文件（每个独立可读）
```

## 反模式（避免）

- ❌ 顺序读取几百个源文件 — 用 Agent 并行
- ❌ 单个大文件包含所有内容 — 拆分为 7 个专题
- ❌ 只写"见源码" — 必须写清楚具体类名、表名、字段
- ❌ 把知识库写成代码注释 — 受众是写文档的人，不是读代码的人
- ❌ 等所有 Agent 完成再开始写 — 边等边读，读够就开始写

## 阶段 5: 迭代补充（Agent 延迟返回）

### 为什么需要阶段 5

后台 Agent 的完成时间不可预测。部分 Agent 可能需要 2-5 分钟甚至更长（如数据库层读 250+ 个文件）。如果你在阶段 3 同步读取到足够的核心信息，不应等待所有 Agent 完成再开始写入——应该在读取到关键文件后立即开始结构化输出。

**Agent 返回后的处理策略**：

1. **不重写整个文件** — 使用 `edit` 工具对已有文件进行定点插入/替换
2. **补充而非覆盖** — Agent 返回的信息应是"增量细节"而非"全新内容"
3. **合并到对应章节** — 后端 Agent 结果 → `03-backend-analysis.md`；数据库 Agent 结果 → `04-database-go-tools.md`
4. **标注补充内容** — 典型的补充：Entity 字段级映射、Mapper 自定义方法、Go CLI 的算法细节、DTO 的领域分组

### 操作模式

```text
阶段 3 同步读取核心文件（PROJECT_CONTEXT.md / 功能模块.md / application.yml / ISSUES.md 等）
    ↓
立即开始阶段 4 写入（此时已有充足信息覆盖 80%+ 内容）
    ↓
后台 Agent 陆续返回 → 阶段 5: 逐个 edit 补充细节
    ↓
Agent 全返回 → 最终 verify: wc -l + find 确认完整性
```

### 关键反模式避免

- ❌ 等待所有 Agent 再写 — 信息已经够用，等待是浪费
- ❌ Agent 返回后重写整个文件 — 会丢失之前的编辑结构
- ❌ 丢弃 Agent 的"非核心"细节 — Entity 表字段、Mapper 架构、SQL 脚本清单都是知识库受众需要的细节

## 适用项目规模

- 全栈项目（前后端 + 数据库 + AI 服务）
- 50+ Controller / 10+ 页面 / 100+ 表
- 有 PROJECT_CONTEXT.md 或类似上下文文档最好（没有也可）

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
| `07-issues-configuration.md` | `Boundary Record` 候选池与运行环境配置（`Appendix` / `Reproducibility`） | 已修复/未修复限制的真实状态核验（仅在通过 Claim Necessity Test 时进入正式正文） |
