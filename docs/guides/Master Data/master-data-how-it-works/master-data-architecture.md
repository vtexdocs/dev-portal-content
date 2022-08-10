---
title: "Architecture"
slug: "master-data-architecture"
hidden: false
metadata: 
  title: "Master Data - Architecture"
createdAt: "2021-04-08T20:20:59.105Z"
updatedAt: "2021-11-18T13:44:22.424Z"
---
This article explains the Master Data services. A service is a kind of program that performs automated tasks and responds to hardware events or requests from other software. Master Data is composed by the following services: API, Worker, Storage and Search Engine.

## API

The API is the service responsible to perform HTTP requests through endpoints that enable access to other services. The other services are the ones that actually store and execute tasks over the data.

The Master Data API endpoints can be found in our API reference for [Master Data V1](ref:master-data-api-v1-overview) and [Master Data V2](ref:master-data-api-v2-overview).

## Worker

The Worker is the service responsible for:

- Sending Documents to the [Search Engine](#search-engine) - This allows the Documents to be searchable and that their latest version are shown in the search results.
- Executing Triggers - This allows the execution of tasks that are triggered from operations in the Documents (i.e.: send an email after any field of a Client Document is changed).
- Import/Export process - Export to a csv file or import from a csv file Documents of a specific Data Entity.

## Storage

The Storage service is where your data is kept. Master Data uses a powerful database to keep billions of documents stored safely.

The [Documents API](ref:documents) retrieves documents directly from the Storage service and it is used to retrieve one Document per request.
[block:callout]
{
  "type": "warning",
  "body": "The data of a store account can only be accessed by this account. One account cannot access the data stored in other accounts and vice versa."
}
[/block]
## Search Engine

The Search Engine is a service that handles filters and aggregations. This service allows Documents to be searchable and is responsible to make the searches. The [Search](ref:search-1) and [Scroll](ref:scroll-1) APIs go to the Search Engine service and can retrieve many Documents at once.

When any data in the Storage is updated, a message is sent to Master Data Worker to execute triggers and to send the latest version of the Documents to the Search Engine, so the updated Documents become searchable. More details about this process can be found in the [Consistency Level](doc:master-data-consistency-level) article.