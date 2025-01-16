---
title: "Master Data best practices"
slug: "master-data-best-practices"
excerpt: "Get started with Master Data document management, data entity customization, and trigger utilization."
hidden: false
createdAt: "2022-07-05T19:11:40.758Z"
updatedAt: "2022-07-05T20:08:04.515Z"
---
Below, you can check some guides to help you get started with Master Data.

## Manage documents

See Master Data v2 endpoints for managing documents:

- `POST` - [Create new document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#post-/api/dataentities/-dataEntityName-/documents)
- `GET` - [Get document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/documents/-id-) 
- `PUT` - [Update entire document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/documents/-id-) 
- `PATCH` - [Update partial document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#patch-/api/dataentities/-dataEntityName-/documents/-id-)
- `DELETE` - [Delete document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#delete-/api/dataentities/-dataEntityName-/documents/-id-)

## Customize data entities

See these articles about customizing data entities and schemas:

- [How to create a data entity](https://help.vtex.com/en/tutorial/creating-data-entity--tutorials_1265)
- [Starting to work on Master Data with JSON Schema](/docs/guides/working-with-json-schemas-in-master-data-v2) 

## Search documents

Below, you can see Master Data v2 endpoints for searching documents.

- `GET` - [Search documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/search) 
- `GET` - [Scroll documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/scroll) 

## Working with triggers

A Master Data trigger is an action executed after the insert or update of a given document.

- [Create triggers with Master Data v1](https://help.vtex.com/en/tutorial/creating-trigger-in-master-data--tutorials_1270)
- [Setting up triggers in Master Data v2](https://developers.vtex.com/docs/guides/setting-up-triggers-on-master-data-v2)
