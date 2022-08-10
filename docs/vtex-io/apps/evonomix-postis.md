---
title: "VTEX Postis"
slug: "evonomix-postis"
excerpt: "evonomix.postis@1.0.1"
hidden: true
createdAt: "2022-07-07T11:40:02.886Z"
updatedAt: "2022-08-09T13:19:56.287Z"
---
This application allows you to integrate multi-carrier shipping using Postis API.

## Installation & Configuration

- Use the vtex toolbelt to install.

```bash
vtex install vtex.postis
```

Open the app settings on your store admin - `https://{{accountName}}.myvtex.com/admin/apps` - click on the Postis app and fill in the:
* `Postis API TOKEN` (required) - provided by the Postis platform

You will also need to link your store's warehouses to your postis account.

1. Go in your VTEX admin `ORDERS > Inventory & shipping > Shipping strategy`, and in the `Warehouses` tab, 
for each active warehouse you must have/create a corresponding location in your postis account.
2. In you postis account, go to `Locations & Carriers`, create/edit a location and set the `External Location Id` to
correspond to the VTEX's warehouse `ID`.


After configuration, the shipping list can be accessed in your VTEX admin `ORDERS > Shipping List`.

# Features

When generating AWBs, there are a variety of helpful features at your disposal:

### 1. Multiple parcels and weight distribution

Having the order's total weight available and displayed, you have the option to either generate AWBs with only one parcel
covering the entire order's weight thus having only one label for the parcel when printing out the AWB, or you can choose
to have more than one parcel per AWB with the possibility to manually distribute the order's weight across the parcels 
weight fields with an indicator alerting you when the distribution is under or over the total weight limit.

This feature is useful when you need to generate AWBs for orders that needs to be split across multiple packages. 
Generating a single AWB will generate labels for each parcel.



### 2. Shipping simulation

Based on selected options, a shipping rate simulation will run, displaying a list of eligible carriers with their respected
shipping rates, from which you can choose a carrier/shipping rate of your desire or leave it on `Automatic`, which will let the 
`postis` API decide the appropriate carrier, based on the web application's configuration.



### 3. Postis pickup points

To activate this feature follow these steps:

1. Install the scheduler by making a `POST` request to the following endpoint
> https://{{accountName}}.myvtex.com/api/scheduler/master/postis?version=4

with the following body:

```json
{    
    "id": "sync-postis-pickup-points",
    "scheduler": {
        "expression": "*/30 * * * *" 
    },
    "request": {
        "uri": "http://{{accountName}}.myvtex.com/no-cache/sync-pickup-points",
        "method": "POST" 
    }
}
```

This will synchronize all available pickup points from postis into vtex.<br>
The pickup points will be available under `ORDERS > Inventory & shipping > Pickup points`.

2. You will also need to add a valid Google Maps API Key under `ORDERS > Inventory & shipping > Geolocation shipping`
and `STORE SETUP > Checkout > {click settings cog} > {click checkout tab} > {Google Maps API Key field}`.


3. Then you must create a shipping policy under `ORDERS > Inventory & shipping > Shipping strategy`, check the `Link pickup points` section
and under `Pickup points tags` select the `postis pickup` tag.
   

4. Configure the shipping rate for the new shipping policy under `ORDERS > Inventory & shipping > Shipping rates`.


### 4. Periodic Postis AWB updates

Turn on the `AWB AUTO-UPDATE` feature in the `Shipping` page.
The update will run every 4 hours.
You can configure which carriers will be included in this update by accessing the `AWB CARRIERS SETTINGS`.


<hr>

## Payment settings

<span style="color: orange">WARNING</span> In order fot the application to work correctly, payment systems must be properly configured:
* `Cash` payment methods must be configured to belong to the `cash` payment group
* `Payment order` payment methods must be configured to belong to the `promissary` payment group.




## Possible Errors

* `Value of field ExternalClientLocation is not valid` - represents the warehouse ID declared in VTEX 
  under `ORDERS > Inventory & shipping > Shipping strategy > Warehouses`.<br>
  In the Postis Web Application, under `Locations & Carriers`, this VTEX warehouses Is must be associated to a 
  location's `External Location Id`.<br>
  Each active warehouse ID declared in VTEX must have a correspondence in the Postis Web Application's `Locations & Carriers`,
  via the `External Location Id`.

## Exposed endpoints:

[Postis DOCS](https://apidocs.postisgate.com/)

### POST - /postis/request-awb

### GET - /postis/get-label/:courier/:trackingNumber

### POST - /postis/request-awb-history