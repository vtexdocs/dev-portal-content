---
title: "PayPal Checkout with Smart Payment Buttons"
slug: "vtex-connector-paypal-commerce-platform"
hidden: false
createdAt: "2022-07-05T14:29:52.628Z"
updatedAt: "2022-12-15T14:22:59.351Z"
---

An app integrating PayPal Checkout with Smart Payment Buttons with a VTEX IO store. This allows a store to place PayPal's Smart Buttons in the VTEX cart, offering a quick checkout via the familiar PayPal experience. The app also makes PayPal available within VTEX's native checkout. This app utilizes VTEX's Payment Provider Framework SDK.

> ⚠️ _Because they allow a user to skip the normal VTEX checkout, the Smart Buttons cannot be used in combination with gift cards or other split payment methods._

> ⚠️ _Currently the Smart Buttons do not support Pickup In Store. To place a Pickup In Store order, shoppers must use PayPal within the native VTEX checkout._

> ⚠️ _Please reference [PayPal's documentation in regard to supported currencies](https://developer.paypal.com/reference/currency-codes/)._

> ⚠️ _For best results, we recommend [configuring your PayPal account to obtain the buyer's phone number during checkout](https://developer.paypal.com/api/nvp-soap/paypal-payments-standard/admin/checkout-settings/#get-contact-telephone-numbers)._

## Features

- Adds PayPal's [Smart Payment Buttons](https://developer.paypal.com/docs/checkout/) to your store's Checkout Cart page (or other locations such as the minicart), allowing users to place orders using PayPal's checkout experience instead of the standard VTEX checkout
- Also allows the user to use PayPal within the native VTEX checkout
- Allows the VTEX Payment Gateway's auto-settle behavior to be configured or disabled
- Allows PayPal Credit ("Pay Later") messaging to be displayed on the PDP and in product shelves

## Configuration

### Installation & Onboarding

> ⚠️ _Only users with access to the **Payments** section in the VTEX admin (or assigned the **PCI Gateway** role in License Manager) will be able to configure the app._

1. Install this app from the [VTEX App Store](https://apps.vtex.com/vtex-connector-paypal-commerce-platform/p) by clicking `Get App`.
2. If you wish to use the **Smart Payment Buttons**, install the Checkout Cart app by following its [documentation](https://developers.vtex.com/docs/apps/vtex.checkout-cart), **OR** modify your store-theme following the [Customization](#customization) section below. If using Checkout Cart, no store-theme modification is necessary.
3. In your VTEX admin dashboard, go to `Payments > PayPal`.
4. Confirm your PayPal account email address. If you don't already have a PayPal account, you will be walked through the steps to create one. If you want to use an email other than your VTEX account's email address, click the `Change` button. Clicking `Change` will also allow you to toggle into `Sandbox Mode` for testing purposes. (Note: If you onboard in Sandbox Mode, you will eventually need to disconnect your sandbox account and perform the onboarding again with a production PayPal account when you are ready to accept live payments.)
5. Click `Connect` and follow PayPal's prompts to complete the onboarding. This process will grant VTEX permission to process PayPal transactions on your behalf.
6. When onboarding is complete, you should be returned to the VTEX admin dashboard, where you will see a PayPal Account Status page. You can also return to this page by going to `Payments > PayPal` from the VTEX admin sidebar. On this page, if you see the message `You are ready to accept PayPal payments in checkout!`, you may proceed to the next step. If not, the page will list the necessary actions to be completed before you are able to accept payments.

### Payment Gateway Configuration

7. In your VTEX admin dashboard, go to `Payments > Settings`.
8. Click the `Gateway Affiliations` tab at the top of the screen, and then the green + button in the upper right corner to create a new Gateway Affiliation.
   - Choose `PayPalCP` from the list of connectors.
   - Enter a name of your choice for the affiliation.
   - If the Test/Live toggle is set to Test mode, a `workspace` input field will appear, allowing you to test the PayPal app in a non-production workspace. Note that you may need to save the affiliation and then edit it before the field will appear. After testing is complete, make sure to set this back to "master". Do not erase the contents of this field.
   - `API key` and `API token` should be left blank.
   - The `Payment Capture` dropdown allows you to control (or disable) VTEX's auto-settle behavior. If you choose the default `Use Behavior Recommended By The Payment Processor` option, payments will be automatically settled 24 hours after authorization.
   - When selecting the `Deactivated: Not Automatically Captured` option, the payment will be captured at the moment the Order associated with that payment is `invoiced`.
   - After configuring the above options, click `Save`.
9. ⚠️ **Important note**: Completing the next step (step 10) will cause a new payment option to appear in your store's checkout. Do not complete this step until you are ready to begin accepting PayPal orders. Alternatively, consider making the Payment Condition active only for an employees-only sales channel so that the payment method can be tested prior to going live.
10. Return to `Payments > Settings` and click the `Payment Conditions` tab at the top of the screen, and then the green + button in the upper right corner to create a new Payment Condition. Choose `PayPalCP` from the list of payment methods. Verify that the condition is set to process with the affiliation that you named in step 8 and that the toggle is set to `Active`. Click `Save`.

### PayPal Smart Payment Buttons Configuration

11. In your VTEX admin dashboard, return to `Payments > PayPal`.
12. In the PayPal Settings section, adjust the Smart Payment Buttons layout and appearance settings as desired.
    - You may also disable the PayPal Credit "Pay Later" button here, if desired. If you are not in a region where PayPal Credit is available, this setting will have no effect.
    - You may also enable Immediate Capture here, if desired. If enabled, PayPal payments will be captured immediately at time of checkout. Behind the scenes, the PayPal order is created using `intent: 'CAPTURE'` rather than `intent: 'AUTHORIZE'`. This setting must be enabled if you are a merchant located in Brazil or Mexico and wish to offer PayPal payments in installments.
13. If you are ready to enable the Smart Payment Buttons for your store users, activate the `Show PayPal Buttons` toggle and click `Save`.
14. The PayPal Smart Payment Buttons will now appear on the Checkout Cart page, directly below the standard `Checkout` button (or, if using customization, wherever the block has been placed).

### PayPal Additional App Configurations

- **Invoice ID** - Choose which value to use as the `invoice_id` in PayPal orders. Default is set to VTEX order sequence (reference) number.
- **Custom ID** - Choose which value to use as the `custom_id` in PayPal orders. Default is set to VTEX order ID.

### PayPal Credit Promotional Messaging

To display [PayPal Credit promotional messaging](https://www.paypal.com/merchantapps/appcenter/accelerategrowth/paylatermessaging?locale.x=en_US) on your PDP and/or product shelves, simply modify your store-theme to place the `product-installments` block in the desired location. This block is provided by the core [Product Price](https://developers.vtex.com/docs/apps/vtex.product-price) app, so no change to your store-theme's dependencies should be needed. When the PayPal app is installed in the same account, it will automatically fill the `product-installments` block with PayPal's messaging.

> ⚠️ Note that promotional messaging will not be displayed if you have chosen to disable the PayPal Credit Smart Payment Button, or if the `product-installments` block is not present in your store-theme.

## Customization

If your store does not have Checkout Cart installed, or if you wish to display the PayPal Smart Payment Buttons in another place, such as within the minicart, you may follow these instructions:

1. Install this app in your account (see step 1 of [Installation & Onboarding](#configuration) above).
2. Modify your store-theme's `manifest.json` file to add this app to its `peerDependencies` like so:

```json
"peerDependencies": {
    "vtex.connector-paypal-commerce-platform": "0.x"
  },
```

3. Modify the JSON within your store-theme's `store` folder to place the block `"one-click-buy.paypal-checkout-button"` in the desired location. The block accepts no props.
4. Continue following the [Installation & Onboarding](#configuration) instructions from step 3.

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://developers.vtex.com/docs/guides/vtex-io-documentation-using-css-handles-for-store-customization).

| CSS Handles                      |
| -------------------------------- |
| `payPalButtonContainer`          |
| `payPalErrorModal`               |
| `payPalProcessingModal`          |
| `payPalPayLaterMessageContainer` |
