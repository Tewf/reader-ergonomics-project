# 0003: A project is six topics, and a check reads them

**Decision:** The shape of a project is a folder of six topics, problem, scope, review, baseline, plan and trail, and a check refuses a project that lacks a part or names no baseline.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/shapes/decision-record.md).

## Context

- The front page promises each step of a project as a topic. The review ended in a named baseline, B1, and found that no step is measured ([review](../evidence/project-method/review.md)).
- The review is finished only when it names a baseline. A rule that depends on a reader remembering it is broken first, so a program should read it.
- Blueprint registers its topic check by copying it into `checks/local/` and declaring its files in `checks/config.toml`. This repository does the same for its shape.

## Decision

- [The project shape](../shapes/project.md) has a root and six parts: problem, scope, review, baseline, plan, trail. Each part is a topic and announces the topic shape.
- The review's fifth step, the baseline, has its own part, so the check can decide on it alone.
- `checks/local/project_shape.py` reads every file that declares the shape. It errors on a missing part, an unlinked part, a part without its own required rows or headings, and a baseline that is empty or a placeholder. It warns on a problem of more than one sentence and on a baseline without a comparison.
- The filled example is the repository's own first job, in [shapes/examples/first-job](../shapes/examples/first-job/README.md).

## Consequences

- A project written in the shape can be resumed from its folder, and the check fails the one that cannot name its baseline.
- The check decides form only. It cannot decide that the baseline is the right one or that the comparison was run; that stays with the maintainer.
- A reader who starts a project with fewer parts gets an error: six parts is a convention, untested ([position](../evidence/project-method/position.md)), and may cost a small job more than it saves.
- **Bad:** the shape is a convention with no measured benefit, and a placeholder list can be evaded by a vague phrase.

## See also

[Decisions](README.md); [the shape](../shapes/project.md); [0002](0002-keep-the-name-name-the-baseline.md).
