---
title: "Request SKU review from seller"
slug: "request-sku-review"
excerpt: "The **Review Received SKUs** API allows marketplace operators to request sellers to review the sent SKUs that were either refused or pending approval. This endpoint allows marketplace operators to point out the exact fields that need sellers’ review, for a specific SKU.  \n\nNote that only one request per SKU is allowed. After operators submitted their first request through this call’s operation, another request can’t be executed in sequence. Operators must wait for the seller to update the SKU in question, and then submit another request, if necessary. Thus, be mindful that you won’t be able to update that initial request. \n\nOperators can add as many custom fields to their request body as they like. The field’s names can also be customized, so sellers know exactly what fields need their review."
hidden: false
createdAt: "2020-12-18T21:45:22.149Z"
updatedAt: "2020-12-18T21:45:22.149Z"
---
