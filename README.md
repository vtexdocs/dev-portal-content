# Dev-portal-content

Welcome to the [VTEX Developer Portal](https://developers.vtex.com) content repository! Here you will find the files for all guides included in that documentation portal. It is managed by the [Tech Writing team at VTEX](https://github.com/vtexdocs/dev-portal-content/graphs/contributors), with lots of love, sweat and PRs.

We're so glad you're here! It means you care about sharing knowledge through documentation ❤️ 📝. So come along, get comfy and learn how to [contribute with documentation](#contributing-with-developer-portal-documentation), [manage content](#managing-content) and [fix errors](#fixing-errors) in this repository.

## Why have we changed platforms from Readme to our custom built Developer Portal?

- Faster navigation
- More control over the search
- Create an interface completely controlled by us
- Managing content in Github
- High efficiency: we saved a considerable amount of our monthly budget.

## Developer Portal repositories

We have created a new organization in Github to host our documentation: [vtexdocs](https://github.com/vtexdocs).

You can find all repositories included in it, [here](https://github.com/vtex/education-tools).

They each serve a different purpose, and will be mentioned in the FAQ below, depending on which action you wish to perform.

### In this repository

You will find the following folders in this repository:

- **.github**: stores workflows configured for this repository.
- **docs**: where the markdown files of all our docs are stored. They are categorized into:
  - **guides**: all API guides.
  - **release-notes**: release notes included in our [changelog](https://developers.vtex.com/updates/release-notes).
  - **vtex-io**: all VTEX IO guides.
- **docs-utils**: scripts used to import documentation from Readme.
- **images**: stores images imported from Readme.
- **readme-api-md**: stores API Reference's markdown imported from Readme/
- **.gitignore**: stores files that should be ignored by Github.

## Contributing with Developer Portal documentation

We're so glad you're here! Thanks for being interested.

### How can I add new articles or release notes?

1. Open a branch in the [dev-portal-content](https://github.com/vtexdocs/dev-portal-content) repository.
2. Add a new file in the [desired folder](#in-this-repository), following our [template](https://github.com/vtexdocs/dev-portal-content/blob/main/docs/guide_template.md).
3. Add your content in markdown.
4. Add images in the chosen guide’s folder, if you wish.
5. To determine the left navigation's order, follow [these](#what-determines-the-left-navigations-order-and-organization) instructions.
6. Submit your PR for review.

*The `/developer-portal-content` repository just stores our documentation, it is not automatically synched to be rendered in the Dev Portal - yet. For now, when a new content is added to it, it is just included in the desired folder. For it to appear in the Developer Portal, our Tech Writing team leaders must run the portal's build.*

>⚠️ Note that we have a limitation of PRs by hour, so we have to accumulate the day's PRs to be all approved and merged by our Tech Writing team leaders. This means that if you want a content to be published, submit your PR for review with at least 2 days in advance from the desired publication date!

### How can I make sure my content will be visible and rendered correctly?

- Make sure you have a unique slug.
- Make sure your slug is the exact copy of your title.
- Images must be saved in the repository. To add it to your markdown, mention its path in the desired place of your guide's body.
- Ask team leaders to run the portal's build.

### How can I deal with page slugs?

The slugs used previously in our old Dev Portal were mostly maintained. You shouldn't have to worry about previous slugs.  

For new content, an article's title will become the page's slug always. **Do not create a slug that is different than the title, the portal will not interpret it otherwise.**

> For the content to be rendered properly, it is mandatory that slugs are unique, so no article should have a repeated title.

In the articles file, we included the header below. Add in the slug column the exact title, between dashes.

### What determines the left navigation's order and organization?

The `/developer-portal-content` repository just stores our documentation, it is not automatically synched to be rendered in the Dev Portal - yet. For now, when a new content is added to it, it is just included in the desired folder. For it to appear in the Developer Portal in the order that you choose for the left navigation, other PRs must be made.

The portal's navigation comes from the navigation [file](https://github.com/vtexdocs/devportal/blob/main/public/navigation.json). It is a json object listing the navigation and hierarchy of all contents in Developer Portal.

The excerpt below represents the first articles of the API Guides section, for instance.

```jsx
{
        "documentation": "API Guides",
        "slugPrefix": "docs/guides/",
        "categories": [
        {
            "name": "Getting Started",
            "slug": "getting-started-category",
            "origin": "",
            "type": "category",
            "children": [
            {
                "name": "Introduction",
                "slug": "getting-started",
                "origin": "",
                "type": "markdown",
                "children": [
                {
                    "name": "Platform overview",
                    "slug": "getting-started-platform-overview",
                    "origin": "",
                    "type": "markdown",
                    "children": []
                },
                {
                    "name": "List of REST APIs",
                    "slug": "getting-started-list-of-rest-apis",
                    "origin": "",
                    "type": "markdown",
                    "children": []
                },
                {
                    "name": "Authentication",
                    "slug": "getting-started-authentication",
                    "origin": "",
                    "type": "markdown",
                    "children": []
                },
                {
                    "name": "Making your first request",
                    "slug": "getting-started-making-your-first-request",
                    "origin": "",
                    "type": "markdown",
                    "children": []
                }
                ]
            },
            {
                "name": "Catalog",
                "slug": "catalog-overview",
                "origin": "",
                "type": "markdown",
                "children": []
            },
            {
                "name": "Orders",
                "slug": "orders-overview",
                "origin": "",
                "type": "markdown",
                "children": []
            },
            {
                "name": "Checkout",
                "slug": "checkout-overview",
                "origin": "",
                "type": "markdown",
                "children": []
            },
            {
                "name": "Payments",
                "slug": "payments-overview",
                "origin": "",
                "type": "markdown",
                "children": []
            },
            {
                "name": "Search",
                "slug": "search-overview",
                "origin": "",
                "type": "markdown",
                "children": []
            },
            {
                "name": "Promotions",
                "slug": "promotions-overview",
                "origin": "",
                "type": "markdown",
                "children": []
            },
            {
                "name": "Pricing",
                "slug": "pricing-overview",
                "origin": "",
                "type": "markdown",
                "children": []
            },
            {
                "name": "Account management",
                "slug": "account-management",
                "origin": "",
                "type": "markdown",
                "children": [
                {
                    "name": "Checking which user is currently authenticated",
                    "slug": "checking-which-user-is-currently-authenticated",
                    "origin": "",
                    "type": "markdown",
                    "children": []
                }
                ]
            }
            ]
        },
```

To add the created content in the left navigation:

1. Open a branch in the [/devportal](https://github.com/vtexdocs/devportal) repository.

    > ⚠️ **Before you start adding commits, read the repository's [readme](http://readme.md) file!** Commits must be done in a certain format for your PR to be approved.

2. In the [navigation.json](https://github.com/vtexdocs/devportal/blob/main/public/navigation.json) file, locate where you want the new content to appear. (Yes, it is a long document, be patient!)
3. Copy the structure below, and replace the values for your desired content.

```jsx
{
                    "name": "Checking which user is currently authenticated",
                    "slug": "checking-which-user-is-currently-authenticated",
                    "origin": "",
                    "type": "markdown",
                    "children": []
}
```

4. Paste the object in the desired spot.
5. Open a PR.

> By opening a PR, a bot will present a preview for you to test the navigation. With each commit, the preview will be updated.

6. Test your navigation through the preview.
7. Send the PR in #dev-portal-pr channel for approval.

### How can I add different colored callouts?

You can use the following syntax for adding callouts, but prefer the simpler markdown version:

```jsx
[block:callout]
{
    "type": "info",
    "body": "Check the new [Payments onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/payments-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Payments and is organized by focusing on the developer's journey.",
    "title": "Onboarding guide"
}
[/block]
```

```jsx
[block:callout]
{
    "type": "warning",
    "body": "Check the new [Payments onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/payments-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Payments and is organized by focusing on the developer's journey.",
    "title": "Onboarding guide"
}
[/block]
```

```jsx
[block:callout]
{
    "type": "danger",
    "body": "Check the new [Payments onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/payments-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Payments and is organized by focusing on the developer's journey.",
    "title": "Onboarding guide"
}
[/block]
```

```jsx
>ℹ️ Information type callout
```

```jsx
>⚠️ Warning type callout
```

```jsx
>❗ Danger type callout
```

### How can I add/fix images in an article?

1. Access the [dev-portal-content/docs/guides](https://github.com/vtexdocs/dev-portal-content/tree/main/docs/guides) folder.
2. Upload the images you wish to include in your guide in the same folder your article is located.
3. Access the file in Github web.
4. Open the raw version of the uploaded file by opening the image in a new tab.
5. Save the URL.
6. Mention the URL in your markdown.

### How can I hide articles from search engines?

When you publish an article in Developer Portal and wish that only those with the link can access it, you can hide it from search engines. This is useful for products in Beta that need documentation for specific clients, instead of publicly available docs, for example.

To do so, when creating the article fill in the header with the value `hidden: true`. You can keep the article out of the navigation bar by not making any changes in `navigation.json`.

```jsx
---
title: "Orders v2"
slug: "orders-getting-started"
hidden: true
createdAt: "2022-09-27T20:34:46.354Z"
updatedAt: "2022-10-04T14:36:08.692Z"
---
```

>️ Be aware that this will hide your article not only in Developer Portal searches, but also in other sites, like Google.

## Managing content

### How can I create a redirect?

Open a PR in this [repository](https://github.com/vtexdocs/devportal/blob/07519dab0c357cb107342cf21bc86ae107cce603/next.config.js#L36).

Netlify will generate a preview link for you to test the redirect.

Follow this format in your PR:

```jsx
{
        source: '/vtex-rest-api/docs/:slug',
        destination: '/docs/guides/:slug',
        permanent: true,
},
```

### API Reference: what about the /openapi-schemas repository?

All API Reference is still documented and managed through our usual repository. Nothing's changed here. There is a 5 minute cache between PRs in the `/openapi-schemas` repository and the Dev Portal, but it should be rendered automatically.

### How can I update docs from IO apps that already have a readme file in the app's repository?

All docs should be included in the /dev-portal-content repository. If the readme is not yet included, create a new file, and copy and paste the text.

## Fixing errors

### How to fix the error type `Error: There are incorrectly formatted code blocks in this file` in #dev-portal-logs?

This error means that there is a <code>`</code> loose somewhere in the document. The system reads it as an inline code block.

### How can I fix the error type in #dev-portal-logs?

This error should already be fixed. Check the log's age to see if it is still valid.

### 404 erros

**What causes 404 errors?**

- Broken callouts
- Broken images
- Missing closing tags in HTML
- Links mentioned in other articles containing previous Dev Portal slugs, or mentions to headings
- Redirects not made from older URLs
- Content does not exist in /dev-portal-content, only on Readme

**404 automatic checker in files**
We have embedded a Github action called [check-links.yml](https://github.com/vtexdocs/dev-portal-content/blob/main/.github/workflows/check-links.yml) to review all URLs mentioned in a file, and checking if they return 404 errors. If there's a link experiencing the 404 error in your file, you must fix it so the branch can be merged.

To identify the broken link:
The broken link will appear in red in your code editor tool (VSCode), and you can learn more about it by clicking on `Details`.
