# Protocol: how the pool was built

Every search, count and rule of this first pass, run on 2026-11-02 by one reviewer. Terms are in [frame](frame.md); the pool is in [sources](sources.md). The method the family's reviews share is in the [topic's evidence](https://github.com/Tewf/reader-ergonomics-topic/blob/86e14fe9a1a9877d6a87a2f8b4e8713f98724b5a/evidence/README.md).

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
- Snowballing: backward from Peffers 2006, which names Hevner 2004. No forward snowballing was done.

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
- Pool bounded: 25 to 40 sources for a first pass; 38 were kept.

## 7. Selection

- Include: a work on the process of a project, on rework, on review before building, on problem solving, on a project's trail, or on resumption.
- Exclude: a work on one genre of document, a model in the loop, or a team organization.
- Grey sources must be a guide, a book, a standard or a stated practice, not a seller's page.

## 8. Quality of grey sources

Garousi 2019, Table 7, 20 criteria, threshold 10. Scores are in [sources](sources.md). One grey source, Ubl 2020, falls below it.

## 9. Extraction and synthesis

- Extracted: the steps prescribed, the figures given, the design of any measurement.
- Synthesis is narrative by question, traceable through sources.

## 10. Not searched, and limits

- Not searched: Q/A sites, forums, talks, patents, practitioner surveys, PMBOK and PRINCE2 (paywalled), ISO 21502 (paywalled).
- Not done: second rater, forward snowballing.
- Sixteen formal works are located only; their claims here are leads, not findings.
- One reviewer. Search engines personalise and change; counts differ on a repeat.
- Counts of titles screened per string were not logged.
- No sign-in, account or identity was sent to any service.
