---
title: "My multi-language store is not functioning in the development workspace"
slug: "multi-language-store-issue"
excerpt: "After creating a development workspace in a multi-language store, there is an error"
tags:
    - store-framework
    - app-development
---

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

This error indicates issues with translations related to either the configuration settings of the `vtex.messages` app, which is utilized for [translating storefront content](https://developers.vtex.com/docs/guides/storefront-content-internationalization#step-by-step), or with the values assigned to the `Locale` field within the [trade policy](https://help.vtex.com/tracks/vtex-store-overview--eSDNk26pdvemF3XKM0nK9/4EPwTXx5oFdSG1dA3zIchz#trade-policy) configuration.

## Solution

To solve this problem, there are several solutions you can consider:

### Checking your store language availability

Make sure the desired language is available for your storefront. In some cases, despite being able to select a language in the Locale field within the trade policy configuration, the storefront may not have been translated into that language. In this case, you will receive that error message.

To check which language is set up for your storefront, do the following:

Access the trade policy configuration by going to the VTEX Admin and navigate to Store Settings > Channels > Trade Policies.

Open a ticket to VTEX Support to check if the translation is available. If the language is unavailable, you may request the translation through our support in the same ticket.

If the language is available and the problem persists, check if the [Locale field](#checking-the-locale-field)’s value is correct.

### Checking the Locale field

Access the trade policy configuration by going to the VTEX Admin and navigate to Store Settings > Channels > Trade Policies.
Ensure the Locale field’s value is correct. As an example, consider a trade policy whose Country Code is Chile (CHL):

>⚠️ Refer to Microsoft’s documentation to check the correct [Language Code Identifiers](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c) to set up in the Locale field.

If you are still experiencing the same issue, [Disable the automatic translations](#disabling-the-automatic-translations) in the `vtex.messages` app settings.

### Disabling the automatic translations

Considering the desired language is available and correct, follow the steps below:

In the VTEX Admin, go to Apps > My Apps, and search for the `vtex.messages` app.

Open the app settings and [disable the automatic translations](https://developers.vtex.com/docs/guides/vtex-io-documentation-disabling-automatic-translation). 