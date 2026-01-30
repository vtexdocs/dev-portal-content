---
title: "Default Values integration"
slug: "default-values-integration"
excerpt: "Learn how to configure and manage default custom field values for B2B checkout forms using the Default Values API."
hidden: false
createdAt: "2026-01-30T00:00:00.000Z"
updatedAt: "2026-01-30T00:00:00.000Z"
---

Default values are purchase details, such as addresses, and B2B custom fields that you configure for an organizational unit so that checkout forms can be completed automatically. This integration guide explains how to use the [Default Values API](https://developers.vtex.com/docs/api-reference/default-values-api) to store and manage these preferences and how they participate in the end-to-end checkout experience.

In typical B2B scenarios, a buyer organization administrator defines which shipping address, billing address, credit card, and custom fields, such as cost center or PO number, should be used by default for each organizational unit. These defaults are stored in VTEX Dynamic Storage and later consumed by session and checkout services to automatically complete orders.

From an architectural perspective, the main actors are:

- Org admin application or custom back office that calls the Default Values API to create and update default values  
- Default Values API, which stores the mapping between entities and their default IDs  
- Shopper-session app, which reads default values and writes them into the shopper session  
- Session service, which exposes the shopper’s defaults to downstream services

## How it works

At a high level, the default values integration works in two phases: configuration and consumption.

1. **Configuration phase**  
     
   - An org admin application identifies the organizational unit, for example, an org unit, contract, or user scope  
   - The application decides which entities should be selected by default  
     - Shipping and billing addresses  
     - Custom field values such as cost center, PO number, release, or location  
   - The application calls the Default Values API to create or update one default values document per unit, sending:  
     - id that uniquely identifies the unit, for example, orgUnitId-123  
     - defaultValues array, where each entry maps:  
       - entity: the type of entity, for example, address/shipping, creditCard  
       - entityValueId: the ID of the chosen default value

   

2. **Consumption phase**  
     
   - At login, the shopper-session app fetches the default values for the shopper’s context and resolves the final default per field based on priority.  
   - The shopper-session app writes the resolved defaults to the shopper session.

## Default values configuration flow

### When to use this flow

* You must define or change default addresses and custom fields for a given organizational unit.  
* You are building a B2B admin experience that allows buyer administrators to manage checkout defaults.  
* You are migrating default values from an external system into VTEX Dynamic Storage.

### Main endpoints involved

* [POST Create default values](http://replace-by-correct-link.create-default-values-document.com/post/api/dataentities/defaultValues/documents)  
* [PATCH Update default values](http://replace-by-correct-link.update-default-values-document.com/patch/api/dataentities/defaultValues/documents/-unitId-)

### Step-by-step

* Identify the organizational unit and define the id value used to store defaults  
* Collect the default entity IDs for addresses, credit cards, and custom fields  
* Build the request body using the DefaultValuesRequest schema  
* Create or update the document using the [Create default values](http://replace-by-correct-link.create-default-values-document.com/post/api/dataentities/defaultValues/documents) or [Update default values](http://replace-by-correct-link.update-default-values-document.com/patch/api/dataentities/defaultValues/documents/-unitId-) endpoints  
* Validate the output and update any dependent session logic

### Request example \- Create default values document

```shell
curl -X POST "https://{{accountName}}.{{environment}}.com.br/api/dataentities/defaultValues/documents" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "X-VTEX-API-AppKey: {{appKey}}" \
  -H "X-VTEX-API-AppToken: {{appToken}}" \
  -d '{
    "id": "orgUnitId-123",
    "defaultValues": [
      { "entity": "address/shipping", "entityValueId": "ed30b8d1-3128-4b0c-be56-f55b79592248" },
      { "entity": "address/billing", "entityValueId": "230e441e-07b6-4740-9f7c-74666da3f682" },
      { "entity": "creditCard", "entityValueId": "EDE0B17747B24EFC9650B6C6B3E06C5F" },
      { "entity": "customFieldValues/poNumberFieldId", "entityValueId": "4498bd3d-7eaf-11f0-b37f-cc2298c87c12" }
    ]
  }'
```

### Response example

```json
{
  "Id": "orgUnitId-123",
  "Href": "https://{{accountName}}.{{environment}}.com.br/api/dataentities/defaultValues/documents/orgUnitId-123",
  "DocumentId": "orgUnitId-123"
}
```

## Default values cleanup flow

### When to use this flow

Use this flow when:

* An organizational unit is removed, and its defaults should no longer be used  
* You must reset all defaults for testing or reconfiguration  
* You are cleaning up deprecated data

### Main endpoint

- [DELETE Delete default values](http://replace-by-correct-link.delete-default-values-document.com/delete/api/dataentities/defaultValues/documents/-unitId-)

### Step-by-step

- Identify the unit to clean up  
- Call the [Delete default values](http://replace-by-correct-link.delete-default-values-document.com/delete/api/dataentities/defaultValues/documents/-unitId-) endpoint to remove the document  
- Coordinate with session and checkout components so defaults are no longer applied

### Request example \- Delete Default Values

```shell
curl -X DELETE "https://{{accountName}}.{{environment}}.com.br/api/dataentities/defaultValues/documents/orgUnitId-123" \
  -H "Accept: application/json" \
  -H "X-VTEX-API-AppKey: {{appKey}}" \
  -H "X-VTEX-API-AppToken: {{appToken}}"
```

## Permissions

The following License Manager resources are required depending on the operation:

| Endpoint | Required resources (any of) |
| :---- | :---- |
| **POST Create default values** | - Insert or update document not remove<br>- Full access to all documents<br>- Master Data administrator |
| **GET Get default values** | - Read-only documents<br>- Insert or update document, not remove<br>- Full access to all documents<br>- Master Data administrator |
| **PATCH Update default values** | - Insert or update document, not remove<br>- Full access to all documents<br>- Master Data administrator |
| **DELETE Delete default values** | - Full access to all documents<br>- Master Data administrator |
