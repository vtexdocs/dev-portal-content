---
title: "Emit Label with App"
slug: "emitlabelwithapp"
excerpt: "This endpoint generates a file that contains one or more labels from the packages sent to the app. This endpoint's response is an url providing access to the generated label file."
hidden: true
createdAt: "2021-01-19T15:35:15.771Z"
updatedAt: "2021-01-19T16:44:17.550Z"
---
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"sender\": {\n        \"cnpj\": \"00000000000000\",\n        \"fantasyName\": null,\n        \"stateRegistration\": null,\n        \"id\": null,\n        \"name\": \"LTDA\",\n        \"address\": {\n            \"postalCode\": \"03475015\",\n            \"country\": {\n                \"code\": \"Brasil\",\n                \"name\": \"Brasil\"\n            },\n            \"subregion1\": {\n                \"code\": \"SP\",\n                \"name\": \"SP\"\n            },\n            \"subregion2\": {\n                \"code\": \"São Paulo\",\n                \"name\": \"São Paulo\"\n            },\n            \"subregion3\": {\n                \"code\": \"Vila Antonieta\",\n                \"name\": \"Vila Antonieta\"\n            },\n            \"street\": \"Rua Exemplo\",\n            \"number\": \"01\",\n            \"complement\": \"\",\n            \"location\": null\n        },\n        \"email\": null,\n        \"phone\": \"+5511111111111\"\n    },\n    \"packages\": [\n        {\n            \"id\": \"6bb4c320-932b-46b6-a628-b61b133052e9\",\n            \"orderId\": \"00-1053722798105-01\",\n            \"items\": [\n                {\n                    \"id\": \"148350\",\n                    \"name\": \"Kit Capacho Geométrico por Marcelo Nunes - 3 Novelos\",\n                    \"quantity\": 1\n                }\n            ],\n            \"dimension\": {\n                \"height\": 20.0,\n                \"length\": 20.0,\n                \"width\": 30.0,\n                \"weight\": 1458.0\n            },\n            \"recipientPostalCode\": \"03681-030\",\n            \"recipient\": {\n                \"cpf\": \"00000000000\",\n                \"id\": null,\n                \"name\": \"Fake Person\",\n                \"address\": {\n                    \"postalCode\": \"00000-000\",\n                    \"country\": {\n                        \"code\": \"BRA\",\n                        \"name\": \"BRA\"\n                    },\n                    \"subregion1\": {\n                        \"code\": \"SP\",\n                        \"name\": \"SP\"\n                    },\n                    \"subregion2\": {\n                        \"code\": \"São Paulo\",\n                        \"name\": \"São Paulo\"\n                    },\n                    \"subregion3\": {\n                        \"code\": \"Burgo Paulista\",\n                        \"name\": \"Burgo Paulista\"\n                    },\n                    \"street\": \"Rua Exemplo\",\n                    \"number\": \"01\",\n                    \"complement\": null,\n                    \"location\": {\n                        \"lat\": -46.48582077026367,\n                        \"lng\": -23.521709442138672\n                    }\n                },\n                \"email\": null,\n                \"phone\": \"+5511111111111\"\n            },\n            \"invoiceData\": {\n                \"number\": \"445494\",\n                \"value\": 6909.0,\n                \"url\": \"\",\n                \"date\": \"2020-08-14T19:43:09.4740645+00:00\",\n                \"invoiceAccessKeys\": [\n                    \"35200844913721000168550010004454941205352231\"\n                ],\n                \"hasIcms\": false,\n                \"hasInsurance\": false\n            },\n            \"trackingData\": {\n                \"number\": \"OM265512653BR\",\n                \"log\": [],\n                \"finished\": false,\n                \"finishedDate\": null\n            },\n            \"origin\": \"Fulfillment\",\n            \"status\": \"invoiced\",\n            \"orderCreationDate\": \"2020-08-11T19:46:40.0305809+00:00\",\n            \"labelIssuedDate\": null,\n            \"shippingEstimate\": \"13bd\",\n            \"shippingEstimateDate\": \"2020-08-31T21:00:00+00:00\",\n            \"shippingData\": {\n                \"shippingPolicyName\": \"VTEXLOG EXAMPLE\",\n                \"shippingPolicyId\": \"vtexlog_policy_id\",\n                \"carrierName\": \"vtexlog\"\n            }\n        }\n    ]\n}",
      "language": "text",
      "name": "Request Example"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n\t\"url\": string\n}",
      "language": "text",
      "name": "Response Example"
    }
  ]
}
[/block]