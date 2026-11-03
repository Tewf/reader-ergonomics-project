# Shape: project

One project, from a problem to its result, written as a tree of six topics. Its first reader is the person who does the
work, its second is whoever resumes it later. The root holds the project and lists its parts; each part is a topic of
its own.

**Shape:** [topic](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md), as every part here. A project root announces this shape the same way, on a line labelled `Shape:`.

## When to use it

- Before a job that takes more than one sitting, or that someone else may resume.
- When the result will be judged against something, so a baseline is worth naming.
- Not for the document the project produces: a report, a design or a talk keeps the shape of its genre.
- Not for one choice made along the way: that is a decision record.

## The skeleton

```markdown
<folder of the project>/
  README.md    the root: title, summary, Shape line, Contents table of the six parts, See also
  problem.md   the problem in one sentence, and what the field calls it
  scope.md     what is in, what is out, and why
  review.md    the review's first four steps: frame, literature review, state of the art, position
  baseline.md  step five, the exit test: the baseline named, and how the result is compared
  plan.md      the steps, what is decided first, what is left to the person
  trail.md     what was asked, found, produced, and where it lives
```

Every file opens as a topic does: one title, then a summary, then the body, and a `Shape:` line linking the topic
shape. The root's Shape line links this shape.

## The parts

| Part | Holds | Why this part | Grade |
|---|---|---|---|
| problem | a line labelled `Problem:`, one sentence | the design science process starts at problem identification (Peffers 2006) | supported with caveat, as a process model; the one-sentence form is a convention |
| scope | a table: in, out, and a Why column | the objectives of a solution come before design (Peffers 2006) | convention, untested |
| review | the headings Frame, Literature review, State of the art, Position | the maintainer's practice, written down for the [review](../evidence/project-method/review.md); no step is measured | convention, untested |
| baseline | a line labelled `Named baseline:` and one labelled `Compared by:` | the review is finished when it can name the baseline ([baseline](../evidence/project-method/baseline.md)) | convention, untested |
| plan | the headings Steps, Decided first, For the person to decide | the person's decisions are settled before the work, so they cost no round trip | convention, untested |
| trail | a table with the rows Asked, Found, Produced, Where it lives | an overview file, a folder per project and a dated log (Noble 2009; Wilson 2017) | convention, adopted by guides; resumption untested |

No source isolates a written scope or a named baseline and measures rework
([the review's finding](../evidence/project-method/review.md); the grades are defined in the [position](../evidence/project-method/position.md)). The shape is a convention to test, not a result.

## The rules

A repository that holds several projects in this shape adds their skeleton files, such as `0*/problem.md`, to `[duplication] exempt` in `checks/config.toml`, because the skeleton is one shape, not one fact copied.

## Where it stops

The shape ends where the genres begin. The plan may name the document the project will produce and link the shape of
its genre; it does not restate it. A software design and its decision records are the business of
[reader-ergonomics-software-design](https://github.com/Tewf/reader-ergonomics-software-design).

## A filled example

[The first job of this repository](examples/first-job/README.md), written in the shape: the literature review that
produced the repository's evidence.

## The check

[`checks/local/project_shape.py`](../checks/local/project_shape.py) reads every file that declares this shape, and
runs on the parts `[project_shape] parts` names in `checks/config.toml`:

| Rule | Kind |
|---|---|
| the six parts exist beside the root, and the root links each | error |
| each part announces the topic shape on a `Shape:` line | error |
| problem: a line labelled `Problem:` | error |
| problem: more than one sentence | warning |
| scope: a table with an `in` row, an `out` row and a Why column | error |
| review: the four step headings | error |
| baseline: a `Named baseline:` line that is not empty or a placeholder | error |
| baseline: no `Compared by:` line | warning |
| plan: the three headings | error |
| trail: the four rows | error |

What a run with no error guarantees: a project that declares the shape has every part, and its review names a baseline.
It does not guarantee that the baseline is the right one, that the comparison was run, or that a part says anything
true; those are judgment. A skeleton inside fenced code, as above, declares nothing.

## See also

[The front page](../README.md); [the baseline of the review](../evidence/project-method/baseline.md);
[the topic shape](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/shapes/topic.md).
