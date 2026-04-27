---
title: "VTEX Skills"
slug: "vtex-skills"
hidden: false
createdAt: "2026-04-09T19:00:00.000Z"
updatedAt: "2026-04-09T19:00:00.000Z"
excerpt: "Install AI agent skills that encode VTEX-specific patterns, constraints, and best practices into your AI coding assistant."
seeAlso:
 - "/docs/guides/ai-assisted-development-overview"
 - "/docs/guides/vtex-developer-mcp"
hidePaginationPrevious: false
hidePaginationNext: false
---

[<i class="fa-brands fa-github"></i> Source code](https://github.com/vtex/skills)

VTEX Skills is a collection of AI agent skills for VTEX platform development. It provides a single source of VTEX-specific guidance.

Skills encode platform-specific patterns, constraints, and best practices into your AI coding assistant, giving it context that goes beyond generic model knowledge.

Generic AI assistants do not reliably know VTEX-specific implementation details. Topics such as Overrides APIs, Payment Provider Protocol (PPP) endpoints, BFF requirements, and Master Data limits often require more context than a general-purpose model can provide on its own. VTEX Skills helps fill that gap with practical guidance grounded in VTEX platform knowledge.

- **Platform-specific constraints**: Give your assistant access to details such as Secure Proxy usage for PCI-sensitive flows, idempotency requirements for payment endpoints, the 2.5-second fulfillment simulation timeout, and the 60-schema Master Data limit.
- **One source, multiple platforms**: Skills are authored once and exported automatically to six supported formats.
- **Based on VTEX documentation**: Skill content is derived from official VTEX documentation.
- **Compatible with existing tools**: Works with Cursor, GitHub Copilot, Claude, OpenCode, Kiro, and many other agent-based development tools.
- **No configuration required**: The `npx` installer detects your supported tools and places files in the appropriate locations.
- **Versioned and maintained**: Skills are versioned and updated as the underlying documentation evolves.

## Behavior

Skills are plain-text files that AI agents can load as a persistent working context before generating code.

When you install VTEX Skills, your agent gets guidance on:

- Which APIs to call for a given use case and what parameters they expect
- Platform constraints that aren't obvious from API docs alone (rate limits, schema caps, timeout windows)
- Correct patterns for common tasks like setting up a FastStore override, implementing a PPP endpoint, or configuring a MasterData entity
- Security requirements specific to VTEX, including PCI scope boundaries and Secure Proxy usage

The VTEX Skills CLI detects supported AI tools installed in your environment and places the exported files in the correct locations automatically.

### VTEX Skills vs. VTEX Developer MCP

VTEX Skills and [VTEX Developer MCP](/docs/guides/vtex-developer-mcp) serve different purposes and can be used together.

The [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp) gives your AI assistant access to VTEX documentation and API references during a task. This is useful when the agent needs to look up information dynamically.

VTEX Skills provides a standing context. Instead of retrieving documentation at runtime, the agent starts with prepackaged guidance about common VTEX patterns and constraints.

For the best results, use both the **VTEX Skills** for persistent platform context and **VTEX Developer MCP** for live documentation lookup.

## Installation

The fastest way to get started is with `npx`. It detects the AI tools you have installed and places skill files in the appropriate locations. If you prefer manual installation or need to target a specific platform, use the platform-specific commands below.

### npx (Recommended)

Works with Cursor, Claude Code, Codex, OpenCode, and 38+ agents. Auto-detects installed AI tools.

```bash
npx skills add vtex/skills
```

Use `--list` to preview available skills, or `--all` to install everything non-interactively. This uses the [open skills CLI](https://github.com/vercel-labs/skills).

### AGENTS.md

Works with Cursor, Copilot, Codex, Windsurf, Amp, Devin, and more:

```bash
curl -sL https://github.com/vtex/skills/releases/latest/download/agents-md.tar.gz | tar xz -C your-project/
```

### Cursor

```bash
mkdir -p your-project/.cursor/rules
curl -sL https://github.com/vtex/skills/releases/latest/download/cursor-rules.tar.gz | tar xz -C your-project/.cursor/rules/
```

### GitHub Copilot

```bash
mkdir -p your-project/.github
curl -sL https://github.com/vtex/skills/releases/latest/download/copilot-instructions.tar.gz | tar xz -C your-project/.github/
```

### Claude Projects

Upload files from [`exports/claude/`](https://github.com/vtex/skills/tree/main/exports/claude) as project knowledge in your Claude Project settings.

### OpenCode

```bash
curl -sL https://github.com/vtex/skills/releases/latest/download/opencode-skills.tar.gz | tar xz -C ~/.config/opencode/skills/
```

### Kiro

Clone the repository and copy the Kiro export files:

```bash
git clone https://github.com/vtex/skills.git
cp -r skills/exports/kiro/. your-project/
```

## Tracks and skills

Skills are organized into six tracks covering the main VTEX development surfaces. Each track group relates skills, so your agent gets focused context for the work at hand. You can install all tracks at once or pick only the ones relevant to your project.

| Track | Skills | Description |
|---|---|---|
| Well-Architected Commerce | 1 | Cross-cutting architecture guidance and solution design |
| FastStore Implementation | 4 | Overrides, theming, SDK hooks, and data fetching for FastStore storefronts |
| Payment Connector Development | 5 | Payment Provider Protocol endpoints, framework lifecycle, idempotency, async flows, and PCI compliance |
| Custom VTEX IO Apps | 24 | Foundations, API exposure, frontend, data and config, security, and operations for IO app development |
| Marketplace Integration | 4 | SKU catalog sync, order hooks, fulfillment simulation, and rate limiting |
| Headless Front-End Development | 4 | BFF architecture, Intelligent Search API, checkout proxy patterns, and caching strategy |

The Custom VTEX IO Apps track is the largest, with 24 skills covering the full lifecycle of IO app development. If you're building a new IO app, install that track first.

## Supported platforms

Skills are available in six formats, one for each major AI development platform. All formats contain the same underlying content. The difference is how each platform discovers and loads the files.

| Platform | Format | Auto-detection |
|---|---|---|
| AGENTS.md | Markdown | Yes (native in 7+ tools) |
| Cursor | `.mdc` rules | Yes (glob + description) |
| GitHub Copilot | Instructions | Yes (auto-loaded) |
| Claude Projects | Knowledge files | Manual upload |
| OpenCode | `SKILL.md` | Yes (auto-discovered) |
| Kiro | `POWER.md` + steering | Yes (auto-discovered) |

The `npx` installer handles placement automatically for all detected tools. For platforms that are not detected automatically such as Claude Projects, use the manual install commands above.

## Keeping skills up to date

Skills are versioned and released alongside VTEX documentation updates. To update to the latest version, re-run the install command for your platform. The `npx` approach always pulls the latest release.

If you installed via `curl`, check the [releases page](https://github.com/vtex/skills/releases) for changelogs before updating.

> **Tip**: Pin a specific version in CI environments to avoid unexpected behavior from skill updates. Use `npx skills add vtex/skills@<version>` or reference a tagged release URL in your `curl` commands.

## Learn more

For the full skill catalog, per-track details, and contributing guide, see the [VTEX Skills GitHub repository](https://github.com/vtex/skills).
