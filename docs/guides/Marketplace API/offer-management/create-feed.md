---
title: "Activate Feed"
slug: "create-feed"
excerpt: "In [Offer Management](https://developers.vtex.com/vtex-rest-api/docs/sent-offers-integration-guide-connectors), after [creating the channel](https://developers.vtex.com/vtex-rest-api/reference/createchannel), the next step is to create a feed, which is a list updated nearly in real time with information about the seller's offers sent to the marketplace. \n\nThis endpoint allows the creation of a feed so that the seller's sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) is connected to the marketplace. Feeds are nearly real time updated with content provided by the marketplace and VTEX modules. \n\nThis endpoint should only be used once, to activate the channel and establish the connection. However, after a [feed is deactivated](https://developers.vtex.com/vtex-rest-api/reference/deactivate-feed), in order to activate it again it will be necessary another call to this endpoint.The integration starts with the creation of the Feed. This endpoint is used to establish the connection between connector and seller through the Sent Offers. The `feedId` attribute that identifies a feed between a seller and a channel, follows a standardized pattern that will be used by connectors when calling this endpoint. It follows the pattern `vendor.channel`."
hidden: false
createdAt: "2022-05-19T19:24:02.278Z"
updatedAt: "2022-06-20T18:08:05.362Z"
---
