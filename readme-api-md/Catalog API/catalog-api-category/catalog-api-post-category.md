---
title: "Create Category"
slug: "catalog-api-post-category"
excerpt: "Creates a new Category.\r\n  ## Request body example\r\n\r\n```json\r\n{\r\n    \"Name\": \"Home Appliances\",\r\n    \"FatherCategoryId\": null,\r\n    \"Title\": \"Home Appliances\",\r\n    \"Description\": \"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\",\r\n    \"Keywords\": \"Kitchen, Laundry, Appliances\",\r\n    \"IsActive\": true,\r\n    \"LomadeeCampaignCode\": null,\r\n    \"AdWordsRemarketingCode\": null,\r\n    \"ShowInStoreFront\": true,\r\n    \"ShowBrandFilter\": true,\r\n    \"ActiveStoreFrontLink\": true,\r\n    \"GlobalCategoryId\": 800,\r\n    \"StockKeepingUnitSelectionMode\": \"SPECIFICATION\",\r\n    \"Score\": null\r\n}\r\n```\r\n\r\n## Response body example\r\n\r\n```json\r\n{\r\n    \"Id\": 1,\r\n    \"Name\": \"Home Appliances\",\r\n    \"FatherCategoryId\": null,\r\n    \"Title\": \"Home Appliances\",\r\n    \"Description\": \"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\",\r\n    \"Keywords\": \"Kitchen, Laundry, Appliances\",\r\n    \"IsActive\": true,\r\n    \"LomadeeCampaignCode\": \"\",\r\n    \"AdWordsRemarketingCode\": \"\",\r\n    \"ShowInStoreFront\": true,\r\n    \"ShowBrandFilter\": true,\r\n    \"ActiveStoreFrontLink\": true,\r\n    \"GlobalCategoryId\": 3367,\r\n    \"StockKeepingUnitSelectionMode\": \"LIST\",\r\n    \"Score\": null,\r\n    \"LinkId\": \"Alimentacao\",\r\n    \"HasChildren\": true\r\n}\r\n```"
hidden: false
createdAt: "2020-03-03T21:03:42.777Z"
updatedAt: "2022-09-09T19:28:14.024Z"
---
## Request body has the following properties:


| Attribute                       | Type    | Description                                                          | Required? |
| ------------------------------- | ------- | -------------------------------------------------------------------- | --------- |
| `Id`                          | integer  | Category ID                                   | No       |
| `Name`                          | string  | Category name (150 characters max)                                   | Yes       |
| `Keywords`                      | string  | Substitute words for the Category                                    | No        |
| `Title`                         | string  | Text used in title tag for Category page                             | No        |
| `Description`                   | string  | Text used in meta description tag for Category page                  | No        |
| `AdWordsRemarketingCode`        | string  | Shows the specific code for the AdWords remarketing platform         | No        |
| `LomadeeCampaignCode`           | string  | Shows the specific code for the LomadeeCampaign                      | No        |
| `FatherCategoryId`              | integer | ID of the parent category, apply in case of category and subcategory | No        |
| `GlobalCategoryId`              | integer | google_product_category for Google Merchant Center                   | No        |
| `ShowInStoreFront`              | boolean | If true, Category is shown in the top and side menu                  | No        |
| `IsActive`                      | boolean | If true, Category page becomes available in store                    | No        |
| `ActiveStoreFrontLink`          | boolean | If true, Category links become active in store                       | No        |
| `ShowBrandFilter`               | boolean | If true, Category page displays a Brand filter                       | No        |
| `Score`                         | integer | Score for search sorting order                                       | No        |
| `StockKeepingUnitSelectionMode` | string  | Product display mode (see table below)                               | No        |

See more details in our Help Center article: [Filling in Category registration fields](https://help.vtex.com/tutorial/category-registration-fields--5Z7RrvW41yumyQCmk2iqoG).

### Product display modes (`StockKeepingUnitSelectionMode` parameter)
[block:parameters]
{
  "data": {
    "0-0": "LIST",
    "1-0": "COMBO",
    "2-0": "RADIO",
    "3-0": "SPECIFICATION",
    "h-0": "Value",
    "0-1": "List of SKUs",
    "1-1": "Combo Boxes",
    "2-1": "Icons with radio selection (radio box)",
    "3-1": "Following definition of SKU specification",
    "h-1": "Description"
  },
  "cols": 2,
  "rows": 4
}
[/block]
## Request body example
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Name\": \"Home Appliances\",\n    \"Keywords\": \"Kitchen, Laundry, Appliances\",\n    \"Title\": \"Home Appliances\",\n    \"Description\": \"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\",\n    \"AdWordsRemarketingCode\": null,\n    \"LomadeeCampaignCode\": null,\n    \"FatherCategoryId\": null,\n    \"GlobalCategoryId\": 222,\n    \"ShowInStoreFront\": true,\n    \"IsActive\": true,\n    \"ActiveStoreFrontLink\": true,\n    \"ShowBrandFilter\": true,\n    \"Score\": null,\n    \"StockKeepingUnitSelectionMode\": \"SPECIFICATION\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response has the following properties:

| Attribute | Type    | Description                   |
| --------- | ------- | ----------------------------- |
| `Id`      | integer | Category numerical identifier |
| `Name`       | string  | Category name |
| `FatherCategoryId`              | integer | ID of the parent category, apply in case of category and subcategory |
| `Title`                         | string  | Text used in title tag for Category page                             |
| `Description`                   | string  | Text used in meta description tag for Category page                  |
| `Keywords`                      | string  | Substitute words for the Category                                    |
| `IsActive`                      | boolean | If true, Category page becomes available in store                    |
| `LomadeeCampaignCode`           | string  | Shows the specific code for the LomadeeCampaign                      |
| `AdWordsRemarketingCode`        | string  | Shows the specific code for the AdWords remarketing platform         |
| `ShowInStoreFront`              | boolean | If true, Category is shown in the top and side menu                  |
| `ShowBrandFilter`               | boolean | If true, Category page displays a Brand filter                       |
| `ActiveStoreFrontLink`          | boolean | If true, Category links become active in store                       |
| `GlobalCategoryId`              | integer | google_product_category for Google Merchant Center                   |
| `StockKeepingUnitSelectionMode` | string  | Product display mode (see table below)                               |
| `Score`                         | integer | Score for search sorting order                                       |
| `LinkId`                         | string | Text Link |
| `HasChildren`                         | boolean | If the Category has a Category Child |