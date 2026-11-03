"""Project shape: a folder whose root declares the project shape has its six parts, and the review names a baseline.

A file is a project root when a line labelled `Shape:` links shapes/project.md (a skeleton inside fenced code
declares nothing). Its parts are the files of its own folder named in `[project_shape] parts`. A run with no error
guarantees, for each project root:
- the six parts exist (problem, scope, review, baseline, plan, trail) and the root links each one;
- each part announces the topic shape on a `Shape:` line, so a reader knows which blocks to expect;
- problem.md holds a line labelled Problem;
- scope.md holds a table with a row for what is in, a row for what is out, and a Why column;
- review.md holds the headings Frame, Literature review, State of the art and Position (the baseline is step 5, in
  baseline.md);
- baseline.md names one: a line labelled `Named baseline:` whose text is not empty or a placeholder, which is the
  exit test of the review (the review is finished when it can name the baseline);
- plan.md holds the headings Steps, Decided first and For the person to decide;
- trail.md holds the rows Asked, Found, Produced and Where it lives.
It warns, as heuristics, when the Problem is more than one sentence and when the baseline names no `Compared by:`
line. What it does not decide: that the baseline is the right one, or that the comparison was run (judgment).
Time O(project roots x size of their parts).
"""
from __future__ import annotations

import posixpath
import re
from pathlib import Path

from framework.check_api import Finding, files_in_scope, prose_only

NAME = "project-shape"
EXACT = True

DEFAULT_PARTS = ["problem.md", "scope.md", "review.md", "baseline.md", "plan.md", "trail.md"]
SHAPE_LINE = re.compile(r"\*\*Shape:\*\*\s*\[[^\]]*\]\(([^)\s]+)\)")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s#]+)(?:#[^)\s]*)?\)")
PLACEHOLDER = re.compile(r"^(none|tbd|todo|unknown|n/a|na|to be (named|decided)|not (yet )?named|\?+|-+|<.*>)\.?$",
                         re.IGNORECASE)


def declares(text: str, shape: str) -> bool:
    """True when a Shape line, outside fenced code, links shapes/<shape>.md (a relative link may reach it as ../<shape>.md)."""
    for link in SHAPE_LINE.findall(prose_only(text)):
        target = link.split("#")[0]
        if target.endswith(f"shapes/{shape}.md") or (not re.match(r"^[a-z]+:", target) and posixpath.basename(target) == f"{shape}.md"):
            return True
    return False


def label(text: str, name: str) -> tuple[int, str] | None:
    """The line number and text of `**Name:** text` or `**Name.** text`, or None."""
    for number, line in enumerate(prose_only(text).splitlines(), 1):
        found = re.match(rf"\s*(?:[-*]\s*)?\*\*{re.escape(name)}[.:]\*\*\s*(.*)$", line, re.IGNORECASE)
        if found:
            return number, found.group(1).strip()
    return None


def headings(text: str) -> set[str]:
    return {m.group(1).strip().lower() for m in re.finditer(r"^#{2,6}\s+(.*?)\s*$", prose_only(text), re.MULTILINE)}


def rows(text: str) -> list[list[str]]:
    """The cells of each table row, lower-cased, separator rows removed."""
    table = []
    for line in prose_only(text).splitlines():
        if line.strip().startswith("|"):
            cells = [cell.strip().strip("*").lower() for cell in line.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells if cell):
                table.append(cells)
    return table


def sentences(text: str) -> int:
    plain = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return len(re.findall(r"[.!?](?:\s+(?=[A-Z0-9*`\"(])|$)", plain.strip()))


def part_findings(name: str, path: str, text: str) -> list[Finding]:
    found = []
    if name == "problem.md":
        problem = label(text, "Problem")
        if problem is None or not problem[1]:
            found.append(Finding(NAME, path, 1, "no line labelled Problem: state the problem in one sentence"))
        elif sentences(problem[1]) > 1:
            found.append(Finding(NAME, path, problem[0], "the Problem runs past one sentence: cut it to one", "warning"))
    elif name == "scope.md":
        table = rows(text)
        firsts = [row[0] for row in table if row]
        if not table or not any("why" in cell for cell in table[0]):
            found.append(Finding(NAME, path, 1, "no scope table with a Why column: say why each row is in or out"))
        for side in ("in", "out"):
            if side not in firsts:
                found.append(Finding(NAME, path, 1, f"the scope table has no '{side}' row"))
    elif name == "review.md":
        have = headings(text)
        for step in ("Frame", "Literature review", "State of the art", "Position"):
            if step.lower() not in have:
                found.append(Finding(NAME, path, 1, f"the review lacks the step '{step}' as a heading"))
    elif name == "baseline.md":
        baseline = label(text, "Named baseline")
        if baseline is None or not baseline[1] or PLACEHOLDER.match(baseline[1]):
            found.append(Finding(NAME, path, baseline[0] if baseline else 1,
                                 "the baseline part names no baseline: the review is not finished until it can"))
        if label(text, "Compared by") is None:
            found.append(Finding(NAME, path, 1, "no line labelled Compared by: say how the result is set against the baseline",
                                 "warning"))
    elif name == "plan.md":
        have = headings(text)
        for part in ("Steps", "Decided first", "For the person to decide"):
            if part.lower() not in have:
                found.append(Finding(NAME, path, 1, f"the plan lacks the part '{part}' as a heading"))
    elif name == "trail.md":
        firsts = [row[0] for row in rows(text) if row]
        for item in ("asked", "found", "produced", "where it lives"):
            if item not in firsts:
                found.append(Finding(NAME, path, 1, f"the trail table has no '{item}' row"))
    return found


def check(root: Path, config: dict) -> list[Finding]:
    settings = config.get("project_shape", {})
    parts = settings.get("parts", DEFAULT_PARTS)
    findings = []
    for path in files_in_scope(root, config, {".md"}):
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        if not declares(text, "project"):
            continue
        folder = posixpath.dirname(path)
        linked = {posixpath.normpath(posixpath.join(folder, link)) for link in LINK.findall(prose_only(text))}
        for name in parts:
            part = posixpath.join(folder, name) if folder else name
            if not (root / part).is_file():
                findings.append(Finding(NAME, path, 1, f"the project lacks its part {name}"))
                continue
            if part not in linked:
                findings.append(Finding(NAME, path, 1, f"the root does not link {name}: a reader cannot reach the part"))
            body = (root / part).read_text(encoding="utf-8", errors="replace")
            if not declares(body, "topic"):
                findings.append(Finding(NAME, part, 1, "a part of a project announces the topic shape on a Shape line"))
            findings += part_findings(name, part, body)
    return findings
