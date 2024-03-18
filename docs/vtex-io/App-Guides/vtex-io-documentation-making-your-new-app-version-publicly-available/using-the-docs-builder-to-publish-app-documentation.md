---
title: "Using the Docs builder to publish app documentation"
slug: "using-the-docs-builder-to-publish-app-documentation"
hidden: false
createdAt: "2023-04-26T16:05:00.000Z"
updatedAt: "2024-03-18T14:32:00.000Z"
excerpt: "Learn how to provide documentation for your users to follow in the VTEX Developer Portal"
category: "App Development"
seeAlso:
 - "/docs/guides/vtex-io-documentation-builders"
hidePaginationPrevious: false
hidePaginationNext: false
---

The `docs` builder is used to publicly publish an app's documentation on the [VTEX Developer Portal](https://developers.vtex.com/), allowing users to access relevant information about your app. Once the app is [published](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app), all Markdown content within the `docs` folder becomes available in the VTEX Developer Portal.

The content will be available in a URL of the following format:

```text
https://developers.vtex.com/docs/apps/{appvendor}.{appname}@{appversion}
```

Any app developer can make their documentation publicly available using the docs builder. So even if your app is not published to the VTEX App Store, you can take advantage of this convenience.

>❗When using the `docs` builder, ensure no sensitive or private information is shared in the files under the `/docs` folder.

## Folder structure

An app that uses the `docs` builder has a folder named `/docs` in its root directory. This folder serves as the repository for the application's documentation, where all documentation files are written in [Markdown](https://www.markdownguide.org/basic-syntax/) format (*.md files).

Following, you can find the basic app’s folder structure of an app using this builder:

```txt
docs
 ┣ 📄 README.md
```

The `README.md` is the main documentation file, where comprehensive information about the app is documented using Markdown syntax.

In addition to the README.md, developers can provide supplementary guides in separate Markdown files. For instance, an additional guide named `OptionalSteps.md` can be included to offer additional instructions or insights.

Each documentation file, including the README.md and any supplementary guides, can be accessed via unique URLs within the VTEX Developer Portal. For example, the `README.md` is accessible at `https://developers.vtex.com/docs/apps/{appvendor}.{appname}@{appversion}`, while supplementary guides like `OptionalSteps.md` can be accessed at `https://developers.vtex.com/docs/apps/{appvendor}.{appname}@{appversion}/OptionalSteps`.

## Usage

To begin using the `docs` builder in your app development, follow these steps.

1. Add the `docs` builder to your app’s builder list in the `manifest.json` file, as the following:

```json
"builders": {
  	  "docs": "0.x"
}
```

2. In the root directory of your app, create a `/docs` folder to manage your app’s documentation.
3. [Publish](https://developers.vtex.com/docs/guides/vtex-io-documentation-publishing-an-app) and [deploy](https://developers.vtex.com/docs/guides/vtex-io-documentation-deploying-the-app-stable-version) your new app version.
4. Once you publish your app, the documentation will be available in the VTEX Developer Portal.

>ℹ️ **Versioning**: Each app version will have its own documentation available at https://developers.vtex.com/docs/apps/{appvendor}.{appname}@{appversion}, while accessing https://developers.vtex.com/docs/apps/{appvendor}.{appname} will direct users to the latest version.

## Use case examples

The `docs` builder plays a crucial role in making an app’s documentation accessible. As a best practice, it is recommended that an app include at least the `README.md` file within the `/docs` folder.

As an example, check the [folder structure](https://github.com/vtex-apps/locale-switcher/tree/master/docs) of this builder in the Locale Switcher app and its [public documentation in the Developer Portal](https://developers.vtex.com/docs/apps/vtex.locale-switcher).

For further guidance on structuring your app's documentation, refer to [Documentation guidelines](https://developers.vtex.com/docs/guides/vtex-io-documentation-docs-guidelines).
