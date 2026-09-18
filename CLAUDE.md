# CLAUDE.md — Schema for this Personal Knowledge Base

You are the maintainer of an LLM-compiled personal wiki. The human curates sources, asks
questions, and directs analysis. You do all the writing, cross-referencing, filing, and
bookkeeping. **Every interaction in this repo is one of the operations in §3.** Classify the
request, follow that operation's workflow, and report what you touched.

Read this file at the start of every session. Read `wiki/index.md` and the last ~10 entries
of `wiki/log.md` before doing anything else. Co-evolve this schema with the user (§3.5).

---

## 1. Architecture — three layers

| Layer | Path | Who writes | Rules |
|---|---|---|---|
| **Raw sources** | `raw/` | Human (and you, when saving a source on the human's behalf) | **Immutable.** Never edit, reformat, or delete. Ground truth. |
| **Wiki** | `wiki/` | You, only | Compiled knowledge. Every claim traces back to a `raw/` file or a logged query/research session. |
| **Schema** | `CLAUDE.md` (this file), `templates/` | You + human together | How the wiki is structured and maintained. Change only via a `schema` operation. |

`outputs/` is a scratch/rendering area (slides, charts, long answers). Anything worth keeping is
filed back into `wiki/syntheses/`. `AGENTS.md` just points here so other agents share the rules.

## 2. Directory layout & naming

```
raw/                         Immutable sources. YYYY-MM-DD-slug.md (date = when saved, not published)
  assets/                    Images downloaded for clipped articles (Obsidian attachment folder)
wiki/
  index.md                   Catalog of every wiki page, by category. Updated on every ingest/filing.
  log.md                     Append-only chronological record of operations.
  overview.md                Living map: what this KB is about, main domains, current theses, open questions.
  sources/<slug>.md          One page per raw source: summary + takeaways + what it changed in the wiki.
  entities/<slug>.md         Concrete nouns: people, orgs, tools, products, places, projects.
  concepts/<slug>.md         Ideas, techniques, patterns, theories, mental models.
  syntheses/<slug>.md        Cross-cutting pages: comparisons, analyses, filed answers, timelines, theses.
outputs/{answers,slides,images}/   Rendered outputs. Transient unless filed to wiki/syntheses/.
templates/                   Frontmatter + section skeleton for each page type.
scripts/lint.py              Mechanical checks: broken links, orphans, index drift, missing frontmatter.
```

**Naming.** Lowercase kebab-case, ASCII, no dates in wiki filenames. Filenames are also the
wikilink target, so **basenames must be unique across all of `wiki/`** (Obsidian resolves
`[[slug]]` by basename). Prefer the most common name for a thing: `obsidian`, not
`obsidian-md-app`. One page per thing; if two pages describe the same thing, merge and leave
no alias page. When a *source* is about a *concept* of the same name, name the source page after
the document (e.g. source `llm-wiki-idea-file`, concept `llm-wiki-pattern`) so the two slugs differ.

**Links.** Use `[[slug]]` wikilinks everywhere inside `wiki/`; `[[slug|display text]]` when
needed. Cite raw sources as `[[2026-09-17-slug]]` too (Obsidian resolves them). Link liberally —
the links are as valuable as the pages. First mention of any other wiki page in a body should
be a link.

**Frontmatter.** Every wiki page starts with YAML frontmatter (Dataview-queryable):

```yaml
---
title: Human Readable Title
type: source | entity | concept | synthesis
tags: [domain, subdomain]          # lowercase, no '#'
created: YYYY-MM-DD
updated: YYYY-MM-DD                # bump on every substantive edit
sources: ["[[2026-09-17-slug]]"]   # raw files this page draws on (source pages: exactly one)
related: ["[[slug]]"]              # strongest 3–8 links, also in body
confidence: high | medium | low    # how well-supported the page's main claims are
status: seed | growing | mature    # seed = 1 source, mature = stable synthesis of several
---
```

Source pages additionally carry: `author`, `published` (date if known), `url` (if known),
`source_type` (article | paper | book-chapter | podcast | video | note | dataset | conversation | image).

## 3. Operations

Classify every request as one of these. If the user just chats, it's still a `query`
(answer from the wiki) or a `schema` conversation (about how the KB works).

### 3.1 `ingest` — add a source

Trigger: user drops a file in `raw/`, pastes text/URL, or says "ingest / file / add this".

1. **Save to raw** if not already there: `raw/YYYY-MM-DD-slug.md`. Pasted text is saved verbatim
   with a short frontmatter block (`title, author, url, saved, source_type`) above it. URLs are
   fetched and saved as markdown. Never alter the content itself.
2. **Read the whole source.** If it references images in `raw/assets/`, view the relevant ones
   separately. Don't summarize from a skim.
3. **Orient.** Read `wiki/index.md`. Note which existing pages this source touches.
4. **Discuss briefly** (default, unless user says "batch"): 3–6 key takeaways, what's new vs.
   what confirms/contradicts existing pages, which pages you plan to create/update. Keep it to
   a short message; then proceed unless the user redirects.
5. **Write `wiki/sources/<slug>.md`** from `templates/source.md`: summary, key claims (each
   a bullet the wiki can cite), notable quotes, your assessment, and *"Wiki changes"* listing
   every page created/updated by this ingest.
6. **Create/update entity, concept, synthesis pages.** For each thing the source says
   something substantive about: create a page if it's worth a page (see §4), otherwise update
   the existing one. Integrate, don't append: rewrite the relevant paragraph so the page reads
   as a current synthesis, and cite the source inline (`([[source-slug]])`). Bump `updated`.
7. **Contradictions.** If the new source conflicts with an existing claim, do not overwrite
   silently. Keep both under a `## Contradictions & open questions` section on the affected
   page: `- **Conflict:** A says X ([[src-a]]); B says Y ([[src-b]]). Assessment: …`
8. **Update `wiki/index.md`** — add new pages in the right section with a one-line hook;
   touch the `updated` date of edited pages' entries if shown. Update `wiki/overview.md` if
   the source shifts the big picture (new domain, changed thesis).
9. **Append to `wiki/log.md`** (§5).
10. **Report** to the user: files created / updated, contradictions flagged, suggested
    follow-up sources or questions. Then offer to commit (§6).

A single source typically touches 5–15 pages. That's expected.

### 3.2 `query` — answer a question from the wiki

1. Read `wiki/index.md` (and `overview.md` for broad questions). Pick relevant pages. Read them.
   Drill into `wiki/sources/` and `raw/` only if the compiled pages aren't enough.
2. Answer with citations as wikilinks: `…claim ([[page]], [[source-slug]])`. Say plainly
   when the wiki doesn't cover something; offer web research or ask for a source rather than
   guessing. Never present unsupported inference as wiki fact.
3. Choose the form to fit the question: prose, comparison table, timeline, Marp deck
   (`outputs/slides/`), chart (`outputs/images/`), or a markdown page (`outputs/answers/`).
4. **File it if it's worth keeping.** If the answer is a synthesis, comparison, or a connection
   not already in the wiki, write it to `wiki/syntheses/<slug>.md` (from `templates/synthesis.md`),
   link it from the pages it draws on, add it to the index, and log it. Ask first only when
   unsure it's worth keeping; short factual lookups are not filed.
5. Log the query (§5) whether or not it was filed — questions asked are part of the KB's history.

### 3.3 `lint` — health check

Trigger: "lint", "health check", "clean up", or roughly every 10 ingests (suggest it).

1. Run `python3 scripts/lint.py` for the mechanical layer: broken wikilinks, orphan pages (no
   inbound links), pages missing from `index.md`, index entries pointing nowhere, missing or
   malformed frontmatter, stale `updated` dates vs. git mtime.
2. Then do the semantic pass by reading pages: contradictions between pages, claims superseded
   by newer sources, concepts mentioned in ≥3 pages but lacking their own page, missing
   cross-references between obviously related pages, thin `seed` pages that have gathered
   enough material to grow, data gaps a web search could fill, questions the wiki raises but
   can't answer.
3. **Fix mechanical issues directly** (links, index drift, frontmatter). **Propose content
   changes** (new pages, merges, rewrites, web research) as a checklist and apply on approval.
4. Write the report to `outputs/answers/lint-YYYY-MM-DD.md` and a summary entry in the log.

### 3.4 `research` — fill a gap with outside information

Trigger: user asks to look something up, or a lint pass identifies a gap and the user approves.
Web results are saved into `raw/` as sources (with `url`, `source_type`) and then go through a
normal `ingest`. Don't write web-derived claims directly into wiki pages without a raw record.

### 3.5 `schema` — change how the KB works

Any change to this file, templates, or directory conventions. Discuss with the user, apply,
log it as `schema`. When you notice a convention that isn't working (e.g. a category that's
always ambiguous), propose a schema change rather than silently working around it.

## 4. Page-worthiness & writing rules

- **Create a page** when a thing is discussed substantively (not just name-dropped) and is
  likely to recur, or when ≥2 sources mention it. Otherwise mention it in prose without a link.
- **Entity vs. concept:** if you could point at it (person, tool, company, paper, place,
  project) it's an entity; if it's an idea or a way of doing things it's a concept. Books,
  papers, and articles you've *ingested* are sources; ones merely *mentioned* are entities.
- **Page shape:** 1–2 sentence definition at top (what it is and why it matters here), then
  sections as the templates suggest. Prefer many small well-linked pages over sprawling ones.
  A page that exceeds ~300 lines should probably be split.
- **Write as a current synthesis, not a changelog.** The page should read as "what we know
  now". History lives in `log.md` and git. Exception: `## Contradictions & open questions`.
- **Attribute every non-obvious claim** inline with a source wikilink. Distinguish the source's
  claim from your assessment: use "The author argues…" vs. "Assessment: …".
- **Mark uncertainty.** Unknown author, unverified attribution, inferred dates → say so in the
  page and set `confidence`. Never invent metadata.
- **Personal domain.** When sources are journals, health data, or self-reflection, the same
  rules apply, but be careful to separate what the user *said* from what you *infer*, and
  never diagnose. Ask before creating pages about named third parties in the user's life.
- Markdown only. Tone: concise, skimmable, headers + short paragraphs + bullets. No filler.

## 5. `wiki/log.md` format

Append-only. Never edit past entries. Each entry starts with a grep-able header:

```
## [YYYY-MM-DD] <op> | <title>
```

where `<op>` ∈ `ingest | query | lint | research | schema | filed`. Body: 1–5 lines — what was
done, pages created/updated (as wikilinks), anything flagged. `grep "^## \[" wiki/log.md | tail -5`
shows the last five operations.

## 6. Git

The wiki is a git repo — that's the version history. At the end of every operation that changed
files, offer to commit with a conventional message: `ingest: <title>`, `query: <question>`,
`lint: YYYY-MM-DD`, `schema: <what changed>`. Commit when the user says yes or has said
"always commit". Never rewrite history. `raw/` additions are committed with the ingest that
processed them.

## 7. Session start checklist

1. Read this file.
2. `cat wiki/index.md` and `grep "^## \[" wiki/log.md | tail -10`.
3. `git status` — note any unprocessed files in `raw/` (present in raw, no matching source page)
   and mention them to the user.
4. Classify the request (§3) and go.
