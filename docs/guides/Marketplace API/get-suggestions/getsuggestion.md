---
title: "Get SKU Suggestion by ID"
slug: "getsuggestion"
excerpt: "This endpoint retrieves the data of a specific SKU sent by the seller, to the marketplace. Marketplaces or external matchers can call this endpoint when they want to check the information about a single SKU. \n\nNote that all the information sent by the seller will be in the [content] object. All remaining information in this endpoint's response is given by the Matcher. \n\nMatcher rates received SKUs by correlating the data sent by sellers, to existing fields in the marketplace. The calculation of these scores determines whether the product has been: \n\n`Approved`: score equal to or greater than 80 points. \n\n`Pending`: from 31 to 79 points.\n\n`Denied`: from 0 to 30 points. \n\nNote that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score."
hidden: false
createdAt: "2021-11-09T18:52:06.556Z"
updatedAt: "2021-11-09T18:52:06.556Z"
---
