# BRIEFING — 2026-06-06T14:17:38-07:00

## Mission
Extract narrative information and major figures for Song of Songs from the Tremper Longman III commentary and inject them into `wiki/texts/song-of-songs.md`, creating/updating figure pages and the index.

## 🔒 My Identity
- Archetype: sub_orch
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_item22
- Original parent: f1262e8c-b892-4f35-a073-31c5678e553b
- Original parent conversation ID: f1262e8c-b892-4f35-a073-31c5678e553b

## 🔒 My Workflow
- **Pattern**: Project / Iteration Loop
- **Scope document**: /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_item22/SCOPE.md
1. **Decompose**: The scope is small enough for a single Explorer -> Worker -> Reviewer -> Auditor loop.
2. **Dispatch & Execute**:
   - **Direct (iteration loop)**: Explorer -> Worker -> Reviewer -> Auditor -> gate
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent
4. **Succession**: at 16 spawns, write handoff.md, spawn successor
- **Work items**:
  1. Extract and inject narrative and figures for Song of Songs [in-progress]
- **Current phase**: 2
- **Current focus**: Executing iteration loop for Song of Songs

## 🔒 Key Constraints
- NEVER write, modify, or create source code files directly.
- NEVER run build/test commands yourself.
- Use file-editing tools ONLY for metadata/state files (.md) in your .agents/ folder.
- Follow CLAUDE.md schema for figure pages.
- Auditor veto is an absolute FAILURE.
- MUST send FULL auditor evidence to the next Explorer iteration if the audit fails.
- Never reuse a subagent after it has delivered its handoff.

## Current Parent
- Conversation ID: f1262e8c-b892-4f35-a073-31c5678e553b
- Updated: not yet

## Key Decisions Made
- Use Project pattern, direct iteration loop.
- Determined the correct source file: `raw/commentaries/Song of Songs (New International Commentar - Longman, Tremper, III.txt`

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
- /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_item22/SCOPE.md - Scope and Milestones
- /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_item22/progress.md - Iteration status
