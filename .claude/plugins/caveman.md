# caveman

> "why use many token when few token do trick."

Token-efficient communication mode for Claude Code. Cuts ~65-75% of output tokens while keeping full technical accuracy.

- **Source**: https://github.com/JuliusBrussee/caveman
- **Author**: Julius Brussee
- **License**: MIT

## What it does

Makes Claude respond in terse, fragment-based language — dropping articles, filler, and verbose explanations. Technical accuracy is preserved.

**Normal:** "The reason your component re-renders is likely because you're creating a new object reference on each render."
**Caveman:** "New object ref each render. Inline object prop = new ref = re-render. Wrap in `useMemo`."

### Intensity levels

| Level | Style |
|-------|-------|
| Lite | Removes filler, keeps grammar |
| Full | Default — drops articles and fragments |
| Ultra | Maximum compression, telegraphic |
| 文言文 | Classical Chinese, extreme compression |

### Extra skills included

- `caveman-commit` — terse commit messages (≤50 chars)
- `caveman-review` — one-line PR comments
- `caveman-compress` — rewrites memory files, ~46% input token savings

## Install

```bash
claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman
```

## Activate

After install, trigger with:
- `/caveman` slash command
- Natural language: "talk like caveman"
