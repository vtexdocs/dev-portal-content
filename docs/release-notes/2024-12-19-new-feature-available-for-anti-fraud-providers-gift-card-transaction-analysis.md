---
title: "New feature available for anti-fraud providers: Gift card transaction analysis"
slug: "2024-12-19-new-feature-available-for-anti-fraud-providers-gift-card-transaction-analysis"
hidden: false
type: "added"
createdAt: "2024-12-19T00:00:00.219Z"
updatedAt: "2024-12-19T00:00:00.219Z"
excerpt: "Gift card transactions can now be analyzed with anti-fraud."
---

Anti-fraud providers integrated with VTEX can now analyze payment transactions made with [gift cards](https://help.vtex.com/en/tutorial/gift-card--tutorials_995).

## What has changed?

The `allowAntifraudOnGiftCard` field was created within the [Anti-fraud Provider Protocol](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works), allowing anti-fraud providers to indicate whether they want to process gift card transaction data in a VTEX store.

Gift card transaction information is sent to providers through the [Send anti-fraud pre-analysis data (optional)](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/pre-analysis) or [Send anti-fraud data](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/transactions) endpoints, as in payment operations made by credit or debit card.

See an example of a payload sent on the [Send anti-fraud data](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#post-/transactions) endpoint, showing the gift card information in the payments object.

```json
…
"payments": [
    {
        "id": "DDB18D1721914346BF88EJ11B01C6312",
        "method": "GiftCard",
        "name": "Gift",
        "value": 395.71,
        "installments": 1,
        "details": {
            "address": {
                "country": "BRA",
                "street": "AV NEWTON DUARTE",
                "number": "321",
                "complement": "APTO 102",
                "neighborhood": null,
                "postalCode": "55555555",
                "city": "SAO PAULO",
                "state": "SP"
            },
            "giftCardId": "67",
            "redemptionToken": "FJPI***************",
            "redemptionCode": "FJPI***************",
            "provider": "VtexGiftCard"
        }
    }
]
…
```

> ℹ️ The information in the `"redemptionToken"` and `"redemptionCode"` fields is sent to anti-fraud providers only in masked format (****), preserving its security.

## What needs to be done?

To enable the gift card data analysis at your anti-fraud provider, follow the steps below:

1. Update your manifest to include the configuration `"allowAntifraudOnGiftCard": true`.
2. Open a ticket with [VTEX Support](https://help.vtex.com/support) requesting the provider integration update.
3. Contact VTEX merchants with whom you have contracts to inform them about the availability of this new anti-fraud analysis service.


> ⚠️ Learn more in the [Announcement Anti-fraud analysis for gift cards](https://help.vtex.com/en/announcements/anti-fraud-analysis-for-gift-cards).