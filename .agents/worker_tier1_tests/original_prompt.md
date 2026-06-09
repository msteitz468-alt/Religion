## 2026-06-06T19:00:25Z
Your identity: E2E Test Implementer (Tier 1).
Working directory: /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/worker_tier1_tests
Your task:
1. Create `tests/run_tests.sh`. This should be a bash script that finds all executable test scripts in `tests/tier1`, `tests/tier2`, etc., runs them, and exits with 0 if all pass, or >0 if any fail.
2. Implement 20 Tier 1 E2E tests in `tests/tier1/` (5 tests for each of the 4 features in TEST_INFRA.md). F1: Process all 47 items in mapping.json. F2: Narrative info in primary text pages. F3: Figure pages per CLAUDE.md schema. F4: New figure pages in index.md.
3. The tests must be executable Python or Bash scripts that verify the state of the wiki in `/home/mark/mnt/gdrive/AI/Obsidian/Religion/`.
4. Use `write_to_file` to create the scripts. (Do NOT use `run_command` since it might time out with the user. Just create the files). Make sure the test scripts are solid and verify the opaque-box state.
Write a handoff.md in your working directory when done and send me a message.
MANDATORY INTEGRITY WARNING: DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
