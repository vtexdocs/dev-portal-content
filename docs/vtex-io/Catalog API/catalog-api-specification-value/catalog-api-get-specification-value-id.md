---
title: "Get Specification Value"
slug: "catalog-api-get-specification-value-id"
excerpt: "Retrieves general information about a Specification Value"
hidden: false
createdAt: "2020-04-16T15:43:24.310Z"
updatedAt: "2020-04-22T20:32:46.942Z"
---
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
      "code": "{\n    \"Id\": 18,\n    \"FieldTypeId\": 9,\n    \"CategoryId\": 1,\n    \"FieldGroupId\": 5,\n    \"Name\": \"Percentual\",\n    \"Description\": \"%\",\n    \"Position\": 1,\n    \"IsFilter\": false,\n    \"IsRequired\": true,\n    \"IsOnProductDetails\": true,\n    \"IsStockKeepingUnit\": false,\n    \"IsWizard\": false,\n    \"IsActive\": true,\n    \"IsTopMenuLinkActive\": true,\n    \"IsSideMenuLinkActive\": true,\n    \"DefaultValue\": \"\"\n}\n",
      "language": "json"
    }
  ]
}
[/block]