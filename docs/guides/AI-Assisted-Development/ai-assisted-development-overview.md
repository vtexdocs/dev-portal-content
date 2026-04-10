---
title: "AI-assisted development"
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

Building on VTEX involves working across APIs, frameworks, and platform-specific requirements. To help AI coding assistants operate more effectively in that environment, VTEX provides two complementary tools: [VTEX Developer MCP](/docs/guides/vtex-developer-mcp) and [VTEX Skills](/docs/guides/vtex-skills).

VTEX Developer MCP gives AI assistants access to VTEX documentation and API references during a task. VTEX Skills provides persistent context about VTEX-specific patterns, constraints, and best practices. Together, these tools help your assistant retrieve up-to-date information and apply platform-specific guidance more effectively.

## VTEX Developer MCP

The `@vtex/developer-mcp` package is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that connects AI coding assistants to VTEX documentation and API specifications. It exposes four tools: documentation search, document fetching, endpoint search, and endpoint detail lookup.

No API key or authentication is required. To run it locally, use:

```sh
npx -y @vtex/developer-mcp
```

VTEX Developer MCP works with Cursor, VS Code with GitHub Copilot, Claude Code, and Claude Desktop.

For setup instructions and available tools, see [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp).

## VTEX Skills

VTEX Skills is a catalog of 42 AI agent skills for VTEX platform development. The catalog is maintained from a single source and exported in six formats for different AI development tools. 

These skills provide guidance on VTEX-specific implementation details, including topics such as Overrides API behavior, Payment Provider Protocol (PPP) endpoints, BFF patterns, and Master Data limits. 

The catalog is organized into six tracks: Architecture, FastStore, Payment, VTEX IO, Marketplace, and Headless.

To install VTEX Skills, run:

```sh
npx skills add vtex/skills
```

For installation options and the full catalog, see [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills).

## How they work together

The MCP and Skills serve different purposes and complement each other well. Use VTEX Developer MCP when your assistant needs to search documentation, inspect API references, or retrieve information dynamically during a task.

Use VTEX Skills when your assistant benefits from persistent context about recommended patterns, known constraints, and platform-specific implementation guidance.

Using both tools together gives your assistant access to current reference material and reusable VTEX-specific context.

| Tool | Purpose | Installation | Supported platforms |
|---|---|---|---|
| [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp) | Connects AI assistants to VTEX documentation and API references | `npx -y @vtex/developer-mcp` | Cursor, VS Code, Claude Code, Claude Desktop |
| [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills) | Provides VTEX-specific patterns, constraints, and best practices as a persistent AI context | `npx skills add vtex/skills` | Cursor, Copilot, Claude, AGENTS.md, OpenCode, Kiro |

## Next steps

- [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp): Set up the MCP server and explore available tools.
- [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills): Install AI skills and browse the track catalog.
- [Developer experience](https://developers.vtex.com/docs/guides/developer-experience): Learn about other VTEX developer tools and resources.
