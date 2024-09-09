---
title: "Documentation guidelines"
slug: "vtex-io-documentation-docs-guidelines"
hidden: false
createdAt: "2024-01-04T10:33:04.345Z"
---

Developing and publishing apps on the VTEX App Store requires meticulous documentation to ensure seamless adoption by developers and business users. Follow these best practices to create clear, engaging, and effective documentation for your VTEX apps.

## Identifying your audience

Clearly distinguish between developers and business users when developing documentation. Developers will focus on installation, setup, and other configuration options, while business users need a streamlined understanding of app functionalities and operations.

## Defining the documentation objectives

Envision what users should achieve after reading your documentation. Clearly outline the learning objectives, ensuring that users leave with a comprehensive understanding of your app's capabilities.

## Structuring your documentation

### Title

The title must be concise and memorable. Ensure that it describes the experiences the app represents.

#### Do’s

- Use the app's name as the article title.

- Clearly state the learning objective of the article, preferably with only one verb.

- Capitalize the first letter of each word.

| ✅ Do                  | ❌ Don't              |
|-------------------------|-----------------------|
| Availability Subscriber | Availability Subscribe|
| Search Bar              | Search bar            |

#### Don’ts

- Do not use punctuation, such as periods, commas, exclamation points, question marks, semicolons, colons, and underscores.

- Do not use the word _App_.

- Do not include the version number of the app.

| ✅ Do              | ❌ Don't                 |
|--------------------|---------------------------|
| Google Tag Manager | Google Tag Manager v3.5.2.|
| Live Shopping      | Live Shopping app         |

### Introduction

The introduction should summarize your app’s purpose and what the user will learn with the documentation.

- Write a short description of the app.
- Emphasize the end-user benefits.
- Add an image that illustrates the app behavior.
- Use [Callout](#callout) for important notes.

| ✅ Do | ❌ Don't |
|--------|----------|
| The `Availability Subscriber` component shows the availability subscriber form displayed when a product is unavailable. This component can be imported and used by any VTEX App. | The `Availability Subscriber` is a First-Party solution and can be imported and used by any VTEX App.|

### (Optional) Before you start

Before the app’s installation, the user may need to meet some prerequisites. For example, an account or permission in another platform, knowledge of specific web technology, or a development tool like the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

- Create bullets or checklists to describe the prerequisites.
- Use [Callout](#callout) if applicable.

| ✅ Do | ❌ Don't |
|--------|--------- |
| You need a Google account to use Google Tag Manager. You can use the same account if you already use Google products like Gmail. If you do not have an account for a Google product, create one at [Creating your Google account](https://support.google.com/accounts/answer/27441?hl=en). | You need a Google account to use Google Tag Manager.|

### Installation

Offer a step-by-step installation guide, utilizing code snippets to enhance user comprehension.

Refer to the _Installation_ section in the [Documentation template](#documentation-template) for an example.

### Configuration

After installation, guide users through configuring the app in their store's theme code or Admin settings. List all essential app settings with detailed step-by-step instructions.

Refer to the _Configuration_ section in the [Documentation template](#documentation-template) for an example.

### (Optional) Customization

If applicable, provide steps for customizing the app. For example, if your app uses CSS handles, provide the CSS handles related to the app and add a table with the available CSS handles. Make sure to add the documentation link for [the instructions to apply CSS customizations](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization).

### (Optional) Contributors

Follow the [All-Contributors specification](https://github.com/all-contributors/all-contributors) and recognize the people who contributed to your app.

### Callout

If you need to highlight information, use one of the following callout types:

#### Information

Highlights an aspect the user should pay attention to, giving additional information about the subject. However, the lack of awareness of that information will not lead to problems.

```md
> ℹ️ Information goes here.
```

#### Warning

Applies when the user must pay attention to information to avoid issues or unexpected behaviors. It shows a medium criticality level that leads to problems.

```md
> ⚠️ Warning message goes here.
```

#### Danger

Represents the highest criticality level. If the user ignores the information given, this might lead to critical issues, possibly breaking the feature.

```md
> ⛔ Danger message goes here.
```

## Documentation template

A basic documentation template structure with the previously described sections for you to start.

<details>
<summary><b>Documentation template</b></summary>

```md
# {Insert the app's name}

The `{insert app's name}` is responsible for `{app's purpose}` so you can `{job to be done}`.

![insert-an-image-preview](/)

## Before you begin

You need to have `{insert what the user needs to have: an account in another platform, CLI, knowledge in another app, etc}`.

If you do not have `{insert what the user needs to have and how it can be done}`.

## Installation

1. [Install](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-installing-an-app) the `{insert app's name}` app in the desired VTEX account by running `vtex install {appVendor}.{appName}` in your terminal.
2. Open your store’s Store Theme app directory in your code editor.
3. Open your app's `manifest.json file` and add the `{insert app's name}` app under the `peerDependencies` field.


      "peerDependencies": {
          "vtex.{appName}": "{appVersion}"
      }
      

4. Declare the `{insert app's name}` app in the desired template. For example:

      "store.home": {
          "blocks": [
      +     "{app-name}",
          ]
      },

*![insert-an-image-preview](/)*

## Configuration

Once you have installed the app, you can `{describe the app's configuration in the VTEX Admin, for example}`.

1. `first step`.
2. `Second step`.
3. `Third step`.

## Customization

To apply CSS customizations to this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles |
| ------------------ |
| csshandlesName |
| csshandlesName |
| csshandlesName |

## Contributors

Thanks go to these wonderful people:

- `{insert the GitHub username}`

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome.
```

</details>

## Related articles

- [App Store Guidelines](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-homologation-requirements-for-vtex-app-store)
- [Preparing your app for distribution](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-preparing-your-app-distribution)
