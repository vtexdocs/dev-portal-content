---
title: "Master Data API"
slug: "master-data-api"
excerpt: Learn how to manage and retrieve documents, define data structures, and configure searchable fields in Master Data.
hidden: false
createdAt: "2021-04-08T20:22:19.710Z"
updatedAt: "2021-10-28T22:16:34.979Z"
seeAlso:
    - /docs/api-reference/master-data-api-v2
    - /docs/api-reference/masterdata-api
---

Master Data API provides a structured way to store, retrieve, and manage data. It is organized into two categories:

- **[Data Plane](#data-plane):** Manages records, enabling tasks such as searching and accessing documents. 
- **[Control Plane](#control-plane):** Defines the structure of records and access configurations.

## Data Plane

The Data Plane stores and retrieves documents. Designed for high-volume operations, the Data Plane ensures quick and reliable data access for store operations.

### Getting a document by `id`

The `/documents` endpoint is used to store and retrieve individual documents. To retrieve a document, you must provide the `id` value of the desired document, which serves as the unique identifier of the document.

### Searching for documents

When the `id` of a document is unknown, you can use the following APIs to locate it using searchable fields or indexes:

- `/search`: Retrieves documents using Index fields. Learn more about Indices in [Components](https://developers.vtex.com/docs/guides/master-data-components).
- `/scroll`: Handles large datasets, enabling bulk document retrieval through Searchable fields.

>ℹ️ Searchable fields are configured to work with the `/search` and `/scroll` endpoints. In Master Data v1, they are defined using the `Is Filter` property. In Master Data v2, they use the `v-indexed` property.

>ℹ️ Learn more about [Extracting data from Master Data with search and scroll](https://developers.vtex.com/docs/guides/extracting-data-from-master-data-with-search-and-scroll).

## Control Plane

The Control Plane manages the structure and behavior of the Data Plane. It enables developers to configure data validation, searchable fields and triggers within data entities. Control Plane operations are less frequent but crucial for defining data structures.

### Master Data v1

Master Data v1 does not provide a Control Plane API. All configurations are handled via the VTEX Admin through the Dynamic Storage at **Store Settings > Storefront > Master Data > ⚙ > Data structure** (`https://{{accountName}}.ds.vtexcrm.com.br`).

### Master Data v2

Master Data v2 has the `/schema` and `/indices` endpoints, allowing for the creation and management of [JSON Schemas](https://json-schema.org/) for data entities. These schemas define the structure of stored data and directly influence how the Data Plane processes and validates documents.

>⚠️ JSON Schemas are exclusive to Master Data v2.

## Master Data API endpoints

The table below summarizes the available endpoints, their categories, descriptions, and supported versions.

| Endpoint | Category | Description | Master Data v1 Documentation | Master Data v2 Documentation |
| - | - | - | - | - |
| `/schemas` | Control Plane | Creates and manages schemas for a data entity. The use of schemas enables searches with custom fields and to add rules when managing documents. Learn more in [Schema Lifecycle](https://developers.vtex.com/docs/guides/master-data-schema-lifecycle). | N/A | <ul><li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/schemas">Get schemas</a></li><li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/schemas/-schemaName-">Get schema by name</a></li><li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/schemas/-schemaName-">Save schema by name</a></li><li><a href="https://developers.vtex.com/docs/api-reference/master-data-api-v2#delete-/api/dataentities/-dataEntityName-/schemas/-schemaName-">Delete schema by name</a></li></ul> |
| `/indices` | Control Plane | Manages indices for fast document access via fields other than `id`. Learn more in [Components](https://developers.vtex.com/docs/guides/master-data-components). | N/A | <ul><li>[Get indices](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/indices)</li><li>[Put indices](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/indices)</li><li>[Get index by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/indices/-index_name-)</li><li>[Delete index by name](https://developers.vtex.com/docs/api-reference/master-data-api-v2#delete-/api/dataentities/-dataEntityName-/indices/-index_name-)</li></ul> |
| `/documents` | Data Plane | Manages individual documents using their `id`. | <ul><li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api#post-/api/dataentities/-acronym-/documents">Create new document</a></li><li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api#put-/api/dataentities/-acronym-/documents/-id-">Create document with custom ID or Update entire document</a></li><li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api#patch-/api/dataentities/-acronym-/documents">Create or update partial document</a></li><li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/documents/-id-">Get document</a></li><li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api#put-/api/dataentities/-acronym-/documents/-id-">Update entire document</a></li><li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api#patch-/api/dataentities/-acronym-/documents/-id-">Update partial document</a></li><li><a href="https://developers.vtex.com/docs/api-reference/masterdata-api#delete-/api/dataentities/-acronym-/documents/-id-">Delete document</a></li></ul> |  <ul><li>[Create new document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#post-/api/dataentities/-dataEntityName-/documents)</li><li>[Create partial document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#patch-/api/dataentities/-dataEntityName-/documents)</li><li>[Get document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/documents/-id-)</li><li>[Create document with custom ID or Update entire document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/documents/-id-)</li><li>[Update partial document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#patch-/api/dataentities/-dataEntityName-/documents/-id-)</li><li>[Delete document](https://developers.vtex.com/docs/api-reference/master-data-api-v2#delete-/api/dataentities/-dataEntityName-/documents/-id-)</li></ul> |
|`/search` | Data Plane | Retrieves documents based on parameters like schemas and indexed fields. | [Search documents](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search) | [Search documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/search) |
|`/scroll` | Data Plane | Retrieves large amount of documents. | [Scroll documents](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/scroll) | [Scroll documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/scroll) |
