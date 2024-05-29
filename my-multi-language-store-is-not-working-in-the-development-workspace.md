---
title: "My multi-language store is not working in the development workspace"
slug: "my-multi-language-store-is-not-working-in-the-development-workspace"
hidden: false
createdAt: "2024-05-29T15:45:35.508Z"
updatedAt: "2024-05-29T15:45:35.508Z"
excerpt: "After creating a development workspace in a multi-language store, there is an error"
tags:
    - store-framework
    - app-development
---

**Keywords:** development workspace, internationalization, messages, multi-language

After [creating a development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) in a multi-language store, the following error is returned when trying to access the website:

```
Error: messages
at throwOnGraphQLErrors (/usr/local/app/node_modules/@vtex/api/lib/HttpClient/GraphQLClient.js:10:15)
at /usr/local/app/node_modules/@vtex/api/lib/HttpClient/GraphQLClient.js:23:15
at runMicrotasks (<anonymous>)
at processTicksAndRejections (internal/process/task_queues.js:97:5)
at MessagesGraphQL.translate (/usr/local/app/node_modules/@vtex/api/lib/clients/apps/MessagesGraphQL.js:50:26)
at dataloader_1.default.batch (/usr/local/app/node_modules/@vtex/api/lib/service/worker/runtime/graphql/schema/messagesLoaderV2.js:69:15)
```

This error indicates issues with translations related either to the configuration settings of the `vtex.messages` app, which is used for [translating storefront content](https://developers.vtex.com/docs/guides/storefront-content-internationalization#step-by-step) or to the values assigned to the `Locale` field within the [trade policy](https://help.vtex.com/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4EPwTXx5oFdSG1dA3zIchz#trade-policy) configuration.

## Solution

To solve this problem, there are several solutions you can consider:

### Checking your store language availability

Make sure the desired language is available for your storefront. In some cases, despite being able to select a language in the Locale field within the trade policy configuration, the storefront may not have been translated into that language. In this case, you will receive that error message.

To check which language is set up for your storefront, do the following:

1. Access the trade policy configuration by going to the VTEX Admin and navigating to Store Settings > Channels > Trade Policies.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/locale-trade-policy-en.png)

Open a ticket with VTEX Support to check if the translation is available. If the language is unavailable, you may request the translation through our support in the same ticket.

If the language is available and the problem continues, check if the [Locale field](#check-the-locale-field)’s value is correct.

### Checking the Locale field

1. Access the trade policy configuration by going to the VTEX Admin and navigating to Store Settings > Channels > Trade Policies.
2. Make sure the Locale field’s value is correct. For example, consider a trade policy whose country code is Chile (CHL):

|✅ Do|❌ Don't|
| :-----: | :-------: |
| es-CL | arn-CL |

>⚠️ See Microsoft’s documentation to check the correct [Language Code Identifiers](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c) to set up in the Locale field.

If you are still experiencing the same issue, [disable the automatic translations](#disable-the-automatic-translations) in the `vtex.messages` app settings.
### Disabling automatic translations

If the desired language is available and correct, follow the steps below:

1. In the VTEX Admin, go to Apps > My Apps, and search for the `vtex.messages` app.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/search-messages-app-en.png)

2. Open the app settings and [disable the automatic translations](https://developers.vtex.com/docs/guides/vtex-io-documentation-disabling-automatic-translation).

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/development/vtex-messages-app-en.png)

The expected behavior is for the multi-language store website to work properly in the development workspace.

After following these steps, if you keep receiving the same error message, open a ticket to VTEX Support.
