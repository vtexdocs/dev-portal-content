---
title: "List pickup points by location"
slug: "list-pickup-points-by-location"
hidden: false
createdAt: ""
updatedAt: ""
---
Pickup points are locations where customers pick up their orders. A store provides pickup points so that its customers have the option of choosing to receive their order at their address (delivery) or to pick it up at a specified location (pickup). For more information, access [pickup points](https://help.vtex.com/en/tutorial/pickup-points--2fljn6wLjn8M4lJHA6HP3R).

This guide will describe how to retrieve information about collection points close to a certain location determined by geographic coordinates or postal and country codes.

## Listing pickup points by location

To list all pickup points near a specific location, you need to use the [List pickup points by location](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/pickup-points) endpoint. There are two methods to retrieve pickup points using query parameters in the URL request.

Base URL: `https://{accountName}.{environment}.com.br/api/checkout/pub/pickup-points`

### 1. Geographic coordinates

Use the geographic coordinates (first longitude, then latitude) of the location where you want to check for nearby pickup points. See a URL request example below:

`https://{accountName}.{environment}.com.br/api/checkout/pub/pickup-points?geoCoordinates=-43.1974334;-22.9573465`

### 2. Postal and Country Codes

Use the postal and country codes of the location where you want to check for nearby pickup points. See a URL request example below:

`https://{accountName}.{environment}.com.br/api/checkout/pub/pickup-points?postalCode=22250040&countryCode=BRA`

> ⚠️ The search for pickup points must be done using only one of the two methods in the URL (geographical coordinates or postal and country codes). If you try to use both query parameters, the request will not return the list of collection points.

After choosing one of the two described methods and sending the URL request, the terminal will return the body of the response containing the information of the registered pickup points closest to the informed location, as shown in the example below:

```json
...
    "items": [
        {
            "distance": 0.13299603760242462,
            "pickupPoint": {
                "friendlyName": "Cantina",
                "address": {
                    "addressType": "pickup",
                    "receiverName": null,
                    "addressId": "300",
                    "isDisposable": true,
                    "postalCode": "22250-040",
                    "city": "Rio de Janeiro",
                    "state": "RJ",
                    "country": "BRA",
                    "street": "Praia de Botafogo",
                    "number": "300",
                    "neighborhood": "Botafogo",
                    "complement": "",
                    "reference": null,
                    "geoCoordinates": [
                        -43.18259,
                        -22.94436
                    ]
                },
                "additionalInfo": null,
                "id": "1_300",
                "businessHours": [
                    {
                        "DayOfWeek": 0,
                        "OpeningTime": "08:00:00",
                        "ClosingTime": "08:00:00"
                    },
                    {
                        "DayOfWeek": 1,
                        "OpeningTime": "08:00:00",
                        "ClosingTime": "08:00:00"
                    },
                    {
                        "DayOfWeek": 2,
                        "OpeningTime": "08:00:00",
                        "ClosingTime": "08:00:00"
                    },
                    {
                        "DayOfWeek": 3,
                        "OpeningTime": "08:00:00",
                        "ClosingTime": "08:00:00"
                    },
                    {
                        "DayOfWeek": 4,
                        "OpeningTime": "08:00:00",
                        "ClosingTime": "08:00:00"
                    },
                    {
                        "DayOfWeek": 5,
                        "OpeningTime": "08:00:00",
                        "ClosingTime": "08:00:00"
                    },
                    {
                        "DayOfWeek": 6,
                        "OpeningTime": "08:00:00",
                        "ClosingTime": "08:00:00"
                    }
                ]
            }
        },
...
```

> ⚠️ The pickup points returned are not necessarily all active. Make sure to validate the current availability information with the responsible for the pick up points on your account.

## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example (code ORD001)**: `"Input string was not in the correct format"`. This message will appear when the `geoCoordinates` value field is not sent correctly in the URL request.

```json
{
    "fields": {},
    "error": {
        "code": "001",
        "message": "Input string was not in a correct format.",
        "exception": null
    },
    "operationId": "2ff8e1f6-92f7-4921-be19-a5143a5b7a90"
}
```

- **Message error example (code CHK0264)**: `"Pickup not found"`. This message will appear when there are no pickup points near the location informed in this request.

```json
{
    "fields": {},
    "error": {
        "code": "CHK0264",
        "message": "Pickup not found",
        "exception": null
    },
    "operationId": "ca010e5c-9943-4485-a575-e79bd0761fa1"
}
```

### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`. Check that the URL data is correct.

```html
<body>
 <h1>404 Not Found</h1>
 <p>The requested URL was not found on this server.</p>
</body>
```
