#!/usr/bin/env python3
"""Mechanical lint for the wiki. Semantic checks (contradictions, stale claims) are the agent's job.

Checks:
  - duplicate basenames (wikilinks resolve by basename)
  - broken [[wikilinks]] (target basename doesn't exist in wiki/ or raw/)
  - orphan wiki pages (no inbound links from any other wiki page)
  - wiki pages missing from wiki/index.md, and index links pointing nowhere
  - missing / malformed frontmatter (required keys)
  - raw sources with no corresponding wiki/sources page (unprocessed)
Usage: python3 scripts/lint.py   (exit code 1 if any problems)
"""
import os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI, RAW = ROOT / "wiki", ROOT / "raw"
SPECIAL = {"index", "log", "overview"}
REQUIRED = ["title", "type", "created", "updated", "sources", "related"]
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)

def basenames(d, problems=None):
    out = {}
    for p in d.rglob("*.md"):
        if p.stem in out and problems is not None:
            problems.append(f"duplicate basename  {out[p.stem].relative_to(ROOT)} and {p.relative_to(ROOT)}")
        out[p.stem] = p
    return out

def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)

def main():
    problems = []
    wiki, raw = basenames(WIKI, problems), basenames(RAW, problems)
    known = set(wiki) | set(raw)
    inbound = {k: 0 for k in wiki}
    for stem, path in wiki.items():
        text = path.read_text(encoding="utf-8")
        body = strip_code(text)
        for target in {m.group(1).strip() for m in LINK_RE.finditer(body)}:
            if target not in known:
                problems.append(f"broken link  {path.relative_to(ROOT)} -> [[{target}]]")
            elif target in inbound and target != stem:
                inbound[target] += 1
        if stem in SPECIAL:
            continue
        m = FM_RE.match(text)
        if not m:
            problems.append(f"no frontmatter  {path.relative_to(ROOT)}")
        else:
            keys = {l.split(":", 1)[0].strip() for l in m.group(1).splitlines() if ":" in l}
            for k in REQUIRED:
                if k not in keys:
                    problems.append(f"frontmatter missing '{k}'  {path.relative_to(ROOT)}")
    for stem, n in inbound.items():
        if n == 0 and stem not in SPECIAL:
            problems.append(f"orphan (no inbound links)  {wiki[stem].relative_to(ROOT)}")
    index = strip_code((WIKI / "index.md").read_text(encoding="utf-8"))
    indexed = {m.group(1).strip() for m in LINK_RE.finditer(index)}
    for stem in wiki:
        if stem not in SPECIAL and stem not in indexed:
            problems.append(f"not in index  {wiki[stem].relative_to(ROOT)}")
    for stem in indexed:
        if stem not in known:
            problems.append(f"index points nowhere  [[{stem}]]")
    cited = set()
    for p in (WIKI / "sources").glob("*.md"):
        cited |= {m.group(1).strip() for m in LINK_RE.finditer(p.read_text(encoding="utf-8"))}
    for stem, p in raw.items():
        if p.parent.name == "assets":
            continue
        if stem not in cited:
            problems.append(f"unprocessed raw source  {p.relative_to(ROOT)}")
    if problems:
        print("\n".join(sorted(problems)))
        print(f"\n{len(problems)} problem(s)")
        return 1
    print(f"ok — {len(wiki)} wiki pages, {len([p for p in raw.values() if p.parent.name != 'assets'])} raw sources, no problems")
    return 0

if __name__ == "__main__":
    sys.exit(main())
