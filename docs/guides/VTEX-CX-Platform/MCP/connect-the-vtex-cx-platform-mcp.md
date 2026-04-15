---
title: "Connect the VTEX CX Platform MCP"
slug: "connect-the-vtex-cx-platform-mcp"
hidden: false
createdAt: "2026-04-14T13:05:20.961Z"
updatedAt: "2026-04-14T13:05:57.445Z"
excerpt: "Learn how to connect VTEX CX Platform Model Context Protocol (MCP) to an AI tool."
---

This guide shows how to connect the [VTEX CX Platform's Model Context Protocol (MCP)](https://modelcontextprotocol.io/) to an AI tool. 

MCP provides a standardized and secure way for AI assistants to access your **VTEX CX Platform** data. Once connected, your AI tool can query and analyze your customer support data directly.

Once connected, you can:

- Explore information about your store's customer support.
- Run interaction analyses without switching between dashboards.
- Create visualizations and insights about your store.

## Before you begin

Make sure you have the following:

- **An MCP-compatible AI development tool**, such as [Claude](https://claude.ai/), [Cursor](https://www.cursor.com/), or [ChatGPT](https://chatgpt.com/).

  > The MCP connection to ChatGPT is only available on paid plans.

- A valid [VTEX CX Platform account](https://dash.weni.ai/orgs) for the projects you want to analyze.
- An active VTEX CX Platform subscription for your organization.
- Access granted by your organization's administrator where applicable.

## Configuring the VTEX CX Platform MCP server

Follow the instructions for your development environment.

### Claude

1. Open Claude, then go to **Settings...** → **Connectors** tab.
2. Click `Add custom connector`.
3. Choose any name for the MCP.
4. Paste this URL in the **Remote MCP server URL** box: `https://mcp.weni.ai/mcp`.
5. Click `Add`.
6. In your connector's menu, look for the VTEX CX Platform MCP and click `Connect`.
7. Authorize access to your data by clicking `Allow access`.
8. Sign in with your VTEX CX Platform account.

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

After you add the connector, you will be redirected to VTEX CX Platform. To complete the configuration, follow the steps below:

1. Authorize access to your data by clicking `Allow access`.
2. Sign in with your VTEX CX Platform account.

### ChatGPT

1. Open ChatGPT, then go to **Settings...** → **Apps** tab.
2. Click `Create app`.
3. Choose a name for the MCP.
4. Paste this URL in the MCP server URL box: `https://mcp.weni.ai/mcp`.
5. Under **Authentication**, choose `OAuth`.
6. Accept the terms and conditions.
7. Click `Create`.

### Sign in and authorize

After you add the connector, you will be redirected to VTEX CX Platform.

To complete the configuration, follow the steps below:

1. Authorize access to your data by clicking `Allow access`.
2. Sign in with your VTEX CX Platform account.

## Usage examples

The following prompts illustrate how to use your AI assistant with the VTEX CX Platform MCP:

- “How many conversations were resolved by the AI last month?”
- “What was the average CSAT last week?”
- “Which topics drove the most transfers to human support?”

## Privacy policy and terms of use

If you want to know about how your data is being handled, you can read the [Terms of use](https://mcp.weni.ai/terms) and the [Privacy policy](https://mcp.weni.ai/privacy).
