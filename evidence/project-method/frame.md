# Frame: the problem and its names

Step 1 of the review on the method of a project, read on 2026-11-02. It states the problem, gives the field's names beside the repository's, and turns the front page's four questions into sub-questions.

**Shape:** [frame](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/frame.md)

## The problem in one sentence

How one person goes from a stated problem to a checked result with the fewest wasted round trips, and leaves a trail another person can resume.

## Names

One row per term. Every file of this folder uses these names.

| Term | What the field means by it | Where met |
|---|---|---|
| **design science research (DSR)** | research that builds an artifact to solve a stated problem and evaluates it | Hevner 2004; Peffers 2006 |
| **DSR process** | six activities: problem identification, objectives, design and development, demonstration, evaluation, communication | Peffers 2006 |
| **objectives of a solution** | what a good solution would do better than the current ones, quantitative or qualitative | Peffers 2006, activity 2 |
| **entry point** | the activity a project starts from; the model is nominally sequential, not required to be | Peffers 2006 |
| **literature review (research methods)** | a written search and synthesis of prior work, done before the work it informs | Webster 2002; Booth 2016 |
| **evidence-based research** | the call that no new study begins without a systematic review of the existing ones | Lund 2016 |
| **research waste** | effort lost to avoidable flaws in questions, design, conduct and reporting | Chalmers 2009; Macleod 2014 |
| **rework** | effort spent redoing work; **avoidable rework** could have been found earlier or avoided | Boehm 2001; Fairley 2005 |
| **delayed-issue effect** | the claim that a defect costs more the later it is found | Boehm 2001; Menzies 2017 |
| **heuristic** | a rule of thumb for solving a problem, such as drawing a figure or working backwards | Polya 1945; Schoenfeld 1985 |
| **personal software process (PSP)** | a method of planning, logging and reviewing one's own work as an engineer | Prechelt 2001b; Hayes 1997 |
| **reproducible research** | a project kept so that someone else can redo and follow it from its files | Noble 2009; Sandve 2013 |
| **project organization** | the folders, README, notebook and change log of one project | Noble 2009; Wilson 2017 |
| **resumption** | going back to a task after an interruption; its cost is the time to rebuild the goal | Altmann 2002; Parnin 2010 |
| **definition of done** | a stated quality standard that work must meet to count | Schwaber 2020 |
| **shaping** | making an idea concrete enough to bet on before building | Singer 2019 |
| **business success criteria** | the measure, set in the first phase, by which the result is judged | Chapman 2000 |

## The field's name against the repository's

- No single field owns the problem. Each part has its own name.
- The steps from problem to evaluated result are the **DSR process** in research, and the **project phases** in practice (CRISP-DM, Scrum).
- The review before building is **evidence-based research** and **research waste** in medicine; the repository calls it the literature review.
- The trail is **project organization** and **reproducible research**.
- The repository's word **project** matches Noble 2009 and Wilson 2017, who write "project" for one person's work. It differs from project management, whose frameworks address teams and organizations.
- Decision: the name stays. Record 0002 gives the reason. The review does not rename the repository.
- One word needs care. In this family, **baseline** is the method a result is compared with. In project management practice it often means an approved plan. This pass did not check that in a source.

## Sub-questions

| Front-page question | Sub-questions of this review |
|---|---|
| Round trips | Q1a: which steps written first are measured to cut rework? Q1b: what causes rework? Q1c: what do the process models and frameworks prescribe before building? |
| Topics | Q2: does writing a plan or scope as a structured text change the outcome? |
| The trail | Q3: what do practice guides leave behind, and what is measured about resuming? |
| The boundary | Q4: where do the process models stop and the document genres begin? |

## Not held here

- The outline and the shallow hierarchy are reviewed in reader-ergonomics, as [overview first](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/principles/document/overview-first.md) and [shallow outline](https://github.com/Tewf/reader-ergonomics/blob/65e42472e2d4cbfd994c2a86e95a47e5dc7301ca/principles/document/shallow-outline.md). This review links them.
- The decision record belongs to reader-ergonomics-software-design.

## See also

[Protocol](protocol.md); [sources](sources.md).
