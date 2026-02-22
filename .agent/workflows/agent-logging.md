---
description: Initialize a named agent session, bootstrap context from past logs, and append interaction logs
---

# Agent Logging Workflow

## Invocation

```
/agent-logging [agent-name] rest of the prompt (if any)
```

- `[agent-name]` — identifier for this agent session. **Normalize** it: lowercase, replace spaces and special characters with dashes (`-`). Examples: `Antigravity` → `antigravity`, `My Agent!` → `my-agent`.
- `rest of the prompt` — optional additional instructions for the current session.

All logs are stored under `/agent-log/[agent-name]/`.

---

## Step 1 — Normalize the agent name

Take the first argument after `/agent-logging`, convert to lowercase, and replace any spaces or special characters with `-`. This normalized name is used for all folder and file paths below.

## Step 2 — Bootstrap context from past logs

Read all existing log files in `/agent-log/[agent-name]/` (sorted oldest to newest). Summarize key decisions, completed tasks, and open items from previous sessions. If no prior logs exist, note that this is a fresh session.

## Step 3 — Handle mid-conversation invocation (if applicable)

If this workflow is triggered **after** the conversation has already started (i.e., there are prior messages in this session before this `/agent-logging` command):

- Replay all prior exchanges from the very first message up to this point.
- Retroactively write a log entry for each prior exchange into `/agent-log/[agent-name]/YYYY-MM-DD.md`, using the timestamp of each exchange.

## Step 4 — Create the log folder

Create `/agent-log/[agent-name]/` if it does not already exist.

## Step 5 — Confirm ready

Briefly confirm to the user:
- The normalized agent name
- How many past sessions were found and key context loaded
- That you are ready to proceed with the rest of the prompt (if any)

---

## Step 6 — Log each interaction (ongoing, run at END of every response)

Append a new entry to `/agent-log/[agent-name]/YYYY-MM-DD.md` after **every** response. Do **NOT** overwrite previous entries.

Use this format exactly:

```markdown
## Entry: YYYY-MM-DD HH:MM:SS+TZ
- **User Prompt:** "The user's FULL original prompt exactly as provided."
- **Task/Interaction:** A summary of what the user asked and what you are doing.
- **Action Taken:** A summary of the actions you performed during this run.
```