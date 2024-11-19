---
title: "Consistency Level"
slug: "master-data-consistency-level"
hidden: false
excerpt: Learn how data synchronization operates across Master Data API endpoints.
createdAt: "2021-04-08T20:22:51.616Z"
updatedAt: "2021-06-23T02:09:50.777Z"
---

Master Data is a distributed database system designed to provide fast global access to data. In such systems, maintaining data consistency is essential to ensure that changes are accurately reflected across all instances.

This consistency is achieved through two approaches: strong consistency and eventual consistency.

## Strong consistency

With strong consistency, any change to data is immediately reflected and accessible after it occurs. This is achieved by locking access to the updated data until all instances have been synchronized.

This approach ensures that all users see the same data at the same time, without delay. For example, when using the `/documents` API to store and retrieve data, strong consistency ensures that the data is immediately up-to-date after any changes to a Document.

## Eventual consistency

In eventual consistency, changes take some time to propagate across instances. The updates are queued and processed asynchronously, meaning users may not see the updated data immediately. This approach is used in resource-intensive tasks, especially in large datasets. As a result, performance is optimized while synchronization occurs gradually.

For example, the `/search` API uses eventual consistency. After a Document is updated, the change will appear in the search results only after the system has processed it. 

When data is persisted in Master Data, the Storage is updated in an atomic operation. A message is sent to the Master Data Worker to trigger actions like sending the updated Document to the Search Engine. Only after the Search Engine is updated will the changes be available through the `/search` API.

For more information on the update process in the Search Engine, refer to [Schema Lifecycle](https://developers.vtex.com/docs/guides/master-data-schema-lifecycle).

## Example

Consider the following Document:

```
{
 	"id": "0e860678-83cc-4c21-8194-3377adcee0b7",
 	"firstName": "Jhon"
}
```

If the `firstName` value is updated to `Super Jhon`, two subsequent API requests made immediately after the update may yield different results:


|Endpoint|Consistency Type|API Request|Response|
|-----|-------|-----------|---------|
|`/documents`|Strongly Consistent|`GET /documents/0e860678-83cc-4c21-8194-3377adcee0b7?_fields=id,firstName`|`{ "id": "0e860678-83cc-4c21-8194-3377adcee0b7", "firstName": "Super Jhon" }`|
|`/search`|Eventually Consistent|`GET /search?_where=firstName="Super Jhon"&_fields=id,firstName`|`{}`|

Note that the `/documents` API provides the updated data immediately (strong consistency), whereas the `/search` API reflects the change only after the update is processed asynchronously (eventual consistency).

## Consistency level by API endpoint

The table below shows the consistency level for each API endpoint.

| Name | Path | Level |
| - | - | - |
| Documents | `/documents` | `Strongly Consistent` |
| Indices | `/indices` | `Strongly Consistent` |
| Schemas | `/schemas` | `Strongly Consistent` |
| Search | `/search` | `Eventually Consistent` |
| Scroll | `/scroll` | `Eventually Consistent` |
