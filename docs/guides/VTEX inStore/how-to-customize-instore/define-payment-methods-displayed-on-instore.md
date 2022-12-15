---
title: "Define payment methods displayed on inStore"
slug: "define-payment-methods-displayed-on-instore"
hidden: false
createdAt: "2021-09-16T22:06:59.987Z"
updatedAt: "2022-10-05T18:22:47.556Z"
---
After creating a payment condition as described in the [inStore - Payments](https://help.vtex.com/en/tracks/instore-payments--43B4Nr7uZva5UdwWEt3PEy/2liigRors32hzqBNs2M1Oa) guide, we need to create the filters that will define which payment methods will appear at inStore’s checkout.

You must do this by inserting a JavaScript object in the `checkout-instore-custom.js `file. Check out the [How to customize inStore](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore) guide for further information on how to access this file.

## Edit the `checkout-instore-custom.js` file

There are two options for defining which payment methods will be displayed on inStore. You can set global payment methods, that is, payment methods that any inStore user will be able to see, or payment methods per vendor, which means only specific users will be able to see them.



### Define global payment methods


1. The object that contains the payment filters is called `window.PAYMENTS_FILTER_GLOBAL`. If this object does not already exist in the code, you should insert it, as described below.

The `window.PAYMENTS_FILTER_GLOBAL` object should contain the following properties:

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`removeFilters`",
    "0-1": "array",
    "0-2": "You should add payment conditions that **will not** be displayed on inStore in this array",
    "1-0": "`filters`",
    "1-1": "array",
    "1-2": "You should add payment conditions that **will** be displayed on inStore in this array"
  },
  "cols": 3,
  "rows": 2
}
[/block]

You must identify each payment condition by their **payment condition ID**. Check [Where to find the payment condition ID](#where-to-find-the-payment-condition-id) for more details.

The code should look similar to the example below.

[block:code]
{
  "codes": [
    {
      "code": "\nwindow.PAYMENTS_FILTER_GLOBAL = {\n  removeFilters: [\n    '6', // Boleto Bancário\n    '45', // Direct debit\n  ],\n  filters: [\n    '2', '4', // Credit card\n    '202' // Cash\n    '125' // Pix\n  ]\n};",
      "language": "javascript"
    }
  ]
}
[/block]

In this example, we are excluding the conditions “Boleto bancário” (ID = 6) and "Direct debit" (ID = 45); and we are including “Credit card” (IDs = 2 and 4), “Cash” (ID = 202) and "Pix" (ID = 125). The first two will not be displayed at checkout, while the last two will be displayed.

2. Still in the `checkout-instore-custom.js` file, you need to add a reference to the object created within the `window.INSTORE_CONFIG` object.

To do this, include the following line of code inside the `window.INSTORE_CONFIG` object:

```javascript
payments: window.PAYMENTS_FILTER_GLOBAL
```

The `window.INSTORE_CONFIG` object should then look like the example below:

```javascript
window.INSTORE_CONFIG = {
    payments: window.PAYMENTS_FILTER_GLOBAL,
};
```
[block:callout]
{
  "type": "danger",
  "body": "Do not remove any of the other properties present in the `window.INSTORE_CONFIG` object to avoid breaking other functionalities."
}
[/block]
3. After making changes in the code, make sure you press the `Save` button.



### Define payment methods per sales associate

After you define the global payment methods that will be displayed in your store, you can override this information with the specific payment methods you want to remove for specific sales associates.

1. You must declare a constant object in the `checkout-instore-custom.js` file. Inside it, you can use `removeFilters` and `filters` properties described in the [Define global payment methods](#define-global-payment-methods) section to define the payment methods that will be displayed for this user.

    The example below determines that the user whose email is `john@email.com` will not see the Cash payment method option on inStore.

```javascript
const vendorConfig = {
  'john@email.com': {
    payments: {
      removeFilters: [
        '202', // Cash
      ],
    },
  },
}
```

2. Add the following functions to your `checkout-instore-custom.js` file. They will observe if the sales associate has a specific configuration associated with them, then set the specific payment methods filter associated with them, and repeat this validation every time a different user logs in.

```javascript
function hasVendorConfig(vendor) {
  const email = vendor && vendor.username
  return (
    email &&
    vendorConfig[email] &&
    vendorConfig[email].payments &&
    (vendorConfig[email].payments.filters ||
      vendorConfig[email].payments.removeFilters)
  )
}

function setPaymentsFilter(vendor) {
  const email = vendor && vendor.username
  if (hasVendorConfig(vendor)) {
    const pFilters = vendorConfig[email].payments
    if (pFilters.filters) {
      window.INSTORE_CONFIG.payments = window.INSTORE_CONFIG.payments || {}
      window.INSTORE_CONFIG.payments.filters = pFilters.filters
    }
    if (pFilters.removeFilters) {
      window.INSTORE_CONFIG.payments = window.INSTORE_CONFIG.payments || {}
      window.INSTORE_CONFIG.payments.removeFilters = pFilters.removeFilters
    }
  } else {
    window.INSTORE_CONFIG.payments = window.PAYMENTS_FILTER_GLOBAL
  }
}

function onVendorChange(vendor) {
  setPaymentsFilter(vendor)
}

document.addEventListener(
  'vendorIdentified',
  function (event) {
    const data = event.data
    const vendor = data.vendor
    onVendorChange(vendor)
  },
  false
)

onVendorChange(getVendor())
```

3. After making changes in the code, make sure you press the `Save` button.

### Where to find the payment condition ID

As explained above, the implementation of payment filters requires listing the payment condition IDs in the `window.PAYMENTS_FILTER_GLOBAL` object.

You can find the ID of each condition in the **Payments** module. In the main menu of the VTEX Admin, click on **Payments** and then on **Settings**.

In the **Payment conditions** tab, you will find the ID next to each of the conditions. In the example below, we see that the payment condition ID for Cash is `202`.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5d9d769-CASH-CODE.png",
        "CASH-CODE.png",
        1161,
        206,
        "#fafafb"
      ]
    }
  ]
}
[/block]
If we wanted to include Cash as a payment condition to be displayed at the inStore checkout, this would be the value we would add to the `filters` array, inside the `window.PAYMENTS_FILTER_GLOBAL` object of the `checkout-instore-custom.js` file.