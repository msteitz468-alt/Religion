#!/bin/bash
sed -i '/| Agent | Type | Work Item | Status | Conv ID |/,/^$/!b;//!d;/| Agent |/!d' /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_proverbs/BRIEFING.md

cat << 'INNER_EOF' >> /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_proverbs/BRIEFING.md
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| explorer_1 | teamwork_preview_explorer | Explore M2 | in-progress | bbd0caa0-401d-43c4-b0ae-bce62520a5d6 |
| explorer_2 | teamwork_preview_explorer | Explore M2 | in-progress | a20463bb-23e6-4769-8838-55db844bcc7f |
| explorer_3 | teamwork_preview_explorer | Explore M2 | in-progress | 9c345ba1-0cae-4891-aaa0-68f7d9bc0fe1 |

INNER_EOF
chmod +x /home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_proverbs/update_roster.sh
/home/mark/mnt/gdrive/AI/Obsidian/Religion/.agents/sub_orch_proverbs/update_roster.sh
