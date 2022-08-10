---
title: "Update Specification"
slug: "catalog-api-put-specification"
excerpt: "Updates a Product or SKU Specification"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2021-03-02T16:11:03.833Z"
---
## Request body has the following properties:

| Attribute            | Type    | Description                                                                                                                                    |
| -------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| FieldTypeId          | integer | Field Type can be 1 - Text, 2 - Multi-Line Text, 4 - Number, 5 - Combo, 5 - Radio, 7 - Checkbox, 8 - Indexed Text, 9 - Indexed Multi-Line Text |
| CategoryId           | integer | Specification Category ID                                                                                |
| FieldGroupId         | integer | Numerical ID of the Group of Specifications that contains the new Specification                                                                |
| Name                 | string  | Specification Name                                                                                              |
| Description          | string  | Specification Description                                                                                 |
| Position             | integer | The current Specification position in comparison to the others                      |
| IsFilter             | boolean | If the Specification can be used as a Filter                                                        |
| IsRequired           | boolean | If the Specification is required or not                                                            |
| IsOnProductDetails   | boolean | If the Specification will be shown on the Product screen in the specification area                                                             |
| IsStockKeepingUnit   | boolean | If the Specification is applied to a specific SKU                                    |
| IsWizard             | boolean | Deprecated                                                                                                      |
| IsActive             | boolean | If the Specification is active or not                                                                  |
| IsTopMenuLinkActive  | boolean | Shows if the Specification is shown in the main menu of the site      |
| IsSideMenuLinkActive | boolean | Shows if the Specification is shown in the side menu                       |
| DefaultValue         | string  | Specification Default Value                                                                            |


## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldTypeId\": 5,\n    \"CategoryId\": 1,\n    \"FieldGroupId\": 13,\n    \"Name\": \"Test\",\n    \"Description\": \"Test\",\n    \"Position\": 1,\n    \"IsFilter\": true,\n    \"IsRequired\": true,\n    \"IsOnProductDetails\": true,\n    \"IsStockKeepingUnit\": false,\n    \"IsWizard\": false,\n    \"IsActive\": false,\n    \"IsTopMenuLinkActive\": false,\n    \"IsSideMenuLinkActive\": true,\n    \"DefaultValue\": \"Test\"\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body has the following properties:

| Attribute            | Type    | Description                                                                                                                                    |
| -------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Id                   | integer | Created Specification’s ID                                                                                                                     |
| FieldTypeId          | integer | Field Type can be 1 - Text, 2 - Multi-Line Text, 3 - Número, 4 - Combo, 5 - Radio, 6 - Checkbox, 7 - Indexed Text, 8 - Indexed Multi-Line Text |
| CategoryId           | integer | Category ID                                                                                                                                    |
| FieldGroupId         | integer | Numerical ID of the Group of Specifications that contains the new Specification                                                                |
| Name                 | string  | Specification Name                                                                                                                             |
| Description          | string  | Specification Description                                                                                                                      |
| Position             | integer | The current Specification position in comparison to the others                                                                                 |
| IsFilter             | boolean | If the Specification can be used as a Filter                                                                                                   |
| IsRequired           | boolean | If the Specification is required or not                                                                                                        |
| IsOnProductDetails   | boolean | If the Specification will be shown on the Product screen in the specification area                                                             |
| IsStockKeepingUnit   | boolean | If the Specification is applied to a specific SKU                                                                                              |
| IsWizard             | boolean | Deprecated                                                                                                                                     |
| IsActive             | boolean | If the Specification is active or not                                                                                                          |
| IsTopMenuLinkActive  | boolean | Shows if the Specification is shown in the main menu of the site                                                                               |
| IsSideMenuLinkActive | boolean | Shows if the Specification is shown in the side menu                                                                                           |
| DefaultValue         | string  | Specification Default Value                                                                                                                    |


## Response body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"Id\": 25,\n    \"FieldTypeId\": 5,\n    \"CategoryId\": 1,\n    \"FieldGroupId\": 13,\n    \"Name\": \"Test\",\n    \"Description\": \"Test\",\n    \"Position\": 1,\n    \"IsFilter\": true,\n    \"IsRequired\": true,\n    \"IsOnProductDetails\": true,\n    \"IsStockKeepingUnit\": false,\n    \"IsWizard\": false,\n    \"IsActive\": false,\n    \"IsTopMenuLinkActive\": false,\n    \"IsSideMenuLinkActive\": true,\n    \"DefaultValue\": \"Test\"\n}",
      "language": "json"
    }
  ]
}
[/block]