---
title: "Documents"
slug: "documents-1"
hidden: false
createdAt: "2019-12-18T22:14:53.633Z"
updatedAt: "2019-12-18T23:11:21.130Z"
---
The APIs within this group are used to save documents and query them by id.

If the document has the id attribute or has fields that have been set to indexes with unique values, VTEX Master Data will attempt to identify the document. If the document is found a change will be made. If it is not found, an inclusion will be made. ** This scenario does not apply to the API with the POST verb**.

Another important note: The id field will only be considered on the **POST** verb if the ID type entered in the Data Entity is the option:

```
A chave primária será informada pelo cliente através do atributo 'id'
```
Otherwise, a new document will always be created.

### Response status code

1. Status Code 201: Document created successfully
2. Status Code 200: Document changed successfully
3. Status Code 304: There were no changes to the document
4. Status Code 400: Invalid information in JSON
5. Status Code 403: Unauthorized access