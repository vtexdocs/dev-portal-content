---
title: "Payments"
slug: "vtex-innoship-technical-documentation"
excerpt: "vtex.innoship@2.2.2"
hidden: true
createdAt: "2022-08-08T11:00:55.314Z"
updatedAt: "2022-08-08T11:00:55.314Z"
---
Payment types are identified by checking `order.paymentData -> transactions -> payments`.

1. Card payment if the `firstDigits` property is not `null`
2. OP payment if the `group` property is set to `promissory`
3. Cash payment if the `group` property is set to `cash`

## Errors

* `Value of field ExternalClientLocation is not valid` - represents the warehouse ID declared in VTEX 
  under `ORDERS > Inventory & shipping > Shipping strategy > Warehouses`.<br>
  In the Innoship Web Application, under `Locations & Carriers`, this VTEX warehouses Is must be associated to a 
  location's `External Location Id`.<br>
  Each active warehouse ID declared in VTEX must have a correspondence in the Innoship Web Application's `Locations & Carriers`,
  via the `External Location Id`.