---
title: "Working with development branches"
hidden: false
slug: "working-with-development-branches"
createdAt: "2026-08-06T12:50:00.813Z"
updatedAt: "2026-08-06T12:50:00.813Z"
excerpt: "Learn how to create and use a development branch to test schema changes in isolation, without affecting your account's live content or merge and publish workflow."
---

In this guide, you'll learn how to create and use a development branch to test [schema](https://developers.vtex.com/docs/guides/content-plugin) changes without affecting your account's live content or merge and publish workflow.

A development branch is a temporary CMS branch used for testing. Unlike a regular branch, it's tied to its own schema version, so any content you create inside it uses that version instead of the one currently live in `main`. Because each branch carries its own schema version, multiple developers can test in parallel without interfering with each other or with the live schema.

You point the branch to a new or updated schema, create test content against it, and see exactly how that schema behaves, without touching production content or the live schema.

```mermaid
flowchart LR
A["Update schema"] --> B["Sync version"]
B --> C["Create development branch"]
C --> D["Test content in branch"]
D --> E["Preview and validate"]

C . "isolated from" .> F

subgraph MAIN["main"]
F["Live schema + published content"]
end
```

## Before you begin

To work with a development branch, you need to have [VTEX CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) and [Content plugin](https://developers.vtex.com/docs/guides/content-plugin) (`@vtex/cli-plugin-content`) installed and be logged in to your account. Also, your [user role](https://help.vtex.com/docs/tutorials/creating-roles) must have the following associated with it:

| Product | Resource | Permission |
| :--------------- | :------- | :---------------- |
| Commerce Content | Branch | Manage Dev Branch |

## Instructions

### Step 1 - Sync your schema version

1. Open your project in a code editor and make your schema changes.

2. Open a terminal and log in to your VTEX account by running `vtex login {accountName}`.

   > ⚠️ Replace `{accountName}` with your store account, for example, `vtex login mystore`.

3. Generate your schema file by running:

   ```bash
   vtex content generate-schema --out cms_schema.json
   ```

4. Upload the schema by running:

    ```bash
    vtex content upload-schema ./cms_schema.json
    ```

5. When the CLI asks which version to associate with the schema, type the full version you want to publish, using a `beta` pre-release tag to avoid affecting the current live schema, for example, `1.7.0-beta.0`.

### Step 2 - Create your development branch

1. Open the VTEX Admin and go to **Storefront > Content > Branches**.
2. Click `+` to create a new branch.
3. Enable the **Development branch** toggle.
4. Under **Schema version**, select the version you published in [Step 1](#step-1-sync-your-schema-version).
5. Click `Create`.

![create-development-branches](https://vtexhelp.vtexassets.com/assets/docs/src/create-development-branches___7e6b97f48ce0869b87c046403fb1d5ff.gif)

> ⚠️ Development branches can't be merged into `main`, so content built on a test schema can never accidentally reach the live store. Also, this type of branch is automatically deleted 15 days after creation.

### Step 3 - Create and test content in the branch

1. Inside the development branch, create new versions of the entries you want to test.

2. Open a version to review it. Versions created in a development branch show a `</>` icon, so you can tell them apart from versions in `main`.

   > ⚠️ Only users with the **Manage Dev Branch** permission can see these versions.

3. To preview content locally while testing, add a Preview URL to the version. This is useful, for example, when testing new React components against a local FastStore instance running on your machine. To do so, point the Preview URL to `http://localhost:<port>/api/preview`.

![localhost-preview](https://vtexhelp.vtexassets.com/assets/docs/src/localhost-preview___52a1236720c070aab93d0f1604854a94.png)
