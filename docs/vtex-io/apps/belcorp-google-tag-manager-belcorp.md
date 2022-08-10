---
title: "Google Tag Manager"
slug: "belcorp-google-tag-manager-belcorp"
excerpt: "belcorp.google-tag-manager-belcorp@2.0.3"
hidden: true
createdAt: "2022-07-06T16:54:29.158Z"
updatedAt: "2022-08-09T23:32:56.998Z"
---
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

The VTEX Google Tag Manager (GTM) app is a first party integration to the [Google Tag Manager solution](https://tagmanager.google.com).

![google-tag-manager-app](https://user-images.githubusercontent.com/52087100/84321347-55e11c80-ab49-11ea-9445-24eec6a07785.png)

## Installing Google Tag Manager app

1. Access the **Apps** section in your account's admin page and look for the Google Tag Manager box;
2. Then, click on the **Install** button;
3. You'll see a warning message about needing to enter the necessary configurations. Scroll down and type in your **GTM ID** in the `Google Tag Manager` field.
4. Click on **Save**.

>ℹ️ **Info**
>
> Access the [Google Tag Manager page](https://tagmanager.google.com/)</a> and login to you account in order to find out what is your account **GTM ID**. The number your should use is the one provided by the `Container ID` column.

### Step 2 - Creating Google Analytics variables
To set up Google Tag Manager in your store, you must create and set up all necessary variables, triggers and tags. Follow the [Setting up Google Tag Manager documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-setting-up-google-tag-manager) to create them.

### Step 3 - Persisting campaign data throughout a user session
To prevent GTM from creating additional session identifiers every time a user navigates the website, you must add the variables `originalLocation` and `originalReferrer` to your GTM container and configure your store’s Google Analytics tags. Notice that this is important to persist campaign data throughout a user session and avoid providing inconsistent campaign data to Google Analytics (GA). 

>⚠️ **Warning**
>
> The `originalLocation` and `originalReferrer` variables are available for VTEX IO Google Tag Manager versions 2.x and 3.x.  

#### Creating the variables Original Location and Original Referrer

1. Log in to your [GTM account](https://tagmanager.google.com) and click on the GTM container you want to work with; 

![gtm-container](https://user-images.githubusercontent.com/67270558/136798596-cc0add2d-e110-4176-bc8d-665ded39da29.png)


2. On the container page, click on **Variables**;

3. In the **Built-In Variables** section, check if the `Page URL` and `Page Path` variables are enabled. Otherwise, click on `Configure` and select `Page URL` and `Page Path` to enable them; 

4. Go to the **User-Defined Variables** section and click on `New`. A side popup will open;

5. Replace the `Untitled Variable` value with `Original Location`;
6. Click on **Variable Configuration**;
7. On **Page Variables**, click on **Data Layer Variable**;
8. In the `Data Layer Variable Name` field, type `originalLocation`;
9. Enable the `Set Default Value` option and fill in the `Default Value` field with the following value:

```
{{Page URL}}
```

![gtm-variable-location](https://user-images.githubusercontent.com/67270558/139482165-21f93c6a-48e5-421a-8e06-c942bda01974.gif)

10. Click on `Save`.

Once you have saved the `originalLocation` variable, create the `originalReferrer` as described on the steps below: 

1. In the **User-Defined Variables** section, click on `New`. A side popup will open;
2. Replace the `Untitled Variable` value with `Original Referrer`;
3. Click on **Variable Configuration**;
4. On **Page Variables**, click on **Data Layer Variable**;
5. In the `Data Layer Variable Name` field, type `originalReferrer`;
6. Enable the `Set Default Value` option and fill in the `Default Value` field with the following value:

```
{{Referrer}}
```

![gtm-variable-referrer](https://user-images.githubusercontent.com/67270558/141315033-56e6e498-8c44-490d-a6dd-51f226dd6fc9.gif)

10. Click on `Save`.

#### Updating Google Analytics Settings variables and tags

Now, let's configure every Google Analytics Settings variable that fires the `originalLocation` and `originalReferrer` variables.

1. Go to the **Variables** section; 
2. On **User-Defined Variables**, click on the name of one of the Google Analytics Settings variables

![ga-variables](https://user-images.githubusercontent.com/67270558/136799579-f1bb7e68-ec4c-4deb-beb2-0dfedb88de10.png)

3. Click on the **Variable Configuration** box;
4. Go to **More Settings > Fields to Set**;
5. Click on `Add Field`;
6. Set the `Field Name` field as `location` and `Value` as `{{Original Location}}`;
7. Then, click on `Add Field` again;
6. Set the `Field Name` field as `referrer` and `Value` as `{{Original Referrer}}`;
8. Click on `Save`.

If you have any Google Analytics tags using the Google Analytics Settings variables you have changed, apply the same changes above directly on the tags that need it.

#### Publishing your changes

Once you have set up the Google Analytics variables and tags, follow Google's official guide on [how to submit and publish your store’s container](https://support.google.com/tagmanager/answer/6107163).


## Restrictions

In order to avoid performance problems and unforeseen behavior, our VTEX IO Google Tag Manager solution uses the native GTM **blacklist** feature. You can read more about this feature on the [Google Developer Guide](https://developers.google.com/tag-manager/web/restrict).

We, by default, blacklist the `html` ID, which automatically blocklists all the tags, variables and triggers of the type `customScripts`. The main consequence of this blocklist is that **Custom HTML tags will not be triggered**.

>⚠️ **Warning**
>
> The HTML blacklist is VTEX Google Tag Manager app's default. If you want to disable this restriction go to `https://{accountName}.myvtex.com/admin/apps/vtex.google-tag-manager@2.x/setup` and check the toggle below.

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