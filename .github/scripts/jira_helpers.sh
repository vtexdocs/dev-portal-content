# Shared Jira helpers for localization-ticket workflow.
# Source after setting LOC_JIRA_BASE_URL, LOC_JIRA_USER_EMAIL, LOC_JIRA_API_TOKEN,
# LOC_JIRA_PROJECT_KEY, PR_NUMBER, GITHUB_REPOSITORY, PR_REF, PR_LABEL, and GH_TOKEN.

jira_post_search() {
  local jql="$1"
  local fields_csv="$2"
  local max_results="${3:-50}"
  local payload response http_code body api_url

  payload=$(jq -n \
    --arg jql "$jql" \
    --arg fields "$fields_csv" \
    --argjson max "$max_results" \
    '{
      jql: $jql,
      maxResults: $max,
      fields: ($fields | split(",") | map(gsub("^\\s+|\\s+$"; "")))
    }')

  for api_url in \
    "${LOC_JIRA_BASE_URL}/rest/api/3/search/jql" \
    "${LOC_JIRA_BASE_URL}/rest/api/2/search"; do
    response=$(curl -s -w "\n%{http_code}" \
      -X POST \
      -H "Content-Type: application/json" \
      -u "${LOC_JIRA_USER_EMAIL}:${LOC_JIRA_API_TOKEN}" \
      -d "$payload" \
      "$api_url")
    http_code=$(echo "$response" | tail -1)
    body=$(echo "$response" | sed '$d')

    if [ "$http_code" = "200" ] || [ "$http_code" = "201" ]; then
      if [ "$(echo "$body" | jq -r '.errorMessages // [] | length')" -gt 0 ]; then
        echo "Jira search error: $(echo "$body" | jq -r '.errorMessages[]')" >&2
        return 1
      fi
      echo "$body"
      return 0
    fi

    if [ "$http_code" != "404" ] && [ "$http_code" != "405" ]; then
      echo "Jira search failed at ${api_url} (HTTP ${http_code}): ${body}" >&2
      return 1
    fi
  done

  echo "Jira search failed: no compatible search endpoint" >&2
  return 1
}

jira_search_first_key() {
  local jql="$1"
  local result
  result=$(jira_post_search "$jql" "key,created" 1) || return 1
  echo "$result" | jq -r '.issues[0].key // empty'
}

resolve_existing_parent_key() {
  local key source

  key=$(gh api \
    "repos/${GITHUB_REPOSITORY}/issues/${PR_NUMBER}/comments" \
    --paginate \
    | jq -r --arg project "$LOC_JIRA_PROJECT_KEY" \
      '[.[] | select(.body | test(":globe_with_meridians: Localization task|Localization ticket \\[" + $project + "-[0-9]+\\]"))] | sort_by(.created_at) | .[0].body // empty' \
    | grep -oE "${LOC_JIRA_PROJECT_KEY}-[0-9]+" | head -1 || true)
  if [ -n "$key" ]; then
    source="PR comment"
  else
    key=$(jira_search_first_key \
      "project = ${LOC_JIRA_PROJECT_KEY} AND labels = \"${PR_LABEL}\" ORDER BY created ASC" || true)
    if [ -n "$key" ]; then
      source="dp-github-pr label"
    else
      key=$(jira_search_first_key \
        "project = ${LOC_JIRA_PROJECT_KEY} AND text ~ \"dp-github-pr-ref: ${PR_REF}\" ORDER BY created ASC" || true)
      if [ -n "$key" ]; then
        source="dp-github-pr-ref marker"
      else
        key=$(jira_search_first_key \
          "project = ${LOC_JIRA_PROJECT_KEY} AND summary ~ \"\\\\[DP\\\\]\" AND text ~ \"#${PR_NUMBER}\" ORDER BY created ASC" || true)
        if [ -n "$key" ]; then
          source="[DP] summary and PR link text"
        fi
      fi
    fi
  fi

  if [ -n "$key" ]; then
    echo "Found existing ticket via ${source}: ${key}" >&2
    echo "$key"
  fi
}
