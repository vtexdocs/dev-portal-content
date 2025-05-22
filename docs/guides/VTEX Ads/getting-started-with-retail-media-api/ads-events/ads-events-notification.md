---
title: "Ads events notification"
slug: "ads-events-notification"
excerpt: "Learn how to send events like impressions, clicks, and conversions to VTEX Ads."
hidden: false
createdAt: "Wed Mar 01 2023 15:46:03 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jun 28 2024 12:53:27 GMT+0000 (Coordinated Universal Time)"
---

The sections below cover sending notifications, specifically handling conversion notifications, which require receiving information about the completed order. We will address this in the following page: [Conversion Event](https://newtail-media.readme.io/reference/evento-de-conversao)

> 🚧 The event URL must never be "constructed" manually; always use the URL provided from the ad request.
> 
> This is extremely important to ensure long-term stability of the integration. This is because the parameters of the event URL may change over time, but the integration itself does not. This makes the entire process evolutionary and transparent for everyone.

# Sending Events (Browser)

Our recommendation for sending notifications in a web environment (browser) is to use the **sendBeacon()** method, as it is the most modern way to send data notifications. The great advantage of using sendBeacon is that the request is truly asynchronous, does not block the loading of the current page nor the next page.

Using the following response from an ad request:

```json
{
  "products": [
    {
      "ad_id": "4a94bc6e-7db1-425f-8430-cb4d17488b3b",
      "sku": "120210",
      "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1",
      "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1",
    },
    {
      "ad_id": "8c293205-52f4-45cf-9a01-37e7c26a5abc",
      "sku": "123123",
      "click_url": "https://events-api.ads.vtex.com/v1/beacon/click/8c293205-52f4-45cf-9a01-37e7c26a5abc?pos=2",
      "impression_url": "https://events-api.ads.vtex.com/v1/beacon/impression/8c293205-52f4-45cf-9a01-37e7c26a5abc?pos=2",
    }
  ],
  "banners": []
}
```

We can take the impression_url from the first ad and use it as follows:

```javascript
let user_data = {
   user_id: "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
   session_id: "5898b8d1-c250-4bb5-931b-8b9d0ee7b499"
}

let beacon_url =  "https://events-api.ads.vtex.com/v1/beacon/impression/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1"

var jsonBlob = new Blob([JSON.stringify(user_data)], { type: 'application/json' });

navigator.sendBeacon(beacon_url, jsonBlob);
```

# Event Sending (Server-side or Native App)

In these cases of sending via server-side or through a native app, the key is to send a POST request to the event URL, passing the user and session information in the payload.

Example of impression sending below:

### Request

```http HTTP
POST https://events-api.ads.vtex.com/v1/beacon/impression/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1 HTTP/1.1
user-agent: newtail
accept: application/json
content-type: application/json

{
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499"
}
```

### Response

> The request will return HTTP status code 202 with no body.
