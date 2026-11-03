# Protocol: how the pool was built

Every search, count and rule of this first pass, run on 2026-11-02 by one reviewer. Terms are in [frame](frame.md); the pool is in [sources](sources.md). The method the family's reviews share is in the [topic's evidence](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/evidence/README.md).

**Shape:** [protocol](https://github.com/Tewf/reader-ergonomics-review/blob/a7f405f26f14cd188291e2a86b630121c4302a94/shapes/protocol.md)

## 1. Why grey literature

Garousi 2019, Table 4, answered for this topic.

| # | Question | Answer |
|---|---|---|
| 1 | Complex, not solvable from formal literature alone? | yes: the process frameworks are written by practitioners |
| 2 | Lack of volume or quality of evidence? | yes: no study isolates scope, baseline or trail |
| 3 | Context important? | yes: research, data mining and product work differ |
| 4 | Corroborate research with practice? | yes: guides against measured projects |
| 5 | Challenge practice with research, or the reverse? | yes: the 100-times claim against a 171-project study |
| 6 | Would a synthesis serve both communities? | yes |
| 7 | Large practitioner volume? | yes: Scrum and CRISP-DM are widely used; no count was taken |

## 2. Review questions

Q1 to Q4 of [frame](frame.md).

## 3. Existing reviews

- Searched first, by the strings S1, S3, S3b and S11 below.
- Found: a rework review limited to global software development (Nawaz 2022), an agile review (Dybå 2008), a problem-solving meta-analysis (Hembree 1992), a waste series (Chalmers 2009, Macleod 2014, Glasziou 2014).
- Not found: a review of design science process models. One web search returned primary papers and uses of the process, no review.
- Not found: a review of what a project trail must hold for resumption.

## 4. Formal search

Counts are from OpenAlex, title and abstract, phrase search, on 2026-11-02, with no key and no identity. Records were looked up on Crossref; abstracts on OpenAlex and Europe PMC.

| ID | String | Count | Result |
|---|---|---|---|
| S1 | "design science research" process | 4,896 | Hevner 2004, Gregor 2013, Wieringa 2014 |
| S2 | "design science research methodology" | 2,530 | Peffers 2006, 2007 |
| S2b | "avoidable rework" | 177 | Boehm 2001 |
| S3 | "research waste" | 1,346 | Chalmers 2009, Macleod 2014, Glasziou 2014, Lund 2016 |
| S3b | "software rework" | 24 | Fairley 2005, Nawaz 2022 |
| S3c | "systematic review" "before new studies" | 2 | Lund 2016 |
| S4 | "heuristics" "problem solving" meta-analysis mathematics | 9 | Hembree 1992 |
| S5 | "reproducible research" "project organization" | 4 | Noble 2009, Sandve 2013, Wilson 2017 |
| S6 | "personal software process" | 429 | Prechelt 2001b, Hayes 1997 |
| S7 | "multivocal literature review" | 488 | method only; Garousi 2019 |
| S11 | "project success" "planning" software | 527 | Serrador 2015, Hofmann 2001, Dybå 2008 |
| S12 | "delayed issue effect" | 1 | Menzies 2017 |
| S13 | "resumption" "interrupted" programming | 137 | Parnin 2010, Altmann 2002 |
| S14 | "implementation intentions" meta-analysis | 71 | screened; none included |

- Zero results was not read as absence: S3c has 2 hits and the work was found by S3.
- Three ways: each topic was searched by its academic name, its acronym where one exists (DSR, PSP) and an author (Peffers, Boehm, Hembree).
- Snowballing: backward from Peffers 2006, which names Hevner 2004. Forward snowballing was done for three sources, in section 11.

## 5. Grey search

| ID | Where | String or visit | Result |
|---|---|---|---|
| S8 | web search engine | CRISP-DM 1.0 step-by-step data mining guide | Chapman 2000 |
| S9 | web search engine | Design Docs at Google | Ubl 2020 |
| S10 | web search engine | software rework systematic literature review causes | Nawaz 2022; Boehm 2001 |
| S15 | web search engine | Serrador Pinto Does Agile work | summaries of Serrador 2015 |
| D1 to D4 | direct visits | the Scrum guide; the Shape Up book; the CRISP-DM document; the design-docs post | Schwaber 2020, Singer 2019, Chapman 2000, Ubl 2020 |

## 6. Stopping rule

- Effort bounded: up to 10 results per string.
- Saturation: stop a string after 5 consecutive results that add no concept.
- Pool bounded: 25 to 40 sources for a first pass; 40 are kept.

## 7. Selection

- Include: a work on the process of a project, on rework, on review before building, on problem solving, on a project's trail, or on resumption.
- Exclude: a work on one genre of document, a model in the loop, or a team organization.
- Grey sources must be a guide, a book, a standard or a stated practice, not a seller's page.

## 8. Quality of grey sources

Garousi 2019, Table 7, 20 criteria, threshold 10. Scores are in [sources](sources.md). The first reviewer's scores were checked by a second rating and reread (section 12). After both, two grey sources fall below the threshold: Singer 2019 (9) and Ubl 2020 (9.5).

## 9. Extraction and synthesis

- Extracted: the steps prescribed, the figures given, the design of any measurement.
- Synthesis is narrative by question, traceable through sources.

## 10. Not searched, and limits

- Not searched: Q/A sites, forums, talks, patents, practitioner surveys, PMBOK and PRINCE2 (paywalled), ISO 21502 (paywalled).
- Not done: a second rater for the formal sources; forward snowballing beyond the three sources in section 11.
- Sixteen formal works are located only; their claims here are leads, not findings.
- One reviewer. Search engines personalise and change; counts differ on a repeat.
- Counts of titles screened per string were not logged.
- No sign-in, account or identity was sent to any service.

## 11. Forward citations

Run on 2026-11-03 through OpenAlex, with the key read from the environment. No account or identity was sent.

The brief asks for the three sources the review cites most. In [review](review.md), five sources are cited twice: Nawaz 2022, Hembree 1992, Peffers 2006, Glasziou 2014 and Prechelt 2001b.

The tie was broken in two steps:

- Nawaz 2022 and Hembree 1992 are each cited in two strands. The other three are cited in one.
- Peffers 2006 is then the most used across the repository, in the frame, the position, the baseline and the shapes.

| Source | OpenAlex record | Citing works | Screened |
|---|---|---|---|
| Nawaz 2022 | W4200449942 | 7 | all 7, by title |
| Hembree 1992 | W2020071675 | 171 | all 171, by title |
| Peffers 2006 | W2311045093, the arXiv record of the paper | 480 | the 200 most cited, by title |

- Strings: a citation filter on each record's identifier, sorted by citation count. Titles were read in that order.
- The DESRIST paper has no separate record in OpenAlex under its title. A title search limited to 2006 found no match, so the arXiv record was used. Its citing works are not all the works of the 2006 paper.
- Titles of 378 works were read. Six abstracts were read.
- Four candidates had no abstract in their record. Their titles were read only: a planning case study (2015), a taxonomy of study design (2022), criteria of progress for design theories (2010) and a note on practitioner design science (2017).
- Stop rule: not needed for the two complete lists. Of the 480 citing works of Peffers 2006, the 280 least cited were not read.

Added, with the abstract read:

- Hohn 2002, from Hembree 1992: a controlled comparison of a taught strategy with traditional instruction.
- Mettler 2014, from Peffers 2006: a review of experiments in design science, with an evaluation framework.

Each changes or sharpens one finding in [review](review.md).

Screened, not added, with the abstract read: a 2006 study of heuristic literacy, a 2026 review of 104 articles on teacher knowledge, and a 2025 study of rework causes. They sharpen strands C and E.

They stay out because the pool is held at 40, the bound in section 6. They are the first candidates for a later pass.

Screened, not added, from the title of a 2025 requirements paper, which is not in the rework strand.

Numbers read in abstracts are marked secondary. Hohn 2002 reports two experiments with 223 elementary students (secondary).

Not searched: other citation indexes, and the citing works of the other 30 sources, which the brief did not ask for.

## 12. Second rating of the grey sources

A second rater scored each grey source blind. It saw the criteria of section 8 and one source's text, nothing else, and it did not see the first scores. Each source was one request, so four requests were made. Each request asked for the eight subtotals, the total and the threshold decision.

The text given was:

- Schwaber 2020: the whole guide, 25,088 characters.
- Singer 2019: the contents page of the web edition, 4,047 characters. The page holds no more text.
- Chapman 2000: the first 25,000 of 174,000 characters: the introduction and the contents.
- Ubl 2020: the first 25,000 of 29,035 characters.

**Agreement, before any reread.** The total scores were 12 and 8, 12.5 and 0, 15.5 and 11.5, and 9 and 3: a mean absolute difference of 6.6 on the total.

| Group | Mean absolute difference over the four sources |
|---|---|
| A authority | 1.75 |
| M methodology | 1.38 |
| O objectivity | 1.25 |
| D date | 0.38 |
| P position | 0.5 |
| N novelty | 1.5 |
| I impact | 1.0 |
| T outlet | 0.38 |

Across the 32 group subtotals the mean absolute difference is 1.0.

On the threshold decision, the two raters agreed on two of four sources: Chapman 2000 above, Ubl 2020 below. Kappa is 0.2. With four sources this is too few to read further; it is reported as it is.

**Resolution.** Every source differed by more than 3 points on the total, so each was reread whole, group by group. A score changed only with the reason written here.

- **Singer 2019, 12.5 to 9.** A 3 to 2: the publisher is the company itself (A1 0.5), and no other work is named (A3 0). M 2.5 to 4: the contents name a stated method (shaping and betting, M2 1) and three case studies (M6 1). O 2 to 0: a contents page shows no balance, objectivity or conclusions, and a part not seen scores 0. D 0.5 to 0: the page gives no date. P 0.5 to 0: no related source is named. I 1 to 0: no citation or adoption count is shown. Below the threshold: an example of practice only. The first reviewer's notes mention definitions that the page does not contain.
- **Chapman 2000, 15.5 to 14.5.** A 4 to 3: no other work of the authors is named in the text read. M 2.5 to 5: the introduction, now in view, states a limit, validation on a narrow set of projects (M4), and names use at three companies (M6). O 3 to 1.5: the authors' firms sell the software and services the guide describes (O3 0). P 1 to 0: no related method is named in the text read. Above the threshold; the grade does not change.
- **Schwaber 2020, 12 to 10.** A 4 to 2.5: the guide is published by its own authors (A1 0.5), and no other work is named (A3 0). M 1.5 to 2: the aim and the question of the guide are in its opening (M1 and M5). O 2 to 1.5: the guide weighs no alternative (O1 0). P 0.5 to 0: no related source is named in the text. Above the threshold, at 10.
- **Ubl 2020, 9 to 9.5.** A 2.5 to 1: a personal blog (A1 0); the author writes as an insider with no byline in the text (A2 0.5). M 1 to 4: the whole post, not the first section, states its aim, its limit (writing a design doc is overhead), a question and a case (Google). O 2 to 1: the post weighs overhead against benefit (O1 0.5), and it describes its author's employer (O3 0). D stays at 1: the page's structured data state the publication date, 2020-07-06, though the body does not. Below the threshold: an example of practice only.

**What the disagreement was about.** The second rater scored the text as if nothing else were given. It gave 0 to parts that the text does show: the contents of Singer 2019, and the author's insider position in Ubl 2020.

The first reviewer's scores on Singer 2019 rested in part on material outside the text read. The reread removed that part.

**Limits.**

- One of the two raters is a language model, so the second rating is not fully independent of the first.
- The first reviewer had read some sources only in part. The reread read more, so the final scores use more text than the blind rating. The table of section 12 records both.
- Four sources give too few cases for kappa.
- The bibliography link for Chapman 2000 returned 404 on 2026-11-03. The bibliography now links an archived copy of 2021, which is the file read here.
- The Scrum guide's outlet tier is 2, a company's own page, as its score of 0.5 already assumed. The label in the first table said tier 1 and is corrected.
