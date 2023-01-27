---
title: "Catalog management for VTEX Marketplace"
slug: "external-seller-integration-vtex-marketplace-operation"
hidden: false
createdAt: "2020-09-01T16:51:41.370Z"
updatedAt: "2022-07-26T18:58:00.596Z"
---
After you build the integration flow explained in the last section of this guide, there is a final configuration step before the marketplace is ready to start receiving SKU offers from the external seller.

## Map the brands, categories, and specifications

For the external seller's offers to integrate into a VTEX marketplace, its brands, categories, and specifications need to be properly mapped in the marketplace. This is necessary for the marketplace to know where to fit each SKU in its catalog structure.

The action is performed in the marketplace's management panel. Read the article [Mapping categories, brands, and specifications for the marketplace](https://help.vtex.com/en/tutorial/mapping-categories-and-brands-for-the-marketplace) for more information on how to do it.

## Approve the seller's SKU offers

The sellers' SKUs are not added directly to the marketplace's catalog. Instead, there is an approval step for each new SKU, which is done by the marketplace in its management panel.

New SKUs are sent by the seller as suggestions, as explained in the section [External Seller Connector](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-connector). Each suggestion is approved or denied by the marketplace in the Received SKUs panel, which can be done individually or in bulk.

To learn more about how to manage suggestions, read our documentation about [Cataloging received SKUs](https://help.vtex.com/tutorial/manual-sku-cataloging--tutorials_396).