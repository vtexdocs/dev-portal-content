# Shared Jira helpers for localization-ticket workflow.
# Source after setting LOC_JIRA_BASE_URL, LOC_JIRA_USER_EMAIL, LOC_JIRA_API_TOKEN,
# LOC_JIRA_PROJECT_KEY, PR_NUMBER, GITHUB_REPOSITORY, PR_REF, PR_LABEL, and GH_TOKEN.

jira_user_search() {
  local query="$1"
  local max_results="${2:-10}"

  curl -s -G \
    -u "${LOC_JIRA_USER_EMAIL}:${LOC_JIRA_API_TOKEN}" \
    --data-urlencode "query=${query}" \
    --data-urlencode "maxResults=${max_results}" \
    "${LOC_JIRA_BASE_URL}/rest/api/2/user/search"
}

# Resolve PR author (GitHub login) to a Jira reporter field object.
# Prints JSON like {"accountId":"..."} or {"name":"..."}; empty if not found.
# Optional: GH_TOKEN (GitHub profile email), LOC_JIRA_REPORTER_EMAIL_DOMAIN (e.g. @vtex.com).
resolve_jira_reporter_from_github() {
  local github_login="$1"
  local candidates match_json email_query derived_email

  if [ -z "$github_login" ] || [ "$github_login" = "null" ]; then
    return 1
  fi

  pick_existing_user() {
    jq -c --arg login "$github_login" '
      [.[] | select(.active != false)] |
      map(select(
        ((.emailAddress // "" | ascii_downcase | split("@")[0]) == ($login | ascii_downcase)) or
        ((.displayName // "" | ascii_downcase | contains($login | ascii_downcase)))
      )) | .[0] // empty
    '
  }

  pick_user_by_email() {
    local email="$1"
    jq -c --arg email "$email" '
      [.[] | select(.active != false and ((.emailAddress // "") | ascii_downcase) == ($email | ascii_downcase))] |
      .[0] // empty
    '
  }

  reporter_field_from_user() {
    jq -c 'if .accountId then {accountId: .accountId} elif .name then {name: .name} else empty end'
  }

  candidates=$(jira_user_search "$github_login" 50)
  match_json=$(echo "$candidates" | pick_existing_user)
  if [ -n "$match_json" ] && [ "$match_json" != "null" ]; then
    echo "$match_json" | reporter_field_from_user
    echo "Resolved Jira reporter for GitHub user ${github_login}" >&2
    return 0
  fi

  if [ -n "${GH_TOKEN:-}" ]; then
    email_query=$(gh api "users/${github_login}" --jq '.email // empty' 2>/dev/null || true)
    if [ -n "$email_query" ]; then
      match_json=$(jira_user_search "$email_query" 5 | pick_user_by_email "$email_query")
      if [ -n "$match_json" ] && [ "$match_json" != "null" ]; then
        echo "$match_json" | reporter_field_from_user
        echo "Resolved Jira reporter for GitHub user ${github_login} via GitHub email" >&2
        return 0
      fi
    fi
  fi

  if [ -n "${LOC_JIRA_REPORTER_EMAIL_DOMAIN:-}" ]; then
    derived_email="${github_login}${LOC_JIRA_REPORTER_EMAIL_DOMAIN}"
    match_json=$(jira_user_search "$derived_email" 5 | pick_user_by_email "$derived_email")
    if [ -n "$match_json" ] && [ "$match_json" != "null" ]; then
      echo "$match_json" | reporter_field_from_user
      echo "Resolved Jira reporter for GitHub user ${github_login} via ${derived_email}" >&2
      return 0
    fi
  fi

  echo "Could not resolve Jira reporter for GitHub user ${github_login}; using API token user" >&2
  return 1
}

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
