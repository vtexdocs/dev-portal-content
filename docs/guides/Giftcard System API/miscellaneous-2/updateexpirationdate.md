---
title: "Update Expiration Date"
slug: "updateexpirationdate"
excerpt: "This endpoint is used to update an existing Gift Card's expiration date."
hidden: true
createdAt: "2019-12-24T01:18:57.539Z"
updatedAt: "2020-02-13T14:24:21.819Z"
---
-------------------------------------
PARAMETERS
[block:parameters]
{
  "data": {
    "0-0": "`cardId`",
    "0-1": "string",
    "0-2": "Giftcard ID",
    "h-0": "Attributes",
    "h-1": "Type",
    "h-2": "Description"
  },
  "cols": 3,
  "rows": 1
}
[/block]
ARGUMENTS
[block:parameters]
{
  "data": {
    "0-0": "`expiringDate`",
    "0-1": "string",
    "0-2": "**Required**. New Date - *Format: aaaa-mm-dd*",
    "h-0": "Attributes",
    "h-1": "Type",
    "h-2": "Description"
  },
  "cols": 3,
  "rows": 1
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
    "1-2": "Redemption code",
    "2-0": "`balance`",
    "2-1": "integer",
    "2-2": "Giftcard value",
    "3-0": "`cardName`",
    "3-1": "string",
    "3-2": "Giftcard name",
    "4-0": "`emissionDate`",
    "4-1": "date",
    "5-1": "integer",
    "5-0": "`expiringDate`",
    "4-2": "Giftcard emission date",
    "5-2": "Giftcard expiration date",
    "6-0": "`multipleCredits`",
    "6-1": "boolean",
    "6-2": "Allows gifcard multiple credit input",
    "7-0": "`multipleRedemptions`",
    "7-1": "boolean",
    "7-2": "Allows giftcard multiple usage",
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
    "h-1": "Type"
  },
  "cols": 3,
  "rows": 12
}
[/block]