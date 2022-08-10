---
title: "Click & collect"
slug: "tommymx-axo-clickncollectorders"
excerpt: "tommymx.axo-clickncollectorders@3.1.3"
hidden: true
createdAt: "2022-08-04T20:37:49.542Z"
updatedAt: "2022-08-06T00:02:23.840Z"
---
This is an app that allow the users watch and follow orders that are in store, it app search orders in an specific store or white label and shows these orders with some filters by status (canceled, pending, delivered or in store). Also allows check the main order's information in an template that contains the order details.

![image](https://user-images.githubusercontent.com/60228986/170093091-2a8aabbf-0c30-4f61-9ca3-f61eb3c1db8c.png)

# How it works

Basically click and collect application is located as an admin module, it works based on 2 information sources:

1. Orders stored at the white label
2. Orders stored at master data entity, its *acronym* must be 'EN'

## Orders table

The main logic takes these two information sources and apply a filter to obtain orders with status 'in store', it searches the principal orders into the seller and into master data's orders table and it orders must have next conditions:

1. The sucursal name must be equal to session store name, which is obtained automatically fronm the user session
2. The order's state value must be "R"

Once orders was filtered the main logic aply the correspondent status to each one, also calculates the days that order has been at store based on field **fecha** from master data order's table.

> **Note:** Is pretty important that the field **fecha** format looks like next example ```24 Mayo 2022```, because it is parsed to calculate days that product has been at store

## Order details
![order-detail](https://user-images.githubusercontent.com/60228986/170093536-23e0e12b-50d3-4376-b318-00db60b5c898.png)