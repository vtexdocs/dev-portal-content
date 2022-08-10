---
title: "Get SKU’s review information"
slug: "get-sku-review-information"
excerpt: "The **Review Received SKUs** API allows marketplace operators to request sellers to review the sent SKUs that were either refused or pending approval. Thus, marketplace operators can point out the exact fields that need sellers’ review. This endpoint allows the user to retrieve the review information from a specific SKU. This call's response includes the following attributes:"
hidden: false
createdAt: "2020-12-18T21:45:22.148Z"
updatedAt: "2021-02-01T19:23:38.486Z"
---
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"closed\": true,\n        \"fields\": {},\n        \"userRequested\": \"email1@email.com\",\n        \"when\": \"2020-12-01T14:47:59.4358442Z\"\n    },\n    {\n        \"closed\": true,\n        \"fields\": {\n            \"reviewTitle\": \"Review product description\",\n            \"reviewDescription\": \"Description exceeds character limit\"\n        },\n        \"userRequested\": \"email2@email.com\",\n        \"when\": \"2021-01-14T18:05:22.9798321Z\"\n    },\n    {\n        \"closed\": true,\n        \"fields\": {\n            \"reviewTitle\": \"Product Image\",\n            \"reviewDescription\": \"Product image has low quality\"\n        },\n        \"userRequested\": \"email3@email.com\",\n        \"when\": \"2021-01-21T13:49:38.3392656Z\"\n    }\n]",
      "language": "text",
      "name": "Response body example"
    }
  ]
}
[/block]