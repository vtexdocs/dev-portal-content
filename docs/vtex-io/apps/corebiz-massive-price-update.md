---
title: "MASSIVE PRICE UPDATE"
slug: "corebiz-massive-price-update"
excerpt: "corebiz.massive-price-update@0.1.4"
hidden: true
createdAt: "2022-08-03T19:01:10.525Z"
updatedAt: "2022-08-08T15:43:06.013Z"
---
Massive SKU price update service

```shell

PUT `https://{{workspace}}--{{accountName}}.myvtex.com/_v/massive/price/update`

```

Curl

```shell
curl --location --request PUT 'https://app.io.vtex.com/vtexarg.massive-price-update/v1/{{accountName}}/{{workspace}}/_v/massive/price/update' \
--header 'VtexIdClientAutCookie: "" \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "markup": 30,
        "listPrice": 40,
        "basePrice": 120,
        "itemId": 1,
        "fixedPrices": [
            {
                "tradePolicyId": "1",
                "value": 50.5,
                "listPrice": 50.5,
                "minQuantity": 2,
                "dateRange": {
                    "from": "2021-12-30T22:00:00-03:00",
                    "to": "2021-12-30T23:00:00-03:00"
                }
            }
        ]
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
  - markup [int32]
  - listPrice [int32]
  - basePrice [int32]
  - itemId [int32]
  - costPrice [int32]
  - fixedPrices[]:
    - tradePolicyId [string]
    - value [int32]
    - listPrice [int32]
    - minQuantity [int32]
    - dateRange:
      - from [string]
      - to [string]

> Read API Information to know what combinations of fields to send [link](https://developers.vtex.com/vtex-rest-api/reference/prices-and-fixed-prices#createupdatepriceorfixedprice)

### Request body example

```json
[
  {
    "markup": 30,
    "listPrice": 50,
    "basePrice": 100,
    "itemId": 1,
    "fixedPrices": [
      {
        "tradePolicyId": "1",
        "value": 50.5,
        "listPrice": 50.5,
        "minQuantity": 2,
        "dateRange": {
          "from": "2021-12-30T22:00:00-03:00",
          "to": "2021-12-30T23:00:00-03:00"
        }
      }
    ]
  }
]
```

### Success Response body example

```json
{
  "successfulResponses": {
    "elements": [
      {
        "itemId": 1,
        "success": "true",
        "markup": 30,
        "listPrice": 50,
        "basePrice": 100,
        "fixedPrices": [
          {
            "tradePolicyId": "1",
            "value": 50.5,
            "listPrice": 50.5,
            "minQuantity": 2,
            "dateRange": {
              "from": "2021-12-30T22:00:00-03:00",
              "to": "2021-12-30T23:00:00-03:00"
            }
          }
        ]
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
  "successfulResponses": {
    "elements": [],
    "quantity": 0
  },
  "failedResponses": {
    "elements": [
      {
        "itemId": 1,
        "success": "false",
        "listPrice": 50,
        "basePrice": 100,
        "fixedPrices": [
          {
            "tradePolicyId": "1",
            "value": 50.5,
            "listPrice": 50.5,
            "minQuantity": 2,
            "dateRange": {
              "from": "2021-12-30T22:00:00-03:00",
              "to": "2021-12-30T23:00:00-03:00"
            }
          }
        ],
        "error": 400,
        "errorMessage": "The request is invalid: Item 1 must have exactly two values filled between basePrice, costPrice and markup\n"
      }
    ],
    "quantity": 1
  },
  "total": 1
}
```

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

[Create a role](https://help.vtex.com/en/tracks/accounts-and-permissions--5PxyAgZrtiYlaYZBTlhJ2A/6Ymo5bNMyEYBGsTmbTC3H9?&utm_source=autocomplete) with the Logistics product and associate the resource 'Logistics access'. Finally add the appKey as a user.

### Convert to JWT

Make a call with the credentials created. The result, if the credentials are valid, will return a token that will be used as the value in the header 'VtexIdclientAutCookie' requested by the massive-stock-update component.

```shell
curl --location --request POST 'http://vtexid.vtexcommercestable.com.br/api/vtexid/apptoken/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "appkey": "...",
    "apptoken": "..."
}'
```

## Testing with bash script

In the tests directory you can find the following sample scripts to compare performance between component execution versus parallel calls to the Pricing API.

- api-pricing-test.sh
- massive-price-update.sh
- update-parallel-api-price.sh

## Flow

![Massive price update flow](https://user-images.githubusercontent.com/33711188/132802870-1b6e5c76-2102-4e32-994d-715c8e3d645c.png)

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/GuidoSdo"><img src="https://avatars.githubusercontent.com/u/33711188?v=4" width="100px;" alt=""/><br /><sub><b>Guido Salcedo</b></sub></a><br /><a href="https://github.com/vtex-apps/massive-stock-update" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!