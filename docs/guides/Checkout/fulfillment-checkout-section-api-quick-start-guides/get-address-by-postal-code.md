---
title: "Get address by postal code"
slug: "get-address-by-postal-code"
hidden: false
createdAt: ""
updatedAt: ""
---
To assist the customer in the process of filling in data at Checkout and also to select the sellers able to deliver the product in a certain area, it is possible to register postal codes and assign them to addresses in the VTEX database. For more information about deliveries, visit [Inventory & shipping - Overview](https://help.vtex.com/en/tutorial/visao-geral-logistics--tutorials_143).

This guide describes how to obtain the registered address information for a specific postal code and country.

## Getting address by postal code

To get the registered address information for a postal code, you need to use the [Get address by postal code](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/postal-code/-countryCode-/-postalCode-) endpoint. The country and postal code information must be sent through the URL request, as shown by the example below:

`https://{accountname}.{environment.com.br}/api/checkout/pub/postal-code/BRA/22250040`

After sending the request, the endpoint will return the response body containing the address information registered, as shown in the example below:

```json
...
{
    "postalCode": "22250040",
    "city": "Rio de Janeiro",
    "state": "RJ",
    "country": "BRA",
    "street": "Praia Botafogo",
    "number": "",
    "neighborhood": "Botafogo",
    "complement": "",
    "reference": "",
    "geoCoordinates": [
        -43.182182312011719,
        -22.94549560546875
    ]
}
...
```

## Error codes

The following errors may appear as a message in the response body.

### 200 - OK

Despite the code `200` (which indicates the success of the request), if there is no registered address in the VTEX database associated with the entered postal code/country, the response body will not contain any address information.

```json
{
    "postalCode": "222500",
    "city": "",
    "state": "",
    "country": "BRA",
    "street": "",
    "number": "",
    "neighborhood": "",
    "complement": "",
    "reference": "",
    "geoCoordinates": []
}
```

### 404 - Not Found

- `Message error example: "The requested URL was not found on the server"`: check that the URL data is correct.

```html
<body>
 <h1>404 Not Found</h1>
 <p>The requested URL was not found on this server.</p>
</body>
```

### 500 - Internal Server Error

- `Message error example (code ORD026): "A communication error with Postal Code Service has occurred"`. This message will appear when less than 3 country code digits are entered in the URL request.

```json
{
    "fields": {},
    "error": {
        "code": "ORD026",
        "message": "A communication error with Postal Code Service has occurred",
        "exception": null
    },
    "operationId": "9e8e40ad-f98d-4e36-81f3-1937caa83f1c"
}
```
