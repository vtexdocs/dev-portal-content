---
title: "Headless authentication"
slug: "headless-authentication"
hidden: true
createdAt: "2023-01-27T15:04:49.386Z"
---

Headless stores have much more flexibility when it comes to their frontend experiences. However, shopper authentication is a sensitive point for any ecommerce. Follow this guide to learn how to implement authentication in your headless shopping experience.

>❗ This feature is currently being tested by a limited number of VTEX accounts. Please do not share this documentation with people outside of your operation.

Building a headless ecommerce means setting up comunication between your frontend and VTEX's REST APIs. Each HTTP request sent from your frontend to VTEX must be authenticated with a [user token](https://developers.vtex.com/docs/guides/getting-started-authentication#user-token).

>ℹ️ Learn more about [machine authentication in VTEX](https://developers.vtex.com/docs/guides/getting-started-authentication).

To obtain 