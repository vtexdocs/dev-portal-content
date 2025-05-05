---
title: "Session Manager"
slug: "session-manager"
hidden: false
createdAt: "2022-08-04T20:39:52.282Z"
updatedAt: "2022-08-04T21:15:25.877Z"
---
Session Manager is a module that tracks the current browsing session of all clients on the VTEX platform. Important session information is automatically captured and stored in a secure and easily accessible location. This includes data such as relevant cookies, query strings, authentication credentials, current profile and pricing information, if applicable.

This article aims to describe Session Manager from a system design perspective. For further details on how to interact with the Session Manager API, check the [API reference](https://developers.vtex.com/docs/api-reference/session-manager-api#overview).

## Getting and storing session information

Whenever a new device comes in contact with the VTEX infrastructure, Session Manager receives a request for a new session. Events that would trigger this request include visiting a store page, opening the VTEX Admin panel and loading the inStore vendor interface, to name a few. After a new session is created, Session Manager will start receiving all the important information associated to navigation from that specific device. 

Using the [Session Manager API](https://developers.vtex.com/docs/api-reference/session-manager-api#overview), you can make a request to receive the session data you need for your application. This includes important inferences made by VTEX modules. See [Data available from VTEX apps](https://developers.vtex.com/docs/guides/session-data-available-from-vtex-apps) for more information.

For instance, a user with a specific campaign referral link might have a promotional price table set on his session, which will cause them to see updated prices when navigating the store that created that campaign.

Besides getting session information for a device navigating in the VTEX infrastructure, Session Manager allows you to store your own custom data in that session. This information is easily recoverable and eliminates the need for other user tracking methods like cookies.
