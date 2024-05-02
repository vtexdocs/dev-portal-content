---
title: "Checkout UI Custom Upload Prescription"
slug: "vtex-checkout-ui-custom"
hidden: true
createdAt: "2020-08-17T17:45:05.312Z"
updatedAt: "2022-08-05T17:29:34.165Z"
---
The Checkout UI Custom app is responsible for customizing your store's Checkout UI through the admin's interface.

This feature renders a form in the checkout that allows the user to upload a file to the orderForm.

<img width="1010" alt="Captura de Pantalla 2021-09-14 a la(s) 11 44 16" src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-checkout-ui-custom-0.png"/>

## Configuration

1. Using your terminal and the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference), log into the desired VTEX account.
2. Run `vtex install vtex install vtexarg.file-manager-rest` on the account you're working on.
3. Run `vtex install vtex.checkout-ui-custom@0.5.3-hkignore.1` on the account you're working on.
4. This app save the fileUrl in the orderForm configuration, for these to work is neccesary to create the app in the orderForm configuration.

## Creating the app in the orderForm configuration

1. First of all, you should [get your current orderForm configuration](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pvt/configuration/orderForm).
2. Through Postman, make a GET request to this endpoint `https://{{account}}.myvtex.com/api/checkout/pvt/configuration/orderForm`.

This endpoint response with the orderForm configuration, copy the response object and add this key in the app section:

```json
"apps": [

+    {
+        "fields": [
+            "data"
+        ],
+        "id": "uploadfiles",
+        "major": 1
+    },

]
```

3. POST the new orderForm configuration with the new app.
4. Through Postman, make a POST request to this endpoint `https://{{account}}.myvtex.com/api/checkout/pvt/configuration/orderForm`.

<img width="1353" alt="Captura de Pantalla 2021-09-14 a la(s) 12 39 35" src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-checkout-ui-custom-1.png"/>

>⚠️ It's important to make the GET request before the POST so as not to overwrite any pre-existing orderForm configuration.
