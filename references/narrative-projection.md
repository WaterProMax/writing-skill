# Narrative Projection

## Purpose

Project evidence and internal analysis use structures that are useful for machines and teams:

- Q/R labels;
- code constants;
- state enums;
- evidence ledgers;
- repeated checklists;
- repository modules;
- symmetric audit forms.

Formal prose should project those structures into explicit actors, stable concepts, and reader-facing arguments.

The transformation is:

`internal structure -> semantic meaning -> formal expression`

---

## 1. Referential clarity

A generic referent such as:

- this;
- that;
- the above;
- the problem;
- the function;
- the chain;
- it;

is acceptable only when the antecedent is unique, nearby, stable, and unambiguous.

If multiple antecedents are plausible, repeat the concrete noun.

Weak:

> “This is then passed to the next stage, where it is handled.”

Better:

> “The structured job-demand record is passed to skill normalization, which maps each unresolved skill mention to a candidate standard skill or retains it for review.”

Referential clarity is a correctness property, not a cosmetic preference.

---

## 2. Actor ownership in engineering prose

For each material process sentence, identify when relevant:

```text
Actor:
Trigger or condition:
Action:
Object or state affected:
Result or handoff:
Failure or human boundary:
```

This is an internal check, not a mandatory sentence template.

Weak:

> “After confirmation, it is updated and enters the next workflow.”

Better:

> “After the reviewer confirms the proposed change, the job-governance service creates a new job version and publishes the updated capability relations to the graph projection.”

Concrete subject repetition is preferable to elegant but ambiguous pronouns.

---

## 3. Three-layer terminology projection

### Layer A — Reader-facing narrative

Use established project and engineering terms in the document’s primary language.

Examples:

- degraded -> 降级运行状态
- blocked -> 阻断状态
- fail closed -> 默认拒绝 or 故障封闭, according to meaning
- fixture -> 固定测试样本 or 测试夹具, according to context
- lease -> 任务租约
- fallback -> 降级方案 or 备用路径

### Layer B — Standard technical terminology

Define a necessary standard English term or acronym once when it improves precision.

Examples:

- 宏平均 F1（Macro-F1）
- 平均倒数排名（MRR）
- 人在回路（Human-in-the-loop）

After definition, use the shortest stable form appropriate for the audience.

### Layer C — Exact implementation identifiers

Preserve exact strings only where exactness matters:

- `WAITING_INPUT`
- `JOB_DISCOVERY`
- `LEARNING_PATH`
- class names;
- fields;
- API states;
- contract versions;
- environment variables.

These belong mainly in implementation mapping tables, schemas, state tables, code excerpts, appendices, or reproducibility notes.

Translate meaning before spelling.

---

## 4. Project ontology before implementation ontology

Use:

`project concept -> implementation anchor`

not:

`implementation identifier -> retrofitted project concept`

Preferred:

> “When required information is missing, the interaction pauses and requests the missing material. The runtime represents this condition as `WAITING_INPUT`.”

Avoid:

> “The user enters WAITING_INPUT and JOB_MATCH is blocked.”

---

## 5. Index labels are navigation aids

Q1–Q6, R1–R7, stage numbers, milestone IDs, and similar labels support navigation and traceability.

They should not routinely serve as grammatical subjects.

Prefer:

> “Multi-source job-demand governance (Q1) provides traceable observations.”

Avoid:

> “Q1 provides observations.”

High-density labels belong in mapping tables, experiment plans, appendices, and traceability matrices.

---

## 6. Visible structure follows the subject

Internal completeness checklists may be symmetric. External sections should follow the causal structure of the subject.

Possible structures:

### Data governance

`data defect -> governance mechanism -> reference truth -> quality evaluation -> residual error`

### Ontology or entity mapping

`semantic ambiguity -> concept model -> candidate retrieval/disambiguation -> mapping evaluation -> graph consistency`

### Temporal evolution

`time semantics -> observation window -> change definition/model -> temporal split/backtest -> delay and error`

### Ranking or matching

`decision target -> constraints/features -> baseline -> ranking/classification experiment -> calibration and error analysis`

### Engineering mechanism

`problem -> operating constraint -> actor and mechanism -> state/data effect -> failure/recovery -> verification`

Checklist symmetry must not become prose symmetry.

---

## 7. Paragraph ownership

Every paragraph should have:

- one primary subject;
- one primary abstraction level;
- one material movement in the argument.

A paragraph may bridge adjacent levels deliberately, for example method -> implementation handoff. It should not jump repeatedly among design, class names, test IDs, defects, and business value.

Preferred movement:

`problem -> constraint -> method/mechanism -> evidence -> conclusion`

Not every paragraph needs all five parts.

### Semantic subject ownership and global-subject saturation

The grammatical subject should normally be the **nearest semantic owner** of the action or claim.

Prefer the method, research object, process, mechanism, actor, or data object that actually performs or carries the meaning:

- “岗位能力演化分析以活动岗位版本作为移动基线……”
- “技能标准化过程分为提及识别、节点解析和关系发布……”
- “个人能力画像保留能力结论与经历证据之间的对应关系……”

Project-wide wrappers such as “本项目”, “本文”, “本研究”, “系统”, “we”, or “the project” are appropriate for:

- chapter or section framing;
- explicit ownership or scope statements;
- cross-cutting synthesis;
- conclusions that genuinely refer to the project as a whole.

They should not become the default subject of successive paragraphs when a more specific semantic owner exists.

Repeated global subjects create **global-subject saturation**: the true method or object is pushed into predicate position, paragraph ownership becomes less informative, and prose acquires a template-shaped rhythm even when individual sentences are correct.

Weak:

> “本项目采用来源快照保存岗位材料。本项目将技能标准化分为三个阶段。本项目以岗位版本作为时间基线。”

Better:

> “岗位材料以不可变来源快照保存。技能标准化过程分为提及识别、节点解析和关系发布。岗位能力演化分析以活动岗位版本作为时间基线。”

Do not solve global-subject saturation by mechanically rotating synonyms such as “本文 / 本研究 / 本系统”. That preserves the same semantic failure under lexical variation.

Do not force a local noun into subject position when the project itself genuinely owns the claim. Subject choice follows semantic ownership, not a repetition quota.

---

## 8. Transitions must express a real relation

A transition should communicate:

- causality;
- contrast;
- prerequisite;
- sequence;
- decomposition;
- evidence consequence;
- scope restriction.

Do not begin a new paragraph with “therefore”, “thus”, “this means”, or “from this” when the paragraph introduces a new subject.

Name the subject directly.

---

## 9. Conclusion discipline

Repeated endings such as these create template-shaped prose when used mechanically:

- “Therefore, the core of this function is…”
- “In summary…” after every subsection
- “This means…” at every transition
- “It is not X, but Y…” repeatedly

A conclusion sentence should remain only when it adds synthesis, comparison, decision, or boundary.

Do not randomize wording to hide a template. Change the argument structure.

---

## 10. Metrics in prose

Metric validity is governed by `claim-evidence-contracts.md`.

Narrative projection adds one requirement: introduce a metric locally so the reader understands:

- what task it measures;
- what higher or lower values mean;
- why it matters to the project.

Do not drop acronyms into prose merely because they exist in an evaluation checklist.

---

## 11. Remove audit and authoring residue

Formal artifacts should not narrate:

- that another chapter is unfinished;
- that an AI or auditor could not infer something;
- that a repository search failed;
- that a table was split for drafting convenience;
- anti-hallucination instructions;
- token or tool constraints;
- TODO/TBD placeholders;
- editing rationale;
- internal defect inventories unrelated to the current claim.

Preserve these in working notes, evidence records, or readiness reports when useful.

---

## 12. Naturalness audit

Do not treat naturalness as sentence variation alone.

Check:

1. Does each section exist because the subject needs it?
2. Does each paragraph name its semantic owner?
3. Does the grammatical subject usually match the nearest semantic owner rather than a repeated project-wide wrapper?
4. Does visible structure follow real causal logic?
5. Are internal identifiers subordinate to project concepts?
6. Are technical terms introduced for reader value?
7. Do conclusion sentences add new synthesis?
8. Does rhythm follow the argument rather than a fixed generator?

Natural formal prose emerges from precise semantic ownership and heterogeneous argument structure.
