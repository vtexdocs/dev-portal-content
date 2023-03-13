---
title: "Store setup for VTEX Marketplace"
slug: "external-seller-integration-vtex-marketplace-setup"
hidden: false
createdAt: "2020-09-01T13:44:53.826Z"
updatedAt: "2022-03-11T17:56:35.431Z"
---

For a VTEX store to act as a marketplace and sell products from external sellers, it has to do the following for each external seller:

- [Register the seller in the marketplace Admin](#register-the-seller-in-the-marketplace-admin)
- [Activate the seller for a trade policy](#activate-the-seller-for-a-trade-policy)
- [Set up API authentication credentials](#set-up-api-authentication-credentials)

This article explains what must be done to complete each of these configuration steps.

---

## Register the seller in the marketplace Admin

An external seller can only integrate into a VTEX store if it is registered there. The responsibility for creating this seller registration lies with the marketplace.

You can call the [Configure Seller Account](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/seller-register/pvt/sellers) to add the external seller through API.

The article [Configuring a seller](https://help.vtex.com/en/tutorial/configuring-the-seller--tutorials_392) shows the path to create the seller in the Admin and explains the form fields.

>ℹ️ The **Fulfillment Endpoint** field should be filled in with the endpoint that will be implemented for the seller to receive the Fulfillment Simulation requests from the marketplace. This implementation is explained in the next section of this guide.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-seller-integration-vtex-marketplace-setup-0.png)

[block:callout]
{
"type": "info",
"body": "The `seller ID`, created during this step, will be essential for the integration. Most of the API requests explained in the next section of this guide will use it to identify the seller."
}
[/block]

## Activate the seller for a trade policy

Trade policies are used in VTEX to group catalog, pricing, promotions, inventory, shipping, and payment settings for different sales channels. In a VTEX marketplace, each trade policy may apply to a different set of sellers. So, after creating a new seller, the marketplace needs to activate this seller for the trade policies that make sense for the business.

To do this, in the marketplace management panel's main menu, click on the option **Trade Policies**, then choose the trade policy you want to edit by clicking on the button **Alter** next to it. Next, select the sellers you want to activate. In the example of the image below, the trade policy "Marketplace" is only enabled for the seller "Store 1".

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/external-seller-integration-vtex-marketplace-setup-1.png)

Check out the Help Center documentation to get the complete explanation on how to [enable the seller for a trade policy](https://help.vtex.com/en/tutorial/configuring-the-seller--tutorials_392#editing-the-trade-policy).

## Set up API authentication credentials

Every private API request to the VTEX system requires authentication through a pair of appKey and appToken. So you will need to create these credentials before you can start building the integration.

Read the [Authentication guide](https://developers.vtex.com/docs/guides/getting-started-authentication#section-creating-the-appkey-and-apptoken) to learn how to create and use the appKey and appToken.

Once the authentication credentials are created, keep the appKey / appToken pair stored in a safe place until you can securely share it with the external seller.
