---
title: "I can't update the EAN of my SKUs via API"
slug: "i-cant-update-the-ean-of-my-skus-via-api"
hidden: false
createdAt: "2024-07-17T12:40:00.508Z"
updatedAt: "2024-09-02T09:20:00.508Z"
tags:
    - catalog
    - sku
---

**Product tags:** Catalog

**Keywords:** SKU, product, EAN, catalog

When trying to update the EAN (European Article Number), which contains the barcode information for a SKU, you may face issues with catalog synchronization between the VTEX Admin and API. This can impact inventory management and customer experience.

## Solution

To solve this issue, consider [deleting the SKU EAN](#deleting-the-sku-ean) and then [adding a new EAN](#step-1-add-a-new-ean-to-the-sku). 

### Deleting the SKU EAN

To update the current SKU EAN, you must first delete all the EAN values associated with the SKU.

- [Delete SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/ean/-ean-): Use the endpoint to delete a specific EAN.
- [Delete all SKU EAN values](https://developers.vtex.com/docs/api-reference/catalog-api#delete-/api/catalog/pvt/stockkeepingunit/-skuId-/ean): Use the endpoint to delete all the EANs associated with the SKU.

#### Step 1 - Add a new EAN to the SKU

Only after all previous EANs have been deleted can you add a new EAN to the SKU. To do this, use the [Create SKU EAN](https://developers.vtex.com/docs/api-reference/catalog-api#post-/api/catalog/pvt/stockkeepingunit/-skuId-/ean/-ean-) endpoint to create the new EAN value.

#### Step 2 - Check whether the SKU EAN has been updated

After adding the new EAN, use the [Get SKU by EAN](https://developers.vtex.com/docs/api-reference/catalog-api#get-/api/catalog_system/pvt/sku/stockkeepingunitbyean/-ean-) endpoint to confirm it has been updated. The new EAN values will be displayed in the `AlternateIdValues` array.

```json
"AlternateIdValues":
[
"8781",
"878181"
]
```
