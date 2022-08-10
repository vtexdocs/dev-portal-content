---
title: "Update Brand"
slug: "catalog-api-put-brand"
excerpt: "Updates a previously existing Brand."
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2022-05-20T22:23:43.804Z"
---
## Request body has the following properties:
| Attribute              | Type    | Description                                                  |
| ---------------------- | ------- | ------------------------------------------------------------ |
| Id                     | integer | Brand’s numerical identifier                                 |
| Name                   | string  | Brand’s name                                                 |
| Text                   | string  | Brand’s description                                          |
| Keywords               | string  | Substitutes words for the Brand                              |
| SiteTitle              | string  | Brand’s page title                                           |
| Active                 | boolean | If the Brand is active                                       |
| MenuHome               | boolean | If the Brand shows on the home menu or not                   |
| AdWordsRemarketingCode | string  | Shows the specific code for the AdWords remarketing platform |
| LomadeeCampaignCode    | string  | Shows the specific code for the LomadeeCampaig               |
| Score                  | integer | Score for search ordination                                  |
| LinkId                 | string  | Brand’s link ID                                              |


## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n   \"Id\": 2000003,\n   \"Name\": \"Orma Carbono\",\n   \"Text\": \"Orma Carbon\",\n   \"Keywords\": \"orma\",\n   \"SiteTitle\": \"Orma Carbon\",\n   \"Active\": true,\n   \"MenuHome\": true,\n   \"AdWordsRemarketingCode\": \"\",\n   \"LomadeeCampaignCode\": \"\",\n   \"Score\": null,\n   \"LinkId\": \"Orma-Carbon\"\n}\n",
      "language": "json"
    }
  ]
}
[/block]

## Response body has the following properties:
| Attribute              | Type    | Description                                                  |
| ---------------------- | ------- | ------------------------------------------------------------ |
| Id                     | integer | Brand’s numerical identifier                                 |
| Name                   | string  | Brand’s name                                                 |
| Text                   | string  | Brand’s description                                          |
| Keywords               | string  | Substitutes words for the Brand                              |
| SiteTitle              | string  | Brand’s page title                                           |
| Active                 | boolean | If the Brand is active                                       |
| MenuHome               | boolean | If the Brand shows on the home menu or not                   |
| AdWordsRemarketingCode | string  | Shows the specific code for the AdWords remarketing platform |
| LomadeeCampaignCode    | string  | Shows the specific code for the LomadeeCampaig               |
| Score                  | integer | Score for search ordination                                  |
| LinkId                 | string  | Brand’s link ID                                              |


## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 2000000,\n    \"Name\": \"Orma Carbono\",\n    \"Text\": \"Orma Carbon\",\n    \"Keywords\": \"orma\",\n    \"SiteTitle\": \"Orma Carbon\",\n    \"Active\": true,\n    \"MenuHome\": true,\n    \"AdWordsRemarketingCode\": \"\",\n    \"LomadeeCampaignCode\": \"\",\n    \"Score\": null,\n    \"LinkId\": \"Craft\"\n}",
      "language": "json"
    }
  ]
}
[/block]