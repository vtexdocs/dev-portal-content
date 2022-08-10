---
title: "Avalara"
slug: "vtex-avalara"
excerpt: "vtex.avalara@3.3.4"
hidden: true
createdAt: "2022-07-12T20:03:44.116Z"
updatedAt: "2022-08-02T20:19:40.459Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

The Avalara Tax Calculator app integrates the VTEX Smart Checkout and OMS with Avalara's real-time tax calculation service, enabling you to calculate taxes based on the items being bought, the inventory addresses, and the shipping address.

Some of the app main functionalities are, namely:

- Calculation of shopping cart taxes.
- Perform commits in the Avalara system when the order is invoiced.
- Manage tax exemptions for specific customers.

> ⚠️ _This app does not support Avalara Brazil. For Avalara Brazil support, please use the [Avalara Brazil App](https://vtex.io/docs/app/vtex.avatax-br)_

## Configuration

> ⚠️ _Before installing this app, make sure you already have an Avalara account, tax codes registered for your products, and registered addresses for your logistics docks._

1. Using your terminal, [install](https://vtex.io/docs/recipes/development/installing-an-app/) the `vtex.avalara@3.x` app. You can confirm that the app has been installed in your account by running `vtex ls` again.

> ℹ️ _It is possible to install the Avalara app using your account's admin page as well. Access the **Apps** section and then click on `Install` in the Avalara box._

2. In your admin sidebar, access the **Other** section and click on `Avalara Tax Calculator`.
3. Fill in your Avalara credentials in the form.
4. Click on `TEST CONNECTION`. If the connection is successful, click `UPDATE` to save your configuration.
5. Perform the desired settings according to the available fields:

- `Production Mode` - Enables production mode in the Avalara API when set as `Yes`.
- `Activate in Checkout`: Activates tax calculation in checkout when set as `Yes`. Caution: this setting may have an impact in your checkout flow. Make sure it is properly configured before saving your changes.
- `Document Commiting`: Commits transaction data to Avalara once orders are invoiced when set as `Yes`. For more information on commits, check out [Avalara's documentation](https://developer.avalara.com/avatax/dev-guide/transactions/should-i-commit/).
- `Activate Refund`: Enables refund transactions to be submitted to Avalara whenever an user submits a refund. This functionality will appear when document committing is set as `Yes`.
- `Location Code`: Select a default location code for all transactions to report to. Selecting `None` will send no locationCode to Avalara. Please checkout [Avalara's documentation](https://developer.avalara.com/avatax/dev-guide/locations/location-based-reporting/) for more information on location based reporting.
- `Avalara Tax Record Date`: Select `Order Placed` setting if you want committed transactions to use the date the order was created. Select `Order Invoiced` if you want committed transactions to use the date the order reached `Invoiced` status.
- `Enable Colorado Retail Delivery Fee`: Activating this toggle will cause the Colorado Retail Delivery Fee to be added to orders with a Colorado shipping destination. See this [Avalara blog post](https://www.avalara.com/blog/en/north-america/2022/05/colorados-new-retail-delivery-fee-takes-effect-july-1-2022.html) for more information.

6. Save your changes.

### (Optional) Address Validation

If your Avalara account is provisioned for address validation, you may validate addresses by sending requests to the following API, using your Avalara `account ID` as authentication. Example requests and responses are provided below.

| Field         | Value                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **URI**       | /avalara/checkout/AddressVerification                                                                                                   |
| **METHOD**    | POST                                                                                                                                    |
| **API Usage** | Verifies address and returns the respective Avalara response. `isValidAddress` field will determine whether or not the address is valid |

_Example Request Body:_

```json
{
  "line1": "19501 19501 Biscayne Blvd Space",
  "city": "Aventurareaa",
  "region": "FL",
  "country": "USA",
  "postalCode": "33180"
}
```

_Example Headers:_
Authorization: **AccountIdValue**

_Example Response With Valid Address:_

```json
{
  "address": {
    "line1": "19501 19501 Biscayne Blvd Space",
    "city": "Aventurareaa",
    "region": "FL",
    "country": "US",
    "postalCode": "33180"
  },
  "validatedAddresses": [
    {
      "addressType": "HighRiseOrBusinessComplex",
      "line1": "19501 BISCAYNE BLVD SPACE 19501",
      "line2": "",
      "line3": "",
      "city": "AVENTURA",
      "region": "FL",
      "country": "US",
      "postalCode": "33180-2342",
      "latitude": 25.955884,
      "longitude": -80.14666
    }
  ],
  "coordinates": {
    "latitude": 25.955884,
    "longitude": -80.14666
  },
  "resolutionQuality": "Intersection",
  "taxAuthorities": [
    {
      "avalaraId": "16",
      "jurisdictionName": "FLORIDA",
      "jurisdictionType": "State",
      "signatureCode": "AKUY"
    },
    {
      "avalaraId": "413",
      "jurisdictionName": "MIAMI-DADE",
      "jurisdictionType": "County",
      "signatureCode": "ALDE"
    },
    {
      "avalaraId": "2001062471",
      "jurisdictionName": "MIAMI DADE CONVENTION DEVELOPMENT DISTRICT SP",
      "jurisdictionType": "Special",
      "signatureCode": "EOBY"
    },
    {
      "avalaraId": "2001062483",
      "jurisdictionName": "MIAMI DADE TOURISM DEVELOPMENT DISTRICT TL",
      "jurisdictionType": "Special",
      "signatureCode": "EOCQ"
    },
    {
      "avalaraId": "2001062545",
      "jurisdictionName": "MIAMI DADE PRO SPORTS FACILITIES DISTRICT SL",
      "jurisdictionType": "Special",
      "signatureCode": "EOFU"
    },
    {
      "avalaraId": "2001074462",
      "jurisdictionName": "AVENTURA",
      "jurisdictionType": "City",
      "signatureCode": "NDPS"
    }
  ],
  "isValidAddress": true
}
```

_Example Response With Invalid Address:_

```json
{
  "address": {
    "line1": "tester",
    "city": "Aventura",
    "region": "FL",
    "country": "US",
    "postalCode": "33180"
  },
  "validatedAddresses": [
    {
      "addressType": "UnknownAddressType",
      "line1": "tester",
      "line2": "",
      "line3": "",
      "city": "Aventura",
      "region": "FL",
      "country": "US",
      "postalCode": "33180",
      "latitude": 25.960861,
      "longitude": -80.138885
    }
  ],
  "coordinates": {
    "latitude": 25.960861,
    "longitude": -80.138885
  },
  "resolutionQuality": "Intersection",
  "messages": [
    {
      "summary": "An exact street name match could not be found",
      "details": "An exact street name match could not be found and phonetically matching the street name resulted in either no matches or matches to more than one street name.",
      "refersTo": "Address.Line0",
      "severity": "Error",
      "source": "Avalara.AvaTax.Common"
    }
  ],
  "isValidAddress": false
}
```

> ⚠️ _Please ensure that the country format is in ISO3, otherwise it will return false. This API only verifies addresses in USA or CAN_

### (Optional) Advanced configuration: Catalog Sync

Avalara provides an optional feature to store the items your store sells in their system. This enables you to configure your items' tax codes (and tariff codes, if you're selling into other countries) within Avalara's admin or through the Avalara API. Avalara will then use this information when calculating taxes for your transactions.

If you wish to use this feature, this app can automatically sync your VTEX catalog with Avalara. Any tax codes in your VTEX catalog will be sent to Avalara, and then additional management of tax and tariff codes can be done through the Avalara admin or API.

To enable this feature in the app:

1. Go to the `Avalara Tax Calculator` page in your VTEX admin, as described above.
2. Enter an [app key and token](https://developers.vtex.com/docs/getting-started-authentication#creating-the-appkey-and-apptoken) pair for your account in the VTEX App Key and VTEX App Token fields, if you haven't already done so.

> ⚠️ _Note: New VTEX App Keys grant zero permissions by default. The App Key used here must have the "Owner" role. [Learn more about how to generate App Keys and manage their permissions here.](https://help.vtex.com/en/tutorial/application-keys--2iffYzlvvz4BDMr6WGUtet#managing-app-key-permissions)_

3. Look for a setting labeled `Sync Catalog with Avalara` and set it to `Yes`.
4. A new option will appear below it, labeled `Product identifier for catalog sync`. This can be set to either `Product ID` or `Product Reference Code`. The identifier that you choose will be used as each product's "Item Code" in the Avalara system.
5. Click `Update` to save these settings.
6. A new button will appear labeled `Send full catalog to Avalara now`. Click this to perform an initial sync of your catalog with Avalara. You only need to do this once; any changes that you make to your VTEX catalog in the future will be automatically synced with Avalara.

### (Optional) Advanced Configuration: HS Code Classification

In the `Item Classification` Tab, when the following three fields (`Avalara Email`, `Avalara Password`, and `Select a Country to Generate HS Codes`) are entered, you can allow Avalara to generate HS codes for the selected country. Ensure that your account has Avalara's Item Classification API enabled and use the same `email` and `password` as that account. Creating and attaching HS Codes can take on average 72 to 120 hours to complete.

- > ⚠️ _This feature only generates Harmonized System (HS) codes for items that are **already in Avalara's catalog** and **does not contain an HS code**._
- > ⚠️ _Avalara may not generate HS codes for all items._
- > ⚠️ _If you select France, Germany, Italy, or Spain, the HS codes will all be the same. For example, there is no need to regenerate an HS Code for Germany if one already exists for Italy._

### (Optional) Advanced configuration: Tax Exempt Customers

In case you have customers with tax exemption certificates, there are three ways to handle this in your store so that they are not charged with sales tax. These options can be used individually or in conjunction:

- **Manage tax exemptions in Avalara's dashboard** - Avalara allows you to store and manage customer data in the Avalara dashboard. This includes storage of tax exemption certificates to keep track of which customers should be considered tax exempt. To use this feature, it's important that the Avalara app send the correct "customer code" when communicating with Avalara, so that the VTEX user can be matched to the Avalara customer record. By default, the Avalara app will send the user's email as their customer code, but the app can be configured to send a profile field from Master Data instead. You will find a dropdown for this on the VTEX Avalara admin page, labeled `Customer Code`.

- **Add the customer to the VTEX admin tax exemption table** - On the VTEX Avalara admin page, click on the `Exemptions` tab at the top of the page to access the exemptions interface. Here, you may click `+ NEW` to add a customer. You will need to input their email address and either a tax exemption certificate number or an entity code. Once a customer's information is saved in the table, they should not see any calculated tax when using checkout.

- **Collect the customer's tax exemption certificate during checkout** - You may customize your checkout to include an input field to collect a customer's tax exemption certificate number, as shown in the instructions below. Once this is implemented, a customer can apply their exemption certificate to an order and the tax calculation will immediately update to reflect that their order is now tax exempt. This certificate number is also sent to Avalara as part of the transaction data.

1. On the Avalara admin page, enter an [app key and token](https://developers.vtex.com/docs/getting-started-authentication#creating-the-appkey-and-apptoken) pair for your account in the VTEX App Key and VTEX App Token fields.
2. Update the [orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration) for your account using the following options:

```json
"apps": [
  {
    "id": "avalara",
    "fields": [
      "exemptionNumber"
    ]
  }
]
```

3. In the admin's Checkout section, access the `Código` (_code_) tab.
4. Add the following JavaScript to your `checkout6-custom.js` file:

```js
function updateOrderForm(method, exemptionNumber) {
  let orderFormID = vtexjs.checkout.orderFormId
  $.ajax({
    url:
      window.location.origin +
      '/api/checkout/pub/orderForm/' +
      orderFormID +
      '/customData/avalara/exemptionNumber',
    type: method,
    data: { value: exemptionNumber },
    success: function () {
      vtexjs.checkout.getOrderForm().done(function (orderForm) {
        if (orderForm.customData) {
          //doSomething()
          $('.tax-exemption__form').addClass('js-success')
        } else {
          //doSomethingElse()
          $('.tax-exemption__input').val('')
          $('.tax-exemption__form').removeClass('js-success')
        }
        //refresh the summary
        vtexjs.checkout.getOrderForm().then(function (orderForm) {
          var clientProfileData = orderForm.clientProfileData
          return vtexjs.checkout.sendAttachment(
            'clientProfileData',
            clientProfileData
          )
        })
      })
    },
  })
}

let taxExemptionFieldHtml = `
  <div class="tax-exemption">
    <p>Tax Exemption Certificate Number</p>
    <form class="tax-exemption__form">
      <input type="text" required maxlength="25" class="tax-exemption__input" name="tax-exemption__input"/>
      <input type="submit"  class="tax-exemption__button btn btn-primary" value="OK" />
      <button class="tax-exemption__button--remove">remove</button>
    </form>
  </div>
`

function taxExemptionBinds() {
  $('.tax-exemption__form').on('submit', function (e) {
    e.preventDefault()
    let exptN = $('.tax-exemption__input').val()
    if (exptN) updateOrderForm('PUT', exptN)
    return false
  })

  $('.tax-exemption__button--remove').on('click', function (e) {
    e.preventDefault()
    updateOrderForm('DELETE', '')
  })
}

function taxExemptionValidateForm(inputVal) {
  if (inputVal) {
    $('.tax-exemption__form').addClass('js-success')
    $('.tax-exemption__input').val(inputVal)
  }
}

function appendField() {
  if (
    ~window.location.hash.indexOf('#/payment') &&
    !$('.tax-exemption').length
  ) {
    let customTaxVal = vtexjs.checkout.orderForm?.customData
      ? vtexjs.checkout.orderForm.customData.customApps
        ? vtexjs.checkout.orderForm.customData.customApps.find(
            (app) => app.id == 'avalara'
          )
        : ''
      : ''
    customTaxVal = customTaxVal ? customTaxVal.fields.exemptionNumber : ''
    if (
      !customTaxVal &&
      !vtexjs.checkout.orderForm?.totalizers.find((x) => x.id === 'CustomTax')
    )
      return false
    $('#payment-data form.form-step.box-new').prepend(taxExemptionFieldHtml)
    taxExemptionValidateForm(customTaxVal)
    taxExemptionBinds()
  }
}

$(window).on('hashchange', function () {
  appendField()
})

$(window).load(function () {
  appendField()
})
```

4. Add the following CSS to your `checkout6-custom.css` file:

```css
.tax-exemption {
  margin-bottom: 10px;
}
.tax-exemption__form {
  display: flex;
}
.tax-exemption__button {
  margin-left: 10px;
  border-radius: 4px;
}

.tax-exemption__button--remove {
  margin-left: 10px;
  border-radius: 4px;
  background: transparent;
  border: none;
  color: #ff4c4c;
  display: none;
}

.tax-exemption__form.js-success {
}
.tax-exemption__form.js-success input.tax-exemption__input {
  border: none !important;
  box-shadow: none;
  pointer-events: none;
  font-weight: bold;
}
.tax-exemption__form.js-success .tax-exemption__button {
  display: none;
}
.tax-exemption__form.js-success .tax-exemption__button--remove {
  display: block;
  text-decoration: underline;
}
```

5. Save your changes.

### (Optional) Advanced configuration: Business VAT Numbers

You may customize your checkout to include an input field to collect a customer's business VAT number, as shown in the instructions below. Once this is implemented, a customer can apply their VAT number to an order and the tax calculation will immediately update to reflect the new taxes. This business VAT number is also sent to Avalara as part of the transaction data.

> ⚠️ _This currently only supports transactions between two European Union Member Countries._

> ⚠️ _For marketplace scenarios, we only support VAT exemptions for committed orders when Commit Origin is set to `Marketplace`. Invoices for seller transactions will not reflect the VAT exemptions._

1. On the Avalara admin page, enter an [app key and token](https://developers.vtex.com/docs/getting-started-authentication#creating-the-appkey-and-apptoken) pair for your account in the VTEX App Key and VTEX App Token fields.
2. Update the [orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration) for your account using the following options:

```json
// For just VAT Number
"apps": [
  {
    "id": "avalara",
    "fields": [
      "vatNumber"
    ]
  }
]

// For both VAT Number and Exemption Number
"apps": [
  {
    "id": "avalara",
    "fields": [
      "exemptionNumber",
      "vatNumber"
    ]
  }
]

```

3. In the admin's Checkout section, access the `Código` (_code_) tab.
4. Add the following JavaScript to your `checkout6-custom.js` file:

```js
function updateOrderFormVAT(method, vat) {
  let orderFormID = vtexjs.checkout.orderFormId
  $.ajax({
    url:
      window.location.origin +
      '/api/checkout/pub/orderForm/' +
      orderFormID +
      '/customData/avalara/vatNumber',
    type: method,
    data: { value: vat },
    success: function () {
      vtexjs.checkout.getOrderForm().done(function (orderForm) {
        if (orderForm.customData) {
          //doSomething()
          $('.business-vat__form').addClass('js-success')
        } else {
          //doSomethingElse()
          $('.vat-number__input').val('')
          $('.business-vat__form').removeClass('js-success')
        }
        //refresh the summary
        vtexjs.checkout.getOrderForm().then(function (orderForm) {
          var clientProfileData = orderForm.clientProfileData
          return vtexjs.checkout.sendAttachment(
            'clientProfileData',
            clientProfileData
          )
        })
      })
    },
  })
}

let vatFieldHtml = `
  <div class="vat-number">
    <p>Business VAT Number</p>
    <form class="business-vat__form">
      <input type="text" required maxlength="25" class="vat-number__input" name="vat-number__input"/>
      <input type="submit"  class="vat-number__button btn btn-primary" value="OK" />
      <button class="vat-number__button--remove">remove</button>
    </form>
  </div>
`

function vatBinds() {
  $('.business-vat__form').on('submit', function (e) {
    e.preventDefault()
    let vat = $('.vat-number__input').val()
    if (vat) updateOrderFormVAT('PUT', vat)
    return false
  })

  $('.vat-number__button--remove').on('click', function (e) {
    e.preventDefault()
    updateOrderFormVAT('DELETE', '')
  })
}

function vatValidateForm() {
  $('.business-vat__form').addClass('js-success')
}

function appendFieldVAT() {
  if (~window.location.hash.indexOf('#/payment') && !$('.vat-number').length) {
    $('#payment-data form.form-step.box-new').prepend(vatFieldHtml)
    vatValidateForm()
    vatBinds()
  }
}

$(window).on('hashchange', function () {
  appendFieldVAT()
})

$(window).load(function () {
  appendFieldVAT()
})
```

4. Add the following CSS to your `checkout6-custom.css` file:

```css
.vat-number {
  margin-bottom: 10px;
}
.business-vat__form {
  display: flex;
}
.vat-number__button {
  margin-left: 10px;
  border-radius: 4px;
}

.vat-number__button--remove {
  margin-left: 10px;
}

.vat-number__form.js-success input.vat-number__input {
  border: none !important;
  box-shadow: none;
  pointer-events: none;
  font-weight: bold;
}
.vat-number__form.js-success .vat-number__button {
  display: none;
}
.vat-number__form.js-success .vat-number__button--remove {
  display: block;
  text-decoration: underline;
}
```

5. Save your changes.

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->