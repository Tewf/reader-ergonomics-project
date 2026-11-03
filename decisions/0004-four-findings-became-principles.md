# 0004: Four findings became principles

**Decision:** The card holds four principles, specify before building, name the baseline, leave a trail and a project is six topics; the missing measurements and the plan's parts stay findings.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/b9732b9814c71768f722691f3c5049ec2b8ed378/shapes/decision-record.md).

## Context

- The extension contract asks a card of principles. A principle is a rule a program can read or a finding graded measured or supported with caveat; a convention enters only if a check enforces it ([extending](https://github.com/Tewf/reader-ergonomics/blob/b9732b9814c71768f722691f3c5049ec2b8ed378/extending.md)).
- The review graded one finding [supported with caveat](../evidence/project-method/position.md), hasty specification as a source of rework, and the rest conventions ([review](../evidence/project-method/review.md)).
- The project check [already enforces](0003-a-project-is-six-topics.md) the scope, the baseline, the trail and the six parts.

## Decision

- **Principles:** specify before building (supported with caveat, and convention for the remedy); name the baseline, leave a trail and a project is six topics (convention, untested, each enforced by `project-shape`).
- **Findings that stay:** no step is measured, and the cost of a late fix has no fixed ratio.
  The plan's parts, Decided first and For the person to decide, have no source but the maintainer's practice.
  They stay in the review and the shape.
- **Checks:** all four principles name `project-shape`. The check already decides each of their forms, so no second program is written; a program per principle would split one reading of one folder.
- The card sits in `standard.md`, built by the standard's builder, with one group, method.

## Consequences

- A rule with no source stays visible as a finding and is not promoted by a check that enforces it.
- **Bad:** three of four principles are conventions, so the card claims little; and one check serves four principles, so a bug in it weakens all four.
- If a source measures a written scope or a named baseline, the grade moves with a cited source, and the principle moves up.

## See also

[Decisions](README.md); [the card](../standard.md); [0003](0003-a-project-is-six-topics.md).
