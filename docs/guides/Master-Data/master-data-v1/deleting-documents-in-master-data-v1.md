---
## title: "Deleting documents in Master Data v1"
slug: "deleting-documents-in-master-data-v1"
hidden: false
createdAt: "2026-07-08T21:34:00.000Z"
updatedAt: "2026-07-08T21:34:00.000Z"
excerpt: "Learn how to delete Master Data v1 documents in bulk through the API to reduce stored volume, and how to recover access when an entity was removed from the Master Data v1 interface."
seeAlso:
 - "/docs/guides/extracting-data-from-master-data-with-search-and-scroll"
 - "/docs/guides/pagination-in-the-master-data-api"
 - "/docs/guides/querying-documents-in-master-data-v1"
---

This guide explains how to delete documents in [custom data entities](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#custom-data-entities) in Master Data v1 through the [Master Data API v1](https://developers.vtex.com/docs/api-reference/masterdata-api) to reduce stored volume and billing. The flow uses [Scroll documents](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/scroll) to list document IDs and [Delete document](https://developers.vtex.com/docs/api-reference/masterdata-api#delete-/api/dataentities/-acronym-/documents/-id-) to remove each record.

> ℹ️ To erase data for one specific customer for privacy reasons, follow [Erasing customer data](https://help.vtex.com/en/tutorial/erasing-customer-data--1R9Fn7A06Ifj4R9YD4JTKU), which uses [Search documents](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search) and [Delete document](https://developers.vtex.com/docs/api-reference/masterdata-api#delete-/api/dataentities/-acronym-/documents/-id-). This guide does not replace that flow.

## Data entities and documents

In Master Data v1, a [data entity](https://help.vtex.com/en/tutorial/data-entity--tutorials_1265) is the schema (table) that defines fields and storage rules. Each record stored in that entity is a **document**, identified by a unique ID. See [Master Data](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#documents) for more on this model.

A common mistake when trying to reduce Master Data billing is clicking **delete** on the data entity in the Master Data v1 interface. That action removes the entity definition but does not delete the documents already stored, so Master Data consumption is not affected. For custom data entities, the monthly snapshot used for [billing](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#billing) continues to count those records, and billed volume does not decrease.

## Step 1: List document IDs with Scroll documents

Bulk deletion requires listing every document ID first. Use [Scroll documents](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/scroll) (`GET /api/dataentities/{acronym}/scroll`), the same endpoint used for large-scale data extraction. For query patterns and scroll limits, see [Extracting data from Master Data with search and scroll](https://developers.vtex.com/docs/guides/extracting-data-from-master-data-with-search-and-scroll#scroll) and [Querying documents in Master Data v1](https://developers.vtex.com/docs/guides/querying-documents-in-master-data-v1).

Send a `GET` request to the **Scroll documents** endpoint, replacing `{acronym}` with the data entity acronym. On the first request only, set `_size` (maximum `1000`) to control how many documents are returned per page. Optionally set `_fields=id` to return only document IDs. You cannot change `_size` or filters on subsequent requests.

**First request example:**

```bash
curl --request GET \
  --url 'https://{accountName}.{environment}.com.br/api/dataentities/{acronym}/scroll?_size=1000&_fields=id' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json'
```

From the response:

1. Collect the `id` value of each document.
2. Read the `X-VTEX-MD-TOKEN` response header from the first request.
3. While the response still contains documents, send another `GET` request with `_token` set to that header value. Repeat until the response returns an empty list. The token expires after 20 minutes of inactivity. For more details, see [Scroll pagination](https://developers.vtex.com/docs/guides/pagination-in-the-master-data-api#scroll-pagination).

**Subsequent request example:**

```bash
curl --request GET \
  --url 'https://{accountName}.{environment}.com.br/api/dataentities/{acronym}/scroll?_token={tokenValue}' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json'
```

## Step 2: Delete each document

For each document ID returned by the scroll requests, send a `DELETE` request to [Delete document](https://developers.vtex.com/docs/api-reference/masterdata-api#delete-/api/dataentities/-acronym-/documents/-id-) (`DELETE /api/dataentities/{acronym}/documents/{id}`).

**Request example:**

```bash
curl --request DELETE \
  --url 'https://{accountName}.{environment}.com.br/api/dataentities/{acronym}/documents/{id}' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json'
```

Repeat for every ID collected in the previous step. A successful deletion returns HTTP status `204 No Content`.

> ⚠️ Document deletion is irreversible. Before running this flow in production, confirm the entity acronym and test with a small set of records when possible.

After you delete documents through the API, they are no longer counted in stored volume.

## Recover access when the entity was deleted from the Admin

If the data entity was already deleted from the Master Data v1 interface, the API can no longer [search](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search) or [scroll](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/scroll) the documents stored under that acronym. Recreate the entity, publish it, and reindex it before you run the deletion flow above.

To do this, follow the instructions below:

1. **Recreate the data entity** in the Master Data v1 interface. See [Data entity](https://help.vtex.com/docs/tutorials/data-entity).
2. **Publish the entity** using the save action on the entity row, as described in [Data entity](https://help.vtex.com/docs/tutorials/data-entity).
3. **Reindex the entity** so the documents become searchable and scrollable through the API again. To reindex, follow the instructions in [Filtering data on Master Data](https://help.vtex.com/docs/tutorials/filtering-data-on-master-data).
4. After reindexing completes, you can run the [scroll and delete flow](#step-1-list-document-ids-with-scroll-documents) to remove the records.
