# Technical Document Code Verification Workflow (`code-verification-workflow.md`)

## Purpose & Role in the Unified Writing Skill

This workflow governs **Mode 3 (Code Verification & Fact-Checking)** and the **Code-Truth Gate** in **Mode 2 / Mode 4**.
While `references/audit-workflow.md` audits macro-level argument structure, Claim-Evidence Contracts (`Research` vs `Engineering` vs `Product`), and Narrative Projection, this workflow performs **line-by-line source-code verification** of concrete technical assertions (table names, class/method names, state enums, sync/async behaviors, module attributions, and AI vs engineering boundaries) and produces **drop-in replacement prose**.

Mode 2 and Mode 3 load **this file** for the code-fact red lines below. Do not enter Mode 1 or open `codebase-knowledge-base-workflow.md` just to reach them. Mode 1 still enforces the same facts in its own workflow.

## Mode 2/3 code-fact red lines

Apply these whenever formal prose states a code fact, including a Scoped limitations memo:

- **Listen / bind.** Do not call a CLI, batch job, or client a long-lived HTTP service without `ListenAndServe` or an equivalent bind. A directory name, a `net/http` import, or an unreferenced URL in config is not a bind. See 偏差 5.
- **Empty Controller.** A class with only a type-level `@RequestMapping` and **0** handler methods is not an API.
- **Secrets and connection strings.** Do not copy passwords, tokens, connection strings, hosts, IPs, secrets, or full JDBC URLs into the body. Name the config key. When the sentence is about an infrastructure default, cite the **source line number** and the **category** only: loopback, public address, or empty DSN.
- **Java property ≠ physical column.** Without `@TableField` or explicit DDL, do not invent a snake_case column. Say the physical column is not declared on the annotation.

---

# 技术文档与代码一致性审查修订

## 适用场景

当你拿到一份已写好的技术文档（如比赛申报书、系统方案说明、技术白皮书），需要在提交前验证其中每一项技术描述与真实代码是否一致，并给出可直接替换的修正版本。

## 核心原则

### 逐行核验，不靠印象

文档中的每一句技术描述——表名、字段名、算法流程、架构关系——都必须用源代码验证。不能因为"之前读过代码"就假设某段描述是对的。

### 最低证据标准

每发现一处偏差，必须提供：
1. 文档原话（具体哪句）
2. 实际代码证据（文件路径 + 关键行）
3. 修正后的文本

### 保持文风，替换即用

输出必须是"直接复制粘贴进文档"的成品文字。不写"你需要把XX改成YY"这种指示性语言，而是直接给修改后的整段。

## 常见的五类偏差

下列典型案例、断言拆解和修正段里的模块名、表名、供应商名与状态常量只说明偏差长什么样。换仓库时以打开的源码为准。不要把这些标识符写进与之无关的项目。

### 偏差 1: 把 A 系统的技术特征错误归因到 B 系统

**典型案例**: 把"RAG 语义向量召回"说成学生技能标准化的能力，但实际代码中 RAG 只用于岗位重绘管线（`service/jobredraw/`），学生技能匹配走的是 `PortraitSkillProfileService.mapFeedbackEvidenceToSkills()` 中精确/别名匹配。

**检查方法**: 
1. 对文档中提到的每个技术组件（ChromaDB、Embedding、DeepSeek 等），grep 它在哪些 Service 中被调用
2. 如果文档说"A 模块用了 X 技术"，但 grep 发现 X 只在 B 模块中使用 → 偏差 1

### 偏差 2: 状态枚举/流程步骤被简化丢失

**典型案例**: 文档写面试状态机只有 6 个状态，代码中实际是 11 个状态（`STATE_POLICY_PROMPT` 中完整枚举）。

**检查方法**: 对文档中的流程描述，直接 read 对应的核心 Service 实现文件，比对状态枚举、步骤数量等。

### 偏差 3: 功能声称与实现不一致

**典型案例**: 文档写"面试结束后系统输出面试总结"，但代码中 `complete()` 返回 `reportStatus: "pending"`——面试总结是由异步评估链路生成的，不是同步返回。

**检查方法**: read 对应 Controller/Service 的响应 DTO 和 return 语句，比对文档声称的输出字段。

### 偏差 4: AI 能力边界被夸大

**典型案例**: 把 AI 的"候选建议"说成"最终结果"。比如技能匹配中 AI 只负责从候选池中选择，但文档可能写成 AI 直接输出技能标签。

**检查方法**: grep 对应 Service 中 AI 调用的上下游——AI 输出后是否有工程校验层（gate/validator/converter）再做最终决策。

### 偏差 5: 把批处理 CLI 客户端写成常驻 HTTP 服务

**典型案例**: 目录名叫 service，入口 import 了 `net/http`，配置里有一个没有任何引用点的端口或 URL，文档就把这条命令写成监听服务。启动函数里没有 `ListenAndServe`，也没有等价的端口绑定。

**检查方法**:
1. 打开该入口的 `main`（或等价启动函数），查找 `ListenAndServe` 或真正占用地址的绑定调用。
2. 目录名、`net/http`（或同类 HTTP 库）的 import、一份未被引用的 URL/端口配置，都不是监听证据。
3. 没有绑定，就写成 CLI / 批处理客户端，不要写成常驻 HTTP 服务。

**证据要求**: 正文中的「监听 / 常驻服务 / 端口开放」必须对应到绑定调用的文件与行号。没有绑定，这句话不能出现。

## 执行流程

### Step 1: 拆解文档为可核验的断言

把用户提交的文档段落拆成逐条技术断言，每条一句话。下面三条是拆解示例，表名与组件名不代表目标仓库：

```
断言 1: "系统将技能项保存至 biz_student_portrait_skill 表"
断言 2: "系统引入 DashScope Embedding 对技能文本向量化"
断言 3: "通过 ChromaDB 向量库进行相似技能召回"
...
```

### Step 2: 对每条断言做代码检索

对每条断言，grep 关键表名/方法名/技术名词：

```bash
# 核验"技能 X 使用了向量召回归因于 Y Service"
grep -r "embedding\|vector\|chroma" --include="*Service*.java"
# 确认技术组件出现在哪些 Service 中
```

### Step 3: 识别架构边界

当一个技术名词同时出现在多个模块时，区分：
- **哪个模块是主调用方**（业务主链路）
- **哪个是辅助/离线链路**（不参与在线业务）

然后比对文档的描述是否正确归因到了主调用方。

### Step 4: 提供修正文本

按照四个等级响应：

| 发现 | 动作 |
|------|------|
| 完全正确 | 不修改，告知用户"这段没问题" |
| 小偏差（术语不准、细节不全） | 在原段基础上润色增强 |
| 架构错误（技术归因错位） | 拆除错误归因，将技术描述移到正确的章节 |
| 夸大声明 | 降级为"代码实际能力"的表述 |

### Step 5: 输出修正版全文

不给"修改建议"（如"可以把第 3 行改成..."），而是直接输出可直接替换的完整段落。用户只需复制粘贴。

## 输出格式

```
原文问题：
- 问题1: [具体哪句描述错了]
- 问题2: [具体哪句描述错了]

修正版：
[完整的可直接替换的段落文本]
```

## 特殊处理：比赛文档

比赛文档在**章节职责是能力陈述**时需要额外注意：

1. **显式标注技术关键词**：RAG 的三层（Retrieval/Augmented/Generation）要分别点出
2. **避免过度谦逊**：如实写出技术实现，不添加"试图""尝试"等弱化词
3. **但不过度夸大**：代码做不到的事不承诺，特别是 AI 的行为边界
4. **表名不加引号包围**：直接用 `table_name` 而非"table_name 表"
5. **段落标题要体现技术深度**：用机制名而不是空泛功能名（e.g. 「检索–增强–生成链路」比「相关功能」更具体）。不要把其他项目的功能名（例如「简历」）写进与之无关的标题。

### 章节职责是 Boundary 时，本节约让路

当这一章的工作是边界或局限性（包括子系统局限性备忘录），不要用第 1、2、5 条来加宽主张：

- 不要为了点满 RAG 三层，把「没有查询入口」写成检索–增强–生成；
- 不要为了去掉「试图 / 尝试」而删掉边界句里必要的范围限定；
- 不要把标题改成能力宣传。

**优先级（显式）**: 偏差 4（AI 能力边界被夸大）和 `references/decision-rules.md` §9（含「子系统局限性备忘录」）高于本节的比赛文风。比赛文风只在章节职责是能力陈述时使用。Boundary 章节保持「可以写 / 不能写」，不把局限改写成能力。

## 与知识库生成的配合

如果项目已有知识库（如 `docs/knowledge-base/`），优先查知识库而非直接 grep 源码。知识库中已整理的 Entity 清单、Service 列表、API 路由矩阵可以加速 Step 2 的断言核验。

Scoped 局限性备忘录不为了这一步去建 `01`–`07`。没有知识库时，直接打开白名单里的源码行。已有知识库只加速检索；是不是监听服务，仍以打开的启动函数里有没有 `ListenAndServe` 或等价绑定为准。

---

## 与证据治理模型（Core Model）的映射关系

在联合执行「代码核验 + 证据治理审计」时，五类常见代码偏差直接对应 `references/audit-workflow.md` 与 `references/decision-rules.md` 中的标准诊断对象：

| 代码核验偏差类型 | 对应的治理根因 (`Root cause`) | 推荐处置动作 (`Narrative Decision`) | 严重度基准 |
|---|---|---|---|
| **偏差 1：把 A 系统的技术特征错误归因到 B 系统** | `Proof substitution` / `Source gravity` | `Restructure` / `Move`（拆除错误归因，移至正确模块章节） | **P0**（关键事实失真） |
| **偏差 2：状态枚举/流程步骤被简化丢失** | `Evidence-state overreach` / `Semantic-projection failure` | `Reframe` / `Substantiate`（补全真实状态语义与关键流转条件） | **P1** 或 **P2**（视是否影响核心机制结论而定） |
| **偏差 3：功能声称与实现不一致（如异步写成同步）** | `Completion pressure` / `Evidence-state overreach` | `Narrow` / `Reframe`（按真实 DTO 与异步链路重写机制描述） | **P0**（虚构运行时行为） |
| **偏差 4：AI 能力边界被夸大（忽略工程门禁/校验层）** | `Proof substitution` / `Completion pressure` | `Narrow` / `Reframe`（如实写出「AI 候选生成 + 工程 gate/validator/converter 校验决策」） | **P0**（夸大算法/AI 能力边界） |
| **偏差 5：把批处理 CLI 客户端写成常驻 HTTP 服务** | `Proof substitution` / `Completion pressure` | `Narrow`（没有 `ListenAndServe` 或等价绑定时，改写为 CLI / 批处理客户端） | **P0**（虚构进程形态） |

## 修正版段落的叙事投射自检（Narrative Projection Check）

在输出「修正版」可直接替换文本前，必须同步满足 `references/narrative-projection.md` 的三项铁律：
1. **语义主语归属（Nearest Semantic Owner）**：不要在修正段落中连续以「本项目 / 本文 / 本系统」开头（避免 Global-subject saturation），应以具体机制、模块、数据结构或业务过程作为主语（e.g. 「同步任务在校验通过后写入目标表……」「批处理客户端按配置路径导出结果……」）。主语里的领域名词必须来自当前仓库，不要照抄其他项目的模块名。
2. **项目概念优先于代码标识符（Project Ontology before Implementation Ontology）**：先用自然中文阐述业务与工程语义，再在必要处标注精确表名（e.g. `order_item`，不加引号包围）或状态常量（e.g. `PENDING`）。标识符必须来自当前仓库已打开的源码；这里的名字只说明写法。
3. **零审计残留（No Audit Residue）**：修正版正文中严禁出现「经核查代码发现」「原文档有误」「暂未实现」等审查过程话术，确保用户复制粘贴即可直接合入正式申报书或技术文档。
