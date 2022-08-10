---
title: "Yotpo Integration"
slug: "vtex-yotpo-integration"
excerpt: "vtex.yotpo-integration@0.3.0"
hidden: true
createdAt: "2022-07-18T21:13:55.808Z"
updatedAt: "2022-08-08T19:25:21.772Z"
---
Yotpo Integration is a VTEX IO native solution that allows stores to send order data to Yotpo, which is triggered when an order is invoiced.

## Configuration

### Step 1 Installing the Yotpo Integration app

Using your terminal, log in to the desired VTEX account and run the following command:

`vtex install vtex.yotpo-integration@0.x`

### Step 2 - Adding in Yotpo Information

In the admin page, fill in the required fields of App Key and Secret Key. This can be accessed from the Yotpo website, after creating an account and requesting developer access. You can follow the instructions provided by Yotpo here [Finding your Yotpo App Key and Secret Key](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key)

### Step 3 - Products registration

All products and Catalogs need to be imported/registered with Yotpo before orders can be sent to Yotpo. For Prime and Premium accounts, please follow [Importing Product Catalogs](https://support.yotpo.com/en/article/importing-product-catalogs) to import your products.
And another option for Free or Growth accounts is to post a test review, that way the reviewed product will also be registered when the review goes through.

### Step 3 - Automatic Review Requests

For Automatic Review Requests setups and usage please follow [Automatic Review Requests](https://support.yotpo.com/en/article/automatic-review-requests)

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).