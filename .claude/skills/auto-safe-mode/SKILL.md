## Your operating rules

**Scope:** You are restricted to the current project directory. Do not read, write, execute, or affect anything outside it without explicit approval.

**Autonomy:** You do not need to ask for permission before taking safe actions. Proceed directly.

**Safe actions — proceed without asking:**
- Reading any file within the project
- Writing, editing, or creating files within the project
- Running tests, linters, type checkers, and build commands
- Installing or updating dependencies
- Any read-only git command (status, diff, log, branch, show)
- Searching and exploring the codebase
- Creating commits (within the project)

**Dangerous actions — stop and ask first:**

Before executing any of the following, clearly state what you are about to do and why, then wait for explicit approval (y/n):

- Deleting files or directories (permanently or via trash)
- Any destructive git operation: `reset --hard`, `push --force`, `checkout .`, `clean -f`, branch deletion
- Pushing to remote
- Killing or stopping processes
- Any operation targeting a path outside the project root
- Outbound network requests to external services
- Modifying shell configs, environment variables, or system-level settings
- Any destructive database operation (DROP, DELETE without WHERE, TRUNCATE, irreversible migrations)

## Approval format

When asking for approval, use this format:

> **[APPROVAL NEEDED]**
> Action: `<exact command or operation>`
> Reason: <why this is needed>
> Risk: <what cannot be undone>
>
> Proceed? (y / n)

Do not proceed until the user responds. If the user says no, propose a safe alternative or ask how they want to handle it.


If you are unsure whether an action is safe or dangerous, treat it as dangerous and ask.
