---
title: "Store setup for VTEX Seller"
slug: "external-marketplace-integration-vtex-seller-setup"
hidden: false
createdAt: "2020-09-01T21:52:08.310Z"
updatedAt: "2021-07-19T18:29:44.841Z"
---

For a VTEX store to act as a seller, it has to do the following for each external marketplace:

- [Define channel settings](#define-channel-settings)
- [Set up catalog notifications](#set-up-catalog-notifications)
- [Set up API authentication credentials](#set-up-api-authentication-credentials)

This article explains what must be done to complete each of these configuration steps.

---

## Define channel settings

[Trade policies](https://help.vtex.com/en/tutorial/creating-a-trade-policy--563tbcL0TYKEKeOY4IAgAE) are used in VTEX to group catalog, pricing, promotions, inventory, shipping and payments settings for different sales channels. The sections that follow describe where you can use trade policies in each of these modules.

Once all the channel settings that should be applied to the marketplace are grouped under a single trade policy, take note of the trade policy ID before you move on to the next step.
[block:callout]
{
"type": "info",
"body": "Multiple sales channels can share the same settings by using the same trade policy. [Request a new trade policy](https://help.vtex.com/en/faq/how-to-configure-a-new-trade-policy--frequentlyAskedQuestions_700) to be able to differentiate settings per sales channel."
}
[/block]

### Catalog

When [adding products to your catalog](https://help.vtex.com/en/tracks/catalog-101--5AF0XfnjfWeopIFBgs3LIQ/1ROhz3Y7mfSMmCO1I1GxEL), you may restrict their availability to certain trade policies. If no restriction is made, the product will be available in all sales channels.
![Catalog: products may be restricted to certain trade policies](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-vtex-seller-setup-0.png)
In the example above, the product will be available only to the sales channels using the **B2C - USA** and **Marketplace - USA** trade policies.

### Pricing

When setting prices for your products, keep in mind that each trade policy is created with its own [price table](https://help.vtex.com/en/tracks/prices-101--6f8pwCns3PJHqMvQSugNfP/1wAm5m3IUfIj6maBdaRJt8). To differentiate prices between your sales channels, you may use:

- [Price rules](https://help.vtex.com/tracks/prices-101--6f8pwCns3PJHqMvQSugNfP/2rBirbpB7wLnei4dQ9KGMW) to set a different markup for specific categories / brands
- [Fixed prices](https://help.vtex.com/tracks/prices-101--6f8pwCns3PJHqMvQSugNfP/3HxF2u5VwidqnUGnFoKdDy) to set a different price for specific products
  ![Prices: define price rules or fixed prices to differentiate prices](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-vtex-seller-setup-1.png)
  In the example above, a price rule applied an additional 10% markup to the **B2C - USA** trade policy and a fixed price of $ 500.00 was set in the **Marketplace - USA** trade policy for SKU 14.
[block:callout]
{
  "type": "info",
  "body": "Read about our [pricing system architecture](https://help.vtex.com/tracks/prices-101--6f8pwCns3PJHqMvQSugNfP/7GptzvlPDVM11ojEjywIQx) if these concepts are unfamiliar to you."
}
[/block]

### Promotions

When creating promotions as a seller, you may restrict their availability to certain trade policies. If no trade policy is selected, the promotion will be available in all sales channels. The origin must be set as **Fulfillment / Delivered by me** in all promotions you offer as a seller.
![Promotions: must be set as fulfillment, may be restricted to certain trade policies](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-vtex-seller-setup-2.png)

In the example above, the promotion will be applied only to **Marketplace - USA** orders where the store is acting as a seller. The promotion will *not* be available in the VTEX storefront.

### Inventory

When defining your shipping strategy, you may restrict the [logistics routes](https://help.vtex.com/en/tracks/logistics-101--13TFDwDttPl9ki9OXQhyjx/1xo0jmMDcnAUU5ZOavdQ7M) available to certain trade policies through loading docks. Each loading dock linked to a trade policy makes inventory available through the warehouses connected to it.
![Inventory: warehouse must be connected to loading docks available to the trade policy](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-vtex-seller-setup-3.png)
In the example above, a warehouse is connected to the **Main Warehouse Dock**. This makes its inventory available to all trade policies linked to that loading dock.

### Shipping

When defining your shipping strategy, you may restrict the [logistics routes](https://help.vtex.com/en/tracks/logistics-101--13TFDwDttPl9ki9OXQhyjx/1xo0jmMDcnAUU5ZOavdQ7M) available to certain trade policies through loading docks. Each loading dock linked to a trade policy makes carriers and pick-up points available through the shipping policies connected to it.
![Shipping: shipping policies must be connected to loading docks available to the trade policy](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-vtex-seller-setup-4.png)
In the example above, the loading dock is linked to **B2C - USA** and **Marketplace - USA**. This makes its associated shipping policies available to those trade policies.

### Payment

When [creating a payment condition](https://help.vtex.com/en/tracks/payments--6GAS7ZzGAm7AGoEAwDbwJG/6bzGxlz4inf8sKmvZ1c7i3), you may restrict its availability to certain trade policies through [special conditions](https://help.vtex.com/en/tutorial/special-conditions--tutorials_456). If no restriction is made, it will be available in all sales channels.
![Payment: payment conditions may be restricted to certain trade policies](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-marketplace-integration-vtex-seller-setup-5.png)
In the example above, the payment condition is linked to **Marketplace - USA**. This makes it available only to the sales channels associated with this trade policy.

## Set up catalog notifications

Affiliates are used in VTEX to broadcast catalog notifications to marketplaces and other external services. These include changes in product information, price and quantity in stock.

To create an affiliate for an external marketplace, go to the *Orders > Orders management > Settings* section of your Admin, select the *Affiliates* tab and click on the *New affiliate* button. Then fill out the form according to the table below:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "Name",
    "0-1": "Marketplace display name in orders management",
    "1-0": "ID",
    "2-0": "Trade Policy",
    "3-0": "E-mail for notifications",
    "4-0": "Search Endpoint",
    "1-1": "3-consonant identifier for marketplace orders",
    "2-1": "ID of the trade policy [defining channel settings](#define-channel-settings)",
    "3-1": "E-mail address that will receive error notifications",
    "4-1": "URL of the marketplace endpoint that will receive catalog notifications"
  },
  "cols": 2,
  "rows": 5
}
[/block]
Once the affiliate is created, take note of the affiliate ID before you move on to the next step.
[block:callout]
{
"type": "info",
"body": "If the external marketplace connector is still under development, you may postpone filling out the *Search Endpoint* field until its [catalog notification endpoint](#) is available."
}
[/block]

## Set up API authentication credentials

To allow the external marketplace connector to authenticate and interact  with your account through API calls, you will need to [create an appKey / appToken](https://developers.vtex.com/docs/guides/getting-started-authentication#creating-the-appkey-and-apptoken) with the **IntegrationProfile - Fulfillment Gateway Oms** [role](https://help.vtex.com/en/tutorial/access-profiles--7HKK5Uau2H6wxE1rH5oRbc#integrationprofile-fulfillment-gateway-oms) or equivalent.

Once the authentication credentials are created, take note of the appKey / appToken pair so you can share it with the external marketplace.
[block:callout]
{
"type": "warning",
"body": "For a matter of safety, the appToken is only shown once after you create it. Copy this token, save it in a safe place and share it only with the external marketplace.",
"title": ""
}
[/block]

## Wrapping up

If you have done things correctly, you should be able to provide the following [seller registration](https://developers.vtex.com/docs/external-marketplace-integration-connector#seller-registration) details to the external marketplace connector:

- Account Name
- Affiliate ID
- API Credentials
- Trade Policy ID
