import os
import sys
from github import Github
import yaml
import re
import json

# Get environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY')
GITHUB_EVENT_PATH = os.getenv('GITHUB_EVENT_PATH')

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

g = Github(GITHUB_TOKEN)
repo = g.get_repo(GITHUB_REPOSITORY)
pr = repo.get_pull(pr_number)

def plural_list(list):
    return 's' if len(list) != 1 else ''

# Get changed Markdown files in the PR (only in 'docs/guides', 'docs/release-notes', 'docs/troubleshooting', and 'docs/faststore' folders)
changed_files = [f for f in pr.get_files() if (
    f.filename.endswith(('.md', '.mdx'))
    and f.filename.startswith(('docs/guides/', 'docs/release-notes/', 'docs/troubleshooting/', 'docs/faststore/'))
)]

print(f"Found {len(changed_files)} markdown file{plural_list(changed_files)} in PR:")

error_found = False
frontmatters = {}
file_errors = {}  # filename -> list of error strings
for f in changed_files:
    print(f"- {f.filename}")
    content = repo.get_contents(f.filename, ref=pr.head.ref)
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
                    generic_errors.append(f"Frontmatter in '{f.filename}' is not a valid YAML dictionary.")
                    error_found = True
                    fm_dict = {}
            except Exception as e:
                generic_errors.append(f"Failed to parse YAML frontmatter: {e}")
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
                        field_errors.append({"field": "title", "message": "'title' must be a non-empty string"})
                        error_found = True
                    continue
                if key == 'excerpt':
                    if not isinstance(value, str):
                        field_errors.append({"field": "excerpt", "message": "'excerpt' must be a string"})
                        error_found = True
                    continue
                if key == 'slug':
                    if not (isinstance(value, str) and re.fullmatch(r'[a-z0-9\-]+', value)):
                        field_errors.append({"field": "slug", "message": "'slug' must contain only lowercase letters, numbers, and hyphens"})
                        error_found = True
                    if value != f.filename.split('/')[-1].replace('.mdx', '').replace('.md', ''):
                        field_errors.append({"field": "slug", "message": "'slug' must match the filename without extension"})
                        error_found = True
                    if f.filename.startswith('docs/release-notes') and not date_regex.match(value):
                        field_errors.append({"field": "slug", "message": "'slug' must start with date in format YYYY-MM-DD"})
                        error_found = True
                    continue
                if key == 'hidden':
                    if not isinstance(value, bool):
                        field_errors.append({"field": "hidden", "message": "'hidden' must be a boolean"})
                        error_found = True
                    continue
                if key == 'createdAt':
                    if not (isinstance(value, str) and iso8601_regex.match(value)):
                        field_errors.append({"field": "createdAt", "message": "'createdAt' must be in ISO 8601 format (YYYY-MM-DDThh:mm:ss.sssZ)."})
                        error_found = True
                    continue
                if key == 'updatedAt':
                    if not (isinstance(value, str) and iso8601_regex.match(value)):
                        field_errors.append({"field": "updatedAt", "message": "'updatedAt' must be in ISO 8601 format (YYYY-MM-DDThh:mm:ss.sssZ)."})
                        error_found = True
                    continue
                if key == 'tags':
                    if not (isinstance(value, list)):
                        field_errors.append({"field": "tags", "message": "'tags' must be a list"})
                        error_found = True
                    continue
                if key == 'type':
                    allowed_types = {"added", "deprecated", "fixed", "improved", "info", "removed"}
                    if not (isinstance(value, str) and value in allowed_types):
                        field_errors.append({"field": "type", "message": "'type' must be one of: added, deprecated, fixed, improved, info, removed"})
                        error_found = True

            # Validate mandatory fields for all doc types
            if 'title' not in fm_dict:
                field_errors.append({"field": "title", "message": "Missing required field: 'title'"})
                error_found = True

            # Validate fields by doc type using folder structure
            def not_present_keys(keys, dict):
                return [key for key in keys if key not in dict]

            rn_mandatory_fields = ['type', 'slug', 'excerpt', 'createdAt']
            guides_mandatory_fields = ['slug', 'excerpt']
            ts_mandatory_fields = ['tags', 'slug', 'excerpt']

            if f.filename.startswith('docs/release-notes'):
                missing_fields = not_present_keys(rn_mandatory_fields, fm_dict)
                if missing_fields:
                    for mf in missing_fields:
                        field_errors.append({"field": mf, "message": f"Missing required field: '{mf}'"})
                    error_found = True
            else:
                if 'type' in fm_dict:
                    field_errors.append({"field": "type", "message": "'type' should not be present for non-release notes."})
                    error_found = True

            if f.filename.startswith('docs/guides'):
                missing_fields = not_present_keys(guides_mandatory_fields, fm_dict)
                if missing_fields:
                    for mf in missing_fields:
                        field_errors.append({"field": mf, "message": f"Missing required field: '{mf}'"})
                    error_found = True

            if f.filename.startswith('docs/troubleshooting'):
                missing_fields = not_present_keys(ts_mandatory_fields, fm_dict)
                if missing_fields:
                    for mf in missing_fields:
                        field_errors.append({"field": mf, "message": f"Missing required field: '{mf}'"})
                    error_found = True

        else:
            generic_errors.append(f"Frontmatter not closed with '---'.")
            error_found = True
    else:
        generic_errors.append(f"Markdown file does not start with frontmatter block ('---').")
        error_found = True

    if generic_errors or field_errors:
        file_errors[f.filename] = {
            "generic": generic_errors,
            "fields": field_errors,
        }

# Post a comment per file with errors
if file_errors:
    comment_body = f"### 🏷️ Frontmatter errors\n\n"
    for filename, issues in file_errors.items():
        generic = issues["generic"]
        fields = issues["fields"]

        comment_body = comment_body + f"#### `{filename}`\n\n"

        # Lista de erros gerais
        if generic:
            for err in generic:
                comment_body += f"- {err}\n"
            comment_body += "\n"

        # Tabela de erros por campo
        if fields:
            comment_body += "#### Field issues\n\n"
            comment_body += "| Field | Error |\n"
            comment_body += "|-------|--------|\n"
            for err in fields:
                field = err.get("field", "") or ""
                message = err.get("message", "")
                comment_body += f"| `{field}` | {message} |\n"


        pr.create_issue_comment(comment_body)
    print(' \n')
    print("Frontmatter errors found. Failing the action.")
    sys.exit(1)