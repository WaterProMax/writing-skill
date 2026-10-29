# Examples and Antipatterns

## Use

Use this file only when concrete failure signatures or rewrite patterns help. Diagnose with the core model and decision rules before copying any rewrite. Table names, module names, and vendor names in the samples illustrate the failure. Do not copy them into an unrelated repository.

---

## 1. Repository-first narrative

Weak:

```text
4.1 Frontend
4.2 Backend
4.3 Agent
4.4 Database
4.5 Deployment
```

Problem: repository or component taxonomy has replaced the reader’s task and project argument.

Safer route:

```text
research output -> user task -> cross-component mechanism -> persisted result -> verification
```

Component sections may remain when they answer a real design question.

---

## 2. Research evidence replaced by engineering evidence

Weak:

> “The API returned a structured match result, so the matching algorithm is accurate.”

The API response is engineering/runtime evidence. Accuracy requires a labeled evaluation protocol.

Safer separation:

- Research claim: report dataset, baseline, metric, threshold, and measured result.
- Engineering claim: report that the result contract was produced and consumed under stated conditions.

---

## 3. Engineering evidence replaced by a model score

Weak:

> “The model achieved F1 = 0.93, so the end-to-end workflow is complete.”

A metric does not prove persistence, routing, recovery, UI rendering, or user completion.

---

## 4. Proposal with caveats but no acceptance contract

Weak:

> “The final accuracy is not yet verified and will be tested later.”

Repeated across every subsection, this is honest but not testable.

Safer proposal form:

> “The method will be compared with keyword matching and vector retrieval on a held-out, manually reviewed test set. Delivery requires mapping F1 of at least 0.90; errors will be analyzed by alias, granularity, and context ambiguity.”

The threshold must have an authorized basis.

---

## 5. Orphan metric

Weak:

> “The evaluation uses weighted Kappa.”

Missing:

- ordinal task;
- rating scale;
- reference rater;
- weighting variant;
- adjudication;
- rationale.

Use Kappa only after the Research Validation Contract establishes those fields. Otherwise remove it.

---

## 6. Ambiguous referent

Weak:

> “This is passed to the next function, where the problem is handled.”

Better:

> “The structured résumé record is passed to skill normalization, which maps each mention to a standard skill or retains it for review.”

---

## 7. Missing engineering actor

Weak:

> “After confirmation, it is updated and later recovered.”

Better:

> “After the reviewer confirms the proposed change, the governance service creates a new version. If a dependent task is incomplete, the scheduler suspends the parent and the reconciliation service resumes it after the dependency reaches a terminal state.”

---

## 8. Q/R labels as concepts

Weak:

> “Q1 provides observations, Q3 provides semantics, and Q4 performs evolution.”

Better:

> “Multi-source job-demand governance (Q1) produces traceable observations. Skill-entity standardization (Q3) aligns those observations in a shared semantic space, which the evolution analysis (Q4) uses to compare changes over time.”

---

## 9. Code constants in ordinary prose

Weak:

> “The user enters WAITING_INPUT, JOB_MATCH is blocked, and the task later becomes degraded.”

Better:

> “When required information is missing, the interaction pauses and requests the missing material. The runtime records this state as `WAITING_INPUT`. Matching remains unavailable until the required input is supplied.”

---

## 10. Checklist-shaped research prose

Weak visible structure repeated six times:

```text
Problem
Method
Data
Result
Contract
```

Better:

- data governance: defects -> governance -> reference truth -> quality evaluation;
- ontology mapping: ambiguity -> concept model -> disambiguation -> mapping evaluation;
- temporal analysis: time semantics -> change model -> backtest;
- matching: decision target -> baseline -> experiment -> error analysis.

The internal checklist may remain symmetric.

---

## 11. Snapshot detail presented as project truth

Weak:

> “On 28 August, commit abc123 passed five local runs with three warnings.”

Safer main-text form:

> “The integrated workflow was executed in a controlled environment covering task creation, persistence, dependency handling, and result return.”

Keep exact commit, date, and warnings in reproducibility evidence when needed.

---

## 12. Overexposure of incomplete work

Weak:

> “The route is incomplete, three warnings remain, one screen is missing, and no fully green path exists.”

If the artifact does not claim full user-facing closure, move the defect inventory to a readiness report.

Necessary boundary when full closure is implied:

> “The reported validation covers backend generation and structured result return; user-interface presentation is evaluated separately.”

---

## 13. Strong-state scope ambiguity

Weak:

> “The system is complete and validated.”

Scoped:

> “The backend matching workflow was validated in a controlled integrated environment using representative cases.”

---

## 14. Claim-Lineage regression

Experiment section:

> “The candidate-generation mechanism was evaluated for reproducibility; market novelty accuracy was not measured.”

Final summary:

> “The project accurately identifies emerging occupations.”

The summary silently expands the claim. Narrow all lineage occurrences to the authoritative form.

---

## 15. Primary contribution displacement

Title:

> “Knowledge graph construction and dynamic evolution analysis”

Document emphasis:

- two pages on graph construction/evolution;
- twenty pages on résumé UI and career advice.

Problem: downstream application evidence has displaced the title-level contribution.

Repair: restore graph construction and dynamic evolution as the principal method, experiment, figure, and conclusion chain; present résumé and matching as downstream validation/application unless the adopted scope says otherwise.

---

## 16. Expected value presented as observed outcome

Weak:

> “The system improves HR decision efficiency.”

Without application evidence, this is an observed-outcome claim.

Safer expected-value form:

> “By presenting structured requirements and source evidence in one view, the system is designed to reduce repeated manual comparison.”

Observed improvement requires a defined user study or application record.

---

## 17. Screenshot-only validity claim

Weak:

> “The result screen proves that the algorithm is effective.”

A screenshot supports presentation. Use experiment evidence for algorithm quality and runtime evidence for execution.

---

## 18. Writing-process leakage

Remove from formal prose:

- “The next chapter has not been written.”
- “The AI could not infer this.”
- “The current repository lacks the final report.”
- “To fit the page, the table was split.”
- “Do not fake success.”

State the project content, acceptance design, and necessary boundary instead.
