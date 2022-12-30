---
title: "Recommendations"
slug: "external-marketplace-integration-recommendations"
hidden: false
createdAt: "2021-09-02T20:37:43.701Z"
updatedAt: "2021-09-02T20:37:56.501Z"
---
To avoid processing gaps due to the big volume of information of the initial load of products, we recommend:



- Using an async messaging architecture, using individual queues by context and store.  
- Creating mechanisms that respect the marketplace API limit rates. We suggest the standard use of the _Circuit Breaker_ integration.  
- In case any of the steps listed above presents failures in communication, we suggest using the contingency mechanism of _deadLetters_.  
- Being TotalReader: whenever possible, in the data transformation process, using standard values accepted by the marketplace, in case the information is not filled or sent by VTEX.  
- In case the marketplace’s processing is in lots - meaning that the connector assembles a group of SKUs, guaranteeing the the limit of records per lot is respected, according to marketplace riles, and sending them to the marketplace at once - it is fundamental to control the lot’s processing, to avoid sending SKU updates without making sure that the product exists in the marketplace.  
- Keeping a states table to know which SKUs have not been integrated with success, attempt date and the response received. This allows the system to use the contingency flow effectively, avoiding infinite loops, and avoiding reaching the request limit.