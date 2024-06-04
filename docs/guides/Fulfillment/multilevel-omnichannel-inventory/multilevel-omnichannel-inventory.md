---
title: "Multilevel Omnichannel Inventory"
slug: "multilevel-omnichannel-inventory"
hidden: false
createdAt: "2022-09-30T21:56:06.725Z"
updatedAt: "2023-04-19T19:15:33.816Z"
---

A [marketplace](https://help.vtex.com/pt/tutorial/estrategias-de-marketplace-na-vtex--tutorials_402) is the environment where the product is sold, or the storefront. The [seller](https://help.vtex.com/en/tutorial/estrategias-de-marketplace-na-vtex--tutorials_402#selling-on-marketplaces) owns the product and is responsible for fulfillment. [VTEX promotes digital collaboration](https://vtex.com/us-en/ecommerce-marketplace/) by allowing multiple combinations of architecture between these two entities. One of these combinations is called [Multilevel Omnichannel Inventory](https://help.vtex.com/pt/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4).

*Multilevel Omnichannel Inventory* is the VTEX setting that allows [franchises](https://help.vtex.com/en/tutorial/o-que-e-conta-franquia--kWQC6RkFSCUFGgY5gSjdl) or [white label sellers](https://help.vtex.com/en/tutorial/white-label-seller--5orlGHyDHGAYciQ64oEgKa)' inventory to be sold in marketplaces to which the main account is connected.

For VTEX sellers, this means being able to sell products from its franchises or white label sellers in a marketplace, without the need to set up the integration with the desired marketplace for all franchise stores, and white label sellers.

For marketplaces, this means selling products from its direct sellers and also physical stores and white label sellers associated with those sellers in a scalable way.

This article covers the account architecture details, chain order flows and necessary settings for VTEX marketplaces to implement this feature via API. 

>⚠️ To know how to implement this feature via VTEX Admin, along with benefits and restrictions around the use of Multilevel Omnichannel Inventory, check out our [Multilevel Omnichannel Inventory Help article](https://help.vtex.com/pt/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4).

## Account architecture

When a store sells its products in a marketplace, we have a one-level relationship between seller and marketplace. However, VTEX's architecture allows stores to act as both sellers and marketplaces, expanding the number of possible combinations.

Stores that have white label sellers and franchises are marketplaces to those accounts. But they can also be connected to external marketplaces, becoming sellers themselves. In this case, we have a three level architecture, as illustrated in the image below.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/multilevel-omnichannel-inventory-0.png)

- **Marketplace (level 1):** storefront where the product is sold and order is placed.
- **Direct seller (level 2):** main account, integrated to the marketplace level 1. Serves as a marketplace for white label sellers, franchise accounts and physical stores connected to it.
- **Franchise accounts/physical stores (level 3):** owns the product, and is responsible for fulfillment. Connected as white label sellers to the main account.

With the Multilevel Omnichannel Inventory setting, all franchise accounts and white label sellers (level 3) are already fully integrated to a store's main account (level 2). This means that when the main account sets up an integration with an external marketplace (level 1), the franchise accounts can be integrated as well, no longer being necessary to manage each franchise individually in order to set up its integration with the marketplace.

>ℹ️ This feature is valid for [VTEX marketplaces](https://help.vtex.com/pt/tutorial/marketplace-strategies-at-vtex--tutorials_402#ser-um-marketplace-vtex), [native connectors](https://help.vtex.com/pt/tutorial/marketplace-strategies-at-vtex--tutorials_402#integrado-a-conector-nativo-vtex) and [certified partners](https://help.vtex.com/pt/tutorial/marketplace-strategies-at-vtex--tutorials_402#integrado-a-conector-certificado-parceiro).

## Order flow

The Multilevel Omnichannel Inventory also affects an order's flow. The order flow describes the status, possibilities, and actions throughout the life cycle of an order. With the flow, retailers can also track the mapped order status on the platform. The table below summarizes all types of order flows that VTEX supports.

<table>
    <tr>
        <td><strong>Order source and destination</strong></td>
        <td><strong>Order type and workflow</strong></td>
    </tr>
    <tr>
        <td>VTEX store is the <strong>source</strong> of an order →</td>
        <td><a
                href="https://help.vtex.com/en/tutorial/fluxo-e-status-de-pedidos--tutorials_196#marketplace-flow">Marketplace order</a>
            with Checkout Workflow.</td>
    </tr>
    <tr>
        <td>VTEX store is <strong>intermediate</strong> in the order flow →</td>
        <td><a
                href="https://help.vtex.com/en/tutorial/fluxo-e-status-de-pedidos--tutorials_196#chain-flow">Chain order</a>
            with Chain Workflow.</td>
    </tr>
    <tr>
        <td>VTEX store is the <strong>destination</strong> of an order →</td>
        <td><a
                href="https://help.vtex.com/en/tutorial/fluxo-e-status-de-pedidos--tutorials_196#seller-flow">Seller order</a>
            with Fulfillment Workflow.</td>
    </tr>
    <tr>
        <td>VTEX store is both the <strong>source</strong> and the <strong>destination</strong> →</td>
        <td><a
                href="https://help.vtex.com/en/tutorial/fluxo-e-status-de-pedidos--tutorials_196#complete-flow">Complete order</a>
            flow with Fulfillment workflow.</td>
    </tr>
</table>

The Multilevel Omnichannel Inventory setting allows the entire inventory from a physical store network to be integrated into marketplaces, creating **chain orders**.

Let's break down how chain orders are applied in Multilevel Omnichannel Inventory architecture:

- Order originates in the marketplace (level 1).
- Order goes through an intermediate agent, in this case, the direct sellers (level 2).
- Order reaches its destination, to be fulfilled by the white label sellers (level 3).

Therefore, chain orders in direct seller have characteristics that come from both *marketplaces*, because they take the role of a seller's marketplace, and *sellers*, since they are also sellers of a marketplace.

Check out the order flow for chain orders in the image below:

![chain-orders-order-flow](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/multilevel-omnichannel-inventory-1.png)

The order flow seen by the level 2 store in a Multilevel Omnichannel Inventory is similar to the marketplace order flow, except for receiving the payment for orders. In the Payment pending stage, instead of the chain receiving payment directly from the gateway, the marketplace informs the chain it has received the payment confirmation.

> VTEX stores cannot use the [change order](https://developers.vtex.com/docs/guides/change-order) feature for chain orders made in VTEX marketplaces. However, it is possible to [Change chain orders in external marketplaces](https://developers.vtex.com/docs/guides/change-orders-multilevel-omnichannel-inventory-external-marketplaces).

## Setup for VTEX marketplaces

The setup for Multilevel Omnichannel Inventory must be made by the marketplace [through their VTEX Admin](https://help.vtex.com/en/tutorial/multilevel-omnichannel-inventory--7M1xyCZWUyCB7PcjNtOyw4) or REST API. This setup can be made in sellers that are already integrated, or sellers being added for the first time.

To configure Multilevel Omnichannel Inventory via REST API:

1. The marketplace must call the endpoint [Configure Seller Account](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/seller-register/pvt/sellers).
2. Fill the `fulfillmentEndpoint` field with the seller's checkout endpoint, following the example below:

   ```
   https://{{sellerAccount}}.vtexcommercestable.com.br/api/checkout?affiliateid={{affiliateId}}&sc={{salesChannel}}
   ```

3. Replace the placeholders with the following values:

   - **sellerAccount**: [Account name](https://help.vtex.com/pt/tutorial/o-que-e-account-name--i0mIGLcg3QyEy8OCicEoC) of the seller in VTEX.
   - **affiliateId**: 3-digit [afiliate](https://help.vtex.com/pt/tutorial/o-que-e-afiliado--4bN3e1YarSEammk2yOeMc0) identification code created by the seller. The seller must inform this ID to the marketplace so that the marketplace can complete the configuration process.
   - **salesChannel**: Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data) associated to the seller account created. The seller must inform this ID to the marketplace so that the marketplace can complete the configuration process.

> Check out the [Multilevel Omnichannel Inventory API integration](https://developers.vtex.com/docs/guides/multilevel-omnichannel-inventory-api-integration) guide to learn how to  external marketplace integrations, and headless architectures can make Multilevel omnichannel inventory available for their sellers.
