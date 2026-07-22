# Shared Jira helpers for localization-ticket workflow.
# Source after setting LOC_JIRA_BASE_URL, LOC_JIRA_USER_EMAIL, LOC_JIRA_API_TOKEN,
# LOC_JIRA_PROJECT_KEY, PR_NUMBER, GITHUB_REPOSITORY, PR_REF, PR_LABEL, and GH_TOKEN.

CROWDIN_UPLOAD_SUCCESS_COMMENT=$'AUTOMATIC CROWDIN UPLOAD SUCCESSFUL\n\nThe Jira ticket and subtasks were created or updated, the files were uploaded to Crowdin, and the word count and Crowdin editor links were added or updated.'

# Post a plain-text comment on a Jira issue. Returns 0 on HTTP 201.
jira_post_comment() {
  local issue_key="$1"
  local body="$2"
  local payload http_code

  payload=$(jq -n --arg body "$body" '{body: $body}')
  http_code=$(curl -s -o jira-comment-response.json -w "%{http_code}" \
    -X POST \
    -H "Content-Type: application/json" \
    -u "${LOC_JIRA_USER_EMAIL}:${LOC_JIRA_API_TOKEN}" \
    -d "$payload" \
    "${LOC_JIRA_BASE_URL}/rest/api/2/issue/${issue_key}/comment")

  if [ "$http_code" -ne 201 ]; then
    echo "Failed to post Jira comment on ${issue_key} (HTTP ${http_code})" >&2
    cat jira-comment-response.json >&2
    return 1
  fi
}

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
# Optional: GH_TOKEN, PR_NUMBER, GITHUB_REPOSITORY, GITHUB_EVENT_PATH,
# LOC_JIRA_REPORTER_EMAIL_DOMAIN (e.g. @vtex.com).
resolve_jira_reporter_from_github() {
  local github_login="$1"
  local candidates match_json email_query derived_email display_name

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

  pick_user_by_display_name() {
    local name="$1"
    jq -c --arg name "$name" --arg first "$(printf '%s' "$name" | awk '{print $1}')" \
      --arg last "$(printf '%s' "$name" | awk '{print $NF}')" '
      [.[] | select(.active != false)] |
      if ($first != "" and $last != "" and ($first | ascii_downcase) != ($last | ascii_downcase)) then
        map(select(
          (.displayName // "" | ascii_downcase | contains($first | ascii_downcase)) and
          (.displayName // "" | ascii_downcase | contains($last | ascii_downcase))
        ))
      else
        map(select((.displayName // "" | ascii_downcase | contains($name | ascii_downcase))))
      end |
      .[0] // empty
    '
  }

  reporter_field_from_user() {
    jq -c 'if .accountId then {accountId: .accountId} elif .name then {name: .name} else empty end'
  }

  try_reporter_from_email() {
    local email="$1"
    local via="$2"

    if [ -z "$email" ]; then
      return 1
    fi

    match_json=$(jira_user_search "$email" 5 | pick_user_by_email "$email")
    if [ -n "$match_json" ] && [ "$match_json" != "null" ]; then
      echo "$match_json" | reporter_field_from_user
      echo "Resolved Jira reporter for GitHub user ${github_login} via ${via}" >&2
      return 0
    fi
    return 1
  }

  github_pr_commit_emails() {
    local repo="${GITHUB_REPOSITORY:-}"
    local pr_number="${PR_NUMBER:-}"

    if [ -z "$repo" ] || [ -z "$pr_number" ]; then
      if [ -n "${GITHUB_EVENT_PATH:-}" ] && [ -f "$GITHUB_EVENT_PATH" ]; then
        repo=$(jq -r '.repository.full_name // empty' "$GITHUB_EVENT_PATH")
        pr_number=$(jq -r '.pull_request.number // empty' "$GITHUB_EVENT_PATH")
      fi
    fi

    if [ -z "${GH_TOKEN:-}" ] || [ -z "$repo" ] || [ -z "$pr_number" ] || [ "$pr_number" = "null" ]; then
      return 0
    fi

    gh api "repos/${repo}/pulls/${pr_number}/commits" --paginate \
      --jq ".[] | select((.author.login // \"\") == \"${github_login}\") | .commit.author.email // empty" \
      2>/dev/null \
      | grep -i '@' \
      | grep -vi 'users.noreply.github.com' \
      | grep -vi 'noreply@github.com' \
      | sort -u
  }

  candidates=$(jira_user_search "$github_login" 50)
  match_json=$(echo "$candidates" | pick_existing_user)
  if [ -n "$match_json" ] && [ "$match_json" != "null" ]; then
    echo "$match_json" | reporter_field_from_user
    echo "Resolved Jira reporter for GitHub user ${github_login}" >&2
    return 0
  fi

  while IFS= read -r email_query; do
    if try_reporter_from_email "$email_query" "PR commit email ${email_query}"; then
      return 0
    fi
  done <<< "$(github_pr_commit_emails)"

  if [ -n "${GH_TOKEN:-}" ]; then
    email_query=$(gh api "users/${github_login}" --jq '.email // empty' 2>/dev/null || true)
    if try_reporter_from_email "$email_query" "GitHub profile email"; then
      return 0
    fi

    display_name=$(gh api "users/${github_login}" --jq '.name // empty' 2>/dev/null || true)
    if [ -n "$display_name" ]; then
      match_json=$(jira_user_search "$display_name" 20 | pick_user_by_display_name "$display_name")
      if [ -n "$match_json" ] && [ "$match_json" != "null" ]; then
        echo "$match_json" | reporter_field_from_user
        echo "Resolved Jira reporter for GitHub user ${github_login} via GitHub name \"${display_name}\"" >&2
        return 0
      fi
    fi
  fi

  if [ -n "${LOC_JIRA_REPORTER_EMAIL_DOMAIN:-}" ]; then
    derived_email="${github_login}${LOC_JIRA_REPORTER_EMAIL_DOMAIN}"
    if try_reporter_from_email "$derived_email" "derived email ${derived_email}"; then
      return 0
    fi
  fi

  echo "Could not resolve Jira reporter for GitHub user ${github_login}; using API token user" >&2
  return 1
}

# Drop PR template sections that should not appear in Jira descriptions.
strip_pr_description_sections() {
  awk '
    /^#{1,6}[[:space:]]+Checklist([[:space:]]*|$)/ { skip=1; next }
    /^#{1,6}[[:space:]]+AI review instructions([[:space:]]*|$)/ { skip=1; next }
    /^#{1,6}[[:space:]]+/ { skip=0 }
    !skip { print }
  '
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
