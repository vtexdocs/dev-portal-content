---
title: "Components"
slug: "master-data-components"
hidden: false
metadata: 
  title: "Master Data - Components"
createdAt: "2021-04-08T20:20:35.782Z"
updatedAt: "2021-04-08T22:22:38.592Z"
---
This article explains the Master Data core components: Data Entity, Document, Field and Index.

>ℹ️ The Master Data core components are equivalent to what is found in database solutions. Some of these components might be found in common database solutions with other names such as record or table.

## Data Entity

In comparison to a regular database, Data Entity is a table in which records (or [Documents](#document)) and [Fields](#field) are always stored.

Master Data currently has two versions (V1 and V2). In V1, a Data Entity is referred by its acronym (a sequence of two uppercase characters). In V2, the Data Entity name is used as reference. For instance, in Master Data V1 a data entity can be identified by NT, while in Master Data V2 it can be identified by Notification.

In Master Data v1, the CL Data Entity is used to keep all customer data related to personal information such as name, email, document and others stored in the same place, and the AD Data Entity is used to store all customers addresses with their respective information such as: receiver name, street, city, etc.

> This module may process personal or sensitive information. Learn more about how VTEX handles data privacy at our [Data privacy](https://developers.vtex.com/docs/guides/data-privacy) guide.

### Document

A Document is a record (a row of the table) inside a Data Entity with an identifier (a Field named `id`). Inside CL Data Entity, for example, each person is represented by a document that has an `id` and other information.

### Field

Documents are composed by one or more Fields (attributes) that specifies characteristics of the Data Entity record. Fields can also be considered as the columns of a Data Entity table. For example, the CL Data Entity has Fields to store the customer's name, email, birth date and document number. 

Data has a shape. A name field is usually expressed as string type, whereas in age is used an integer number type. You can configure the shape of your data for each Data Entity to guarantee consistency. In other words, every Document follows the shape defined by the Data Entity in which it is inserted and its Fields.

Meaning that each Field has a Type which indicates the format of the attribute being string, number, date, null, object or array.

## Index

An Index is a shortcut to find Documents whenever users do not know the Document `id`. An Index can be set up for each Field of a Data Entity. As well as when using an `id`, the Index is used to retrieve a single Document at a time, but using the value of indexed Field instead. For instance, users can find a Document inside CL Data Entity through the email because it has a native Index for the email Field. Indexes are set up in [Master Data V1 using the Admin](https://help.vtex.com/en/tutorial/setting-up-an-index-on-master-data--tutorials_785) and in [Master Data V2 through the API](https://developers.vtex.com/docs/api-reference/master-data-api-v2#put-/api/dataentities/-dataEntityName-/indices).

>⚠️ The Index of a Document is created when the Document is created or modified. Documents will only have Index if the creation or change occurs after the Index of the Data Entity was set up. Documents created before the Index set up of the Data Entity need to be updated to receive the Index.

Once a Document has an Index, you can retrieve it by using the [Search documents](https://developers.vtex.com/docs/api-reference/masterdata-api#get-/api/dataentities/-acronym-/search?endpoint=get-/api/dataentities/-acronym-/search) endpoint with the Field name as a query parameter and the value of Field as the value of the parameter. Example: `/dataentities/CL/search?email=my@email.com`.
