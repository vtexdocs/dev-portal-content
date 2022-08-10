---
title: "Order Placed"
slug: "zaffarilab-order-placed"
excerpt: "zaffarilab.order-placed@2.18.1"
hidden: true
createdAt: "2022-07-08T19:22:50.462Z"
updatedAt: "2022-07-28T17:29:03.705Z"
---
<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Configuration](#configuration)
- [Blocks](#blocks)
  - [`order-placed`](#order-placed-1)
  - [`op-section`](#op-section)
  - [`op-header`](#op-header)
  - [`op-footer`](#op-footer)
  - [`op-confirmation-icon`](#op-confirmation-icon)
  - [`op-confirmation-title`](#op-confirmation-title)
  - [`op-confirmation-message`](#op-confirmation-message)
  - [`op-print-button`](#op-print-button)
  - [`op-notices`](#op-notices)
  - [`op-summary-section`](#op-summary-section)
  - [`op-bank-invoice-section`](#op-bank-invoice-section)
  - [`op-order`](#op-order)
  - [`op-order-number`](#op-order-number)
  - [`op-order-datetime`](#op-order-datetime)
  - [`op-order-seller`](#op-order-seller)
  - [`op-order-split-notice`](#op-order-split-notice)
  - [`op-order-customer`](#op-order-customer)
  - [`op-order-options`](#op-order-options)
  - [`op-order-payment`](#op-order-payment)
  - [`op-order-delivery-packages`](#op-order-delivery-packages)
  - [`op-order-pickup-packages`](#op-order-pickup-packages)
  - [`op-order-total`](#op-order-total)
- [API](#api)
- [Customization](#customization)
- [Contributing](#contributing)
- [Contributors ✨](#contributors)

<!-- /code_chunk_output -->

## Configuration

The `order-placed` app comes already installed on all stores and with it, it's possible to build your own page with the blocks exported by the app.

After defining a `order-placed` block inside your `store/blocks` directory or in your `blocks.json` file, the page can be constructed with [blocks](#blocks) and customized with [css handles](#css-handles).

_Note: this is the default `order-placed` layout implementation._

```jsonc
// store/blocks/order-placed.jsonc
{
  "order-placed": {
    "blocks": ["op-header", "op-order"]
  },
  "op-header": {
    "children": [
      "op-section#confirmation",
      "op-section#notices",
      "op-summary-section",
      "op-bank-invoice-section"
    ]
  },
  "op-section#confirmation": {
    "props": {
      "name": "confirmation",
      "marginBottom": 9,
      "borderless": true
    },
    "children": [
      "op-confirmation-icon",
      "op-confirmation-title",
      "op-confirmation-message",
      "flex-layout.row#confirmation-buttons"
    ]
  },
  "flex-layout.row#confirmation-buttons": {
    "props": {
      "blockClass": "confirmationButtons",
      "marginTop": 8,
      "marginBottom": 8,
      "horizontalAlign": "center",
      "preventHorizontalStretch": true
    },
    "children": ["flex-layout.col#confirmation-buttons"]
  },
  "flex-layout.col#confirmation-buttons": {
    "children": ["op-print-button"]
  },
  "op-section#notices": {
    "props": {
      "name": "notices",
      "marginBottom": 9,
      "borderless": true
    },
    "children": ["op-notices"]
  },
  // each order section
  "op-order": {
    "children": [
      "flex-layout.row#order-header",
      "op-order-split-notice",
      "op-order-customer",
      "op-section#payments",
      "op-section#pickup-packages",
      "op-section#delivery-packages",
      "op-order-takeaway-packages",
      "op-order-total"
    ]
  },
  // each order header
  "flex-layout.row#order-header": {
    "props": {
      "fullWidth": true,
      "colSizing": "auto",
      "colGap": 5,
      "marginBottom": 5
    },
    "children": [
      "flex-layout.col#order-header-info",
      "flex-layout.col#order-header-options"
    ]
  },
  "flex-layout.col#order-header-info": {
    "children": ["op-order-number", "op-order-datetime", "op-order-seller"]
  },
  "flex-layout.col#order-header-options": {
    "children": ["responsive-layout.desktop#order-options-desktop"]
  },
  "responsive-layout.desktop#order-options-desktop": {
    "children": ["op-order-options"]
  },
  // payment section
  "op-section#payments": {
    "props": {
      "name": "paymentMethods"
    },
    "children": [
      "op-order-payment",
      "responsive-layout.mobile#order-options-mobile"
    ]
  },
  // bottom of top section of order header
  "responsive-layout.mobile#order-options-mobile": {
    "children": ["op-order-options#mobile"]
  },
  "op-order-options#mobile": {
    "props": {
      "blockClass": "mobile",
      "fullWidth": true
    }
  },
  "op-section#pickup-packages": {
    "props": {
      "name": "pickupPackages"
    },
    "children": ["op-order-pickup-packages"]
  },
  "op-section#delivery-packages": {
    "props": {
      "name": "deliveryPackages"
    },
    "children": ["op-order-delivery-packages"]
  }
}
```

Make sure you have the Order Placed page defined in your theme:

```json
  "store.orderplaced": {
    "children": ["order-placed"]
  },
```

## Blocks

### `order-placed`

Main block, responsible for rendering the whole order placed page. It accepts the following blocks:

- [`op-header`](#op-header)
- [`op-order`](#op-order)
- [`op-footer`](#op-footer)

### `op-section`

Splits your page into separate and semantic sections.

**Composition:**
Accepts an array of any kind of children blocks.

**Props:**

| Prop name       | Type                                             | Description                                                    | Default value |
| --------------- | ------------------------------------------------ | -------------------------------------------------------------- | ------------- |
| `borderless`    | `MaybeResponsiveInput<boolean>` &#124; `boolean` | Remove the bottom border of the section                        | `false`       |
| `marginBottom`  | `MaybeResponsiveInput<number>` &#124; `number`   | Margin space below the section                                 | `0`           |
| `paddingBottom` | `MaybeResponsiveInput<number>` &#124; `number`   | Padding space below the section                                | `0`           |
| `width`         | `MaybeResponsiveInput<string>` &#124; `string`   | Width of the section                                           | `100%`        |
| `name`          | `string`                                         | Name of the section. Use it to have custom css handles for it. | `undefined`   |

**CSS Handles:**

| CSS Handles       | Description          |
| ----------------- | -------------------- |
| `section`         | All section blocks   |
| `section--{name}` | Section named `name` |

### `op-header`

Defines the header content of the page.

**Composition:**
Accepts an array of any kind of children blocks.

**Props:** none.

**CSS Handles:**

| CSS Handles         | Description     |
| ------------------- | --------------- |
| `orderPlacedHeader` | The page header |

### `op-footer`

Defines the footer content of the page.

**Composition:**
Accepts an array of any kind of children blocks.

**Props:** none.

**CSS Handles:**

| CSS Handles         | Description     |
| ------------------- | --------------- |
| `orderPlacedFooter` | The page footer |

### `op-confirmation-icon`

Renders the confirmation icon.

**Composition:** none.

**Props:** none.

**CSS Handles:**

| CSS Handle                | Description  |
| ------------------------- | ------------ |
| `confirmationIconWrapper` | Icon wrapper |

| Default appearance                                         |
| ---------------------------------------------------------- |
| ![op-confirmation-icon](https://user-images.githubusercontent.com/17712401/89224372-c38c5080-d5ae-11ea-8112-9870c854e5a2.png) |

### `op-confirmation-title`

Renders the confirmation title.

**Composition:** none.

**Props:** none.

**CSS Handles:**

| CSS Handle          | Description                     |
| ------------------- | ------------------------------- |
| `confirmationTitle` | Confirmation title `h4` element |

| Default appearance                                           |
| ------------------------------------------------------------ |
| ![op-confirmation-title](https://user-images.githubusercontent.com/17712401/89224442-df8ff200-d5ae-11ea-824a-25d7530249dd.png) |

### `op-confirmation-message`

Renders the confirmation message, containing the clients email.

**Composition:** none.

**Props:** none.

**CSS Handles:**

| CSS Handle            | Description                      |
| --------------------- | -------------------------------- |
| `confirmationMessage` | Confirmation message `p` element |

| Default appearance                                               |
| ---------------------------------------------------------------- |
| ![op-confirmation-message](https://user-images.githubusercontent.com/17712401/89224480-f0406800-d5ae-11ea-8602-0cb9541b0459.png) |

### `op-print-button`

Renders a button that triggers a full page print.

**Composition:** none.

**Props:** none.

**CSS Handles:**: none.

| Default appearance                 |
| ---------------------------------- |
| ![op-print](https://user-images.githubusercontent.com/17712401/89224547-0817ec00-d5af-11ea-9b6a-9ae33a89daef.png) |

### `op-notices`

Renders a list of important informations relevant to the currently placed order. The messages may vary according to the type of order.

**Composition:** none.

**Props:** none.

**CSS Handles:**

| CSS Handle       | Description                 |
| ---------------- | --------------------------- |
| `noticesList`    | List `ul` element           |
| `noticeListItem` | Each list `li` item element |

| Default appearance                     |
| -------------------------------------- |
| ![op-notices](https://user-images.githubusercontent.com/17712401/89224594-16fe9e80-d5af-11ea-9c3e-4cfddcf76a4c.png) |

### `op-summary-section`

If a placed order is split between delivery and pickup, renders a summary of all pickup and delivery packages with informations such as number of items, packages, pickup/delivery address and pickup/delivery SLA.

**Composition:** none.

**Props:** none.

**CSS Handles:**

| CSS Handle             | Description                                 |
| ---------------------- | ------------------------------------------- |
| `section--summary`     | Summary whole section                       |
| `summaryRow`           | Row wrapper of both summary boxes           |
| `summaryCol`           | Column wrapper of each summary box          |
| `summaryAddress`       | Wrapper of the pickup address               |
| `summaryBox`           | Surrounding box of the summary              |
| `summaryBox--delivery` | Surrounding box of the delivery summary     |
| `summaryBox--pickup`   | Surrounding box of the pickup summary       |
| `summaryContent`       | Wrapper of the whole content of the box     |
| `summaryItems`         | Wrapper of the number of items and packages |
| `summaryShippingSLA`   | Wrapper of the shipping SLA information     |
| `summaryTitle`         | Box `h5` title element                      |

| Default appearance                                     |
| ------------------------------------------------------ |
| ![op-summary-section](https://user-images.githubusercontent.com/17712401/89224626-267de780-d5af-11ea-80c1-7771c6dae670.png) |

### `op-bank-invoice-section`

Renders the bank invoice section if payment method chosen was bank invoice.

**Composition:** none.

**Props:** none.

**CSS Handles:**

| CSS Handle                   | Description                                   |
| ---------------------------- | --------------------------------------------- |
| `section--bankInvoice`       | Bank invoice whole section                    |
| `barCodeWrapper`             | Wrapper of the barcode number and copy button |
| `barCodeNumber`              | Barcode number element                        |
| `barCodeCopyButtonWrapper`   | Wrapper of the copy button                    |
| `bankInvoiceEmbedWrapper`    | Wrapper of the bank invoice iframe            |
| `bankInvoiceEmbedBackground` | Background of the bank invoice iframe         |
| `bankInvoiceEmbed`           | Embed of the bank invoice PDF                 |

| Default appearance                                               |
| ---------------------------------------------------------------- |
| ![op-bank-invoice-section](https://user-images.githubusercontent.com/17712401/89224654-3695c700-d5af-11ea-9b17-98c68450370d.png) |

### `op-order`

Defines an order context to be able to render its meta information and packages. Must be used to display order data.

**Composition:**
Accepts an array of any kind of children blocks.

**Props:** none.

**CSS Handles:**

| CSS Handle     | Description                                       |
| -------------- | ------------------------------------------------- |
| `orderWrapper` | Wrapper of an order meta information and packages |

### `op-order-number`

Renders the order id number. Must be placed inside an [`op-order`](#op-order) block.

**Composition:** none.

**Props:** none.

**CSS Handles:**

| CSS Handle    | Description               |
| ------------- | ------------------------- |
| `orderNumber` | Order number `h3` element |

| Default appearance                               |
| ------------------------------------------------ |
| ![op-order-number](https://user-images.githubusercontent.com/17712401/89224695-4c0af100-d5af-11ea-866e-bea733073346.png) |

### `op-order-datetime`

Renders the date and time an order was placed. Must be placed inside an [`op-order`](#op-order) block.

**Composition:** none.

**Props:** none.

**CSS Handles:**

| CSS Handle      | Description                         |
| --------------- | ----------------------------------- |
| `orderDatetime` | Order date and time `small` element |

| Default appearance                                   |
| ---------------------------------------------------- |
| ![op-order-datetime](https://user-images.githubusercontent.com/17712401/89224728-5a590d00-d5af-11ea-8901-7654c543d9e9.png) |

### `op-order-seller`

Renders the seller of an order. Must be placed inside an [`op-order`](#op-order) block.

**Composition:** none.

**Props:** none.

**CSS Handles:**

| CSS Handle    | Description                   |
| ------------- | ----------------------------- |
| `orderSoldBy` | Seller phrase `small` element |
| `orderSeller` | Seller name `span` element    |

| Default appearance                               |
| ------------------------------------------------ |
| ![op-order-seller](https://user-images.githubusercontent.com/17712401/89224779-765cae80-d5af-11ea-9320-29902e7f47dd.png) |

### `op-order-split-notice`

Renders a message with the number of packages of an order if the order was split in more than one package. Must be placed inside an [`op-order`](#op-order) block.

**Composition:** none.

**Props:** none.

**CSS Handles:**

| CSS Handle    | Description                    |
| ------------- | ------------------------------ |
| `splitNotice` | Wrapper of the message element |

| Default appearance                                           |
| ------------------------------------------------------------ |
| ![op-order-split-notice](https://user-images.githubusercontent.com/17712401/89224825-88d6e800-d5af-11ea-8801-7f2d5267da5b.png) |

### `op-order-customer`

Renders the customer information. Must be placed inside an [`op-order`](#op-order) block.

**Composition:** none.

**Props:** none.

**CSS Handles:** none.

| Default appearance                                   |
| ---------------------------------------------------- |
| ![op-order-customer](https://user-images.githubusercontent.com/17712401/89224880-a015d580-d5af-11ea-8314-bc223b3da0aa.png) |

### `op-order-options`

Renders the customer information. Must be placed inside an [`op-order`](#op-order) block.

**Composition:** none.

**Props:**

| Prop name   | Type      | Description                                         | Default value |
| ----------- | --------- | --------------------------------------------------- | ------------- |
| `fullWidth` | `boolean` | Make the options wrapper take full horizontal space | `false`       |

**CSS Handles:**

| CSS Handles           | Description                   |
| --------------------- | ----------------------------- |
| `orderOptionsWrapper` | Wrapper of the option buttons |

| Default appearance                                 |
| -------------------------------------------------- |
| ![op-order-options](https://user-images.githubusercontent.com/17712401/89224923-b754c300-d5af-11ea-8b28-0efa82329e96.png) |

### `op-order-payment`

Renders the customer information. Must be placed inside an [`op-order`](#op-order) block.

**Composition:** none.

**CSS Handles:**

| CSS Handles           | Description                         |
| --------------------- | ----------------------------------- |
| `orderPaymentWrapper` | Wrapper of the payment methods list |
| `orderPaymentItem`    | Wrapper of each payment method item |

| Default appearance                                 |
| -------------------------------------------------- |
| ![op-order-payment](https://user-images.githubusercontent.com/17712401/89225037-eec36f80-d5af-11ea-82af-267cb69c7d7b.png) |

### `op-order-delivery-packages`

Renders an order delivery packages information and product list. Must be placed inside an [`op-order`](#op-order) block.

**Composition:** none.

**CSS Handles:**

| CSS Handles               | Description                                    |
| ------------------------- | ---------------------------------------------- |
| `package`                 | All package sections                           |
| `package--delivery`       | The delivery package section                   |
| `packageHeaderColumn`     | Column of header of a package section          |
| `packageHeader`           | Header of a package section                    |
| `packageHeader--delivery` | Header of the delivery package section         |
| `packageShippingEstimate` | Delivery estimate `small` element              |
| `packageAddressWrapper`   | Wrapper of the package shipping address        |
| `packageAddressTitle`     | Wrapper of the address title                   |
| `packageDeliveryTitle`    | Wrapper of the delivery title                  |
| `productList`             | Product list `ul` element                      |
| `productListItem`         | Product list `li` item element                 |
| `productWrapper`          | Wrapper of a single product                    |
| `productImageColumn`      | Column of a product's image                    |
| `productImageWrapper`     | Wrapper of a product's image                   |
| `productInfoColumn`       | Column of a product's information              |
| `productName`             | Product's `a` element                          |
| `productMeasurementUnit`  | Product's measurement unit `small` element     |
| `productQuantity`         | Product's quantity `small` element             |
| `productPrice`            | Product's price                                |
| `attachmentWrapper`       | Wrapper for a product's attachment             |
| `attachmentHeader`        | Header of an attachment                        |
| `attachmentTitle`         | Title of a attachment                          |
| `attachmentToggleWrapper` | Wrapper of the toggle button of an attachment  |
| `attachmentToggleButton`  | Button for toggling the attachment's accordion |
| `attachmentToggleLabel`   | Attachment's toggle label                      |
| `attachmentContent`       | Attachment's content wrapper                   |
| `attachmentContentItem`   | Each attachment's content paragraph            |

| Default appearance                                                     |
| ---------------------------------------------------------------------- |
| ![op-order-delivery-packages](https://user-images.githubusercontent.com/17712401/89225054-f8e56e00-d5af-11ea-9c0a-b2cc37fe34f4.png) |

### `op-order-pickup-packages`

Renders an order pickup packages information and product list. Must be placed inside an [`op-order`](#op-order) block.

**Composition:** none.

**CSS Handles:**

_Note: Include the same CSS handles as [`op-order-delivery-packages`](#op-order-delivery-packages)_

| CSS Handles             | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| `package`               | All package sections                                         |
| `package--pickup`       | The pickup package section                                   |
| `packageInfoWrapper`    | Wrapper of a **pickup** package's information                |
| `packageReceiver`       | Package's **pickup** receiver information container          |
| `packageReceiverName`   | Name of the package's **pickup** receiver                    |
| `packageAdditionalInfo` | Wrapper of additional information about a **pickup** package |

| Default appearance                                                 |
| ------------------------------------------------------------------ |
| ![op-order-pickup-packages](https://user-images.githubusercontent.com/17712401/89225074-03076c80-d5b0-11ea-840e-69998a41ec9d.png) |

### `op-order-total`

Renders an order delivery packages information and product list. Must be placed inside an [`op-order`](#op-order) block.

**Composition:** none.

**CSS Handles:**

| CSS Handles          | Description                                 |
| -------------------- | ------------------------------------------- |
| `totalListWrapper`   | Wrapper of the total price list of an order |
| `totalList`          | An order's total list `ul` element          |
| `totalListItem`      | An order's total item `li` element          |
| `totalListItemLabel` | Label of a price item                       |
| `totalListItemValue` | Value of a price item                       |

| Default appearance                             |
| ---------------------------------------------- |
| ![op-order-total](https://user-images.githubusercontent.com/17712401/89225092-0b5fa780-d5b0-11ea-976e-da3c64453eff.png) |

## API

The `order-placed` app exports two hooks to allow customization using the current order data: `useOrderGroup` and `useOrder`.

`useOrderGroup`: used to get the data of the current order group. An order group is the collection of all orders created by an users's purchase.

```js
import { useOrderGroup } from 'vtex.order-placed/OrderGroupContext'

//...
const orderGroup = useOrderGroup()
```

`useOrder`: used to get the data of the current order being accessed in the order loop.

```js
import { useOrder } from 'vtex.order-placed/OrderContext'

//...
const order = useOrder()
```

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                  |
| ---------------------------- |
| `attachmentContent`          |
| `attachmentContentItem`      |
| `attachmentHeader`           |
| `attachmentTitle`            |
| `attachmentToggleButton`     |
| `attachmentToggleLabel`      |
| `attachmentToggleWrapper`    |
| `attachmentWrapper`          |
| `bankInvoiceEmbed`           |
| `bankInvoiceEmbedBackground` |
| `bankInvoiceEmbedWrapper`    |
| `barCodeCopyButtonWrapper`   |
| `barCodeContainer`           |
| `barCodeNumber`              |
| `barCodeWrapper`             |
| `confirmationIconWrapper`    |
| `confirmationMessage`        |
| `confirmationTitle`          |
| `errorMessage`               |
| `errorTitle`                 |
| `errorWrapper`               |
| `noticeListItem`             |
| `noticesList`                |
| `orderDatetime`              |
| `orderList`                  |
| `orderListItem`              |
| `orderNumber`                |
| `orderOptionsWrapper`        |
| `orderPaymentItem`           |
| `orderPaymentWrapper`        |
| `orderPlacedFooter`          |
| `orderPlacedHeader`          |
| `orderPlacedMainWrapper`     |
| `orderPlacedWrapper`         |
| `orderSeller`                |
| `orderSoldBy`                |
| `orderWrapper`               |
| `package--delivery`          |
| `package--pickup`            |
| `package`                    |
| `packageAdditionalInfo`      |
| `packageAddressWrapper`      |
| `packageGiftDescription`     |
| `packageHeader--delivery`    |
| `packageHeader--pickup`      |
| `packageHeader`              |
| `packageHeaderColumn`        |
| `packageInfoWrapper`         |
| `packageReceiver`            |
| `packageReceiverName`        |
| `packageShippingEstimate`    |
| `packageSLA`                 |
| `printButtonWrapper`         |
| `printHintWrapper`           |
| `productImageColumn`         |
| `productImageWrapper`        |
| `productInfoColumn`          |
| `productName`                |
| `productListItem`            |
| `productList`                |
| `productMeasurementUnit`     |
| `productPrice`               |
| `productQuantity`            |
| `productWrapper`             |
| `section--bank-invoice`      |
| `section--confirmation`      |
| `section--deliveryPackages`  |
| `section--notices`           |
| `section--paymentMethod`     |
| `section--pickupPackages`    |
| `section--summary`           |
| `section`                    |
| `splitNotice`                |
| `summaryRow`                 |
| `summaryCol`                 |
| `summaryAddress`             |
| `summaryBox--delivery`       |
| `summaryBox--pickup`         |
| `summaryBox`                 |
| `summaryContent`             |
| `summaryItems`               |
| `summaryShipping`            |
| `summaryTitle`               |
| `totalList`                  |
| `totalListItem`              |
| `totalListItemLabel`         |
| `totalListItemValue`         |
| `totalListWrapper`           |

## Contributing

Check it out [how to contribute](https://github.com/vtex-apps/awesome-io#contributing) with this project.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/gustavopvasconcellos"><img src="https://avatars1.githubusercontent.com/u/49173685?v=4?s=100" width="100px;" alt=""/><br /><sub><b>gustavopvasconcellos</b></sub></a><br /><a href="https://github.com/vtex-apps/order-placed/commits?author=gustavopvasconcellos" title="Code">💻</a></td>
    <td align="center"><a href="https://razvanudrea.com"><img src="https://avatars.githubusercontent.com/u/71461884?v=4?s=100" width="100px;" alt=""/><br /><sub><b>razvanudream</b></sub></a><br /><a href="https://github.com/vtex-apps/order-placed/commits?author=razvanudream" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/claudiu-iviteb"><img src="https://avatars.githubusercontent.com/u/73105476?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Claudiu Ionita</b></sub></a><br /><a href="https://github.com/vtex-apps/order-placed/commits?author=claudiu-iviteb" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!