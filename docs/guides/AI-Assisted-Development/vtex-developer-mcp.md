---
title: "VTEX Developer MCP"
slug: "vtex-developer-mcp"
hidden: false
createdAt: "2026-04-09T19:00:00.000Z"
updatedAt: "2026-04-09T19:00:00.000Z"
excerpt: "Connect your AI coding assistant to VTEX documentation and API references using the Model Context Protocol (MCP)."
seeAlso:
 - "/docs/guides/ai-assisted-development-overview"
 - "/docs/guides/vtex-skills"
hidePaginationPrevious: false
hidePaginationNext: false
---

[<i class="fa-brands fa-github"></i> Source code](https://www.npmjs.com/package/@vtex/developer-mcp)

`@vtex/developer-mcp` is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that enables AI coding assistants to access VTEX documentation and API references. It provides a standardized interface for retrieving documentation content and API specifications directly from development tools such as editors or AI assistants.

Once connected, your AI assistant can:

- Search VTEX documentation
- Retrieve full documentation articles
- Search API endpoints based on OpenAPI definitions
- Retrieve detailed endpoint specifications

These capabilities allow AI assistants to generate responses based on up-to-date VTEX content.

## Before you begin

Make sure you have the following:

- **Node.js 18 or later**: Run `node --version` to check your installed version.
- **An MCP-compatible AI development tool**, such as [Cursor](https://www.cursor.com/), [VS Code](https://code.visualstudio.com/) with GitHub Copilot, [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), or [Claude Desktop](https://claude.ai/download).

## Configuring the MCP server

Follow the instructions for your development environment.

### Cursor

Add the server to `.cursor/mcp.json` in your project root (or `~/.cursor/mcp.json` for a global config):

```json
{
  "mcpServers": {
    "vtex-developer": {
      "command": "npx",
      "args": ["-y", "@vtex/developer-mcp"]
    }
  }
}
```

### VS Code / GitHub Copilot

Add the server to `.vscode/mcp.json` in your project root:

> VS Code uses `"servers"` as the top-level key, not `"mcpServers"`.

```json
{
  "servers": {
    "vtex-developer": {
      "command": "npx",
      "args": ["-y", "@vtex/developer-mcp"],
      "type": "stdio"
    }
  }
}
```

### Claude Code

Run the following command in your terminal:

```bash
claude mcp add vtex-developer -- npx -y @vtex/developer-mcp
```

Or add a `.mcp.json` file at your project root:

```json
{
  "mcpServers": {
    "vtex-developer": {
      "command": "npx",
      "args": ["-y", "@vtex/developer-mcp"]
    }
  }
}
```

### Claude Desktop

1. Open Claude Desktop, then go to **Claude** menu → **Settings...** → **Developer** tab.
2. Click **Edit Config** to open `claude_desktop_config.json`.
3. Add the following configuration:

```json
{
  "mcpServers": {
    "vtex-developer": {
      "command": "npx",
      "args": ["-y", "@vtex/developer-mcp"]
    }
  }
}
```

4. Quit and reopen Claude Desktop.

## Available tools

Once connected, your AI assistant has access to four tools:

| Tool | Description | Key parameters |
|---|---|---|
| `search_documentation` | Searches VTEX Help Center and Developer Portal content (provides hybrid semantic and keyword search across VTEX Help Center and Developer Portal) | `query` (required), `locale` (en, es, pt — required), `limit` (1–50), `format` |
| `fetch_document` | Retrieves the full content of a VTEX documentation article by URL | `url` (required), `format` |
| `search_endpoints` | Searches VTEX API endpoints by query over OpenAPI definitions | `query` (required), `limit` (1–50), `method` (GET, POST, etc.), `format` |
| `get_endpoint_details` | Retrieves the full OpenAPI specification of a given endpoint | `endpoint_id` (required), `format` |

A few tips on how to combine them:

- Use `search_documentation` to find relevant articles, then `fetch_document` to get the full content.
- Use `search_endpoints` to find API endpoints, then `get_endpoint_details` for the complete OpenAPI specification.
- All tools support a `format` parameter (`markdown`, `json`, `yaml`, `toml`) — defaults to `markdown`.

## Usage examples

The following prompts illustrate how to use your AI assistant with the VTEX Developer MCP:

- "Search VTEX documentation for payment provider integration"
- "Fetch the full guide at <https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol>"
- "Find documentation about the Catalog API"
- "Search for API endpoints related to order placement"
- "Get the full specification for the Create Order endpoint"

## Troubleshooting

**Node.js not installed**
The server requires Node.js 18 or later. Check your version with `node --version`. If it's missing or outdated, install it from [nodejs.org](https://nodejs.org).

**`npx` not found**
`npx` ships with Node.js. Reinstall Node.js to get it back.

**Server not connecting**
Check that you have internet access. If you're behind a corporate firewall, make sure outbound HTTPS traffic is allowed.

**Server not appearing in your MCP client**
Restart your editor. Claude Desktop requires a full quit and reopen, not just a window close.

**VS Code: tools not appearing**
Make sure you're using `"servers"` (not `"mcpServers"`) as the top-level key in `.vscode/mcp.json`.


