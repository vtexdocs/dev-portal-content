---
title: "Notification"
slug: "notification-1"
hidden: false
createdAt: "2021-04-29T19:54:24.203Z"
updatedAt: "2021-04-29T21:34:19.270Z"
---
Access the [boilerplate repository for the notification app](https://github.com/vtex-apps/carrier-hubs-examples/tree/main/carrier-notifier-example) to clone it and begin development.

A notification app published by a carrier will include an endpoint like this one:
`https://app.io.vtex.com/{app_name}/{app_version}/{account}/{workspace}/notify`

After an order is invoiced, the VTEX notification hub automatically makes a `POST` request to this endpoint with the package’s details. Then the app should respond with the order’s tracking number. See the examples below, and to learn more about this request, access the [notification API request documentation](https://developers.vtex.com/vtex-developer-docs/reference/vtex-log-notification-app).

Request body example:
```json
{
    "email": "email",
    "dispatchOrder": {
        "id": "653560c2-7965-4614-a730-8e45c89bf284",
        "packages": [
            {
                "id": "6bb4c320-932b-46b6-a628-b61b133052e9",
                "orderId": "00-1053722798105-01",
                "items": [
                    {
                        "id": "148350",
                        "name": "Kit Capacho Geométrico por Marcelo Nunes - 3 Novelos",
                        "quantity": 1
                    }
                ],
                "dimension": {
                    "height": 20.0,
                    "length": 20.0,
                    "width": 30.0,
                    "weight": 1458.0
                },
                "recipientPostalCode": "03681-030",
                "recipient": {
                    "cpf": "00000000000",
                    "id": null,
                    "name": "Fake Person",
                    "address": {
                        "postalCode": "00000-000",
                        "country": {
                            "code": "BRA",
                            "name": "BRA"
                        },
                        "subregion1": {
                            "code": "SP",
                            "name": "SP"
                        },
                        "subregion2": {
                            "code": "São Paulo",
                            "name": "São Paulo"
                        },
                        "subregion3": {
                            "code": "Burgo Paulista",
                            "name": "Burgo Paulista"
                        },
                        "street": "Rua Exemplo",
                        "number": "01",
                        "complement": null,
                        "location": {
                            "lat": -46.48582077026367,
                            "lng": -23.521709442138672
                        }
                    },
                    "email": null,
                    "phone": "+5511111111111"
                },
                "invoiceData": {
                    "number": "445494",
                    "value": 6909.0,
                    "url": "",
                    "date": "2020-08-14T19:43:09.4740645+00:00",
                    "invoiceAccessKeys": [
                        "35200844913721000168550010004454941205352231"
                    ],
                    "hasIcms": false,
                    "hasInsurance": false
                },
                "trackingData": {
                    "number": "OM265512653BR",
                    "log": [],
                    "finished": false,
                    "finishedDate": null
                },
                "origin": "Fulfillment",
                "status": "invoiced",
                "orderCreationDate": "2020-08-11T19:46:40.0305809+00:00",
                "labelIssuedDate": null,
                "shippingEstimate": "13bd",
                "shippingEstimateDate": "2020-08-31T21:00:00+00:00",
                "shippingData": {
                    "shippingPolicyName": "VTEXLOG EXAMPLE",
                    "shippingPolicyId": "vtexlog_policy_id",
                    "carrierName": "vtexlog"
                }
            }
        ],
        "sender": {
            "cnpj": "00000000000000",
            "fantasyName": null,
            "stateRegistration": null,
            "id": null,
            "name": "LTDA",
            "address": {
                "postalCode": "03475015",
                "country": {
                    "code": "Brasil",
                    "name": "Brasil"
                },
                "subregion1": {
                    "code": "SP",
                    "name": "SP"
                },
                "subregion2": {
                    "code": "São Paulo",
                    "name": "São Paulo"
                },
                "subregion3": {
                    "code": "Vila Antonieta",
                    "name": "Vila Antonieta"
                },
                "street": "Rua Exemplo",
                "number": "01",
                "complement": "",
                "location": null
            },
            "email": null,
            "phone": "+5511111111111"
        },
        "carrier": {
            "cnpj": "00000000000000",
            "fantasyName": "carrier",
            "stateRegistration": "096/3624636",
            "id": "vtexlog_exemplo",
            "name": "Carrier LTDA.",
            "address": {
                "postalCode": "90200001",
                "country": {
                    "code": "BRA",
                    "name": "Brasil"
                },
                "subregion1": {
                    "code": "RS",

                  "name": "Rio Grande do Sul"
                },
                "subregion2": {
                    "code": "Porto_Alegre",
                    "name": "Porto Alegre"
                },
                "subregion3": {
                    "code": "Anchieta",
                    "name": "Anchieta"
                },
                "street": "Rua Exemplo",
                "number": "01",
                "complement": "Pavilhão 6",
                "location": null
            },
            "email": "email",
            "phone": "+5511111111111"
        }
    }
}
```

Response body example:
```json
{
    <packageId> : {
        "tracking": {
            "number": string,
            "url": string
        },
        "notification": {
            "id": string
        }
    }
}
```


## Learn more

See this guide on [how to develop carrier apps on VTEX IO](https://developers.vtex.com/vtex-rest-api/docs/getting-started-with-vtex-io-for-carriers). You can also learn more about the [integration flow](https://developers.vtex.com/vtex-rest-api/docs/integration-flow) and [tracking](https://developers.vtex.com/vtex-rest-api/docs/tracking-1) for carrier apps.