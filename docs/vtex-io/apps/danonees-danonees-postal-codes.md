---
title: "Name"
slug: "danonees-danonees-postal-codes"
excerpt: "danonees.danonees-postal-codes@1.0.0"
hidden: true
createdAt: "2022-07-19T14:16:35.368Z"
updatedAt: "2022-08-01T07:17:24.120Z"
---
danonees-postal-codes


## Description

Application developed to allow the customer to choose the type of shipment based on zipcode by assigning the correct sales channel

## Installation
You will then install this application from the command console:

```cmd
vtex install danonees.danonees-postal-codes@x.x.x
```


## Dependencies
```
  {
    "vtex.store": "2.x",
    "vtex.store-graphql": "2.x",
    "vtex.render-runtime": "8.x",
    "vtex.order-manager": "0.x",
    "vtex.order-items": "0.x",
    "vtex.styleguide": "9.x",
    "vtex.css-handles": "0.x",
    "vtex.checkout-graphql": "0.x",
    "vtex.session-client": "1.x"
  },
```

You will then install this applications from the command console:

```cmd
  vtex install vtex.store@2.x
  vtex install vtex.store-graphql@2.x
  vtex install vtex.render-runtime@8.x
  vtex install vtex.order-manager@0.x
  vtex install vtex.order-items@0.x
  vtex install vtex.styleguide@9.x
  vtex install vtex.css-handles@0.x
  vtex install vtex.checkout-graphql@0.x
  vtex install vtex.session-client@1.x
```

## Configuration

1. Add the Danone ES postal codes app to your theme's dependencies in the `manifest.json` file:

```diff
 "dependencies": {
   "danonees.danonees-postal-codes": "0.x"
 }
```

2. On the desired page template, such as `header`, you can add with the interface available: `delivery-zipcode-banner` block:

```json
  "sticky-layout#desktop": {
    "children": [
      ...,
     "delivery-zipcode-banner"
    ]
  },
  "sticky-layout#mobile": {
    "children": [
      ...,
      "delivery-zipcode-banner"
    ]
  },
```

* This configuration will show us a banner 

Desktop/Mobile view
- On the first load, it checks if the `DeliveryPostalCode` cookie exists, which stores the postal code where the products will be shipped, if it exists, it will show a banner with the postal code stored in the cookie 

![delivery-zipcode-banner](./postal-code-banner.png)

- You can change the postal code pressing the banner and a popup will open where we can select the postal code. The change of postal code can suppose a change of commercial policy. 

![delivery-postalcode-modal](./postal-code-modal.png)

- In case of being a commercial policy different from the one of the previous postal code, it is verified that the products of the cart are in the new commercial policy, if not, it indicates it to us and it gives us the option to remain in the current policy or change, thus losing the products that are not in the new commercial policy.

![delivery-postalcode-products-error](./postal-code-products-error.png)

- If the postal code entered is not registered, it tells us and we can check another postal code.

![delivery-postalcode-error](./modal-postal-code-error.png)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.