---
title: "ShipStation"
slug: "vtex-ship-station"
excerpt: "vtex.ship-station@0.7.2"
hidden: true
createdAt: "2022-08-01T20:10:56.868Z"
updatedAt: "2022-08-01T20:10:56.868Z"
---
The ShipStation app sends orders placed in VTEX to ShipStation.  When the orders are shipped in ShipStation, the shipping information will be updated in VTEX.

## Configuration

### Step 1 - Create API credentials in ShipStation

1. Log in to ShipStation
2. In the upper right hand corner, click the gear icon.
3. In the left hand menu, click Account, then API Settings
4. Generate API Keys.  Record the Key and Secret.
![image](https://user-images.githubusercontent.com/47258865/110505541-3d983100-80cc-11eb-9b5c-990bf254bad3.png)

### Step 2 - Create a store

1. In the left-hand column, choose ‘Selling Channels’ and then ‘Store Setup’
![image](https://user-images.githubusercontent.com/47258865/110505168-e4300200-80cb-11eb-815e-2f78cdef29e6.png)
2. Click ‘ Connect a Store or Marketplace’ and search for ‘Shipstation’
![image](https://user-images.githubusercontent.com/47258865/110505238-f742d200-80cb-11eb-85dd-8ffccfd4d01a.png)
3. Name the store and click Connect.
![image](https://user-images.githubusercontent.com/47258865/110505261-fca01c80-80cb-11eb-9752-1df0ab4e6453.png)

### Step 3 - Install the ShipStation app

Using your terminal, log in to the desired VTEX account and run the following command:
`vtex install vtex.ship-station`

### Step 4 - Defining the app settings

1. In the VTEX admin, under Orders, choose Inventory & Shipping, then ShipStation
2. Enter The API Key & Secret from Step 1
3. Choose Weight Unit
4. Choose optional settings
- **Split Shipment by Location** - A separate order for each shipping location will be created in ShipStation
- **Send Pickup In Store Orders to Shipstation** - Orders that are for in store pickup will be sent to ShipStation
- **Only Send Marketplace Orders** - Send only Marketplace orders to ShipStation
- **Include Brand Name and Categories in Item Details** - Show item brand name and categories in Shipstation item details
- **Include Sku Specifications in Item Details** - Show sku specifications in ShipStation item details
- **Update order status to 'Start Handling' when order has been sent to ShipStation** - Change the order status in VTEX to 'Start Handling' when the order has been exported to Shipstation
- **Use Reference Code as Sku** - Use the item Reference Code as sku in ShipStation
- **Show Warehouse Location in Item Details** - Show item warehouse location in Shipstation item details
- **Add Payment Method to Custom field 1** - Show the order payment method in Custom field 1 in ShipStation
5. Save Settings
6. Create Webhooks

### Notes
Orders that are manually marked as shipped in ShipStation are considered Fulfillments and will be invoiced based on the item information in ShipStation.
Orders that are invoiced in VTEX will be marked as Shipped in ShipStation.
New orders will be sent to ShipStation when payment is approved.
Items shipped in ShipStation will be invoiced when the item notification is received.
Items fulfilled in ShipStation will be invoiced within one hour.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!