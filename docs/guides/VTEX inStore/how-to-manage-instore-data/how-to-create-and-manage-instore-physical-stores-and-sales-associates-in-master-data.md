---
title: "Create and manage physical stores and sales associates in Master Data"
slug: "how-to-create-and-manage-instore-physical-stores-and-sales-associates-in-master-data"
hidden: false
createdAt: "2021-08-04T20:29:56.258Z"
updatedAt: "2022-02-24T20:44:34.927Z"
---
inStore is VTEX’s core product for Unified Commerce operations. It allows your store to deliver a real omnichannel experience by seamlessly integrating your online and in-store channels and having your clients in the core of your business.

When setting inStore in your business, you might need to add physical stores and sales associates to the system, as well as managing existing stores and sales associates. You can do this by using VTable, as described in [this article](https://help.vtex.com/en/tracks/instore-setting-up--zav76TFEZlAjnyBVL5tRc/5PSjRstg7UU4lOm0s8aqKN), or you can use the [Master Data API - V2](https://developers.vtex.com/vtex-developer-docs/reference/documents), as described below.

[block:html]
{
  "html": "<br>"
}
[/block]
## Stores

[block:html]
{
  "html": "<br>"
}
[/block]
### Create a store

If you want to create a new physical store on inStore, you should use the [Create or update entire document](https://developers.vtex.com/vtex-developer-docs/reference/createorupdateentiredocument) endpoint with the params listed below.

| **Param** | **Value**|
|---|---|
| `data_entity_name` | `stores` |
| `_schema` | `v1` |

The request body should have the following properties:

| **Attribute** | **Type** | **Description** |
|---|---|---|
| `name` | string | Store name |
| `mobileNumber` | string | Store phone number |
| `pickupPoint` | string | Store pickup point ID number |
| `franchiseAccount` | string | Franchise account name |
| `postalCode` | string | Store postal code |
| `tradePolicy` | string | Trade Policy’s unique numerical identifier |
| `country` | string | Country code |
| `state` | string | State where the store is located |
| `city` | string | City where the store is located |
| `neighborhood` | string | Neighborhood where the store is located |
| `address` | string | Street where the store is located |
| `number` | string | Street number of the store |
| `complement` | string | Complementary information to the store’s address |

Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"Botafogo Store\",\n  \"mobileNumber\": \"9999999999\",\n  \"pickupPoint\": \"1098765\",\n  \"franchiseAccount\": \"franchise1\",\n  \"postalCode\": \"222222\",\n  \"tradePolicy\": \"1\",\n  \"country\": \"BRA\",\n  \"state\": \"Rio de Janeiro\",\n  \"city\": \"Rio de Janeiro\",\n  \"neighborhood\": \"Botafogo\",\n  \"address\": \"Praia de Botafogo\",\n  \"number\": \"300\",\n  \"complement\": \"3rd floor\"\n}",
      "language": "json"
    }
  ]
}
[/block]
When the request is successful, the response is a `json` schema including a new `DocumentId` attribute, which represents the store ID number:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": \"stores-16aa42c4-f489-11eb-82ac-0ea70a628d87\",\n    \"Href\": \"http://accountname.vtexcommercestable.com.br/api/dataentities/stores/documents/16aa42c4-f489-11eb-82ac-0ea70a628d87?_schema=v1\",\n    \"DocumentId\": \"16aa42c4-f489-11eb-82ac-0ea70a628d87\"\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:html]
{
  "html": "<br>"
}
[/block]

### Update store information

To update store information, you can use the same request you would use to [Create a store](#create-a-store), but including the `id` field in the request body and changing any attribute you want:

| **Attribute** | **Type** | **Description** |
|---|---|---|
| `id` | string | Store `DocumentId` value, which represents the store ID number |

Request body example (changing the `mobileNumber`):
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"id\": \"16aa42c4-f489-11eb-82ac-0ea70a628d87\",\n  \"name\": \"Botafogo Store\",\n  \"mobileNumber\": \"888888888\",\n  \"pickupPoint\": \"1098765\",\n  \"franchiseAccount\": \"franchise1\",\n  \"postalCode\": \"222222\",\n  \"tradePolicy\": \"1\",\n  \"country\": \"BRA\",\n  \"state\": \"Rio de Janeiro\",\n  \"city\": \"Rio de Janeiro\",\n  \"neighborhood\": \"Botafogo\",\n  \"address\": \"Praia de Botafogo\",\n  \"number\": \"300\",\n  \"complement\": \"3rd floor\"\n}",
      "language": "json"
    }
  ]
}
[/block]
Response body example:  
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": \"stores-16aa42c4-f489-11eb-82ac-0ea70a628d87\",\n    \"Href\": \"http://accountname.vtexcommercestable.com.br/api/dataentities/stores/documents/16aa42c4-f489-11eb-82ac-0ea70a628d87?_schema=v1\",\n    \"DocumentId\": \"16aa42c4-f489-11eb-82ac-0ea70a628d87\"\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:html]
{
  "html": "<br>"
}
[/block]
### Find a store

In case you need to find an existing physical store to check their ID or other information, you should use the [Search documents](https://developers.vtex.com/vtex-developer-docs/reference/searchdocuments) endpoint. You can use any other query params you want in this request.

| **Param** | **Value** |
|---|---|
| `data_entity_name` | `stores` |
| `_schema` | `v1` |

[block:html]
{
  "html": "<br>"
}
[/block]
### Delete a store

In order to delete a physical store and remove its data in Master Data, you should use the [Delete document](https://developers.vtex.com/vtex-developer-docs/reference/deletedocument) endpoint.

| **Param** | **Value** |
|---|---|
| `data_entity_name` | `stores` |
| `id` | Store `DocumentId` value, which represents the store ID number |


[block:html]
{
  "html": "<br>"
}
[/block]
## Sales associates

[block:html]
{
  "html": "<br>"
}
[/block]
### Create a sales associate

If you want to create a new sales associate on inStore, you should use the [Create or update entire document](https://developers.vtex.com/vtex-developer-docs/reference/createorupdateentiredocument) endpoint. Using this request, you will give the sales associate access to inStore and automatically give them the inStore Sales Person role in your account.

| **Param** | **Value**|
|---|---|
| `data_entity_name` | `vendors` |
| `_schema` | `v1` |

The request body should have the following properties:

| **Attribute** | **Type** | **Description** |
|---|---|---|
| `name` | string | Sales associate name |
| `user` | string | User email |
| `code` | string | Sales associate code (optional) |
| `store` | string | Store `DocumentId` value, which represents the store ID number |

Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"Jane Doe\",\n  \"user\": \"jane@email.com\",\n  \"code\": \"123456\",\n  \"store\": \"16aa42c4-f489-11eb-82ac-0ea70a628d87\"\n}",
      "language": "json"
    }
  ]
}
[/block]
When the request is successful, the response is a `json` including a new `DocumentId` attribute, which represents the sales associate ID number: 
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": \"vendors-d74145dc-f494-11eb-82ac-1271e6f73475\",\n    \"Href\": \"http://accountname.vtexcommercestable.com.br/api/dataentities/vendors/documents/d74145dc-f494-11eb-82ac-1271e6f73475?_schema=v1\",\n    \"DocumentId\": \"d74145dc-f494-11eb-82ac-1271e6f73475\"\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:html]
{
  "html": "<br>"
}
[/block]
### Update sales associate information

To update sales associate information, you can use the same request you would use to [Create a sales associate](#create-a-sales-associate), but including the `id` field in the request body:

| **Attribute** | **Type** | **Description** |
|---|---|---|
| `id` | string | Sales associate `DocumentId` value, which represents the sales associate ID number |

Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"id\": \"d74145dc-f494-11eb-82ac-1271e6f73475\",\n  \"name\": \"Jane Doe\",\n  \"user\": \"jane.doe@email.com\",\n  \"code\": \"123456\",\n  \"store\": \"16aa42c4-f489-11eb-82ac-0ea70a628d87\",\n}",
      "language": "json"
    }
  ]
}
[/block]
Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": \"vendors-d74145dc-f494-11eb-82ac-1271e6f73475\",\n    \"Href\": \"http://accountname.vtexcommercestable.com.br/api/dataentities/vendors/documents/d74145dc-f494-11eb-82ac-1271e6f73475?_schema=v1\",\n    \"DocumentId\": \"d74145dc-f494-11eb-82ac-1271e6f73475\"\n}",
      "language": "json"
    }
  ]
}
[/block]

[block:html]
{
  "html": "<br>"
}
[/block]
### Find a sales associate

In case you need to find an existing sales associate to check their ID or other information, you should use the [Search documents](https://developers.vtex.com/vtex-developer-docs/reference/searchdocuments) endpoint. You can use any other query params you want in this request. The response body will contain information about the sales associate and the store they are associated with.

| **Param** | **Value** |
|---|---|
| `data_entity_name` | `vendors` |
| `_schema` | `v1` |


[block:html]
{
  "html": "<br>"
}
[/block]
### Delete a sales associate

In order to delete a sales associate and remove their data in Master Data, you should use the [Delete document](https://developers.vtex.com/vtex-developer-docs/reference/deletedocument) endpoint.

| **Param** | **Value** |
|---|---|
| `data_entity_name` | `vendors` |
| `id` | Sales associate `DocumentId` value, which represents the sales associate ID number |