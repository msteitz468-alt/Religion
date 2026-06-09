# BRIEFING — 2026-06-06T19:00:57-07:00

## Mission
Process mapping.json items 16-17: Extract narrative and figure info from raw_files for Joel, Obadiah, Jonah, Micah, Hosea, Amos. Update text pages, create figure pages, and update index.md.

## 🔒 My Identity
- Archetype: sub_orch
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_batch2_4
- Original parent: 4ffff892-443b-4c4c-8eb3-7e98b3dd2215
- Original parent conversation ID: 4ffff892-443b-4c4c-8eb3-7e98b3dd2215

## 🔒 My Workflow
- **Pattern**: Iteration Loop (Explorer → Worker → Reviewer)
- **Scope document**: /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_batch2_4/SCOPE.md
1. **Decompose**: We will run a single Iteration Loop per item or combined. Since the tasks are similar (extract narrative info, update texts and figures), we'll dispatch an Explorer to analyze both items, then a Worker to execute the changes, then Reviewer.
2. **Dispatch & Execute**:
   - **Direct (iteration loop)**: Explorer → Worker → Reviewer → gate
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent (sub-orchestrators only, last resort)
4. **Succession**: at 16 spawns, write handoff.md, spawn successor
- **Work items**:
  1. Process Item 16 (Micah, Jonah, Obadiah) [pending]
  2. Process Item 17 (Hosea, Amos, Joel) [pending]
- **Current phase**: 2
- **Current focus**: Process Item 16 & 17

## 🔒 Key Constraints
- Never reuse a subagent after it has delivered its handoff — always spawn fresh
- Do not run build/test commands myself.

## Current Parent
- Conversation ID: 4ffff892-443b-4c4c-8eb3-7e98b3dd2215
- Updated: not yet

## Key Decisions Made
- Discovered mapping.json has wrong raw_file for items 16 & 17 (all point to Craigie's Deuteronomy). Identified the correct files in raw/commentaries/:
  - The Books of Joel, Obadiah, and Jonah - James D. Nogalski;.txt
  - The Book of Micah - James D. Nogalski;.txt
  - Hosea (NICOT) - J. Andrew Dearman.txt
  - The Book of Amos - M Daniel Carroll R.txt

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|

## Succession Status
- Succession required: no
- Spawn count: 0 / 16
- Pending subagents: none
- Predecessor: none
- Successor: not yet spawned

## Active Timers
- Heartbeat cron: not started
- Safety timer: none

## Artifact Index
- /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_batch2_4/SCOPE.md — scope description
- /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_batch2_4/progress.md — task progress
