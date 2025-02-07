---
title: "Data consistency and synchronization in Master Data"
slug: "data-consistency-and-synchronization-in-master-data"
hidden: false
excerpt: Learn how data synchronization operates across Master Data API endpoints.
createdAt: "2021-04-08T20:22:51.616Z"
updatedAt: "2021-06-23T02:09:50.777Z"
---

Master Data is a distributed database system designed to provide fast global access to data. In such systems, maintaining data consistency is essential to ensure that changes are accurately reflected across all instances.

This consistency is achieved through two approaches: strong consistency and eventual consistency.

## Strong consistency

With strong consistency, any change to data is immediately reflected and accessible after it occurs. This is achieved by locking access to the updated data until all instances have been synchronized.

This approach ensures that all users see the same data at the same time, without delay. For example, when using the `/documents` API to store and retrieve data, strong consistency ensures that the data is immediately up-to-date after any changes to a document.

## Eventual consistency

In eventual consistency, changes take some time to propagate across instances, and synchronization occurs gradually. Updates are queued and processed asynchronously, meaning users may not see the updated data immediately. This approach enhances scalability and performance, especially for large datasets.

For example, the `/search` API uses eventual consistency. After a document is updated, the change will appear in the search results only after the system has processed it. While this allows for optimized performance, there is a delay before updates become visible in search queries.

When data is persisted in Master Data, the Storage update occurs in an atomic operation, meaning all changes happen at once, ensuring data integrity. A message is sent to the Master Data Worker, which then triggers actions like forwarding the updated document to the Search engine. Only after the Search engine is updated changes are available through the `/search` API.

For more information on the update process in the Search Engine, refer to [Schema Lifecycle](https://developers.vtex.com/docs/guides/master-data-schema-lifecycle).

## Example

Consider the following document:

```json
{
 	"id": "0e860678-83cc-4c21-8194-3377adcee0b7",
 	"firstName": "John"
}
```

If the `firstName` value is updated to `Richard`, two subsequent API requests made immediately after the update may yield different results:

| Endpoint | Consistency type | API request | Response |
| - | - | - | - |
| `/documents` | Strong consistency |`GET /documents/0e860678-83cc-4c21-8194-3377adcee0b7?_fields=id,firstName` | `{ "id": "0e860678-83cc-4c21-8194-3377adcee0b7", "firstName": "Richard" }` |
| `/search` | Eventual consistency |`GET /search?_where=firstName="Richard"&_fields=id,firstName` | `{}` |

Note that the `/documents` API provides the updated data immediately (strong consistency), whereas the `/search` API reflects the change only after the update is processed asynchronously (eventual consistency).

## Consistency level by endpoint

The table below shows the consistency level for each Master Data API path.

| Name | Path | Level |
| - | - | - |
| Documents | `/documents` | Strong consistency |
| Indices | `/indices` | Strong consistency |
| Schemas | `/schemas` | Strong consistency |
| Search | `/search` | Eventual consistency |
| Scroll | `/scroll` | Eventual consistency |

For more details on specific endpoints, refer to the [Master Data API - v1](https://developers.vtex.com/docs/api-reference/masterdata-api) and [Master Data API - v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2) reference.
