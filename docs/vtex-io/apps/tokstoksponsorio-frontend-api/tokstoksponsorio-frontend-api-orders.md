---
title: "Orders API"
slug: "tokstoksponsorio-frontend-api-orders"
excerpt: "tokstoksponsorio.frontend-api@0.20.2"
hidden: true
createdAt: "2022-07-18T11:36:17.420Z"
updatedAt: "2022-08-01T14:03:46.913Z"
---
## Middleware for get order delivery availability from TokStok online store

### Route:
- **GET** `/api/io/orders-api/availability/:orderId`

### Response:

``` json
[
	{
		"dataEntrega": "2019-08-26T17:29:53.664Z",
		"ordemSite": 0,
		"periodoEntrega": "string",
		"idCapacidadeEntrega": 0,
		"quantidadeDias": 0
	}
]
```

**Obs.:** `ordemSite` and `quantidadeDias` are not required.

## Middleware for get VTEX order dates from TokStok online store

### Route:
- **GET** `/api/io/orders-api/dates/:orderId`

### Response:

``` json
[
	{
		"dataPrevisaoAtendimento": "2019-10-04T00:00:00",
		"dataPrevisaoEstoque": "2019-08-29T00:00:00",
		"dataProgramacaoEntrega": "2019-10-04T00:00:00",
		"statusPedido": "string"
	}
]
```

**Obs.:** `dataPrevisaoAtendimento`, `dataPrevisaoEstoque`, `dataProgramacaoEntrega` and `statusPedido` can be `null`.

## Middleware to reschedule orders from TokStok online store

### Route:
- **POST** `/api/io/orders-api/update-delivery/:orderId`

### Body:

``` json
{
	"dataEntrega": "2019-08-26T12:30:03.350Z",
	"ordemSite": 0,
	"periodoEntrega": "string",
	"idCapacidadeEntrega": 0,
	"quantidadeDias": 0
}
```