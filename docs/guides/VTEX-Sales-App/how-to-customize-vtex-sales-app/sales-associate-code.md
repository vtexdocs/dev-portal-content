---
title: "Enable the sales associate code"
slug: "sales-associate-code"
excerpt: "Learn how to enable the sales associate code."
hidden: false
createdAt: "2021-03-26T16:37:08.694Z"
updatedAt: "2025-09-30T15:21:12.126Z"
---

>⚠️ The sales associate code is enabled by default for stores that start using the VTEX Sales App. This article is intended for stores that may have disabled this field due to customizations. To retrieve the sales associate code, use the [Get order](https://developers.vtex.com/docs/api-reference/orders-api-pii-version#get-/api/orders/pvt/document/-orderId-) endpoint and check the `salesAssociateId` value inside the `merchantContextData` object.

The sales associate code field is an additional customization of the [**Observation** field](https://developers.vtex.com/vtex-rest-api/docs/enable-the-remarks-field-in-the-order-screen) that turns this component into a field where vendors should insert their code during the purchase flow.

Once enabled, this field becomes a mandatory step in the purchase flow, meaning that the order can only be completed if the `sales associate code` field is filled with a personal code.

![The VTEX Sales App's UI once the sales rep code is enabled on the purchase flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/sales-associate-code-0.PNG)

## Prerequisites

Before customizing the **sales associate code** field, you must enable the **Observation** field on VTEX Sales App. Check [this article](https://developers.vtex.com/vtex-rest-api/docs/enable-the-remarks-field-in-the-order-screen) to learn how to do that.

## Edit the `checkout-instore-custom.js` file

After enabling the **Observation** field, you should [configure the sales associate code](https://help.vtex.com/en/tracks/vtex-sales-app-customizations--1z9kBm12oBPyVNDo1ivVc2/5kNtS80hbBGg58jMeF8CRv) by editing the `checkout-instore-custom.js` file.

You can configure the JavaScript file according to your needs, using different value combinations for the three properties: `type`, `skipValidation`, and `mask`.

```json
{
  "data": {
    "0-0": "`type`",
    "1-0": "`skipValidation`",
    "2-0": "`mask`",
    "h-0": "Property",
    "0-1": "string",
    "0-2": "Defines the ‘vendors’ field format. The possible values are `text` and `textarea`, for big text blocks. `input`, a text field for simple keys. `select`, showing a combobox to quickly select.",
    "1-1": "boolean",
    "2-2": "A regular variable expression that applies a validation logic to the type property value. In other words, the person responsible for editing the `window.INSTORE_CONFIG` object can create the variable expression they find most appropriate for the sales rep code.",
    "1-2": "Activates the validation performed via Master Data.",
    "2-1": "string",
    "h-2": "Description",
    "h-1": "Type",
    "3-0": "`autofill`",
    "3-1": "boolean",
    "3-2": "Defines whether VTEX Sales App will automatically insert the sales associate code when the Social Selling feature is active.\n\nWhen this value is `true` (default), the vendor code is automatically filled by VTEX Sales App.\n\nWhen this value is `false`, the operator must inform the vendor code manually.\n\nThis flag does not change any behavior when Social Selling is not activated."
  },
  "cols": 3,
  "rows": 4
}
```

[block:callout]
{
  "type": "danger",
  "title": "Condition for the customization",
  "body": "Even though all properties are not mandatory, the JavaScript file must have at least one of them described in the code.\n\nOtherwise, the customization will fail."
}
[/block]
To fill the `mask` field, you must create a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions). As the sales associate code is built on JavaScript, your regular expression should follow the same programming language as well.

In VTEX, the JavaScript regular expressions follow the ECMAScript flavor. Check the step-by-step guide to constructing a regular expression according to this pattern in the [Mozilla documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp).
[block:callout]
{
  "type": "info",
  "title": "Test the regular expression",
  "body": "Once the regular expression is complete, a pro tip is to analyze the mask field functioning on a test workspace before deploying the code on the master. We recommend testing it on [Regular Expressions 101](https://regex101.com/)."
}
[/block]

### Example code

[block:code]
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = {\n  noteAsVendorCode: {\n    type: 'input',\n    skipValidation: true,\n    mask: '^(HE|TU)[A-Za-z0-9]{5,8}$',\n    autofill: false,\n  },\n}",
      "language": "javascript",
      "name": "JavaScript"
    }
  ]
}
[/block]

### Use cases

- <strong>Validation according to sales associate’s document ID</strong>: in this example, the regular expression applied in the mask expresses that the code has three numbers and two letters.
[block:code]
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = {\n  noteAsVendorCode: {\n       type: 'text',\n       skipValidation: true,\n       mask: '^\\\\d{3}[a-zA-Z]{2}$',\n       autofill: false,\n   },\n}",
      "language": "javascript"
    }
  ]
}
[/block]
- **Validation only on Master Data**: the following regular expression doesn't have any mask applied on the JS file, which means that the system will proceed with the Master Data's validation.
[block:code]
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = {\n  noteAsVendorCode: {\n       type: 'text',\n       skipValidation: false,\n    \t autofill: false,\n   },\n}",
      "language": "javascript"
    }
  ]
}
[/block]
- **Validation according to the mask only**: in this example, the regular expression applied in the mask expresses that the code has two numbers.
[block:code]
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = {\n  noteAsVendorCode: {\n       type: 'text',\n       skipValidation: true,\n       mask: '^\\\\d{2}$',\n    \t autofill: false,\n   },\n}",
      "language": "javascript"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "Get in touch",
  "body": "In case of doubt, contact Customer Excellence by creating a [support ticket](https://help.vtex.com/en/tutorial/abrir-chamados-para-o-suporte-vtex--16yOEqpO32UQYygSmMSSAM)."
}
[/block]
