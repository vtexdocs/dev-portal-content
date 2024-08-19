---
title: "My store catalog does not show the price range filter"
slug: "my-store-catalog-does-not-show-the-price-range-filter"
hidden: false
createdAt: "2024-08-19T00:00:00.000Z"
updatedAt: ""
---

# My store catalog does not show the price range filter
**Keywords:** price range |  filters |  catalog

The price range functionality allows you to [create a filter](https://help.vtex.com/en/tutorial/setting-up-the-price-range-filter--tutorials_240) containing price ranges that can be displayed to the customer in the store.

After creating [price range filters](https://help.vtex.com/en/tutorial/setting-up-the-price-range-filter--tutorials_240) in your store catalog, there may be rendering issues and they may not display on the product listing page (PLP).

![](https://raw.githubusercontent.com/vtexdocs/.png)

In some situations, price filters may have rendering issues and may not be shown on the product listing page (PLP).

## ## Solution
To solve this problem, consider checking the information below:

- [Price ranges filter configuration](#check-price-ranges-filter-configuration)
- [simulationBehavior](#heading=h.miblh2erzort)[ field value](#check-simulationBehavior-field-value)
- [priceRange](#heading=h.jzixxyx4uel6)[ field value](#check-priceRange-field-value)

### Check price ranges filter configuration

To confirm that the price range filters have been properly configured, follow the steps below:

1. In the VTEX Admin, go to **Catalog > Categories.**
2. Click on the desired category.
3. Click on **ACTIONS** and **Price range**.
4. Check the registered price ranges and make changes, if necessary.

![](https://raw.githubusercontent.com/vtexdocs/.png)

### Check `simulationBehavior` field value

Access your [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) app and in the `store.search` parameter, check if the property `simulationBehavior` is set as `default`.

```json
{
    "store.search": {
        "blocks": [
            "search-result-layout"
        ],
        "props": {
            "context": {
                "skusFilter": "FIRST_AVAILABLE",
                "simulationBehavior": "default"
            }
        }
    }
}
```

### Check `priceRange` field value

1. Access your [Search Result](https://developers.vtex.com/docs/apps/vtex.search-result) and within the `search-result-layout.desktop` and `search-result-layout.mobile` blocks, verify that the property `priceRange` exists and is set to `false`.
2. Verify if the custom filter property follows the default value `false`. If it is `true`, its value should not appear.

> ⚠️ If this field does not exist or the value is true, the price range filter will not be displayed in the store.

```json
…
"search-result-layout.desktop": {
        "children": [
            "flex-layout.row#searchbread",
            "flex-layout.row#searchtitle",
            "flex-layout.row#result",
        …
        ],
        "props": {
            "hiddenFacets": {
               "priceRange": false
        },
        …
    }
…
```

```json
…
"search-result-layout.mobile": {
        "children": [
            "flex-layout.row#searchbread",
            "flex-layout.row#searchtitle",
            "flex-layout.row#result",
        …
        ],
        "props": {
            "hiddenFacets": {
               "priceRange": false
        },
        …
    }
…
```
