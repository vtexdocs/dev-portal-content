---
title: "List Giftcard"
slug: "listgiftcard"
excerpt: "This API lists all the gift cards created by single customer.\r\n\r\nThis being said, it's really import to emphasize that the API does not lists all the store's Gift Cards."
hidden: true
createdAt: "2019-12-24T01:18:57.539Z"
updatedAt: "2020-02-13T14:24:21.543Z"
---
To complete this endpoint, you must collect the variable `customerId` in the Master Data - VTEX's database. 

After getting the variable, you should work the API just fine. 

For a reasonable response, expect a 200 OK.

PARAMETERS
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`customerId`",
    "0-1": "string",
    "0-2": "Gift Card's owner profile ID"
  },
  "cols": 3,
  "rows": 1
}
[/block]
ARGUMENTS
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`description`",
    "0-1": "string",
    "0-2": "Transaction Description",
    "1-0": "`value`",
    "1-1": "string",
    "1-2": "Required. Value to add or remove from Gift Card."
  },
  "cols": 3,
  "rows": 2
}
[/block]
ATTRIBUTES
[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "`id`",
    "0-1": "integer",
    "0-2": "Giftcard ID",
    "1-0": "`redemptionCode`",
    "2-0": "`balance`",
    "3-0": "`cardName`",
    "4-0": "`emissionDate`",
    "1-1": "string",
    "1-2": "Redemption Code",
    "2-1": "integer",
    "2-2": "Giftcard Value",
    "3-1": "string",
    "3-2": "Giftcard Name",
    "4-1": "date",
    "4-2": "Giftcard Emission Date",
    "5-0": "`expiringDate`",
    "5-1": "integer",
    "5-2": "Giftcard Expiration date",
    "7-0": "`multipleCredits`",
    "7-1": "boolean",
    "7-2": "Allows Giftcard multiple usage",
    "8-0": "`customerId`",
    "6-0": "`multipleCredits`",
    "6-1": "boolean",
    "6-2": "Allows giftcard multiple credit input",
    "8-1": "string",
    "8-2": "Giftcard's owner client profile ID",
    "9-0": "`restrictedToOwner`",
    "9-1": "boolean",
    "9-2": "Is restricted?",
    "10-0": "`statusId`",
    "10-1": "integer",
    "10-2": "Giftcard Status",
    "11-0": "`caption`",
    "11-1": "string",
    "11-2": "Giftcard Description"
  },
  "cols": 3,
  "rows": 12
}
[/block]