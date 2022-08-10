---
title: "Add / Remove Credit to Giftcard"
slug: "addremovecredittogiftcard"
excerpt: "The customer can add or remove credit to a existing Gift Card."
hidden: true
createdAt: "2019-12-24T01:18:57.539Z"
updatedAt: "2020-02-13T14:24:21.730Z"
---
This endpoint can be used for two different actions:

* Add credit; 
* Remove credit.

In each case, you should complete the body with the respective values.

Check the examples below:

**ADD CREDIT**
 ```
{
   "description": "Adiciona R$10,00",
   "value": 1000
 }
```

**REMOVE CREDIT**
```
 {
   "description": "Debita R$10,00",
   "value": **-**1000
 }
```

PARAMETERS
[block:parameters]
{
  "data": {
    "h-0": "Attributes",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`cardId`",
    "0-1": "string",
    "0-2": "**Required**. Giftcard ID"
  },
  "cols": 3,
  "rows": 1
}
[/block]
ARGUMENTS
[block:parameters]
{
  "data": {
    "0-0": "`description`",
    "0-1": "string",
    "0-2": "Transaction description",
    "1-0": "`value`",
    "1-1": "string",
    "1-2": "**Required**. Value to add or remove from Giftcard | *Add (positive value) - Remove (negative value)*",
    "h-0": "Attributes",
    "h-1": "Type",
    "h-2": "Description"
  },
  "cols": 3,
  "rows": 2
}
[/block]
ATTRIBUTES
[block:parameters]
{
  "data": {
    "0-0": "`id`",
    "0-1": "integer",
    "0-2": "Giftcard ID",
    "1-0": "`redemptionCode`",
    "1-1": "string",
    "1-2": "Redemption Code",
    "2-0": "`balance`",
    "2-1": "integer",
    "2-2": "Giftcard Value",
    "3-0": "`cardName`",
    "3-1": "string",
    "3-2": "Giftcard Name",
    "4-0": "`emissionDate`",
    "4-1": "date",
    "4-2": "Giftcard Emission date",
    "5-0": "`expiringDate`",
    "5-1": "integer",
    "5-2": "Giftcard Expiration date",
    "6-0": "`multipleCredits`",
    "6-1": "boolean",
    "6-2": "Allows Giftcard multiple credit input",
    "7-0": "`multipleRedemptions`",
    "7-1": "boolean",
    "7-2": "Allows Giftcard multiple usage",
    "8-0": "`customerId`",
    "8-1": "string",
    "8-2": "Giftcard's owner client profile ID",
    "9-0": "`restrictedToOwner`",
    "9-1": "boolean",
    "9-2": "Is restricted?",
    "10-0": "`statusId`",
    "10-1": "integer",
    "10-2": "Giftcard status",
    "11-0": "`caption`",
    "11-1": "string",
    "11-2": "Giftcard description",
    "h-0": "Attributes",
    "h-2": "Description",
    "h-1": "Type"
  },
  "cols": 3,
  "rows": 12
}
[/block]