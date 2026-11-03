# Specify before building

**Claim:** a project writes its scope, what is in and what is out and why, before the work starts.

- **Grade:** supported with caveat for hasty specification as a major source of avoidable rework (an expert report, and one review limited to global software development); convention, untested for a written scope as the remedy.
- **Evidence:** [review, strand E](../../evidence/project-method/review.md); [position, what the repository can claim](../../evidence/project-method/position.md); [against, the cost of late defects](../../evidence/project-method/against.md); Boehm 2001, sections TWO and THREE; Nawaz 2022 (secondary); Peffers 2006, activity 2.
- **Check:** `project-shape` (errors): the project has a scope part with an `in` row, an `out` row and a Why column. Whether the scope is the right one is judgment.
- **Reader styles:** none.

## What it asks

- Write the scope as a table: a row for what is in, a row for what is out, and a Why for each.
- Write it before the plan and before the work; the [project shape](../../shapes/project.md) puts it second.
- Name the neighbour that holds what is out, so the boundary has an owner.

## Why

- Current projects spend about 40 to 50 percent of effort on avoidable rework, and hastily specified requirements are a
  major source (Boehm 2001, an expert report).
- The design science process infers the objectives of a solution from the problem, before design (Peffers 2006).

## Limits

- No study isolates a written scope and measures rework or round trips.
- The cost of a late fix is not a fixed ratio: a delayed-issue effect was not found in 171 projects (Menzies 2017, secondary).
- Some rework is good: iteration needs it (Fairley 2005). The aim is fewer wasted round trips, not none.
