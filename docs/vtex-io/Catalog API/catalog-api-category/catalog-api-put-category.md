---
title: "Update Category"
slug: "catalog-api-put-category"
excerpt: "Updates a previously existing Category"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-04-17T15:47:25.927Z"
---
## Request body has the following properties:

| Attribute                     | Type    | Description                                                          |
| ----------------------------- | ------- | -------------------------------------------------------------------- |
| Name                          | string  | Category Name                                                        |
| FatherCategoryId              | integer | ID of the father category, apply in case of category and subcategory |
| Title                         | string  | Category Title                                                       |
| Description                   | string  | Describes details about the Category                                 |
| Keywords                      | string  | Substitutes words for the Category                                   |
| IsActive                      | boolean | Shows if the Category is active or not                               |
| LomadeeCampaignCode           | string  | Shows the specific code for the LomadeeCampaign                      |
| AdWordsRemarketingCode        | string  | Shows the specific code for the AdWords remarketing platform         |
| ShowInStoreFront              | boolean | Shows if is on side and upper menu                                   |
| ShowBrandFilter               | boolean | If Category has Brand filter                                         |
| ActiveStoreFrontLink          | boolean | If the Category has an active link on the website                    |
| GlobalCategoryId              | integer | Google Global Category ID                                            |
| StockKeepingUnitSelectionMode | string  | Shows how the SKU will be exhibit                                    |

## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Name\": \"Home Appliances\",\n    \"FatherCategoryId\": null,\n    \"Title\": \"Home Appliances\",\n    \"Description\": \"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\",\n    \"Keywords\": \"Kitchen, Laundry, Appliances\",\n    \"IsActive\": true,\n    \"LomadeeCampaignCode\": null,\n    \"AdWordsRemarketingCode\": null,\n    \"ShowInStoreFront\": true,\n    \"ShowBrandFilter\": true,\n    \"ActiveStoreFrontLink\": true,\n    \"GlobalCategoryId\": 800,\n    \"StockKeepingUnitSelectionMode\": \"SPECIFICATION\",\n    \"Score\": null\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute                     | Type    | Description                                                          |
| ----------------------------- | ------- | -------------------------------------------------------------------- |
| Id                            | integer | Category ID                                                          |
| Name                          | string  | Category Name                                                        |
| FatherCategoryId              | integer | ID of the father category, apply in case of category and subcategory |
| Title                         | string  | Category Title                                                       |
| Description                   | string  | Describes details about the Category                                 |
| Keywords                      | string  | Substitutes words for the Category                                   |
| IsActive                      | boolean | Shows if the Category is active or not                               |
| LomadeeCampaignCode           | string  | Shows the specific code for the LomadeeCampaign                      |
| AdWordsRemarketingCode        | string  | Shows the specific code for the AdWords remarketing platform         |
| ShowInStoreFront              | boolean | Shows if is on the side and upper menu                                   |
| ShowBrandFilter               | boolean | If Category has Brand filter                                         |
| ActiveStoreFrontLink          | boolean | If the Category has an active link on the website                    |
| GlobalCategoryId              | integer | Google Global Category ID                                            |
| StockKeepingUnitSelectionMode | string  | Shows how the SKU will be exhibit                                    |
| Score                         | integer | Score for search ordination                                          |
| LinkId                        | string  | Text Link                                                            |
| HasChildren                   | boolean | If the Category has a Category Child                                 |


## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 1,\n    \"Name\": \"Home Appliances\",\n    \"FatherCategoryId\": null,\n    \"Title\": \"Home Appliances\",\n    \"Description\": \"Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\",\n    \"Keywords\": \"Kitchen, Laundry, Appliances\",\n    \"IsActive\": true,\n    \"LomadeeCampaignCode\": \"\",\n    \"AdWordsRemarketingCode\": \"\",\n    \"ShowInStoreFront\": true,\n    \"ShowBrandFilter\": true,\n    \"ActiveStoreFrontLink\": true,\n    \"GlobalCategoryId\": 3367,\n    \"StockKeepingUnitSelectionMode\": \"LIST\",\n    \"Score\": null,\n    \"LinkId\": \"Alimentacao\",\n    \"HasChildren\": true\n}",
      "language": "json"
    }
  ]
}
[/block]