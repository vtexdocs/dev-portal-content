---
title: "Headless cart and checkout"
slug: "headless-cart-and-checkout"
hidden: false
createdAt: "2021-03-31T21:20:32.157Z"
updatedAt: "2024-09-19T20:20:32.157Z"
excerpt: "This guide explains how to implement a shopping cart and manage the checkout process in a headless ecommerce store, using the Checkout API to handle all interactions through API requests, without a traditional user interface."
---

A [headless](https://developers.vtex.com/docs/guides/headless-commerce) store handles all ecommerce integration without a traditional user interface, relying solely on API requests. In this guide, you will learn how to create a shopping cart and manage the checkout flow using features from the [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api) in your headless store.

## Shopping cart

In the Checkout API, the VTEX shopping cart information is organized using the `orderForm`, an object containing all information relevant to the purchase, from the products to shipping and payment information, among others.

The `orderForm` is a complex data structure with many customization possibilities. The essential section for placing an order is divided into [`items`](#cart-items) and [`attachments`](#cart-attachments).

For a customer to make a purchase, the store must have a shopping cart that contains an `orderForm` for them. When you use the [Get current or create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm) endpoint, you get an `orderFormId` in the response.

> ⚠️ If your headless storefront is not browser-based (e.g., native app), it is important that you save the `orderFormId` and use it to manage the cart's information with the requests above. Otherwise, VTEX cookies will automatically manage this information in the customer's browser.

<CH.Scrollycoding>

### Cart items

In the `orderForm`, product information is stored inside `items`, where each object corresponds to a SKU contained in the cart. Below is a basic example of a shopping cart containing two units of SKU `123`, to be fulfilled by seller 1, at a price of `$100.00` per unit.

```json Request
"items": [
    {
        "id": "123",
        "quantity": 2,
        "seller": "1",
        "price": 10000
    }
]
```

The information above is sufficient to place an order, but there are other possible fields for shopping cart items, many of which are populated by VTEX modules.

To learn how to add products to a shopping cart, read the guide [Add cart items](https://developers.vtex.com/docs/guides/add-cart-items).

>ℹ️ If the customer leaves the store, make sure you keep the `orderFormId` so you can retrieve their previously abandoned cart with the [Get cart information by ID](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm/-orderFormId-) endpoint.

---

### Cart attachments

Shopping cart attachments are `orderForm` objects containing order information related to the [client profile](https://developers.vtex.com/docs/guides/add-client-profile), [shipping address and delivery option](https://developers.vtex.com/docs/guides/add-shipping-address-and-delivery-option-to-the-cart), [marketing data](https://developers.vtex.com/docs/guides/add-marketing-information-to-the-cart), [payment data](https://developers.vtex.com/docs/guides/adding-payment-information-to-the-cart), and [merchant context data](https://developers.vtex.com/docs/guides/add-merchant-context-information-to-the-cart). Check a basic example of a cart attachments.

```json Request
{
  "userProfileId": "fb542e51-5488-4c34-8d17-ed8fcf597a94",
  "profileProvider": "VTEX",
  "availableAccounts": [],
  "availableAddresses": [
    {
      "addressType": "residential",
      "receiverName": "Clark Kent",
      "addressId": "666c2e830bd9474ab6f6cc53fb6dd2d2",
      "isDisposable": false,
      "postalCode": "12345-000",
      "city": "Metropolis",
      "state": "NY",
      "country": "USA",
      "street": "My street",
      "number": "123",
      "neighborhood": "My neighborhood",
      "complement": null,
      "reference": null,
      "geoCoordinates": [-47.924747467041016, -15.832582473754883]
    }
  ],
  "userProfile": {
    "email": "clark.kent@example.com",
    "firstName": "Clark",
    "lastName": "Kent",
    "document": "12345678900",
    "documentType": "cpf",
    "phone": "+556199999999",
    "corporateName": null,
    "tradeName": null,
    "corporateDocument": null,
    "stateInscription": null,
    "corporatePhone": null,
    "isCorporate": false,
    "profileCompleteOnLoading": null,
    "profileErrorOnLoading": null,
    "customerClass": null
  },
  "isComplete": true
}
```

> ℹ️ Some attachments may contain arrays of objects, where each object corresponds to an item in the [items](#cart-items) array.

---

## Place order

There are two ways of placing orders with the Checkout API:

- [Place new order](#place-new-order): Manage shopping cart information in your frontend and then use one API request to send all order information to VTEX.
- [Place order from existing cart](#place-order-from-existing-cart): Manage shopping cart information in the VTEX platform throughout the shopping experience, then place an order from that data using just the cart ID.

The [place new order](#place-new-order) method increases the complexity of your application since you must manage all shopping cart data to correctly assemble the [`orderForm`](#shopping-cart). Additionally, placing a new order does not send shopping cart information to VTEX until the customers complete their purchase.

The [place order from existing cart](#place-order-from-existing-cart) method is recommended in most cases. Use [place new order](#place-new-order) if your operation has specific requirements, such as limiting the number of HTTP requests sent from your storefront.

### Place new order

To place a new order without any shopping cart data previously stored on the VTEX platform, use the [Place order](https://developers.vtex.com/docs/api-reference/checkout-api#put-/api/checkout/pub/orders) endpoint.

For a tutorial of this method, check the guide [Create a regular order from an existing cart](https://developers.vtex.com/docs/guides/create-a-regular-order-using-the-checkout-api) or follow the steps in the [Create a regular order using the Checkout API](https://developers.vtex.com/docs/guides/create-a-regular-order-using-the-checkout-api).

### Place order from existing cart

You can also place an order from an existing cart, which already has an orderForm structure and a shopping cart ID. To do so, use the [Place order from an existing cart](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/transaction) endpoint or follow the steps in the [Create a regular order from an existing cart](https://developers.vtex.com/docs/guides/create-a-regular-order-from-an-existing-cart) guide.

This endpoint may be used to perform tasks such as adding products to a cart or linking shipping information to the order.

## Order privacy

During the process of placing the order, merchants need to account for the security and privacy of customer information throughout checkout.

When a new cart is created, a new cookie named `CheckoutOrderFormOwnership` is sent empty alongside the existing `checkout.vtex.com` cookie, which contains the cart's `orderFormId`. This mechanism ensures that only the customer who created the cart has unrestricted access to their personal information.

You need to make requests with the client data to set `CheckoutOrderFormOwnership` to a value. Without this cookie, the returned order form will have masked personal data such as `clientProfileData` and `shippingData`.

> ⚠️ Please contact [VTEX support](https://support.vtex.com/hc/en-us/requests) to enable this feature in your store. This feature is not available to stores using [FastStore](https://developers.vtex.com/docs/guides/faststore).

### Add client profile data

Once you created a new cart, use the [Get current or create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm) endpoint to retrieve the created `orderForm`, as in the example.

```json Response Get current or create a new cart
{
  "orderFormId": "9ceee0fde6db489fbc682a0e2ab13a86",
  "salesChannel": "1",
  "loggedIn": false,
  "isCheckedIn": false,
  "storeId": "1",
  "checkedInPickupPointId": "21",
  "allowManualPrice": false,
  "canEditData": true,
  "userProfileId": "fb542e51-5488-4c34-8d17-ed8fcf597a94",
  "userType": "User type",
  "ignoreProfileData": false,
  "value": 0,
  "messages": [],
  "items": [],
  "selectableGifts": [],
  "totalizers": [],
  "shippingData": null,
// !mark(1:17) gold
  "clientProfileData": {
    "email": "clark.kent@examplemail.com",
    "firstName": "Clark",
    "lastName": "Kent",
    "document": "12345678900",
    "documentType": "cpf",
    "phone": "+5500123456789",
    "corporateName": "company-name",
    "tradeName": "trade-name",
    "corporateDocument": "12345678000100",
    "stateInscription": "12345678",
    "corporatePhone": "551100988887777",
    "isCorporate": false,
    "profileCompleteOnLoading": false,
    "profileErrorOnLoading": false,
    "customerClass": null
  },
  "paymentData": {
    "installmentOptions": [],
    "paymentSystems": [],
    "payments": [
      {
        "paymentSystem": 6,
        "bin": null,
        "accountId": "12",
        "tokenId": null,
        "value": 34390,
        "referenceValue": 34390,
        "giftCardRedemptionCode": null,
        "giftCardProvider": null,
        "giftCardId": null
      }
    ],
    "giftCards": [],
    "giftCardMessages": [],
    "availableAccounts": [],
    "availableTokens": []
  },
  "marketingData": null,
  "sellers": [],
  "clientPreferencesData": {
    "locale": "pt-BR",
    "optinNewsLetter": null
  },
  "commercialConditionData": null,
  "storePreferencesData": {
    "countryCode": "BRA",
    "saveUserData": true,
    "timeZone": "E. South America Standard Time",
    "currencyCode": "BRL",
    "currencyLocale": 1046,
    "currencySymbol": "R$",
    "currencyFormatInfo": {
      "currencyDecimalDigits": 2,
      "currencyDecimalSeparator": ",",
      "currencyGroupSeparator": ".",
      "currencyGroupSize": 3,
      "startsWithCurrencySymbol": true
    }
  },
  "giftRegistryData": null,
  "openTextField": null,
  "invoiceData": null,
  "customData": null,
  "itemMetadata": {
    "items": [
      {
        "id": "1",
        "seller": "1",
        "name": "Purina Friskies Wet Cat Food Gravy Pate",
        "skuName": "Purina Friskies Wet Cat Food Gravy Pate",
        "productId": "1",
        "refId": "0001",
        "ean": "123456789",
        "imageUrl": "http://lojadobreno.vteximg.com.br/arquivos/ids/155450-55-55/Racao-Royal-Canin-Feline-Urinary-SO.jpg?v=637139444438700000",
        "detailUrl": "/racao-royal-canin-feline-urinary/p",
        "assemblyOptions": []
      }
    ]
  },
  "hooksData": null,
  "ratesAndBenefitsData": {
    "rateAndBenefitsIdentifiers": [],
    "teaser": []
  },
  "subscriptionData": null,
  "itemsOrdination": {
    "criteria": "NAME",
    "ascending": true
  }
}
```

Once you have the `orderForm`, you must add the client data to it. To do so, send the profile data in the [Add client profile](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/clientProfileData) endpoint request, as in the example.

```json Request Add client profile
{
  "email": "customer@examplemail.com",
  "firstName": "first-name",
  "lastName": "last-name",
  "documentType": "cpf",
  "document": "123456789",
  "phone": "+55110988887777",
  "corporateName": "company-name",
  "tradeName": "trade-name",
  "corporateDocument": "12345678000100",
  "stateInscription": "12345678",
  "corporatePhone": "+551100988887777",
  "isCorporate": false
}
```

For more information about this endpoint, check the guide [Adding customer profile information to the cart](https://developers.vtex.com/docs/guides/add-customer-profile-information-to-the-cart).

After making this request, the `CheckoutOrderFormOwnership` cookie will be set as a string with encrypted values of the client profile data.

---

### Add address data

Once the client data has been added, it is also important to add the customer address data to the `orderForm`. This data includes all information about the delivery of the order to the customer. To do so, use the [Add shipping address and select delivery option](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/shippingData) endpoint.

```json Request
{
  "clearAddressIfPostalCodeNotFound": false,
  "selectedAddresses": [
    {
      "addressType": "residential",
      "receiverName": "receiver name",
      "addressId": "c3701fc4c61b4d1b91f67e81415db44d",
      "postalCode": "12345-000",
      "city": "Rio de Janeiro",
      "state": "RJ",
      "country": "BRA",
      "street": "Praia de Botafogo",
      "number": "300",
      "neighborhood": "Botafogo",
      "complement": "3rd floor",
      "reference": "Grey building",
      "geoCoordinates": [-47.924747467041016, -15.832582473754883]
    }
  ],
  "logisticsInfo": [
    {
      "itemIndex": 0,
      "selectedDeliveryChannel": "delivery",
      "selectedSla": "normal"
    }
  ]
}
```

For more information about this endpoint, check the [Adding shipping address and delivery options to the cart](https://developers.vtex.com/docs/guides/add-shipping-address-and-delivery-option-to-the-cart) guide.

When making [this request](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/orderForm/-orderFormId-/attachments/shippingData), the `CheckoutOrderFormOwnership` cookie is updated with this new information.

---

### Unmask `orderForm`

[VTEX Personal Identifiable Information (PII) data](https://developers.vtex.com/docs/guides/pii-data-architecture-specifications) is masked by default. This means that when you access a shopper's order history in the VTEX Admin panel or when you request their profile information via API, for example, any PII information returned will be masked.

After adding the client profile data and address data, you can access the previously masked information. Use the [Get current or create a new cart](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/orderForm) endpoint again, but include the latest `CheckoutOrderFormOwnership` cookie value in the request.

With the correct ownership cookie, both client profile data and address data are unmasked, providing the full details.

## Complete order

After placing an order using either of the methods presented above, you will receive an `orderId` and `transactionId` in the response body, along with some login values. Your integration must use this information to complete the purchase process within five minutes. This involves [sending payment information](#send-payment-information) and then [requesting order processing](#process-order).

> ❗ Failing to perform these steps within five minutes will cause the order to be automatically canceled and tagged as [`incomplete`](https://help.vtex.com/en/tutorial/how-incomplete-orders-work--tutorials_294).

### Send payment information

To send the payment information to VTEX, use one of these endpoints:

- [Send payment information (public)](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pub/transactions/-transactionId-/payments)
- [Send payment information (private)](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/payments).

The request body used in this step is based on the order's `paymentData` attachment. You can get this data from the response of the [Get client profile by email](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/profiles), as in the example.

```json Request
"paymentData":{
   "updateStatus":"updated",
   "installmentOptions":[
      {
         "paymentSystem":2,
         "bin":null"paymentName":null"paymentGroupName":null"value":65780,
         "installments":[
            {
               "count":1,
               "hasInterestRate":false,
               "interestRate":0,
               "value":65780,
               "total":65780,
               "sellerMerchantInstallments":[
                  {
                     "id":"MYSHOP",
                     "count":1,
                     "hasInterestRate":false,
                     "interestRate":0,
                     "value":65780,
                     "total":65780
                  }
               ]
            }
         ]
      }
   ]
}
```

Learn more about these endpoints:

- [`POST` Send payment information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pub/transactions/-transactionId-/payments)
- [`POST` Send payment information with a saved credit card](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pvt/transactions/-transactionId-/payments)

> ❗ Make sure that all value-related fields match the information sent when [placing the order](#place-order) to create a successful request.

---

#### Retrieving saved credit cards

In the payment section at checkout, we recommend retrieving the saved credit card information from the customer profile. This can ease the checkout process as the customer would only need to select the chosen credit card and input the CVV (Card Verification Value). This process will only display the last four numbers of a credit card to the customer, making it a secure interaction with the client data.

To check if the customer has any saved cards, use the [Get client profile by email](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/profiles) endpoint. This endpoint returns the available cards. The card information is displayed in the `availableAccounts` array, as shown in the examples.

```json Response for customer with available cards
{
    "userProfileId": "f072eafc-53a4-4aa7-9e14-6b266f918e77",
    "profileProvider": "PROFILE PROVIDER DESCRIPTION",
// !mark(1:16) gold
    "availableAccounts": [
        {
            "accountId": "AD6ADBF4359F4B3EBCC4A61ADD176BBE",
            "paymentSystem": "2",
            "paymentSystemName": "Visa",
            "cardNumber": "************7127",
            "bin": "415275",
            "availableAddresses": [
                "XJC",
                "6356888228140",
                "SPT",
                "XPJ"
            ],
            "isExpired": null
        }
    ],
...
}
```

```json Response for customer with no available cards
{
    "userProfileId": "f072eafc-53a4-4aa7-9e14-6b266f918e77",
    "profileProvider": "PROFILE PROVIDER DESCRIPTION",
// !mark(1) gold
    "availableAccounts": [],
...
}
```

> ℹ️ You can enable a checkbox that allows the customer to choose if they want to save the credit card information or not. To learn how to enable it, read the guide [Enable the Save user data opt-in](https://developers.vtex.com/docs/guides/enable-the-save-user-data-opt-in#saving-personal-and-payment-data).

---

### Process order

Lastly, you must request order processing by using the [Process order](https://developers.vtex.com/docs/api-reference/checkout-api#post-/api/checkout/pub/gatewayCallback/-orderGroup-) endpoint after the order's payment is approved. If the payment has not been approved yet, it will return a status code `500` error.

> ⚠️ Keep in mind that this process uses the [gateway connectors](https://help.vtex.com/en/tutorial/what-is-the-connector--3lze0Cu0bmyC6u2o2iaeEA#) configured in your VTEX environment. Be careful when using it to avoid any unwanted charges or unexpected payment denials.

## Verify order status

Once you have successfully placed an order, sent payment information, and requested order processing, you will be able to see the order in the [Order management module](https://help.vtex.com/en/tutorial/orders-list--tutorials_200#) in VTEX Admin.

You can also use the [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) and [List orders](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders) endpoints for this purpose. Another way to check the order updates is by integrating [Feed v3](https://developers.vtex.com/docs/guides/orders-feed#best-practices-for-integrations) and [Hook](https://developers.vtex.com/docs/guides/orders-feed#hook) with your store.

## Checkout interface

When a customer goes to your store checkout, your [frontend implementation](https://help.vtex.com/en/tracks/trilha-da-loja-vtex--eSDNk26pdvemF3XKM0nK9/67SCtUreXxKYWhZh8n0zvZ) must handle several tasks. Follow the sections below to implement these tasks effectively.

### Order details

Order details provided by customers at checkout, such as profile information or shipping address, are [attachments](#cart-attachments) of the [shopping cart](#shopping-cart).

You must handle this information based on the order placement method you choose. Refer to the corresponding section for detailed instructions:

- [Place new order](#place-new-order)
- [Place order from existing cart](#place-order-from-existing-cart)

### Address autofill

Implement an address autofill feature using the following endpoint:

- [`GET` Get address by postal code](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/postal-code/-countryCode-/-postalCode-)

### Pickup points

Shipping information is added to the order as [`orderForm` attachments](#order-details). To allow customers to choose nearby pickup points, use the following endpoint:

- [`GET` List pickup points by location](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/pickup-points)

>❗️ [reCAPTCHA integration](https://help.vtex.com/en/tutorial/using-recaptcha-at-checkout--18Te3oDd7f4qcjKu9jhNzP) does not work in Headless checkout. It only works with stores using [Checkout v6](https://help.vtex.com/en/tutorial/enable-checkout-v6--7qVqv3ptRvpVVplrvg8ruH).

## Learn more

Check these other guides to learn more about building a headless shopping experience using VTEX:

- [Headless commerce overview](https://developers.vtex.com/docs/guides/headless-commerce)
- [Headless catalog and search](https://developers.vtex.com/docs/guides/headless-catalog)
- [Headless profile management and order history](https://developers.vtex.com/docs/guides/headless-profile-management-and-order-history)

</CH.Scrollycoding>
