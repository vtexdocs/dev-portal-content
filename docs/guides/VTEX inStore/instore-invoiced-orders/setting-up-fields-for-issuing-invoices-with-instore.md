---
title: "Setting up fields for issuing invoices with inStore"
slug: "setting-up-fields-for-issuing-invoices-with-instore"
hidden: false
createdAt: "2022-09-13T20:52:17.438Z"
updatedAt: "2022-09-13T21:13:38.490Z"
---
For the invoice of an order made using inStore to have all the necessary fields, you need to configure some extra fields in the **orderForm**. In addition, these extra fields allow VTEX orders module to correctly identify when an order is made through inStore.

To set these extra fields up, follow the steps below:

1. Make a request to the [Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration).
2. Save the response from this request.
3. You will see that the "apps" property will have the value of an empty array (`[]`). Insert the following snippet in the brackets:

```json
     {
       "fields": [
  "cart-extra-context",
  "cart-type",
      ],
      "id": "cart-extra-context",
      "major": 1
      }
```

4. Save your text file.
5. Make a request to the [Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration). The body of this `POST` will be the entire content of the file from the previous step.

Now the orderForm of your orders already has the extra fields. To check if the `POST` has succeeded, you can check the update by using the [Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration) and verify that the "apps" property has the new information.