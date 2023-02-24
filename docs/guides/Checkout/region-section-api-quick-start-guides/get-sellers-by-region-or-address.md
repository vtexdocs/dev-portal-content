---
title: "Get sellers by region or address"
slug: "get-sellers-by-region-or-address"
hidden: false
createdAt: ""
updatedAt: ""
---
When customers access your store, they expect to view products that can be delivered to their location. To guarantee item availability in the window display, the VTEX platform selects the sellers linked to the [marketplace](https://help.vtex.com/en/tutorial/marketplace).

This guide will describe how to obtain a list of [White label sellers](https://help.vtex.com/en/tutorial/white-label-sellers-selection) in your store serving a given delivery region or address.

>⚠️ The sellers shown in the list are only a reference of those that would be able to attend an order placed to a delivery location. From this filter, only sellers with stock and delivery methods available to that specific address will be shown to the customer in the store and considered able to fulfill the order.

## Accessing the list of sellers

To access the list of sellers serving a specific region or address, you need to use the [Get sellers by region or address](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/regions/-regionId-) endpoint. In this request, you must __choose one__ of the following methods:

1. Send the identification of the list of sellers (`regionId`) through the URL address.

> `https://{accountName}.{environment}.com.br/api/checkout/pub/regions/v2.1DC18HE648C5111C0933734FE83EC783`

2. Send the `country` (3-digit ISO code) and at least one of the two values ​​(`postal Code` or `geoCoordinates`) as query parameters through the URL. If you wish, you can send both values (`postalCode` or `geoCoordinates`) ​​in the same request.

> `https://{accountName}.{environment}.com.br/api/checkout/pub/regions?country=BRA&postalCode=22050040`

After sending the request, the endpoint will return the response body containing the `regionId`, `id` and `name` of stores able to deliver in the selected address region, as shown in the example below:

```json
[
    {
        "id": "v2.1DC18HE648C5111C0933734DD83ED783",
        "sellers": [
            {
                "id": "partnerchallenge9",
                "name": "partnerchallenge9",
                "logo": ""
            },
            {
                "id": "qastorees",
                "name": "qastorees",
                "logo": ""
            },
            {
                "id": "qastoremg",
                "name": "qastoremg",
                "logo": ""
            },
            {
                "id": "qastorerj",
                "name": "qastorerj",
                "logo": ""
            },
            {
                "id": "qastoresp",
                "name": "qastoresp",
                "logo": ""
            }
        ]
    }
]
```

## Error codes

The following errors may appear as a message in the response body.

### 200 - OK

Despite the code `200` (which indicates the success of the request), if there are no White label sellers allocated in the `regionId` informed, the response body will not contain any seller information.

```json
[
    {
        "id": "v2.1BB18CE648B5111D0933734ED83EC783",
        "sellers": []
    }
]
```

### 400 - Bad Request

- `Message error example (code 001): "O campo CEP (220500) nos dados de entrega é inválido" (Postal code (220500) in delivery data is invalid)`. The `postalCode` information is not valid.

```json
{
    "fields": {},
    "error": {
        "code": "001",
        "message": "O campo CEP (220500) nos dados de entrega é inválido",
        "exception": null
    },
    "operationId": "f2b8107f-e5d5-4b7c-b719-344d1b05d1fa"
}
```

- `Message error example (code CHK0119): "Endereços devem ter código postal ou geocoordenadas" (Addresses must have postal code or geocoordinates)`. This message can be displayed in two situations: 
      - 1) `postalCode` was not informed in the request, or;
      - 2) `geoCoordinates` information is not valid or was not informed in the request.

```json
{
    "fields": {},
    "error": {
        "code": "CHK0119",
        "message": "Endereços devem ter código postal ou geocoordenadas",
        "exception": null
    },
    "operationId": "e144a38c-2e7c-40fa-bd71-12d0ceaa2517"
}
```

- `Message error example (code CHK0127): "País inválido" (invalid country)`. The `country` code was not informed in the request.

```json
{
    "fields": {},
    "error": {
        "code": "CHK0127",
        "message": "País inválido",
        "exception": null
    },
    "operationId": "d0119920-aa3e-4295-a063-6d85ba34a400"
}
```