---
title: "Payments"
slug: "evonomix-postis-technical-documentation"
excerpt: "evonomix.postis@1.0.1"
hidden: true
createdAt: "2022-08-09T13:19:56.891Z"
updatedAt: "2022-08-09T13:19:56.891Z"
---
Payment types are identified by checking `order.paymentData -> transactions -> payments`.

1. Card payment if the `firstDigits` property is not `null`
2. OP payment if the `group` property is set to `promissory`
3. Cash payment if the `group` property is set to `cash`

## Errors

* `Value of field ExternalClientLocation is not valid` - represents the warehouse ID declared in VTEX 
  under `ORDERS > Inventory & shipping > Shipping strategy > Warehouses`.<br>
  In the Postis Web Application, under `Locations & Carriers`, this VTEX warehouses Is must be associated to a 
  location's `External Location Id`.<br>
  Each active warehouse ID declared in VTEX must have a correspondence in the Postis Web Application's `Locations & Carriers`,
  via the `External Location Id`.