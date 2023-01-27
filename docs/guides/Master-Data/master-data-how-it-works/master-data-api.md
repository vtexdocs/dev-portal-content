---
title: "API"
slug: "master-data-api"
hidden: false
metadata: 
  title: "Master Data - API"
createdAt: "2021-04-08T20:22:19.710Z"
updatedAt: "2021-10-28T22:16:34.979Z"
---
Master Data allows users to store and manage data in a structured manner. To abstract this kind of organization, the Master Data API is divided in two categories: Data Plane and Control Plane. The Data Plane is where the management of records happen, including searches and accessing Documents. The Control Plane is where the structure of both the records and the access to them is defined.

## Data Plane

The Data Plane is the category to store and retrieve Documents. The Data Plane has a higher access volume to provide the necessary data to the stores, so the access to the Data Plane happens quickly and is highly available.

The `/documents` API can be used to store and retrieve Documents. In case of retrieval, you must indicate the `id` Field of the desired Document. The `id` Field contains an unique identifier of the Document.

In many cases, the user doesn’t know the `id` Field of a Document, but it can be found through a search using other Fields (i.e.: the name of a client). The `/search` and `/scroll` APIs can be used to find documents by Fields that are Searchable or Index.

Searchable is a Field configuration which enables the Field to be used in the `/scroll` API. At Master Data V1 is the property `Is Filter` whereas Master Data V2 is the property `v-indexed`.

An Index is a configuration which enables a shortcut to retrieve Documents faster and to guarantee uniqueness.

## Control Plane

The Control Plane is the category that lets you manage how Data Plane behaves. Users can configure validation, search and triggers to Data Entities. Since the Control Plane only deals with the structure, and not the records themselves, access to the Control Plane happens less frequently than to the Data Plane.

Master Data V1 does not have a Control Plane API. All configuration is handled by the Admin through the Dynamic Storage, which can be accessed using the link https://{{account}}.ds.vtexcrm.com.br.

Master Data V2 has the `/schema` and `/indices` APIs and allows users to create and update [JSON Schemas](https://spacetelescope.github.io/understanding-json-schema/) to any Data Entity at Master Data V2.
[block:callout]
{
  "type": "warning",
  "body": "Creating and updating JSON Schemas changes the Data Plane behavior. JSON Schemas only exist in Master Data V2."
}
[/block]
## API Summary

The endpoints in the Master Data API are:
- [Schemas](ref:schemas): Allows to create and read Schemas for a Data Entity. The use of Schemas enables searches with custom Fields and to add rules when managing Documents. More information about Schemas can also be found in the article [Schema Lifecycle](/docs/guides/master-data-schema-lifecycle).
- [Indices](ref:indices): Indices are shortcuts to Documents that enable fast access using other Fields beyond the Document `id`. More information about Indices can be found in the article [Components](/docs/guides/master-data-components).
- [Documents](ref:documents): This is the API to manage Documents directly, accessing them individually through their `id`.
- [Search](ref:search): Allows the retrieval of many Documents with a variety of parameters, including Schemas and indexed Fields.
- [Scroll](ref:scroll): Allows the retrieval of a very large amount of Documents.

The table below shows what endpoints belong to which category and Master Data version.

| Name | Path | Category | Version |
| - | - | - | - |
| Schemas | `/schemas` | Control Plane | `Master Data V2` |
| Indices | `/indices` | Control Plane | `Master Data V2` |
| Documents | `/documents` | Data Plane | `Master Data V1` `Master Data V2` |
| Search | `/search` | Data Plane | `Master Data V1` `Master Data V2` |
| Scroll | `/scroll` | Data Plane | `Master Data V1` `Master Data V2` |