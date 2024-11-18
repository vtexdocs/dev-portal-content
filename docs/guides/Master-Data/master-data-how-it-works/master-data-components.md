---
title: "Components"
slug: "master-data-components"
hidden: false
metadata: 
  title: "Master Data - Components"
createdAt: "2021-04-08T20:20:35.782Z"
updatedAt: "2021-04-08T22:22:38.592Z"
---

This guide introduces the key components of Master Data and their functionalities. These components are conceptually similar to those in traditional database systems, but with distinct terminology:  

- **Data Entity**: Represents a table-like structure that contains multiple Documents.
- **Document**: Represents a record (row) within a Data Entity.
- **Field**: Represents an attribute (column) of a Document.
- **Index**: Represents an optimization layer linked to a specific field to speed up searches.

![Master Data Structure](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/master-data-components.jpg)

## Data Entity

A Data Entity is analogous to a table in traditional databases. It stores records (or [Documents](#document)) and [Fields](#field), representing the structure of data in Master Data.

Master Data has two versions (V1 and V2):
- **V1:** Data Entities are identified by a two-letter uppercase acronym (e.g., `NT`).
  - Example: `CL` stores customer-related data like name, email, and document; `AD` stores customer address data, such as street, city, and recipient name.
- **V2:** Data Entities are identified by their full name (e.g., `Notification`).

> This module may process personal or sensitive information. Learn more about how VTEX handles data privacy in our [Data privacy](https://developers.vtex.com/docs/guides/data-privacy) guide.

### Document

A Document represents a record (or row) within a Data Entity. Each Document has a unique identifier (the `id` Field). 

For example, in the `CL` Data Entity, each customer is represented by a Document that includes fields like `id`, `name`, `email`, and other personal details.

### Field

A Field is a specific attribute or characteristic of a Document within a Data Entity, analogous to columns in a database table. Each Field has a defined data type:  

- `string`: Text-based data (e.g., `name`).
- `number`: Numeric data (e.g., `age`).
- `date`: Date-based data (e.g., `birthdate`) 
- `object`: A structured data type with key-value pairs.
- `array`: A list of values.
- `null`: Explicitly undefined value.

For example, in the `CL` Data Entity, Fields may include `name`, `email`, `birthdate`, and `document_number`. Each Field has a type that determines its data format:

Consistent structure is enforced across all Documents in a Data Entity based on its defined Fields.

## Index

An Index enables you to search for Documents based on a Field, without needing the Document's `id`. You can create an Index for any Field in a Data Entity.

For example, if the `CL` Data Entity has an Index on the `email` Field, you can retrieve a Document by querying the `email` value instead of the `id`.

Indexes are configured differently depending on the Master Data version:
- **V1:** Managed via the Admin interface. For more information, refer to [Indexes in Master Data V1](https://help.vtex.com/en/tutorial/setting-up-an-index-on-master-data--tutorials_785). Once an Index is set up, you can retrieve Documents using the [Search documents](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search) endpoint with the Field name as the query parameter and the value of Field as the value of the parameter. Example: `/dataentities/CL/search?email=my@email.com`.
- **V2:** Managed via API. Refer to [PUT - Create index](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/indices) for more information. Once an Index is set up, you can retrieve Documents using the [Search documents](https://developers.vtex.com/docs/api-reference/master-data-api-v2#get-/api/dataentities/-dataEntityName-/search) endpoint.

When using an `id`, the Index retrieves a single Document at a time, but using an indexed Field allows you to search for Documents based on that Field's value instead.

>⚠️ Indexes are created when a Document is created or modified. Documents will only have an Index if the Data Entity's Index was set up before or during the Document's creation or modification. Documents created before the Index was set up must be updated to receive it.
