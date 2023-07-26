---
title: "Setting up white label seller as pickup point"
slug: "setting-up-white-label-seller-as-pickup-point"
hidden: false
createdAt: "2023-07-25T20:30:14.043Z"
updatedAt: "2023-07-25T20:30:14.127Z"
---

Every [franchise account](https://help.vtex.com/en/tutorial/what-is-a-franchise-account--kWQC6RkFSCUFGgY5gSjdl) created in VTEX is also automatically a [white label seller](https://help.vtex.com/en/tutorial/white-label-seller--5orlGHyDHGAYciQ64oEgKa) of the main account. So any [pickup points](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R) configured in the franchise account will be available options for shoppers who place orders in the main account.

>❗ All settings must be made in the franchise account, which is the white label seller. Items will only be displayed at Checkout for shoppers with the pickup point option if the SKU is available in the inventory of the main account and also in the inventory of the franchise account.

## Initial setup

To set up a white label seller as a pickup point, you have to make the following configurations:

- [Pickup point](https://help.vtex.com/en/tutorial/creating-pickup-points--2R5ClQiwe4KoSQgsuiOw4E): create the pickup point with the franchise account address. You can use the [Create/Update Pickup Point](https://developers.vtex.com/docs/api-reference/logistics-api#put-/api/logistics/pvt/configuration/pickuppoints/-pickupPointId-) endpoint.
- [Shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140): set up a shipping policy and link it to a registered pickup point. You can use the [Create shipping policy](https://developers.vtex.com/docs/api-reference/logistics-api#post-/api/logistics/pvt/shipping-policies) endpoint.
- [Loading dock](https://help.vtex.com/en/tutorial/managing-loading-docks--7K3FultD8I2cuuA6iyGEiW): configure a loading dock and link it to the shipping policy associated with the pickup point. You can use the [Create/update dock](https://developers.vtex.com/docs/api-reference/logistics-api#post-/api/logistics/pvt/configuration/docks) endpoint.
- [Warehouse](https://help.vtex.com/en/tutorial/managing-warehouses--tutorials_137): you must configure a warehouse and link it to the shipping policy associated with the pickup point. You can use the [Create/update warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#post-/api/logistics/pvt/configuration/warehouses) endpoint.

## Fill in inventory quantity

After setting the pickup point, the shipping policy, the loading dock, and the warehouse, fill in the quantity of the items in inventory. You can also use the [Update inventory by SKU and warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#put-/api/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-) endpoint.

The franchise account does not have its own catalogue, it inherits products and SKU information from the main account, so it is necessary to update quantity through the [import and export of the inventory spreadsheet](https://help.vtex.com/en/tutorial/importing-and-exporting-an-inventory-spreadsheet--tutorials_2034).

## Validate configuration

When you made the pickup point configurations correctly in the franchise account, SKUs with inventory and price can be sold on the main account. The franchise account will work as white label seller and the main account will work as marketplace.

>❗ Make sure your white label seller is active. In your VTEX Admin, go to __Marketplace > Sellers > Management__, and in the seller row in column _Status_, click `Active`.

### White label seller and franchise account

To check if the white label seller is delivering a SKU through the registered pickup point, use the [Cart simulation endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForms/simulation).

When the configuration was made correctly, the call will return the shipping information of a given SKU. That is enough to check if the shipping is occurring by the registered pickup point.

### Marketplace and main account

To check if the marketplace is including the SKU of the white label seller in the shopping cart, use the [Cart simulation endpoint](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForms/simulation).

The call should return shopping cart information to where the SKU was sent in the context of the request body.
