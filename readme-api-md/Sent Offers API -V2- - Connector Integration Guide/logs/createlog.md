---
title: "Create Log"
slug: "createlog"
excerpt: "Logs are the granular details of actions that happen within an interaction, organized in a timeline. They are the way an interaction is made visible in Sent Offer’s UI. All micro steps that go through an interaction will be represented through logs. This endpoint adds logs that take place within an interaction. To add logs in a specific interaction, the connector must take the `interactionId` created previously, through the Open  Interaction endpoint. \n\n`Errors`: When Sent Offers, or the connectors, find an error that prevents sending or updating an offer to a channel, they should open a type `failure` log, and fill in its details through the `errors` attribute. From the information sent through this attribute, sellers can identify and fix errors on their offers. Connectors must identify all errors, and send them all in a single request. This means that connectors should go through every possible validation, and only after all errors are identified, create the failure log."
hidden: true
createdAt: "2020-12-16T19:45:10.160Z"
updatedAt: "2020-12-16T19:45:10.160Z"
---
