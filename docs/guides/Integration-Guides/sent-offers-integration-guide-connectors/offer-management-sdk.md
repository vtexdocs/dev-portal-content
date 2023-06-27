---
title: "Offer Management SDK"
slug: "offer-management-sdk"
hidden: false
createdAt: "2022-07-06T14:04:18.259Z"
updatedAt: "2022-07-06T14:38:05.752Z"
---
[block:callout]
{
  "type": "info",
  "body": "To evolve your experience in synchronizing and updating offers, the VTEX team is developing a new functionality that will replace the current module **Offer Management**. As a result, the module will not receive new updates or maintenance.
  For connectors and marketplaces already integrated into the module, please contact the development team by email [taissa.araujo@vtex.com.br](taissa.araujo@vtex.com.br).
  For connectors interested in starting the integration, we ask you to wait for the release of the new module, as soon as it is available we will announce it to all customers through the [dev portal](https://developers.vtex.com/updates/release-notes) and [help VTEX](https://help.vtex.com/pt/en/announcements)."
}
[/block]

[block:callout]
{
  "type": "info",
  "body": "For the guide based on APIs, see [Offer Management Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/sent-offers-integration-guide-connectors)."
}
[/block]
The [Offer Management](https://help.vtex.com/en/tutorial/offer-management--7MRb9S78aBdZjFGpbuffpE) allows sellers to track the sending and syncing of their offers in marketplaces integrated with their store. The feature helps sellers identify updates and solve errors in their offers during the sending process, guaranteeing they were sent to the marketplace and synced correctly.  In VTEX, an offer is an SKU from a seller that has been sent to a marketplace and whose price and inventory information have been configured. 

The current document is a Software Development Kit (SDK) created to facilitate the integration between a connector and Offer Management. The SDK includes the implementation of Offer Management’s main features and a .NET library via MyGet.

The integration using this SDK follows the same concepts presented in the [Offer Management Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/sent-offers-integration-guide-connectors):

[block:parameters]
{
  "data": {
    "h-0": "Concept",
    "h-1": "Description",
    "0-0": "Feed",
    "1-0": "Interaction",
    "2-0": "Logs",
    "0-1": "The `feedId` attribute created by the connector will identify sellers’ feeds with a channel.",
    "1-1": "For every action that happens to an offer, whether it is a status notification or a price update, the connector creates an interaction about it.",
    "2-1": "Logs are the granular details of actions that happen within an interaction, and they are organized in a timeline. Logs registers last for ten days."
  },
  "cols": 2,
  "rows": 3
}
[/block]
Offer Management works with the creation of a feed, followed by the creation of interactions and logs. After the log is created, it is necessary to close the interaction, and that process is what makes an offer update visible for sellers in Offer Management’s UI.

These SDK is organized in the following sections:

1. [Installing dependencies](#installing-dependencies)
2. [Offer Management APIs](#offer-management-apis)
3. [Unified contract](#unified-contract)
4. [Integration flows](#integration-flows)

## Installing dependencies

**Step 1 -** Open the terminal and add the package to the project dependencies:
[block:code]
{
  "codes": [
    {
      "code": "<PackageReference Include=\"SentOffers.SDK\" Version=\"0.0.4\" />",
      "language": "text"
    }
  ]
}
[/block]
**Step 2 -** Inject dependencies in the project:
[block:code]
{
  "codes": [
    {
      "code": "services.AddSingleton<ISentOffersClient, SentOffersClient>();",
      "language": "text"
    }
  ]
}
[/block]
## Offer Management APIs

All of the APIs responses are contained in the object `SentOffersResponse`, which can be used to check if a transaction was successful or presented an error. All errors are listed in the `errors` attribute.

This section is organized as below:

- [Authentication](#authentication)
- [Create feed](#create-feed)
- [Deactivate feed](#deactivate-feed)
- [Create interaction](#create-interaction)
- [Create log](#create-log)
[block:callout]
{
  "type": "info",
  "body": "This SDK does not reference all the APIs related to Offer Management, however, they can be found in VTEX API Reference under **Marketplace APIs > [Offer Management](https://developers.vtex.com/vtex-rest-api/reference/createchannel)**."
}
[/block]
### Authentication

Authentication in Offer Management works as in VTEX REST APIs, as it can be seen in [Authentication](https://developers.vtex.com/docs/guides/getting-started-authentication). Through the `SentOffersCredentials` class, the connector can send information about AppKey, AppToken and VTEX IO token.

### Create feed

The creation of a feed establishes the connection between the seller's [affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187) ID and the marketplace’s ID, which corresponds to the attribute `Id` (also referred to as `feedId`).
[block:code]
{
  "codes": [
    {
      "code": "SentOffersResponse<FeedCreateResponseDto> response;\n\nresponse = await soClient.CreateFeedAsync(\n   \"account\",\n   new FeedCreateDTO\n   {\n      Id = \"vtex.marketplace\",\n      SalesChannel = \"1\",\n      AffiliatedId = \"AFL\"\n   },\n   credentials\n);",
      "language": "text"
    }
  ]
}
[/block]
### Deactivate feed

When a feed is deactivated, all data related to the marketplace is removed from Offer Management’s UI, including channels, offers, interactions, and errors. Deactivating a feed does not mean deleting information, and the seller can restore the data through the endpoint [Activate Feed](https://developers.vtex.com/vtex-rest-api/reference/create-feed).

In order to [delete a feed](https://developers.vtex.com/vtex-rest-api/reference/deactivate-feed), implement the code below:
[block:code]
{
  "codes": [
    {
      "code": "var response = await soClient.DeleteFeedAsync(\n   \"account\",\n   “vtex.marketplace”,\n   “credentials”\n);",
      "language": "text"
    }
  ]
}
[/block]
### Create interaction

An interaction should be created before the connector’s integration flow. The reason is that for any flow it will be necessary to inform the interaction context, whether it is a setup or a synchronization. 

To create an interaction, do the following:
[block:code]
{
  "codes": [
    {
      "code": "var response = await soClient.CreateInteractionAsync(\n  \"account\",\n  \"vtex.makertplace\",\n  new InteractionCreateDTO\n  {\n     StartDate = Datetime.UtcNow.ToString(),\n     Source =  InteractionSourceType.seller,\n     Origin = OriginType.inventory,\n     Context = InteractionContextType.sync\n  },\n  credentials",
      "language": "text"
    }
  ]
}
[/block]
### Create log

Logs can be created as the following:
[block:code]
{
  "codes": [
    {
      "code": "CreateLogDTO log = new()\n{\n   Description = \"sdk test\",\n   Type = \"Info\",\n   Agent = \"channel\",\n   Date = DateTime.Now.ToString(),\n   Data = new CreateLogDataRequest() { Status = \"Sending\" }\n};\n\nstring skuId = \"1\";\nstring interactionId = \"3DB3542A2C93412298AC95964A66A995\";\n \nvar result = await _soClient.CreateLogAsync(\n  \"account\",\n  \"vtex.marketplace\",\n  skuId, \n  interactionId, \n  log, credentials\n  );",
      "language": "text"
    }
  ]
}
[/block]
## Unified contract

In order to facilitate the integration with Offer Management, all the contracts presented in the previous sections were grouped in a single contract, that does the following:

1. Creates an interaction.
2. Receives a log.
3. Closes an interaction.
[block:callout]
{
  "type": "warning",
  "body": "We highly recommend using this route when integrating with [Offer Management](https://help.vtex.com/en/tutorial/gestao-de-anuncios--7MRb9S78aBdZjFGpbuffpE). Other specific routes should be used only when the unified contract does not meet the connector's needs."
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "UnifiedInteractionCreateDTO unifiedContract = new()\n{\n   Date = \"2021-10-15T16:20:19.561754Z\",\n   Source = \"channel\",\n   Origin = \"catalog\",\n   Context = \"ongoing\",\n   Description = \"Info example\",\n   Type = \"Info\",\n   Agent = \"My-Conector\"\n};\n\nstring skuId = \"1\";\n \nvar result = await _soClient.CreateUnifiedInteractionAsync(\n  \"account\",\n  \"vtex.marketplace\",\n  skuId,\n  unifiedContract,\n  credentials\n);",
      "language": "text"
    }
  ]
}
[/block]
## Integration flows

If the [unified contract](#unified-contract) was not a solution for the connector, then this section’s specific flows must be implemented. 

In order to integrate a VTEX seller’s SKU with a marketplace, the connector has to implement the flows as in the list below:

- [Catalog integration](#catalog-integration)
- [Price update](#price-update)
- [Inventory update](#inventory-update)
- [Integration error](#integration-errors)
[block:callout]
{
  "type": "info",
  "body": "After the creation of the feed, each interaction in Offer Management must start with the same `OriginType` attribute used in the integration flow that is operating, whether it is about inventory, price or catalog."
}
[/block]
### Catalog integration 

In order to create catalog integration, do as the following example:
[block:code]
{
  "codes": [
    {
      "code": "CreateLogDTO log = new()\n{\n   Description = \"SKU enviado ao marketplace\",\n   Type = \"Failure\",\n   Agent = \"channel\",\n   Date = DateTime.Now.ToString(),\n   Errors = new CreateLogErrorRequest[] {\n      new  CreateLogErrorRequest{\n        Code = “\n      }\n   }\n};\n\nstring skuId = \"1\";\nstring interactionId = \"3DB3542A2C93412298AC95964A66A995\";\n \nvar result = await _soClient.CreateLogAsync(\n  \"account\",\n  \"vtex.marketplace\",\n  skuId, \n  interactionId, \n  log, credentials\n);",
      "language": "text"
    }
  ]
}
[/block]
### Price update

In order to update price in the integration, do as the following example:
[block:code]
{
  "codes": [
    {
      "code": "CreateLogDTO log = new()\n{\n   Description = \"SKU enviado ao marketplace\",\n   Type = \"Info\",\n   Agent = \"channel\",\n   Date = DateTime.Now.ToString(),\n   Data = new CreateLogDataRequest\n     Status = \"Synchronized\",\n     Price = 124,\n     Currency = \"BRL\"\n   }\n};\n\nstring skuId = \"1\";\nstring interactionId = \"3DB3542A2C93412298AC95964A66A995\";\n \nvar result = await _soClient.CreateLogAsync(\n  \"account\",\n  \"vtex.marketplace\",\n  skuId, \n  interactionId, \n  log, credentials\n);",
      "language": "text"
    }
  ]
}
[/block]
### Inventory update

In order to update inventory in the integration, do as the following example:
[block:code]
{
  "codes": [
    {
      "code": "CreateLogDTO log = new()\n{\n   Description = \"SKU enviado ao marketplace\",\n   Type = \"Info\",\n   Agent = \"channel\",\n   Date = DateTime.Now.ToString(),\n   Data = new CreateLogDataRequest\n     Status = \"Synchronized\",\n     Inventory= 8\n   }\n};\n\nstring skuId = \"1\";\nstring interactionId = \"3DB3542A2C93412298AC95964A66A995\";\n \nvar result = await _soClient.CreateLogAsync(\n  \"account\",\n  \"vtex.marketplace\",\n  skuId, \n  interactionId, \n  log, credentials\n);",
      "language": "text"
    }
  ]
}
[/block]
### Integration errors

To integrate errors cases, do as the following example:
[block:code]
{
  "codes": [
    {
      "code": "string skuId = \"1\";\nstring interactionId = \"3DB3542A2C93412298AC95964A66A995\";\n \nvar result = await _soClient.CreateLogAsync(\n  \"account\",\n  \"vtex.marketplace\",\n  skuId, \n  interactionId, \n  log, credentials\n);",
      "language": "text"
    }
  ]
}
[/block]