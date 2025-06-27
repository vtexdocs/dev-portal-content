# VTEX Developer Portal content

>ℹ This repository is managed by the [VTEX Tech Writing](https://github.com/vtexdocs/dev-portal-content/graphs/contributors) team.

This repository contains all the files for the guides featured in the [VTEX Developer Portal](https://developers.vtex.com).

## Table of Contents

- [Contributing to the documentation](#contributing-to-the-documentation)
  - [Feedback button](#feedback-button)
    - [Feedback type](#feedback-type)
  - [Was this helpful?](#was-this-helpful)
  - [Suggest edits (GitHub)](#suggest-edits-github)
- [GitHub Actions](#github-actions)
  - [Preview Modified Pages](#preview-modified-pages)
  - [Write Good](#write-good)
  - [Check Links](#check-links)
  - [Links Issues](#links-issues)
  - [Update MDX Images](#update-mdx-images)
  - [Check Broken Links](#check-broken-links)
  - [Check VTEX Styleguide](#check-vtex-styleguide)
  - [Navigation Preview](#navigation-preview)
  - [Markdown Lint](#markdown-lint)

## Contributing to the documentation

We invite you to join us and learn how to contribute to our documentation. Your help makes a huge difference in improving our documentation experience. Below are several ways you can do it:

- [Feedback button](#feedback-button)
- [Was this helpful?](#was-this-helpful)
- [Suggest edits (GitHub)](#suggest-edits-github)

## Feedback button

You can provide feedback on any page in the Developer Portal by clicking the `Feedback` button in the top corner of the page.

![feedback](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/feedback.png)

By clicking `Feedback`, a new browser window will open with a [form](https://docs.google.com/forms/d/e/1FAIpQLSfmnotPvPjw-SjiE7lt2Nt3RQgNUe10ixXZmuO2v9enOJReoQ/viewform) where you can share your feedback. Here's the information you need to include in the form:

- **Platform:** Select *Developer Portal* from the three available options: Help Center, Developer Portal, or VTEX Learning Center.
- **URL (Optional):** Enter the exact URL of the specific page you're providing feedback on, such as `https://developers.vtex.com/docs/guides/getting-started-with-storefront-solutions`. Leave this field blank if you're giving a general feedback.
- **Feedback type:** Select the type of feedback you want to give:

| Feedback type | Description |
| --- | --- |
| Comment | Leave a comment about the documentation. |
| Question | Ask any questions you have about the documentation content. |
| Error | Report inaccurate information or issues, such as an unavailable page. |
| Improvement | Suggest improvements to the content. |

- **Feedback:** Describe your feedback based on the selected **Feedback type**.
- **Suggestions (Optional):** Propose changes or improvements to the content.
- **Attachment (Optional):** Upload relevant files, such as screenshots, images, or spreadsheets, to support your feedback.
- **Follow-up:** If you'd like us to contact you about your feedback, select `Yes`. On the next page of the form, provide your name and email so we can reach out to you.

## Was this helpful?

You can submit feedback about any page in the Developer Portal by responding to the `Was this helpful?` option.

![was-this-helpful](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/was-this-helpful.gif)

Select your answer and leave a comment to explain your feedback. Click `Send feedback` to submit it.

## Suggest edits (GitHub)

You can contribute to any page in the Developer Portal by clicking `Suggest edits (GitHub)`.

![suggest-edits-github](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/suggest-edits-github.gif)

By clicking `Suggest edits (GitHub)`, a new browser window will open with the documentation repository page. Follow these steps to contribute using `Suggest edits (GitHub)`:

1. On the documentation repository page, edit the documentation file to include your suggestions.

  > ⚠ Make sure your suggestions follow the documentation guidelines and the code of conduct, and keep the documentation structured as in the template.

2. Click `Commit changes…`.
3. In the **Propose changes** modal, complete the following:

| Field name | Description |
| --- | --- |
| Commit message | Write a short description of your commit, for example, `Fix typo`. |
| Extended description (Optional) | Provide a detailed description of your changes. |
| Create a new branch for this commit and start a pull request | Name your branch to open a pull request, allowing the team to review your suggestions. |

4. Click `Propose changes`.
5. Create a pull request with your changes by completing the following:

![pull-request](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/pull-request.png)

| Field name | Description |
| --- | --- |
| Add a title | Enter a title for your pull request by adding the type of change, the filename, and what you changed, for example, `Fix (customer-credit-integration-guide.md): Documentation typos`. |
| Add a description | Check the type(s) of change(s) you are proposing: New content, Improvement, Fix, or Spelling and grammar accuracy. Also, feel free to provide more details in your description to help the team review your suggestion. |
| Reviewers | Click `Reviewers` and select the group `vtexdocs/vtex-education`. |

6. Click `Create pull request`.

Once you create a pull request, our team will review your changes as soon as possible and follow up with you in the pull request comments.

  > ⚠ Pull requests go through a review process to ensure quality and consistency. Our team may request changes before approving them.


## GitHub Actions

This repository uses several GitHub Actions to ensure documentation quality and provide helpful previews. Here's a detailed overview of each action:

### Preview Modified Pages
**Trigger**: Pull requests  
**Purpose**: Generates preview links for modified markdown/MDX files.  
**Dependencies**:
- `actions/checkout@v3`: Checks out the repository
- `tj-actions/branch-names@v7`: Gets branch name information
- `tj-actions/changed-files@v36`: Detects changed markdown files
- `actions/github-script@v6`: Runs JavaScript in the workflow
- `thollander/actions-comment-pull-request@v2`: Comments on PRs with preview links

### Write Good
**Trigger**: Pull requests  
**Purpose**: Checks documentation quality using textlint with the write-good rule.  
**Dependencies**:
- `actions/checkout@v2`: Checks out the repository
- `actions/setup-node@v1`: Sets up Node.js environment
- `tsuyoshicho/action-textlint@v3`: Runs textlint checks and reports issues

### Check Links
**Trigger**: Pull requests  
**Purpose**: Validates links in modified markdown files.  
**Dependencies**:
- `actions/checkout@master`: Checks out the repository
- `gaurav-nelson/github-action-markdown-link-check@v1`: Performs link checking

### Links Issues
**Trigger**: Repository dispatch, manual workflow, or daily at 17:00 UTC  
**Purpose**: Performs comprehensive link checking and creates issues for broken links.  
**Dependencies**:
- `actions/checkout@v3`: Checks out the repository
- `lycheeverse/lychee-action@v1.5.4`: Performs link checking
- `peter-evans/create-issue-from-file@v4`: Creates issues from check results

### Update MDX Images
**Trigger**: Pull requests to main branch  
**Purpose**: Updates and manages images in MDX files.  
**Dependencies**:
- `actions/checkout@v3`: Checks out the repository
- `tj-actions/changed-files@v29.0.2`: Detects changed files
- `stefanzweifel/git-auto-commit-action@v4`: Commits image updates
- Node.js packages: `front-matter`, `image-downloader`

### Check Broken Links
**Trigger**: Pull requests (opened or synchronized)  
**Purpose**: Checks for broken links in modified markdown files.  
**Dependencies**:
- `actions/checkout@v3`: Checks out the repository
- `actions/setup-node@v3`: Sets up Node.js environment
- `tj-actions/changed-files@v45`: Detects changed markdown files
- `reviewdog/action-setup@v1`: Sets up Reviewdog
- Node.js packages: `node-fetch`, `@actions/core`

### Check VTEX Styleguide
**Trigger**: Pull requests (opened or synchronized)  
**Purpose**: Ensures documentation follows VTEX style guidelines.  
**Dependencies**:
- `actions/checkout@v3`: Checks out the repository
- `actions/setup-node@v3`: Sets up Node.js environment
- `tj-actions/changed-files@v45`: Detects changed markdown files
- `reviewdog/action-setup@v1`: Sets up Reviewdog
- Node.js packages: `@actions/core`

### Changelog Generation
**Trigger**: Push to main branch or merged pull requests  
**Purpose**: Automatically generates changelog entries based on commit messages.  
**Dependencies**:
- `actions/checkout@v4`: Checks out the repository
- `actions/setup-node@v4`: Sets up Node.js environment
Commit types supported:
- new: New guides, troubleshooting articles, or release notes
- fix: Bug fixes for typos, broken links, or markdown
- media: Media asset updates
- update: Content updates
- remove: File removals
- loc: Localization changes
- docs: README documentation updates
- feat: New features
- test: Test updates

### Navigation Preview
**Trigger**: Pull requests  
**Purpose**: Provides preview links for navigation changes.  
**Dependencies**:
- `actions/checkout@v3`: Checks out the repository
- `tj-actions/branch-names@v7`: Gets branch name information
- `tj-actions/changed-files@v36`: Detects navigation file changes
- `actions/github-script@v6`: Runs JavaScript in the workflow
- `thollander/actions-comment-pull-request@v2`: Comments on PRs with preview links

### Markdown Lint
**Trigger**: Pull requests  
**Purpose**: Lints markdown files for consistent formatting.  
**Dependencies**:
- `actions/checkout@v1`: Checks out the repository
- `reviewdog/action-markdownlint@v0`: Runs markdown linting with reviewdog integration
