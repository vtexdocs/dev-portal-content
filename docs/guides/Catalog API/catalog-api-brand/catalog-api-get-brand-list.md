---
title: "Get Brand List"
slug: "catalog-api-get-brand-list"
excerpt: "Retrieves all Brands registered in the store's Catalog."
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2022-02-03T14:43:25.132Z"
---
## Response object has the following properties:


| Attribute    | Type        | Description |
| --------------- |:---------:| -------------------------------------------------------------------------------------------:|
| `id` | integer | ID of the Brand |
| `name` | string      |  Name of the Brand  |
| `imageUrl`  | string | Category Image URL |
| `isActive` | boolean    | If the Brand is active  |
| `title` | string | Meta Title for the Brand page |
| `metaTagDescription` | string | Meta Description for the Brand page |




## Authentication

This is a private API which needs credentials with viewer access.

> Learn more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)