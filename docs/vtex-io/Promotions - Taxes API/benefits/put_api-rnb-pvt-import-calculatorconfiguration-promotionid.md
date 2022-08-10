---
title: "Update Multiple SKU Promotion"
slug: "put_api-rnb-pvt-import-calculatorconfiguration-promotionid"
excerpt: "Updates information from a Multiple SKU Promotion. This scenario allows to create a single promotion for multiples SKUs with the Percentage Effect"
hidden: false
createdAt: "2020-09-17T19:28:49.756Z"
updatedAt: "2021-03-04T21:10:07.178Z"
---
## Body params
You must upload a CSV file to the body param. This should be sent as a raw text on the request body. The file must contain the SKU ID and the percentage of the discount. Use the example below as a reference. 
[block:code]
{
  "codes": [
    {
      "code": "sku,effect\n1,10\n2,12\n3,15\n4,10.5",
      "language": "text",
      "name": "CSV File"
    }
  ]
}
[/block]
The first line must have the headers `sku` and `effect`. The next lines must be the SKU ID and the percentage, without any spaces. For decimal values, use `.` as in `10.5`. 
[block:callout]
{
  "type": "warning",
  "title": "Attention",
  "body": "The CSV file has a maximum of 400 lines."
}
[/block]