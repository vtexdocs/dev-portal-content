---
title: "Using the Docs builder to publish app documentation"
slug: "using-the-docs-builder-to-publish-app-documentation"
hidden: false
createdAt: "2023-04-26T16:05:00.000Z"
updatedAt: "2023-04-26T16:05:00.000Z"
excerpt: "Learn how to provide documentation for your users to follow in the VTEX Developer Portal"
category: "App Development"
seeAlso:
 - "/docs/guides/vtex-io-documentation-builders"
hidePaginationPrevious: false
hidePaginationNext: false
---

## Using the Docs builder to publish app documentation

If you are publishing an app, you might want to be able to provide documentation for your users to follow. The Docs builder allows you to do that, right here in the VTEX Developer Portal.

In short, all Markdown content in the `/docs` folder of your app identified as `{appvendor}.{appname}@{appversion}` will be made available once the app is [published](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app), in a URL of the following format:

```text
https://developers.vtex.com/docs/apps/{appvendor}.{appname}@{appversion}
```

Any app developer can make their documentation publicly available using the docs builder. So even if your app is not published to the VTEX App Store, you can take advantage of this convenience.

> ⚠️ Keep in mind that access is not restricted to accounts/users that have the app installed. **Do not share any information that cannot be public to the web!**

## Step by step

1. Add the  `docs` to your app's builder list in the `manifest.json` file. [This is seen in the manifest.json of vtex.store-theme@5.x](https://github.com/vtex-apps/store-theme/tree/master/manifest.json#L9). For example:

    ```json
    "builders": {
      "docs": "0.x"
    },
    ```

2. In the root directory of your app, create a `docs` folder to manage your app's documentation. It should be written in [Markdown](https://www.markdownguide.org/basic-syntax/), on a file named `README.md`. [This is the docs folder of vtex.store-theme@5.x](https://github.com/vtex-apps/store-theme/tree/master/docs).

3. Once you publish your app, the documentation will be available in the VTEX Developer Portal. [This is the published documentation for vtex.store-theme@5.x](https://developers.vtex.com/docs/apps/vtex.store-theme@5.x).
