---
title: "Dynamic expressions in Master Data v2"
slug: "adding-document-field-values-with-dynamic-expressions"
hidden: false
createdAt: "2022-08-03T14:54:11.873Z"
updatedAt: "2022-08-03T14:57:56.514Z"
---
Use dynamic expressions to add a document field value. For example, you can configure the client email to send marketing emails dynamically using triggers. See examples below of how you can set up your JSON schema.
[block:callout]
{
  "type": "info",
  "body": "Learn more about [Master Data v2 schemas](https://developers.vtex.com/vtex-rest-api/docs/starting-to-work-on-master-data-with-json-schema)"
}
[/block]
- trigger JSON
```json
    {
      "action": {
        "to": "{!email}"
      }
    }
```
    
- client document
```json
    {
      "email": "client@email.com"
    }
```
    

## Setting up dynamic expressions

Pattern:

`{!fieldName}`
    
Example:

`{!email}`
    
Access nested fields using a dot.

`{!order.clientProfiledata.email}`