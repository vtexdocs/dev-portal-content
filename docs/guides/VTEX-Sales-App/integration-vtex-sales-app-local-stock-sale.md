---
title: "Integration VTEX Sales App Local stock sale"
slug: "integration-vtex-sales-app-local-stock-sale"
hidden: false
createdAt: ""
updatedAt: ""
excerpt: "Learn how to integrate the VTEX Sales App Local stock sale"
seeAlso:
hidePaginationPrevious: false
hidePaginationNext: false
---
## Integration VTEX Sales App Local stock sale

To first identify Local stock sale sales the first thing to do is to look for [VTEX Sales App](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc/7fnnVlG3Kv1Tay9iagc5yf) sales. VTEX Sales App sales can be filtered by a specific OMS filter called "VTEX Sales App", this filter looks for user agent information that sets a specific user agent that can be used to track VTEX Sales App sales. This tag is not available at the Order Payload or databases (redshift), but it can be used at [list orders API](https://developers.vtex.com/vtex-rest-api/reference/listorders) to filter VTEX Sales App Sales. Another field that can be used for this is `marketingData.marketingTags`, if the array contains an "VTEX Sales App" tag the order was made by VTEX Sales App application. This field can be found at the Order Payload and Redshift databases.

The next step is to understand if the order generated will be processed by the same store that has created it. To do that, check first if the `checkedIn` flag is `true`, next run through all products of this order looking at  `shippingData.logisticsInfo`. Inside this key, it is needed to compare `pickupPointId` with `checkedInPickupPointId` the value of those tags must be the same and not null, meaning that the store that created the order is responsible for delivering the order.

## Integration Methods

Now that VTEX Sales App Orders and _"Local stock sale delivery method"_ can be identified in our OMS, the next step is to use the available methods to consume OMS APIs to process Local stock sale orders. There are two options for that:

### Tracking Local stock sale Order

The Local stock sale Order tracking can be active or passive regarding what works best for the business. Although we strongly recommend to use **Web Hook Integrations** for Physical Stores Sales Operations, since it provides the best response time.

### API Integration

It is recommended to get a list from all On Hand Orders in a specific time gap. You can use this method to display all Local stock sale orders or to double check the orders and reprocess any of it that had issues for invoicing or updating the ERP / POS inventory. Although it is not recommended to track orders using this method, for that it is needed to integrate by Web Hook APIs.

As an example you can use this request:

```shell
curl --request GET \
     --url 'https://accountname.environment.com.br/api/oms/pvt/orders?f_creationDate=creationDate%3A%5B2016-01-01T02%3A00%3A00.000Z%20TO%202021-01-01T01%3A59%3A59.999Z%5D&f_hasInputInvoice=false&f_isInstore=true' \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json'
```

This is a normal request using the Get Orders List method by OMS API. To filter VTEX Sales App orders it is needed to set the flag **f_isInstore=true.** Then to know if it is an Local stock sale Orders check if the flag **checkedInPickupPointId is not null** and compare the value of it is equal to the tag **shippingData.logisticsInfo.pickupPointId** on every product.

### Web Hook Integration

First, it is necessary to configure a web hook to receive Local stock sale orders. For this it can be used the following expression, inside the filter tag  ([Order Hooks Documentation](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#configuration-1)):

```json
{
    "filter": {
        "type": "FromOrders",
        "expression": "(\"instore\" in marketingData.marketingTags) and (checkedInPickupPointId != null) and (checkedInPickupPointId in shippingData.logisticsInfo[].pickupPointId)",
        "disableSingleFire": false
    },
    "hook": {
        "url": "https://endpoint.example/path",
            "headers": {
                "key": "value"
            }
    }
}
```

As response of this configuration, the endpoint used at the example before is going to receive the following payload when a new Local stock sale order is placed ([Order Hooks documentation](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook-notifications)):

```json
{
  "Domain": "OrdersDocumentUpdated",
  "OrderId": "v40484048naf-01",
  "State": "unknow",
  "LastState": null,
  "LastChange": "2022-12-15T20:32:06.6120711",
  "CurrentChange": "0001-01-01T00:00:00",
  "Origin": {
    "Account": "accountABC",
    "Key": "vtexappkey-keyEDF"
  }
}
```

The received order id can be used to get the full Order information, including the products on it by using the OMS API Method: Get Order ([Orders API reference](https://developers.vtex.com/vtex-rest-api/reference/getorder)).


### Invoicing Local stock sale Order

After getting the Order Data, the next step is to start an Invoice Emission, this step is not handled by VTEX and each Merchant can pick the solution that fits best their operation (ie: using POS software to emit and print it at the physical store, using ERP to send it through email…).

Regardless of the solution adopted to emit the invoice, one important thing is to attach the invoice data into the VTEX OMS system. By this, VTEX Sales App can inform the sales associate that the order invoice was invoiced. To do that, it can be used the following OMS resource sending an payload as the example below ([Order Invoice API reference](https://developers.vtex.com/vtex-rest-api/reference/invoicenotification)):

```json
{
   "type": "Output",
   "invoiceNumber": "NFe-00001",
   "courier": "",
   "trackingNumber": "",
   "trackingUrl": "",
   "items": [
      {
         "id": "345117",
         "quantity": 1,
         "description": "335",
         "price": 9003
      }
   ],
   "issuanceDate": "2013-11-21T00:00:00",
   "invoiceValue": 9508
}
```


