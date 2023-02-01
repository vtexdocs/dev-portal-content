---
title: "External seller processing payments"
slug: "external-seller-processing-payments"
hidden: false
createdAt: "2021-08-30T20:30:22.048Z"
updatedAt: "2022-02-03T13:21:17.263Z"
---
Although in our [marketplace / seller architecture](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-architecture) payments are usually processed by the marketplace, this can also be done by the seller. This decision of where to process payments depends on the commercial conditions they have negotiated with the payment provider.  Therefore, there are two possibilities for processing payments:

- **Marketplace processing payments:** no development is needed from the seller.
- **External seller processing payments:** seller should follow the instructions below.

## Split Payments

Marketplace orders can often contain items from multiple sellers, which are paid for in a unified checkout experience at the marketplace’s storefront. If external sellers process payments, they are tied to the conditions determined in our [Transaction Split](https://help.vtex.com/en/tutorial/split-payment--6k5JidhYRUxileNolY2VLx#transaction-split). If marketplaces decide to process payments, they can either transfer seller's purchase amount outside of VTEX, or fall under the [Payout split](https://help.vtex.com/en/tutorial/split-payment--6k5JidhYRUxileNolY2VLx#payout-split) flow. We suggest that you read our [Split Payment](https://help.vtex.com/en/tutorial/split-payment--6k5JidhYRUxileNolY2VLx) article to better inform the decision of who processes payments.

## Seller setup

The following steps are required to enable external sellers to process payments:

### Create Gateway Account

For sellers to process payments received from an order, it is necessary to create a VTEX [Gateway](https://help.vtex.com/en/tutorial/what-is-a-payment-gateway--2KH9Wdi7F6swOU4amECSOk) account, even though their stores are not hosted in VTEX.

VTEX marketplaces can request  Gateway accounts to be created for their sellers for a fixed monthly fee. For this type of account, no variable billing is applied.

The marketplace should send an email to one of the addresses below, depending on their region, requesting the additional Gateway account for their external seller. Make sure to include the following information in your email request:

- Account name, included in the VTEX environment url `{accountname}.myvtex.com/admin`
- Name of the user responsible for the account
- Email of the user responsible for the account

Example:

_Account Name: sellerstore_
_User: Carol Danvers_
_Email:_ `caroldanvers@sellerstore.com`

| Region                  | Email                     | Monthly Fee |
|-------------------------|---------------------------|-------------|
| Brazil                  | `sales-ops-br@vtex.com.br`  | R$750,00    |
| Europe                  | `sales-operations@vtex.com` | EUR 250     |
| United States and LatAm | `sales-operations@vtex.com` | 250 USD     |

### Configure payment settings

The seller’s Gateway account created will be used to set up the [payments’ architecture](https://help.vtex.com/en/tracks/payments--6GAS7ZzGAm7AGoEAwDbwJG) on the seller's side. Some steps are only executed through the VTEX Admin of the Gateway account, while others can be done by API integration. Follow the steps below to configure your payment settings.

#### Set up gateway affiliations

A gateway affiliation is a set of configurations that represent your contract with a payment gateway of your choice. VTEX has a number of gateway affiliations already working natively in our environment that you can plug into your account.

You can view all the affiliations natively connected to VTEX through your VTEX Admin so you can decide which one suits your payment settings, and then register it through the VTEX Admin by following the steps below.
[block:callout]
{
  "type": "info",
  "body": "In case the affiliations natively connected to VTEX do not suit your needs, you can develop your own by following the Payment Provider Protocol.",
  "title": "Payment Provider Protocol"
}
[/block]

1. Access the **VTEX Admin** through your Gateway Account.
2. On the left navigation menu, click on the **Payments** tab.
3. Click on the **Settings** page.
4. Click on `+` to see available affiliations.
5. Give your affiliation a name.
6. Enter the contract data sent by the chosen Gateway.
7. Click on `Save`.
[block:callout]
{
  "type": "warning",
  "body": "The full list of affiliations is only visible through the VTEX Admin, by following the steps above from steps 1-4. Once you choose the affiliation that will be implemented, you can use our [Insert affiliation](https://developers.vtex.com/vtex-rest-api/reference/insertaffiliation) endpoint to configure it to your account, instead of following steps 5-7. You can check all affiliations implemented to your store through the [Get Affiliations](https://developers.vtex.com/vtex-rest-api/reference/affiliations) endpoint.",
  "title": "API Integration"
}
[/block]

#### Set up Payment Conditions and Antifraud

To finalize Payment settings on the seller's side, it is necessary to set up Payment Conditions, or Rules, and an Antifraud for transactions.

It is possible to setup payment conditions through your gateway account’s VTEX Admin.  Check [Set up  the payment options](https://help.vtex.com/en/tutorial/how-to-configure-payment-conditions) to know how.

If you wish to realize this step through API calls, use [Get Rules](https://developers.vtex.com/vtex-rest-api/reference/rules) > [Insert Rule](https://developers.vtex.com/vtex-rest-api/reference/insertrule) calls.

The Antifraud can be set up  through your gateway account’s VTEX Admin.  Check [Set up the Antifraud](https://help.vtex.com/tutorial/how-to-configure-the-anti-fraud--tutorials_446) to know how.

To configure it through API, fill in the `antifraud` object in the [Insert Rule](https://developers.vtex.com/vtex-rest-api/reference/insertrule) edpoint.

## Wrapping up

Once these steps are done, you can move on to the External Seller Connector section of this guide. To finalize the process it is necessary to [send your Gateway account name to the marketplace](https://developers.vtex.com/vtex-rest-api/docs/external-seller-integration-connector#seller-processing-payments).
