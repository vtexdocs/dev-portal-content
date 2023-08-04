---
title: "Enable the Region for SKUs"
slug: "enable-the-region-for-skus"
hidden: false
createdAt: "2022-03-16T13:25:27.263Z"
updatedAt: "2022-10-20T17:37:06.455Z"
---
The Region feature is one of the features made available by the session system installation. It aims to regionalize user experience of the store. It allows, for example, for sellers to set their own prices and that the marketplaces display them according to the client’s region.

After you [set up delivery](https://help.vtex.com/en/tutorial/setting-up-price-and-availability-of-skus-by-region--12ne58BmvYsYuGsimmugoc#setting-up-delivery-in-franchise-accountseller-white-label) of a SKU to a White Label Seller from your store, it is necessary for the session system to identify the zip code and country of the user browsing the store to show the custom price and availability by region.

This information about ZIP code and country can be stored in the cookie [vtex_session](https://help.vtex.com/en/tutorial/setting-up-price-and-availability-of-skus-by-region--12ne58BmvYsYuGsimmugoc), due to a purchase made previously by the user, or can be entered via JavaScript in the session.

To enter the country and zip code in the session, you must perform a `POST` in the following route:
`{{account-name}}.{{environment}}.com.br/api/sessions`

Below are examples of bodies to be sent to `POST`:

- Update session by zipCode.

```json
{
	"public":{
		"country":{
			"value":"USA"
		},
		"postalCode":{
			"value":"32004"
		}
	}
}
```

- Update session by geo-coordinates.

```json
{
	"public":{
		"country":{
			"value":"USA"
		},
		"geoCoordinates":{
			"value":"22.123,-14.1"
		}
	}
}
```

- Update session by address.

```Json
{
    "public": {
        "storeUserEmail": {
            "value": "<mailto:example@example.complexample.com>"
        },
        "adressId": {
            "value": "123456789"
        }
    }
}
```

To verify that the session has updated the country and zip code data, simply do a `GET` on the route below and search for the ` country` and `Post Code` fields:
`{{account-name}}.{{environment}}.com.br/api/sessions?items={{namespace}}.{{value}},{{namespace}}.{{value2}}`

After updating the page where the SKUs are being viewed in the store, the price and availability information will be updated according to the region specified in the country and zip code information.
