---
title: "VTEX Developer MCP"
slug: "vtex-developer-mcp"
hidden: false
createdAt: "2026-04-09T19:00:00.000Z"
updatedAt: "2026-06-09T19:00:00.000Z"
excerpt: "Connect your AI coding assistant to VTEX documentation and API references using the Model Context Protocol (MCP)."
seeAlso:
 - "/docs/guides/vtex-ai-developer-toolkit-overview"
 - "/docs/guides/vtex-skills"
hidePaginationPrevious: false
hidePaginationNext: false
---

VTEX Developer MCP is a [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server, available as part of the [VTEX AI Developer Toolkit](https://developers.vtex.com/docs/guides/vtex-ai-developer-toolkit-overview). It connects AI coding assistants to VTEX documentation ([Help Center](https://help.vtex.com/) and [Developer Portal](https://developers.vtex.com/)) and the [API Reference](https://developers.vtex.com/docs/api-reference), allowing assistants to retrieve documentation content and API specifications directly from VTEX sources during a task.

> The [VTEX AI Developer Toolkit](https://developers.vtex.com/docs/guides/vtex-ai-developer-toolkit-overview) also includes [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills). VTEX Skills and VTEX Developer MCP are complementary: VTEX Developer MCP retrieves documentation and API references at runtime, while VTEX Skills loads persistent platform context before a task starts.

## Available tools

The VTEX Developer MCP exposes four tools:

| Tool | Description | Parameters |
|---|---|---|
| `search_documentation` | Hybrid semantic and keyword search across VTEX Help Center and Developer Portal content | `query` (required), `locale` (required: `en`, `es`, `pt`), `limit` (default 10, max 50), `format` |
| `fetch_document` | Retrieves the full content of a VTEX documentation article by URL | `url` (required), `format` |
| `search_endpoints` | Hybrid semantic and keyword search over VTEX API endpoints in OpenAPI definitions | `query` (required), `limit` (default 10, max 50), `method` (`GET`, `POST`, etc.), `format` |
| `get_endpoint_details` | Retrieves the full OpenAPI specification of a given endpoint | `endpoint_id` (required), `format` |

All tools accept a `format` parameter (`markdown`, `json`, `yaml`, `toml`), which defaults to `markdown`. Common workflows include:

- Use `search_documentation` to find relevant articles, then `fetch_document` to get the full content.
- Use `search_endpoints` to find API endpoints, then `get_endpoint_details` with the returned `endpoint_id` for the complete OpenAPI specification.

## Usage examples

The following prompts illustrate how to use an AI assistant with the VTEX Developer MCP:

```text
Search VTEX documentation for payment provider integration.
```

```text
Fetch the full guide at https://developers.vtex.com/docs/guides/payments-integration-payment-provider-protocol.
```

```text
Find documentation about the Catalog API.
```

```text
Search for API endpoints related to order placement.
```

```text
Get the full specification for the Create Order endpoint.
```

## Configuration

Configure the MCP server in the AI development tool you use.

### Before you begin

Make sure you have the following:

- **Node.js 18 or later**: Run `node --version` to check your installed version.
- **An MCP-compatible AI development tool**, such as [Cursor](https://www.cursor.com/), [VS Code](https://code.visualstudio.com/) with GitHub Copilot, [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), or [Claude Desktop](https://claude.ai/download).

### Cursor

Add the server to `.cursor/mcp.json` in your project root, or to `~/.cursor/mcp.json` for a global configuration:

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

> VS Code uses `"servers"` as the top-level key, not `"mcpServers"`.

### Claude Code

Run the following command in your terminal:

```bash
claude mcp add vtex-developer -- npx -y @vtex/developer-mcp
```

Alternatively, add a `.mcp.json` file at your project root:

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

### Troubleshooting

#### Node.js not installed

The server requires Node.js 18 or later. Check your version with `node --version`. If it's missing or outdated, install it from [nodejs.org](https://nodejs.org).

#### `npx` not found

`npx` ships with Node.js. Reinstall Node.js to restore it.

#### Server not connecting

Check that you have internet access. If you're behind a corporate firewall, make sure outbound HTTPS traffic is allowed.

#### Server not appearing in your MCP client

Restart your editor. Claude Desktop requires a full quit and reopen, not just a window close.

#### VS Code: tools not appearing

Make sure you're using `"servers"` (not `"mcpServers"`) as the top-level key in `.vscode/mcp.json`.

