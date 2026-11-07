# The project standard

What running a project shares, as far as the evidence goes: write the scope before the work, name the baseline that
ends the review, and leave a trail someone else can resume from. It extends
[reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/0206e6950b4feca4194af419384c217863b7c42e/standard.md), the standard for any reader, and builds on the
[topic](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md), the unit every step is written in: read the standard first, then the topic. This page adds only
what a project changes. No step is measured to cut rework, so most grades are conventions.

## How to use it

1. **Pick the shape:** the [project shape](shapes/project.md), and name it in the project's root with a `**Shape:**`
   line that links it; the check finds the project by that line.
2. **Write to the principles** below, and to those of reader-ergonomics, which still hold.
3. **Check:** copy `checks/local/` into your repository and run the standard's checks. `project-shape` finds each
   project root by its Shape line and reads its six parts.

Grades mean what they mean in [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/0206e6950b4feca4194af419384c217863b7c42e/standard.md#grades): measured, supported with caveat,
convention, not supported. Each principle states its grade and never claims more.

## Principles

<!-- principles:start -->

### Method: from a problem to its result

| Principle | Claim | Grade |
|---|---|---|
| [A project is six topics](principles/method/a-project-is-six-topics.md) | a project is a folder of six parts, problem, scope, review, baseline, plan and trail, each written as a topic. | convention, untested; an outline raised judged writing quality in an experiment (Kellogg 1988, secondary), and a plan written as a topic is not tested |
| [Leave a trail](principles/method/leave-a-trail.md) | a job leaves what was asked, what was found, what was produced and where it lives, so that a second person can resume it. | convention, untested. The guides agree with each other; no study tests that a set of files lets a second person resume |
| [Name the baseline](principles/method/name-the-baseline.md) | a review is finished when it names the baseline the result will be compared with, and says how. | convention, untested for the effect; the neglect of prior evidence is measured, descriptive |
| [Specify before building](principles/method/specify-before-building.md) | a project writes its scope, what is in and what is out and why, before the work starts. | supported with caveat for hasty specification as a major source of avoidable rework (an expert report, and one review limited to global software development); convention, untested for a written scope as the remedy |

<!-- principles:end -->

## Where the evidence is

Every principle links its review in [evidence/](evidence/README.md), and every work cited is listed once in the
[bibliography](evidence/bibliography.md).
