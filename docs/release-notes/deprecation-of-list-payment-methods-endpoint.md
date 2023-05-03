---
slug: "deprecation-of-list-payment-methods-endpoint"
title: "Deprecation of List Payment Methods endpoint"
excerpt: "VTEX will deprecate the List Payment Methods endpoint. The List Payment Provider will replace it."
createdAt: 2023-05-03T12:00:00.000Z
hidden: false
type: "added"
---

The **List Payment Methods endpoint** (route `https://{providerApiEndpoint}/payment-methods`) is being deprecated as it provides the same response information as the [List Payment Provider Manifest endpoint](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest).

From now on, when you need to check payment information (methods, types, and countries) that are applicable to a specific payment provider, you should use the [List Payment Provider Manifest endpoint](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#get-/manifest).