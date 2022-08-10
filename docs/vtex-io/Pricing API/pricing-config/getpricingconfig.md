---
title: "Get Pricing Config"
slug: "getpricingconfig"
excerpt: "Retrieves Pricing Module Configuration"
hidden: false
createdAt: "2019-12-30T17:39:05.877Z"
updatedAt: "2020-10-08T21:19:21.604Z"
---
Retrieve Pricing Module Configuration

> know more about [Prices in VTEX Help](https://help.vtex.com/en/tutorial/prices-v2)




## Response body has the following properties:


| Attribute    | Type        | Description |
| ------------ |:-----------:| -----------:|
| `hasMigrated` | boolean |  If has migrated to Pricing V2 |
| `migrationStatus` | string | Pricing v2 Migration Status |
| `defaultMarkup` | integer | Account Default Markup |
| `priceVariation` | object | Price Variation Object |
| `upperLimit` | integer | Upper Variation Limit |
| `lowerLimit` | integer | Lower Variation Limit |
| `minimumMarkups` | integer | Account Minimum Markup |
| `tradePolicyConfigs` | object |  Trade Policy Configurations Object |
| `tradePolicyId` | string | Trade Policy Id |
| `minimumMarkup` | integer | Trade Policy Minimum Markup |
| `rulesShouldAffectListPrice` | boolean | If Price Rule should affect list price too |
| `sellersToOverride` | array of objects | Overrides prices from sellers |
| `hasPriceInheritance` | boolean |  Deprecated. Use the field `priceInheritance` instead. |
| `priceInheritance` | string |  Condition of price inheritance from its parent account. This field can have three possible values - **"never"** to the store should never inherit prices, **"nonexistent"** to the store should only inherit prices in case of nonexistent prices for a given product, and **"always"** to the store should always inherit prices, regardless of its own prices. |
| `hasOptionalBasePrice` | boolean | If optional base price is allowed |
| `blockAccount` | boolean | If access to the Pricing APIs is blocked for external requests |
| `blockedRoutes` | object | Array with all blocked routes |
| `priceTableSelectionStrategy` | string | The strategy used to get prices when there is more than one option. Possible values: `first`, `highest`, `lowest`. Default: `first` |
| `priceTableLimit` | integer |  |

## Response body example:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"hasMigrated\": true,\n    \"migrationStatus\": \"Completed\",\n    \"defaultMarkup\": 30,\n    \"priceVariation\": {\n        \"upperLimit\": null,\n        \"lowerLimit\": null\n    },\n    \"minimumMarkups\": null,\n    \"tradePolicyConfigs\": [],\n    \"sellersToOverride\": [],\n    \"hasPriceInheritance\": false,\n    \"priceInheritance\": \"never\",\n    \"hasOptionalBasePrice\": false,\n    \"blockAccount\": false,\n    \"blockedRoutes\": null,\n    \"priceTableSelectionStrategy\": \"first\",\n    \"priceTableLimit\": null\n}",
      "language": "json"
    }
  ]
}
[/block]
## Authentication


This is a private API and need credentials with viewer access


> know more about [Creating appKeys and appTokens to authenticate integrations](https://help.vtex.com/en/tutorial/creating-appkeys-and-apptokens-to-authenticate-integrations)