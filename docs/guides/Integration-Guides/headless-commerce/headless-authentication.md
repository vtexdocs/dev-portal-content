---
title: "Headless authentication"
slug: "headless-authentication"
hidden: true
createdAt: "2023-01-27T15:04:49.386Z"
---

Headless stores have much more flexibility when it comes to their frontend experiences. However, shopper authentication is a sensitive point for any ecommerce and must be implemented in according to some guidelines.

>❗ This feature is currently being tested by a limited number of VTEX accounts. Please do not share this documentation with people outside of your operation.

Building a headless ecommerce means setting up comunication between your frontend and VTEX's REST APIs. Each HTTP request sent from your frontend to VTEX must be authenticated with a [user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token). The implementation shown below describes how to obtain this token in your frontend.

>ℹ️ Learn more about [machine authentication in VTEX](https://developers.vtex.com/docs/guides/getting-started-authentication).

## Implementation

To obtain a VTEX user token, there are a few steps you must follow