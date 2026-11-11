#!/usr/bin/env bash
# Smoke tests for .github/scripts/jira_helpers.sh (no live Jira).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck source=../scripts/jira_helpers.sh
source "$ROOT/scripts/jira_helpers.sh"

fail=0
assert_eq() {
  local got="$1" want="$2" msg="$3"
  if [ "$got" != "$want" ]; then
    echo "FAIL: $msg (got='$got' want='$want')" >&2
    fail=1
  else
    echo "OK: $msg"
  fi
}

assert_eq "$(jira_http_retryable 000 && echo yes || echo no)" yes "000 retryable"
assert_eq "$(jira_http_retryable 429 && echo yes || echo no)" yes "429 retryable"
assert_eq "$(jira_http_retryable 503 && echo yes || echo no)" yes "503 retryable"
assert_eq "$(jira_http_retryable 201 && echo yes || echo no)" no "201 not retryable"
assert_eq "$(jira_http_retryable 400 && echo yes || echo no)" no "400 not retryable"

command -v jira_post_comment_best_effort >/dev/null
echo "OK: jira_post_comment_best_effort defined"

TMP=$(mktemp -d)
cat >"$TMP/curl" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
count_file="${JIRA_TEST_CURL_COUNT}"
n=0
if [ -f "$count_file" ]; then
  n=$(cat "$count_file")
fi
n=$((n + 1))
printf '%s' "$n" >"$count_file"
outfile=/dev/null
while [ $# -gt 0 ]; do
  case "$1" in
    -o) outfile=$2; shift 2 ;;
    *) shift ;;
  esac
done
if [ "$n" -lt 3 ]; then
  : >"$outfile"
  printf '000'
  exit 0
fi
printf '{"ok":true}' >"$outfile"
printf '201'
exit 0
EOF
chmod +x "$TMP/curl"
export PATH="$TMP:$PATH"
export JIRA_TEST_CURL_COUNT="$TMP/count"
export LOC_JIRA_USER_EMAIL=x LOC_JIRA_API_TOKEN=y LOC_JIRA_BASE_URL=https://example.invalid
export LOC_JIRA_HTTP_RETRIES=3 LOC_JIRA_HTTP_RETRY_SLEEP=0
: >"$JIRA_TEST_CURL_COUNT"

code=$(jira_curl "$TMP/out.json" POST "https://example.invalid/rest/api/2/issue/X/comment" \
  -H "Content-Type: application/json" -d '{}')
assert_eq "$code" "201" "jira_curl retries then succeeds"
assert_eq "$(cat "$JIRA_TEST_CURL_COUNT")" "3" "jira_curl used 3 attempts"
assert_eq "$(cat "$TMP/out.json")" '{"ok":true}' "jira_curl wrote body"

rm -rf "$TMP"
exit "$fail"
