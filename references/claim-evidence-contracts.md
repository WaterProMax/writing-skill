# Claim–Evidence Contracts

## Purpose

This file defines the proof obligations for the three Claim Types in `core-model.md`.

The three contracts are different because they answer different questions:

```text
Research -> Does the method solve the analytical problem, and how well?
Engineering -> Is the mechanism implemented, and does it behave correctly under stated conditions?
Product/Application -> What user or organizational problem is addressed, and what value is expected or observed?
```

No contract may borrow another contract’s evidence to fill its own proof gap.

---

## 1. Claim-Type routing

Route by the conclusion being asserted, not by the source being inspected.

| Claim asks the reader to believe | Primary Claim Type |
|---|---|
| A model, method, ranking, extraction, or analysis is accurate/effective/robust | Research |
| A service, workflow, state transition, integration, or recovery mechanism exists and works | Engineering |
| A user or organization can perform a task or gain a decision benefit | Product/Application |

Split a sentence when it combines multiple proof obligations.

Example:

> “The matching algorithm is accurate and the complete user journey works.”

This contains at least two Claim Records:

- Research: matching quality;
- Engineering/Product: user-facing journey completion.

---

# Research Evidence Contract

## 2. Research Validation Contract

Every material Research claim should be traceable to:

```text
Research object or question:
Hypothesis or decision to establish:
Input population and scope:
Dataset or sample source:
Reference truth / gold label:
Label authority:
Annotation and adjudication protocol:
Train/dev/test, grouped, or temporal split:
Leakage controls:
Baseline or comparator:
Proposed method:
Metric:
Metric rationale:
Acceptance target:
Measured result, if claimed:
Uncertainty or significance, when material:
Error analysis:
External-validity boundary:
```

The final artifact may express this through prose, tables, figures, and experiment sections rather than showing the template literally.

---

## 3. Plan, target, result, and conclusion

Keep these as distinct claims:

1. **Method plan** — what will be done.
2. **Acceptance target** — what level counts as acceptable delivery.
3. **Measured result** — what a defined experiment produced.
4. **Validated conclusion** — what the result justifies within the protocol.

Example:

- Plan: A held-out, manually reviewed test set will be used.
- Target: Skill-mapping F1 must be at least 0.90.
- Result: The method achieved F1 = 0.92.
- Conclusion: The method exceeded the predefined threshold on the frozen test distribution.

A target is not a result. A result requires experiment evidence.

---

## 4. Proposal obligation when results are incomplete

A proposal may be valid before all experiments are complete, but it must remain testable.

When current measured results are unavailable, define:

- evaluation population;
- reference truth;
- baseline;
- split and leakage controls;
- metric and rationale;
- minimum acceptance target;
- planned error analysis.

Do not replace this contract with repeated “not yet verified” language.

Acceptance targets require a stated basis, such as:

- competition or contractual requirement;
- adopted product quality requirement;
- fair baseline performance;
- domain standard;
- risk tolerance approved by the owner.

Do not invent a threshold merely to make the proposal look complete.

---

## 5. Baseline obligation

A performance claim normally needs a comparator measured on the same evaluation population and under the same protocol.

Possible baselines include:

- simple rules or keyword methods;
- conventional statistical methods;
- established models;
- current production methods;
- ablations;
- random or majority baselines when meaningful.

The baseline must be fair. Do not choose a deliberately weak comparator.

---

## 6. Metric Admissibility Test

Before a material metric enters research prose, establish:

```text
Task:
Target variable:
Reference-truth source:
Label authority:
Exact metric variant, when material:
Why the metric fits the decision:
Evaluation population and aggregation:
Baseline:
Acceptance target:
Measured value, if claimed:
Interpretation:
Limit:
```

If the first six fields are missing, the metric is an **orphan metric** and should not appear as a formal evaluation claim.

If the contract is defined but no value exists, the metric may appear as part of the planned acceptance protocol—not as a result.

Specific metric examples belong in `examples.md`.

---

# Engineering Evidence Contract

## 7. Engineering Evidence Contract

Every material Engineering claim should be traceable to:

```text
Requirement or engineering problem:
Owning actor or component:
Trigger or precondition:
Action or mechanism:
Input and stable identifiers:
State or data mutation:
Output or handoff:
Failure or degraded condition:
Recovery, rejection, or human boundary:
Verification evidence:
Acceptance conclusion:
```

A strong explanation usually makes this chain visible:

`actor -> condition -> action -> state/data effect -> output -> failure handling -> verification`

This is an internal completeness check, not a mandatory sentence template.

---

## 8. Engineering verification

Engineering evidence can support claims such as:

- an interface validates a contract;
- a workflow reaches a defined state;
- a transaction preserves consistency;
- a retry or reconciliation mechanism recovers execution;
- a UI renders a supported result schema;
- a user action is accepted, rejected, or routed correctly;
- a representative end-to-end path executes under stated conditions.

Engineering evidence cannot establish:

- classification accuracy;
- extraction precision or recall;
- ranking quality;
- model generalization;
- scientific novelty;
- real-world user impact.

---

# Product/Application Evidence Contract

## 9. Product/Application Evidence Contract

Every material Product/Application claim should be traceable to:

```text
Target user or organization:
Problem, task, or decision:
User-visible capability:
Required research basis:
Required engineering basis:
Usage context:
Expected value:
Observed outcome, if claimed:
Application evidence:
Adoption or decision boundary:
```

### Expected value vs observed outcome

Keep these distinct:

- **Expected application value** — a reasoned future-facing benefit supported by requirements, validated research outputs, and implemented system capability.
- **Observed application outcome** — a measured or documented result from actual users or real operating contexts.

Examples:

- Expected: “The capability can reduce repeated manual comparison by presenting structured evidence.”
- Observed: “In a controlled user study, reviewers completed the comparison task 28% faster.”

The second statement requires application evidence; the first requires a defensible mechanism and context.

---

## 10. Product projection

Product/Application prose should normally follow:

`user problem -> visible capability -> relevant research basis -> relevant engineering basis -> decision or output -> boundary`

Do not lead product prose with internal task types, worker pools, table names, or status constants.

A screenshot may show presentation. It does not by itself prove algorithm quality, workflow completeness, or user value.

---

# Cross-type rules

## 11. Prohibited substitutions

- Code existence does not prove research effectiveness.
- Runtime success does not prove generalized performance.
- Model accuracy does not prove integration or recovery.
- Screenshots do not prove algorithm validity.
- Engineering completion does not prove adoption or business outcome.
- Expected value does not equal observed application impact.

---

## 12. Research-to-engineering handoff

A research output should be handed off semantically before it is handed off as code:

```text
Research output meaning:
Required fields and uncertainty:
Version or provenance requirement:
Allowed downstream use:
Consumer need:
Engineering representation:
```

Research prose should normally stop at stable semantic output and validation boundaries.

Engineering prose may then explain DTOs, manifests, state models, persistence, services, and UI projection.

Do not end every research subsection with source-code contract details unless the contract itself is part of the research contribution or reproducibility requirement.

---

## 13. Cross-type acceptance chain

For a full project claim, establish the chain explicitly:

```text
Research validity
  -> engineering realization
  -> product/application consumption
  -> application outcome, when claimed
```

A gap in one link must not be hidden by stronger evidence in another link.
