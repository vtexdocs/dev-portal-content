---
title: "Contributing"
slug: "contributing"
hidden: false
createdAt: "2021-03-18T22:45:55.338Z"
updatedAt: "2021-03-24T18:19:35.480Z"
---

VTEX IO is an open-source project. Contributions of all kinds are welcome, including feature requests, bug reports, and updates to our codebase and documentation.

# Codebase

VTEX IO native apps are fully stored in the [VTEX Apps Organization](https://github.com/vtex-apps) on <span class="fa fa-github"></span> GitHub.

That means you can contribute to our codebase by looking for the desired app on the VTEX Apps Organization and then [opening an issue](#opening-an-issue) or [creating a Pull Request.](#creating-a-pull-request)

> ℹ️ When looking for an app on the VTEX Apps Organization, keep in mind that the name of VTEX IO apps are [kebab case.](https://en.wiktionary.org/wiki/kebab_case) That means they are comprised of lowercase letters separated by hyphens. Therefore, if, for example, you want to contribute to the Product Summary app you must look for [`product-summary`](https://github.com/vtex-apps/product-summary) on the VTEX Apps Organization.

## Opening an issue

There are three main situations you should opt for opening an issue:

- Report a bug you can’t solve by yourself.
- Request a new feature or suggest an idea.
- Ask questions you had during development.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/vtex-io/Hello/112347367-8db6ec00-8ca5-11eb-997f-39b179b855d2_26.png)

Once you open an issue, our team will evaluate your contribution as soon as possible.

### Filtering issues

We use GitHub tags to classify issues between **Questions, Bugs or Enhancements.** This way, you can filter issues by specifying a label and author.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/vtex-io/Hello/60682041-0a69bd00-9e68-11e9-8ee2-f388ddf225a8_34.png)

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/vtex-io/Hello/60682095-5d437480-9e68-11e9-9933-5651efa063a4_36.png)

You can also change the **sort criteria** for the issues. For example, you can look for the most and least commented issues, the ones with most 👍 and most recently updated.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/vtex-io/Hello/60682317-39ccf980-9e69-11e9-9b4e-95c51753bee0_40.png)

## Creating a Pull Request

We recommend creating a Pull Request for trivial fixes or if you have already started working on a specific solution.

To create a Pull Request, take the following steps:

1. [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) the desired repository and create a local clone of it.
2. [Create a branch](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-and-deleting-branches-within-your-repository) from `master`, respecting the following name pattern: `<type>/<description>`, where `description` must provide a brief description of what is being developed and `type` must be one of the following:

- `feature` - new feature or behavior.
- `fix` - bug fix.
- `update` - dependecy update.
- `chore` - technical adjustments.

```sh
git checkout master
git checkout -b feature/nice-new-thing
```

3. Commit changes to your new branch.

```sh
git commit -m "Add nice new thing"
```

4. Test your changes.
5. [Create a Pull Request.](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) Make sure to include screenshots and a comprehensive description of the changes performed.

Once you open a Pull Request, our team will evaluate your contribution as soon as possible.

# Documentation

There are three main ways to contribute to VTEX IO documentation:

- [Giving feedback](#giving-feedback) - start a discussion regarding a specific document and leave quick suggestions.
- [Creating a Pull Request](#creating-a-pull-request-1) - work directly on a solution for improving a specific document and create a Pull Request.
- [Writing new documentation](#writing-new-documentation) - keep up with our best practices and write the documentation of your custom app.

## Giving feedback

Fill out our [📣 Feedback form](https://docs.google.com/forms/d/e/1FAIpQLSfmnotPvPjw-SjiE7lt2Nt3RQgNUe10ixXZmuO2v9enOJReoQ/viewform?entry.1972292648=developers.vtex.com&entry.1799503232=) and leave your suggestions on how we can improve a specific document.

Responses to the form are automatically added to our internal backlog and assigned to the team concerned. If you ask for a follow-up, we will let you know once we have addressed your feedback.

## Creating a Pull Request

All guides, references, and tutorials from the [VTEX IO Developer Documentation](link) is fetched from the [`io-documentation`](https://github.com/vtex-apps/io-documentation) repository.

In its turn, the documentation of VTEX IO apps are fetched directly from its corresponding GitHub repository.

> ⚠️ App documentation is fetched only from apps using the Docs builder.

Therefore, you can create a Pull Request with your fixes directly on the [`io-documentation`](https://github.com/vtex-apps/io-documentation) repository or on the repository of the corresponding app you want to contribute (e.g., [`product-summary`](https://github.com/vtex-apps/product-summary))

## Writing new documentation

To make the documentation of your custom app public on the Developer Portal, you must take the following steps:

1. Create a `docs/` folder in the app’s root.
2. Update the app's `manifest.json` file to declare `vtex.docs` as one of the app's builders.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/vtex-io/Hello/64052096-a99eee00-cb53-11e9-8d69-925a451231ab_103.png)

3. Inside the `docs/` folder create a `README.md` file.

   > ℹ️ When writing the documentation of your app, make sure to follow our [documentation templates.](#documentation-templates)

4. Contact us to make your documentation visible.

> ℹ️ In order to not have to keep track of two `README.md` files (one in the project’s root and another it the `docs/` folder), you can delete the former and only keep the latter. GitHub will read the one from the `docs/` folder and render it on the landing page.

### Documentation templates

#### React app README template

[React app template](https://github.com/vtex-apps/react-app-template)

```markdown
📢 Use this project, [contribute](https://github.com/{OrganizationName}/{AppName}) to it or open issues to help evolve it using [Store Discussion](https://github.com/vtex-apps/store-discussion).

# APP NAME

<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

Under the app's name, you should explain the topic, giving a **brief description** of its **functionality** in a store when installed.

Next, **add media** (either an image of a GIF) with the rendered components, so that users can better understand how the app works in practice. 

![Media Placeholder](https://user-images.githubusercontent.com/52087100/71204177-42ca4f80-227e-11ea-89e6-e92e65370c69.png)

## Configuration 

In this section, you first must **add the primary instructions** that will allow users to use the app's blocks in their store, such as:

1. Adding the app as a theme dependency in the `manifest.json` file;
2. Declaring the app's main block in a given theme template or inside another block from the theme.

Remember to add a table with all blocks exported by the app and their descriptions. You can verify an example of it on the [Search Result documentation](https://vtex.io/docs/components/all/vtex.search-result@3.56.1/). 

Next, add the **props table** containing your block's props. 

If the app exports more than one block, create several tables - one for each block. For example:

### `block-1` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `XXXXX`      | `XXXXXX`       | XXXXXXXX         | `XXXXXX`        |


### `block-2` props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `XXXXX`      | `XXXXXX`       | XXXXXXXX         | `XXXXXX`        |

Prop types are: 

- `string` 
- `enum` 
- `number` 
- `boolean` 
- `object` 
- `array` 

When documenting a prop whose type is `object` or `array` another prop table will be needed. You can create it following the example below:

- `propName` object:

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `XXXXX`      | `XXXXXX`       | XXXXXXXX         | `XXXXXX`        |


Remember to also use this Configuration section to  **showcase any necessary disclaimer** related to the app and its blocks, such as the different behavior it may display during its configuration. 

## Modus Operandi *(not mandatory)*

There are scenarios in which an app can behave differently in a store, according to how it was added to the catalog, for example. It's crucial to go through these **behavioral changes** in this section, allowing users to fully understand the **practical application** of the app in their store.

If you feel compelled to give further details about the app, such as it's **relationship with the VTEX admin**, don't hesitate to use this section. 

## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

`In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).`

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles |
| ----------- | 
| `XXXXX` | 
| `XXXXX` | 
| `XXXXX` | 
| `XXXXX` | 
| `XXXXX` |


If there are none, add the following sentence instead:

`No CSS Handles are available yet for the app customization.`

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->

---- 

Check out some documentation models that are already live: 
- [Breadcrumb](https://github.com/vtex-apps/breadcrumb)
- [Image](https://vtex.io/docs/components/general/vtex.store-components/image)
- [Condition Layout](https://vtex.io/docs/components/all/vtex.condition-layout@1.1.6/)
- [Add To Cart Button](https://vtex.io/docs/components/content-blocks/vtex.add-to-cart-button@0.9.0/)
- [Store Form](https://vtex.io/docs/components/all/vtex.store-form@0.3.4/)
```

#### Pixel app README template

[Pixel app template](https://github.com/vtex-apps/pixel-app-template)

```markdown
📢 Use this project, [contribute](https://github.com/vtex-apps/CHANGEME) to it or open issues to help evolve it using [Store Discussion](https://github.com/vtex-apps/store-discussion).

# APP NAME

<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

Under the app's name, you should explain the topic, giving a **brief description** of the **app's functionality** (what is it for?) in a store.

Next, you can **add media** (either an image of a GIF) if possible, so that users can better understand how the app works in practice. 

![Media Placeholder](https://user-images.githubusercontent.com/52087100/71204177-42ca4f80-227e-11ea-89e6-e92e65370c69.png)

## Configuration

It is possible to install in your store either by using App Store or the VTEX IO Toolbelt.

### Using VTEX App Store

1. Access the **Apps** section in your account's admin page and look for the Icommkt box;
2. Then, click on the **Install** button;
3. You'll see a warning message about needing to enter the necessary configurations. Scroll down and type in your **NAME OF A SETTINGS FIELD** in the `NAME OF THE APP` field.
4. Click on **Save**.

### Using VTEX IO Toolbelt

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the `vtex.icommkt@0.x` app. You can confirm that the app has now been installed by running `vtex ls` again. 
2. Access the **Apps** section in your account's admin page and look for the NAME OF THE APP box. Once you find it, click on the box.
3. Fill in the `NAME OF THE APP` field with your **NAME OF THE SETTINGS FIELD**.
4. Click on **Save**.

<!-- Remember to also **showcase any necessary disclaimer** related to the app in this section, such as the different behavior it may display during its configuration. -->

## Modus Operandi *(not mandatory)*

There are scenarios in which an app can behave differently in a store, according to its configuration. It's crucial then to go through these **behavioral changes** in this section, allowing users to fully understand the **practical application** of the app in their store.

If you feel compelled to give further details, such as the app's **relationship with others**, don't hesitate to use this section. 

<!-- DOCS-IGNORE:start -->
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!
<!-- DOCS-IGNORE:end -->
```
