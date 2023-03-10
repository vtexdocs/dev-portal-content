---
title: "Consult product search information"
slug: "consult-product-search-information"
hidden: false
createdAt: "2022-10-14T21:11:36.747Z"
updatedAt: "2022-11-02T14:39:45.843Z"
---

It is essential to understand the products searched in your store to present personalized marketing information to shoppers. You can use the [Intelligent Search API](https://developers.vtex.com/vtex-rest-api/reference/intelligent-search-api-overview), as detailed in the following sections, to gather information about shoppers’ product searches. This way, you can create [synonyms](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/1pxAWPEglBey1UFdvcetZV) or [banners](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/1pxAWPEglBey1UFdvcetZV) that include common searches on your store.


## Get a list of suggested terms for a search term

To get a list of suggested terms for a search term, you must use the [Get list of suggested terms similar to the search term](https://developers.vtex.com/vtex-rest-api/reference/get_search-suggestions) endpoint. You can filter the endpoint response by defining the term's `locale` and `query`.

**Response body example:**

```json
{
  "searches": [
	{
  	"term": "mountain bike",
  	"count": 66
	},
	{
  	"term": "bike helmet",
  	"count": 121
	},
	{
  	"term": "electric bike",
  	"count": 78
	},
	{
  	"term": "bike rack",
  	"count": 161
	},
	{
  	"term": "road bike",
  	"count": 28
	}
  ]
}
```

## Get correction of misspelled words of a search

To get the system corrections for a misspelled search term, you must use the [Get attempt of correction of a misspelled term](https://developers.vtex.com/vtex-rest-api/reference/get_correction-search) endpoint. You can filter the endpoint response by defining the term's `locale` and `query`.

**Response body example:**

```json
{
  "correction": {
	"correction": true,
	"misspelled": true,
	"text": "mountain bike",
	"highlighted": "mountain <em>bike</em>"
  }
}
```

## Get product list for a specific search

To get a product list for a search term, you must use the [Get list of products for a query](https://developers.vtex.com/vtex-rest-api/reference/get_product-search-facets) endpoint. You can filter the endpoint response by defining the term's `locale` and `query`.

**Response body example:**

```json
{
  "products": [
	{
  	"cacheId": "sp-2000003",
  	"productId": "2000003",
  	"description": "With this beautiful design piece you will never miss an appointment anymore. Yay.",
  	"productName": "Top Wood Clock",
  	"productReference": "clock120",
  	"linkText": "wood-clock",
  	"brand": "Sony",
  	"brandId": 2000005,
  	"link": "/wood-clock/p",
  	"categories": [
    	"/Home & Decor/"
  	],
  	"categoryId": "40",
  	"categoriesIds": [
    	"/40/"
  	],
  	"priceRange": {
    	"sellingPrice": {
      	"highPrice": 197.99,
      	"lowPrice": 197.99
    	},
    	"listPrice": {
      	"highPrice": 197.99,
      	"lowPrice": 197.99
    	}
  	},
  	"specificationGroups": [
    	{
      	"originalName": "allSpecifications",
      	"name": "allSpecifications",
      	"specifications": [
        	{
          	"originalName": "sellerId",
          	"name": "sellerId",
          	"values": [
            	"1"
          	]
        	}
      	]
    	}
  	],
  	"skuSpecifications": [],
  	"productClusters": [
    	{
      	"id": "1970",
      	"name": "Summer"
    	}
  	],
  	"clusterHighlights": [
    	{
      	"id": "1970",
      	"name": "Summer"
    	}
  	],
  	"properties": [
    	{
      	"name": "sellerId",
      	"originalName": "sellerId",
      	"values": [
        	"1"
      	]
    	}
  	],
  	"items": [
    	{
      	"sellers": [
        	{
          	"sellerId": "1",
          	"sellerName": "VTEX",
          	"addToCartLink": "",
          	"sellerDefault": true,
          	"commertialOffer": {
            	"DeliverySlaSamplesPerRegion": {},
            	"DeliverySlaSamples": [],
            	"AvailableQuantity": 10000,
            	"discountHighlights": [],
            	"Installments": [
              	{
                	"Value": 197.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 1,
                	"Name": "American Express à vista",
                	"PaymentSystemName": "American Express"
              	},
              	{
                	"Value": 197.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 1,
                	"Name": "Visa à vista",
                	"PaymentSystemName": "Visa"
              	},
              	{
                	"Value": 98.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 2,
                	"Name": "Visa 2 vezes sem juros",
                	"PaymentSystemName": "Visa"
              	},
              	{
                	"Value": 65.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 3,
                	"Name": "Visa 3 vezes sem juros",
                	"PaymentSystemName": "Visa"
              	},
              	{
                	"Value": 49.49,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 4,
                	"Name": "Visa 4 vezes sem juros",
                	"PaymentSystemName": "Visa"
              	},
              	{
                	"Value": 39.59,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 5,
                	"Name": "Visa 5 vezes sem juros",
                	"PaymentSystemName": "Visa"
              	},
              	{
                	"Value": 32.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 6,
                	"Name": "Visa 6 vezes sem juros",
                	"PaymentSystemName": "Visa"
              	},
              	{
                	"Value": 197.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 1,
                	"Name": "Diners à vista",
                	"PaymentSystemName": "Diners"
              	},
              	{
                	"Value": 100.48,
                	"InterestRate": 100,
                	"TotalValuePlusInterestRate": 200.96,
                	"NumberOfInstallments": 2,
                	"Name": "Diners 2 vezes com juros",
                	"PaymentSystemName": "Diners"
              	},
              	{
                	"Value": 197.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 1,
                	"Name": "Mastercard à vista",
                	"PaymentSystemName": "Mastercard"
              	},
              	{
                	"Value": 197.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 1,
                	"Name": "Boleto Bancário à vista",
                	"PaymentSystemName": "Boleto Bancário"
              	},
              	{
                	"Value": 197.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 1,
                	"Name": "Vale à vista",
                	"PaymentSystemName": "Vale"
              	},
              	{
                	"Value": 197.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 1,
                	"Name": "Promissory à vista",
                	"PaymentSystemName": "Promissory"
              	},
              	{
                	"Value": 197.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 1,
                	"Name": "Customer Credit à vista",
                	"PaymentSystemName": "Customer Credit"
              	},
              	{
                	"Value": 98.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 2,
                	"Name": "Customer Credit 2 vezes sem juros",
                	"PaymentSystemName": "Customer Credit"
              	},
              	{
                	"Value": 67.97,
                	"InterestRate": 100,
                	"TotalValuePlusInterestRate": 203.91,
                	"NumberOfInstallments": 3,
                	"Name": "Customer Credit 3 vezes com juros",
                	"PaymentSystemName": "Customer Credit"
              	},
              	{
                	"Value": 197.99,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 197.99,
                	"NumberOfInstallments": 1,
                	"Name": "Free à vista",
                	"PaymentSystemName": "Free"
              	}
            	],
            	"Price": 197.99,
            	"ListPrice": 197.99,
            	"spotPrice": 197.99,
            	"taxPercentage": 0,
            	"PriceWithoutDiscount": 197.99,
            	"Tax": 0,
            	"GiftSkuIds": [],
            	"BuyTogether": [],
            	"ItemMetadataAttachment": [],
            	"RewardValue": 0,
            	"PriceValidUntil": "2023-04-01T13:13:20Z",
            	"GetInfoErrorMessage": null,
            	"CacheVersionUsedToCallCheckout": "",
            	"teasers": [
              	{
                	"name": "8% Boleto",
                	"conditions": {
                  	"minimumQuantity": 0,
                  	"parameters": [
                    	{
                      	"name": "PaymentMethodId",
                      	"value": "6"
                    	}
                  	]
                	},
                	"effects": {
                  	"parameters": [
                    	{
                      	"name": "PercentualDiscount",
                      	"value": "8.0"
                    	}
                  	]
                	}
              	}
            	]
          	}
        	}
      	],
      	"images": [
        	{
          	"imageId": "155484",
          	"cacheId": "155484",
          	"imageTag": "",
          	"imageLabel": "",
          	"imageText": "",
          	"imageUrl": "https://storecomponents.vtexassets.com/arquivos/ids/155484/Frame.jpg?v=636793817478300000"
        	},
        	{
          	"imageId": "155485",
          	"cacheId": "155485",
          	"imageTag": "",
          	"imageLabel": "",
          	"imageText": "",
          	"imageUrl": "https://storecomponents.vtexassets.com/arquivos/ids/155485/Frame-1.jpg?v=636793817642000000"
        	},
        	{
          	"imageId": "155486",
          	"cacheId": "155486",
          	"imageTag": "",
          	"imageLabel": "",
          	"imageText": "",
          	"imageUrl": "https://storecomponents.vtexassets.com/arquivos/ids/155486/Frame-2.jpg?v=636793817785530000"
        	}
      	],
      	"itemId": "2000534",
      	"name": "1",
      	"nameComplete": "Top Wood Clock 1",
      	"complementName": "",
      	"referenceId": [
        	{
          	"Key": "RefId",
          	"Value": "16001"
        	}
      	],
      	"measurementUnit": "un",
      	"unitMultiplier": 1,
      	"variations": [],
      	"ean": "16001",
      	"modalType": "",
      	"videos": [],
      	"attachments": [],
      	"isKit": false
    	}
  	],
  	"origin": "intelligent-search"
	},
	{
  	"cacheId": "sp-2000214",
  	"productId": "2000214",
  	"description": "",
  	"productName": "kevin1",
  	"linkText": "kevin1-lkn",
  	"brand": "Sony",
  	"brandId": 2000005,
  	"link": "/kevin1-lkn/p",
  	"categories": [
    	"/Home & Decor/"
  	],
  	"categoryId": "40",
  	"categoriesIds": [
    	"/40/"
  	],
  	"priceRange": {
    	"sellingPrice": {
      	"highPrice": 10,
      	"lowPrice": 10
    	},
    	"listPrice": {
      	"highPrice": 10,
      	"lowPrice": 10
    	}
  	},
  	"specificationGroups": [
    	{
      	"originalName": "allSpecifications",
      	"name": "allSpecifications",
      	"specifications": [
        	{
          	"originalName": "sellerId",
          	"name": "sellerId",
          	"values": [
            	"1"
          	]
        	}
      	]
    	}
  	],
  	"skuSpecifications": [],
  	"productClusters": [],
  	"clusterHighlights": [],
  	"properties": [
    	{
      	"name": "sellerId",
      	"originalName": "sellerId",
      	"values": [
        	"1"
      	]
    	}
  	],
  	"items": [
    	{
      	"sellers": [
        	{
          	"sellerId": "1",
          	"sellerName": "VTEX",
          	"addToCartLink": "",
          	"sellerDefault": true,
          	"commertialOffer": {
            	"DeliverySlaSamplesPerRegion": {},
            	"DeliverySlaSamples": [],
            	"AvailableQuantity": 10000,
            	"discountHighlights": [],
            	"Installments": [
              	{
                	"Value": 10,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 10,
                	"NumberOfInstallments": 1,
                	"Name": "American Express à vista",
                	"PaymentSystemName": "American Express"
              	},
              	{
                	"Value": 10,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 10,
                	"NumberOfInstallments": 1,
                	"Name": "Visa à vista",
                	"PaymentSystemName": "Visa"
              	},
              	{
                	"Value": 10,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 10,
                	"NumberOfInstallments": 1,
                	"Name": "Diners à vista",
                	"PaymentSystemName": "Diners"
              	},
              	{
                	"Value": 10,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 10,
                	"NumberOfInstallments": 1,
                	"Name": "Mastercard à vista",
                	"PaymentSystemName": "Mastercard"
              	},
              	{
                	"Value": 10,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 10,
                	"NumberOfInstallments": 1,
                	"Name": "Boleto Bancário à vista",
                	"PaymentSystemName": "Boleto Bancário"
              	},
              	{
                	"Value": 10,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 10,
                	"NumberOfInstallments": 1,
                	"Name": "Vale à vista",
                	"PaymentSystemName": "Vale"
              	},
              	{
                	"Value": 10,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 10,
                	"NumberOfInstallments": 1,
                	"Name": "Promissory à vista",
                	"PaymentSystemName": "Promissory"
              	},
              	{
                	"Value": 10,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 10,
                	"NumberOfInstallments": 1,
                	"Name": "Customer Credit à vista",
                	"PaymentSystemName": "Customer Credit"
              	},
              	{
                	"Value": 5,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 10,
                	"NumberOfInstallments": 2,
                	"Name": "Customer Credit 2 vezes sem juros",
                	"PaymentSystemName": "Customer Credit"
              	},
              	{
                	"Value": 3.43,
                	"InterestRate": 100,
                	"TotalValuePlusInterestRate": 10.29,
                	"NumberOfInstallments": 3,
                	"Name": "Customer Credit 3 vezes com juros",
                	"PaymentSystemName": "Customer Credit"
              	},
              	{
                	"Value": 10,
                	"InterestRate": 0,
                	"TotalValuePlusInterestRate": 10,
                	"NumberOfInstallments": 1,
                	"Name": "Free à vista",
                	"PaymentSystemName": "Free"
              	}
            	],
            	"Price": 10,
            	"ListPrice": 10,
            	"spotPrice": 10,
            	"taxPercentage": 0,
            	"PriceWithoutDiscount": 10,
            	"Tax": 0,
            	"GiftSkuIds": [],
            	"BuyTogether": [],
            	"ItemMetadataAttachment": [],
            	"RewardValue": 0,
            	"PriceValidUntil": "2023-04-01T13:13:20Z",
            	"GetInfoErrorMessage": null,
            	"CacheVersionUsedToCallCheckout": "",
            	"teasers": [
              	{
                	"name": "8% Boleto",
                	"conditions": {
                  	"minimumQuantity": 0,
                  	"parameters": [
                    	{
                      	"name": "PaymentMethodId",
                      	"value": "6"
                    	}
                  	]
                	},
                	"effects": {
                  	"parameters": [
                    	{
                      	"name": "PercentualDiscount",
                      	"value": "8.0"
                    	}
                  	]
                	}
              	}
            	]
          	}
        	}
      	],
      	"images": [
        	{
          	"imageId": "155675",
          	"cacheId": "155675",
          	"imageTag": "",
          	"imageLabel": "vtex",
          	"imageText": "vtex",
          	"imageUrl": "https://storecomponents.vtexassets.com/arquivos/ids/155675/vtex.jpg?v=637655270451200000"
        	}
      	],
      	"itemId": "310124211",
      	"name": "kevin1sku",
      	"nameComplete": "kevin1sku",
      	"complementName": "",
      	"referenceId": [
        	{
          	"Key": "RefId",
          	"Value": "2983678w63478"
        	}
      	],
      	"measurementUnit": "un",
      	"unitMultiplier": 1,
      	"variations": [],
      	"ean": "2398428937489",
      	"modalType": "",
      	"videos": [],
      	"attachments": [],
      	"isKit": false
    	}
  	],
  	"origin": "intelligent-search"
	}
  ],
  "recordsFiltered": 5,
  "correction": {
	"misspelled": false
  },
  "fuzzy": "0",
  "operator": "and",
  "translated": false
}
```

