# Writing Skill (`writing-skill` `v1.1.0`)

> **写文档 Skill — 整合代码库知识库生成、证据治理写作与文档代码逐行核验**  
> **Unified Technical Writing, Codebase Knowledge Base & Evidence Governance Skill**

规则不绑定任何具体产品仓库。下文若出现函数名或模块名，只作为举例或反例。历史试跑与分数见 [`CHANGELOG.md`](CHANGELOG.md)。

---

## 为什么需要这个 Skill？（团队 AI 协作三件套）

在课程项目、比赛申报与团队协作中，三份 Skill 按交付物接力，而不是互相替代：

1. 🛠️ **开发 Skill（[`WaterProMax/dev-skill`](https://github.com/WaterProMax/dev-skill)）**：契约与代码。从一句话需求或已有仓库扩模块，锁住文件白名单、接口契约和业务不变量。
2. 📝 **写作 Skill（本仓库 [`WaterProMax/writing-skill`](https://github.com/WaterProMax/writing-skill)）**：知识库与证据治理文档。把仓库事实收成可核验的本地索引，再写成不跨类顶替、不主语坍塌的正式文档。
3. 🎨 **画图 Skill（[`WaterProMax/drawing-skill`](https://github.com/WaterProMax/drawing-skill)）**：蓝图图。在契约、代码和已核验文档稳定之后，画架构图与机制图。

交接顺序：

`dev-skill` 契约与代码 → `writing-skill` 知识库与证据治理文档 → `drawing-skill` 蓝图图

本仓库把三条写作能力收成一个统一、无冲突、全链路闭环的 **一站式写文档 Skill (`writing-skill`)**：

1. **`codebase-knowledge-base-generation`（代码库知识库生成）**
   - 5 阶段并行代码库探索（`广度全量探索 -> 4+ 后台 Agent 并行深挖 -> 核心上下文同步读取 -> 7+1 结构化专题输出 -> 增量定点补充`）
   - 产出 `docs/knowledge-base/HOME.md`（按角色/按模块导航总索引）与 `01`～`07` 七个专题知识库文件，精确到类名、代码行数、数据表字段、API 路由矩阵与问题修复状态。模块名来自当前仓库，不写死其他项目的目录名。
2. **`project-document-evidence-governance`（项目文档证据治理写作与审计）**
   - 围绕五大核心对象（`Artifact Brief`、`Claim Record`、`Evidence Profile`、`Narrative Decision`、`Boundary Record`）构建正式项目文档、比赛申报书、研究报告与架构白皮书。
   - 严格区分 **Research（算法/研究）**、**Engineering（系统工程）** 与 **Product/Application（产品/应用）** 三类证明责任（Proof Obligations），杜绝跨类证据顶替、把验收目标当实测结果、把目录结构当章节大纲、以及连续以「本项目/本文/系统」开头的语义主语坍塌（Global-subject saturation）。
3. **`technical-doc-code-verification`（技术文档与代码逐行核验）**
   - 将技术文档拆解为原子级技术断言，结合知识库与真实源码（Controller / Service / Entity / Prompt）逐行核验。
   - 精准拦截五类高频偏差：（1）跨系统/跨模块技术张冠李戴、（2）状态枚举/流程步骤被简化丢失、（3）同步/异步实现机制与声称不符、（4）AI 能力边界被夸大（忽略工程门禁/校验层）、（5）把批处理 CLI 客户端写成常驻 HTTP 服务（须有 `ListenAndServe` 或等价绑定），并直接输出**可复制粘贴替换的完整修正段落**及源码行号证据。
   - 监听、空 Controller、密钥与连接串、Java 属性不等于物理列，是 **Mode 2/3 共用代码事实红线**，写在 `references/code-verification-workflow.md`。写子系统局限时不必进入 Mode 1 才能读到它们。

---

## 一键复制话术模板（直接喂给 Cursor / Claude Code / Cloud Agent）

先对上场景再粘贴。选错路线时，单模块局限会被写成整库知识库，或知识库目录会被当成申报书大纲。

### 场景 A：Mode 1 整库知识库生成

5 阶段并行探索，产出 `docs/knowledge-base/HOME.md` + `01`～`07`。不要把这次输出当成正式申报书。

```text
请严格加载并遵循 `writing-skill`（SKILL.md）的 Mode 1（知识库生成）与 `references/codebase-knowledge-base-workflow.md`。
目标仓库：【在这里填仓库路径，或写「当前仓库」】
交付物：在 `docs/knowledge-base/` 生成 `HOME.md` 与 `01`～`07`。不要把这 7+1 文件写成正式申报书或架构白皮书的章节大纲。

按 5 阶段执行，不要改成逐文件通读：
1. 阶段 1：2 级目录、模块所有权、配置与文档；行数只用本次统计。
2. 阶段 2：4+ 后台探索并行深挖；先全库扫入口，再按目录所有权拆主产品进程与独立工具进程（目录名只是举例，例如 `tools/**`）。前端除 `fetch` / `axios` 外，跟进本仓库自己的请求包装函数（e.g., custom wrapper functions such as apiClient / request / schoolFetch）。未跟进的调用只记「未覆盖」，禁止写「前端无某模块 API」。
3. 阶段 3：先读治理入口；路径缺失记新路径或 Boundary，不要回退同名历史目录。问题状态抽查必须打开指名源码，未打开则写「未打开源码核对（仅保留手记原词）」。
4. 阶段 4：输出 `HOME.md` + `01`～`07`。模块名只来自本仓库代码或 Wiki，不要写死其他项目的模块名（例如「用户系统/画像/简历」）。每张静态符号表开头声明：本表仅证明符号/映射在源码中存在，不代表方法体分支、鉴权或运行时业务契约已验证。`canonical_for` 留空；若已有 Wiki，开篇指向它并声明不替代。
5. 阶段 5：后台结果未回传前，在「阶段 5 增补」放置「占位：后台探索尚未回传，以下仅为主会话已核对范围。」回传后删除占位，只并入主会话已逐行核对的事实。

代码事实红线：无监听绑定（`ListenAndServe` 或等价绑定）不要写成常驻 HTTP 服务；空 Controller 不是 API；不要写入口令、连接串或完整 JDBC URL；没有 `@TableField` 或 DDL 不要臆造物理列名。
冲突优先级：running code > Flyway/entities > generated OpenAPI > Wiki non-canonical prose > test notes > experiment directories。
```

### 场景 B：Mode 2 + Scoped 单模块/单目录边界与局限性备忘录

严禁进入 Mode 1 建整库知识库。先列文件白名单，遵循 §9 与代码事实红线。

```text
请严格加载并遵循 `writing-skill`（SKILL.md）的 Mode 2 + 深度 Scoped。
范围：【在这里填单个目录或单条工具链】
交付物：该范围的边界与局限性备忘录。不要写整库知识库。

硬门禁：
1. 严禁进入 Mode 1，严禁创建 `docs/knowledge-base/HOME.md` 或 `01`～`07`。不要为了「先有证据」去建整库索引。证据只来自白名单内打开的源码行。
2. 先列出文件白名单。邻接代码只用来回答「会不会把 A 的技术写成 B」。
3. 必读：`references/core-model.md`、`references/writing-workflow.md`、`references/decision-rules.md` §9「子系统局限性备忘录」、`references/code-verification-workflow.md` 的 Mode 2/3 代码事实红线（含偏差 5）。不要加载 `codebase-knowledge-base-workflow.md`、`document-architecture.md`、`examples.md`。
4. 每个入口一行：进程形态、默认开关、写入目标、门禁。不要把不同入口的默认空跑合并成一句。「可以写 / 不能写」集中在一节。
5. 「比赛 / 申报」不会把本任务升到 Deep。章节职责是 Boundary 时，不要点满 RAG 三层、不要删掉必要限定、不要把标题改成能力宣传。偏差 4 与 §9 高于比赛文风。
6. 没有 `ListenAndServe` 或等价绑定，就不要把 CLI / 批处理写成常驻 HTTP 服务。邻接实验分数默认删除，除非本节 Claim Type 是 Research 且协议完整。
```

### 场景 C：Mode 2 + Standard/Deep 正式项目文档 / 比赛申报书 / 架构白皮书起草

五大核心对象 + Research / Engineering / Product 三类证明责任分离 + 杜绝主语坍塌。单个目录的局限备忘录不要走这条。

```text
请严格加载并遵循 `writing-skill`（SKILL.md）的 Mode 2，深度按篇幅选 Standard 或 Deep。
文稿类型：【正式项目文档 / 比赛申报书 / 架构白皮书，三选一】
读者与用途：【在这里填】
已有材料：【知识库路径、实验记录、源码仓库；没有就写「无」】

写作时保持五个对象分开，不要把调查过程写进正文：
1. Artifact Brief
2. Claim Record
3. Evidence Profile
4. Narrative Decision
5. Boundary Record

每条材料主张先归入 Research（算法/研究）、Engineering（系统工程）或 Product/Application（产品/应用）之一，再判断证据。禁止用运行结果顶替算法性能，用模型指标顶替编排/持久化/集成，或把验收目标写成实测结果。

主语规则：连续段落不要以「本项目 / 本文 / 本研究 / 系统」开头。语法主语用最近的机制、过程、参与者或数据对象。不要靠同义词轮换掩盖主语坍塌。

深度：
- 只写一个实质性章节或一条主张谱系：Standard。
- 全篇结构、多源对账、章节职责是能力的比赛申报书或终稿：Deep。此时再读 `document-architecture.md` 与 `examples.md`。
- 若交付物其实是单个目录的局限备忘录，改走场景 B（Scoped），不要升到 Deep。

`01`～`07` 与仓库目录只作 Investigator 索引，不得成为章节大纲。必要局限只给一个权威落点。标识符和模块名只来自当前仓库已打开的源码，不要套用其他项目的表名或功能名。
```

### 场景 D：Mode 3 技术文档与源码逐行核验审计

拆解原子断言、拦截 5 类高频代码偏差、输出可直接替换的修正段落与 P0/P1/P2 审计表。

```text
请严格加载并遵循 `writing-skill`（SKILL.md）的 Mode 3（代码核验与治理审计）。
待核验文档：【在这里贴路径或正文】
源码与知识库：【在这里填路径；知识库只加速检索，以打开的源码行为准】

执行顺序：
1. 把文档拆成原子断言，每条一句。
2. 先查知识库（若有），再打开对应源码。分清在线主链与离线/辅助工具。
3. 逐条归类：Exact match / Minor polish / Architecture misattribution / Exaggerated claim。
4. 重点拦截五类偏差：
   (1) 跨系统/跨模块技术张冠李戴；
   (2) 状态枚举或流程步骤被简化丢失；
   (3) 同步/异步实现与声称不符；
   (4) AI 能力边界被夸大（忽略工程门禁/校验层）；
   (5) 把批处理 CLI 客户端写成常驻 HTTP 服务（须有 `ListenAndServe` 或等价绑定；目录名、`net/http` import、未被引用的 URL 配置都不是绑定）。
5. 先诊断再改写。每处偏差给出：(1) 原文引用，(2) 文件路径 + 行号，(3) 可直接替换的完整修正段落。
6. 另给 P0/P1/P2 审计表：受影响主张、Claim Type、证据状态、根因、读者影响、主要处置。修正段落不要连续使用「本项目/本文/系统」作主语，不要残留「经核查代码发现」之类审查话术。

没有监听绑定、空 Controller、密钥与连接串、Java 属性不等于物理列，按 `references/code-verification-workflow.md` 的代码事实红线处理。
```

---

## 只写一个模块的边界时，停在 Scoped

队友只负责单体仓库里的一个后端模块或一条工具链，交付物是该范围的局限 / 申报边界，并且明确不要整库知识库时：

- 深度选 **Scoped**，模式选 **Mode 2**。不要进入 Mode 1，不要创建 `HOME.md` 或 `01`–`07`。
- 先写文件白名单。邻接代码只用来回答「会不会把 A 的技术写成 B」。
- 按 `references/decision-rules.md` §9「子系统局限性备忘录」：每个入口一行（进程形态、默认开关、写入目标、门禁）；不要把不同入口的默认空跑合并成一句；可以写 / 不能写集中在一节。
- 「比赛 / 申报」这几个字不会把本任务升到 Deep。章节职责是 Boundary 时，比赛文风（点满 RAG 三层、去掉谦辞、标题写成能力宣传）让路于偏差 4 和 §9。

这条规则适用于任何仓库。引入它的试跑记录在 `CHANGELOG.md` 的 1.0.3。整库 Mode 1 的接地约束仍由 1.0.1 / 1.0.2 保持有效。直接粘贴上面的场景 B。

---

## 四大工作模式（Operating Modes）

| 模式 | 适用场景 | 必读核心文件 |
|---|---|---|
| **Mode 1：知识库生成** (`Knowledge-Base Generation`) | 为大型多模块全栈代码库生成结构化本地知识库 (`HOME.md` + `01`..`07`) | `SKILL.md` + `references/codebase-knowledge-base-workflow.md` |
| **Mode 2：证据治理写作** (`Evidence-Governed Writing`) | 起草、改写、扩写比赛申报书、技术方案、架构文档、研究论文；**Scoped** 时只写一个目录或一条工具链的边界/局限 | `SKILL.md` + `references/core-model.md` + `references/writing-workflow.md`（Scoped 必读 §9 与代码事实红线；整篇架构按需） |
| **Mode 3：代码核验与治理审计** (`Code Verification & Audit`) | 逐行核验技术文档与源码是否一致、审计证据链与主语归属、输出可直接替换的修正版全文 | `SKILL.md` + `references/core-model.md` + `references/audit-workflow.md` + `references/code-verification-workflow.md` |
| **Mode 4：端到端全流程** (`End-to-End Pipeline`) | 从代码库出发，完成「知识库沉淀 → 证据治理成文 → 代码与证据谱系核验」闭环 | 依次串联 Mode 1 → Mode 2 → Mode 3 |

---

## 目录结构（Repository Layout）

```text
writing-skill/
├── SKILL.md                                         # 统一入口与四模式/四深度路由器（含 Scoped）+ 核心铁律
├── README.md                                        # 仓库说明、三件套交接与一键复制话术（v1.1.0）
├── CHANGELOG.md                                     # 版本演进；历史试跑与仓库名只记在这里
├── references/                                      # 完整保留并对齐的 10 个深度规范与工作流文件
│   ├── core-model.md                                # 五大标准工作对象与术语唯一真源
│   ├── writing-workflow.md                          # 预防式证据治理写作六阶段工作流 (Phases 0–6)
│   ├── audit-workflow.md                            # 事后证据治理审计与修复七步工作流 (Passes 0–6)
│   ├── codebase-knowledge-base-workflow.md          # 代码库 5 阶段并行探索与 7+1 知识库生成完整规范
│   ├── code-verification-workflow.md                # 技术文档与源码逐行核验 5 步法、Mode 2/3 代码事实红线、5 类偏差与比赛文档细则（Boundary 让路）
│   ├── claim-evidence-contracts.md                  # Research / Engineering / Product 三类证明契约与指标准入测试
│   ├── decision-rules.md                            # 证据状态分类、强状态词作用域、委托证明、披露必要性与 P0/P1/P2 定级
│   ├── narrative-projection.md                      # 内部结构向正式叙事投射、三层术语映射与最近语义主语规则
│   ├── document-architecture.md                     # 核心贡献重心、章节职责、跨层依赖与图表表征匹配
│   └── examples.md                                  # 18 类典型反模式与正反改写对照示例
└── tests/                                           # 静态拓扑校验与 19 个行为回归测试用例
    ├── README.md
    ├── regression-cases.yaml
    └── validate_structure.py
```

---

## 快速校验（Validation）

在仓库根目录下运行静态拓扑与预算检查脚本：

```bash
python3 tests/validate_structure.py
```
