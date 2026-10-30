---
title: "Schema versioning"
hidden: false
slug: "schema-versioning"
createdAt: "2026-09-21T12:00:00.000Z"
updatedAt: "2026-09-21T12:00:00.000Z"
excerpt: "Understand how CMS schema versions work, following semantic versioning with support for pre-release tags, so you can evolve your content structure safely."
---

Every time you upload a schema, the CMS registers it as a new version, following [semantic versioning](https://semver.org/) (`major.minor.patch`), the same convention used for npm packages. This lets you evolve your content structure over time while keeping a clear history of what changed and when.

## Stable and pre-release versions

| Version type | Example | Effect |
| :---- | :---- | :---- |
| **Stable version** | `1.2.0` | Syncs normally and powers the live storefront schema. |
| **Pre-release version** | `1.2.3-beta` | Syncs without affecting the live schema, letting you test a new structure safely before it goes live. |

Because a pre-release version doesn't touch the live schema, multiple developers can test different schema versions against real content in parallel, without conflicts or coordination overhead. This is the mechanism behind [development branches](https://developers.vtex.com/docs/guides/working-with-development-branches).

## Choosing a version number

When the CLI prompts you for a version, base your choice on the nature of the change:

| Change type | Version bump | Example |
| :---- | :---- | :---- |
| New optional field or component added | **Minor** | `1.5.0` → `1.6.0` |
| Bug fix or small correction | **Patch** | `1.5.0` → `1.5.1` |
| Breaking change (removed or renamed field) | **Major** | `1.5.0` → `2.0.0` |

> ⚠️ Always review your schema before confirming the upload. If you publish a new version without a pre-release tag (for example, `1.6.0` instead of `1.6.0-beta.1`), it replaces the current production schema immediately. To test changes without affecting production, append a pre-release tag such as `-beta` to the version.

## Related workflows

Versioning isn't a standalone step, it's built into the two workflows where you actually publish or test a schema:

- **Uploading a schema**: see [Local setup and development](https://developers.vtex.com/docs/guides/local-development-and-setup#step-2---syncing-the-schema) for the day-to-day sync workflow and version prompt.
- **Testing a schema in isolation**: see [Working with development branches](https://developers.vtex.com/docs/guides/working-with-development-branches) for how to pair a pre-release version with a development branch to test content against it.

## Next steps

<Flex>

<WhatsNextCard
  linkTo="https://developers.vtex.com/docs/guides/local-development-and-setup"
  title="Local setup and development"
  description="Learn the daily workflow for creating, syncing, and versioning component schemas."
  linkTitle="See more"
/>

<WhatsNextCard
  linkTo="https://developers.vtex.com/docs/guides/working-with-development-branches"
  title="Working with development branches"
  description="Test a pre-release schema version against real content, without affecting the live schema."
  linkTitle="See more"
/>

</Flex>
