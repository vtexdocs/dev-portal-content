---
title: "How to set up functions in the Message Center templates"
slug: "how-to-set-up-functions-in-the-message-center-templates"
hidden: false
createdAt: "2021-10-15T15:21:14.824Z"
updatedAt: "2022-02-10T20:58:11.681Z"
---

The purpose of this article is to present the most used commands and all the functions that can be used to boost your store’s email templates using Message Center.

To configure its templates, Message Center uses a language called Handlebars, with a few commands that make it easy to implement while expanding its customization.

When editing the email template on VTEX Admin, in **Store Settings** > **Email Templates** > **Templates**, it is possible to use a range of variables provided by the system. To use these variables in the email layout, you must follow this syntax using Handlebars: `{{class.attribute}}`. The `{{class.attribute}}` is obtained using the JSON Data field.

>⚠️ Always configure transactional email templates relying on the information retrieved by the [Get Order API](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-).

Check out the following example in which the template uses the `HostName` information from the JSON Data:

**HTML email template:**

```html
<strong>{{_accountInfo.HostName}}</strong>
```

**Example JSON Data:**

```json
"_accountInfo": { 
  "HostName": "lojadosuporte" 
}
```

**Result**: **lojadosuporte**

![exemplo html](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-to-set-up-functions-in-the-message-center-templates-0.png)

The above example can have different values when comparing Sellers and Marketplaces.

## Functions

The use of the functions follows the syntax `{{function class.attribute}}`.

Consider the following JSON Data example to understand the available functions, described in the table below.

**Example JSON Data:**

```json
"items": [ 
  { 
    "name": "Product A", 
    "sellingPrice": 20000, 
    "priceValidUntil": "2050-05-30T21:00:00Z", 
    "deliveryTime": "8bd" 
  }, 
  {
    "name": "Product B", 
    "sellingPrice": 3000, 
    "priceValidUntil": "2050-09-23T11:00:00Z", 
    "deliveryTime": "10d" 
  } 
]
```

| Function | Description | Example syntax | Example result |
| - | - | - | - |
| `formatCurrency` |  Formats a value as currency, separating decimal values with a comma `,`. | `{{formatCurrency items.0.sellingPrice}}` | 200,00 |
| `formatUSDCurrency` | Formats a value as currency, separating decimal values with a dot `.`. | `{{formatUSDCurrency items.0.sellingPrice}}` | 200.00 |
| `formatCurrencyWithoutDecimals` | Formats a value as currency without decimal values. | `{{formatCurrencyWithoutDecimals items.0.sellingPrice}}` | 200 |
| `multiplyCurrency` | Formats a value as currency and multiplies it by a number. This function has the following syntax: `{{formatCurrency class.attribute multiplier}}` | `{{formatCurrency items.0.sellingPrice 4}}` | 800,00 |
| `formatDate` | Formats a date as `dd/mm/yyyy`. | `{{formatDate items.0.priceValidUntil}}` | 30/05/2050 |
| `formatUSDate` | Formats a date as `mm/dd/yyyy`. | `{{formatUSDate items.0.priceValidUntil}}` | 05/30/2050 |
| `formatDateTime` | Formats a date  as `dd/mm/yyyy hh:mm:ss`. | `{{formatDateTime items.0.priceValidUntil}}` | 30/05/2050 21:00:00 |
| `formatDateUtc` | Formats a date as `dd/mm/yyyy mh:mm:ss` and converts it to the local UTC | `{{formatDateUtc items.0.priceValidUntil}}` | 30/05/2050 18:00:00 |
| `replace` | Replaces a given value with another. This function has the following syntax: `{{replace class.attribute "previous value" "new value"}}` | `{{replace deliveryTime "bd" " business days"}}` | 8 business days |

> If necessary, you should add currency symbols — such as `$` or `R$` — directly on the template, since they are not automatically retrieved by functions.

## Example

**Handlebars code:**

```handlebars
{{#each items}} 
{{name}} 
Entrega{{#each ../shippingData.logisticsInfo}} 
{{#eq itemId ../id}} 
{{#each slas}} 
{{#eq ../selectedSla id}} 
{{#if deliveryWindow}} 
agendada entre{{formatDateTime deliveryWindow.startDateUtc}} e {{formatDateTime deliveryWindow.endDateUtc}} 
{{else}} 
em até{{#hasSubStr shippingEstimate 'bd'}} 
{{replace shippingEstimate 'bd' ' dias úteis.'}} 
{{else}} 
{{replace shippingEstimate 'd' ' dias.'}} 
{{/hasSubStr}} 
{{/if}} 
{{/eq}} 
{{/each}} 
{{/eq}} 
{{/each}} 
{{quantity}}x R$ {{formatCurrency sellingPrice}} 
{{/each}}
```

**Result:**
![result-example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/how-to-set-up-functions-in-the-message-center-templates-1.png)
