---
title: "Custom - Checkout UI Settings"
slug: "arcaplanetqa-checkout-v6-invoice-data"
excerpt: "arcaplanetqa.checkout-v6-invoice-data@0.0.2"
hidden: true
createdAt: "2022-07-27T13:17:57.532Z"
updatedAt: "2022-07-27T15:32:24.811Z"
---
1. [Available configuration parameters](#available-configuration-parameters)
1. [Modify app settings](#modify-app-settings)

## Available configuration parameters

- locale: language in which the form will be displayed.

  - type: string
  - expected values: en, es, fr, it, pl
  - default value: en

- invoiceDataMandatory: the billing information form must be completed as required.

  - type: boolean
  - expected values: true, false
  - default value: false

- showSDIPECSelector **(only available for Italy)**: show or hide the SDI / PEC document selector.

  - type: boolean
  - expected values: true, false
  - default value: true

- defaultSDIPEC **(only available for Italy)**: when the form is loaded, the indicated value will appear selected by default.

  - type: string
  - expected values: sdi, pec
  - default value: pec

- showPersonTypeSelector: show or hide the person type selector. If this selector is hidden, the value for defaultPersonType must be mandatory.

  - type: boolean
  - expected values: true, false
  - default value: true

- defaultPersonType: when the form is loaded, the indicated value will appear selected by default.

  - type: string
  - expected values: private, company
  - default value: empty

- autocompleteNameSurname: the name and surname fields of the billing form will be completed with the values of the profile form.

  - type: boolean
  - expected values: true, false
  - default value: true

- hidePersonalData: the personal data of the billing form will not be displayed, only the billing address will appear.

  - type: boolean
  - expected values: true, false
  - default value: false

- companyMessage: the content of this message will be displayed if the customer type "company" is chosen.

  - type: string
  - expected values: text or html content
  - default value: empty

- invoiceMandatoryPostalCodes: if the client chooses any of the postal codes included in this array, they must complete the billing form as required.

  - type: array
  - expected values: ['12345', '5678']
  - default value: empty

- defaultSameShippingAddress: The checkbox that determines whether the same address is used for billing and shipping will be checked or unchecked depending on the value of this property.

  - type: boolean
  - expected values: true, false
  - default value: true

- requiredFields: contains the required fields by language and form within the billing form

  - type: object
  - expected values: true, false
  - default value:

  ```js
  {
    en: {
      profile: [
        'user-person-type',
        'custom-corporate-name',
        'custom-corporate-document'
      ],
      address: [
        'custom-corporate-street',
        'custom-corporate-number',
        'custom-corporate-postal-code',
        'custom-corporate-city',
        'custom-corporate-state'
      ]
    },
    fr: {
      profile: [
        'user-person-type',
        'custom-corporate-name',
        'custom-corporate-document'
      ],
      address: [
        'custom-corporate-street',
        'custom-corporate-number',
        'custom-corporate-city',
        'custom-corporate-postal-code'
      ]
    },
    es: {
      profile: [
        'user-person-type',
        'custom-corporate-name',
        'custom-corporate-document'
      ],
      address: [
        'custom-corporate-street',
        'custom-corporate-number',
        'custom-corporate-postal-code',
        'custom-corporate-city',
        'custom-corporate-state'
      ]
    },
    it: {
      profile: [
        'user-person-type',
        'custom-corporate-name',
        'custom-corporate-document',
        'custom-corporate-document2'
      ],
      address: [
        'user-country',
        'custom-corporate-street',
        'custom-corporate-number',
        'custom-corporate-postal-code',
        'custom-corporate-city',
        'custom-corporate-state'
      ]
    },
    pl: {
      profile: [
        'user-person-type',
        'custom-corporate-name',
        'custom-corporate-document'
      ],
      address: [
        'custom-corporate-street',
        'custom-corporate-number',
        'custom-corporate-city',
        'custom-corporate-postal-code'
      ]
    }
  }
  ```

## Modify app settings

In your client's administrator, within the Checkout UI Custom section (_/admin/vtex-checkout-ui-custom/_), you must go to the "Javascript" section and include a script with the following function modifying the necessary parameters for your needs:

```js
// This is an example
function setVtexAppsConfig(vtexAppsConfig, appName) {
  if (appName == "checkout-v6-invoice-data") {
    vtexAppsConfig.locale = "it";
    vtexAppsConfig.invoiceDataMandatory = true;
    vtexAppsConfig.showPersonTypeSelector = false;
    vtexAppsConfig.defaultPersonType = "company";
    vtexAppsConfig.companyMessage = "<p>Example message</p>";
    vtexAppsConfig.requiredFields.it = {
      profile: ["user-person-type", "custom-corporate-name"],
      address: ["custom-corporate-street"],
    };
  }
}
```