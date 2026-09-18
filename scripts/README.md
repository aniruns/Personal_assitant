# Scripts

- `lint.py` — mechanical wiki checks (broken wikilinks, orphans, index drift, frontmatter,
  unprocessed raw sources). Run `python3 scripts/lint.py`. The agent runs this as step 1 of
  every `lint` operation (see `CLAUDE.md` §3.3); the semantic pass is done by the agent.
- Recent operations: `grep "^## \[" wiki/log.md | tail -5`
