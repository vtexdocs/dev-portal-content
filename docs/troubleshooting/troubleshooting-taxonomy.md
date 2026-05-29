# Troubleshooting taxonomy companion for `dev-portal-content`

This document complements the repository strategy file for troubleshooting content.

Use it as the operational guide for applying the taxonomy in daily editorial work. The source of truth for the taxonomy itself is:

- `docs/troubleshooting-categorization-and-filter-strategy.md`

Use the article-by-article mapping file as the operational reference for current assignments:

- `docs/troubleshooting/troubleshooting-taxonomy-matrix.csv`

## Purpose

This companion document exists to:

- explain how to apply the troubleshooting taxonomy in practice
- standardize article structure and naming
- separate repository-specific execution guidance from the governance rules in the strategy file
- highlight what can later be reused across repositories

## How to use this file

When creating or revising a troubleshooting article:

1. Use `docs/troubleshooting-categorization-and-filter-strategy.md` to choose:
   - the primary category
   - the `domainFilters`
   - the `symptomFilters`
2. Use `docs/troubleshooting/troubleshooting-taxonomy-matrix.csv` to check whether an equivalent or overlapping article already exists.
3. Use the guidelines below to shape the article title and body.

## Recommended article structure

Each troubleshooting article should follow this structure when applicable:

1. **Problem**
   Describe the visible issue, error message, or unexpected behavior.
2. **Possible causes**
   Summarize the most likely reasons for the problem.
3. **Solution**
   Provide step-by-step instructions, grouped by cause when useful.
4. **Additional checks**
   Cover edge cases, environment-specific checks, and verification steps.
5. **Related docs**
   Link only to the supporting references needed to complete the solution.

## Editorial guidance

### Titles

Use symptom-first, user-language titles.

Recommended patterns:

- `I can't ...`
- `My ... is not ...`
- `... returns ... error`

Avoid:

- generic titles
- root-cause titles
- procedure-oriented titles that sound like tutorials

### Scope

Each troubleshooting article should focus on one user-visible problem.

If an article starts covering multiple distinct problems, prefer one of these:

- split it into multiple troubleshooting articles
- keep one article, but organize the solution by clear decision paths

### Readability

Prefer:

- short problem statements
- short cause summaries
- actionable step-by-step instructions
- explicit verification steps after the proposed fix

Avoid:

- long conceptual introductions before the first actionable step
- tutorial-style explanations that delay the diagnosis
- repeating product background that already exists in linked reference docs

## Reusable standards vs repository-specific execution

### Repository-specific execution

These decisions should stay in `dev-portal-content`:

- article-specific screenshots and examples
- product-area examples tuned for developer audiences
- repository-specific cross-links
- article-level scope decisions and splits

### Reusable standards

These are the parts that could later be shared with other repositories or centralized in `vtexdocs/components`:

- the three-layer troubleshooting model:
  - primary category
  - domain filters
  - symptom filters
- title conventions
- article structure template
- editorial rules for scannability and actionability
- front matter validation rules for troubleshooting content

## Related files

- Taxonomy strategy:
  - `docs/troubleshooting-categorization-and-filter-strategy.md`
- Current article matrix:
  - `docs/troubleshooting/troubleshooting-taxonomy-matrix.csv`
