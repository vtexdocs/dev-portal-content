---
title: "VTEX Developer MCP and Skills"
slug: "2026-04-09-vtex-developer-mcp-and-skills"
type: "added"
createdAt: "2026-04-09T19:00:00.000Z"
updatedAt: "2026-04-09T19:00:00.000Z"
hidden: false
excerpt: "VTEX now offers two AI-assisted development tools: the VTEX Developer MCP for real-time documentation access and VTEX Skills for encoding platform-specific patterns into AI coding assistants."
---

## What has changed?

VTEX now offers two AI-assisted development tools for developers building on the platform:

- **[VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp)**: A Model Context Protocol (MCP) server that gives AI coding assistants direct access to VTEX documentation and API references. Run it with `npx -y @vtex/developer-mcp` — no API key or authentication required. Works with Cursor, VS Code (GitHub Copilot), Claude Code, and Claude Desktop.

- **[VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills)**: A catalog of 42 AI agent skills for VTEX platform development, covering six tracks (Architecture, FastStore, Payment, VTEX IO, Marketplace, and Headless). Install with `npx skills add vtex/skills`. Available for Cursor, GitHub Copilot, Claude, AGENTS.md, OpenCode, and Kiro.

## Why did we make this change?

AI coding assistants are increasingly central to developer workflows, but they lack VTEX-specific knowledge. The Developer MCP gives assistants real-time access to the latest documentation and API specs. Skills encode platform constraints, patterns, and best practices that prevent common mistakes. Together, they help developers build on VTEX faster and more correctly.

## What needs to be done?

No migration is required. These are new, additive tools. To get started:

- Set up the [VTEX Developer MCP](https://developers.vtex.com/docs/guides/vtex-developer-mcp) in your editor.
- Install [VTEX Skills](https://developers.vtex.com/docs/guides/vtex-skills) in your project.
- Read the [AI-Assisted Development overview](https://developers.vtex.com/docs/guides/ai-assisted-development-overview) to learn how the tools complement each other.
