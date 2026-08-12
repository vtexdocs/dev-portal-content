#!/usr/bin/env bash
# Structural checks for localization-ticket.yml (no Actions run).
set -euo pipefail
WF="$(cd "$(dirname "$0")/.." && pwd)/workflows/localization-ticket.yml"
fail=0
check() {
  local pat="$1" msg="$2"
  if ! grep -qE "$pat" "$WF"; then
    echo "FAIL: $msg ($pat)" >&2
    fail=1
  else
    echo "OK: $msg"
  fi
}
check 'LOC_JIRA_PROJECT_KEY: LOC' 'hardcoded LOC project key'
check 'Comment on parent with prepare result' 'prepare result comment step'
check 'Comment on parent with finalize result' 'finalize result comment step'
check 'jira_post_comment_best_effort' 'best-effort Jira comments'
check 'jira_curl subtask-response.json' 'retried subtask create'
# prepare before Crowdin upload
python3 - <<PY
from pathlib import Path
text = Path("$WF").read_text()
assert text.index("Comment on parent with prepare result") < text.index("Upload touched files to Crowdin"), "prepare must precede Crowdin"
assert text.index("Comment on PR with Jira link") < text.index("Upload touched files to Crowdin"), "PR comment must precede Crowdin"
print("OK: step ordering")
PY
exit "$fail"
