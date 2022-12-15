---
title: "Create Specification"
slug: "catalog-api-post-specification"
excerpt: "Creates a new Product or SKU Specification. \r\n## Request body example\r\n\r\n```json\r\n{\r\n    \"FieldTypeId\": 1,\r\n    \"CategoryId\": 4,\r\n    \"FieldGroupId\": 20,\r\n    \"Name\": \"Material\",\r\n    \"Description\": \"Composition of the product.\",\r\n    \"Position\": 1,\r\n    \"IsFilter\": true,\r\n    \"IsRequired\": true,\r\n    \"IsOnProductDetails\": false,\r\n    \"IsStockKeepingUnit\": false,\r\n    \"IsActive\": true,\r\n    \"IsTopMenuLinkActive\": false,\r\n    \"IsSideMenuLinkActive\": true,\r\n    \"DefaultValue\": \"Cotton\"\r\n}\r\n```\r\n\r\n## Response body example\r\n\r\n```json\r\n{\r\n    \"Id\": 88,\r\n    \"FieldTypeId\": 1,\r\n    \"CategoryId\": 4,\r\n    \"FieldGroupId\": 20,\r\n    \"Name\": \"Material\",\r\n    \"Description\": \"Composition of the product.\",\r\n    \"Position\": 1,\r\n    \"IsFilter\": true,\r\n    \"IsRequired\": true,\r\n    \"IsOnProductDetails\": false,\r\n    \"IsStockKeepingUnit\": false,\r\n    \"IsWizard\": false,\r\n    \"IsActive\": true,\r\n    \"IsTopMenuLinkActive\": false,\r\n    \"IsSideMenuLinkActive\": true,\r\n    \"DefaultValue\": \"Cotton\"\r\n}\r\n```"
hidden: false
createdAt: "2020-03-15T18:58:38.467Z"
updatedAt: "2022-11-25T00:41:23.104Z"
---
[block:callout]
{
  "type": "warning",
  "title": "",
  "body": "SKU Fields can be only of the Radio or Combo type."
}
[/block]