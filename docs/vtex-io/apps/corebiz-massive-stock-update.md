---
title: "MASSIVE STOCK UPDATE"
slug: "corebiz-massive-stock-update"
excerpt: "corebiz.massive-stock-update@0.1.4"
hidden: true
createdAt: "2022-08-03T18:33:58.031Z"
updatedAt: "2022-08-08T15:44:54.035Z"
---
This application exposes an endpoint of massive stock update

---

```shell
PUT https://{{workspace}}--{{accountName}}.myvtex.com/_v/massive/stock/update

```

## Curl

```shell
curl --location --request PUT 'https://{{workspace}}--{{accountName}}.myvtex.com/_v/massive/stock/update' \
--header 'VtexIdClientAutCookie: "" \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "sku": 1,
        "warehouseId": 1,
        "quantity": 1,
        "unlimitedQuantity": false,
        "dateUtcOnBalanceSystem": null
    }
]'
```

## Specification

### Headers

- Required
  - Accept : application/json
  - Content-Type : application/json; charset=utf-8
  - VtexIdclientAutCookie : `eyJhbGciOi...`

### Path params

- Required
  - sku [int32]
  - warehouseId [int32] || [string]
  - quantity [int32]
  - unlimitedQuantity [boolean]
  - dateUtcOnBalanceSystem [string]

> Read the API information for more information [link](https://developers.vtex.com/vtex-rest-api/reference/inventory#updateinventorybyskuandwarehouse)

### Request body example

```json
[
  {
    "sku": 1,
    "warehouseId": 123,
    "quantity": 50,
    "unlimitedQuantity": false,
    "dateUtcOnBalanceSystem": null
  }
]
```

### Success Response body example

```json
{
  "successfulResponses": {
    "elements": [
      {
        "sku": 1,
        "success": true,
        "warehouseId": 123,
        "quantity": 50,
        "unlimitedQuantity": false,
        "dateUtcOnBalanceSystem": null
      }
    ],
    "quantity": 1
  },
  "failedResponses": {
    "elements": [],
    "quantity": 0
  },
  "total": 1
}
```

### Error Response body example

```json
{
  "failedResponses": {
    "elements": [
      [
        {
          "sku": 159076,
          "quantity": 12,
          "dateUtcOnBalanceSystem": null,
          "success": "false",
          "error": 400,
          "errorMessage": "The request is invalid: The 'warehouseId' field is required."
        }
      ]
    ],
    "quantity": 1
  }
}
```

---

## Credentials

### What Header to use?

You can use the following headers:

- X-VTEX-API-AppKey
- X-VTEX-API-AppToken

Or

- VtexIdClientAutCookie

### Create appKey y appToken

To generate app keys in your account, you should follow the instructions seen in the [Application Keys](https://help.vtex.com/en/tutorial/application-keys--2iffYzlvvz4BDMr6WGUtet) article in our Help Center.

### Create role

[Create a role](https://help.vtex.com/en/tutorial/perfiles-de-acceso--7HKK5Uau2H6wxE1rH5oRbc) with the following resources and add your user to that role

- Logistics / Logistics access / Logistics full access

### Convert to JWT

Make a call with the credentials created. The result, if the credentials are valid, will return a token that will be used as the value in the header 'VtexIdclientAutCookie' requested by the massive-stock-update component.

```shell
>>>>>>> 91953ff0fc5154ad45335f9f2a8dbc6141fadf81
curl --location --request POST 'https://vtexid.vtexcommercestable.com.br/api/vtexid/apptoken/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "appkey": "...",
    "apptoken": "..."
}'
```

## Testing with bash script

In the tests directory you can find the following sample scripts to compare performance between component execution versus parallel calls to the Logistic API.

- api-logistic-inventory-test.sh
- massive-stock-update-test.sh
- update-parallel-api-logistic.sh

## Flow

![Massive stock update flow](https://user-images.githubusercontent.com/33711188/132750831-38272a4d-5abb-446b-ac1b-574969cb8561.png)

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/GuidoSdo"><img src="https://avatars.githubusercontent.com/u/33711188?v=4" width="100px;" alt=""/><br /><sub><b>Guido Salcedo</b></sub></a><br /><a href="https://github.com/vtex-apps/massive-stock-update" title="Code">💻</a></td>

   <td align="center"><a href="https://github.com/lucasdellasala"><img src="https://avatars.githubusercontent.com/u/55720621?v=4" width="100px;" alt=""/><br /><sub><b>Lucas Della Sala</b></sub></a><br /><a href="https://github.com/vtex-apps/massive-stock-update" title="Code">💻</a></td>
  </tr>
  
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!