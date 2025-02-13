---
title: "I don't see my Store Theme changes"
slug: "i-dont-see-my-store-theme-changes"
excerpt: "After linking your Store Theme app, the changes are not reflected in the workspace."
hidden: false
createdAt: "2025-01-30T14:25:00.00Z"
updatedAt: "2025-01-30T14:25:00.00Z"
tags:
    - development
---

**Keywords:** Store Theme | Workspace | Cache

Once you [link your app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app), you should see all your changes live at `https://{workspace}--{accountName}.myvtex.com`. If the changes in your [Store Theme app](https://developers.vtex.com/docs/guides/vtex-io-documentation-store-theme) are not reflecting on your store workspace, check the following solutions to fix your scenario.

## Solution

### My workspace does not reflect changes in Typescript types

The [`vtex link` command](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-command-reference#link) does not automatically detect changes in [Typescript types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html). To address this issue, follow these steps:

1. Stop the link process with `vtex unlink`.
2. Update the Typescript types in your code.
3. Run `vtex link` to link the app again.

### My endpoint is returning outdated values

If your endpoint is returning outdated values, consider disabling caching temporarily by setting the `no-cache` option on your endpoint's response, as in the following example:

```typescript
ctx.set('Cache-Control', 'no-cache')
```

>⚠️ Please note that caching is enabled by default to enhance performance. Only use this option during development if a real-time response is necessary. Ensure not to disable caching for production stores by removing the `no-cache` option.

### There is a conflict between the installed and the linked store themes

To see your changes in action, the [version](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version#understanding-app-versioning) of the Store Theme you are working must be in the same major as the one from the Store Theme app installed on your account.

1. [Log in to your VTEX account](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage#logging-in-to-your-vtex-account).
2. [List the apps installed on your account](https://developers.vtex.com/docs/guides/vtex-io-documentation-listing-an-accounts-apps) by running `vtex ls`.
3. Check if the major of the Store Theme app installed is different from the one you are developing.
4. Check if there is another Store Theme app installed on your VTEX account. If positive, uninstall it.
