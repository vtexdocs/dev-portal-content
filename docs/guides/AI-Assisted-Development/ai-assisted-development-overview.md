---
title: "AI-Assisted Development"
slug: "ai-assisted-development-overview"
hidden: false
createdAt: "2026-04-09T19:00:00.000Z"
updatedAt: "2026-04-09T19:00:00.000Z"
excerpt: "Learn how VTEX AI-powered tools help developers build on the platform faster with real-time documentation access and domain-specific AI skills."
seeAlso:
 - "/docs/guides/vtex-developer-mcp"
 - "/docs/guides/vtex-skills"
hidePaginationPrevious: false
hidePaginationNext: false
---

VTEX is a composable and complete commerce platform, and building on it means working with a large surface area of APIs, frameworks, and platform-specific constraints. Two complementary tools help your AI coding assistant navigate that surface: the **VTEX Developer MCP** and **VTEX Skills**.

The VTEX Developer MCP gives AI assistants real-time access to VTEX documentation and API references. VTEX Skills encodes platform-specific patterns, constraints, and best practices directly into your AI agent. Together, they give your assistant both current knowledge and domain expertise — so it can look things up and know how to build correctly.

## VTEX Developer MCP

The `@vtex/developer-mcp` package is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that connects AI coding assistants to VTEX documentation and API specifications. It exposes four tools: documentation search, document fetching, endpoint search, and endpoint detail lookup.

No API key or authentication is required. Run it with a single command:

```sh
npx -y @vtex/developer-mcp
```

It works with Cursor, VS Code (GitHub Copilot), Claude Code, and Claude Desktop.

For setup instructions and available tools, see the [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp) guide.

## VTEX Skills

VTEX Skills is a catalog of 42 AI agent skills for VTEX platform development, available in six export formats from a single source. Skills encode real platform constraints that LLMs don't know out of the box — things like Overrides API behavior, PPP endpoint requirements, BFF patterns, and MasterData limits.

The catalog covers six tracks: Architecture, FastStore, Payment, VTEX IO, Marketplace, and Headless. Install the full set with:

```sh
npx skills add vtex/skills
```

For installation options and the full skill catalog, see the [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills) guide.

## How they work together

The MCP and Skills serve different purposes and complement each other well. The MCP handles real-time lookups — your assistant can fetch the latest API spec or search the docs mid-task. Skills handle domain knowledge — your assistant already knows the right patterns before it starts writing code.

Use both for the best experience. The MCP keeps your assistant current; Skills keep it correct.

## Quick comparison

| Tool | What it does | How to install | Supported platforms |
|---|---|---|---|
| [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp) | Gives AI assistants access to VTEX documentation and API references | `npx -y @vtex/developer-mcp` | Cursor, VS Code, Claude Code, Claude Desktop |
| [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills) | Encodes VTEX-specific patterns and constraints into AI agents | `npx skills add vtex/skills` | Cursor, Copilot, Claude, AGENTS.md, OpenCode, Kiro |

## Next steps

- [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp) — Set up the MCP server and explore available tools.
- [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills) — Install AI skills and browse the track catalog.
- [Developer experience](https://developers.vtex.com/docs/guides/developer-experience) — Learn about other VTEX developer tools and resources.
