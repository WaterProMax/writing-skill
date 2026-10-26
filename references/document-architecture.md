# Document Architecture

## Purpose

Design a formal artifact around the reader’s reasoning path and the project’s primary contribution.

This reference is upstream of sentence-level writing. It does not impose one universal outline.

---

## 1. Primary-contribution gravity

Extract from the Artifact Brief:

```text
Primary contribution objects:
Primary research or solution actions:
Material qualifiers:
Downstream applications:
```

Then check whether:

- chapter space;
- strongest evidence;
- experiments;
- figures;
- summaries;
- final conclusions;

preserve the same hierarchy.

Title language creates a proof obligation, but title alone is not absolute. Binding rubric or contractual requirements set hard obligations; adopted scope and explicit owner intent determine emphasis within those obligations. Material conflict requires project-owner resolution.

Downstream applications must not become the apparent project center merely because they are easier to demonstrate.

---

## 2. Argument closure

A formal project artifact should let the reader trace:

`real problem -> defined need -> method or solution -> engineering realization -> verification -> value`

The headings may differ. The requirement is justified closure, not a fixed template.

A document that lists assets, models, modules, and screens without showing their dependency does not form one project argument.

---

## 3. Chapter responsibility

For every major section, complete:

> “This section is responsible for helping the reader conclude ______.”

Typical roles:

- background: why the problem exists and matters;
- requirements: what capability or constraint is needed;
- research: what analytical problem is solved and how it is evaluated;
- engineering: how validated outputs and business rules are realized as a system;
- verification: what behavior or performance is established;
- summary: what contribution is supported and where the limits remain.

A locally correct paragraph is still misplaced if another section owns its responsibility.

---

## 4. Dependency coherence

For each major unit, identify:

```text
Upstream input:
Transformation or responsibility:
Output:
Downstream consumer:
Feedback or update path:
```

Dependencies may be:

- data;
- causal;
- semantic;
- decision;
- verification.

Make enough dependencies explicit to prevent the document from reading like independent mini-projects joined by a title.

---

## 5. Cross-layer traceability

Important claims should be traceable across the project chain:

`problem -> requirement -> research claim -> semantic output -> engineering capability -> verification -> application`

Not every paragraph needs the full chain. The artifact as a whole should support it.

Research-to-engineering handoff should first define semantic meaning, uncertainty, provenance, and allowed use. Exact DTOs and task constants belong to engineering or reproducibility layers.

---

## 6. Narrative salience

Allocate space according to:

`importance × differentiation × evidence strength × reader need`

Do not distribute words or figures evenly simply because the system has several modules.

Give more space to mechanisms that:

- solve the central problem;
- distinguish the project;
- carry major risk;
- require evidence for trust.

---

## 7. Reader journey vs system taxonomy

Repository decomposition and narrative decomposition are different decisions.

A repository may contain frontend, backend, agents, infrastructure, and tests. A reader may understand the project better through:

- a user task;
- a data journey;
- a decision flow;
- a research dependency;
- a lifecycle.

Use system taxonomy as a supporting view, not an automatic table of contents.

---

## 8. Scenario-driven explanation

A representative flow can connect components:

`user input -> interpretation -> domain task -> method/tool -> persisted result -> human confirmation -> downstream decision`

Introduce components where they matter to the flow.

Component-specific sections remain valid when they answer a real design question rather than merely catalog technologies.

---

## 9. Contrastive argument

Innovation becomes understandable through:

`existing approach -> material limitation -> project change -> resulting capability or evidence`

Comparators must be fair and accurately represented.

Do not turn an ordinary implementation choice into an innovation merely because it appears in code.

---

## 10. Representation fit

| Relationship | Preferred representation |
|---|---|
| Sequence or handoff | Flowchart or sequence diagram |
| Role and permission | Responsibility or use-case view |
| State transition | State machine |
| Layered system | Architecture diagram |
| Alternative or gap | Comparison table |
| Cross-layer mapping | Traceability matrix |
| Time change | Timeline or trend chart |
| Many-to-many relation | Graph or matrix |
| Precise field contract | Schema or table |

A figure should reduce reasoning cost, not decorate the page.

---

## 11. Conceptual grounding

Use established academic or industrial concepts accurately when they provide shared vocabulary or comparison context.

Examples:

- human-in-the-loop;
- versioned knowledge graph;
- evidence provenance;
- event-driven architecture;
- idempotency.

Grounding must not disguise an ordinary implementation as a novel theory.

---

## 12. Architecture audit

Ask:

1. What should the reader conclude after each chapter?
2. Does the document prove a problem or merely announce one?
3. Do major modules form dependencies or only a list?
4. Does the primary contribution own the strongest evidence?
5. Can important capabilities be traced across research, engineering, and application?
6. Does the narrative follow reader reasoning or repository taxonomy?
7. Are figures matched to the relationships they carry?
8. Are downstream applications proportionate to the central contribution?
9. Are semantic outputs stable before implementation details appear?
10. Does the conclusion foreground the same contribution promised at the start?
