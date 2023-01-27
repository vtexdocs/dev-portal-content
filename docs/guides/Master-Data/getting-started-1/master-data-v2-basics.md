---
title: "Master Data v2 basics"
slug: "master-data-v2-basics"
hidden: false
createdAt: "2022-07-18T17:19:39.913Z"
updatedAt: "2022-07-18T19:58:52.998Z"
---
Master Data v2 provides a powerful data base solution for your store, that you can manage via the [Master Data v2 API](https://developers.vtex.com/vtex-rest-api/reference/master-data-api-v2-overview). Below you can learn about some basic features and how to use them.

## Saving documents

If you do not need to validate your data, you may save your documents without any setup. You can use the following API requests:
- [Create new document](ref:createnewdocument)
- [Create partial document](ref:createorupdatepartialdocument) 
- [Update entire document](ref:updateentiredocument) 
- [Update partial document](ref:updatepartialdocument) 

In case you need to validate the data, you must first [create a JSON schema](https://developers.vtex.com/vtex-rest-api/reference/saveschemabyname). After that, you'll add the name of the JSON Schema to the query, like in this example:
```
api/dataentities/{data-entity-name}/documents?_schema={my-schema}
```

## Getting documents

There are three ways of getting documents. If you have the document's ID, you must use the [Get document](ref:getdocument) endpoint.

To get multiple documents, you may use the [Search documents](ref:searchdocuments) API request.


And finally, if you want to get all documents that attend to a specific set of criteria, you must use the [Scroll documents](ref:scrolldocuments) API endpoint.

As said before, the documents could comply with none or multiple JSON Schemas. You may add the schema parameter to the query to filter the documents based in the JSON Schema. See the example below.

```
api/dataentities/{data-entity-name}/documents/{id}?_schema={my-schema}
api/dataentities/{data-entity-name}/search?_schema={my-schema}
api/dataentities/{data-entity-name}/scroll?_schema={my-schema}
```