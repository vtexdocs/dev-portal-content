---
title: "Lead Time (Beta)"
slug: "lead-time-beta"
hidden: true
createdAt: "2023-07-13T13:17:05.725Z"
updatedAt: "2023-07-13T13:17:33.816Z"
---

> The Lead Time feature is in beta, which means that we are working to improve it.

_Lead Time_ is an optional configuration you can make for a given SKU in a warehouse. The solution allows you to have more flexibility in managing logistic operations, and it is especially useful in some [scenarios](#use-cases), such as dropshipping and selling manufactured products.

The following sections will explain key concepts about [fulfillment](#logistics-and-fulfillment-in-vtex) and [inventory management](#inventory-management) in VTEX. Afterward, you will find the [Lead Time](#lead-time) definition and how to [configure](#lead-time-configuration) it.

## Logistics and fulfillment in VTEX

In VTEX, there are specific terms to identify the entities involved in order [fulfillment](https://developers.vtex.com/docs/guides/fulfillment). An important concept is [Shipping strategy](https://help.vtex.com/en/tutorial/shipping-strategy--58vLBDbjYVQzJ6rRc5QNz3), defined as the relationship between the following entities:

* [Shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140): Set of rules that define the shipping conditions, including carriers working hours, delivery time frames, shipping rates, and more.
* [Loading dock](https://help.vtex.com/en/tutorial/loading-dock--5DY8xHEjOLYDVL41Urd5qj): Entity that links your products to a shipping policy, and the physical location from where products will be shipped.
* [Warehouse](https://help.vtex.com/en/tutorial/warehouse--6oIxvsVDTtGpO7y6zwhGpb): Location where your products are stored.

For more concepts and definitions, see our [Logistics Glossary](https://help.vtex.com/en/tutorial/logistics-glossary--16DSSiXn548rsidi0A8Hby).

### Inventory Management

Inventory is the relationship between stored products and their availability for sales, which means a store's inventory is composed of the items available for sales.

The inventory contains information about the store's available products and the warehouse where they are stored. You can use the inventory to keep track of the updates for each SKU, like the quantity of items available, who made changes, when that happened, and more.

You can manage your inventory with the [Logistics API](https://developers.vtex.com/docs/api-reference/logistics-api#overview) or using the VTEX Admin, by accessing _Catalog > Inventory > Inventory Management_. Regardless of what [VTEX account type](https://help.vtex.com/en/tutorial/choosing-between-standard-account-franchise-account-or-seller-portal--4S90HzzhMyZESsHqrnUs78) you have, (franchise or seller portal account, for example), the [Inventory Management](https://help.vtex.com/en/tutorial/inventory-management--tutorials_139) module will be the same.

## Lead Time

The _Lead Time_ feature allows you to configure a time frame for a given SKU in a warehouse. The solution is part of the shipping time displayed to shoppers at Checkout, as in the example below:

![lead_time_image_total_time_diagram_final](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Fulfillment/lead_time_image_total_time_diagram_final.png)

* **Lead Time:** Amount of time you can configure for a specific SKU in a warehouse. The _Lead Time_ could represent handling time or fabrication, for example. Defining Lead Time is optional.
* **[Warehouse time](https://help.vtex.com/en/tutorial/managing-warehouses--tutorials_137):** Amount of time a SKU takes to leave a warehouse to a loading dock. Defining warehouse time is required, but you can set the time to `0`.
* **[Loading Dock time](https://help.vtex.com/en/tutorial/managing-loading-docks--7K3FultD8I2cuuA6iyGEiW):** Amount of time an SKU takes to leave a loading dock, which is an intermediate point between the warehouse and the [carrier](https://help.vtex.com/en/tutorial/carries-on-vtex--7u9duMD5UQa2QQwukAWMcE), and it is where products are shipped from. Defining loading dock time is required, but you can set the time to `0`.
* **[Shipping Policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140):** Defines the conditions that will be displayed to shoppers at Checkout, and includes information like:
  * [Shipping rates](https://help.vtex.com/en/tutorial/planilha-de-frete--tutorials_127)
  * [Carrier](https://help.vtex.com/tutorial/carries-on-vtex--7u9duMD5UQa2QQwukAWMcE) working hours
  * Delivery time frames
  * [Delivery capacity](https://help.vtex.com/en/tutorial/managing-delivery-capacity--2y217FQZCjD0I1n62yxVcz)
  * Deliverable products types (modals)

### Use cases

Configuring the _Lead Time_ for a SKU is suitable in many scenarios, such as:

#### External suppliers

You can better manage the time it takes for external suppliers (such as a factory or a manufacturer) to produce, handle, dispatch and/or deliver a specific product.

#### Dropshippers

You have more flexibility to set delivery or handling times of products offered by dropshipper directly to the shopper. Besides, you can lack inventory for a SKU and still make it valid for the Checkout heuristic.

#### Large and customizable products

When you sell large products like furniture or customizable products, you can better manage the handling time for specific SKUs of your logistic operation.

### SKU inventory

Depending on whether or not there is inventory for a SKU, the platform behaves as the following:

* **Inventory with SKU:** You can configure _Lead Time_ and Checkout heuristic will consider it for the shipping calculation, summing up the Lead Time to the shipping calculation based on the shipping policies.
* **Inventory without SKU:** You can configure _Lead Time_, but Checkout heuristic will not consider the SKU valid for sales, since it has no available units for purchase
* **Infinite inventory:** You can configure _Lead Time_, Checkout heuristic will consider it for the shipping calculation, and the SKU will be valid for sales for as long as the inventory is enabled as infinite.

## Lead Time configuration

There are two ways you can configure _Lead Time_:

* [Via VTEX Admin](#configuration-via-vtex-admin): You are able to configure it for days only.
* [Via Logistics API](#configuration-via-logistics-api): You are able to configure it for days, hours, minutes, and seconds.

_Lead Time_ is calculated considering [holidays](https://help.vtex.com/en/tutorial/registering-holidays--2ItOthSEAoyAmcwsuiO6Yk) and business days according to your shipping policy configuration. You can configure _Lead Time_ duration up to 365 days, whether by VTEX Admin or via Logistics API.

By default, shipping policies are created considering business days for shipping time calculation, but you can [configure a shipping policy to consider calendar days](#configuration-of-calendar-days-optional). That way, you can have Lead Time counted as calendar days.

### Configuration via VTEX Admin

To configure _Lead Time_, follow the steps below:

1. In the VTEX Admin, go to **Catalog > Inventory > Inventory Management**, or type _Inventory Management_ in the search bar at the top of the page.
2. Select the SKU you wish to configure. You can use the search bar and the [search filters](https://help.vtex.com/en/tutorial/managing-stock-items--tutorials_139#search-filters).
3. In the SKU row and **Lead time (days)** column, type the desired number of days. This is an optional configuration and the field starts at `0` by default.
4. At the bottom of the page, click `Save changes`.

### Configuration via Logistics API

You can configure _Lead Time_ using the _Update inventory by SKU and warehouse_ endpoint, which allows you to do the following:

* **Define quantity:** If you indicate a specific number of SKU units in a warehouse, it will decrease whenever a unit is sold. The store can eventually run out of inventory for that SKU.
* **Configure Lead Time:** If you set the _Lead Time_ for the SKU in a warehouse, Checkout heuristic will consider that time for shipping calculation. You can configure _Lead Time_ in days, hours, minutes, and seconds.
* **Set infinite inventory:** If you enable infinite inventory for the SKU in a warehouse, your store will always have these SKU units available for sales, which means not running out of inventory.

>⚠️ The difference between the [current endpoint](https://developers.vtex.com/docs/api-reference/logistics-api#put-/api/logistics/pvt/inventory/skus/-skuId-/warehouses/-warehouseId-) and the new beta endpoint is that the new version supports the `leadTime` request body field, which allows you to configure Lead Time for a SKU in a warehouse.

#### Endpoint

**PUT** - `https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/skus/{skuId}/warehouses/{warehouseId}`

#### Path params

| Name | Type | Description | Example |
|:---:|:---:|:---|:---:|
| `skuId` | string | SKU ID is the unique identifier of the SKU you wish to update. | `36` |
| `warehouseId` | string | Warehouse ID is the unique identifier of the [warehouse](https://help.vtex.com/en/tutorial/warehouse--6oIxvsVDTtGpO7y6zwhGpb) associated with the SKU you wish to update. | `warehouse-1-StoreName` |

#### Headers

| Key | Value | Description |
|:---:|:---:|:---|
| `Accept` | `application/json` | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. |
| `Content-Type` | `application/json` | Type of the content being sent. |

#### Request body example

```json
{
"quantity": 101,
"unlimitedQuantity": false,
"leadTime": "10.00:00:00",
"dateUtcOnBalanceSystem": "2023-03-15T00:52:16"
}
```

#### Request body description

| Field name | Type | Description | Example |
|:---:|:---:|:---|:---:|
| `quantity` | integer | Quantity of SKU units you wish to update the [inventory](https://help.vtex.com/tutorial/inventory-management--tutorials_139) in the given [warehouse](https://help.vtex.com/en/tutorial/warehouse--6oIxvsVDTtGpO7y6zwhGpb). Note that:<p>- Sending it as `null` sets the quantity to `0`.</p><p>- Not sending it sets the quantity to `0`.</p><p>- Sending `unlimitedQuantity` as `true` overrules the  `quantity` field.</p> | `101` |
| `unlimitedQuantity` | boolean | When set as `true`, you make the SKU from the given warehouse permanently available for sales. No matter how many units are sold, the default quantity of `1000000` items does not decrease, and the store never runs out of stock. When set as `false`, every sold unit will decrease your inventory quantity. Note that:<p>- Sending this field as `null` sets the value to `false`.</p><p>-Not sending this field sets the value to `false`.</p><p>- Sending this field as `true` overrules `quantity`.</p> | `false` |
| `leadTime` |  string | Defines _Lead Time_, which is an optional time configuration you can make for a SKU in a warehouse. It can be handling time, fabrication or how long it takes for the item to be available to be shipped to the shopper.<p>The Lead Time is part of the total shipping time and will be considered by Checkout for the shipping calculation.</p><p>The format is `dd.hh:mm:ss` (days.hours:minutes:seconds). Note that:</p><p>-Sending this field as `null` sets the value to `0`.</p><p>- Not sending this field sets the value to `0`.</p> | `10.23:59:15` |
| `dateUtcOnBalanceSystem` |  string | Defines the corresponding moment to the given warehouse. It is useful due to the liberation of handling order reservations.<p>When set as `null`, the value will be the date/time of the request. Its format is `DateTimeOffset`, as in `yyyy-mm-dd-Thh:mm:ss`. For example:  `2023-03-15T00:52:16`.</p> | `2023-03-15T00:52:16` |

#### Response body example

`200 OK`

```json
true
```

Successful requests receive a `200 OK` with a single `true` in the response body. If an error occurs, you will not get a `false` in the response body, but a message instead. For example, sending a malformatted request body makes you get a `400 Bad Request` as a response.

### Configuration of calendar days (optional)

By default, _Lead Time_ is configured in business days. If necessary, you can change it to calendar days in your [shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140) via API with the [Update shipping policy](https://developers.vtex.com/docs/api-reference/logistics-api#put-/api/logistics/pvt/shipping-policies/-id-) endpoint.

To configure _Lead Time_ for calendar days via VTEX Admin, follow the steps below:

1. In the VTEX Admin, go to **Shipping > Shipping Strategy > Shipping Policies**, or type _Shipping Strategy_ in the search bar at the top of the page.
2. Find the desired [shipping policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140). You can use the search bar and filters.

  > To create a new shipping policy, see [Shipping Policy](https://help.vtex.com/en/tutorial/shipping-policy--tutorials_140).

3. In the shipping policy row, click the menu icon <i class="fas fa-ellipsis-v"></i> and select `Edit`.
4. In the **Weekends and Holidays** section, enable the desired toggles:

    * <i class="fas fa-toggle-on"></i> **Saturday delivery**
    * <i class="fas fa-toggle-on"></i> **Sunday delivery**
    * <i class="fas fa-toggle-on"></i> **Holiday delivery**

    ![print_lead_time_holidays](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Fulfillment/print_lead_time_holidays.png)

5. Click `Save changes`.

## Endpoints that retrieve Lead Time information

The following endpoints return the `leadTime` field in their response bodies:

* [GET - List inventory by SKU](#1-list-inventory-by-sku)
* [GET - List inventory per warehouse](#2-list-inventory-per-warehouse)
* [GET - List inventory per dock](#3-list-inventory-per-dock)
* [GET - List inventory per dock and warehouse](#4-list-inventory-per-dock-and-warehouse)
* [GET - List inventory with dispatched reservations](#5-list-inventory-with-dispatched-reservations)

The table below shows the path params of these requests:

### Path params (GET endpoints)

| Name | Type | Description | Example |
|:---:|:---:|:---|:---:|
| `skuId` | string | Every SKU has a unique identifier called SKU ID. | `36` |
| `itemId` | string | SKU unique identifier called SKU ID. This field is an equivalent to `skuId`. | `89` |
| `dockId` | string | Dock ID is the unique identifier of the [loading dock](https://help.vtex.com/en/tutorial/loading-dock--5DY8xHEjOLYDVL41Urd5qj). | `dock-13a` |
| `warehouseId` | string | Warehouse ID is the unique identifier of the warehouse. | `warehouse-1-StoreName` |

### 1. List inventory by SKU

Lists [inventory](https://help.vtex.com/en/tutorial/inventory-management--tutorials_139) information by a SKU unique identifier (SKU ID).

#### 1. Endpoint

**GET** - `https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/skus/{skuId}`

#### 1. Response body example

`200 OK`

```json
{
    "skuId": "11",
    "balance": [
        {
            "warehouseId": "estoqueA",
            "warehouseName": "Galpão Principal",
            "totalQuantity": 10000,
            "reservedQuantity": 445,
            "hasUnlimitedQuantity": false,
            "timeToRefill": null,
            "dateOfSupplyUtc": null,
            "leadTime": "00:00:00"
        },
        {
            "warehouseId": "andreia-wh-01",
            "warehouseName": "andreia-wh-01",
            "totalQuantity": 200,
            "reservedQuantity": 0,
            "hasUnlimitedQuantity": false,
            "timeToRefill": null,
            "dateOfSupplyUtc": null,
            "leadTime": "10.00:00:00"
        },
        {
            "warehouseId": "leadstock_1",
            "warehouseName": "LeadStock1",
            "totalQuantity": 500,
            "reservedQuantity": 1,
            "hasUnlimitedQuantity": false,
            "timeToRefill": null,
            "dateOfSupplyUtc": null,
            "leadTime": "30.00:00:00"
        }
    ]
}
```

See the complete documentation on [List inventory by SKU](https://developers.vtex.com/docs/api-reference/logistics-api#get-/api/logistics/pvt/inventory/skus/-skuId-).

### 2. List inventory per warehouse

Lists inventory information by [warehouse](https://help.vtex.com/en/tutorial/warehouse--6oIxvsVDTtGpO7y6zwhGpb).

#### 2. Endpoint

**GET** - `https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/items/{skuId}/warehouses/{warehouseId}`

#### 2. Response body example

`200 OK`

```json
[
    {
        "skuId": "11",
        "warehouseId": "leadstock_2",
        "dockId": "doca-vini-02",
        "totalQuantity": 200,
        "reservedQuantity": 0,
        "availableQuantity": 200,
        "isUnlimited": false,
        "salesChannel": [
            "1"
        ],
        "deliveryChannels": [
            "delivery"
        ],
        "timeToRefill": null,
        "dateOfSupplyUtc": null,
        "supplyLotId": null,
        "keepSellingAfterExpiration": false,
        "transfer": null,
        "leadTime": "5.00:00:00"
    }
]
```

See the complete documentation on [List inventory per warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#get-/api/logistics/pvt/inventory/items/-skuId-/warehouses/-warehouseId-).

### 3. List inventory per dock

Lists inventory information by [loading dock](https://help.vtex.com/en/tutorial/loading-dock--5DY8xHEjOLYDVL41Urd5qj).

#### 3. Endpoint

**GET** - `https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/items/{skuId}/docks/{dockId}`

#### 3. Response body example

`200 OK`

```json
[
    {
        "skuId": "11",
        "warehouseId": "leadstock_2",
        "dockId": "doca-vini-02",
        "totalQuantity": 200,
        "reservedQuantity": 0,
        "availableQuantity": 200,
        "isUnlimited": false,
        "salesChannel": [
            "1"
        ],
        "deliveryChannels": [
            "delivery"
        ],
        "timeToRefill": null,
        "dateOfSupplyUtc": null,
        "supplyLotId": null,
        "keepSellingAfterExpiration": false,
        "transfer": null
    }
]
```

See the complete documentation on [List inventory per dock](https://developers.vtex.com/docs/api-reference/logistics-api#get-/api/logistics/pvt/inventory/items/-skuId-/docks/-dockId-).

### 4. List inventory per dock and warehouse

Lists inventory information from the combination of a [loading dock](https://help.vtex.com/en/tutorial/loading-dock--5DY8xHEjOLYDVL41Urd5qj) and a [warehouse](https://help.vtex.com/en/tutorial/warehouse--6oIxvsVDTtGpO7y6zwhGpb).

#### 4. Endpoint

**GET -** `https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/items/{skuId}/docks/{dockId}/warehouses/{warehouseId}`

#### 4. Response body example

`200 OK`

```json
[
    {
        "skuId": "11",
        "warehouseId": "leadstock_2",
        "dockId": "doca-vini-02",
        "totalQuantity": 200,
        "reservedQuantity": 0,
        "availableQuantity": 200,
        "isUnlimited": false,
        "salesChannel": [
            "1"
        ],
        "deliveryChannels": [
            "delivery"
        ],
        "timeToRefill": null,
        "dateOfSupplyUtc": null,
        "supplyLotId": null,
        "keepSellingAfterExpiration": false,
        "transfer": null
    }
]
```

See the complete documentation on [List inventory per dock and warehouse](https://developers.vtex.com/docs/api-reference/logistics-api#get-/api/logistics/pvt/inventory/items/-skuId-/docks/-dockId-/warehouses/-warehouseId-).

### 5. List inventory with dispatched reservations

[Reservation](https://help.vtex.com/en/tutorial/how-does-reservation-work--tutorials_92) is the VTEX solution that prevents stores from selling the same item more than once. Adding products to the shopping cart does not create reservation, that only happens after the shopper completes the purchase.

This endpoint lists [inventory](https://help.vtex.com/tutorial/inventory-management--tutorials_139) information about dispatched reservations from a given warehouse. A reservation is considered dispatched after the order has passed the `authorize-fulfillment` status in the [order flow](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196) and is not canceled.

**Response 400 Bad Request:** When the store has more than 2.000 active reservations, you receive a `400 Bad Request` error with the message: _“Too many active reservations”_.

#### 5. Endpoint

**GET** - `https://{accountName}.{environment}.com.br/api/logistics/pvt/inventory/items/{itemId}/warehouses/{warehouseId}/dispatched`

#### 5. Response body example

`200 OK`

```json
[
    {
        "skuId": "11",
        "warehouseId": "leadstock_2",
        "dockId": "doca-vini-02",
        "totalQuantity": 200,
        "reservedQuantity": 0,
        "availableQuantity": 200,
        "isUnlimited": false,
        "salesChannel": [
            "1"
        ],
        "deliveryChannels": [
            "delivery"
        ],
        "timeToRefill": null,
        "dateOfSupplyUtc": null,
        "supplyLotId": null,
        "keepSellingAfterExpiration": false,
        "transfer": null,
        "leadTime": null
    }
]
```

See the complete documentation on [List inventory with dispatched reservations](https://developers.vtex.com/docs/api-reference/logistics-api#get-/api/logistics/pvt/inventory/items/-itemId-/warehouses/-warehouseId-/dispatched).
