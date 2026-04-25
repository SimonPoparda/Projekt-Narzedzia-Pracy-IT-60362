# karpathy-guidelines

Behavioral guidelines to reduce common LLM coding mistakes, derived from Andrej Karpathy's observations on coding pitfalls.

- **Source**: https://github.com/forrestchang/andrej-karpathy-skills
- **Author**: forrestchang
- **License**: MIT

## What it does

Enforces four principles that address the most common ways LLMs go wrong when coding:

| Principle | Problem it solves |
|-----------|------------------|
| **Think Before Coding** | Models making unexamined assumptions without clarifying |
| **Simplicity First** | Tendency toward overengineering and bloated abstractions |
| **Surgical Changes** | Inadvertently modifying code outside the intended scope |
| **Goal-Driven Execution** | Vague success criteria leading to endless back-and-forth |

## Install

```bash
claude plugin marketplace add forrestchang/andrej-karpathy-skills && claude plugin install andrej-karpathy-skills@karpathy-skills
```

## Activate

The plugin loads its guidelines as a skill. Trigger with:
- `/karpathy-guidelines`
- Natural language: "enable karpathy" / "use karpathy guidelines"
