---
title: "Financial commission for Marketplace"
slug: "vtex-marketplace-financial-commission"
excerpt: "vtex.marketplace-financial-commission@0.3.21"
hidden: true
createdAt: "2022-07-11T20:29:08.191Z"
updatedAt: "2022-08-01T21:24:14.179Z"
---
# API REST
 > **Warning** 
 > Some endpoints exposed by this app are meant to be used in integrations. Pay attention to the Authorization header in each of the REST endpoints. If they require type: bearer it means that a token must be generated using this endpoint or via the admin panel.

 <br />

# Dashboard

## List Sellers
![](https://img.shields.io/static/v1?label=&message=GET&color=blue) `https://{{accountmarketplace}}.myvtex.com/_v/sellers/list`

This endpoint lists all Sellers.

##### PATH PARAMS
| accountmarketplace  |
| ------------ |
|  Name of the VTEX account of the marketplace. |

```bash
curl --request GET \
  --url https://example.myvtex.com/_v/sellers/list
```

#### **Response**

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`

```json
{
	"items": [
		{
			"id": "1",
			"name": "seller name",
			"account": "seller account",
			"productCommissionPercentage": 0,
			"freightCommissionPercentage": 0,
			"isActive": true
		},
		{
			...
		}
	],
	"paging": {
		"total": 90
	}
}
```
__________________________________________________

## Generate Dashboard
![](https://img.shields.io/static/v1?label=&message=POST&color=brightgreen) `https://app.io.vtex.com/vtex.marketplace-financial-commission/v0/{{accountmarketplace}}/master/dashboard/generate`

This endpoint is in charge of generating the commissions dashboard.

<br />

#### **Headers**
| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| X-VTEX-API-AppKey       | string      | Yes       |The AppKey configured by the merchant             |
| X-VTEX-API-AppToken     | string      | Yes       |The AppToken configured by the merchant           | 

<br />

#### **Path parameters**

| accountmarketplace  |
| ------------ |
|  Name of the VTEX account of the marketplace. |

<br />

#### **Request parameters allowed**
| Attribute   | Type        | Mandatory | Description |
| ----------- | ----------- |---------- | ----------- |
| dateStart   | string      | No        |Start date of generation in ```"yyyy-mm-dd"``` format          |
| dateEnd     | string      | No        |End date of generation in ```"yyyy-mm-dd"``` format            | 

<br />

```bash
curl --request POST \
  --url 'https://app.io.vtex.com/vtex.marketplace-financial-commission/v0/example/master/dashboard/generate?dateStart=2022-04-25&dateEnd=2022-04-30' \
  --header 'X-VTEX-API-AppKey: 12345' \
  --header 'X-VTEX-API-AppToken: 12345'
```
<br />

#### **Response** 

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`\
If the number of days is less than 5 days

```json
{
	"Sellers": [
		{
			"Id": "vtex_marketplace_financial_commission_sellersdashboards-DSH-example-2022-01-16",
			"Href": "http://api.vtex.com/api/dataentities/vtex_marketplace_financial_commission_sellersdashboards/documents/DSH-example-2022-01-16?an=example&_schema=0.0.1",
			"DocumentId": "DSH-example-2022-01-16"
		}
	],
	"Statistics": [
		{
			"Id": "vtex_marketplace_financial_commission_statisticsdashboards-DSH-Statistics-example-2022-01-16",
			"Href": "http://api.vtex.com/api/dataentities/vtex_marketplace_financial_commission_statisticsdashboards/documents/DSH-Statistics-example-2022-01-16?an=example&_schema=0.0.1",
			"DocumentId": "DSH-Statistics-example-2022-01-16"
		}
	]
}
```
\
If the number of days is greater than 5 days

```json
{
	"message": "We are processing your request, please validate in 15 minutes."
}
```
<br />

> **Note** If the volume of information to be generated is large, it is recommended to do it for each day of the month.

__________________________________________________

## Search Sellers Dashboard
![](https://img.shields.io/static/v1?label=&message=GET&color=blue) `https://{{accountmarketplace}}.myvtex.com/_v/dashboard/sellers/search`

Retrieve commission information of the sellers,  for a specific date range, from the orders that are invoiced in VTEX.

<br />

#### **Path parameters**

| accountmarketplace  |
| ------------ |
|  Name of the VTEX account of the marketplace. |

<br />

#### **Request parameters allowed**
| Attribute     | Type        | Mandatory | Description |
| -----------   | ----------- |---------- | ----------- |
| dateStart     | string      | Yes       | Start date of consulting  in ```"yyyy-mm-dd"``` format          |
| dateEnd       | string      | Yes       | End date of consulting  in ```"yyyy-mm-dd"``` format            |
| page          | number      | Yes       | Page Number                                                     |
| pageSize      | number      | Yes       | Number of items per page                                        |
| sellersId     | string      | No        | Sellers to be returned in the query. Separate the seller's Id with commas. For example ```sellersId=sellerId1,sellerId2,sellerId3```. You can also leave empty to get all sellers. | 
| reIndex       | boolean     | No        | Performs reindex of the search by refreshing and updating the information. | 

<br />

```bash
curl --request GET \
  --url 'https://example.myvtex.com/_v/dashboard/sellers/search?dateStart=2022-04-01&dateEnd=2022-04-30&page=1&pageSize=20&reIndex=true' \
```
<br />

#### **Response** 

| Attribute          | Type        | Description                                      |
| --------------     | ----------- |------------------------------------------------- |
| dateStart          | string      | Start date of consulting  in ```"yyyy-mm-dd"``` format  |
| dateEnd            | string      | End date of consulting  in ```"yyyy-mm-dd"``` format    |
| sellers            | object      | Array with sellers                                      |
| id                 | string      | Seller id                                               |
| account            | string      | Seller account                                          |
| name               | string      | Seller name                                             |
| statistics         | object      | Object with seller's totals                             |
| ordersCount        | number      | Number of orders                                        |
| totalComission     | number      | Total commission value                                  |
| totalComission     | number      | Total order value                                       |
| outstandingBalance | number      | Total invoiced value                                    |


![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`\
If the number of days is less than 5 days

```json
{
	"dateStart": "2022-04-01",
	"dateEnd": "2022-04-30",
	"sellers": [
		{
			"id": "sellerId1",
			"account": "sellerId1",
			"name": "sellerId1_Name",
			"statistics": {
				"ordersCount": 252,
				"totalComission": 396.11,
				"totalOrderValue": 3784,
				"outstandingBalance": 0
			}
		},
    {
      ...
    }
	],
	"pagination": {
		"currentPage": 1,
		"pageSize": 20,
		"totalPage": 5
	}
}

```

<br />

### Search for specific sellersId
> When specifying one or more sellers in the search in the service it will additionally return the ```statistics``` object, returning the total statistics.

```bash
curl --request GET \
  --url 'https://example.myvtex.com/_v/dashboard/sellers/search?dateStart=2022-04-01&dateEnd=2022-04-30&page=1&pageSize=20&sellersId=sellerId1&reIndex=true' \
```
<br />

#### **Response** 

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`

```json
{
	"dateStart": "2022-04-01",
	"dateEnd": "2022-04-30",
	"sellers": [
		{
			"id": "sellerId1",
			"account": "sellerId1",
			"name": "sellerId1_Name",
			"statistics": {
				"ordersCount": 252,
				"totalComission": 396.11,
				"totalOrderValue": 3784,
				"outstandingBalance": 0
			}
		}
	],
	"statistics": {
		"ordersCount": 252,
		"totalComission": 396.11,
		"totalOrderValue": 3784
	},
	"pagination": {
		"currentPage": 1,
		"pageSize": 1,
		"totalPage": 1
	}
}

```

<br />
__________________________________________________

## Search Statistics Dashboard
![](https://img.shields.io/static/v1?label=&message=GET&color=blue) `https://{{accountmarketplace}}.myvtex.com/_v/dashboard/statistics/search`

Retrieve totals information of the sellers,  for a specific date range, from the orders that are invoiced in VTEX.

<br />

#### **Path parameters**

| accountmarketplace  |
| ------------ |
|  Name of the VTEX account of the marketplace. |

<br />

#### **Request parameters allowed**
| Attribute     | Type        | Mandatory | Description |
| -----------   | ----------- |---------- | ----------- |
| dateStart     | string      | Yes       | Start date of consulting  in ```"yyyy-mm-dd"``` format  |
| dateEnd       | string      | Yes       | End date of consulting  in ```"yyyy-mm-dd"``` format    | 

<br />

```bash
curl --request GET \
  --url 'https://example.myvtex.com/_v/dashboard/statistics/search?dateStart=2022-04-01&dateEnd=2022-04-30' \
```
<br />

#### **Response** 

| Attribute          | Type        | Description                                      |
| --------------     | ----------- |------------------------------------------------- |
| dateStart          | string      | Start date of consulting  in ```"yyyy-mm-dd"``` format  |
| dateEnd            | string      | End date of consulting  in ```"yyyy-mm-dd"``` format    |
| statistics         | object      | Object with seller's totals                             |
| ordersCount        | number      | Number of orders                                        |
| totalComission     | number      | Total commission value                                  |
| totalComission     | number      | Total order value                                       |

<br />

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`

```json
{
	"dateStart": "2022-04-01",
	"dateEnd": "2022-04-30",
	"statistics": {
		"ordersCount": 264,
		"totalComission": 398.61,
		"totalOrderValue": 4716.8
	}
}

```

<br />
__________________________________________________

# Token Authorization

## Create Token
![](https://img.shields.io/static/v1?label=&message=POST&color=brightgreen) `https://app.io.vtex.com/vtex.marketplace-financial-commission/v0/{{accountmarketplace}}/master/_v/token/{{sellerId}}`

Create a security token for a specific seller.

<br />

#### **Headers**
| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| X-VTEX-API-AppKey       | string      | Yes       |The AppKey configured by the merchant             |
| X-VTEX-API-AppToken     | string      | Yes       |The AppToken configured by the merchant           | 

<br />

#### **Path parameters**

| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| accountmarketplace      | string      | Yes       | Name of the VTEX account of the marketplace.             |
| sellerId                | string      | Yes       | Seller Id                                                | 

<br />

```bash
curl --request POST \
  --url https://app.io.vtex.com/vtex.marketplace-financial-commission/v0/example/master/_v/token/sellerId1 \
  --header 'X-VTEX-API-AppKey: 12345' \
  --header 'X-VTEX-API-AppToken: 12345'
```
<br />

#### **Response** 

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`\

```json
{
	"message": "Successful token creation",
	"sellerId": "sellerId1",
	"autheticationToken": "abcdefghijk123456789",
	"creationDate": "2022-05-31T19:56:26.291Z",
	"resultVBase": [
		{
			"path": "/example/master/buckets/vtex.marketplace-financial-commission/TokenConfig/files/martketplaceSellerID1",
			"hash": "F5C201AD90EBF1C5E7D8F9412334"
		}
	]
}

```

<br />
__________________________________________________

## Get Token
![](https://img.shields.io/static/v1?label=&message=GET&color=blue) `https://app.io.vtex.com/vtex.marketplace-financial-commission/v0/{{accountmarketplace}}/master/_v/token/{{sellerId}}`

Retrieves the token information created for a specific seller.

<br />

#### **Headers**
| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| X-VTEX-API-AppKey       | string      | Yes       |The AppKey configured by the merchant             |
| X-VTEX-API-AppToken     | string      | Yes       |The AppToken configured by the merchant           | 

<br />

#### **Path parameters**

| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| accountmarketplace      | string      | Yes       | Name of the VTEX account of the marketplace.             |
| sellerId                | string      | Yes       | Seller Id                                                | 

<br />

```bash
curl --request GET \
  --url https://app.io.vtex.com/vtex.marketplace-financial-commission/v0/example/master/_v/token/sellerId1 \
  --header 'X-VTEX-API-AppKey: 12345' \
  --header 'X-VTEX-API-AppToken: 12345'
```
<br />

#### **Response** 

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`\

```json
{
	"account": "sellerId1",
	"autheticationToken": "abcdefghijk123456789",
	"enabled": true,
	"name": "sellerId1_name",
	"id": "sellerId1"
}

```

<br />
__________________________________________________

## Update Token
![](https://img.shields.io/static/v1?label=&message=PUT&color=orange) `https://app.io.vtex.com/vtex.marketplace-financial-commission/v0/{{accountmarketplace}}/master/_v/token/{{sellerId}}`

Allows you to update the status of the token

<br />

#### **Headers**
| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| X-VTEX-API-AppKey       | string      | Yes       |The AppKey configured by the merchant             |
| X-VTEX-API-AppToken     | string      | Yes       |The AppToken configured by the merchant           | 

<br />

#### **Path parameters**

| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| accountmarketplace      | string      | Yes       | Name of the VTEX account of the marketplace.             |
| sellerId                | string      | Yes       | Seller Id                                                | 

<br />

```bash
curl --request PUT \
  --url https://app.io.vtex.com/vtex.marketplace-financial-commission/v0/example/master/_v/token/sellerId1 \
  --header 'X-VTEX-API-AppKey: 12345' \
  --header 'X-VTEX-API-AppToken: 12345'
```
<br />

#### **Request Body Example** 

| Attribute                   | Type        | Description                                             |
| ----------------------------| ----------- |-------------------------------------------------------- |
| enabled                     | boolean     | Indicates whether the token is enabled or disabled.     |


```json
{
	"enabled": true
}

```

<br />

#### **Response** 

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`\

```json
{
	"message": "Successful token update",
	"sellerId": "sellerId1",
	"lastModificationDate": "2022-05-31T19:57:54.745Z",
	"resultVBase": [
		{
			"path": "/example/master/buckets/vtex.marketplace-financial-commission/TokenConfig/files/martketplaceSellerID1",
			"hash": "6ADD1F2B0F5614326400BA0F3132456"
		}
	]
}

```
__________________________________________________
<br />

# Seller Invoice Detail


## Search Orders
![](https://img.shields.io/static/v1?label=&message=GET&color=blue) `https://{{accountmarketplace}}.myvtex.com/_v/private/orders`

Retrieve a list of orders according to the filters described below, for a specific date range, from the orders placed in VTEX. 

<br />

> **Note** The date range is the creation date of the orders if the filtered status is ```Invoiced``` it will be filtered by invoice date in VTEX.

<br />

#### **Path parameters**

| accountmarketplace  |
| ------------ |
|  Name of the VTEX account of the marketplace. |

<br />

#### **Authorization**
> **Type** ```Bearer Token```

| Attribute | Type        | Mandatory | Description |
| ----------| ----------- |---------- | ----------- |
| Token     | string      | Yes       |The token configured by the marketplace in financial commission             |


<br />

#### **Request filters allowed**
| Attribute     | Type        | Mandatory | Description |
| -----------   | ----------- |---------- | ----------- |
| dateStart     | string      | Yes       | Start date of consulting  in ```"yyyy-mm-dd"``` format  |
| dateEnd       | string      | Yes       | End date of consulting  in ```"yyyy-mm-dd"``` format    |
| page          | number      | Yes       | Page Number                                             |
| perpage       | number      | Yes       | Number of items per page                                |
| sellerId      | string      | Yes       | Seller ID                                               |
| status        | string      | No        | Order Status Value                                      | 

<br />

##### **Order Status avaible to filter**

| Status                               | 
| ----------------------------------   | 
| waiting-for-sellers-confirmation     | 
| payment-pending                      | 
| payment-approved                     | 
| ready-for-handling                   | 
| handling                             | 
| invoiced                             |
| canceled                             |  

<br />

```bash
curl --request GET \
  --url 'https://example.myvtex.com/_v/private/orders?dateStart=2022-04-01&dateEnd=2022-01-30&page=1&perpage=100&sellerId=sellerId1' \
  --header 'Authorization: Bearer abcdefghijk12345'
```
<br />

#### **Response** 

| Attribute                   | Type        | Description                                             |
| ----------------------------| ----------- |-------------------------------------------------------- |
| data                        | object      | Order detail                                            |
| orderId                     | string      | Order Id                                                |
| sellerOrderId               | string      | Order Seller Id                                         |
| totalOrderValue             | number      | Payment value                                           |
| totalComission              | number      | Commission on payment value                             |
| status                      | string      | Order status                                            |
| statusDescription           | string      | Status description                                      |
| creationDate                | string      | Order creation date                                     |
| rate                        | object      | Rate detail object                                      |
| itemId                      | string      | Item id                                                 |
| nameItem                    | string      | Item name                                               |
| rate                        | object      | Array object to contain the rates configured by item    |
| freightCommissionPercentage | number      | Freight commission percentage                           |
| productCommissionPercentage | number      | Product commission percentage                           |
| paging                      | object      | Paging details object                                   |
| total                       | number      | Total number of items                                   |
| pages                       | number      | Paging total pages                                      |
| currentPage                 | number      | Current page                                            |
| perPage                     | number      | Paging total per Page                                   |

<br />

> **Warning**
>* Throttling: Each account can make up to 5000 requests per minute.
>* The maximum number of items per page is 100.
>* The maximum number of pages to process is 30, if the number of pages is more than 30, you must refine the filter.

<br />

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`

```json
{
	"data": [
		{
			"orderId": "123456789-01",
			"sellerOrderId": "GCB-123456789-01",
			"totalOrderValue": 27,
			"totalComission": 6.75,
			"status": "payment-approved",
			"statusDescription": "Pagamento Aprovado",
			"creationDate": "2022-05-25T11:08:01.3004547+00:00",
			"rate": [
				{
					"itemId": "116",
					"nameItem": "Sare marina grunjoasa Solaris, 500 g",
					"rate": {
						"freightCommissionPercentage": 0,
						"productCommissionPercentage": 25
					}
				}
			]
		},
		{
			...
		}
  ],
	"paging": {
		"total": 232,
		"pages": 3,
		"currentPage": 1,
		"perPage": 100
	}
}

```
<br />
__________________________________________________

## Generate Invoice 
![](https://img.shields.io/static/v1?label=&message=GET&color=blue) `https://app.io.vtex.com/vtex.marketplace-financial-commission/v0/{{accountmarketplace}}/master/dashboard/generate`

This endpoint is responsible for generating the invoices, according to the cut-off cycle programmed in the marketplace or seller's configuration in the marketplace-financial-commission application.

<br />

#### **Headers**
| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| X-VTEX-API-AppKey       | string      | Yes       |The AppKey configured by the merchant             |
| X-VTEX-API-AppToken     | string      | Yes       |The AppToken configured by the merchant           | 

<br />

#### **Path parameters**

| accountmarketplace  |
| ------------ |
|  Name of the VTEX account of the marketplace. |

<br />


```bash
curl --request GET \
  --url 'https://app.io.vtex.com/vtex.marketplace-financial-commission/v0/example/master/invoice/generate ' \
  --header 'X-VTEX-API-AppKey: 12345' \
  --header 'X-VTEX-API-AppToken: 12345'
```
<br />

#### **Response** 

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`\

<br />
__________________________________________________

## List of invoices issued to the seller

![](https://img.shields.io/static/v1?label=&message=POST&color=brightgreen) `https://{{accountmarketplace}}.myvtex.com/_v/financial-commission/{{sellerId}}/invoices`

Retrieve a list of invoices for a specific seller in a date range.

<br />

#### **Authorization**
> **Type** ```Bearer Token```

| Attribute | Type        | Mandatory | Description |
| ----------| ----------- |---------- | ----------- |
| Token     | string      | Yes       |The token configured by the marketplace in financial commission             |


<br />

#### **Path parameters**

| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| accountmarketplace      | string      | Yes       | Name of the VTEX account of the marketplace.             |
| sellerId                | string      | Yes       | Seller Id                                                | 

<br />

#### **Request**
| Attribute     | Type        | Mandatory | Description |
| -----------   | ----------- |---------- | ----------- |
| dateStart     | string      | Yes       | Start date of consulting  in ```"yyyy-mm-dd"``` format  |
| dateEnd       | string      | Yes       | End date of consulting  in ```"yyyy-mm-dd"``` format    |
| page          | number      | Yes       | Page Number                                             |
| pageSize      | number      | Yes       | Number of items per page                                |

<br />

```bash
curl --request POST \
  --url https://example.myvtex.com/_v/financial-commission/sellerId1/invoices \
  --header 'Authorization: Bearer 123456' \
  --header 'Content-Type: application/json' \
  --data '{
	"startDate": "2022-06-17",
	"endDate": "2022-06-17",
	"page": 1,
	"pageSize": 10
}'
```
<br />

```json
{
	"startDate": "2022-06-17",
	"endDate": "2022-06-17",
	"page": 1,
	"pageSize": 10
}
```

<br />

#### **Response** 

| Attribute                   | Type        | Description                                             |
| ----------------------------| ----------- |-------------------------------------------------------- |
| data                        | object      | Array object to order invoice detail                    |
| id                          | string      | Invoice Id                                              |
| status                      | string      | Invoice status                                          |
| invoiceCreatedDate          | string      | Invoice creation date                                   |
| totalizers                  | object      | Totalizer object                                        |
| subTotal                    | string      |                                                         |
| fee                         | string      |                                                         |
| total                       | object      | Total value                                             |
| pagination                  | object      | Paging details object                                   |
| total                       | number      | Total number of items                                   |
| page                        | number      | Current page                                            |
| pageSize                    | number      | Paging total per Page                                   |

<br />

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`

```json
{
	"data": [
		{
			"id": "sellerId1_2ca6e388933d",
			"status": "unpaid",
			"invoiceCreatedDate": "2022-06-17",
			"totalizers": {
				"subTotal": 6.37,
				"fee": 0,
				"total": 6.37
			}
		}
	],
	"pagination": {
		"page": 1,
		"pageSize": 10,
		"total": 1
	}
}

```
<br />
__________________________________________________

# Single Invoice

<br />

## Get Invoice

![](https://img.shields.io/static/v1?label=&message=GET&color=blue) `https://{{accountmarketplace}}.myvtex.com/_v/private/financial-commission/{{sellerId}}/invoice/{{invoiceId}}`

Retrieve a single invoice.

<br />

#### **Authorization**
> **Type** ```Bearer Token```

| Attribute | Type        | Mandatory | Description |
| ----------| ----------- |---------- | ----------- |
| Token     | string      | Yes       |The token configured by the marketplace in financial commission             |


<br />

#### **Path parameters**

| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| accountmarketplace      | string      | Yes       | Name of the VTEX account of the marketplace.             |
| sellerId                | string      | Yes       | Seller Id                                                |
| invoiceId               | string      | Yes       | InvoiceId                                                |  

<br />

```bash
curl --request GET \
  --url https://example.myvtex.com/_v/private/financial-commission/sellerId1/invoice/sellerId1_2ca6e388933d \
  --header 'Authorization: Bearer 123456'
```
<br />

#### **Response** 

| Attribute                   | Type        | Description                                             |
| ----------------------------| ----------- |-------------------------------------------------------- |
| id                          | string      | Invoice Id                                              |
| status                      | string      | Invoice status                                          |
| invoiceCreatedDate          | string      | Invoice creation date                                   |
| seller                      | object      | Seller Detail                                           |
| name                        | string      | Seller name                                             |
| contact                     | object      | Seller's contact information                            |
| phone                       | string      | Phone number                                            |
| orders                      | object      | Array order invoice                                     |
| orderId                     | string      | Order Id marketplace                                    |
| sellerOrderId               | string      | Order Id of seller                                      |
| totalComission              | number      | Commission on payment value                             |
| totalOrderValue             | number      | Payment total value                                     |
| totalDiscounts              | number      | Discounts value                                         |
| totalOrdersItems            | number      | Value of items net of payment                           |
| totalShipping               | number      | Shipping value                                          |
| totalTax                    | number      | Tax value                                               |
| totalOrderRate              | number      | Rate value                                              |
| totalizers                  | object      | Totalizer object                                        |
| subTotal                    | number      | Subtotal value of the order's invoice                   |
| fee                         | number      |                                                         |
| total                       | number      | Total value of the order's invoice                      |

<br />

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`

```json
{
	"id": "sellerId1_2ca6e388933d",
	"status": "unpaid",
	"invoiceCreatedDate": "2022-06-17",
	"seller": {
		"name": "sellerName",
		"contact": {
			"phone": "123456798"
		}
	},
	"orders": [
		{
			"orderId": "123456798-01",
			"sellerOrderId": "GCB-123456798-01",
			"totalComission": 4.12,
			"totalOrderValue": 38.5,
			"totalDiscounts": 0,
			"totalOrdersItems": 24,
			"totalShipping": 14.5,
			"totalTax": 0,
			"totalOrderRate": null
		},
		{
			...
		}
	],
	"totalizers": {
		"subTotal": 6.37,
		"fee": 0,
		"total": 6.37
	}
}

```
<br />
__________________________________________________

<br />

## Create Invoice

![](https://img.shields.io/static/v1?label=&message=POST&color=brightgreen) `https://{{accountmarketplace}}.myvtex.com/_v/private/financial-commission/{{sellerId}}/invoice/{{invoiceId}}`

Create a single invoice.

<br />

#### **Authorization**
> **Type** ```Bearer Token```

| Attribute | Type        | Mandatory | Description |
| ----------| ----------- |---------- | ----------- |
| Token     | string      | Yes       |The token configured by the marketplace in financial commission             |


<br />

#### **Path parameters**

| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| accountmarketplace      | string      | Yes       | Name of the VTEX account of the marketplace.             |
| sellerId                | string      | Yes       | Seller Id                                                |
| invoiceId               | string      | Yes       | InvoiceId                                                |  

<br />

#### **Request**
| Attribute     | Type        | Mandatory | Description |
| -----------   | ----------- |---------- | ----------- |
| startDate     | string      | Yes       | Start date of order invoice in VTEX in ```"yyyy-mm-dd"``` format  |
| endDate       | string      | Yes       | End date of order invoice in VTEX in ```"yyyy-mm-dd"``` format    |

<br />

```json
{
	"startDate": "2022-06-17",
	"endDate": "2022-06-17",
}
```

<br />


```bash
curl --request POST \
  --url https://example.myvtex.com/_v/private/financial-commission/sellerId1/invoice/sellerId1_2ca6e388933d \
  --header 'Authorization: Bearer 123456' \
  --header 'Content-Type: application/json' \
  --data '{
	"startDate":"2022-05-01",
	"endDate":"2022-05-30"
}'
```
<br />

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`

```shell
Invoice sellerId1_2ca6e388933d created

```
<br />
__________________________________________________

<br />

## Update Invoice

![](https://img.shields.io/static/v1?label=&message=PATCH&color=orange) `https://{{accountmarketplace}}.myvtex.com/_v/private/financial-commission/{{sellerId}}/invoice/{{invoiceId}}`

Update a single invoice.

<br />

#### **Authorization**
> **Type** ```Bearer Token```

| Attribute | Type        | Mandatory | Description |
| ----------| ----------- |---------- | ----------- |
| Token     | string      | Yes       |The token configured by the marketplace in financial commission             |


<br />

#### **Path parameters**

| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| accountmarketplace      | string      | Yes       | Name of the VTEX account of the marketplace.             |
| sellerId                | string      | Yes       | Seller Id                                                |
| invoiceId               | string      | Yes       | InvoiceId                                                |  

<br />

#### **Request** 

| Attribute                   | Type        | Description                                             |
| ----------------------------| ----------- |-------------------------------------------------------- |
| status                      | string      | Invoice status                                          |
| invoiceCreatedDate          | string      | Invoice creation date                                   |
| seller                      | object      | Seller Detail                                           |
| name                        | string      | Seller name                                             |
| contact                     | object      | Seller's contact information                            |
| phone                       | string      | Phone number                                            |
| orders                      | object      | Array order invoice                                     |
| orderId                     | string      | Order Id marketplace                                    |
| sellerOrderId               | string      | Order Id of seller                                      |
| totalComission              | number      | Commission on payment value                             |
| totalOrderValue             | number      | Payment total value                                     |
| totalDiscounts              | number      | Discounts value                                         |
| totalOrdersItems            | number      | Value of items net of payment                           |
| totalShipping               | number      | Shipping value                                          |
| totalTax                    | number      | Tax value                                               |
| totalOrderRate              | number      | Rate value                                              |
| totalizers                  | object      | Totalizer object                                        |
| subTotal                    | number      | Subtotal value of the order's invoice                   |
| fee                         | number      |                                                         |
| total                       | number      | Total value of the order's invoice                      |

<br />

```json
{
	"status": "unpaid",
	"invoiceCreatedDate": "2022-06-17",
	"seller": {
			"name": "SellerName",
			"contact": {
				"phone": "123456798"
			}
		},
	"orders": [
			{
				"orderId": "12345789-01",
				"sellerOrderId": "GCB-12345789-01",
				"totalComission": 4.12,
				"totalOrderValue": 38.5,
				"totalDiscounts": 0,
				"totalOrdersItems": 24,
				"totalShipping": 14.5,
				"totalTax": 0,
				"totalOrderRate": null
			},
			{
				....
			}
		],
		"totalizers": {
			"subTotal": 6.37,
			"fee": 0,
			"total": 6.37
		}
}
```

<br />


```bash
curl --request POST \
  --url https://example.myvtex.com/_v/private/financial-commission/sellerId1/invoice/sellerId1_2ca6e388933d \
  --header 'Authorization: Bearer 123456' \
  --header 'Content-Type: application/json' \
  --data '{
	"status": "unpaid",
	"invoiceCreatedDate": "2022-06-17",
	"seller": {
			"name": "SellerName",
			"contact": {
				"phone": "123456798"
			}
		},
	"orders": [
			{
				"orderId": "123456789-01",
				"sellerOrderId": "GCB-123456789-01",
				"totalComission": 4.12,
				"totalOrderValue": 38.5,
				"totalDiscounts": 0,
				"totalOrdersItems": 24,
				"totalShipping": 14.5,
				"totalTax": 0,
				"totalOrderRate": null
			}
		],
		"totalizers": {
			"subTotal": 6.37,
			"fee": 0,
			"total": 6.37
		}
}'
```
<br />

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`

```shell
Invoice sellerId1_2ca6e388933d updated

```
<br />
__________________________________________________

## Delete Invoice

![](https://img.shields.io/static/v1?label=&message=DELETE&color=red) `https://{{accountmarketplace}}.myvtex.com/_v/private/financial-commission/{{sellerId}}/invoice/{{invoiceId}}`

Delete a single invoice.

<br />

#### **Authorization**
> **Type** ```Bearer Token```

| Attribute | Type        | Mandatory | Description |
| ----------| ----------- |---------- | ----------- |
| Token     | string      | Yes       |The token configured by the marketplace in financial commission             |


<br />

#### **Path parameters**

| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| accountmarketplace      | string      | Yes       | Name of the VTEX account of the marketplace.             |
| sellerId                | string      | Yes       | Seller Id                                                |
| invoiceId               | string      | Yes       | InvoiceId                                                |  

<br />

```bash
curl --request POST \
  --url https://example.myvtex.com/_v/private/financial-commission/sellerId1/invoice/sellerId1_2ca6e388933d \
    --header 'Authorization: Bearer 132456'
```
<br />

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`

```shell
Invoice sellerId1_2ca6e388933d  deleted

```
<br />
__________________________________________________

# Email & Template

## GetTemplate

![](https://img.shields.io/static/v1?label=&message=GET&color=blue) `https://{{accountmarketplace}}.myvtex.com/_v/segment/template`

Retrieve template email.

<br />

#### **Path parameters**

| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| accountmarketplace      | string      | Yes       | Name of the VTEX account of the marketplace.             |

<br />

```bash
curl --request GET \
  --url https://example.myvtex.com/_v/segment/template
```
<br />

#### **Response** 

```Message``` field contains the html template used in the mailing.

<br />

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`

```json
{
	"template": {
		"Name": "invoice-detail",
		"FriendlyName": "Invoice Detail",
		"Description": "Templeate used for invoice detail",
		"IsDefaultTemplate": false,
		"AccountId": null,
		"AccountName": null,
		"ApplicationId": null,
		"IsPersisted": true,
		"IsRemoved": false,
		"Type": "",
		"Templates": {
			"email": {
				"To": "{{message.to}}",
				"CC": null,
				"BCC": null,
				"Subject": "Invoice Detail",
				"Message": "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional //EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\r\n<html>\r\n  <head>\r\n    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />\r\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\" />\r\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\r\n    <title>{{_accountInfo.TradingName}}</title>\r\n  </head>\r\n  <body style=\"background-color: #f1f1f1 !important\">\r\n    <center>\r\n      <table\r\n        style=\"\r\n          border-bottom-color: #e7e9ee !important;\r\n          border-bottom-style: solid !important;\r\n          border-bottom-width: 2px !important;\r\n          font-family: Helvetica, Arial, sans-serif !important;\r\n          line-height: 150% !important;\r\n          margin: 0px !important;\r\n          min-width: 800px;\r\n          background-color: #fff !important;\r\n        \"\r\n        align=\"center\"\r\n        border=\"0\"\r\n        cellpading=\"0\"\r\n        cellspacing=\"0\"\r\n        width=\"800\"\r\n      >\r\n        <tbody\r\n          style=\"\r\n            background-color: #fff !important;\r\n            font-family: Helvetica, Arial, sans-serif !important;\r\n            line-height: 150% !important;\r\n            margin: 0px !important;\r\n            min-width: 600px !important;\r\n          \"\r\n        >\r\n          <tr\r\n            style=\"\r\n              font-family: Helvetica, Arial, sans-serif !important;\r\n              line-height: 150% !important;\r\n              margin: 0px !important;\r\n            \"\r\n          >\r\n            <td\r\n              style=\"\r\n                font-family: Helvetica, Arial, sans-serif !important;\r\n                line-height: 150% !important;\r\n                margin: 0px !important;\r\n                padding: 22px 30px;\r\n              \"\r\n            >\r\n              <a href=\"https://vtex.com\" style=\"color: #f71963; fill: #f71963\"\r\n                ><img\r\n                  alt\r\n                  border=\"0\"\r\n                  width=\"auto\"\r\n                  src=\"http://licensemanager.vtex.com.br/api/site/pub/accounts/e39d05f9-0c54-4469-a626-8bb5cff169f8/logos/show\"\r\n                  style=\"\r\n                    vertical-align: top;\r\n                    outline: none;\r\n                    text-decoration: none;\r\n                    -ms-interpolation-mode: bicubic;\r\n                    max-width: 100%;\r\n                    border: none;\r\n                    width: 15% !important;\r\n                  \"\r\n              /></a>\r\n            </td>\r\n            <td\r\n              align=\"right\"\r\n              valign=\"center\"\r\n              style=\"\r\n                font-family: Helvetica, Arial, sans-serif !important;\r\n                line-height: 150% !important;\r\n                margin: 0px !important;\r\n                padding: 22px 30px;\r\n              \"\r\n            >\r\n              <h2 style=\"color: #717786; font-size: 16px !important\">\r\n                Invoice Detail\r\n              </h2>\r\n              <p style=\"color: #717786; font-size: 12px !important\">\r\n                Invoice: {{id}}<br />Date: {{invoiceCreatedDate}}\r\n              </p>\r\n            </td>\r\n          </tr>\r\n        </tbody>\r\n      </table>\r\n      <table\r\n        style=\"\r\n          font-family: Helvetica, Arial, sans-serif !important;\r\n          line-height: 150% !important;\r\n          border-bottom-color: #e7e9ee !important;\r\n          border-bottom-style: solid !important;\r\n          border-bottom-width: 2px !important;\r\n          margin: 0px !important;\r\n        \"\r\n        align=\"center\"\r\n        border=\"0\"\r\n        cellpading=\"0\"\r\n        cellspacing=\"0\"\r\n        width=\"800\"\r\n      >\r\n        <tbody\r\n          style=\"\r\n            font-family: Helvetica, Arial, sans-serif !important;\r\n            line-height: 150% !important;\r\n            margin: 0px !important;\r\n          \"\r\n        >\r\n          <tr\r\n            style=\"\r\n              background-color: #fff !important;\r\n              font-family: Helvetica, Arial, sans-serif !important;\r\n              line-height: 150% !important;\r\n              margin: 0px !important;\r\n            \"\r\n          >\r\n            <td\r\n              style=\"\r\n                font-family: Helvetica, Arial, sans-serif !important;\r\n                line-height: 150% !important;\r\n                margin: 0px !important;\r\n                padding: 52px 30px 20px;\r\n                width: 50% !important;\r\n              \"\r\n            >\r\n              <p>\r\n                E-mail: {{seller.contact.email}}<br />\r\n                Phone: {{seller.contact.phone}}\r\n              </p>\r\n            </td>\r\n            <td\r\n              style=\"\r\n                font-family: Helvetica, Arial, sans-serif !important;\r\n                line-height: 150% !important;\r\n                margin: 0px !important;\r\n                padding: 15px 80px 20px 180px;\r\n                width: 50%;\r\n                text-align: end !important;\r\n              \"\r\n            >\r\n              <p><span>To:</span><br />{{seller.name}}<br /></p>\r\n            </td>\r\n          </tr>\r\n        </tbody>\r\n      </table>\r\n      <table\r\n        style=\"\r\n          font-family: Helvetica, Arial, sans-serif !important;\r\n          line-height: 150% !important;\r\n          margin: 0px !important;\r\n        \"\r\n        align=\"center\"\r\n        border=\"0\"\r\n        cellpading=\"0\"\r\n        cellspacing=\"0\"\r\n        width=\"800\"\r\n      >\r\n        <tbody\r\n          style=\"\r\n            font-family: Helvetica, Arial, sans-serif !important;\r\n            line-height: 150% !important;\r\n            margin: 0px !important;\r\n          \"\r\n        >\r\n          <tr\r\n            style=\"\r\n              background-color: #fff !important;\r\n              font-family: Helvetica, Arial, sans-serif !important;\r\n              line-height: 150% !important;\r\n              margin: 0px !important;\r\n            \"\r\n          >\r\n            <td\r\n              style=\"\r\n                font-family: Helvetica, Arial, sans-serif !important;\r\n                line-height: 150% !important;\r\n                margin: 0px !important;\r\n                padding: 20px 30px 64px;\r\n              \"\r\n              align=\"center\"\r\n            >\r\n              <p>\r\n                <b><span>Comments or special instructions:</span></b>\r\n                <br />{{comment}}\r\n              </p>\r\n            </td>\r\n          </tr>\r\n        </tbody>\r\n      </table>\r\n      <table\r\n        style=\"\r\n          font-family: Helvetica, Arial, sans-serif !important;\r\n          line-height: 150% !important;\r\n          border-bottom-color: #e7e9ee !important;\r\n          border-bottom-style: solid !important;\r\n          border-bottom-width: 2px !important;\r\n          margin: 0px !important;\r\n        \"\r\n        align=\"center\"\r\n        border=\"0\"\r\n        cellpading=\"0\"\r\n        cellspacing=\"0\"\r\n        width=\"800\"\r\n      >\r\n        <tbody\r\n          style=\"\r\n            font-family: Helvetica, Arial, sans-serif !important;\r\n            line-height: 150% !important;\r\n            margin: 0px !important;\r\n          \"\r\n        >\r\n          <tr\r\n            style=\"\r\n              background-color: #fff !important;\r\n              font-family: Helvetica, Arial, sans-serif !important;\r\n              line-height: 150% !important;\r\n              margin: 0px !important;\r\n            \"\r\n          >\r\n            <th style=\"font-size: 14px; width: 25% !important\">ID</th>\r\n            <th style=\"font-size: 14px; width: 25% !important\">TOTAL</th>\r\n            <th style=\"font-size: 14px; width: 25% !important\">COMMISSION</th>\r\n          </tr>\r\n          {{#each orders}}\r\n          <tr>\r\n            <td\r\n              style=\"\r\n                text-align: center;\r\n                background-color: #fff;\r\n                padding-bottom: 10px !important;\r\n              \"\r\n            >\r\n              {{this.sellerOrderId}}\r\n            </td>\r\n            <td\r\n              style=\"\r\n                text-align: center;\r\n                background-color: #fff;\r\n                padding-bottom:10px !important;\r\n              \"\r\n            >\r\n              {{this.totalOrderValue}}\r\n            </td>\r\n            <td\r\n              style=\"\r\n                text-align: center;\r\n                background-color: #fff;\r\n                padding-bottom: 10px !important;\r\n              \"\r\n            >\r\n              ${{this.totalComission}}\r\n            </td>\r\n          </tr>\r\n          {{/each}}\r\n        </tbody>\r\n      </table>\r\n      <table\r\n        style=\"\r\n          font-family: Helvetica, Arial, sans-serif !important;\r\n          line-height: 150% !important;\r\n          border-bottom-color: #e7e9ee !important;\r\n          border-bottom-style: solid !important;\r\n          border-bottom-width: 2px !important;\r\n          margin: 0px !important;\r\n        \"\r\n        align=\"center\"\r\n        border=\"0\"\r\n        cellpading=\"0\"\r\n        cellspacing=\"0\"\r\n        width=\"800\"\r\n      >\r\n        <tbody\r\n          style=\"\r\n            font-family: Helvetica, Arial, sans-serif !important;\r\n            line-height: 150% !important;\r\n            margin: 0px !important;\r\n          \"\r\n        >\r\n          <tr\r\n            style=\"\r\n              background-color: #fff !important;\r\n              font-family: Helvetica, Arial, sans-serif !important;\r\n              line-height: 150% !important;\r\n              margin: 0px !important;\r\n            \"\r\n          >\r\n            <th style=\"width: 25% padding-top: 40px !important;\"></th>\r\n            <th\r\n              style=\"\r\n                font-size: 14px;\r\n                width: 25%;\r\n                text-align: initial;\r\n                padding-top: 40px !important;\r\n              \"\r\n            >\r\n              SUBTOTAL:\r\n            </th>\r\n            <td\r\n              style=\"width: 25%; text-align: end; padding-top: 40px !important\"\r\n            >\r\n              {{totalizers.subtotal}}\r\n            </td>\r\n            <th style=\"width: 25%; padding-top: 40px !important\"></th>\r\n          </tr>\r\n          <tr\r\n            style=\"\r\n              background-color: #fff !important;\r\n              font-family: Helvetica, Arial, sans-serif !important;\r\n              line-height: 150% !important;\r\n              margin: 0px !important;\r\n            \"\r\n          >\r\n            <th style=\"width: 25%\"></th>\r\n            <th\r\n              style=\"\r\n                font-size: 14px;\r\n                width: 25%;\r\n                text-align: initial !important;\r\n              \"\r\n            >\r\n              SERVICE FEE:\r\n            </th>\r\n            <td style=\"width: 25%; text-align: end !important\">\r\n              ${{totalizers.fee}}\r\n            </td>\r\n            <th style=\"width: 25%\"></th>\r\n          </tr>\r\n          <tr\r\n            style=\"\r\n              background-color: #fff !important;\r\n              font-family: Helvetica, Arial, sans-serif !important;\r\n              line-height: 150% !important;\r\n              margin: 0px !important;\r\n            \"\r\n          >\r\n            <th style=\"width: 25%; padding-bottom: 40px !important\"></th>\r\n            <th\r\n              style=\"\r\n                font-size: 14px;\r\n                width: 25%;\r\n                text-align: initial;\r\n                padding-bottom: 40px !important;\r\n              \"\r\n            >\r\n              TOTAL DUE:\r\n            </th>\r\n            <td\r\n              style=\"\r\n                width: 25%;\r\n                text-align: end;\r\n                padding-bottom: 40px !important;\r\n              \"\r\n            >\r\n              ${{totalizers.total}}\r\n            </td>\r\n            <th style=\"width: 25%; padding-bottom: 40px !important\"></th>\r\n          </tr>\r\n        </tbody>\r\n      </table>\r\n      <table\r\n        style=\"\r\n          font-family: Helvetica, Arial, sans-serif !important;\r\n          line-height: 150% !important;\r\n          margin: 0px !important;\r\n        \"\r\n        align=\"center\"\r\n        border=\"0\"\r\n        cellpading=\"0\"\r\n        cellspacing=\"0\"\r\n        width=\"800\"\r\n      >\r\n        <tbody\r\n          style=\"\r\n            font-family: Helvetica, Arial, sans-serif !important;\r\n            line-height: 150% !important;\r\n            margin: 0px !important;\r\n          \"\r\n        >\r\n          <tr\r\n            style=\"\r\n              background-color: #fff !important;\r\n              font-family: Helvetica, Arial, sans-serif !important;\r\n              line-height: 150% !important;\r\n              margin: 0px !important;\r\n            \"\r\n          >\r\n            <td\r\n              style=\"\r\n                font-family: Helvetica, Arial, sans-serif !important;\r\n                line-height: 150% !important;\r\n                margin: 0px !important;\r\n                padding: 30px 30px 24px;\r\n              \"\r\n              align=\"left\"\r\n            >\r\n              <p>\r\n                <b>Thanks you for your business!</b>\r\n              </p>\r\n            </td>\r\n          </tr>\r\n        </tbody>\r\n      </table>\r\n    </center>\r\n  </body>\r\n</html>\r\n",
				"Type": "E",
				"ProviderId": "336932c2-1ea6-4e30-8d59-3359b0aca076",
				"ProviderName": null,
				"IsActive": true,
				"withError": false
			},
			"sms": {
				"Type": "S",
				"ProviderId": null,
				"ProviderName": null,
				"IsActive": false,
				"withError": false,
				"Parameters": [
					{
						"Name": "Destination",
						"Value": "Destination"
					},
					{
						"Name": "MessageText",
						"Value": "MessageText"
					}
				]
			}
		}
	}
}

```
<br />
__________________________________________________

## Send Email

![](https://img.shields.io/static/v1?label=&message=POST&color=blue) `https://{{accountmarketplace}}.myvtex.com/_v/mail`

Send email.

<br />

#### **Path parameters**

| Attribute               | Type        | Mandatory | Description |
| ----------------------- | ----------- |---------- | ----------- |
| accountmarketplace      | string      | Yes       | Name of the VTEX account of the marketplace.             |

<br />

#### **Request**
| Attribute     | Type        | Mandatory | Description |
| -----------   | ----------- |---------- | ----------- |
| email         | string      | Yes       | Mail of the recipient to send. |
| jsonData      | string      | Yes       | Contains the json in string format of the invoiced data to be sent in the email according to the parameterized template.    |

```bash
curl --request POST \
  --url https://example.myvtex.com/_v/mail \
  --header 'Content-Type: application/json' \
  --data '{
	"email": "destinataio@example.com",
	"jsonData": "{\"id\":\"sellerId1_ebf209071ae7\",\"status\":\"unpaid\",\"invoiceCreatedDate\":\"2022-06-14\",\"seller\":{\"name\":\"sellerName\",\"id\":\"sellerId1\",\"contact\":{\"phone\":null}},\"orders\":[{\"orderId\":\"123456-01\",\"sellerOrderId\":\"GCB-123456-01\",\"totalComission\":0,\"totalOrderValue\":522.5,\"totalDiscounts\":0,\"totalOrdersItems\":522.5,\"totalShipping\":0,\"totalTax\":0,\"totalOrderRate\":null}],\"totalizers\":{\"subTotal\":0,\"fee\":0,\"total\":0},\"comment\":\"Invoicemanuallycreatedon2022-06-14\"}"
}'
```
<br />

```json
{
	"email": "destinataio@example.com",
	"jsonData": "{\"id\":\"sellerId1_ebf209071ae7\",\"status\":\"unpaid\",\"invoiceCreatedDate\":\"2022-06-14\",\"seller\":{\"name\":\"sellerName\",\"id\":\"sellerId1\",\"contact\":{\"phone\":null}},\"orders\":[{\"orderId\":\"123456-01\",\"sellerOrderId\":\"GCB-123456-01\",\"totalComission\":0,\"totalOrderValue\":522.5,\"totalDiscounts\":0,\"totalOrdersItems\":522.5,\"totalShipping\":0,\"totalTax\":0,\"totalOrderRate\":null}],\"totalizers\":{\"subTotal\":0,\"fee\":0,\"total\":0},\"comment\":\"Invoicemanuallycreatedon2022-06-14\"}"
}
```

<br />

#### **Response** 

<br />

![](https://img.shields.io/static/v1?label=&message=200&color=green) `OK`

```shell
ok

```
<br />
__________________________________________________