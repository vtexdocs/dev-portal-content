---
title: "Checkout"
slug: "checkout-overview"
hidden: false
createdAt: "2020-09-11T23:12:53.108Z"
updatedAt: "2022-07-25T20:07:02.554Z"
---
[block:callout]
{
  "type": "info",
  "body": "📣 Help us improve our documentation! Share your feedback by filling out [this form](https://forms.gle/VVZpy2zFBHcoLp5Q8)."
}
[/block]
## Customizing Checkout UI 

All VTEX stores have a native Checkout UI ready to be used from the beginning of their operations on the platform. However, if the merchant wants to change some features on this UI, VTEX also offers the option of customizing the Checkout. See the links below for useful information and apps to customize your store’s Checkout UI.

* [Checkout customization guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-customization-guide)
* [Checkout UI Custom App](https://developers.vtex.com/vtex-developer-docs/docs/vtex-checkout-ui-custom-v0)
* [Checkout UI Settings App](https://developers.vtex.com/vtex-developer-docs/docs/vtex-checkout-ui-settings)
* [Checkout Settings (B2B)](https://developers.vtex.com/vtex-developer-docs/docs/vtex-b2b-checkout-settings)
* [Customizing the Header and Footer blocks by page](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-customizing-the-header-and-footer-blocks-by-page)
* [Customizing the Checkout Confirmation pages](https://developers.vtex.com/vtex-rest-api/docs/customizing-the-checkout-confirmation-pages)
* [Enabling an Observation field on the Checkout page](https://developers.vtex.com/vtex-rest-api/docs/enabling-an-observation-field-on-the-checkout-page)
* [Layout Development Guide for payment methods in Smart Checkout VTEX](https://developers.vtex.com/vtex-rest-api/docs/layout-development-guide-for-payment-methods-in-smart-checkout-vtex)
* [How to setup and use checkout data from client side (vtex.js for Checkout)](https://developers.vtex.com/vtex-rest-api/docs/vtexjs-for-checkout)
* [Changing the names of payment methods at the Checkout](https://developers.vtex.com/vtex-rest-api/docs/changing-the-names-of-payment-methods-at-the-checkout)<br>
Smart Checkout - Payment layout customization example:


[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4767f4f-Layout_Dev_Guide_-_Guide.gif",
        "Layout Dev Guide - Guide.gif",
        512,
        421,
        "#f1f4f3"
      ],
      "caption": ""
    }
  ]
}
[/block]
## Understanding Checkout data structures

The architecture of VTEX Checkout is organized in such a way that the main data structure is the `orderForm` object. It is composed of several sections and fields that allow you to have control over all the important information of a purchase order. See the links below for useful information and endpoints related to the `orderForm` object.

* [OrderForm overview](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields)
* [Using Checkout API to set a discount](https://developers.vtex.com/vtex-rest-api/docs/using-checkout-api-to-set-a-discount)
* [Enabling the orderForm optimization - Store Framework only](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-enabling-order-form-optimization)
* [GET- Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)
* [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)
* [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)


## Collecting custom client data

To request client data additional to those available in the `orderForm`, stores can create `custom fields`. See the links below for useful information and endpoints related to custom client data.

* [Creating customizable fields in the cart with Checkout API](https://developers.vtex.com/vtex-rest-api/docs/customizable-fields-with-checkout-api)
* [How to add and handle custom information in the order (B2B)](how-to-add-and-handle-custom-information-in-the-order)
* [Custom fields created by Mercado Libre connector](https://developers.vtex.com/vtex-rest-api/docs/get-payment-data-mercado-libre-orders-api#understanding-customdata)
* [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)
* [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)
* [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)


## Accessing client data

Once you already have the client information registered, you can check their profile data or even add them to a specific cart. See the links below to access endpoints related to client data.

* [Save user data opt-in on Checkout](https://developers.vtex.com/vtex-rest-api/docs/save-user-data-opt-in-on-checkout)
* [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)
* [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)
* [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)
* [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)


## Accessing seller data

In the marketplace context, you can check the seller's database to find out which sellers are available in a given region and configure the exchange of sellers that fulfill a purchase order. See the links below to access endpoints related to seller data.

* [GET - Get sellers by region](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
* [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)
* [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)


## Handling the shopping cart 

In your store, you can perform various actions related to the shopping cart, including adding security items, simulating carts, modifying item quantities, etc. See the links below for useful information and endpoints related to the handle the shopping cart in your store.

* [Minicart - Configuration & Customization](https://developers.vtex.com/vtex-developer-docs/docs/vtex-minicart)
* [ADD TO CART Button](https://developers.vtex.com/vtex-developer-docs/docs/vtex-add-to-cart-button#configuration)
* [reCAPTCHA](https://developers.vtex.com/vtex-rest-api/docs/recaptcha)
* [Implementing reCAPTCHA in integrations](https://developers.vtex.com/vtex-rest-api/docs/implementing-recaptcha-in-integrations)
* [Enabling Manual Price](https://developers.vtex.com/vtex-rest-api/docs/enabling-manual-price-in-my-store)
* [Why are the UTMs not being applied to the cart?](https://developers.vtex.com/vtex-rest-api/docs/why-are-the-utms-not-being-applied-to-the-cart)
* [Identifying whether marketing UTMs are being sent to Checkout](https://developers.vtex.com/vtex-rest-api/docs/identifying-whether-marketing-utms-are-being-sent-to-checkout)
* [POST - Cart simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)
* [GET - Get current cart or create a new one](https://developers.vtex.com/vtex-rest-api/reference/getcurrentcartorcreateanewone)
* [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)
* [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)
* [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)
* [PATCH - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)
* [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)
* [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)
* [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)
* [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)
* [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)
* [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)
<br>
Minicart view:
<br>
![minicart-v2-gif](https://user-images.githubusercontent.com/52087100/73321194-7f477e80-4220-11ea-844b-f24d1c10363c.gif)
<br>
<br>
reCAPTCHA view:
<br>     

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5d0eb13-newCaptchaAnchor.gif",
        "newCaptchaAnchor.gif",
        616,
        164,
        "#f0f1f3"
      ],
      "caption": ""
    }
  ]
}
[/block]
## Getting information and simulating delivery logistics

By verifying addresses, pickup points, and fulfillment simulations, it is possible to have an overview of how the delivery process will be carried out in your store. Additionally, you can configure your store to allow delivery to other countries. See the links below to access endpoints related to delivery logistics.

* [Calculate SLA](https://developers.vtex.com/vtex-rest-api/reference/calculatesla)
* [Setting up the Global Checkout](https://developers.vtex.com/vtex-rest-api/docs/setting-up-the-global-checkout)
* [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)
* [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)
* [POST - Fulfillment simulation](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation#request-body-example---checkout-simulation)


## Making orders via API

Through APIs it is possible to simulate all the steps in the order process carried out by the client. See the links below for useful information and endpoints related to the flow of an order.

* [Using APIs to place a regular order](https://developers.vtex.com/vtex-rest-api/docs/using-apis-to-place-a-regular-order)
* [PUT - Place an order (no cart information available)](https://developers.vtex.com/vtex-rest-api/reference/placeorder) 
* [POST - Place an order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)
* [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)


## Configuring tax customization systems

When your store sells products to many regions or has stocks in different locations, you may need to calculate different taxes to apply to each order. To facilitate this procedure, at VTEX you can integrate an external tax calculation provider. See the links below to access information on how to integrate an external tax calculation provider into your store.

* [Tax Service - Overview](https://developers.vtex.com/vtex-rest-api/docs/tax-services-overview) 
* [Tax Service - Specification](https://developers.vtex.com/vtex-rest-api/docs/tax-services-specification#checkout-configuration)
* [Tax Service - Recipe](https://developers.vtex.com/vtex-rest-api/docs/tax-services-recipe)
* [Tax Service - Implementation](https://developers.vtex.com/vtex-rest-api/docs/tax-services-reference-implementation)


## Integrating Checkout with apps 

At VTEX checkout, some features are activated through apps. See the links below to access information about the apps available for your store's checkout.

* [Setting up Google Tag Manager](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-setting-up-google-tag-manager#creating-variables)
* [Migrating Google Tag Manager app from major 2.x to major 3.x](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-migrating-google-tag-manager-app#before-you-start)
* [Hotjar App - Website Heatmaps & Behavior Analytics Tools](https://developers.vtex.com/vtex-developer-docs/docs/vtex-hotjar)
* [PowerReviews App - UGC (User Generated Content) Ratings & Reviews Tool](https://developers.vtex.com/vtex-developer-docs/docs/vtex-powerreviews)
<br>
Hotjar heatmap example:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/df6d1e8-Hotjar_heatmap_example.png",
        "Hotjar heatmap example.png",
        952,
        646,
        "#808489"
      ],
      "caption": ""
    }
  ]
}
[/block]
<br>
Product review example:
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ac54295-Shop-for-Soft-Clean-Silky-Hydrating-Lotion-by-Estee-Lauder-Shoppers-Drug-Mart-copy-1009x1024.png",
        "Shop-for-Soft-Clean-Silky-Hydrating-Lotion-by-Estée-Lauder-Shoppers-Drug-Mart-copy-1009x1024.png",
        1009,
        1024,
        "#edebe9"
      ],
      "caption": ""
    }
  ]
}
[/block]