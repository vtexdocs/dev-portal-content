---
title: "How to set up functions in the Message Center templates"
slug: "how-to-set-up-functions-in-the-message-center-templates"
hidden: false
createdAt: "2021-10-15T15:21:14.824Z"
updatedAt: "2022-02-10T20:58:11.681Z"
---
The purpose of this article is to present the most used commands and all the functions that can be used to boost your store’s templates.

To configure its templates, Message Center uses a language called **HandleBars**, which is quite simple, with only a few commands, making it easy to implement while expanding its customization.

When editing the email, it is possible to use a range of variables provided by the system. Use of these variables in the email layout has the following Handlebars syntax: `{{class.attribute}}`. The `classe.atributo` is obtained using the JSON Data field.
[block:callout]
{
  "type": "warning",
  "body": "The JSON attributes are the same for every VTEX store, however, the values may differ depending on the way you configured your store. So it is important to remember to configure your store relying on the info displayed by the [Get Order API](https://developers.vtex.com/vtex-rest-api/reference/getorder) of your store."
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "\"_accountInfo\": { \n  \"HostName\": \"lojavirtual\" \n}",
      "language": "json"
    }
  ]
}
[/block]
**Template HTML:** `<strong>{{_accountInfo.HostName}}</strong> => lojavirtual`
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b9d5c9b-exemplohtml.png",
        "exemplohtml.png",
        1209,
        214,
        "#f4f4f6"
      ]
    }
  ]
}
[/block]
The above example can have different values when comparing Sellers and Marketplaces.

## Functions

The use of the functions follows the following syntax: `{{funcão classe.atributo}}`
[block:code]
{
  "codes": [
    {
      "code": "\"items\": [ \n  { \n    \"name\": \"Produto A\", \n    \"sellingPrice\": 20000, \n    \"priceValidUntil\": \"2050-05-30T21:00:00Z\", \n    \"deliveryTime\": \"8bd\" \n  }, \n  {\n    \"name\": \"Produto B\", \n    \"sellingPrice\": 3000, \n    \"priceValidUntil\": \"2050-09-23T11:00:00Z\", \n    \"deliveryTime\": \"10d\" \n  } \n]",
      "language": "json"
    }
  ]
}
[/block]
- **formatCurrency**: formats a value for currency `{{formatCurrency items.0.sellingPrice}}`
  - **Result:** R$ 200,00
- **formatUSDCurrency:** formats a value for the american decimal pattern `{{formatUSDCurrency items.0.sellingPrice}}`
  - **Result:** $ 200.00
- **formatCurrencyWithoutDecimals:** formats a value for the currency without the decimal places `{{formatCurrencyWithoutDecimals items.0.sellingPrice}}`
  - **Result:** R$ 200
- **multiplyCurrency:** formats a value for currency and multiplies it by a value This function has the following syntax: `{{formatCurrency classe.atributo multiplicador}}`  `{{formatCurrency items.0.sellingPrice 4}}`
  - **Result:** R$ 800,00
- **formatDate:** formats a date to its (`dd/mm/yyyy`) default value `{{formatDate items.0.priceValidUntil}}`
  - **Result:** 30/05/2050
- **formatDateTime:** formats a date to its (`dd/mm/yyyy hh:mm:ss`) value `{{formatDateTime items.0.priceValidUntil}}`
  - **Result:** 30/05/2050 21:00:00
- **formatDateUtc:** formats the date to its (`dd/mm/yyyy mh:mm:ss`) default value and converts it to the local UTC `{{formatDateUtc items.0.priceValidUntil}}`
  - **Result:** 30/05/2050 18:00:00 (-3h, for example)
- **replace:** its function is to replace a given value with another This function has the following syntax: `{{replace classe.atributo "Valor Substituído" "Valor Novo"}}` `{{replace deliveryTime "bd" " dias úteis"}}`
  - **Result:** 8 business days

## Example
[block:code]
{
  "codes": [
    {
      "code": "{{#each items}} \n{{name}} \nEntrega{{#each ../shippingData.logisticsInfo}} \n{{#eq itemId ../id}} \n{{#each slas}} \n{{#eq ../selectedSla id}} \n{{#if deliveryWindow}} \nagendada entre{{formatDateTime deliveryWindow.startDateUtc}} e {{formatDateTime deliveryWindow.endDateUtc}} \n{{else}} \nem até{{#hasSubStr shippingEstimate 'bd'}} \n{{replace shippingEstimate 'bd' ' dias úteis.'}} \n{{else}} \n{{replace shippingEstimate 'd' ' dias.'}} \n{{/hasSubStr}} \n{{/if}} \n{{/eq}} \n{{/each}} \n{{/eq}} \n{{/each}} \n{{quantity}}x R$ {{formatCurrency sellingPrice}} \n{{/each}}",
      "language": "handlebars"
    }
  ]
}
[/block]
**Result:**
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/715c58d-3.1.jpg",
        "3.1.jpg",
        582,
        173,
        "#f2f2f1"
      ]
    }
  ]
}
[/block]