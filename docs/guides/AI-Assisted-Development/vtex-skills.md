---
title: "VTEX Skills"
slug: "vtex-skills"
hidden: false
createdAt: "2026-04-09T19:00:00.000Z"
updatedAt: "2026-06-08T19:00:00.000Z"
excerpt: "Install AI agent skills that encode VTEX-specific patterns, constraints, and best practices into your AI coding assistant."
seeAlso:
 - "/docs/guides/vtex-ai-developer-toolkit-overview"
 - "/docs/guides/vtex-developer-mcp"
hidePaginationPrevious: false
hidePaginationNext: false
---

[<i class="fa-brands fa-github"></i> Source code](https://github.com/vtex/skills)

VTEX Skills is a catalog of AI agent skills for VTEX platform development, available as part of the [VTEX AI Developer Toolkit](https://developers.vtex.com/docs/guides/vtex-ai-developer-toolkit-overview). 

> The [VTEX AI Developer Toolkit](https://developers.vtex.com/docs/guides/vtex-ai-developer-toolkit-overview) also includes the [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp), which retrieves VTEX documentation and API references on demand. VTEX Skills and VTEX Developer MCP are complementary: VTEX Skills loads persistent platform context before a task starts, while the MCP provides live lookup.

A skill is a plain-text file that an AI agent loads as persistent context before generating code. In VTEX Skills, this context provides platform-specific guidance based on VTEX product knowledge and official documentation. Use skills to help agents follow VTEX patterns, constraints, and implementation requirements when working with VTEX projects.

VTEX Skills covers:

- **Platform constraints**: Limits and requirements specific to the VTEX platform, such as rate limits, schema caps, and timeout windows.
- **APIs and parameters**: Which APIs to call for a given use case and the parameters they expect.
- **Implementation patterns**: Recommended approaches for common tasks, such as setting up a FastStore override, implementing a PPP endpoint, or configuring a Master Data entity.
- **Security requirements**: VTEX-specific boundaries, including PCI scope and Secure Proxy usage.

## Available skills

Skills are organized into tracks. Each track groups related skills for a VTEX development area, so the agent gets focused context for the task. You can install all tracks at once or select only the ones relevant to your project.

| Track | Description |
|---|---|
| Commerce architecture | Architecture guidance and solution design for VTEX projects |
| FastStore | Overrides, theming, SDK hooks, and data fetching for FastStore storefronts |
| Headless frontend development | BFF architecture, Intelligent Search API, checkout proxy patterns, and caching strategy |
| Marketplace | SKU catalog sync, order hooks, fulfillment simulation, and rate limiting |
| Payment | Payment Provider Protocol endpoints, framework lifecycle, idempotency, async flows, and PCI compliance |
| [Sales App](https://developers.vtex.com/docs/guides/vtex-sales-app-extensions-skill) | VTEX Sales App extension points (cart, PDP, menu), [React hooks](https://developers.vtex.com/docs/guides/sales-app-extension-hooks-and-types), TypeScript types, secure API integration patterns, code generation, validation, and deployment |
| VTEX IO | App foundations, API exposure, frontend, data and configuration, security, and operations for IO app development |

The VTEX IO track covers the full lifecycle of VTEX IO app development. If you are building a new VTEX IO app, install this track first.

For the full skill catalog, per-track details, and contributing guide, see the [VTEX Skills GitHub repository](https://github.com/vtex/skills).

## Installation

Installation with `npx` is recommended. It auto-detects the AI tools installed in your environment and places the skill files where each one expects them. 

```bash
npx skills add vtex/skills
```

Use `--list` to preview available skills, or `--all` to install all available skills without interactive prompts. 

The installer supports tools such as Cursor, Claude Code, Codex, and OpenCode. To use VTEX Skills with Claude Projects, manually upload the skill files as described in the instructions below.


### Manual installation

- **Claude Projects**: Upload the files from [`exports/claude/`](https://github.com/vtex/skills/tree/main/exports/claude) as project knowledge in your Claude Project settings.

- **AGENTS.md**: Use this format for tools that support AGENTS.md, including Cursor, Copilot, Codex, Windsurf, Amp, and Devin.
  
    ```bash
    curl -sL https://github.com/vtex/skills/releases/latest/download/agents-md.tar.gz | tar xz -C your-project/
    ```

- **Cursor**

    ```bash
    mkdir -p your-project/.cursor/rules
    curl -sL https://github.com/vtex/skills/releases/latest/download/cursor-rules.tar.gz | tar xz -C your-project/.cursor/rules/
    ```

- **GitHub Copilot**

    ```bash
    mkdir -p your-project/.github
    curl -sL https://github.com/vtex/skills/releases/latest/download/copilot-instructions.tar.gz | tar xz -C your-project/.github/
    ```

- **OpenCode**

    ```bash
    curl -sL https://github.com/vtex/skills/releases/latest/download/opencode-skills.tar.gz | tar xz -C ~/.config/opencode/skills/
    ```

- **Kiro**: Clone the repository and copy the Kiro export files.
   
   ```bash
   git clone https://github.com/vtex/skills.git
   cp -r skills/exports/kiro/. your-project/
   ```

## Versioning and updates

Skills are versioned and released alongside VTEX documentation updates. To update to the latest version, re-run the install command for your platform. The `npx` command always pulls the latest release.

If you installed via `curl`, check the [releases page](https://github.com/vtex/skills/releases) for changelogs before updating.

> ⚠️ To avoid unexpected behavior from skill updates in CI environments, you can pin a specific version. Use `npx skills add vtex/skills@<version>` or reference a tagged release URL in your `curl` commands.
