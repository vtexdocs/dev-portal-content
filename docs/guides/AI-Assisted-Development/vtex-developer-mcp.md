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

`@vtex/developer-mcp` is a [Model Context Protocol](https://modelcontextprotocol.io) server that gives AI coding assistants direct access to VTEX documentation and API references. Your AI assistant can search documentation, retrieve full articles, and look up API endpoint specifications — all from within your editor. No API key or authentication required.

## Before you begin

Make sure you have the following:

- **Node.js 18 or later** — check your version with `node --version`
- **An MCP-compatible AI development tool** — Cursor, VS Code with GitHub Copilot, Claude Code, or Claude Desktop

## Platform setup

Choose your editor below and follow the setup steps.

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

Run this command in your terminal:

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

1. Quit and reopen Claude Desktop.

## Available tools

Once connected, your AI assistant has access to four tools:

| Tool | Description | Key parameters |
|---|---|---|
| `search_documentation` | Hybrid semantic + keyword search across VTEX Help Center and Developer Portal | `query` (required), `locale` (en, es, pt — required), `limit` (1–50), `format` |
| `fetch_document` | Retrieve the full content of a VTEX documentation article by URL | `url` (required), `format` |
| `search_endpoints` | Search VTEX API endpoints by query over OpenAPI definitions | `query` (required), `limit` (1–50), `method` (GET, POST, etc.), `format` |
| `get_endpoint_details` | Get the full OpenAPI specification for a specific endpoint | `endpoint_id` (required), `format` |

A few tips on how to combine them:

- Use `search_documentation` to find relevant articles, then `fetch_document` to get the full content.
- Use `search_endpoints` to find API endpoints, then `get_endpoint_details` for the complete OpenAPI specification.
- All tools support a `format` parameter (`markdown`, `json`, `yaml`, `toml`) — defaults to `markdown`.

## Usage examples

You can ask your AI assistant things like:

- "Search VTEX documentation for payment provider integration"
- "Fetch the full guide at <https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol>"
- "Find documentation about the catalog API"
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

---

For more details, see the [@vtex/developer-mcp](https://www.npmjs.com/package/@vtex/developer-mcp) npm package.
