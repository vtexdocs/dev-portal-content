---
title: "B2B Seller Price"
slug: "seller-price"
hidden: true
createdAt: "2021-11-08T16:34:25.542Z"
updatedAt: "2022-06-13T16:08:09.500Z"
---
[block:callout]
{
  "type": "info",
  "body": "This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests)."
}
[/block]
In B2B commerce, it is often necessary to offer personalized prices. For example, in the commercial relationship between a distributor (seller) and different supermarkets (buyers), there might be specific price deals in place for each supermarket. In this case, the distributor (seller) needs to set specific prices for each customer.

This scenario gets more complex when the seller’s products are offered in a B2B marketplace, since marketplaces usually centralize the relationship with customers.

Considering this, our B2B Seller Price feature allows sellers from B2B marketplaces to configure specific price tables for each customer, based on their email address, and apply these personalized prices using [Pricing Hub](https://developers.vtex.com/vtex-rest-api/reference/pricing-hub-overview). This feature works for all types of sellers in the B2B scenario, whether they are white label or not.


## How it works

The diagram below shows how the process works, after all the required [configurations](#setup). 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/32e8e14-image1.png",
        "image1.png",
        997,
        619,
        "#f7f7f7"
      ]
    }
  ]
}
[/block]
When a customer logs in on a B2B marketplace which has Pricing Hub enabled, it will make a `POST` [Get Prices](https://developers.vtex.com/vtex-rest-api/reference/post_api-pricing-hub-prices) request to the Pricing Hub API to fetch prices information from the B2B Seller’s external prices app. The app will then return the prices information in the response, applying the specific prices associated with each customer email, as set by the seller.


## Setup

To set up this process, the marketplace and each seller must follow the instructions below.


### Marketplace

The marketplace must follow the steps below to activate the B2B Seller Price:

1. Contact our [Support](https://support.vtex.com/hc/en-us/requests) and open a request to enable Pricing Hub on the marketplace and seller accounts.
2. Enable the use of external prices by the seller through the `PUT` [Configure External Price Source](https://developers.vtex.com/vtex-rest-api/reference/configexternalpricesource) of the Pricing Hub API.
3. Allow VTEX to share customers’ email addresses with the seller. To do so, it is necessary to set `'AllowEmailSharing'` as the value for the TrustPolicy field in the `POST` [Create Seller](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-seller#catalog-api-post-seller) or `PUT` [Update Seller](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-seller#catalog-api-put-seller) endpoints of the Catalog API.
[block:callout]
{
  "type": "info",
  "body": "Make sure to manage the relationship between the marketplace’s catalog and the sellers’ catalogs in the Received SKUs page. Read the article on [Cataloging received SKUs](https://help.vtex.com/en/tutorial/manual-sku-cataloging--tutorials_396) for more information on this process."
}
[/block]

### Seller

The B2B sellers – white label or not – who want to use this feature must follow the instructions below.

1. Configure specific price tables associated with the customers’ respective email addresses, either using the [Pricing API](https://developers.vtex.com/vtex-rest-api/reference/pricing-api-overview) or the [VTEX Admin panel](https://help.vtex.com/en/tutorial/configurar-price-tables-especificas--5S9oDOMHNmY4K0kAewAiWY).
2. Develop a VTEX IO app to allow querying price tables by email, integrating with external price systems, and install it in the master workspace.

    We offer a reference implementation template to simplify this process: [Node template](https://github.com/vtex/unilever-external-prices-node). This template app can be customized to use other price parameters, by following the instructions on the app repository.

    Make sure your app complies with the [specifications detailed in the Pricing Hub documentation](https://developers.vtex.com/vtex-rest-api/reference/pricing-hub-overview#specifications).

[block:callout]
{
  "type": "warning",
  "body": "Pricing Hub only recognizes the master workspace. This means linking it to a test workspace will not work. For more information on the different types of workspaces, read our [Workspace](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-workspace) documentation."
}
[/block]

## Learn more

* [Pricing Hub - Overview](https://developers.vtex.com/vtex-rest-api/reference/pricing-hub-overview)
* [Pricing Hub - Get Prices](https://developers.vtex.com/vtex-rest-api/reference/post_api-pricing-hub-prices)