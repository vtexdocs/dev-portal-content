---
title: "Get Specification"
slug: "get_api-catalog-pvt-specification-specificationid"
excerpt: "Retrieves information of a Product or SKU Specification."
hidden: false
createdAt: "2021-06-22T00:21:32.697Z"
updatedAt: "2022-08-05T17:22:36.078Z"
---
## Response body has the following properties:

| Attribute            | Type    | Description                                                                                                                                    |
| -------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Id                   | integer | Created Specification’s ID                                                                                                                     |
| FieldTypeId          | integer | Field Type can be 1 - Text, 2 - Multi-Line Text, 4 - Number, 5 - Combo, 6 - Radio, 7 - Checkbox, 8 - Indexed Text, 9 - Indexed Multi-Line Text |
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
      "code": "{\n   \"Id\": 32,\n   \"FieldTypeId\": 6,\n   \"CategoryId\": 10,\n   \"FieldGroupId\": 11,\n   \"Name\": \"Peso\",\n   \"Description\": \"Peso\",\n   \"Position\": 1,\n   \"IsFilter\": false,\n   \"IsRequired\": true,\n   \"IsOnProductDetails\": false,\n   \"IsStockKeepingUnit\": true,\n   \"IsWizard\": false,\n   \"IsActive\": true,\n   \"IsTopMenuLinkActive\": false,\n   \"IsSideMenuLinkActive\": false,\n   \"DefaultValue\": NULL\n}",
      "language": "json"
    }
  ]
}
[/block]