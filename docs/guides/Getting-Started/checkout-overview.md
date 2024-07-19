---
title: "Checkout"
slug: "checkout-overview"
hidden: false
createdAt: "2020-09-11T23:12:53.108Z"
updatedAt: "2022-10-21T13:19:52.868Z"
seeAlso:
  - "/docs/api-reference/checkout-api#overview"
---

> **Help us improve our documentation!** Tell us about your experience with this article by completing [this form](https://forms.gle/fQoELRA1yfKDqmAb8).

## Customizing the Checkout UI

All VTEX stores have a native Checkout UI ready to be used from the start of their operations on the platform. However, if the merchant wants to change some features on this UI, VTEX offers the option of customizing the Checkout. See the links below for helpful information and apps to customize the Checkout UI of your store.

* [Checkout customization guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-customization-guide)
* [Checkout UI Custom app](https://developers.vtex.com/docs/guides/vtex-checkout-ui-custom-v0)
* [Checkout UI Settings app](https://developers.vtex.com/docs/guides/vtex-checkout-ui-settings)
* [Checkout Settings (B2B)](https://developers.vtex.com/docs/guides/vtex-b2b-checkout-settings)
* [Customizing the Header and Footer blocks by page](https://developers.vtex.com/docs/guides/vtex-io-documentation-customizing-the-header-and-footer-blocks-by-page)
* [Customizing checkout confirmation pages](https://developers.vtex.com/vtex-rest-api/docs/customize-checkout-confirmation-pages)
* [Enabling an Observation field on the Checkout page](https://developers.vtex.com/vtex-rest-api/docs/enable-an-observation-field-on-the-checkout-page)
* [Layout Development Guide for payment methods in Smart Checkout VTEX](https://developers.vtex.com/vtex-rest-api/docs/layout-development-guide-for-payment-methods-in-smart-checkout-vtex)
* [How to set up and use checkout data from the customer side (vtex.js for Checkout)](https://developers.vtex.com/vtex-rest-api/docs/vtexjs-for-checkout)
* [Changing payment methods on Checkout](https://developers.vtex.com/vtex-rest-api/docs/change-payment-method-names-in-checkout)<br>

Smart Checkout - Payment layout customization example:

![Layout Dev Guide - Guide](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Checkout/Layout_Dev_Guide_29.gif)

## Understanding Checkout data structures

In the VTEX Checkout architecture, the main data structure is the `orderForm` object. This object has several sections and fields that allow you to control all the important information about the order. See the links below for helpful information and endpoints related to the `orderForm` object.

* [OrderForm overview](https://developers.vtex.com/docs/guides/orderform-fields)
* [Setting discounts using the Checkout API](https://developers.vtex.com/vtex-rest-api/docs/set-a-discount-using-the-checkout-api)
* [Enabling orderForm optimization - Store Framework only](https://developers.vtex.com/docs/guides/vtex-io-documentation-enabling-order-form-optimization)
* [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)
* [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)
* [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)

## Collecting custom customer information

To request additional customer information besides what the `orderForm` collects, stores can create `custom fields`. See the links below for helpful information and endpoints related to custom customer information.

* [Adding and handling custom information in the order](https://developers.vtex.com/docs/guides/add-and-handle-custom-information-in-the-order)
* [Custom fields created by the Mercado Libre connector](https://developers.vtex.com/vtex-rest-api/docs/get-payment-data-mercado-libre-orders-api#understanding-customdata)
* [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)
* [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)
* [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)

> This module may process personal or sensitive information. Learn more about how VTEX handles data privacy at our [Data privacy](https://developers.vtex.com/docs/guides/data-privacy) guide.

## Accessing customer information

Once you have the customer information, you can check their profile information or even add them to a specific cart. See the links below to access endpoints related to customer information.

* [Enable the Save user information opt-in](https://developers.vtex.com/vtex-rest-api/docs/enable-the-save-user-data-opt-in)
* [GET - Get customer profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)
* [POST - Add customer profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)
* [POST - Add customer preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)
* [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)

## Accessing seller information

In a marketplace, you can check the seller database to find out which sellers are available in a given region and configure the exchange of sellers that fulfill an order. See the links below to access endpoints related to seller information.

* [GET - Get sellers by region or address](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/regions/-regionId-)
* [GET - Get the seller change window](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)
* [POST - Update the seller change window](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)

## Handling the shopping cart

In your store, you can perform many actions related to the shopping cart, including adding security items, simulating carts, changing the number of items, among others. See the links below for helpful information and endpoints related to handling the store shopping cart.

* [Minicart - Configuration and customization](https://developers.vtex.com/docs/guides/vtex-minicart)
* [ADD TO CART button](https://developers.vtex.com/docs/guides/vtex-add-to-cart-button#configuration)
* [reCAPTCHA](https://developers.vtex.com/vtex-rest-api/docs/recaptcha)
* [Implementing reCAPTCHA in integrations](https://developers.vtex.com/vtex-rest-api/docs/implementing-recaptcha-in-integrations)
* [Enabling Manual Price](https://developers.vtex.com/vtex-rest-api/docs/enable-the-manual-price)
* [Checking marketing UTMs used at Checkout](https://developers.vtex.com/vtex-rest-api/docs/check-marketing-utms-used-at-checkout)
* [POST - Cart simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)
* [GET - Get current or create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm)
* [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)
* [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)
* [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)
* [PATCH - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)
* [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)
* [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)
* [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)
* [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)
* [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)
* [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons) <br> Minicart view: <br> ![minicart-v2-gif](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Checkout/Minicart_Dev_Guide_1.gif) <br> <br> reCAPTCHA view: <br>

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Checkout/reCAPTCHA_Dev_Guide_1.gif)

## Getting information and simulating shipping logistics

By verifying addresses, pickup points, and fulfillment simulations, you can have an overview of how the shipping process will be carried out in your store. Additionally, you can configure your store to allow shipping to other countries. See the links below to access endpoints related to shipping.

* [Calculating SLA](https://developers.vtex.com/vtex-rest-api/reference/calculatesla)
* [Configuring Global Checkout](https://developers.vtex.com/vtex-rest-api/docs/configure-the-global-checkout)
* [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)
* [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)
* [POST - Fulfillment simulation](https://developers.vtex.com/vtex-rest-api/reference/fulfillment-simulation#request-body-example---checkout-simulation)

## Creating orders via API

APIs allow you to simulate all the order steps a customer goes through. See the links below for helpful information and endpoints related to the order flow.

* [Creating a regular order using the Checkout API](https://developers.vtex.com/vtex-rest-api/docs/create-a-regular-order-using-the-checkout-api)
* [Creating a regular order from an existing cart](https://developers.vtex.com/docs/guides/create-a-regular-order-from-an-existing-cart)
* [PUT - Place an order (no cart information available)](https://developers.vtex.com/vtex-rest-api/reference/placeorder)
* [POST - Place an order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)
* [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)

## Configuring tax customization systems

When your store sells products in several regions or has inventories in different locations, you may need to calculate different taxes for each order. To facilitate this, VTEX allows you to integrate an external tax calculation provider. See the links below to access information on how to integrate an external tax calculation provider with your store.

* [Tax service - Overview](https://developers.vtex.com/vtex-rest-api/docs/tax-services-overview)
* [Tax service - Specification](https://developers.vtex.com/vtex-rest-api/docs/tax-services-specification#checkout-configuration)
* [Tax service - Recipe](https://developers.vtex.com/vtex-rest-api/docs/tax-services-recipe)
* [Tax service - Implementation](https://developers.vtex.com/vtex-rest-api/docs/tax-services-reference-implementation)

## Integrating Checkout with apps

On VTEX checkout, some features are activated through apps. See the links below for information about available apps for your store checkout.

* [Setting up Google Tag Manager](https://developers.vtex.com/docs/guides/vtex-io-documentation-setting-up-google-tag-manager#creating-variables)
* [Migrating Google Tag Manager app from major 2.x to major 3.x](https://developers.vtex.com/docs/guides/vtex-io-documentation-migrating-google-tag-manager-app#before-you-start)
* [Hotjar App - Website Heatmaps & Behavior Analytics Tools](https://developers.vtex.com/docs/guides/vtex-hotjar)
* [PowerReviews App - UGC (User Generated Content) Ratings & Reviews Tool](https://developers.vtex.com/docs/guides/vtex-powerreviews) <br> Hotjar heatmap example:

![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Checkout/Hotjar_example_Dev_Guide_1.png)

<br>

Product review example: ![](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Checkout/Product_review_example_Dev_Guide_1.png)
