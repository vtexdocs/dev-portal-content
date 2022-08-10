---
title: "Get rules for a price table"
slug: "createrulesforapricetable"
excerpt: "This method will retrieve the rules from a specific Price Table. It will delete all the rules from the requested Price Table and create new rules based on the content of the request"
hidden: false
createdAt: "2019-12-30T17:39:05.877Z"
updatedAt: "2020-03-02T17:21:16.239Z"
---
A price table rule is a configuration that allows the user to specify different percentual modifiers for every price in that price table for an specific context.

| Attribute      |  Type  |    Description |
|----------------|:------:|---------------:|
| `priceTableId` | string | Price Table ID |



| Attribute    | Type       | Description |
| --------------- |:-----------:|:------------:| ------------------------------------------------------------------------------|
| `tradePolicyId` | string | Trade Policy ID (Price Table ID) |
| `rules` | object| Array of rules to be created for this price table |
|⮡  &nbsp;`id` | integer | Rule Id |
|&nbsp; &nbsp`percentualModifier` | integer | Percentual value of the price variation to be applied |
| &nbsp; &nbsp`context` | object | Rule Context is a group of filters to be checked at an item level when applying the rule. If all those filters check out, the rule will be applied for that item, unless there is a fixed price for that item |
| &nbsp; &nbsp;     ⮡  &nbsp; `categories` | object | Categories that an item should have to be eligible for the rule. Format: key: `categoryId`, value: `categoryName`  |
|  &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp;  ⮡  &nbsp; `brands` | object | Brands that an item should have to be eligible for the rule. Format: key: `brandId`, value: `brandName` |
|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; `markupRange` | object | For an item to be eligible to the rule, it's markup should be in this Markup Range |
|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  ⮡  &nbsp; `from` | float |  Item markup should be greater than or equal to this value |
|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp;  `to` | float |  Item markup should be less than or equal to this value |
|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; `dateRange` | object | The rule will be active during this time range |
|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  ⮡  &nbsp`from` | string |  First date that rule will be active. Date format: `RFC3339` |
|&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp;   `to` | string | Last date that the rule will be active. Date format: `RFC3339` |


#### Response codes
201 - Success

401 - Unauthorized request

403 - The credentials is not enabled to access the service

429 - Too many requests