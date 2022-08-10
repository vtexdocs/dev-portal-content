---
title: "Create Specification"
slug: "catalog-api-post-specification"
excerpt: "Creates a new Product or SKU Specification."
hidden: false
createdAt: "2020-03-15T18:58:38.467Z"
updatedAt: "2022-05-20T22:23:45.037Z"
---
[block:callout]
{
  "type": "warning",
  "title": "Attention:",
  "body": "SKU Field can be only of the Radio or Combo type"
}
[/block]
## Request body has the following properties:

| Attribute            | Type    | Description                                                                                                                                    |
| -------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| FieldTypeId          | integer | Field Type can be 1 - Text, 2 - Multi-Line Text, 4 - Number, 5 - Combo, 6 - Radio, 7 - Checkbox, 8 - Indexed Text, 9 - Indexed Multi-Line Text |
| CategoryId           | integer | Category ID                                                                                                                                    |
| FieldGroupId         | integer | ID of the Group of Specifications that contains the new Specification                                                                          |
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


## Request body example:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"FieldTypeId\": 1,\n    \"CategoryId\": 4,\n    \"FieldGroupId\": 20,\n    \"Name\": \"Test\",\n    \"Description\": \"Test\",\n    \"Position\": 1,\n    \"IsFilter\": true,\n    \"IsRequired\": true,\n    \"IsOnProductDetails\": false,\n    \"IsStockKeepingUnit\": false,\n    \"IsActive\": true,\n    \"IsTopMenuLinkActive\": false,\n    \"IsSideMenuLinkActive\": true,\n    \"DefaultValue\": \"Test\"\n}",
      "language": "json"
    }
  ]
}
[/block]

## Response body has the following properties:

| Attribute            | Type    | Description                                                                                                                                  |
| -------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Id                   | integer | Created Specification’s ID                                                                                                                   |
| FieldTypeId          | integer | Field Type can be 1 - Texto, 2 - Texto Grande, 4 - Número, 5 - Combo, 6 - Radio, 7 - Checkbox, 8 - Texto Indexado, 9 - Texto Grande Indexado |
| CategoryId           | integer | Category ID                                                                                                                                  |
| FieldGroupId         | integer | Numerical ID of the Group of Specifications that contains the new Specification                                                              |
| Name                 | string  | Specification Name                                                                                                                           |
| Description          | string  | Specification Description                                                                                                                    |
| Position             | integer | The current Specification position in comparison to the others                                                                               |
| IsFilter             | boolean | If the Specification can be used as a Filter                                                                                                 |
| IsRequired           | boolean | If the Specification is required or not                                                                                                      |
| IsOnProductDetails   | boolean | If the Specification will be shown on the Product screen in the specification area                                                           |
| IsStockKeepingUnit   | boolean | If the Specification is applied to a specific SKU                                                                                            |
| IsWizard             | boolean | Deprecated                                                                                                                                   |
| IsActive             | boolean | If the Specification is active or not                                                                                                        |
| IsTopMenuLinkActive  | boolean | Shows if the Specification is shown in the main menu of the site                                                                             |
| IsSideMenuLinkActive | boolean | Shows if the Specification is shown in the side menu                                                                                         |
| DefaultValue         | string  | Specification Default Value                                                                                                                  |