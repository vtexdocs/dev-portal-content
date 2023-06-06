---
title: "Setting up Google Tag Manager"
slug: "vtex-io-documentation-setting-up-google-tag-manager"
hidden: false
createdAt: "2020-06-03T16:02:44.272Z"
updatedAt: "2022-12-13T20:17:44.813Z"
category: "Storefront development"
excerpt: "Steps to update the Google Tag Manager app to version 3.x."
seeAlso:
  - "/docs/guides/google-tag-manager"
  - "/docs/guides/vtex-io-documentation-migrating-google-tag-manager-app"
  - "/docs/guides/vtex-io-documentation-setting-up-google-analytics-search-tracking"
---

Once you have installed the [VTEX IO Google Tag Manager app](https://developers.vtex.com/docs/guides/google-tag-manager), set it up in your store by configuring all the necessary variables, triggers, and tags.

> ⚠️ If you are using Google Tag Manager 2.x., **we strongly recommend migrating to major 3.x.** Google Tag Manager 3.x tracks the entire user journey through the store, from viewing a product to purchasing it. See [Migrating Google Tag Manager app from major 2.x to major 3.x](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-google-tag-manager-app) and follow the steps.

## Before you begin

**The VTEX IO GTM app is compliant with the Universal Analytics [Enhanced Ecommerce](https://developers.google.com/analytics/devguides/collection/ua/gtm/enhanced-ecommerce) events format**, meaning it supports the following events:

- Product Impression.
- Product Click.
- Product Detail Impression.
- Add/Remove from Cart.
- Promotion Impression.
- Promotion Click.
- Checkout.
- Purchase.

GTM components trigger these events, allowing you to measure your store data. If you are not familiar with GTM components, **, we strongly recommend** checking the [Google Tag Manager documentation](https://support.google.com/tagmanager/answer/6103657?hl=en) before starting the setup.

> ℹ To track the events related to search use on your site in Google Analytics, learn how to [set up Google Analytics search tracking](https://developers.vtex.com/docs/guides/vtex-io-documentation-setting-up-google-analytics-search-tracking) in your VTEX IO store.

Follow the steps below to create all the GTM components that your store needs.

## Instructions

### Step 1 - Creating variables

Variables are small data points you can use in tags or triggers to indicate when and where to fire a tag based on a trigger condition. For example, if you want to fire a tag on a page view, you need to decide if the tag will be fired on all page views or in a specific page.

To start, create the essential variables to work within GTM: **Data Layer** and **Google Analytics settings.**

- **Data Layer variables:** Store and deliver data from your website to GTM. Data includes page title and URL, user ID, product ID, product price, and other.

- **Google Analytics settings variables:** A template to set up Google Analytics tags in one place instead of making changes in each tag. These variables track page views, events, and ecommerce transactions.

1. Open the [Google Tag Manager dashboard](https://tagmanager.google.com).
2. Click **Variables.**
3. In the **User-Defined Variables** box, click **New.**

![variables-overview](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/vtex-io/Storefront-Guides/google-tag-manager/vtex-io-documentation-setting-up-google-tag-manager-0.png)

#### Data Layer variables

1. Click the **Variable Configuration** box and select **Data Layer Variable.**
2. Type `currency` in the `Data Layer Variable Name` field.
3. Click `Save` and save it as **Data Layer Variable - currency**.

Repeat the instructions above changing the data layer variable name to each of the following variables, except **Data Layer Variable - currency**, which was already declared in the example above:

| Variable name                          | Value              | Description                                                        | Tags that will use it            |
| -------------------------------------- | ------------------ | ------------------------------------------------------------------ | -------------------------------- |
| Data Layer Variable - currency         | `currency`         | Indicates the local currency for all transaction currency amounts. | `Google Ads Conversion Tracking` |
| Data Layer Variable - transactionId    | `transactionId`    | Indicates a unique transaction identifier.                         | `Google Ads Conversion Tracking` |
| Data Layer Variable - transactionTotal | `transactionTotal` | Indicates the transaction total amount.                            | `Google Ads Conversion Tracking` |

| Variable name                | Value         | Description                                                                                                                                                         | Variables that will use it                     |
| ---------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Data Layer Variable - userId | `userId`      | Enables linking one or more sessions to a unique and persistent ID for your store users.                                                                            | `Google Analytics`                             |
| ecommerceV2                  | `ecommerceV2` | Triggers events to track the entire user journey through the store, from viewing a product to purchasing it. **This variable is part of major 3.x** of the GTM app. | `Google Analytics - Checkout and Order Placed` |

There are two other variables, **`originalLocation` and `originalReferrer`,** that you must create to **prevent GTM from making additional session identifiers every time a user navigates the website.** Learn how to create them in the following steps.

##### Creating the Original Location and Original Referrer variables

Creating the following variables is important for making campaign data persist throughout a user session and to avoid sending inconsistent campaign data to Google Analytics (GA).

1. On the container page, click **Variables.**
2. In the **Built-In Variables** section, check if the `Page URL` and `Page Path` variables are enabled. If they aren't, click Configure and select Page URL and Page Path to enable them.
3. Go to the **User-Defined Variables** section and click `New`. A side popup will open.
4. Replace the `Untitled Variable` value with `Original Location`.
5. Click `Variable Configuration`.
6. In **Page Variables**, click `Data Layer Variable`.
7. In the `Data Layer Variable Name` field, enter `originalLocation`.
8. Enable the `Set Default Value` option and complete the `Default Value` field with the following value: `{{Page URL}}`.

![gtm-variable-location](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-setting-up-google-tag-manager-1.gif)

9. Click `Save`.

Once you have saved the `originalLocation` variable, create the `originalReferrer` as described in the steps below:

1. In the **User-Defined Variables** section, click `New`. A side popup will open.
2. Replace the `Untitled Variable` value with `Original Referrer`.
3. Click `Variable Configuration`.
4. In **Page Variables**, click `Data Layer Variable`.
5. In the `Data Layer Variable Name` field, enter `originalReferrer`.
6. Enable the `Set Default Value` option and complete the `Default Value` field with the following value: `{{Referrer}}`.

![gtm-variable-referrer](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-io-documentation-setting-up-google-tag-manager-2.gif)

7. Click `Save`.

#### Google Analytics variables

You will create one variable for the storefront — default — and another one for the store checkout.

| Variable type                | Description                                                                         | Tags that will use it                                                                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Default - For the storefront | Tracks page views.                                                                  | `Google Analytics - Enhanced Ecommerce - No Interaction`, `Google Analytics - Enhanced Ecommerce - Yes Interaction`, `Google Analytics - Page View` |
| For the store checkout       | Tracks the user journey through the store, from viewing a product to purchasing it. | `Google Analytics - Checkout and Order Placed`                                                                                                      |

##### Default - For the storefront

1. In the **User-Defined Variables** box, click `New`.
2. Click the **Variable Configuration** box and select **Google Analytics Settings**.
3. Enter your [**Google Analytics Tracking ID**](https://support.google.com/tagmanager/answer/9207621#ga_id), `{{Analytics Tracking ID}}`.
4. Go to **More Settings > Fields to Set**.
5. Click the **Add Field** button. Then, enter `location` in **Field Name** and `{{Original Location}}` in the **Value** field.
6. Click **Add Field**. Then, enter `referrer` in **Field Name** and `{{Original Referrer}}` in the **Value** field.
7. Click **Add Field**. Then, enter `page` in **Field Name** and `{{Page Path}}` in the **Value** field.

![img-example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/vtex-io/Storefront-Guides/google-tag-manager/vtex-io-documentation-setting-up-google-tag-manager-3.png)

7. Then, go to **Ecommerce** and tick the `Enable Enhanced Ecommerce Features` and `Use data layer` boxes.
8. Save your changes as **Google Analytics**.

If you intend to use the [User ID feature of Google Analytics](https://support.google.com/analytics/answer/3123662#zippy=%2Cneste-artigo), you need to set a field using the `userId` variable previously created. To do this, click Fields to set and add the `userId` field with the desired value.

##### For the store checkout

1. In the **User-Defined Variables** box, click `New`.
2. Click the **Variable Configuration** box and select **Google Analytics Settings**.
3. Enter your **Google Analytics Tracking ID**, `{{Analytics Tracking ID}}`.
4. Go to **More Settings > Fields to Set**.
5. Click the **Add Field** button. Then, enter `location` in **Field Name** and `{{Original Location}}` in the **Value** field.
6. Click the **Add Field** button. Then, enter `referrer` in **Field Name** and `{{Original Referrer}}` in the **Value** field.
7. Click the **Add Field** button. Then, type `page` in **Field Name** and `{{Page Path}}` in the **Value** field.
8. Then, go to the **Ecommerce** section and tick the `Enable Enhanced Ecommerce Features` option.
9. Select the `{{ecommerceV2}}` option in **Read data from variable**.
10. Save your changes as **Google Analytics - Checkout and Order Placed**.

> ⚠️ If you have any Google Analytics tags using the Google Analytics Settings variables you have changed, apply the same changes above directly to the tags that need it.

### Step 2 - Creating triggers

Triggers are conditions to control when should tags fire. For example, if you want to activate the Google Ads conversion tag when a visitor signs up for your store newsletter, you use a trigger. To create a trigger, click Trigger in the left menu and then New:

![trigger-overview](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/vtex-io/Storefront-Guides/google-tag-manager/vtex-io-documentation-setting-up-google-tag-manager-4.png)

#### Custom events

1. Click the **Trigger Configuration** box.
2. Select **Custom Event**.
3. Enter `addToCart` in the **Event Name** field.
4. Click `Save`and save it as **Custom Event - addToCart**.

Repeat the instructions above, changing the event name for each of the following event triggers:

- `cart`
- `email`
- `orderPlaced`
- `payment`
- `productClick`
- `productDetail`
- `productImpression`
- `promotionClick`
- `promoView`
- `profile`
- `removeFromCart`
- `shipping`
- `pageView`

> ⚠️ To trigger the `promotionClick` event for an image in a store component, you need to include the URL path of the image. To do this, access the **CMS > Site Editor** and select the image within the component. Then, in the editing view, go to **URL** and enter the path you want to use, for example, `/collections/valentines-70-off`.

### Step 3 - Creating tags

Tags are the tracking code you want to implement in your store. For example, a tag can allow you to track a page view and send the data to Google Analytics.

To create a tag, click Tags in the left menu and then New:

![tag-overview](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/vtex-io/Storefront-Guides/google-tag-manager/vtex-io-documentation-setting-up-google-tag-manager-5.png)

#### Google Analytics - Checkout and Order Placed

1. Click the **Tag Configuration box.**
2. Select **Google Analytics - Universal Analytics.**
3. Select **Event** from the **Track Type field.**
4. Enter **Ecommerce** in the Category field.
5. Enter **Event** in the Action field.
6. In **Non-Interaction Hit**, select `True`.
7. In **Google Analytics Settings**, select `{{Google Analytics - Checkout and Order Placed}}`.
8. In the **Triggering** box, choose the following triggers:

- `Custom Event - cart`
- `Custom Event - email`
- `Custom Event - orderPlaced`
- `Custom Event - payment`
- `Custom Event - profile`
- `Custom Event - shipping`

9. Save the new tag as **Google Analytics - Checkout and Order Placed**.

#### Google Analytics - Enhanced Ecommerce - No Interaction

1. Click the **Tag Configuration** box.
2. Select **Google Analytics - Universal Analytics**.
3. Choose **Event** from the Track Type field.
4. Enter **Ecommerce** in the Category field.
5. Enter **Event** in the Action field.
6. Select **True** in the Non-Interaction Hit field.
7. In **Google Analytics Settings**, choose **{{Google Analytics}}**.
8. In the **Triggering** box, choose the following triggers:

- `Custom Event - productDetail`
- `Custom Event - productImpression`
- `Custom Event - promoView`

9. Save the new tag as **Google Analytics - Enhanced Ecommerce - No Interaction**.

#### Google Analytics - Enhanced Ecommerce - Yes Interaction

1. Click the **Tag Configuration** box.
2. Select **Google Analytics - Universal Analytics**.
3. Select **Event** from the Track Type field.
4. Enter **Ecommerce** in the Category field.
5. Enter **Event** in the Action field.
6. Select **False** in the Non-Interaction Hit field.
7. Choose **{{Google Analytics}}** in the Google Analytics Settings field.
8. In the **Triggering box**, choose the following triggers:

- `Custom Event - addToCart`
- `Custom Event - removeFromCart`
- `Custom Event - productClick`
- `Custom Event - promotionClick`

8. Save the new tag as **Google Analytics - Enhanced Ecommerce - Yes Interaction**.

### Google Analytics - Page View

1. Click the **Tag Configuration** box.
2. Select **Google Analytics - Universal Analytics**.
3. Choose **Page View** from the Track Type field.
4. In **Google Analytics Settings**, select **{{Google Analytics}}**.
5. In the **Triggering** box, select the **Custom Event - pageView** trigger.
6. Save the new tag as **Google Analytics - Page View**.

#### Conversion Linker

1. Click the **Tag Configuration** box.
2. Select **Conversion Linker**.
3. In the **Triggering** box, choose the **All Pages** trigger.
4. Save the new tag as **Conversion Linker**.

#### Google Ads Conversion Tracking

1. Click the **Tag Configuration** box.
2. Select **Google Ads Conversion Tracking**.
3. Complete the fields **Conversion ID** and **Conversion Label** following the instructions on the Google Ads dashboard.
4. Complete the following fields with Data Layer variables:

- Conversion Value: `{{Data Layer Variable - transactionTotal}}`
- Transaction ID: `{{Data Layer Variable - transactionId}}`
- Currency Code: `{{Data Layer Variable - currency}}`

> ⚠️ Remember to replace the values in curly brackets with the values that apply to your scenario.

5. In the **Triggering** box, select the **Custom Event - orderPlaced** trigger.
6. Save the new tag as **Google Ads Conversion Tracking**.

### Step 4 - Publishing your changes

Once you have set up the Google Analytics variables, triggers, and tags, follow Google's official guide [to submit and publish your store container](https://support.google.com/tagmanager/answer/6107163).

### (Optional) Advanced configurations with Enhanced Ecommerce

To make the product information consistent across all store areas and help capture the entire user journey in the store, [Google Tag Manager 3.x.](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-google-tag-manager-app) includes Enhanced Ecommerce properties for the product data schema as events. These properties enable stores to provide additional information, such as product printing, promotion, and sales data.

| Prop name  | Description                                                                          |
| ---------- | ------------------------------------------------------------------------------------ |
| id         | Product ID - Previously SKU ID.                                                      |
| variant    | SKU ID - Previously SKU Name. The variant of the product. For example: "Rebel pink". |
| name       | Product Name - Previously Product Name or SKU Name.                                  |
| quantity   | Product quantity.                                                                    |
| price      | Product price.                                                                       |
| category   | Product category. For example: "Apparel".                                            |
| brand      | Product brand.                                                                       |
| dimension1 | Product Reference ID.                                                                |
| dimension2 | SKU Reference ID.                                                                    |
| dimension3 | SKU Name (does not include the Product Name).                                        |

The `dimension1`, `dimension2`, and `dimension3` properties are custom dimensions that you can use to collect and analyze data that Google Analytics does not automatically create.

For more information about custom dimensions and Enhanced Ecommerce, see [Custom dimensions and metrics](https://support.google.com/analytics/answer/2709828?hl=en&ref_topic=2709827#configuration&zippy=%2Cin-this-article) and [Google Enhanced ecommerce official guide](https://developers.google.com/analytics/devguides/collection/analyticsjs/enhanced-ecommerce#ecommerce-data) respectively.

