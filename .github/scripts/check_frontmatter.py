import os
import sys
from github import Auth, Github
import yaml
import re
import json

# Get environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY')
GITHUB_EVENT_PATH = os.getenv('GITHUB_EVENT_PATH')
GITHUB_SERVER_URL = os.getenv('GITHUB_SERVER_URL', 'https://github.com')
GITHUB_RUN_ID = os.getenv('GITHUB_RUN_ID')

if not (GITHUB_TOKEN and GITHUB_REPOSITORY and GITHUB_EVENT_PATH):
    print('Missing required environment variables.')
    sys.exit(1)

# Load event data
event = {}
with open(GITHUB_EVENT_PATH, 'r') as f:
    event = json.load(f)

pr_number = event.get('pull_request', {}).get('number')
if not pr_number:
    print('Not a pull request event.')
    sys.exit(0)

g = Github(auth=Auth.Token(GITHUB_TOKEN))
repo = g.get_repo(GITHUB_REPOSITORY)
pr = repo.get_pull(pr_number)

# Fixed marker used to identify the frontmatter review comment
COMMENT_MARKER = "<!-- frontmatter-review-comment -->"

# Commit being reviewed
head_sha = pr.head.sha

def plural_list(list):
    return 's' if len(list) != 1 else ''


# Get changed Markdown files in the PR (only in 'docs/guides', 'docs/release-notes', 'docs/troubleshooting', and 'docs/faststore' folders)
# Skip files deleted in the PR: they don't exist at head_sha, so get_contents would raise a 404
changed_files = [f for f in pr.get_files() if (
    f.status != 'removed'
    and f.filename.endswith(('.md', '.mdx'))
    and (
        f.filename.startswith(('docs/guides/', 'docs/release-notes/', 'docs/faststore/'))
        or (f.filename.startswith('docs/troubleshooting/') and f.filename.count('/') > 2)
    )
)]

print(f"Found {len(changed_files)} markdown file{plural_list(changed_files)} in PR:")

error_found = False
warning_found = False
frontmatters = {}
file_issues = {}  # filename -> {"generic": [...], "fields": [...]}
for f in changed_files:
    print(f"- {f.filename}")
    content = repo.get_contents(f.filename, ref=head_sha)
    text = content.decoded_content.decode('utf-8')
    generic_errors = []
    field_errors = []

    # Extract frontmatter
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            frontmatter = text[3:end+1].strip()
            try:
                fm_dict = yaml.safe_load(frontmatter)
                if not isinstance(fm_dict, dict):
                    generic_errors.append({"severity": "error", "message": f"Frontmatter in '{f.filename}' is not a valid YAML dictionary."})
                    error_found = True
                    fm_dict = {}
            except Exception as e:
                generic_errors.append({"severity": "error", "message": f"Failed to parse YAML frontmatter: {e}"})
                error_found = True
                fm_dict = {}

            print(fm_dict)
            frontmatters[f.filename] = fm_dict

            # Regular expression for ISO 8601 date format (YYYY-MM-DDThh:mm:ss.sssZ)
            iso8601_regex = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$")

            # Regular expression for date format (YYYY-MM-DD)
            date_regex = re.compile(r"^\d{4}-\d{2}-\d{2}-")

            # Validate formatting in present fields
            for key, value in fm_dict.items():
                if key == 'title':
                    if not isinstance(value, str) or not value:
                        field_errors.append({"field": "title", "severity": "error", "message": "'title' must be a non-empty string"})
                        error_found = True
                    continue
                if key == 'excerpt':
                    if not isinstance(value, str):
                        field_errors.append({"field": "excerpt", "severity": "error", "message": "'excerpt' must be a string"})
                        error_found = True
                    continue
                if key == 'slug':
                    if not (isinstance(value, str) and re.fullmatch(r'[a-z0-9\-]+', value)):
                        field_errors.append({"field": "slug", "severity": "error", "message": "'slug' must contain only lowercase letters, numbers, and hyphens"})
                        error_found = True
                    if value != f.filename.split('/')[-1].replace('.mdx', '').replace('.md', ''):
                        field_errors.append({"field": "slug", "severity": "error", "message": "'slug' must match the filename without extension"})
                        error_found = True
                    if f.filename.startswith('docs/release-notes') and not date_regex.match(value):
                        field_errors.append({"field": "slug", "severity": "error", "message": "'slug' in release notes must start with date in format YYYY-MM-DD"})
                        error_found = True
                    continue
                if key == 'hidden':
                    if not isinstance(value, bool):
                        field_errors.append({"field": "hidden", "severity": "error", "message": "'hidden' must be a boolean"})
                        error_found = True
                    continue
                if key == 'createdAt':
                    if not (isinstance(value, str) and iso8601_regex.match(value)):
                        field_errors.append({"field": "createdAt", "severity": "error", "message": "'createdAt' must be in ISO 8601 format (YYYY-MM-DDThh:mm:ss.sssZ)."})
                        error_found = True
                    continue
                if key == 'updatedAt':
                    if not (isinstance(value, str) and iso8601_regex.match(value)):
                        field_errors.append({"field": "updatedAt", "severity": "error", "message": "'updatedAt' must be in ISO 8601 format (YYYY-MM-DDThh:mm:ss.sssZ)."})
                        error_found = True
                    continue
                if key == 'tags':
                    if not (isinstance(value, list)):
                        field_errors.append({"field": "tags", "severity": "error", "message": "'tags' must be a list"})
                        error_found = True
                    continue
                if key == 'domainFilters':
                    if not isinstance(value, list):
                        field_errors.append({"field": "domainFilters", "severity": "error", "message": "'domainFilters' must be a list"})
                        error_found = True
                    continue
                if key == 'symptomFilters':
                    if not isinstance(value, list):
                        field_errors.append({"field": "symptomFilters", "severity": "error", "message": "'symptomFilters' must be a list"})
                        error_found = True
                    continue
                if key == 'type':
                    allowed_types = {"added", "deprecated", "fixed", "improved", "info", "removed"}
                    if not (isinstance(value, str) and value in allowed_types):
                        field_errors.append({"field": "type", "severity": "error", "message": "'type' must be one of: added, deprecated, fixed, improved, info, removed"})
                        error_found = True

            # Validate mandatory fields for all doc types
            if 'title' not in fm_dict:
                field_errors.append({"field": "title", "severity": "error", "message": "Missing required field: 'title'"})
                error_found = True

            # Validate fields by doc type using folder structure
            def not_present_keys(keys, dict):
                return [key for key in keys if key not in dict]

            rn_mandatory_fields = ['type', 'slug', 'excerpt', 'createdAt']
            guides_mandatory_fields = ['slug']
            ts_mandatory_fields = ['domainFilters', 'symptomFilters', 'slug']

            if f.filename.startswith('docs/release-notes'):
                missing_fields = not_present_keys(rn_mandatory_fields, fm_dict)
                if missing_fields:
                    for mf in missing_fields:
                        field_errors.append({"field": mf, "severity": "error", "message": f"Missing required field: '{mf}'"})
                    error_found = True
            else:
                if 'type' in fm_dict:
                    field_errors.append({"field": "type", "severity": "error", "message": "'type' should not be present for non-release notes."})
                    error_found = True
                if 'excerpt' not in fm_dict:
                    field_errors.append({"field": "excerpt", "severity": "warning", "message": "Missing recommended field: 'excerpt'"})
                    warning_found = True

            if f.filename.startswith('docs/guides'):
                missing_fields = not_present_keys(guides_mandatory_fields, fm_dict)
                if missing_fields:
                    for mf in missing_fields:
                        field_errors.append({"field": mf, "severity": "error", "message": f"Missing required field: '{mf}'"})
                    error_found = True

            if f.filename.startswith('docs/troubleshooting'):
                missing_fields = not_present_keys(ts_mandatory_fields, fm_dict)
                if missing_fields:
                    for mf in missing_fields:
                        field_errors.append({"field": mf, "severity": "error", "message": f"Missing required field: '{mf}'"})
                    error_found = True

        else:
            generic_errors.append({"severity": "error", "message": "Frontmatter not closed with '---'."})
            error_found = True
    else:
        generic_errors.append({"severity": "error", "message": "Markdown file does not start with frontmatter block ('---')."})
        error_found = True

    if generic_errors or field_errors:
        file_issues[f.filename] = {
            "generic": generic_errors,
            "fields": field_errors,
        }

def find_existing_comment():
    """Find the PR comment previously created by this script (identified by the marker)."""
    # Only look at issue comments of the PR (not line-level review comments)
    for comment in pr.get_issue_comments():
        if COMMENT_MARKER in comment.body:
            return comment
    return None

def upsert_pr_comment(body):
    """Edit the existing marker comment if there is one; otherwise create a new one."""
    existing_comment = find_existing_comment()
    if existing_comment:
        print("Updating existing frontmatter review comment...")
        existing_comment.edit(body)
    else:
        print("Creating new frontmatter review comment...")
        pr.create_issue_comment(body)

SEVERITY_LABELS = {
    "error": "❌ Error",
    "warning": "⚠️ Warning",
}

run_url = (
    f"{GITHUB_SERVER_URL}/{GITHUB_REPOSITORY}/actions/runs/{GITHUB_RUN_ID}"
    if GITHUB_RUN_ID
    else None
)
footer = f"Review made on commit {head_sha or '(unknown)'}"
if run_url:
    footer += f"\nGenerated by [check-frontmatter workflow]({run_url})"

# Build and post a single comment with the review results
if file_issues:
    heading = "### 🏷️ Frontmatter issues"
    comment_body = f"{COMMENT_MARKER}\n{heading}\n\n"
    for filename, issues in file_issues.items():
        generic = issues["generic"]
        fields = issues["fields"]

        comment_body += f"#### `{filename}`\n\n"

        # General issues list
        if generic:
            for item in generic:
                severity_label = SEVERITY_LABELS.get(item.get("severity", "error"), "❌ Error")
                comment_body += f"- **{severity_label}:** {item['message']}\n"
            comment_body += "\n"

        # Per-field issues table
        if fields:
            comment_body += "#### Field issues\n\n"
            comment_body += "| Field | Severity | Issue |\n"
            comment_body += "|-------|----------|-------|\n"
            for item in fields:
                field = item.get("field", "") or ""
                severity_label = SEVERITY_LABELS.get(item.get("severity", "error"), "❌ Error")
                message = item.get("message", "")
                comment_body += f"| `{field}` | {severity_label} | {message} |\n"
            comment_body += "\n"

    comment_body += f"\n{footer}"
    upsert_pr_comment(comment_body)

    if error_found:
        print(' \n')
        print("Frontmatter errors found. Failing the action.")
        sys.exit(1)
    else:
        print("⚠️ Frontmatter warnings found. Passing the action.")
else:
    comment_body = (
        f"{COMMENT_MARKER}\n"
        "### ✅ Frontmatter check passed\n\n"
        "No frontmatter issues were found in the modified files.\n\n"
        f"{footer}"
    )
    upsert_pr_comment(comment_body)
    print("✅ No frontmatter issues found.")
