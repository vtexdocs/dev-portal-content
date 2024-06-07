---
title: "Master Data - API"
slug: "master-data-api"
hidden: false
createdAt: "2021-04-08T20:22:19.710Z"
updatedAt: "2021-10-28T22:16:34.979Z"
---
Master Data allows users to store and manage data in a structured manner. To abstract this kind of organization, the Master Data API is divided in two categories: Data Plane and Control Plane. The Data Plane is where the management of records happens, including searches and accessing documents. The Control Plane is where the structure of both the records and the access to them is defined.

## Data Plane

The Data Plane is the category to store and retrieve documents. The Data Plane has a higher access volume to provide the necessary data to the stores, so the access to the Data Plane happens quickly and is highly available.

The `/documents` API can be used to store and retrieve documents. In case of retrieval, you must indicate the `id` field of the desired document. The `id` field contains an unique identifier of the document.

The `id` field of a document can be found through a search using other fields (i.e.: the name of a client). The `/search` and `/scroll` APIs can be used to find documents by fields that are set up as Searchable or as an Index.

Searchable is a field configuration which enables the field to be used in the `/scroll` API. In Master Data V1, it is the `Is Filter` property. In Master Data V2, it is the `v-indexed` property.

An Index is a configuration which enables a shortcut to retrieve documents faster and to guarantee uniqueness, which represents an alternative to using the `id`. More information about Indices can be found in the article [Components](https://developers.vtex.com/docs/guides/master-data-components).

## Control Plane

The Control Plane is the category that lets you manage how Data Plane behaves. Developers can configure validation, search and triggers within Data Entities. Since the Control Plane only deals with the structure, and not the records themselves, access to the Control Plane happens less frequently than to the Data Plane.

Master Data V1 does not have a Control Plane API. All configuration is handled by the Admin through the Dynamic Storage, which can be accessed using the link `https://{{account}}.ds.vtexcrm.com.br` or through Admin, on **Store Settings > Storefront > Master Data > ⚙ > Data structure**.

Master Data V2 has the `/schema` and `/indices` APIs and allows users to create and update [JSON Schemas](https://spacetelescope.github.io/understanding-json-schema/) to any Data Entity at Master Data V2.

>⚠️ Creating and updating JSON Schemas changes the Data Plane behavior. JSON Schemas only exist in Master Data V2.

## Master Data API

The table below shows what endpoints from Master Data API belong to which category and Master Data version.

| Name | Path | Category | Description | Version |
| - | - | - | - | - |
| Schemas | `/schemas` | Control Plane |  Create and read schemas for a Data Entity. The use of schemas enables searches with custom fields and to add rules when managing documents. More information about schemas can also be found in the article [Schema Lifecycle](https://developers.vtex.com/docs/guides/master-data-schema-lifecycle). | [Master Data API - v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2) |
| Indices | `/indices` | Control Plane | Retrieve, create or delete indices, which are shortcuts to documents that enable fast access using other fields beyond the document `id`. More information about indices can be found in the article [Components](https://developers.vtex.com/docs/guides/master-data-components). | [Master Data API - v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2) |
| Documents | `/documents` | Data Plane | Manage documents directly, accessing them individually through their `id`. | [Master Data API - v1](https://developers.vtex.com/docs/api-reference/masterdata-api) <br> [Master Data API - v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2) |
| Search | `/search` | Data Plane | Retrieve documents with a variety of parameters, including schemas and indexed fields. | [Master Data API - v1](https://developers.vtex.com/docs/api-reference/masterdata-api) <br> [Master Data API - v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2) |
| Scroll | `/scroll` | Data Plane | Retrieve a large amount of documents. | [Master Data API - v1](https://developers.vtex.com/docs/api-reference/masterdata-api) <br> [Master Data API - v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2) |
