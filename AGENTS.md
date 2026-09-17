# Agent Instructions

You are maintaining a personal knowledge base for the user. Follow these rules whenever you're asked to ingest, compile, query, or clean up this repo.

## Ingest

- New source material lands in `raw/`. Leave it close to its original form (clipped markdown, PDFs, images, exported notes).
- Give each item a sensible filename and, if there's an obvious topic, a subfolder under `raw/<topic>/`.
- Don't delete or rewrite files in `raw/` — it's the ground truth. All editorializing happens in `wiki/`.

## Compile the wiki

- For each new item in `raw/`, write or update a short summary and file it under the right concept in `wiki/concepts/`.
- One concept = one article. If a new source doesn't fit an existing concept, create a new article using `templates/article-template.md`.
- Every article should link to related articles (`[[wikilink]]` style works well in Obsidian) and cite which `raw/` source(s) it was drawn from.
- Update `wiki/index.md` whenever a new concept article is added, so the index always reflects the current set of articles.
- Prefer many small, well-linked articles over a few sprawling ones.

## Answer questions

- When asked a question, search `wiki/` first (the index + article summaries should usually be enough at this repo's scale — don't reach for embeddings/RAG unless the wiki gets huge).
- If the wiki doesn't have the answer, research it (web search, re-reading `raw/`), then write the answer up as a new file in `outputs/answers/`.
- If the user wants slides, use Marp-formatted markdown in `outputs/slides/`. If they want a chart, save the image to `outputs/images/`.
- If an answer is broadly useful, offer to file it back into `wiki/` (and link it from `wiki/index.md`) so it isn't lost.

## Health checks / linting

- When asked to "clean up" or "health check" the wiki: look for orphaned articles (no backlinks), broken links, stale or contradictory information, and gaps that could use a web search to fill in.
- Suggest new articles or connections you notice, but don't create them unprompted — propose first.
- Keep a running note of what you changed in `scripts/CHANGELOG.md` (create it if it doesn't exist) so the user can see what the last health check touched.

## Style

- Markdown only, no proprietary formats.
- Keep articles concise and skimmable — headers, short paragraphs, bullet lists where useful.
- Always attribute: every wiki article should be traceable back to a `raw/` source or a research session.
