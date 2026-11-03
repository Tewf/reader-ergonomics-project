# Review

Step 2 of the review: what each strand holds, by question. Existing reviews come first. Terms are in [frame](frame.md); grades and reading depth per source are in [sources](sources.md). A number from an abstract or a summary is marked (secondary).

**Shape:** [review](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/review.md)

## Strand 0: existing reviews

- Nawaz 2022 reviews 23 studies of rework, 2009 to 2020, in global software development only. It sorts causes into 6 categories; communication and requirements management are reported most (secondary).
- Dybå 2008 reviews agile studies; its abstract was not retrieved.
- Hembree 1992 is a meta-analysis of problem-solving research; two secondary summaries put it at 487 reports.
- Chalmers 2009, Macleod 2014 and Glasziou 2014 are a series on research waste.
- No review of design science process models turned up, and none of what a project trail must hold.

## Strand A: the process from problem to result

- Peffers 2006 synthesises seven process models into six activities: problem identification and motivation, objectives of a solution, design and development, demonstration, evaluation, communication.
- The order is nominal. A project may start at any activity and move outward; Peffers 2006 lists four entry points.
- Objectives are inferred from the problem. They can be quantitative, in terms in which a solution would be better than current ones.
- That step needs "knowledge of the state of problems and current solutions". The comparison target sits there, with no review step named.
- Evaluation compares the objectives with observed results, then decides whether to iterate to design or to go on.
- Communication is the last activity, and the paper may follow its structure.
- Grade: convention. The model is a synthesis and a demonstration on two cases, not a test.
- Mettler 2014 reviews experiments in design science and proposes an evaluation framework: questions to ask and pitfalls to avoid (secondary).
- The abstract names no review step and no comparison target, so the framework sharpens evaluation without adding the missing step.
- Hevner 2004, Gregor 2013 and Wieringa 2014 were located, not opened.

## Strand B: reviewing before building

- Lund 2016 makes the call: "no new studies should be done without a systematic review of existing evidence".
- Glasziou 2014 reports, in its abstract, that investigators of new trials rarely set their findings in the context of a systematic review.
- It reports that 40 to 89 percent of published trials were not replicable, because their interventions were poorly described (secondary).
- The evidence measures the neglect. No source found measures that doing the review changes the outcome of a project.
- Grade: convention, untested for effect; the neglect is measured, descriptive.
- Webster 2002 and Booth 2016 were located as guides to reviewing; not opened.

## Strand C: heuristics

- Polya 1945 and Schoenfeld 1985 were located, not opened.
- Hembree 1992, in secondary summaries: checking work, drawing diagrams and using heuristics go with higher problem-solving scores.
- The same summaries say heuristics had a clear effect only where teachers were trained in them, and that students told to follow fixed steps scored lower than students using flexible approaches.
- Hohn 2002 reports two controlled experiments with 223 elementary students (secondary).
- A named five-phase strategy, taught over several lessons, did better than traditional instruction, short term and delayed.
- The abstract does not say whether students followed the phases as fixed steps, so the older warning about fixed steps is not tested here.
- Grade: measured, for students of mathematics, now in two controlled experiments and the summaries; transfer to a person's own project is not tested.

## Strand D: frameworks and personal process

| Source | What it prescribes before building | Measured |
|---|---|---|
| Schwaber 2020 | a Product Goal, a Sprint Goal and a Definition of Done, as commitments; a sprint of one month or less | nothing in the guide |
| Singer 2019 | shaping an idea before a bet; a pitch; a six-week cycle and a two-week cool-down | nothing in the contents page read; below the threshold on the second rating, an example of practice only |
| Chapman 2000 | phase 1: business objectives, situation, success criteria, a project plan; the process loops back | nothing in the sections read |
| Ubl 2020 | a design doc before coding, to find design issues while changes are cheap; an example only, below the threshold | the owner's claim |
| Serrador 2015 | agile use against project success | correlational, 1,002 projects (secondary) |
| Prechelt 2001b | a taught personal process: plan, log, review | controlled experiment |

- Prechelt 2001b found positive effects, but smaller than proponents assume. The trained group estimated productivity better and made fewer trivial mistakes.
- CRISP-DM names success criteria in phase 1. It is the closest practice to a named baseline.
- Grade for the prescriptions: convention, untested.

## Strand E: rework and its causes

- Boehm 2001, section TWO: current projects spend about 40 to 50 percent of effort on avoidable rework. Section ONE: a late fix is "often" 100 times dearer, and 5:1 for small noncritical systems.
- Section THREE: about 80 percent of avoidable rework comes from 20 percent of the defects. Two major sources are hastily specified requirements and nominal-case design.
- Fairley 2005 adds that rework is not all bad: iteration needs some, and too little may signal too little review (abstract).
- Hofmann 2001 quotes Jones: requirements engineering is deficient in more than 75 percent of enterprises (secondary).
- Grade: the shares are expert reports. The cause, requirements specified in haste, is supported with caveat by Boehm and by Nawaz 2022 for global development.

## Strand F: the trail

- Noble 2009: one folder per project with data, results, doc and source; dated experiment folders; a dated notebook. The reader is "someone else", often the author later.
- Wilson 2017: an overview file (3a), a folder per project (4a), a change log serving as a lab notebook (5f). Its workshops reached over 11,000 people since 2010.
- Sandve 2013: ten rules, first "for every result, keep track of how it was produced".
- Altmann 2002 models memory for goals and the cost of interruption, fitted to a puzzle task. Parnin 2010 on programmers was located, not opened.
- Grade: convention, untested. These guides agree with each other. No study tests that a set of files lets a second person resume.

## Answers to the four questions

| Question | Answer | Grade |
|---|---|---|
| Q1 round trips | the process models name objectives and evaluation; the cause of avoidable rework is hasty specification; the benefit of a written scope, baseline or decision list is not measured | convention, untested |
| Q2 topics | an outline raised judged writing quality in an experiment (secondary, Kellogg 1988); a plan written as a topic is not tested | not tested; outline measured for writing |
| Q3 trail | practice guides converge on a README, a folder per project and a dated log | convention, untested |
| Q4 boundary | the DSR process ends in communication; a document's shape is outside the process | convention |

## See also

[State of the art](state-of-the-art.md); [against](against.md).
