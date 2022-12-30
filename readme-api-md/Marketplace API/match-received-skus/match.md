---
title: "Match Received SKUs individually"
slug: "match"
excerpt: "All SKUs sent from a seller to a marketplace must be reviewed and matched. Actions in the matching process are added in the request body through the [matchType] object. Match type actions include: \n\n1. `newproduct`: match the SKU as a new product. \n\n2. `itemMatch`: associate the received SKU to an existing SKU. \n\n3. `productMatch`: associate the received SKU to an existing product. \n\n4. `deny`: deny the received SKU. \n\n5. `pending`: the received SKU requires attention. \n\n6. `incomplete`: the received SKU is lacking information to be matched. \n\n7. `insufficientScore`: the score given by the Matcher to this received SKU doesn't qualify it to be matched. \n\nNote that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score."
hidden: false
createdAt: "2021-11-09T18:52:06.558Z"
updatedAt: "2021-11-09T18:52:06.558Z"
---
