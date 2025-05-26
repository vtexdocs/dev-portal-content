---
title: "Views"
slug: "views"
excerpt: "Track views for banner ads."
hidden: false
createdAt: "2025-05-21T22:18:24.684Z"
updatedAt: "2025-05-21T22:18:24.684Z"
---

VTEX Ads uses view tracking to measure when banner advertisements are effectively displayed to users. This guide explains how to properly send view events when banner ads become visible to users.

## View event rules

- View events should only be sent for banner ads.
- View events require both `user_id` and `session_id` for proper attribution.
- View URLs are unique to each ad and should be obtained from the [Get ads](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/rma/-publisher_id-) response.

> 🚧 Don't construct event URLs manually. Always use the URL provided from the `POST` [Get ads](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/rma/-publisher_id-) request.
>
> This is extremely important to ensure long-term stability of the integration, because the parameters of the event URL may change over time, but the integration itself does not.

## Sending a view event

Use the `POST` [Track ad views](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/beacon/view/-ad_id-) endpoint to send view events. Check the endpoint documentation for detailed information about all available fields.

Request example:

```json
POST https://events-api.ads.vtex.com/v1/beacon/view/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1 HTTP/1.1
accept: application/json
content-type: application/json

{
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499"
}
```

Successful response example:

>ℹ️ A successful response will have HTTP code 202.

```json
{
 "messages": [
  "view will be processed soon"
 ]
}
```

Failed response example:

>ℹ️ A failed response will have HTTP code 422. The error message follows the [RFC 8927](https://datatracker.ietf.org/doc/rfc8927/) format.

```json
[
  {
    "instancePath": "",
    "keyword": "required",
    "message": "must have required property 'user_id'",
    "params": { "missingProperty": "user_id" },
    "schemaPath": "#/anyOf/0/required"
  },
  {
    "instancePath": "",
    "keyword": "required",
    "message": "must have required property 'session_id'",
    "params": { "missingProperty": "session_id" },
    "schemaPath": "#/anyOf/1/required"
  },
  {
    "instancePath": "",
    "keyword": "anyOf",
    "message": "must match a schema in anyOf",
    "params": {},
    "schemaPath": "#/anyOf"
  }
]
```
