---
title: "Ads events notification"
slug: "ads-events-notification"
excerpt: "Learn how to send events like impressions, clicks, and conversions to VTEX Ads."
hidden: false
createdAt: "2025-05-21T22:18:24.684Z"
updatedAt: "2025-05-21T22:18:24.684Z"
---

This guide explains how to send event notifications to VTEX Ads. You can send events in two ways:

- Through a web browser using the `sendBeacon()` API
- Server-side or through native apps using REST endpoints

> 🚧 Don't construct event URLs manually. Always use the URL provided from the `POST` [Get ads](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/rma/-publisher_id-) request.
>
> This is extremely important to ensure long-term stability of the integration, because the parameters of the event URL may change over time, but the integration itself does not.

## Sending events via browser

For sending notifications in a web environment (browser), use the `sendBeacon()` method, as it is the most modern way to send data notifications. The advantage of using `sendBeacon()` is that the request is asynchronous, which means it doesn't block the loading of the current page nor the next page.

Response example from `POST` [Get ads](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/rma/-publisher_id-):

```json
{
  "products": [
    {
      "ad_id": "4a94bc6e-7db1-425f-8430-cb4d17488b3b",
      "sku": "120210",
      "click_url": "https://events.newtail-media.newtail.com.br/v1/beacon/click/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1",
      "impression_url": "https://events.newtail-media.newtail.com.br/v1/beacon/impression/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1",
    },
    {
      "ad_id": "8c293205-52f4-45cf-9a01-37e7c26a5abc",
      "sku": "123123",
      "click_url": "https://events.newtail-media.newtail.com.br/v1/beacon/click/8c293205-52f4-45cf-9a01-37e7c26a5abc?pos=2",
      "impression_url": "https://events.newtail-media.newtail.com.br/v1/beacon/impression/8c293205-52f4-45cf-9a01-37e7c26a5abc?pos=2",
    }
  ],
  "banners": []
}
```

To send an impression event, for example, take the `impression_url` from the first ad and use it as follows:

```javascript
let user_data = {
   user_id: "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
   session_id: "5898b8d1-c250-4bb5-931b-8b9d0ee7b499"
}

let beacon_url =  "https://events.newtail-media.newtail.com.br/v1/beacon/impression/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1"

var jsonBlob = new Blob([JSON.stringify(user_data)], { type: 'application/json' });

navigator.sendBeacon(beacon_url, jsonBlob);
```

## Sending events server-side or through a native app

In the cases that require sending via server-side or through a native app, make a `POST` request to the event URL, sending the user and session information in the payload.

You can use one of the following endpoints, depending on the event:

- `POST`  [Track ad impressions](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/beacon/impression/-ad_id-)
- `POST`  [Track ad clicks](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/beacon/click/-ad_id-)
- `POST`  [Track ad views](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/beacon/view/-ad_id-)
- `POST`  [Track conversions](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/beacon/conversion)

Request example:

```json
POST https://events.newtail-media.newtail.com.br/v1/beacon/impression/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1 HTTP/1.1
user-agent: newtail
accept: application/json
content-type: application/json

{
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499"
}
```

>ℹ️ A successful response will return HTTP status code 202 with no body.
