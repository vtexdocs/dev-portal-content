---
title: "Fulfillment"
slug: "fulfillment"
hidden: false
createdAt: "2023-01-11T13:13:50.000Z"
updatedAt: "2023-01-11T13:13:50.000Z"
---

> Help us improve our documentation! Tell us about your experience with this article by filling out [this form](https://forms.gle/fQoELRA1yfKDqmAb8)!

[Fulfillment](https://help.vtex.com/en/tutorial/fulfillment-logistics-vtex--53udnvI5eBy8DKo8FOjMoP) is the process of storing merchandise and receiving, managing, packing and shipping orders. It starts when a shopper buys a product and ends when the life cycle of the order is complete with the shopper receiving the purchase.

This overview article goes over what you can accomplish with VTEX logistics’ capabilities, like the registration and control of your inventory, shipping rates management, items availability control, tracking deliveries, and more.

## Importing inventory from an ERP or Back office

If your store has an ERP integration or another integration for inventory management and shipping, it will be necessary to integrate with VTEX platform. The links below provide a general view of the integration flow between a back office system and a VTEX store regarding inventory:

* [Back office (ERP/PIM/WMS)](https://developers.vtex.com/docs/guides/erp-integration-guide)
* [Import inventory](https://developers.vtex.com/docs/guides/erp-integration-import-inventory)

>ℹ️ If you wish to customize the fulfillment capabilities in the storefront, see the [Checkout guide](https://developers.vtex.com/docs/guides/checkout-overview) overview.

## Understanding fulfillment process

When a shopper selects an item and proceeds to checkout, after entering their location, the VTEX platform:

1. Checks the availability of the item and where it will be picked up from.
2. Selects the place and the time when the [carrier](https://help.vtex.com/tutorial/carries-on-vtex--7u9duMD5UQa2QQwukAWMcE) must collect the item.
3. Calculates the shipping conditions, or Service Level Agreement (SLA), that will be offered to the shopper.

The shopper chooses one option from the shipping conditions displayed and completes the order’s payment. That is when the logistic part of packing and shipping takes place.

The following image summarizes the fulfillment process:

![fulfillment_image_1](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/fulfillment_image_1.svg)

In VTEX, there are specific terms to identify the entities involved in order fulfillment, which can be checked in our [Logistics Glossary](https://help.vtex.com/en/tutorial/logistics-glossary--16DSSiXn548rsidi0A8Hby). An important concept is [Shipping strategy](https://help.vtex.com/en/tutorial/shipping-strategy--58vLBDbjYVQzJ6rRc5QNz3), defined as the relationship between the following entities:

* [Shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140): is a set of rules that define the shipping conditions, including carrier’s working hours, delivery time frames, shipping rates, and more.
* [Loading dock](https://help.vtex.com/en/tutorial/managing-loading-docks--7K3FultD8I2cuuA6iyGEiW): entity that links your products to a shipping policy.
* [Warehouse](https://help.vtex.com/en/tutorial/warehouse--6oIxvsVDTtGpO7y6zwhGpb): location where your products are stored.

The following image shows how these entities connect to each other:

![fulfillment_image_2](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/fulfillment_image_2.svg)

## Setting up shipping strategy (mandatory)

Configuring your shipping strategy means setting up a shipping policy, a loading dock, and a warehouse. For the system to perform as expected, we suggest you follow the order below:

1. [Shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140)
2. [Loading dock](https://help.vtex.com/en/tutorial/managing-loading-docks--7K3FultD8I2cuuA6iyGEiW)
3. [Warehouse](https://help.vtex.com/en/tutorial/warehouse--6oIxvsVDTtGpO7y6zwhGpb)

**In VTEX Admin:** Orders > Inventory & Shipping > Shipping Strategy > Shipping Policies/Loading Docks/Warehouses

**In Redesigned VTEX Admin:** Shipping > Shipping Strategy > Shipping Policies/Loading Docks/Warehouses

### 1. Shipping policy

[Shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140) defines the shipping conditions offered to the shopper at checkout, including costs and deadlines. This shipping policy set of rules includes carriers working hours, shipping capacity, and more.

* [POST - Create shipping policy](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/shipping-policies)

### 2. Loading dock

[Loading dock](https://help.vtex.com/en/tutorial/managing-loading-docks--7K3FultD8I2cuuA6iyGEiW) connects the warehouse to the shipping policy. The loading dock corresponds to a physical location from where products will be shipped. By default, when you create a new loading dock, it is generated as activated.

* [POST - Create/update dock](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/docks)
* [POST - Activate dock](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/docks/-dockId-/activation)

### 3. Warehouse

[Warehouse](https://help.vtex.com/en/tutorial/warehouse--6oIxvsVDTtGpO7y6zwhGpb) is the physical location where you store your products. The items sold go from the warehouse to the loading dock for the carriers to deliver them. By default, when you create a new warehouse, it is generated as activated.

* [POST - Create/update warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/warehouses)
* [POST - Activate warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/warehouses/-warehouseId-/activation)

## Managing Shipping Strategy

Manage your [Shipping strategy](https://help.vtex.com/en/tutorial/shipping-strategy--58vLBDbjYVQzJ6rRc5QNz3) by editing your shipping policies, loading docks, and warehouses.

**In VTEX Admin:** Orders > Inventory & Shipping > Shipping Strategy > Shipping Policies/Loading Docks/Warehouses

**In Redesigned VTEX Admin:** Shipping > Shipping Strategy > Shipping Policies/Loading Docks/Warehouses

### Shipping policy

You can list shipping policies, deactivate, reactivate, update or delete them.

* [GET - List shipping policies](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/shipping-policies)
* [GET - Retrieve shipping policy by ID](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/shipping-policies/-id-)
* [PUT - Update shipping policy](https://developers.vtex.com/docs/api-reference/logistics-api#put-/logistics/pvt/shipping-policies/-id-)
* [DELETE - Delete shipping policies by ID](https://developers.vtex.com/docs/api-reference/logistics-api#delete-/logistics/pvt/shipping-policies/-id-)

### Loading dock

You can list loading docks, deactivate, reactivate, update or delete them.

* [GET - List all docks](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/docks)
* [GET - List dock by ID](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/docks/-dockId-)
* [POST - Deactivate dock](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/docks/-dockId-/deactivation)
* [DELETE - Delete dock](https://developers.vtex.com/docs/api-reference/logistics-api#delete-/logistics/pvt/configuration/docks/-dockId-)
* [POST - Create/update dock](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/docks)
* [POST - Activate dock](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/docks/-dockId-/activation)

### Warehouse

You can list warehouses, deactivate, reactivate, update or delete them.

* [GET - List all warehouses](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/warehouses)
* [GET - List warehouse by ID](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/warehouses/-warehouseId-)
* [POST - Deactivate warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/warehouses/-warehouseId-/deactivation)
* [POST - Activate warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/warehouses/-warehouseId-/activation)
* [DELETE - Remove warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#delete-/logistics/pvt/configuration/warehouses/-warehouseId-)
* [POST - Create/update warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/warehouses)

## Managing inventory

Once you have your Shipping strategy set up, you will need to manage the items available for sales, which compose your [inventory](https://help.vtex.com/en/tutorial/inventory-management--tutorials_139). In VTEX, inventory is the relationship between your stored products and their availability for sales.

### Inventory

You can update your inventory or retrieve information about it.

* [PUT - Update inventory by SKU and warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#put-/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-)
* [GET - List inventory by SKU](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/inventory/skus/-skuId-)
* [GET - List inventory per warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/inventory/items/-skuId-/warehouses/-warehouseId-)
* [GET - List inventory per dock](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/inventory/items/-skuId-/docks/-dockId-)
* [GET - List inventory per dock and warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/inventory/items/-skuId-/docks/-dockId-/warehouses/-warehouseId-)
* [GET - List inventory with dispatched reservations](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/inventory/items/-itemId-/warehouses/-warehouseId-/dispatched)

**In VTEX Admin:** Orders > Inventory & Shipping > Inventory Management

**In Redesigned VTEX Admin:** Catalog > Inventory > Inventory Management

## Setting up shipping configurations (Optional)

VTEX offers different solutions for your logistic process according to your business needs. You can configure shipping geolocations, work with the reservation, create scheduled delivery windows, define holidays, register pickup points, and more.

**In VTEX Admin:** Orders > Inventory & Shipping > Geolocation Shipping/Delivery capacity/Holidays

**In Redesigned VTEX Admin:** Store Settings > Shipping > Settings/Geolocation Shipping/Holidays

### Geolocation shipping (polygons)

[Geolocation shipping](https://help.vtex.com/en/tutorial/gerenciar-geolocalizacao--tutorials_138) is the registration of shipping locations using polygons to delimitate areas, usually for delivering in rural and industrial areas.

* [PUT - Create/update polygon](https://developers.vtex.com/docs/api-reference/logistics-api#put-/logistics/pvt/configuration/geoshape)
* [GET - List paged polygons](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/geoshape)
* [GET - List polygon by ID](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/geoshape/-polygonName-)
* [DELETE - Delete polygon](https://developers.vtex.com/docs/api-reference/logistics-api#delete-/logistics/pvt/configuration/geoshape/-polygonName-)

### Reservations

[Reservation](https://help.vtex.com/en/tutorial/how-does-reservation-work--tutorials_92) is the solution that prevents the same item from being sold more than once. After the shopper completes the purchase, the item bought status changes from `Available` to `Reserved` in the [inventory management](https://help.vtex.com/en/tutorial/inventory-management--tutorials_139).

* [POST - Create reservation](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/inventory/reservationsn)
* [GET - List reservation by ID](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/inventory/reservations/-reservationId-)
* [GET - List reservation by warehouse and SKU](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/inventory/reservations/-warehouseId-/-skuId-)
* [POST - Confirm reservation](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/inventory/reservations/-reservationId-/confirm)
* [POST - Acknowledgment reservation](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/inventory/reservations/-reservationId-/acknowledge)
* [POST - Cancel reservation](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/inventory/reservations/-reservationId-/cancel)

### Scheduled delivery

[Scheduled delivery](https://help.vtex.com/en/tutorial/scheduled-delivery--22g3HAVCGLFiU7xugShOBi) allows you to set delivery time frames for shoppers to choose the day and time to receive the order.

* [POST - Add blocked delivery windows](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/carriers/-carrierId-/adddayofweekblocked)
* [GET - Retrieve blocked delivery windows](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/carriers/-carrierId-/getdayofweekblocked)
* [POST - Remove blocked delivery windows](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/carriers/-carrierId-/removedayofweekblocked)
* [GET - Search capacity reservations in time range](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics-capacity/resources/carrier@-capacityType-@-shippingPolicyId-/time-frames)
* [GET - Get capacity reservation usage by window](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics-capacity/resources/carrier@-capacityType-@-shippingPolicyId-/time-frames/-windowDay-F-windowStartTime-T-windowEndTime-)

### Holidays

The [Holidays](https://help.vtex.com/en/tutorial/registering-holidays--2ItOthSEAoyAmcwsuiO6Yk) feature allows you to configure days that should not be considered valid for delivery so that VTEX platform considers those days when calculating the shipping estimated time.

* [PUT - Create/update holiday](https://developers.vtex.com/docs/api-reference/logistics-api#put-/logistics/pvt/configuration/holidays/-holidayId-)
* [GET - List holiday by ID](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/holidays/-holidayId-)
* [GET - List all holidays](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/holidays)
* [DELETE - Delete holiday](https://developers.vtex.com/docs/api-reference/logistics-api#delete-/logistics/pvt/configuration/holidays/-holidayId-)

### Pickup points

[Pickup points](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R) are physical locations from where shoppers can pick up their orders.

* [PUT - Create/Update Pickup Point](https://developers.vtex.com/docs/api-reference/logistics-api#put-/logistics/pvt/configuration/pickuppoints/-pickupPointId-)
* [GET - List all pickup points](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/pickuppoints)
* [GET - List Pickup Point By ID](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/pickuppoints/-pickupPointId-)
* [GET - List paged Pickup Points](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/pickuppoints/_search)
* [DELETE - Delete Pickup Point](https://developers.vtex.com/docs/api-reference/logistics-api#delete-/logistics/pvt/configuration/pickuppoints/-pickupPointId-)

**In VTEX Admin:** Orders > Inventory & Shipping > Pickup Points

**In Redesigned VTEX Admin:** Shipping > Pickup Points

## Calculating shipping estimate time

When the shopper enters their address at checkout, the VTEX platform analyzes the order fulfillment conditions and displays the available shipping options to the shopper.

### SLA

Service Level Agreement (SLA) refers to the order’s fulfillment conditions presented to the shopper, including shipping type - delivery or pick up -, costs and deadlines.

* POST - [Calculate SLA](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/shipping/calculate)

## Optimizing fulfillment process with carriers

[Carriers](https://help.vtex.com/en/tutorial/transportadoras-na-vtex--7u9duMD5UQa2QQwukAWMcE), or couriers, are the companies responsible for delivering orders, and their operating profiles are configured in your [shipping policies](https://help.vtex.com/pt/tutorial/shipping-policy--tutorials_140). The service contract details with carriers, like shipping ZIP code ranges and packages weight limits, are configured via [shipping rate template](https://help.vtex.com/en/tutorial/shipping-rate-template--tutorials_127).

### Freight values

Create carriers’ freight values and retrieve information about them.

* [POST - Create/update freight values](https://developers.vtex.com/docs/api-reference/logistics-api#post-/logistics/pvt/configuration/freights/-carrierId-/values/update)
* [GET - List freight values](https://developers.vtex.com/docs/api-reference/logistics-api#get-/logistics/pvt/configuration/freights/-carrierId-/-cep-/values)

### VTEX Shipping Network (independent App)

[VTEX Shipping Network](https://developers.vtex.com/vtex-rest-api/reference/vtex-shipping-network-api-overview) is an app that connects your store with carriers to deliver orders at better freight costs and with optimized logistic operation. Currently, the solution is available exclusively in Brazil.

With VTEX Shipping Network you coordinate the actions of:

1. Notifying carriers of new package deliveries.
2. Issuing shipping labels.
3. Tracking the shipping process steps until the order is fulfilled.

#### Notification

The endpoint below notifies the carrier of the dispatched package information, including fiscal information, and a contact email.

* [POST - Notify Carrier with App](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/-app_name-/v-app_version-/-account-/-workspace-/notify)

#### Tracking

The endpoint below updates tracking events for pending deliveries using a list of tracking codes.

* [POST - Tracking Events with App](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/-app_name-/v-app_version-/-account-/-workspace-/tracking)

### VTEX Tracking (independent App)

[VTEX Tracking](https://vtex.com/br-pt/tracking/) is an app that enables the merchant to control and manage deliveries in real-time, having visibility of indicators like the driver's location and order delivery status. Shoppers can also keep up with deliveries in real-time. Currently, the solution is available exclusively in Brazil.

>❗ We strongly recommend that a call to a VTEX Tracking GET endpoint is made only once every 6 hours. Retrieving data from the same endpoint more than once during a 6-hour window represents a load to our API that will slow down the overall usage of systems.

* [POST - Asynchronous Login](https://developers.vtex.com/docs/api-reference/tracking#post-/auth)
* [PUT - Remove Packing List](https://developers.vtex.com/docs/api-reference/tracking#put-/services)
* [POST - Post Delivery Service](https://developers.vtex.com/docs/api-reference/tracking#post-/services)
* [GET - Get Delivery Services List](https://developers.vtex.com/docs/api-reference/tracking#get-/services)
* [GET - Get Delivery Service by ID](https://developers.vtex.com/docs/api-reference/tracking#get-/services/-idDeliveryService-)
* [POST - Post Delivery Service With Route Scheduling](https://developers.vtex.com/docs/api-reference/tracking#post-/services/routes)
* [GET - Get Delivery Services List by Route](https://developers.vtex.com/docs/api-reference/tracking#get-/services/routes)
* [GET - Get Delivery Service by Invoice](https://developers.vtex.com/docs/api-reference/tracking#get-/services/invoice)
