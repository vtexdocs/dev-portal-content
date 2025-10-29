---
title: "Preparing your app for distribution"
slug: "vtex-io-documentation-preparing-your-app-distribution"
excerpt: "Learn how to prepare your app for distribution in the VTEX App Store."
hidden: false
createdAt: "2022-03-04T20:09:05.195Z"
updatedAt: "2025-10-29T12:20:00.000Z"
category: "App Development"
---

This guide will teach you how to prepare your app for distribution in the VTEX App Store and enable merchants to benefit from your solution.

Note that every app goes through a homologation process before being available in the VTEX App Store. During this process, our team can reject apps that do not follow the quality, viability, and usability standards presented in the [App Store Guidelines](https://developers.vtex.com/docs/guides/vtex-io-documentation-homologation-requirements-for-vtex-app-store). Therefore, be sure to review these guidelines as you develop and prepare your app for distribution.

## Before you begin

Before proceeding, ensure you have:

1. Developed your app. Refer to the [Developing an app](https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-an-app) guide for more information.

2. Registered as a [VTEX App Store developer](https://developers.vtex.com/docs/guides/vtex-io-documentation-becoming-a-registered-vtex-app-store-developer).

## Instructions

### Step 1 - Preparing your app billing options

After developing your app, you must establish whether your app will be charged and whether it will be public or private on the VTEX IO platform. To set up these options, refer to the [Setting your app's billing model](https://developers.vtex.com/docs/guides/vtex-io-documentation-setting-your-apps-billing-model) guide. Also, check the [App Monetization](https://developers.vtex.com/docs/guides/vtex-io-documentation-business-guidelines-app-monetization) guidelines for more information on this topic.

### Step 2 - Setting the `public` folder

After establishing your app's billing model, you must set up the marketing assets (e.g., icons, images, and descriptions) that will compose your app's page on the VTEX App Store. During this step, refer to our [Marketing](https://developers.vtex.com/docs/guides/vtex-io-documentation-business-guidelines-marketing-assets) guidelines.

![App Page on the VTEX App Store](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Perks/vtex-io-documentation-homologation-requirements-for-vtex-app-store/app-store-page-example.png?raw=true)

1. Create a new folder named `public` in the root directory of your project.
2. Inside the `public` folder, create the `metadata` folder. Also, create the `images`, `licenses`, and `messages` folders inside `metadata`.
3. Create the following folders and files as shown:

    ```plaintext
    ┗ 📂 public
      ┣ 📂 metadata
        ┣ 📂 images
          ┣ 📄 icon.png
          ┗ 📂 screenshots
            ┣ 📂 desktop
            ┗ 📂 mobile
      ┣ 📂 licenses
        ┣ 📄 en-US.md
        ┣ 📄 es-AR.md
        ┗ 📄 pt-BR.md
      ┗ 📂 messages
        ┣ 📄 en-US.json
        ┣ 📄 es-AR.json
        ┗ 📄 pt-BR.json
    ```

4. Create the files and folders needed to compose your App Page as follows:

#### `images` folder

The `images` folder stores the images for your app's page. They may include the app's icon and screenshots showing how the application behaves in the Admin or the storefront. Inside this folder, you must have:

```plaintext
┗ 📂 images
  ┣ 📄 icon.png
  ┗ 📂 screenshots
    ┣ 📂 desktop
      ┣ 📄 {add-a-file}.png
      ┗ 📄 {add-a-file}.png
    ┗ 📂 mobile
      ┣ 📄 {add-a-file}.png
      ┗ 📄 {add-a-file}.png
```

- `icon.png` - The app icon file.
- `screenshots` - A folder containing the images that will be presented in the App Page's carousel.

Note that you can use the `desktop` and `mobile` subfolders to store device-specific images. For example: `public/metadata/images/screenshots/mobile` and `public/metadata/images/screenshots/desktop`.

#### `licenses` folder

The `licenses` folder contains the terms and conditions of your app. Licenses establish the direct business relationship between the vendor and the retailer that installs the app.

Inside the `licenses` folder, create the files named using locale codes to provide your app's terms and conditions in different languages (e.g., `public/metadata/licenses/en-US.md`, `public/metadata/licenses/es-AR.md`, `public/metadata/licenses/pt-BR.md`).

#### `messages` folder

The `messages` folder contains textual information regarding your app, such as its name and list of features, in different languages.
See the base template for structuring this file below:

```json
{
  "name": "Order Tracker",
  "headline": "Headline Order Tracker.",
  "overview": "Tracks all orders\\nSecond line\\n\\nThird line\\n\\n\\n\\n\\nFourth line",
  "features": [
    "First feature",
    "Second feature",
    "Third feature",
    "Fourth feature"
  ],
  "additionalinformation": "Additional information\\nYou can also write new lines here\\n\\n\\nIt should work just like the overview",
  "video": "https://www.youtube.com/embed/645ASYhJS-Q",
  "websiteURL": "https://www.website.com/en",
  "support": {
    "email": "a@bcd.io",
    "url": "www....",
    "phone": "+1...."
  },
  "metricDescription": {
    "track": "English description for metric track",
    "notify": "English description for metric notify en-US"
  }
}
```

- **`name`:** App name, limited to 26 characters.
- **`headline`:** Short description of the main functionality of your application. The field has a 120-character limit.
- **`overview`:** Detailed description of your app’s main purposes and benefits. There is no character limit.
- **`features`:** List of your app’s main features and highlights.
- **`websiteURL`:** Link to the app's landing page or your corporate website.
- **`support`:** Link to the support channel. This can be an email address, a ticket portal, or a phone number.
- **`additionalinformation`:** Additional details and disclaimers related to your app.
- **`video`:** URL of a video featuring the app's behavior.
- **`metricDescription`:** Billing options' metrics (declared in the app's `manifest.json` file). **This field is required only for apps whose pricing is based on one or more metrics. Do not fill in this field if this is not applicable.**

The files in this folder must be available in English, Spanish, and Portuguese, in the following paths: `public/metadata/messages/en-US.json`, `public/metadata/messages/es-AR.json` and `public/metadata/messages/pt-BR.json`, respectively.

### Step 3 - Publishing and deploying your app on the VTEX IO development platform

If you are satisfied with your new app and marketing content, follow the [Deploying a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-making-your-new-app-version-publicly-available) guide to deploy your changes.

After deploying your app's latest version, follow the [Submitting your app to the VTEX App Store](https://developers.vtex.com/docs/guides/vtex-io-documentation-submitting-your-app-in-the-vtex-app-store) guide.
