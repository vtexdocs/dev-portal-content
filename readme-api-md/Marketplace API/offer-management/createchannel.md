---
title: "Create Channel"
slug: "createchannel"
excerpt: "The first step for connectors to integrate with [Offer Management](https://developers.vtex.com/vtex-rest-api/docs/sent-offers-integration-guide-connectors) is to create a channel, that represents the marketplace to where sellers will send their offers. \n\nThis endpoint creates a channel and the integration developers should call it once for each marketplace. The information about the marketplace sent in the request will be shown to sellers in their [Offer Management UI](https://help.vtex.com/en/tutorial/offers-listing--7MRb9S78aBdZjFGpbuffpE). \n\nThe `feedId` created by this call will apply to all sellers connected to the given channel, and will be necessary for the next step of the integration flow, which is to [activate feed](https://developers.vtex.com/vtex-rest-api/reference/create-feed). \n\n> ℹ️ Offer Management is available for integrations with [Mercado Livre (Classic and Premium)](https://help.vtex.com/pt/tracks/configurar-integracao-do-mercado-livre--2YfvI3Jxe0CGIKoWIGQEIq), [Netshoes](https://help.vtex.com/pt/tracks/configurar-integracao-da-netshoes--5Ua87lhFg4m0kEcuyqmcCm), and VTEX marketplaces. For more information, see [Offer Management Integration Guide](https://developers.vtex.com/vtex-rest-api/docs/sent-offers-integration-guide-connectors)."
hidden: false
createdAt: "2022-06-15T20:37:35.134Z"
updatedAt: "2022-06-17T18:30:43.704Z"
---
