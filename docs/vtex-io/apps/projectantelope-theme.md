---
title: "Project Antelope"
slug: "projectantelope-theme"
excerpt: "projectantelope.theme@0.4.4"
hidden: true
createdAt: "2022-07-11T06:36:46.529Z"
updatedAt: "2022-08-02T10:26:13.005Z"
---
This is store theme repo for front model based on the VTEX IO Store Framework, components IO apps and theme. Customizations will be done on this to acheive Project Antelope specific designs.

## Dev Process

#### DOs

- Use Tachyons classes
- Create separate folders for each modules
- Follow lint and other pre-checks
- Include the blocks in .jsonc files
- Follow PR template instructions
- Always add JIRA ID in comments and PR titles

#### DONT's

- Don't ignore standard folder structure
- Don't mix other theme or site changes in this repo
- Don't include unneccessary libraries or dependencies

## Configuration

#### Step 1 - Basic setup

Access the VTEX IO [basic setup guide](https://vtex.io/docs/getting-started/build-stores-with-store-framework/2) and follow all the given steps.

By the end of the setup, you should have the VTEX command line interface (Toolbelt) installed along with a developer workspace you can work in.

#### Step 2 - Cloning this repo.

#### Step 3 - Installing required apps

In order to use Store Framework and work on your store theme, it is needed to have both `vtex.store-sitemap` and `vtex.store` installed.

Run `vtex list` and check whether those apps are already installed.

If they aren't, run the following command to install them: `vtex install vtex.store-sitemap vtex.store -f`

#### Step 4 - Uninstalling any existing theme

By running `vtex list`, you can verify if any theme is installed.

It is common to already have a `vtex.store-theme` installed when you start the store's front development process.

Therefore, if you find it in the app's list, copy its name and use it together with the command `vtex uninstall`. For example:

```json
vtex uninstall vtex.store-theme
```

#### Step 5- Run and preview your store

Then time has come to upload all the changes you made in your local files to the platform. For that, use the `vtex link` command.

If the process runs without any errors, the following message will be displayed: `App linked successfully`. Then, run the `vtex browse` command to open a browser window having your linked store in it.

This will enable you to see the applied changes in real time, through the account and workspace in which you are working.