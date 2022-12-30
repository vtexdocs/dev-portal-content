---
title: "Get all SKU suggestions"
slug: "getsuggestions"
excerpt: "This endpoint retrieves a list of all SKUs sent by the seller for the Marketplace's approval. Marketplace operators should use this endpoint whenever they want to check the full list of received SKUs and their  information. \n\nNote that all the information sent by the seller will be in the [content] object. All remaining information in this endpoint's response is given by the Matcher. \n\nMatcher rates received SKUs by correlating the data sent by sellers, to existing fields in the marketplace. The calculation of these scores determines whether the product has been: \n\n`Approved`: score equal to or greater than 80 points. \n\n`Pending`: from 31 to 79 points.\n\n`Denied`: from 0 to 30 points. \n\nNote that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score."
hidden: false
createdAt: "2021-11-09T18:52:06.555Z"
updatedAt: "2021-11-09T18:52:06.555Z"
---
