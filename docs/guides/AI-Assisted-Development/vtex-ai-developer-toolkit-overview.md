---
title: "VTEX AI Developer Toolkit"
slug: "vtex-ai-developer-toolkit-overview"
hidden: false
createdAt: "2026-04-09T19:00:00.000Z"
updatedAt: "2026-06-08T19:00:00.000Z"
excerpt: "Learn how the VTEX AI Developer Toolkit provides documentation access and domain-specific AI skills for building on the platform."
seeAlso:
 - "/docs/guides/vtex-developer-mcp"
 - "/docs/guides/vtex-skills"
---

The VTEX AI Developer Toolkit provides tools that AI agents and coding assistants can use when working with the VTEX platform. The toolkit includes two tools:

- [VTEX Developer MCP](/docs/guides/vtex-developer-mcp): Provides access to VTEX documentation, including the [Help Center](https://help.vtex.com/) and [Developer Portal](https://developers.vtex.com/), and the [VTEX API Reference](https://developers.vtex.com/docs/api-reference). The assistant retrieves this content on demand during a task.
- [VTEX Skills](/docs/guides/vtex-skills): Loads persistent context about VTEX-specific architecture patterns, platform constraints, and implementation guidance.

The two tools serve different purposes and can be used independently or together. Use VTEX Developer MCP when an assistant needs to search documentation, inspect API references, or retrieve information during a task. Use VTEX Skills when an assistant needs persistent context about recommended patterns, known constraints, and platform-specific implementation guidance. Using both tools provides access to reference material and reusable VTEX-specific context within the same workflow.

| Tool | Installation | Supported platforms |
|---|---|---|
| [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp) | `npx -y @vtex/developer-mcp` | Cursor, VS Code, Claude Code, Claude Desktop |
| [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills) | `npx skills add vtex/skills` | Cursor, Copilot, Claude, AGENTS.md, OpenCode, Kiro |


## VTEX Developer MCP

The `@vtex/developer-mcp` package is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that connects AI coding assistants to VTEX documentation ([Help Center](https://help.vtex.com/) and [Developer Portal](https://developers.vtex.com/)) and API specifications. It runs locally, requires no API key or authentication, and exposes four MCP tools:

- `search_documentation`: Finds relevant documentation based on a query.
- `fetch_document`: Retrieves the full content of a documentation article by URL.
- `search_endpoints`: Finds API endpoints based on a query.
- `get_endpoint_details`: Retrieves the full OpenAPI specification of an endpoint.

To use the server, add it to the MCP configuration of an AI assistant. The assistant then starts the server and calls its tools as needed during a task. VTEX Developer MCP works with Cursor, VS Code with GitHub Copilot, Claude Code, and Claude Desktop. For setup instructions per assistant, see [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp).

## VTEX Skills

VTEX Skills is a catalog of AI agent skills for VTEX platform development. A skill is a plain-text file that an AI agent loads as persistent context before generating code. VTEX Skills provides VTEX-specific implementation guidance that is not included in the agent's default context.

The skills cover implementation details that generic assistants don't reliably know, such as Overrides API behavior, Payment Provider Protocol (PPP) endpoints, BFF requirements, and Master Data limits. They are organized into tracks by development area (including FastStore, Payment, VTEX IO, Marketplace, and Headless) and maintained from a single source, then exported to the supported AI development platforms.

VTEX Skills supports several AI development tools. The recommended way to install is with npx, which detects the supported tools you have installed and places the skill files where each one expects them (in your project or in your environment, depending on the tool):

```sh
npx skills add vtex/skills
```

For installation options and the full catalog, see [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills).

## Next steps

- [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp): Set up the MCP server and explore available tools.
- [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills): Install AI skills and browse the track catalog.
- [Developer experience](https://developers.vtex.com/docs/guides/developer-experience): Learn about other VTEX developer tools and resources.
