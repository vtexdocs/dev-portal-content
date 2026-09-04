---
title: "Layout development guide for payment methods in VTEX Smart Checkout"
slug: "layout-development-guide-for-payment-methods-in-smart-checkout-vtex"
excerpt: "Learn how to build, test, and submit the checkout interface of a new payment method using Payment Mocker."
hidden: false
createdAt: "2021-12-29T19:47:24.134Z"
updatedAt: "2026-09-03T00:00:00.000Z"
---

This guide is intended for those responsible for integrating new payment methods into VTEX Smart Checkout. Besides integrating with the PCI Gateway, integrators must provide a user interface (UI) that aligns with the visual identity of the payment method being presented.

> ⚠️ All layout updates made through this guide only apply to [Checkout v6](https://help.vtex.com/pt/docs/tutorials/ativar-o-checkout-v6).

When shoppers select a payment method at checkout, they express their interest in using it. For this reason, the layout must communicate briefly and clearly how the payment method works and what its advantages are. Information such as contact details, like a phone number or email address, can also help shoppers solve any problem or question at the time of purchase.

The following sections describe the requirements for a payment method layout, how to develop it with [Payment Mocker](https://github.com/vtex/payment-mocker), and how to submit it to VTEX.

> ℹ️ You can't create a new layout for custom payment methods, which are those developed by the merchant that only work in their own stores, such as notes payable, co-branded cards, or private label cards.

## Before you begin

Before developing your layout, make sure you meet the following requirements:

| Requirement | Description |
| ----------- | ----------- |
| Payment provider integration | Your payment provider must be integrated with VTEX, as described in [Integrating a new payment provider on VTEX](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex). |
| Checkout version | The store must use [Checkout v6](https://help.vtex.com/pt/docs/tutorials/ativar-o-checkout-v6), as layout updates don't apply to other versions. |
| Development environment | [Node.js](https://nodejs.org/en/download) and npm installed on your machine, plus a [Git](https://git-scm.com/downloads) client to clone the Payment Mocker repository. |
| Front-end knowledge | Familiarity with HTML, CSS, and [LESS](https://lesscss.org/), since Payment Mocker compiles the layout styles from a LESS file. |

## Layout requirements

### User interface: Structure and code

#### Bootstrap framework

The Smart Checkout code is based on Bootstrap v2.3.2 standards. You can use classes such as `grid` and `alignment` to structure the HTML and CSS code.

> ⚠️ Bootstrap v2.3.2 classes differ significantly from those of later Bootstrap versions. Refer to the [Bootstrap v2.3.2 documentation](https://getbootstrap.com/2.3.2/) when structuring your layout.

#### CSS and LESS

The styling code can be written to be interpreted by LESS, the CSS preprocessor used by Payment Mocker. When writing that code, the following rules are mandatory:

- Global selectors that can interfere with the structure or other elements of the page aren't permitted.
- IDs can't be used as selectors, except for the Smart Checkout selectors already declared in Payment Mocker, as explained in [Development](#development).
- A maximum of two nested selectors is permitted.
- All classes must be in English, with lowercase letters and words separated by a hyphen, such as `.my-payment-method`.

We also recommend using only classes as selectors.

#### Responsiveness

Your layout must render correctly on the following screen sizes:

- **Desktop and horizontal tablet**: Width greater than or equal to 768 pixels. The container is 462 pixels wide, and its height can vary between 200 and 330 pixels, depending on the content.
- **Vertical tablet and mobile**: Width less than 768 pixels. The container takes up 100% of the width, with a margin of 30 pixels and padding of 15 pixels.

> ℹ️ You can freely use additional breakpoints.

### User interface: Design and elements

#### Color and images

Colors and images can follow the visual identity of the payment method, without restrictions. Images must be optimized and grouped into a single file, using the CSS sprites technique.

#### Typography

Following the Bootstrap pattern, Smart Checkout adopts the following fonts, in this order:

- Helvetica Neue
- Helvetica
- Arial
- Sans Serif

> ℹ️ We don't recommend using other fonts. If another font is strictly necessary, it must be part of the standard system package, as importing new fonts isn't possible.

#### Scripts and links

Scripts and links aren't essential for completing the purchase, as they distract shoppers and may even take them out of the checkout.

> ⚠️ Using scripts and links isn't permitted.

All content available in the checkout area must be informative only. The checkout button must be the only call to action presented on the screen.

### Internationalization

All texts must be written in:

- **en-US**: US English. This language is mandatory.
- **Other languages**: The languages of the countries or regions where you intend to operate, if they aren't English-speaking. See the [ISO 639-1 standard language codes](https://www.andiamo.co.uk/resources/iso-language-codes/).

Besides localizing texts, images must be adapted to suit each language.

## Development

> ⚠️ Use [Payment Mocker](https://github.com/vtex/payment-mocker) to test how your layout renders within VTEX Smart Checkout and ensure the expected behavior.

Follow these steps to create your layout:

1. Download the [Payment Mocker repository](https://github.com/vtex/payment-mocker) to your local machine, either by cloning it with Git or by downloading it as a ZIP file.

   ![Payment Mocker repository page on GitHub, with the Code button expanded and the Download ZIP option available.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/layout-development-guide-for-payment-methods-in-smart-checkout-vtex-0.png)

2. Install [Node.js](https://nodejs.org/en/download).
3. In the terminal, run the following commands to install Grunt and Sass:

   - **Grunt**: `npm i -g grunt-cli`
   - **Sass**: `npm i -g sass`

   > ℹ️ On macOS and Linux, global installations may require `sudo` or a Node version manager such as [nvm](https://github.com/nvm-sh/nvm). On Windows, run the commands in PowerShell or Command Prompt without `sudo`.

4. Still in the terminal, go to the project folder and run `npm i` to install the project dependencies.
5. Run `grunt` in the project folder.
6. Open your preferred browser and go to `http://localhost:8080`.
7. Modify the following files according to the requirements described in [User interface: Structure and code](#user-interface-structure-and-code):

   - *src/partials/payment.html*: Insert the HTML structure of your layout in this file. When adding information about a new payment method, replace the `newpayment` text in the file with the name of the payment method you created. For example, when creating the SafetyPay payment method, replace `newpayment` with `safetypay`.

     > ⚠️ Use lowercase letters and separate words with hyphens when replacing `newpayment`, as required by the class naming rule in [CSS and LESS](#css-and-less). For example, use `payment-safetypay-title`, not `payment-SafetyPay-title`.

   - *src/assets/css/less/style.less*: Insert the classes responsible for styles, spacing, fonts, and other CSS customizations of your layout in this file. Remember to follow the guidelines described in [Layout requirements](#layout-requirements).
   - *src/assets/img*: Insert all images used in your layout in this folder and reference them from your styles.
   - *src/i18n*: This folder contains four files, each one corresponding to one language: `pt-BR`, `en-US`, `es`, and `fr`. Change the values of the keys in these files and check whether the languages render correctly by clicking the flags in the upper left corner of Payment Mocker, as shown in [Layout example](#layout-example).

8. Open the *src/assets/css/less/style.less* file, find the `#payment-group-template-PaymentGroup .payment-group-item-text` rule, and update its `background-image` attribute to insert the icon of your payment method.

   > ℹ️ This rule overrides a selector that Smart Checkout already declares, so it's the only case where you edit an ID selector. This isn't an exception to the rule that forbids creating new ID selectors, described in [CSS and LESS](#css-and-less).

   > ⚠️ If you don't change the `background-image` attribute, no icon renders next to the payment method label.

9. Open the *src/i18n/{language}.json* file and change the value of the `paymentData.paymentGroup.title` key to customize the label of your payment method at checkout.

   > ℹ️ If you don't change the value of the `paymentData.paymentGroup.title` key, the payment method renders with the default label.

   > ⚠️ If the name chosen for your new payment method is the same as or similar to an existing payment method on the VTEX platform, you can't register it. To check the payment methods already registered, in the VTEX Admin, go to **Store Settings > Payments > Settings > Payment Conditions**.

## Delivery

To deliver your code, compress the Payment Mocker repository containing all modifications related to your payment method into a `.zip` or `.rar` file, and submit it by opening a ticket at the [VTEX Support Portal](https://help.vtex.com/support).

> ⚠️ Before compressing the repository, delete any files or folders created during the build process, such as the *node_modules* folder or the *yarn.lock* file, if you use the Yarn package manager.

After submission, VTEX reviews the layout against the requirements described in this guide and returns any feedback through the same support ticket. Once the layout is approved, VTEX publishes it for Checkout v6. Follow the ticket for status updates and requests for adjustments.

## Layout example

The following images show an example of a layout and language switching for payment methods in VTEX Smart Checkout.

> ℹ️ Manual language switching is only available in Payment Mocker, for testing purposes. Once the layout is deployed, Checkout switches the language automatically.

![Custom payment method layout rendered in the payment step of VTEX Smart Checkout, showing the method title, description, and benefits.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/layout-development-guide-for-payment-methods-in-smart-checkout-vtex-1.png)

![Animation showing the language switcher in Payment Mocker changing the texts of the payment method layout.](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/layout-development-guide-for-payment-methods-in-smart-checkout-vtex-2.gif)

## Learn more

- [Payment Mocker: HTML structure](https://github.com/vtex/payment-mocker/blob/master/src/partials/payment.html)
- [Payment Mocker: Styles](https://github.com/vtex/payment-mocker/blob/master/src/assets/css/less/style.less)
- [Payment Mocker: Internationalization](https://github.com/vtex/payment-mocker/tree/master/src/i18n)
- [Integrating a new payment provider on VTEX](https://developers.vtex.com/docs/guides/integrating-a-new-payment-provider-on-vtex)
- [Payment App](https://developers.vtex.com/docs/guides/payments-integration-payment-app)
