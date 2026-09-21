---
title: "Translations by locale"
hidden: false
slug: "translations-by-locale"
createdAt: "2026-09-21T12:00:00.000Z"
updatedAt: "2026-09-21T12:00:00.000Z"
excerpt: "The CMS localizes content per locale with automatic fallback, so shoppers always see relevant content even when a translation is missing. See where this is documented."
---

The CMS supports multiple locales, such as `en-US`, `pt-BR`, and `es-MX`, for the content you model as a developer. When a field isn't translated for a given locale, the CMS automatically falls back to a more general or default locale, so shoppers always see relevant content instead of a blank field.

> ⚠️ Right-to-left (RTL) languages, such as Arabic or Hebrew, aren't supported yet. Keep this in mind if you're evaluating the CMS for a market that requires RTL layouts.

Locale configuration and translation management happen in the VTEX Admin and are documented in the Help Center, which is the source of truth for this workflow:

| Topic | Help Center resource |
| :---- | :---- |
| Editing and translating content per locale, and how fallback applies to a field | [Localizing content overview](https://help.vtex.com/docs/tutorials/localizing-content) |
| Setting up locales and the default locale for a store | [Configuring locales](https://help.vtex.com/en/docs/tutorials/configuring-locales) |
| Choosing a fallback strategy (default-locale fallback vs. core-language fallback) | [Understanding locale fallback rules](https://help.vtex.com/en/docs/tutorials/understanding-locale-fallback-rules) |

## Next steps

<Flex>

<WhatsNextCard
  linkTo="https://developers.vtex.com/docs/guides/creating-and-publishing-content"
  title="Creating and publishing content"
  description="Find the Help Center resources for creating, previewing, and publishing content in branches."
  linkTitle="See more"
/>

<WhatsNextCard
  linkTo="https://developers.vtex.com/docs/guides/understanding-cms-architecture-and-schema-declarations"
  title="Understanding CMS architecture and schema declarations"
  description="Deep dive into CQRS architecture, schema declarations, and folder structure."
  linkTitle="See more"
/>

</Flex>
