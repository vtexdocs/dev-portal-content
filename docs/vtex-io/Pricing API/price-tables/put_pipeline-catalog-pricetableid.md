---
title: "Update rules for a price table"
slug: "put_pipeline-catalog-pricetableid"
excerpt: "This method will update the rules from a specific Price Table. It will delete all the rules from the requested Price Table and create new rules based on the content of the request"
hidden: false
createdAt: "2020-03-02T07:47:33.056Z"
updatedAt: "2020-03-05T15:07:27.403Z"
---
## Request has the following properties:
| Attribute          | Type    | Description           |
| ------------------ | ------- | --------------------- |
| rules              | object  | Rules for Price Table |
| id                 | integer | Rule ID               |
| context            | object  | Rule Context          |
| categories         | object  | Categories Context    |
| brands             | object  | Brands Context        |
| stockStatuses      | object  | Stock status uses     |
| internalCategories | object  | Internal Categories   |
| markupRange        | object  | Markup Rule           |
| dateRange          | object  | Date Range Rule       |
| percentualModifier | float   | Percentual Modifier   |

## Request body example
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"tradePolicyId\": \"api-teste\",\n    \"rules\": [\n        {\n            \"id\": 1,\n            \"context\": {\n                \"categories\": null,\n                \"brands\": null,\n                \"stockStatuses\": null,\n                \"internalCategories\": null,\n                \"markupRange\": null,\n                \"dateRange\": null\n            },\n            \"percentualModifier\": 70\n        }\n    ]\n}",
      "language": "json"
    }
  ]
}
[/block]