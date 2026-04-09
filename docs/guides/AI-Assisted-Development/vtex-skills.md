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

VTEX Skills is a collection of 42 AI agent skills for VTEX platform development. One source, six export formats. Skills encode VTEX-specific patterns, constraints, and best practices into your AI coding assistant, giving it domain expertise that goes beyond generic LLM knowledge.

## Why use VTEX Skills

AI assistants don't know VTEX-specific patterns out of the box. The Overrides API, PPP endpoints, BFF requirements, and MasterData schema limits aren't in any LLM's training data at the depth you need. Skills fill that gap with real constraints, not generic advice.

- **Platform-specific constraints**: PCI compliance via the Secure Proxy, idempotency requirements on payment endpoints, the 2.5s fulfillment simulation timeout, the 60-schema MasterData limit. These are the details that prevent costly mistakes in production.
- **One source, six platforms**: Skills are authored once and exported automatically. No manual sync, no drift between tools.
- **Built from official VTEX documentation**: Content comes from the same source your team already trusts.
- **Works with your existing tools**: Cursor, GitHub Copilot, Claude, OpenCode, Kiro, and 38+ other agents are supported.
- **No configuration required**: The `npx` installer detects your tools and places files in the right locations. Install once and your agent has the context it needs.
- **Versioned and maintained**: Skills are updated when VTEX documentation changes, so your agent's knowledge stays current.

## How it works

Skills are plain text files your AI agent reads before generating code. When you install VTEX Skills, your agent gets context about:

- Which APIs to call for a given use case and what parameters they expect
- Platform constraints that aren't obvious from API docs alone (rate limits, schema caps, timeout windows)
- Correct patterns for common tasks like setting up a FastStore override, implementing a PPP endpoint, or configuring a MasterData entity
- Security requirements specific to VTEX, including PCI scope boundaries and Secure Proxy usage

The skills CLI detects which AI tools you have installed and places files in the right locations automatically. You don't need to configure anything manually.

### VTEX Skills vs. VTEX Developer MCP

These two tools are complementary, not alternatives.

The [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp) gives your AI assistant real-time access to VTEX documentation and API references. It's useful when your agent needs to look something up during a task.

VTEX Skills encodes that knowledge as standing context. Your agent doesn't need to search for it. Skills are loaded once and stay active throughout your session, so your agent already knows the patterns before you ask your first question.

Use both together for the best results: Skills for domain expertise, MCP for live documentation lookup.

## Quick start

The fastest way to get started is with `npx`. It detects your installed AI tools and places skill files in the right locations. If you prefer manual installation or need to target a specific platform, use the platform-specific commands below.

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

Skills are organized into six tracks covering the main VTEX development surfaces. Each track groups related skills so your agent gets focused context for the work at hand. You can install all tracks at once or pick only the ones relevant to your project.

| Track | Skills | Description |
|---|---|---|
| Well-Architected Commerce | 1 | Cross-cutting architecture guidance and solution design |
| FastStore Implementation | 4 | Overrides, theming, SDK hooks, and data fetching for FastStore storefronts |
| Payment Connector Development | 5 | Payment Provider Protocol endpoints, framework lifecycle, idempotency, async flows, and PCI compliance |
| Custom VTEX IO Apps | 24 | Foundations, API exposure, frontend, data and config, security and operations for IO app development |
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

The `npx` installer handles placement automatically for all detected tools. For platforms not detected automatically (like Claude Projects), use the manual install commands above.

## Keeping skills up to date

Skills are versioned and released alongside VTEX documentation updates. To update to the latest version, re-run the install command for your platform. The `npx` approach always pulls the latest release.

If you installed via `curl`, check the [releases page](https://github.com/vtex/skills/releases) for changelogs before updating.

> **Tip**: Pin a specific version in CI environments to avoid unexpected behavior from skill updates. Use `npx skills add vtex/skills@<version>` or reference a tagged release URL in your `curl` commands.

## Learn more

For the full skill catalog, per-track details, and contributing guide, see the [VTEX Skills GitHub repository](https://github.com/vtex/skills).
