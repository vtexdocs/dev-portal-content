---
title: "Consistency Level"
slug: "master-data-consistency-level"
hidden: false
metadata: 
  title: "Master Data - Consistency Level"
createdAt: "2021-04-08T20:22:51.616Z"
updatedAt: "2021-06-23T02:09:50.777Z"
---
Master Data is a distributed database system, which allows the data to be quickly accessed and managed all over the world. A distributed system is a network of servers spread around the world. An important feature of this kind of system is that the data needs to be consistent. In other words, when there is a change in the data, this change needs to be replicated to be available by all other instances. The propagation of this change to all instances is what guarantees the consistency of the data. This happens in two ways: with strong consistency and with eventual consistency.

## Strong consistency

Strong consistency means that a change can be accessed immediately after it occurred. For that to occur, the other instances will lock the access to that piece of data until all of them are updated.

When using `/documents` API to store and retrieve documents, users experience a strong consistency for reading after a Document is updated.

Take the following Document as example in a Data Entity:

```
{
 	"id": "0e860678-83cc-4c21-8194-3377adcee0b7",
 	"firstName": "Jhon"
}
```

In this example, the value of `firstName` is changed to `Super Jhon` and, immediately after that, two API requests are made to get the Document. The first one tries to obtain the Document through the ID using the `/documents` endpoint. The second request is a search looking for the new value of `firstName` using the `/search` endpoint. The two requests are made as:

`GET /documents/0e860678-83cc-4c21-8194-3377adcee0b7?_fields=id,firstName`

and

`GET /search?_where=firstName="Super Jhon"&_fields=id,firstName`

You will notice the following responses respectively:

```
GET /documents/0e860678-83cc-4c21-8194-3377adcee0b7?_fields=id,firstName
Status Code: 200
{
 	"id": "0e860678-83cc-4c21-8194-3377adcee0b7",
 	"firstName": "Super Jhon"
}
```

and

```
GET /search?_where=firstName="Super Jhon"&_fields=id,firstName
Status Code: 200
{
}
```

The `/document` API is strongly consistent and it will respond to the data updated immediately after the change. But with the `/search` API, the result of the change does not appear since it is not strongly consistent.

## Eventual consistency

Eventual consistency means that the change takes some time to be reflected and be available to the user. In other words, the change will enter in a queue and eventually will be propagated to all the server instances.

Unlike the operations with `/document`, the `/search` API is eventually consistent and the updated data will be shown after a short time.

The `/document` API goes directly to the Storage service whereas the `/search` API goes to the Search Engine service. When some data is persisted in Master Data, the Storage is updated in an atomic operation. A message is sent to Master Data Worker to execute triggers and to send the Document to the Search Engine. Only after the Search Engine is updated that the updated Documents will be available through the `/search` API.
[block:callout]
{
  "type": "info",
  "body": "The necessity of eventual consistency for the `/search` API is that indexing the Documents in the Search Engine is a costly operation (even more when the amount of Documents is too large), so it happens asynchronously from the direct access of the Documents using the `/document` API."
}
[/block]
A more detailed explanation of the update process in the Search Engine can be found in the article [Schema Lifecycle](doc:master-data-schema-lifecycle).

## Consistency level

The table below shows the consistency level for each API.

| Name | Path | Level |
| - | - | - |
| Documents | `/documents` | `Strongly Consistent` |
| Indices | `/indices` | `Strongly Consistent` |
| Schemas | `/schemas` | `Strongly Consistent` |
| Search | `/search` | `Eventually Consistent` |
| Scroll | `/scroll` | `Eventually Consistent` |