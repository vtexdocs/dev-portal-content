---
title: "Tax Fallback API"
slug: "vtex-tax-fallback"
excerpt: "vtex.tax-fallback@0.0.5"
hidden: true
createdAt: "2022-07-27T16:25:53.486Z"
updatedAt: "2022-07-27T16:25:53.486Z"
---
This app's API provides tax tables that can be used for simple tax calculation when a dynamic tax calculation is not available. New tax tables are downloaded every 4 weeks.

You do not need to install this app in your account. It is installed in the `vtexus` account and other apps can send requests to its API there.

To retrieve taxes for a given postal code, your app can send a GET request to the following URL:

### https://vtexus.myvtex.com/_v/tax-fallback/{country}/{provider}/{postalCode}

| URL Param    |   Type   |            Description             |   Supported Values   |
| ------------ | :------: | :--------------------------------: | :------------------: |
| `country`    | `string` |     Destination country (ISO2)     |         `us`         |
| `provider`   | `string` |         Tax table provider         |      `avalara`       |
| `postalCode` | `string` | Destination postal code (5 digits) | (any US postal code) |

Example request:

`GET https://vtexus.myvtex.com/_v/tax-fallback/us/avalara/14617`

Example response:

```json
{
  "id": "13a3e885-1496-11eb-8374-12b3893429c7",
  "date": "2020-10-26",
  "ZIP_CODE": "14617",
  "STATE_ABBREV": "NY",
  "COUNTY_NAME": "MONROE",
  "CITY_NAME": "ROCHESTER",
  "STATE_SALES_TAX": 0.04,
  "STATE_USE_TAX": 0.04,
  "COUNTY_SALES_TAX": 0.04,
  "COUNTY_USE_TAX": 0.04,
  "CITY_SALES_TAX": 0,
  "CITY_USE_TAX": 0,
  "TOTAL_SALES_TAX": 0.08,
  "TOTAL_USE_TAX": 0.08,
  "TAX_SHIPPING_ALONE": true,
  "TAX_SHIPPING_AND_HANDLING_TOGETHER": true
}
```