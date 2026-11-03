# Project

[![Checks against reader-ergonomics](https://github.com/Tewf/reader-ergonomics-project/actions/workflows/checks.yml/badge.svg)](https://github.com/Tewf/reader-ergonomics-project/actions/workflows/checks.yml)
[![Site](https://github.com/Tewf/reader-ergonomics-project/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/reader-ergonomics-project/)

How one person prepares and runs a **project**, from a problem to its result, with the fewest round trips. The steps
are the scope, the literature review, the baseline, the plan, the execution and its refinement, each written as a
topic. The folder a job leaves behind is part of it, so that someone else can resume the work. The reasoning of a project is the subject; the
documents it produces belong to the genres.

This page in French: [README.fr.md](README.fr.md).

> **Status (2026-11-03):** version 0.1.0. Built: the first pass of the literature review, 40 sources, five steps, a named baseline;
> the [card](standard.md) with four principles; the [project shape](shapes/project.md) with one filled example and a check with 19 unit tests.
> Open: the comparison with the baseline is named, not run, and no step is measured. The name stays, for the reason in decision 0002. It is not an official
> standard, not a peer-reviewed study and not a new result.
>
> **How it is made:** with Claude, an AI assistant by Anthropic, under the maintainer's direction, the way
> reader-ergonomics was made. Corrections are welcome as issues.

## Take it

The project shape is meant to be copied and kept as your own. Copy it from a tagged release
([tags](https://github.com/Tewf/reader-ergonomics-project/tags)), so a later change here never changes your copy.

1. Copy [shapes/project.md](shapes/project.md), the shape, and [checks/local/project_shape.py](checks/local/project_shape.py),
   the check, into the same paths of your repository. [shapes/examples/first-job/](shapes/examples/first-job/) is a
   filled project to start from.
2. Write one folder per project, with the six topics: problem, scope, review, baseline, plan and trail.
3. Add `checks/config.toml`; the last two tables are for a repository with no site stylesheet:

   ```toml
   extends = "reader-ergonomics"

   [project_shape]
   parts = ["problem.md", "scope.md", "review.md", "baseline.md", "plan.md", "trail.md"]

   [readable_measure]
   stylesheets = []

   [sufficient_contrast]
   stylesheets = []
   ```

4. Pin the standard by commit (`ref:` in [checks.yml](.github/workflows/checks.yml)) and run its checks; the project
   check runs beside them:

   ```sh
   git clone https://github.com/Tewf/reader-ergonomics
   git -C reader-ergonomics checkout 2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a
   python3 reader-ergonomics/checks/run.py path/to/your/repository
   ```

5. How to take your own version, and where a disagreement goes: the standard's
   [Take your own version](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/README.md#take-your-own-version).

## Where it sits

![ai-augmented-project uses reader-ergonomics-project, which builds on reader-ergonomics-topic, which obeys reader-ergonomics; every arrow points down.](where-it-sits.svg)

<details>
<summary>Graphviz source</summary>

```dot
// Where reader-ergonomics-project sits: what uses it, what it uses. Colours: one per family, named in each box;
// reader-ergonomics family blue, AI-augmented family green; this repository has the thick border.
digraph where_it_sits {
  graph [rankdir=TB, nodesep=0.45, ranksep=0.5, bgcolor="white", pad=0.2, fontname="Inter"];
  node  [shape=box, style="rounded,filled", fontname="Inter", fontsize=13, margin="0.2,0.1", penwidth=1.5, fontcolor="#1F2328"];
  edge  [fontname="Inter", fontsize=11, color="#3D434B", fontcolor="#55575F", penwidth=1.3, arrowsize=0.8];
  AP [label=<<b>ai-augmented-project</b><br/><font point-size="11" color="#55575F">AI-augmented family: the same project,</font><br/><font point-size="11" color="#55575F">with a model and a machine set up</font>>, fillcolor="#E6F2EA", color="#2E7D4F"];
  P  [label=<<b>reader-ergonomics-project</b><br/><font point-size="11" color="#55575F">reader-ergonomics family: one person,</font><br/><font point-size="11" color="#55575F">from problem to result, as topics</font>>, fillcolor="#E8EEF8", color="#2F5DA8", penwidth=2.6];
  T  [label=<<b>reader-ergonomics-topic</b><br/><font point-size="11" color="#55575F">the unit of writing every step follows</font>>, fillcolor="#E8EEF8", color="#2F5DA8"];
  RE [label=<<b>reader-ergonomics</b><br/><font point-size="11" color="#55575F">how any text serves its reader</font>>, fillcolor="#E8EEF8", color="#2F5DA8"];
  AP -> P [label=" uses"];
  P -> T [label=" builds on"];
  T -> RE [label=" obeys"];
}
```

</details>

- **It builds on the [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md)** (reader-ergonomics-topic v0.6.1): every step of a
  project is a topic, with its title, its summary and its parts.
- **It obeys [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/standard.md)** (v1.21.0) and runs its checks in CI.
- **It links down only.** Both are pinned by commit; neither links up to this repository. Its counterpart with a model
  in the loop is [ai-augmented-project](https://github.com/Tewf/ai-augmented-project), one level above.
- **The family it mirrors** is mapped at [ai-augmented](https://github.com/Tewf/ai-augmented); the bridge between the two is
  [reader-ergonomics-blueprint](https://github.com/Tewf/reader-ergonomics-blueprint), the topic with a checker on each part.

## Scope

| | What | Why |
|---|---|---|
| in | the steps from a problem to its result: scope, review, baseline, plan, execution, refinement | they are what every project repeats, whatever its genre |
| in | each step written as a topic: one claim, its summary, its parts | the person does not get lost, and a reader can follow the reasoning |
| in | what cuts round trips: what is decided before starting, what is the person's to decide, when the baseline is named | the cost of a project is mostly the work redone |
| in | the folder a job leaves behind: what was asked, what was found, what was produced, where it lives | a second person, or the same one later, resumes from it |
| out | the writing of any one document: a report, a design, a talk, a proof | the [reader-ergonomics family](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/extending.md) holds each genre's shape |
| out | the design document and the decision record | [reader-ergonomics-software-design](https://github.com/Tewf/reader-ergonomics-software-design) holds them; this links them where a step needs one |
| out | a language model or a machine in the loop | [ai-augmented-project](https://github.com/Tewf/ai-augmented-project) |

## The first job: a literature review

A first pass is done, in [evidence/project-method](evidence/project-method/). It follows the order of a thesis review, and it is finished when it can name the baseline.

1. **Frame:** the problem in one sentence, and what each field calls it. The review found no single name, so the
   repository keeps its own.
2. **Review:** each name below, searched by its academic name, its acronym and its author; surveys first.
   - design science research, and its process models;
   - research methodology: how a thesis is framed, reviewed and positioned before anything is built;
   - heuristics for solving problems, Polya first;
   - project and process frameworks, read as grey literature: what they prescribe, what was measured;
   - rework and its causes in software and research projects;
   - what reader-ergonomics already holds: overview first, the shallow outline, the decision record.
3. **State of the art, and the case against.**
4. **Position:** what this repository asks that the field does not already answer.
5. **Baseline:** the method the maintainer already follows, written down, compared with the best process the review
   found.

## What the review found

A first pass of 40 sources, 35 formal and 5 grey; sixteen formal works are located, not opened ([protocol](evidence/project-method/protocol.md)).

- **No step is measured.** No source isolates a written scope, a named baseline or a list of the person's decisions and
  measures rework. These stay conventions, untested ([review](evidence/project-method/review.md)).
- **A major cause of avoidable rework is hasty specification.** An expert report puts avoidable rework at 40 to 50 percent of effort and
  names hastily specified requirements as a major source (Boehm 2001). Menzies 2017 found no delayed-issue effect in 171
  projects, so a fixed 100-times cost of late defects is not supported ([against](evidence/project-method/against.md)).
- **The design science process has no literature-review step.** It names objectives and evaluation against them, so a
  comparison target is there, but no activity for a literature review (Peffers 2006). A 2014 review of design science
  experiments gives questions for evaluation, and no review step (Mettler 2014).
- **The trail is practice without a test.** Guides agree on a README, a folder per project and a dated log (Noble 2009;
  Wilson 2017). No study tests that a second person can resume from them.
- **The method ends where the genre begins.** The process ends in communication; a document's shape is outside it
  ([position](evidence/project-method/position.md)).

Answers to the four questions are in [the review](evidence/project-method/review.md).

## The baseline

**B1** is the six activities of the design science research process (Peffers 2006) for the steps, and the project
organization of Noble 2009 and Wilson 2017 for the trail. The maintainer's practice, written down for this review, is
compared with it by paired jobs: round trips, rework and the questions a second person asks. The comparison is named,
not run ([baseline](evidence/project-method/baseline.md)).

## Questions the review must answer

- **Round trips.** Which steps, when written before the work starts, are measured to cut rework: the scope, the
  baseline, the list of decisions that are the person's?
- **Topics.** Does writing the scope and the plan as topics change the outcome, or only the reading?
- **The trail.** What must a job leave behind for a second person to resume it without asking? Four files are the
  maintainer's current answer: the brief, the notes, the output, the pointers.
- **The boundary.** Where does the method stop and the genre shapes begin? A plan is a topic; a design document is
  software-design's.

## Check it

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py path/to/this/repository
```

CI runs the same checks on every push, and a run fails on any error
([checks.yml](https://github.com/Tewf/reader-ergonomics-project/blob/master/.github/workflows/checks.yml)). Every push
to master also renders the site, [tewf.github.io/reader-ergonomics-project](https://tewf.github.io/reader-ergonomics-project/)
([pages.yml](https://github.com/Tewf/reader-ergonomics-project/blob/master/.github/workflows/pages.yml)).

## Contents

| Part | Summary |
|---|---|
| [evidence](evidence/) | the review behind this repository: a first pass on the method of a project, and the bibliography |
| [standard](standard.md) | the card: four principles with their grades, read after the standard and the topic |
| [principles](principles/) | one file per principle: the claim, its grade, its evidence and its check |
| [shapes](shapes/) | the project shape: six topics from a problem to its result, a filled example, and the check that reads them |
| [decisions](decisions/) | one record per choice that shapes this repository, each opening with the decision in one sentence |

## Licence

Code under the [Apache License 2.0](LICENSE); prose under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Reuse it as you wish,
with credit to this repository; [CITATION.cff](CITATION.cff) gives a citation if you need one.
