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
for f in changed_files:
    print(f"- {f.filename}")
    content = repo.get_contents(f.filename, ref=pr.head.ref)
    text = content.decoded_content.decode('utf-8')

    # Extract frontmatter
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            frontmatter = text[3:end+1].strip()
            try:
                fm_dict = yaml.safe_load(frontmatter)
                if not isinstance(fm_dict, dict):
                    print(' \n')
                    print(f"ERROR: Frontmatter in '{f.filename}' is not a valid YAML dictionary.")
                    error_found = True
                    fm_dict = {}
            except Exception as e:
                print(f"ERROR: Failed to parse YAML frontmatter in '{f.filename}': {e}")
                error_found = True
                fm_dict = {}
            frontmatters[f.filename] = fm_dict
            print(' \n')
            print(f"Frontmatter dict for '{f.filename}':\n{{")
            for k, v in fm_dict.items():
                print(f"  {k}: {v}")
            print('}')

            # Validate formatting in present fields
            iso8601_regex = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$")
            for key, value in fm_dict.items():
                if key == 'title':
                    if not isinstance(value, str) or not value:
                        print(f"ERROR: '{key}' in '{f.filename}' must be a non-empty string.")
                        error_found = True
                    continue
                if key == 'excerpt':
                    if not isinstance(value, str):
                        print(f"ERROR: '{key}' in '{f.filename}' must be a string.")
                        error_found = True
                    continue
                if key == 'slug':
                    if not (isinstance(value, str) and re.fullmatch(r'[a-z0-9\-]+', value)):
                        print(f"ERROR: 'slug' in '{f.filename}' must contain only lowercase letters, numbers, and hyphens.")
                        error_found = True
                    if value!= f.filename.split('/')[-1].replace('.mdx', '').replace('.md', ''):
                        print(f"ERROR: 'slug' in '{f.filename}' must match the filename without extension.")
                        error_found = True
                    continue
                if key == 'hidden':
                    if not isinstance(value, bool):
                        print(f"ERROR: 'hidden' in '{f.filename}' must be a boolean (true or false).")
                        error_found = True
                    continue
                if key == 'createdAt':
                    if not (isinstance(value, str) and iso8601_regex.match(value)):
                        print(f"ERROR: '{key}' in '{f.filename}' must be a string in ISO 8601 format (YYYY-MM-DDThh:mm:ss.sssZ).")
                        error_found = True
                    continue
                if key == 'updatedAt':
                    if not (isinstance(value, str) and iso8601_regex.match(value)):
                        print(f"ERROR: '{key}' in '{f.filename}' must be a string in ISO 8601 format (YYYY-MM-DDThh:mm:ss.sssZ).")
                        error_found = True
                    continue
                if key == 'tags':
                    if not (isinstance(value, list)):
                        print(f"ERROR: 'tags' in '{f.filename}' must be a list.")
                        error_found = True
                    continue
                if key == 'type':
                    allowed_types = {"added", "deprecated", "fixed", "improved", "info", "removed"}
                    if not (isinstance(value, str) and value in allowed_types):
                        print(f"ERROR: 'type' in '{f.filename}' must be one of: {', '.join(allowed_types)}.")
                        error_found = True

            # Validate mandatory fields for all doc types
            if 'title' not in fm_dict:
                print(f"ERROR: '{f.filename}' must have a 'title' field in frontmatter.")
                error_found = True

            # Validate fields by doc type using folder structure
            def not_present_keys(keys, dict):
                return [key for key in keys if key not in dict]

            rn_mandatory_fields = ['type', 'slug', 'excerpt', 'hidden', 'createdAt', 'updatedAt']
            guides_mandatory_fields = ['slug', 'excerpt', 'hidden', 'createdAt', 'updatedAt']
            ts_mandatory_fields = ['tags', 'slug', 'excerpt', 'hidden', 'createdAt', 'updatedAt']

            if f.filename.startswith('docs/release-notes'):
                missing_fields = not_present_keys(rn_mandatory_fields, fm_dict)
                if missing_fields:
                    print(f"ERROR: '{f.filename}' release note missing {missing_fields} field{plural_list(missing_fields)} in frontmatter.")
                    error_found = True
            else:
                if 'type' in fm_dict:
                    print(f"ERROR: '{f.filename}' should not have a 'type' field in frontmatter for non-release notes.")
                    error_found = True

            if f.filename.startswith('docs/guides'):
                missing_fields = not_present_keys(guides_mandatory_fields, fm_dict)
                if missing_fields:
                    print(f"ERROR: '{f.filename}' guide missing {missing_fields} field{plural_list(missing_fields)} in frontmatter.")
                    error_found = True

            if f.filename.startswith('docs/troubleshooting'):
                missing_fields = not_present_keys(ts_mandatory_fields, fm_dict)
                if missing_fields:
                    print(f"ERROR: '{f.filename}' troubleshooting missing {missing_fields} field{plural_list(missing_fields)} in frontmatter.")
                    error_found = True

            if f.filename.startswith('docs/faststore'):
                if fm_dict.keys() != {'title'}:
                    print(f"ERROR: '{f.filename}' FastStore docs must have only 'title' field in frontmatter.")
                    error_found = True

        else:
            print(f"ERROR: '{f.filename}' frontmatter not closed with '---'.")
            error_found = True
    else:
        print(f"ERROR: '{f.filename}' does not start with frontmatter block ('---').")
        error_found = True

if error_found:
    print(' \n')
    print("Frontmatter errors found. Failing the action.")
    sys.exit(1)
