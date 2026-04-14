---
title: "Connect the VTEX CX Platform MCP"
slug: "connect-the-vtex-cx-platform-mcp"
hidden: false
createdAt: "2026-04-14T13:05:20.961Z"
updatedAt: "2026-04-14T13:05:57.445Z"
excerpt: "Learn how to connect VTEX CX Platform Model Context Protocol (MCP) to an AI tool."
---

This guide explains how to use [VTEX CX Platform's Model Context Protocol (MCP)](https://modelcontextprotocol.io/) to access your data inside the platform. It provides a standardized and secure way to access your information.

Once connected, you can:

- Explore information about your store's customer support.
- Run interactions analyses without switching between dashboards.
- Create visualizations and insights about your store.

## Before you begin

Make sure you have the following:

- **An MCP-compatible AI development tool**, such as [Cursor](https://www.cursor.com/), [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), [Claude Desktop](https://claude.ai/download), or [ChatGPT](https://chatgpt.com/).

> ChatGPT can only be connected to the MCP where connector support is available.

- A valid [VTEX CX Platform account](https://dash.weni.ai/orgs) for the projects you want to analyze.
- An active VTEX CX Platform subscription for your organization.
- Access granted by your organization's administrator where applicable.

## Configuring the VTEX CX Platform MCP server

Follow the instructions for your development environment.

### Cursor

Add the server to `.cursor/mcp.json` in your project root (or `~/.cursor/mcp.json` for a global config):

```json
{
  "mcpServers": {
    "vtex-cx-platform": {
      "url": "https://mcp.weni.ai/mcp"
    }
  }
}
```

### Claude Code

Add a `.mcp.json` file at your project root:

```json
{
  "mcpServers": {
    "vtex-cx-platform": {
      "url": "https://mcp.weni.ai/mcp"
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
    "vtex-cx-platform": {
      "url": "https://mcp.weni.ai/mcp"
    }
  }
}
```

4. Quit and reopen Claude Desktop.

### ChatGPT




### Step 2 — Sign in and authorize

After you add the connector:

1. Complete the redirect to VTEX CX Platform.
2. Sign in with your account.
3. Authorize access to your data.

## Usage examples

The following prompts illustrate how to use your AI assistant with the VTEX CX Platform MCP:

- “How many conversations were resolved by the AI last month?”
- “What was the average CSAT last week?”
- “Which topics drove the most transfers to human support?”
