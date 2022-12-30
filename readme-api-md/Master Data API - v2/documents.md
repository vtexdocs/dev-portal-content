---
title: "Documents"
slug: "documents"
hidden: false
createdAt: "2019-12-16T06:09:28.493Z"
updatedAt: "2019-12-16T22:39:51.771Z"
---
The APIs within this group are used to save documents and query them by id.

If the document has the id attribute or has fields that have been set to indexes with unique values, VTEX Master Data will attempt to identify the document. If the document is found a change will be made. If it is not found, an inclusion will be made. ** This scenario does not apply to the API with the POST verb**.

Otherwise, a new document will always be created.

You can use the query string `_where` to apply an update only if the document is compliant with the clause.

In addition with this feature you can use the schema parameter `_schema` to apply the update only if the document is compliant with the schema.

### Response status code

1. Status Code 201: Document created successfully
2. Status Code 200: Document changed successfully
3. Status Code 304: There were no changes to the document
4. Status Code 400: Invalid information in JSON
5. Status Code 403: Unauthorized access