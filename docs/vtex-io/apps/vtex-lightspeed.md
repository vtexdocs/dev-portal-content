---
title: "Lightspeed"
slug: "vtex-lightspeed"
excerpt: "vtex.lightspeed@0.12.0"
hidden: true
createdAt: "2022-07-14T20:21:37.712Z"
updatedAt: "2022-08-01T13:34:23.459Z"
---
The lightspeed All-in-One Cloud-Based Point of Sale (POS) System, this app will integrate invoiced orders to Lightspeed

## Functionalities

- Sales Integration
- Customer Integration
- Inventory and Pricing Integration
- Incomplete Orders Report
- Order Lookup
- Latest Sync Report

## Configuration

Step 1 - In the terminal, log in to the desired VTEX account and [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the app by running `vtex install vtex.lightspeed@x.x`

Step 2 - At the Admin, navigate to **Apps > Lightspeed Integration**, at the second tab **Credentials** fill with your Lightspeed Account's credentials, and save it.

Step 3 - Still at **Apps > Lightspeed Integration**, now at the third tab **Defaults** select the default options that the app will use to submit the orders and save them. Now you should be able to connect your Lightspeed account with VTEX.

![Queue](./images/Options_LS.png)
![Credentials](./images/Credentials_LS.png)
![Defaults](./images/Defaults_LS.png)

## Incomplete Orders Report and Order Lookup

- To find all the incomplete and error orders, go to the fourth tab **Incomplete Orders**, and click **GET INCOMPLETE ORDERS**. The report shows Error orders Id, Blocked step, Error message, and the relevant time.
- The table also provides **retry orders** function. Simply check the desired orders and click **RETRY SELECTED**, try not to retry too many orders at a time to avoid time-out errors.

![Incomplete](./images/Incomplete_LS.png)
![OrderLookup](./images/OrderLookup_LS.png)

## Manual Inventory and Pricing Sync

- On the Admin page, you can manually sync Lightspeed inventory and pricing information by using the relevant buttons.
- This sync updates the VTEX databases based on information received from Lightspeed
- This process can take some time, so make sure not to refresh the page while it's running.

![Sync](./images/Sync_LS.png)

## Daily Inventory and Pricing Schedule Job Sync

- On a daily basis, there will be a scheduled job tasked with inventory/pricing syncs
- It will run every 2 minutes to sync every 3000 items (ex: items 1-3000, then 3001-6000, etc)

## Latest Sync Report

- This table will show the detail of the latest Sync no matter if it is manual sync or daily sync. It shows the item SKU and previous and updated quantity.

![SyncReport](./images/SyncReport_LS.png)

## Basic Flow of the App

![Basic Flow](./images/Flowchart_LS.jpg)