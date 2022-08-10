---
title: "Get Computed Price by price table"
slug: "getcomputedpricebypricetable"
excerpt: "Gets a computed Price (Price after all steps in pricing pipeline) for an SKU in a specific Trade Policy (or Price Table)"
hidden: false
createdAt: "2019-12-30T17:39:05.877Z"
updatedAt: "2020-02-27T16:56:10.955Z"
---
`sellingPrice` is the computed price before applying coupons/taxes/benefits (this may change before reaching the  shelf)

`listPrice` is the *"from"* price (this may change before reaching the shelf)

`priceValidUntil` represents the next time this price will change, due to some scheduling. If no scheduling is present, this will be set a year from the current time.



> know more about [Price Tables in VTEX Help](https://help.vtex.com/en/announcement/from-now-on-you-can-create-promotional-price-tables)


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `itemId` | string | SKU Id |
| `priceTableId` | integer | SKU Price Table Id |
| `categoryId` | integer | Category Id |
| `brandId` | integer | Brand Id |
| `quantity` | integer | SKU quantity |





For example, in case you need get calculated price from SKU Id `9997`, on Price Table `1`, Category `99`, Brand Id `79` and Quantity `5`  .

You will have to replace the variables `itemId` for `9997`, `priceTableId` for `1`, `categoryId` for `99`, `brandId` for `79` and `quantity` for `5` :

```
https://teststore.myvtex.com/api/pricing/prices/9997/computed/1?categoryIds=[99]&brandId=79&quantity=5
```




## Response object has the following properties:


| Attribute    | Type        | Description |
| ------------ |:-----------:| -----------:|
| `tradePolicyId` | string | Trade Policy Id |
| `listPrice` | integer | Trade Policy List Price Value |
| `sellingPrice` | integer | Computed Price Value |
| `priceValidUntil` | string | Computed Price End Date |




## Authentication


This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)