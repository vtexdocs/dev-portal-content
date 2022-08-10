---
title: "Order Configuration"
slug: "vtex-order-configuration"
excerpt: "vtex.order-configuration@3.3.1"
hidden: false
createdAt: "2020-08-07T17:26:01.522Z"
updatedAt: "2022-03-21T17:10:43.606Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The **Order Configuration** app, designed for B2B scenarios, displays a form responsible for collecting order data in a modal.

![order-configuration-gif](https://user-images.githubusercontent.com/52087100/91925199-e5125200-ecaa-11ea-8734-f98921ddb384.gif)


Once the form is submitted, the order data collected will be available at Master Data and saved in the current VTEX session.

> ℹ This app can be used to enable customization of all kinds of behaviors, such as custom prices, custom products, etc. Keep in mind the Order Configuration app does not offer these functionalities, it only enables other apps to do so.

Follow the steps below to install and set up the **Order Configuration** app in your store.

### Step 1: Install the app

 First, you must add the `order-configuration` app to your theme's dependencies in the `manifest.json` file:

```json
dependencies: {
  "vtex.order-configuration": "2.x"
}
```

This will enable you to use the blocks exported by the `order-configuration` app. Check out the full list below:

| Block name     | Description                                     |
| -------------- | ----------------------------------------------- |
| `order-config` | Parent block only responsible for rendering its children blocks, that in turn build the Order Configuration component. |
| `order-config.title` | Renders the component title, that is, the message text displayed for users to present the component. On the image above, the component title is `Order Configuration`. |
| `order-config.modal` | Renders the modal responsible for displaying the component content. |
| `order-config.form` | Renders the component content, that is, a form to be filled out by users.  |


### Step 2: Declare the required blocks

Add the `order-config` block in the Header component, as shown in the example below.

```json
{
  "header-layout.desktop": {
    "children": [
      "flex-layout.row#1-desktop",
      "flex-layout.row#2-desktop",
      "flex-layout.row#3-desktop",
      "sticky-layout#4-desktop"
    ]
  },
  "flex-layout.row#3-desktop": {
    "props": {
      "blockClass": "menu-link",
      "horizontalAlign": "center",
      "preventHorizontalStretch": true,
      "preventVerticalStretch": true,
      "fullWidth": true
    },
    "children": [
      "vtex.menu@2.x:menu#websites",
      "flex-layout.col#spacer",
+     "order-config#header",
      "vtex.menu@2.x:menu#institutional"
    ]
  },
```

Then, declare the `order-config#header` block and its children blocks: `order-config.title` and `order-config.modal`. Example:

```json
{
  "order-config#header": {
    "children": [
      "order-config.title#header",
      "order-config.modal#header"
    ],
    "props": {
      "blockClass": "header",
      "formFields": [
        {
          "name": "orderType",
          "type": "string",
          "fieldType": "radio",
          "label": "Order Type",
          "defaultValue": "resale",
          "options": [
            {
              "label": "Resale",
              "value": "resale"
            },
            {
              "label": "Consumption",
              "value": "consumption"
            }
          ]
        },
        {
          "name": "state",
          "type": "string",
          "fieldType": "select",
          "label": "State",
          "showInTitle": true,
          "options": [
            {
              "label": "ES",
              "value": "ES"
            },
            {
              "label": "SP",
              "value": "SP"
            }
          ]
        }
      ]
    }
  },
  "order-config.modal#header": {
    "children": [
      "order-config.form"
    ]
  },
  "order-config.title#header": {
    "props": {
      "formTitle": "Order Configuration for Header"
    }
  },
}
```

> ℹ If the `order-config.form` block does not have any children configured, a default form will be rendered automatically based on the [React Hook Form JSON Schema](https://github.com/vtex/react-hook-form-jsonschema) library. To declare children blocks according to your business needs, check out the [Advanced configuration](#advanced-configuration) section below.

### Step 3: Create `main` schema in Master Data

You must create a schema named `main` in Master Data, using the `order_configuration` data entity.

You can place a request using the Save schema by name endpoint of the [Master Data API - v2](https://developers.vtex.com/vtex-rest-api/reference/schemas#saveschemabyname) to do so.

The schema should contain all the data that you added in the form above, otherwise the data will not be persisted.

#### Request body example

```json
{
    "v-cache": false,
    "properties": {
        "clientId": {
            "type": "string"
        },
        "orderType": {
            "type": "string"
        },
        "state": {
            "type": "string"
        }
    },
    "v-default-fields": [
        "clientId",
        "orderType",
        "state"
    ],
    "v-indexed": [
        "clientId",
        "orderType",
        "state"
    ]
}
```

Refer to [Master Data API - v2 documentation](https://developers.vtex.com/vtex-rest-api/reference/schemas#saveschemabyname) for more details.

### Step 4: Update orderForm configuration

It is also necessary to configure a new app in the `orderForm`.

First, place a `GET` [Get orderForm configuration](https://developers.vtex.com/vtex-developer-docs/reference/getorderformconfiguration) request to retrieve the current `orderForm` settings before updating them. By doing so you ensure that you will only change the properties you want in the next step.

Then, place a `POST` [Update orderForm configuration](https://developers.vtex.com/vtex-developer-docs/reference/updateorderformconfiguration) request, setting the following object inside the `apps` object in the request body:

```json
        {
            "fields": [
                "values"
            ],
            "id": "orderconfig",
            "major": 1
        }
```

#### Request body example

```json
{
    "paymentConfiguration": {
        "requiresAuthenticationForPreAuthorizedPaymentOption": false,
        "allowInstallmentsMerge": null,
        "blockPaymentSession": null,
        "paymentSystemToCheckFirstInstallment": null,
        "defaultPaymentSystemToApplyOnUserOrderForm": null
    },
    "taxConfiguration": null,
    "minimumQuantityAccumulatedForItems": 1,
    "decimalDigitsPrecision": 2,
    "minimumValueAccumulated": null,
    "apps": [
        {
            "fields": [
                "quoteId"
            ],
            "id": "b2b-quotes-graphql",
            "major": 1
        },
        {
            "fields": [
                "values"
            ],
            "id": "orderconfig",
            "major": 1
        }
    ],
    "allowMultipleDeliveries": true,
    "allowManualPrice": true,
    "maxNumberOfWhiteLabelSellers": null,
    "maskFirstPurchaseData": null,
    "recaptchaValidation": "vtexcriteria",
    "maskStateOnAddress": true
}
```

You can refer to [Checkout API documentation](https://developers.vtex.com/vtex-developer-docs/reference/updateorderformconfiguration) for more information.


### Advanced configuration

If desired, you can declare the `order-config.form` block by adding and configuring the `formFields` prop and an array of form children blocks (whose descriptions you can find below).

```json
{
  "order-config#static-page": {
    "props": {
      "formFields": [
        {
          "name": "orderType",
          "type": "string",
          "fieldType": "select",
          "label": "Order Type",
          "defaultValue": "res",
          "showInTitle": true,
          "options": [
            {
              "label": "Resale",
              "value": "res"
            },
            {
              "label": "Consumption",
              "value": "cons"
            }
          ]
        },
        {
          "name": "state",
          "type": "string",
          "fieldType": "select",
          "label": "State",
          "showInTitle": true,
          "required": true,
          "options": [
            {
              "label": "ES",
              "value": "ES"
            },
            {
              "label": "SP",
              "value": "SP"
            }
          ]
        },
        {
          "name": "someTextInput",
          "label": "Some Text Input",
          "fieldType": "input",
          "type": "string",
          "required": true,
          "showInTitle": true
        }
      ]
    },
    "children": [
      "order-config.title#static-page",
      "order-config.form#static-page"
    ]
  },
  "order-config.form#static-page": {
    "children": [
      "flex-layout.row#state-and-payment-method",
      "order-config.text#some-text-input",
      "order-config.submit"
    ]
  },
  "flex-layout.row#state-and-payment-method": {
    "children": [
      "order-config.dropdown#state",
      "order-config.radiogroup#payment-method"
    ],
    "props": {
      "blockClass": "stateAndPaymentMethod"
    }
  },
  "order-config.dropdown#state": {
    "props": {
      "pointer": "#/properties/state"
    }
  },
  "order-config.radiogroup#payment-method": {
    "props": {
      "pointer": "#/properties/paymentMethod"
    }
  },
  "order-config.text#some-text-input": {
    "props": {
      "pointer": "#/properties/someTextInput"
    }
  },
  "order-config.title#static-page": {
    "props": {
      "formTitle": "Order Configuration for Static Page"
    }
  }
}
```

| Block name     | Description                                     |
| -------------- | ----------------------------------------------- |
| `order-config.submit` | Renders a `Submit` button. |
| `order-config.dropdown` | Renders the a dropdown field. |
| `order-config.radiogroup` | Renders a radiogroup field. |
| `order-config.text` | Renders a text field. |
| `order-config.textarea` | Renders a text field with a wider range of available characters. |
| `order-config.checkbox` | Renders a checkbox field. |

#### Props

Check out the description of the available props below.

| Prop name | Type | Description  | Default Value | Block name |
| --------- | -------- | ------------| ----------------- | -------- | 
| `pointer`  | `string` | Path to which the block must point in the `formFields` prop in order to properly work.  | `undefined`              | `order-config.dropdown`, `order-config.radiogroup`, `order-config.text`, `order-config.textarea`, and `order-config.checkbox` |
| `formFields`  | `object` | Object responsible for defining the form fields.  | `undefined`              | `order-config.form`  |

The `formFields` object contains the following props:

| Prop name | Type | Description                                                                                                                                                                                                                                          | Default Value  |
| --------| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `name` | `string` |  Name of the field (only used as an identifier in your code). | `undefined`              |
| `type` | `enum` |  Value type accepted by the field. Possible values are `string` and `number`. | `string`              |
| `fieldType` | `enum` | Input type accepted by the field. Possible values are: `text`, `textarea`, `select`, `radio`, and `checkbox`. | `text`              |
| `label` | `string` | Field name shown to users. | `undefined` |
| `showInTitle` | `boolean` |  Whether to display the value type accepted by the field on its name (`true`) or not (`false`). | `false`  |
| `options` | `object` | Field options to be defined in case `select`, `radio`, or `checkbox` values were declared in the `fieldType` prop. | `undefined`  |

The `options` object contains the following props:

| Prop name   | Type                                 | Description                                                   | Default Value |
| ----------- | ----------------------------------------- | -------------------------------------------------------------------------------------- | ----------------- |
| `label` | `string` | Option name shown to users. | `undefined`           |
| `value` | `string` | Option value. | `undefined`           |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles |
| ----------- |
| `formSubmitButton` |
| `formSubmitContainer` |
| `formErrorServer` |
| `formErrorUserInput` |
| `loader` |
| `orderConfigFormWrapper` |
| `formObject` |
| `title` |
| `titleValues` |
| `titleWrapper` |
| `wrapper` |

<!-- DOCS-IGNORE:start -->
## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->