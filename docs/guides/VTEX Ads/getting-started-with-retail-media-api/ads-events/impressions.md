---
title: "Impressions"
slug: "impressions"
excerpt: "Track when an ad is rendered or visible to a user."
hidden: false
createdAt: "Wed Mar 01 2023 15:45:55 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jun 28 2024 12:53:13 GMT+0000 (Coordinated Universal Time)"
---
> 🚧 The event URL must not be "constructed" manually—always use the URL provided from the ad query.
>
> This is very important to ensure the long-term stability of the integration. The reason is that the parameters in the event URL may change over time, but the integration itself does not. This makes the entire process evolutionary and transparent for everyone.

# Impression Notification

Example of impression submission below:

### Request

```http HTTP
POST https://events-api.ads.vtex.com/v1/beacon/impression/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1 HTTP/1.1
accept: application/json
content-type: application/json

{
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499"
}
 
```

### Response

> The request will return an HTTP 202 status code

```
{
	"messages": [
		"impression will be processed soon"
	]
}
```

> A failed request will return an HTTP 422 status code
>
> The error response follows RFC 8927 <https://datatracker.ietf.org/doc/rfc8927/>

```json
[
  {
    instancePath: '',
    keyword: 'required',
    message: "must have required property 'user_id'",
    params: { missingProperty: 'user_id' },
    schemaPath: '#/anyOf/0/required',
  },
  {
    instancePath: '',
    keyword: 'required',
    message: "must have required property 'session_id'",
    params: { missingProperty: 'session_id' },
    schemaPath: '#/anyOf/1/required',
  },
  {
    instancePath: '',
    keyword: 'anyOf',
    message: 'must match a schema in anyOf',
    params: {},
    schemaPath: '#/anyOf',
  }
]
```
