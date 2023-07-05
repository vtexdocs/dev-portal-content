---
title: "Search API: "Teasers" field deprecation"
slug: "2023-07-06-search-api-teasers-field-deprecation"
excerpt: "From September 2023, the Teasers field in Search API requests will be deprecated."
hidden: false
createdAt: "2023-07-06T15:54:00.000Z"
type: "deprecated"
---

From September 2023, the `Teasers` field in [Search API requests](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search) will be deprecated. While some VTEX stores may use this entity to create integrations, we recommend using the new `PromotionTeasers` field as it provides more straightforward information. We encourage all users to update their integrations accordingly to ensure a seamless transition.

## What has changed?

We have already added the `PromotionTeasers` field to Search API endpoints. Currently, both fields coexist, and it is possible to view previously recorded information. From September 2023, VTEX will deprecate the `Teasers` field for all accounts and maintain `PromotionTeasers` only.

### Before  - "Teasers" example

```json
"Teasers": [
    {
        "<Name>k__BackingField": "AdditionalInfo",
        "<GeneralValues>k__BackingField": {
            "Team": "Flamengo",
            "Name": "Pedro",
            "Number": "9"
        },
        "<Conditions>k__BackingField": {
            "<MinimumQuantity>k__BackingField": 0,
            "<Parameters>k__BackingField": [
                {
                    "<Name>k__BackingField": "PaymentMethodId",
                    "<Value>k__BackingField": "4"
                }
            ]
        },
        "<Effects>k__BackingField": {
            "<Parameters>k__BackingField": [
                {
                    "<Name>k__BackingField": "PercentualDiscount",
                    "<Value>k__BackingField": "1"
                }
            ]
        }
    }
]
```

### After - "PromotionTeasers" example

```json
"PromotionTeasers": [
    {
        "Name": "AdditionalInfo",
        "GeneralValues": {
            "Team": "Flamengo",
            "Name": "Pedro",
            "Number": "9"
        },
        "Conditions": {
            "MinimumQuantity": 0,
            "Parameters": [
                {
                    "Name": "PaymentMethodId",
                    "Value": "4"
                }
            ]
        },
        "Effects": {
            "Parameters": [
                {
                    "Name": "PercentualDiscount",
                    "Value": "1"
                }
            ]
        }
    }
]
```



## What needs to be done?

If you have integrations that depend on the `Teasers` field, you must adapt your implementation to use `PromotionTeasers` instead as soon as possible. You can find more information about the new field in [Search API reference](https://developers.vtex.com/docs/api-reference/search-api#get-/api/catalog_system/pub/products/search).
