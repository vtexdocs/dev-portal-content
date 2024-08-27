---
title: "Offer Management SDK"
slug: "offer-management-sdk"
hidden: false
createdAt: "2022-07-06T14:04:18.259Z"
updatedAt: "2022-07-06T14:38:05.752Z"
---
>❗ The Offer Management module has been discontinued and is no longer supported. The module has been replaced by [Offer Status](https://help.vtex.com/en/tutorial/status-de-anuncios-beta--2OE87wU26F7lApl99OdwvJ).
To learn more, visit the [announcement](https://help.vtex.com/en/announcements/modulo-status-dos-anuncios-para-integracoes-com-marketplaces-vtex--1EeGgit1Brq3mmm8qhv2m3).

The [Offer Management](https://help.vtex.com/en/tutorial/offer-management--7MRb9S78aBdZjFGpbuffpE) allows sellers to track the sending and syncing of their offers in marketplaces integrated with their store. The feature helps sellers identify updates and solve errors in their offers during the sending process, guaranteeing they were sent to the marketplace and synced correctly.  In VTEX, an offer is an SKU from a seller that has been sent to a marketplace and whose price and inventory information have been configured.

The current document is a Software Development Kit (SDK) created to facilitate the integration between a connector and Offer Management. The SDK includes the implementation of Offer Management’s main features and a .NET library via MyGet.

The integration using this SDK follows the same concepts presented in the [Offer Management Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/sent-offers-integration-guide-connectors):

| Concept     | Description                                                                                                                                         |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feed        | The `feedId` attribute created by the connector will identify sellers’ feeds with a channel.                                                        |
| Interaction | For every action that happens to an offer, whether it is a status notification or a price update, the connector creates an interaction about it.    |
| Logs        | Logs are the granular details of actions that happen within an interaction, and they are organized in a timeline. Logs registers last for ten days. |

Offer Management works with the creation of a feed, followed by the creation of interactions and logs. After the log is created, it is necessary to close the interaction, and that process is what makes an offer update visible for sellers in Offer Management’s UI.

These SDK is organized in the following sections:

1. [Installing dependencies](#installing-dependencies)
2. [Offer Management APIs](#offer-management-apis)
3. [Unified contract](#unified-contract)
4. [Integration flows](#integration-flows)

## Installing dependencies

**Step 1 -** Open the terminal and add the package to the project dependencies:

```
<PackageReference Include=\"SentOffers.SDK\" Version=\"0.0.4\" />
```

**Step 2 -** Inject dependencies in the project:

```
services.AddSingleton<ISentOffersClient, SentOffersClient>();
```

## Offer Management APIs

All of the APIs responses are contained in the object `SentOffersResponse`, which can be used to check if a transaction was successful or presented an error. All errors are listed in the `errors` attribute.

This section is organized as below:

- [Installing dependencies](#installing-dependencies)
- [Offer Management APIs](#offer-management-apis)
  - [Authentication](#authentication)
  - [Create feed](#create-feed)
  - [Deactivate feed](#deactivate-feed)
  - [Create interaction](#create-interaction)
  - [Create log](#create-log)
- [Unified contract](#unified-contract)
- [Integration flows](#integration-flows)
  - [Catalog integration](#catalog-integration)
  - [Price update](#price-update)
  - [Inventory update](#inventory-update)
  - [Integration errors](#integration-errors)

>ℹ️ This SDK does not reference all the APIs related to Offer Management, however, they can be found in VTEX API Reference under **Marketplace APIs > [Offer Management](https://developers.vtex.com/vtex-rest-api/reference/createchannel)**.

### Authentication

Authentication in Offer Management works as in VTEX REST APIs, as it can be seen in [Authentication](https://developers.vtex.com/docs/guides/getting-started-authentication). Through the `SentOffersCredentials` class, the connector can send information about AppKey, AppToken and VTEX IO token.

### Create feed

The creation of a feed establishes the connection between the seller's [affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187) ID and the marketplace’s ID, which corresponds to the attribute `Id` (also referred to as `feedId`).

```
SentOffersResponse <FeedCreateResponseDto> response;

response = await soClient.CreateFeedAsync(
   "account",
   new FeedCreateDTO
   {
      Id = "vtex.marketplace",
      SalesChannel = "1",
      AffiliatedId = "AFL"
   },
   credentials
)
```

### Deactivate feed

When a feed is deactivated, all data related to the marketplace is removed from Offer Management’s UI, including channels, offers, interactions, and errors. Deactivating a feed does not mean deleting information, and the seller can restore the data through the endpoint [Activate Feed](https://developers.vtex.com/vtex-rest-api/reference/create-feed).

In order to [delete a feed](https://developers.vtex.com/vtex-rest-api/reference/deactivate-feed), implement the code below:

```
var response = await soClient.DeleteFeedAsync(
   "account",
   “vtex.marketplace”,
   “credentials”
)
```

### Create interaction

An interaction should be created before the connector’s integration flow. The reason is that for any flow it will be necessary to inform the interaction context, whether it is a setup or a synchronization.

To create an interaction, do the following:

```
var response = await soClient.CreateInteractionAsync(
  "account",
  "vtex.makertplace",
  new InteractionCreateDTO
  {
     StartDate = Datetime.UtcNow.ToString(),
     Source =  InteractionSourceType.seller,
     Origin = OriginType.inventory,
     Context = InteractionContextType.sync
  },
  credentials
  ```

### Create log

Logs can be created as the following:

```
CreateLogDTO log = new()
{
   Description = "sdk test",
   Type = "Info",
   Agent = "channel",
   Date = DateTime.Now.ToString(),
   Data = new CreateLogDataRequest() { Status = "Sending" }
};

string skuId = "1";
string interactionId = "3DB3542A2C93412298AC95964A66A995";

var result = await _soClient.CreateLogAsync(
  "account",
  "vtex.marketplace",
  skuId,
  interactionId,
  log, credentials
  )
  ```

## Unified contract

In order to facilitate the integration with Offer Management, all the contracts presented in the previous sections were grouped in a single contract, that does the following:

1. Creates an interaction.
2. Receives a log.
3. Closes an interaction.

>⚠️ We highly recommend using this route when integrating with [Offer Management](https://help.vtex.com/en/tutorial/gestao-de-anuncios--7MRb9S78aBdZjFGpbuffpE). Other specific routes should be used only when the unified contract does not meet the connector's needs.

```
UnifiedInteractionCreateDTO unifiedContract = new()
{
   Date = "2021-10-15T16:20:19.561754Z",
   Source = "channel",
   Origin = "catalog",
   Context = "ongoing",
   Description = "Info example",
   Type = "Info",
   Agent = "My-Conector"
};

string skuId = "1";

var result = await _soClient.CreateUnifiedInteractionAsync(
  "account",
  "vtex.marketplace",
  skuId,
  unifiedContract,
  credentials
)
```

## Integration flows

If the [unified contract](#unified-contract) was not a solution for the connector, then this section’s specific flows must be implemented.

In order to integrate a VTEX seller’s SKU with a marketplace, the connector has to implement the flows as in the list below:

- [Catalog integration](#catalog-integration)
- [Price update](#price-update)
- [Inventory update](#inventory-update)
- [Integration error](#integration-errors)
[block:callout]

>ℹ️ After the creation of the feed, each interaction in Offer Management must start with the same `OriginType` attribute used in the integration flow that is operating, whether it is about inventory, price or catalog.

### Catalog integration

In order to create catalog integration, do as the following example:

```
CreateLogDTO log = new()
{
   Description = "SKU enviado ao marketplace",
   Type = "Failure",
   Agent = "channel",
   Date = DateTime.Now.ToString(),
   Errors = new CreateLogErrorRequest[] {
      new  CreateLogErrorRequest{
        Code = “
      }
   }
};

string skuId = "1";
string interactionId = "3DB3542A2C93412298AC95964A66A995";
var result = await _soClient.CreateLogAsync(
  "account",
  "vtex.marketplace",
  skuId,
  interactionId,
  log, credentials
)
```

### Price update

In order to update price in the integration, do as the following example:

```
CreateLogDTO log = new()
{
   Description = "SKU enviado ao marketplace",
   Type = "Info",
   Agent = "channel",
   Date = DateTime.Now.ToString(),
   Data = new CreateLogDataRequest
     Status = "Synchronized",
     Price = 124,
     Currency = "BRL"
    };

string skuId = "1";
string interactionId = "3DB3542A2C93412298AC95964A66A995";

var result = await _soClient.CreateLogAsync(
  "account",
  "vtex.marketplace",
  skuId,
  interactionId,
  log, credentials
)
```

### Inventory update

In order to update inventory in the integration, do as the following example:

```
CreateLogDTO log = new()
{
   Description = "SKU enviado ao marketplace",
   Type = "Info",
   Agent = "channel",
   Date = DateTime.Now.ToString(),
   Data = new CreateLogDataRequest
     Status = "Synchronized",
     Inventory= 8
   };

string skuId = "1";
string interactionId = "3DB3542A2C93412298AC95964A66A995";

var result = await _soClient.CreateLogAsync(
  "account",
  "vtex.marketplace",
  skuId,
  interactionId,
  log, credentials
)
```

### Integration errors

To integrate errors cases, do as the following example:

```
string skuId = "1";
string interactionId = "3DB3542A2C93412298AC95964A66A995";

var result = await _soClient.CreateLogAsync(
  "account",
  "vtex.marketplace",
  skuId,
  interactionId,
  log, credentials
)
```