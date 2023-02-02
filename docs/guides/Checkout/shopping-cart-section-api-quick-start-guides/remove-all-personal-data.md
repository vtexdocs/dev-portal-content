---
title: "Remove all personal data from cart"
slug: "remove-all-personal-data"
hidden: false
createdAt: "2022-10-14T14:46:50.016Z"
updatedAt: "2022-11-03T22:36:44.199Z"
---
The shopping cart is where the information on the products chosen by the customer while browsing a store is gathered. This data may include item prices, shipping value, payment, and delivery methods, among others.

This guide will describe how to remove all personal data from a shopping cart by the API.

## Getting and accessing shopping cart information

The first step is to get the `orderFormId` and access the shopping cart information that you want to remove personal data. For more information, access the [Get cart information by ID](https://developers.vtex.com/vtex-rest-api/docs/get-cart-information-by-id) guide.

See below an example of some personal data contained in a shopping cart:

```json
...
"clientProfileData": {
     "email": "clark.kent@examplemail.com",
    "firstName": "Clark",
    "lastName": "Kent",
    "document": "44444444444",
    "documentType": "cpf",
    "phone": "+5511123456789",
    "corporateName": null,
    "tradeName": null,
    "corporateDocument": null,
    "stateInscription": null,
    "corporatePhone": null,
    "isCorporate": false,
    "profileCompleteOnLoading": false,
    "profileErrorOnLoading": false,
    "customerClass": null
},
…
"availableAddresses": [
    {
     "addressType": "residential",
     "receiverName": "Clark Kent",
     "addressId": "ae3173b32bf64663a81fc42b057be211",
     "isDisposable": true,
     "postalCode": "70386060",
     "city": "Brasília",
     "state": "DF",
     "country": "BRA",
     "street": "Quadra SQS 116 Bloco F",
     "number": "101",
     "neighborhood": "Asa Sul",
     "complement": null,
     "reference": null,
     "geoCoordinates": [
        -47.925922393798828,
        -15.832707405090332
     ]
    }
]
...
```

> ℹ️️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) overview.

## Removing all personal data from the shopping cart 

To remove all personal data from a shopping cart, you can use your browser to create an URL based on the  `orderFormId` value. See an example below:

- **ordeFormId**: `9620cbb7ebc34ca68a86621428816c5a`
- **New URL**: `https://{accountname}.{environment.com.br}/checkout/changeToAnonymousUser/9620cbb7ebc34ca68a86621428816c5a`

After accessing the URL created in your browser, you will be redirected to the cart page, where all personal data has been removed.

**Important**: The page with the cart without personal information is displayed, because when the URL is accessed, a new orderForm is generated and a new cookie is saved in the browser.



[block:callout]
{
  "type": "warning",
  "body": "Alternatively, if you are using a backend or similar implementation, it is also possible to create a new cart (without any personal data) using the [Create a new Cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart) endpoint and adding the same items from the previous cart through the [Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)."
}
[/block]