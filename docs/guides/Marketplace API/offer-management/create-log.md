---
title: "Create Log"
slug: "create-log"
excerpt: "In [Offer Management](https://developers.vtex.com/vtex-rest-api/docs/sent-offers-integration-guide-connectors), logs are the granular details of actions that happen within an [interaction](https://developers.vtex.com/vtex-rest-api/reference/open-interaction), and they are organized in a timeline. All of the micro-steps of an interaction are represented through logs; they are how interactions become visible in Offer Management UI. \n\nThis endpoint adds logs that take place within an interaction, which can be done after [creating an interaction](https://developers.vtex.com/vtex-rest-api/reference/open-interaction) so that there will be an `interactionId`. \n\n`Errors`: When Offer Management, or the connectors, find an error that prevents sending or updating an offer to a channel, they should open a type failure log, and fill in its details through the `errors` attribute. The information provided should enable sellers to identify and fix errors on their offers. \n\nThe connectors should go through every possible validation, identify all errors, and only after that create the failure log, with the information in a single request."
hidden: false
createdAt: "2022-05-19T19:24:02.281Z"
updatedAt: "2022-06-15T18:54:01.405Z"
---
