---
title: "Get Fixed Prices"
slug: "getfixedprices"
excerpt: "Fixed Prices are a sub resource of Prices. This method get an array of Fixed Prices for an SKU in a Trade Policy with Minimum Quantities"
hidden: false
createdAt: "2019-12-30T17:39:05.877Z"
updatedAt: "2020-02-13T14:24:45.328Z"
---
*Fixed Prices* are a sub resource of Prices. This method get an array of Fixed Prices for an SKU in a Trade Policy with Minimum Quantities.

The default value for a *Minimum Quantity* is `1`. This means a Fixed Price will be valid for a SKU in a Trade Policy for orders containing the specified number of *Minimum Quantity* or above, unless a higher *Minimum Quantity* is specified.

Fixed prices may, *optionally*, be scheduled. If so, these objects will contain a property `dateRange` with `from` and `to`, indicating the starting and ending time of the scheduled fixed price in the *RFC3339* timestamp format (`YYYY-MM-DDT23:59:60Z`). 
Note that the 'Z', at the end, represents the UTC time (GMT+00:00).
If it was in GMT-03:00, for example, it would be (`YYYY-MM-DDT23:59:60-03:00`)

> know more about [Prices in VTEX Help](https://help.vtex.com/en/tutorial/prices-v2)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `itemId` | string | SKU Id |


For example, in case you need get fixed price from SKU Id `9997` .

You will have to replace the variables `itemId` for `9997`:

```
https://api.vtex.com/teststore/pricing/prices/9997/fixed
```




## Response object has the following properties:


| Attribute    | Type        | Description |
| ------------ |:-----------:| -----------:|
| `tradePolicyId` | string | Trade Policy Id |
| `value` | integer | Trade Policy Fixed Price Value |
| `listPrice` | integer | Trade Policy List Price Value |
| `minQuantity` | integer |  Trade Policy Fixed Price Minimum Item Quantity |
| `dateRange` | object | Trade Policy Fixed Price Validity Period Object |
| `from` | string | Validity start Date |
| `to` | string | Validity end Date |




## Authentication


This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)