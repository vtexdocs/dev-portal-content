---
title: "UTMs are not being applied to the cart at Checkout"
slug: "utms-are-not-being-applied-to-the-cart-at-checkout"
hidden: false
createdAt: "2022-07-25T19:16:25.665Z"
updatedAt: "2025-01-03T00:00:00.446Z"
excerpt: "Verify that traffic and marketing source information is being attributed to your store's carts."
tags:
    - checkout
    - cms
    - store-framework
---
Keywords: utm source | utm campaign | utm medium | checkout | cart

When an [UTM parameter](https://help.vtex.com/en/tutorial/what-are-utm-source-utm-campaign-and-utm-medium--2wTz7QJ8KUG6skGAoAQuii) (`utm_source`, `utm_campaign` or `utm_medium`) is used to load a store page, the system creates a cookie named **IPS** whose value is equal to the value of the parameter.

The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) structure of orders closed by the user will receive this cookie in the header of the request sent to Checkout (until this cookie expires). In other words, the moment the customer clicks the `Buy` button native control (`<vtex.cmc:BuyButton/>`), it will trigger a `POST` request to send the value of the `utm_source` parameter to the Checkout.

In this way, the Checkout will be able to assemble the orderForm considering the `marketingData` used in the purchase.

> ⚠️ The IPS cookie is created for Legacy CMS Portal accounts only. For stores using the [Store Framework](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-store-framework), information from marketing UTMs is sent to Checkout through the Sessions system.

However, there are some situations in which the UTM parameters are not being loaded into the cart, preventing the identification of the origin of the traffic or the application of a specific promotion assigned to an UTM.

## Solutions

To check whether the UTM parameters are being correctly applied to the cart and possible actions to correct if there is an error, see the following actions below:

### Confirming the presence of an UTM in the cart

Carry out procedures to check the existence of UTMs in the cart according to your type of store:

- **Legacy CMS Portal**

  1. Access any page of the store with the UTM in the querystring (e.g. `{accountName}.{environment}.com.br/?utm_source=facebook`).
  2. Go to the **Developer tools** screen (**F12** in Chrome, if you are in Windows, or **Cmd+Opt+I** on a Mac).
  3. Click the **Application** tab, and under **Cookies**, click the name **IPS**.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/check-marketing-utms-used-at-checkout-0.PNG)

- **Store Framework**

  1. Access any page of the store with the UTM in the querystring (e.g. `{accountName}.{environment}.com.br/?utm_source=facebook`).
  2. Go to a product page and add it to the cart.
  3. Access the cart.
  4. Refresh the page (**F5** in Chrome, if you are in Windows, or **Cmd+R** on a Mac) and monitor the requests on the **Network** tab (also located on the **Developer tools** screen).
  5. In the **Preview** tab, open the `marketingData` node.
  6. Check the value of the `utmSource` field.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/check-marketing-utms-used-at-checkout-1.PNG)

> ℹ️ If the value found in the `utmSource` field is the same as the UTM previously entered in the page address querystring, it means that Checkout is correctly receiving the information in the cart. If the `utmSource` field is blank, it indicates that the information was not assigned to the cart, preventing the tracking of the origin of the traffic, the application of promotions related to UTM and the registration of the parameter in the orders carried out by the OMS.

## Adding UTM parameters to the cart

As previously stated, the native buy button control (`<vtex.cmc:BuyButton/>`) triggers a POST request sending all the data needed to the Checkout, including the value of the `utm_source`, `utm_campaign` and `utm_medium`.

If the UTM parameters are not being sent to the cart, you should check if your store is using a **custom purchase POST call** instead of the native control. After confirming the existence of a custom purchase POST call, you can update its settings to ensure that contains all the data needed to assemble the orderForm, including the marketing context, or perform one of the actions below:

- Send UTM parameters for a specific cart by accessing the [Add marketing data](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/marketingData) endpoint or by entering the `marketingData` information via the [sendAttachment](https://developers.vtex.com/docs/guides/vtexjs-for-checkout#sendattachmentattachmentid-attachment-expectedorderformsections).
- Use the [Cartman](https://help.vtex.com/en/tutorial/configure-cartman--1ACMTStZYkMqB0lTgwg451#define-marketing-data) tool on the checkout screen to add UTM parameters directly to the cart.

For more information about error scenarios when applying UTM to cart, visit Known Issues articles [Price by UTM doesn&#39;t work when using special characters](https://help.vtex.com/en/known-issues/price-by-utm-doesnt-work-when-using-special-characters--5vQnjYgbE48426q2e6GMUY) and [Applying a Coupon Removes Initial UTM Campaign Promotion from Cart](https://help.vtex.com/en/known-issues/applying-a-coupon-removes-initial-utm-campaign-promotion-from-cart--2A1S6PgEwD9SgQo1UHrFFS).
