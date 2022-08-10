---
title: "Export endpoints"
slug: "elefantqa2-intershop-integration"
excerpt: "elefantqa2.intershop-integration@0.6.7"
hidden: true
createdAt: "2022-07-27T13:51:41.711Z"
updatedAt: "2022-07-28T13:04:01.249Z"
---
You can find the export endpoints documentation in the [export endpoints folder](export%20endpoints):

* [Categories](export%20endpoints/categories.md)
* [Products](export%20endpoints/products.md)
* [Seller offers](export%20endpoints/seller-offers.md)
* [Stock](export%20endpoints/stock.md)

#### Schema instructions:
Always when modifying a schema also update it in constants > DATA_ENTITY_ARRAY 

#### Category Schema URL - `https://elefantqa.myvtex.com/api/dataentities/category_import2/schemas/intershop`

```json
{
  "properties": {
    "vtexCategId": {
      "type": "string",
      "description": "Vtex Categ ID"
    },
    "parent": {
      "type": "string",
      "description": "ID to parent category"
    },
    "marketplaceCommission": {
      "type": "string",
      "description": "Marketplace Commission"
    },
    "oldUrl": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string"
          },
          "language": {
            "type": "string"
          }
        }
      }
    },
    "description": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string"
          },
          "language": {
            "type": "string"
          }
        }
      }
    },
    "displayName": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "value": {
            "type": "string"
          },
          "language": {
            "type": "string"
          }
        }
      }
    }
  },
  "v-indexed": ["vtexCategId"],
  "v-cache": false
}
```

#### Product Association Schema URL - `https://elefantqa.myvtex.com/api/dataentities/product_association/schemas/intershop`

- **variationAttributes is deprecated and should not be used, check product_extra_info for use**

```json
{
  "properties": {
    "masterProductIds": {
      "type": "string"
    },
    "variationAttributes": {
      "type": "array"
    },
    "vtexProductId": {
      "type": "string"
    }
  },
  "v-indexed": ["vtexProductId", "masterProductIds"],
  "v-cache": false
}
```

#### Product Extra Info Schema URL - `https://elefantqa.myvtex.com/api/dataentities/product_extra_info/schemas/intershop`

```json
{
  "properties": {
    "supplierName": {
      "type": "string"
    },
    "supplierSku": {
      "type": "string"
    },
    "vtexProductId": {
      "type": "string"
    },
    "costPrices": {
      "type": "array"
    },
    "listPrices": {
      "type": "array"
    },
    "variationAttributes": {
      "type": "array"
    }
  },
  "v-indexed": ["vtexProductId"],
  "v-cache": false
}
```

#### Product Changed Property Schema URL - `https://elefantqa.myvtex.com/api/dataentities/product_changed_property/schemas/intershop`

```json
{
  "properties": {
    "vtexProductId": {
      "type": "string"
    },
    "hasProductChanged": {
      "type": "boolean"
    },
    "isNewSellerProduct": {
      "type": "boolean"
    },
    "isProcessing": {
      "type": "boolean"
    },
    "processId": {
      "type": ["string", "null"]
    }
  },
  "v-indexed": [
    "vtexProductId",
    "hasProductChanged",
    "isNewSellerProduct",
    "isProcessing"
  ],
  "v-cache": false
}
```

#### Product offer sync Schema URL - `https://elefantqa.myvtex.com/api/dataentities/product_offer_sync/schemas/main`

```json
{
  "properties": {
    "isPriceChanged": {
      "type": "boolean",
      "description": "DEPRECATED!"
    },
    "isSkuChanged": {
      "type": "boolean",
      "description": "If true product price/stock has changed"
    },
    "isProcessing": {
      "type": "boolean",
      "description": "true if product is being processed"
    },
    "processId": {
      "type": [
        "string",
        "null"
      ]
    },
    "skuId": {
      "type": "string"
    },
    "sellerChain": {
      "type": "string"
    }
  },
  "v-indexed": [
    "isSkuChanged",
    "sellerChain",
    "isProcessing",
    "isPriceChanged",
    "skuId"
  ]
}
```

#### Product stock sync Schema URL - `https://elefantqa.myvtex.com/api/dataentities/stock_sync/schemas/main`

```json
{
  "properties": {
    "isStockChanged": {
      "type": "boolean",
      "description": "If true product stock has changed"
    },
    "sellerChain": {
      "type": "string"
    }
  },
  "v-indexed": ["isStockChanged", "sellerChain"]
}
```

#### Custom Attributes Schema URL - `https://elefantqa.myvtex.com/api/dataentities/custom_attributes/schema/intershop`

```json
{
  "properties": {
    "attributeName": {
      "type": "string"
    },
    "attributeId": {
      "type": "string"
    },
    "vtexSkuCategoryToSpecDefIds": {
      "type": "object"
    },
    "vtexProdCategoryToSpecDefIds": {
      "type": "object"
    },
    "vtexAttributeName": {
      "type": "string"
    },
    "categoryId": {
      "type": "string"
    },
    "isProductAttribute": {
      "type": "boolean"
    },
    "isSkuAttribute": {
      "type": "boolean"
    },
    "isVariationAttribute": {
      "type": "boolean"
    },
    "filter": {
      "type": "boolean"
    },
    "multipleValues": {
      "type": "boolean"
    },
    "predefinedValues": {
      "type": "boolean"
    },
    "dataType": {
      "type": "string"
    },
    "isMandatory": {
      "type": "boolean"
    },
    "attributeValues": {
      "type": "array"
    }
  },
  "v-indexed": [
    "attributeId",
    "attributeName",
    "vtexAttributeName",
    "categoryId"
  ],
  "v-cache": false
}
```

#### Custom Attribute Values Schema URL - `https://elefantqa.myvtex.com/api/dataentities/custom_attribute_values/schemas/intershop`

```json
{
  "properties": {
    "skuId": {
      "type": "string"
    }
  },
  "v-indexed": ["skuId"],
  "v-cache": false
}
```

#### MAP_TYPES pt export atribute

```Markdown table

| VTEX type | EXPORT type |
|-----------|-------------|
|     1     |   string    |
|-----------|-------------|
|     4     |     int     |
|-----------|-------------|
|     5     |   string    |
|-----------|-------------|
|     6     |   boolean   |
|-----------|-------------|
|     7     |   string    |
|-----------|-------------|
|     8     |    date     |

```

#### Seller Offers instructions:

In order to able to receive affiliate change notifications  
(ex when product price or stock is updated), make sure there  
is an affiliate with Search Endpoint set to:  
https://{env}.myvtex.com/_v/intershop/affiliate/notification  
(In Admin -> Orders => Orders management => Settings => Affiliates)

In order to check if there are any crons running on this environment  
you should send a request from postman:  
METHOD: GET  
URL: http://{env}.myvtex.com/api/scheduler/{workspace}/intershop-sync?version=4


#### SFTP Connection Settings

In order to be able to export any file on SFTP make sure there is the correct sftp user 
added in app settings:
(Admin -> Account Settings -> Apps -> My apps => Intershop Integration setup) 

Also, if the connection require passphrase, make sure to have this one added in app settings as well. 

#### Setup for CRON

1. Create CRON using V4 Scheduler:

Method - POST; Endpoint - http://{{account}}.{{environment}}/api/scheduler/:workspace/:app

Params:
  Query Params:
  KEY: version ; Value: 4

  Path Variables:
  KEY: workspace; Value: yourWorkspace or master
  KEY: app;       Value: intershop-integration

Headers:
  KEY: Content-Type; Value: application/json
  KEY: X-VTEX-API-AppKey;   Value: {{X-VTEX-API-AppKey}}.
  KEY: X-VTEX-API-AppTokem; Value: {{X-VTEX-API-AppToken}}

Body:
{
  "id": "test-create-ping-scheduler", 
  "scheduler": {
      "expression": "*/5 * * * *",
      "endDate": "2222-03-13T23:59:00"
  },
  "request": {
      "uri": "https://{{replaceWithPublicDNS}}/_v/intershop/ping?workspace=yourWorkspace",
      "method": "GET",
      "body": {
          "test": "TestPingScheduler"
      }
  }
}

2. Update CRON:

Method - PUT; Endpoint - http://{{account}}.{{environment}}/api/scheduler/:workspace/:app

Params:
    Query Params:
    KEY: version ; Value: 4

    Path Variables:
    KEY: workspace; Value: yourWorkspace or master
    KEY: app;       Value: intershop-integration

Headers:
    KEY: Content-Type; Value: application/json
    KEY: X-VTEX-API-AppKey;   Value: {{X-VTEX-API-AppKey}}.
    KEY: X-VTEX-API-AppTokem; Value: {{X-VTEX-API-AppToken}}

Body:
{
  "id": "test-create-ping-scheduler", 
  "scheduler": {
      "expression": "*/5 * * * *",
      "endDate": "2222-03-13T23:59:00"
  },
  "request": {
      "uri": "https://{{replaceWithPublicDNS}}/_v/intershop/ping?workspace=yourWorkspace",
      "method": "GET",
      "body": {
          "test": "TestPingScheduler"
      }
  }
}

3. Delete CRON

Method - DEL; Endpoint - http://{{account}}.{{environment}}/api/scheduler/:workspace/:app/:id

Params:
    Query Params:
    KEY: version ; Value: 4

    Path Variables:
    KEY: workspace; Value: yourWorkspace or master
    KEY: app;       Value: intershop-integration
    KEY: id;        Value: test-create-ping-scheduler (from your POST Method's BODY)

Headers:
    KEY: Content-Type; Value: application/json
    KEY: X-VTEX-API-AppKey;   Value: {{X-VTEX-API-AppKey}}
    KEY: X-VTEX-API-AppTokem; Value: {{X-VTEX-API-AppToken}}

Download the Postman Collection: https://gitlab.com/vtexro/1st-party-apps/elefant/intershop-integration/-/wikis/scheduler%20collection

## Affiliate Event Flow

![Affiliate Event Flow](/docs/AffiliateEventFlow.png "Affiliate Event Flow")

## Cron - Stock Update

![Cron - Stock Update](/docs/Cron - Stock Update.png "Cron - Stock Update")

## Export Offers Intershop

![ExportOffersIntershop](/docs/ExportOffersIntershop.png "ExportOffersIntershop")

## Process Vendor Offers Ids

![ProcessVendorOffersIds](/docs/ProcessVendorOffersIds.png "ProcessVendorOffersIds")

## Seller Offer Sync Event

![SellerOfferSyncEvent](/docs/SellerOfferSyncEvent.png "SellerOfferSyncEvent")