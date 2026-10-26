# Writing Skill (`writing-skill`)

> **写文档 Skill — 整合代码库知识库生成、证据治理写作与文档代码逐行核验**  
> **Unified Technical Writing, Codebase Knowledge Base & Evidence Governance Skill**

本仓库将 `Lenquest/KariosArc` 中的三个核心写作与核验 Skill 深度整合为一个统一、无冲突、全链路闭环的 **一站式写文档 Skill (`writing-skill`)**：

1. **`codebase-knowledge-base-generation`（代码库知识库生成）**
   - 5 阶段并行代码库探索（`广度全量探索 -> 4+ 后台 Agent 并行深挖 -> 核心上下文同步读取 -> 7+1 结构化专题输出 -> 增量定点补充`）
   - 产出 `HOME.md`（按角色/按模块导航总索引）与 `01`～`07` 七个专题知识库文件，精确到类名、代码行数、数据表字段、API 路由矩阵与问题修复状态。
2. **`project-document-evidence-governance`（项目文档证据治理写作与审计 v0.5.1）**
   - 围绕五大核心对象（`Artifact Brief`、`Claim Record`、`Evidence Profile`、`Narrative Decision`、`Boundary Record`）构建正式项目文档、比赛申报书、研究报告与架构白皮书。
   - 严格区分 **Research（算法/研究）**、**Engineering（系统工程）** 与 **Product/Application（产品/应用）** 三类证明责任（Proof Obligations），杜绝跨类证据顶替、把验收目标当实测结果、把目录结构当章节大纲、以及连续以「本项目/本文/系统」开头的语义主语坍塌（Global-subject saturation）。
3. **`technical-doc-code-verification`（技术文档与代码逐行核验）**
   - 将技术文档拆解为原子级技术断言，结合知识库与真实源码（Controller / Service / Entity / Prompt）逐行核验。
   - 精准拦截五类高频偏差：（1）跨系统/跨模块技术张冠李戴、（2）状态枚举/流程步骤被简化丢失、（3）同步/异步实现机制与声称不符、（4）AI 能力边界被夸大（忽略工程门禁/校验层）、（5）把批处理 CLI 客户端写成常驻 HTTP 服务（须有 `ListenAndServe` 或等价绑定），并直接输出**可复制粘贴替换的完整修正段落**及源码行号证据。
   - 监听、空 Controller、密钥与连接串、Java 属性不等于物理列，是 **Mode 2/3 共用代码事实红线**，写在 `references/code-verification-workflow.md`。写子系统局限时不必进入 Mode 1 才能读到它们。

---

## 只写一个模块的边界时，停在 Scoped（v1.0.3）

队友只负责单体仓库里的一个后端模块或一条工具链，交付物是该范围的局限 / 申报边界，并且明确不要整库知识库时：

- 深度选 **Scoped**，模式选 **Mode 2**。不要进入 Mode 1，不要创建 `HOME.md` 或 `01`–`07`。
- 先写文件白名单。邻接代码只用来回答「会不会把 A 的技术写成 B」。
- 按 `references/decision-rules.md` §9「子系统局限性备忘录」：每个入口一行（进程形态、默认开关、写入目标、门禁）；不要把不同入口的默认空跑合并成一句；可以写 / 不能写集中在一节。
- 「比赛 / 申报」这几个字不会把本任务升到 Deep。章节职责是 Boundary 时，比赛文风（点满 RAG 三层、去掉谦辞、标题写成能力宣传）让路于偏差 4 和 §9。

依据：Lenquest/KariosArc 范围化局限性试跑（PR #21，引导质量 **6/10**）。整库 Mode 1 仍由 1.0.1 / 1.0.2 约束。

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
├── README.md                                        # 仓库说明与架构概览
├── CHANGELOG.md                                     # 版本演进与三合一整合说明
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
