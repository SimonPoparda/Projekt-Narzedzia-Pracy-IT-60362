---
name: project-init
description: Safely initializes isolated development environments (venv, npm, etc.) and project scaffolding.
---

# Project Isolation & Initialization Rules

## 1. The Containment Rule (Strict)
- **NO GLOBAL INSTALLS:** Never use `sudo`, `pip install` (without venv), or `npm install -g`.
- **Venv Enforcement:** If this is a Python project, the first step MUST be: 
  `python -m venv .venv && source .venv/bin/activate` (or Windows equivalent).
- **Scope Check:** Before running any install command, verify the current working directory is the project root.

## 2. Scaffolding Checklist
When starting a new project or module, always create:
- `.gitignore`: Include `.venv`, `__pycache__`, `.env`, and OS-specific junk.
- `.env.example`: A template for required secrets (never the secrets themselves).
- `README.md`: Basic setup instructions.
- `tests/`: A directory for unit tests.

## 3. Tool Selection
- Prefer `uv` or `poetry` for Python if available (faster/safer).
- Use `npm` or `pnpm` based on existing lockfiles.
- Always check for an existing `requirements.txt` or `package.json` before proposing new libraries.

## 4. Execution Flow
1. **Detect** environment (Python, JS, Go, etc.).
2. **Isolate** (Create venv/local config).
3. **Verify** (Run a version check to ensure the local tool is being used).