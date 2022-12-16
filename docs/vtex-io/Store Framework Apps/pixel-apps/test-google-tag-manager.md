---
title: "Test - Google Tag Manager"
slug: "test-google-tag-manager"
hidden: true
createdAt: "2021-10-06T18:18:03.895Z"
updatedAt: "2021-10-06T20:09:57.389Z"
---
📢 Use this project, [contribute](https://github.com/vtex-apps/google-tag-manager) to it or open issues to help evolve it using [Store Discussion](https://github.com/vtex-apps/store-discussion).

# Google Tag Manager

<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

The VTEX Google Tag Manager app is a first party integration to the [Google Tag Manager solution](https://tagmanager.google.com).

![google-tag-manager-app](https://user-images.githubusercontent.com/52087100/84321347-55e11c80-ab49-11ea-9445-24eec6a07785.png)

## Configuration

It is possible to install the VTEX native GTM app in your store either by using App Store or the VTEX IO Toolbelt.

### Using VTEX App Store

1. Access the **Apps** section in your account's admin page and look for the Google Tag Manager box;
2. Then, click on the **Install** button;
3. You'll see a warning message about needing to enter the necessary configurations. Scroll down and type in your **GTM ID** in the `Google Tag Manager` field.
4. Click on **Save**.

>ℹ️ *Access the [Google Tag Manager page](https://tagmanager.google.com/) and login to your account in order to find out what is your account **GTM ID**. The number your should use is the one provided by the `Container ID` column.*

### Using VTEX IO Toolbelt

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the `vtex.google-tag-manager@2.x` app. You can confirm that the app has now been installed by running `vtex ls` again.
2. Access the **Apps** section in your account's admin page and look for the Google Tag Manager box. Once you find it, click on the box.
3. Fill in the `Google Tag Manager` field with your **GTM ID**.
4. Click on **Save**.

:information_source: Access the [Google Tag Manager page](https://tagmanager.google.com/)</a> and login to you account in order to find out what is your account **GTM ID**. The number your should use is the one provided by the `Container ID` column.

After installing the app, you are ready to use your GTM as usual by accessing your account dashboard directly on the [Google Tag Manager](https://tagmanager.google.com/) page.

## Restrictions

In order to avoid performance problems and unforeseen behavior, our VTEX IO Google Tag Manager solution uses the native GTM **blacklist** feature. You can read more about this feature on the [Google Developer Guide](https://developers.google.com/tag-manager/web/restrict).

We, by default, blacklist the `html` ID, which automatically blocklists all the tags, variables and triggers of the type `customScripts`. The main consequence of this blocklist is that **Custom HTML tags will not be triggered**.

> ⚠️ *The HTML blacklist is VTEX Google Tag Manager app's default. If you want to disable this restriction go to `https://{accountName}.myvtex.com/admin/apps/vtex.google-tag-manager@2.x/setup` and check the toggle below.*

<img src="https://user-images.githubusercontent.com/11340665/103930428-7c762e80-50fd-11eb-9cab-bc9e542b4dbf.png">

Most of the widely used Custom HTML tags are integrations with third-party services, like Customer Chat, Analytics, Remarketing, and Pixel tags. If your store needs a Custom HTML for one of those cases, the integration can either be done by transforming the tags into a [VTEX IO Pixel App](https://vtex.io/docs/apps/pixel/) or by removing this restriction.

Check out below the full list of tags and variables that are blocked, by default, in VTEX IO Google Tag Manager solution below:

### Blocked tags

- Custom HTML Tag - `html`
- Eulerian Analytics Tag - `ela`
- SaleCycle JavaScript Tag  - `scjs`
- Upsellit Global Footer Tag - `uslt`
- Upsellit Confirmation Tag - `uspt`

### Blocked variables

- Custom JavaScript Variable - `jsm`

Check out a list with all the GTM available tags on the [Google Developer Guide](https://developers.google.com/tag-manager/devguide).

## Troubleshooting
### Persisting campaign data across user navigation

VTEX IO’s page routing system requires a special configuration in the Google Tag Manager container to maintain the [Google Tag Manager (GTM)](https://developers.vtex.com/vtex-developer-docs/docs/vtex-google-tag-manager)  session identifier. Without the configuration, the GTM detects that the campaign data is no longer in the URL and It creates a new session without the data, leading to inconsistent Google Analytics (GA) campaign data.

To persist campaign data across user navigation you must add the variable `OriginalLocation` to your GTM container and configure your store’s Google Analytics tags to persist campaign data correctly and prevent GTM from creating additional sessions when a user navigates the website. Follow the step-by-step below to add the variable and persist the campaign data during user navigation.

> ⚠️ *The variable, `OriginalLocation`, is already available by the VTEX app (versions 2.x or 3.x). If you have another Google Tag Manager app installed, we strongly recommend using [The VTEX Google Tag Manager app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-google-tag-manager#configuration) to use the variable.* 


### Step-by-step

#### Step 1 - Creating the variable Original Location

1. Login into your [GTM account](https://tagmanager.google.com) and click on the GTM container you want to work with. 


> ℹ️  *The GTM ID is in your store's Admin, and in the section **My Apps**, search for the Google Tag Manager app. Click on the app and, on the settings page, look for the "Google Tag Manager" field with the GTM ID value, for example:,`GTM-XXXXXXX`.* 

1. On the container's page, click on **Variables**.

2. In the section **Built-In Variables**, check if the variables `Page URL` and `Page Path` are enabled. Otherwise, click on `Configure` and select `Page URL` and `Page Path` to enable them. 

4. Once you have enabled the variables, go to the section **User-Defined Variables**, click on `New`, and a side popup will open.

5. Type on the `Untitled Variable` field the variable name: `Original Location`.
6. Next, click on **Variable Configuration** and in **Page Variables** click on **Data Layer Variable**.
7. In the `Data Layer Variable Name` field, type `OriginalLocation`.
8. Select `Set Default Value` and fill the `Default Value` with the following value:

```
{{Page URL}}

```
![gif1](https://user-images.githubusercontent.com/67270558/136271386-afe75beb-32f3-46db-bb31-726f9275973d.gif)

9. Click on `Save`

#### Step 2 - Updating Google Analytics Settings variables and Google Analytics tags

After [creating the variable `OriginalLocation`](#link para o step1), use the Google Analytics Settings variables to configure every Google Analytics Tags that fire.

> ℹ️ * to create a Google Analytics Settings variable follow the [Google Tag Manager documentation](https://support.google.com/tagmanager/answer/9207621?hl=en)*


1. Click on the **Variables** section, on **User-Defined Variables** and select one of the  Google Analytics Settings variables.

![img](https://user-images.githubusercontent.com/67270558/136271858-f8e783e4-177d-4fd0-b6f1-3768cc175fef.png)

2. Click on **Variable Configuration** box and in **More Settings** select **Fields to Set**.
3. In **Fields to set**, click on `Add Field`.
4. Set the `Field Name` field as `location` and `Value` as `{{Original Location}}`.
5. Click on `Save`. 

> ⚠️ *Ensure that you do not have any Google Analytics tags using the Google Analytics Settings variables you have changed. Otherwise, apply the same changes above directly on the tags that need it. *

#### Step 3 - Publishing your changes

Once you have set up the Google Analytics variables and tags, follow Google's official guide on [how to submit and publish your store’s container changes](https://support.google.com/tagmanager/answer/6107163).


<!-- DOCS-IGNORE:start -->

## Contributors ✨

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->