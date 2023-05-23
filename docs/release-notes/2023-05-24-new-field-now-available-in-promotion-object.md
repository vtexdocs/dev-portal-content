---
title: New field now available in Promotion object
slug: "new-field-now-available-in-promotion-object"
hidden: false
type: "added"
excerpt: "The field `nominalDiscountType` has been added to the promotion object."
createdAt: "2023-04-23T14:47:00.000Z"
---

The field `nominalDiscountType` has been added to the promotion object. This field accepts two string values:

- **Item:** This option applies the intended nominal discount on every item present on the cart.
- **Cart:** This option keeps the behavior as it currently, the cart receives a nominal discount that is distributed among the items.

The following endpoints have been updated with the addition of the new field:

- [GET: Get All Promotions](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#get-/api/rnb/pvt/benefits/calculatorconfiguration)
- [GET: Get Promotion or Tax by ID](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#get-/api/rnb/pvt/calculatorconfiguration/-idCalculatorConfiguration-)
- [POST: Create or update Promotion or Tax](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#post-/api/rnb/pvt/calculatorconfiguration)
- [GET: List Archived Promotions](https://developers.vtex.com/docs/api-reference/promotions-and-taxes-api#get-/api/rnb/pvt/archive/benefits/calculatorConfiguration)
