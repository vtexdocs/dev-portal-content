---
title: "Views"
slug: "views"
excerpt: "Track views for banner ads."
hidden: false
createdAt: "Wed Mar 01 2023 15:46:50 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Sep 30 2024 14:19:09 GMT+0000 (Coordinated Universal Time)"
---

> 🚧 The event URL must not be "constructed" manually—always use the URL provided when retrieving the ads.
> 
> This is extremely important to ensure long-term integration stability. The event URL parameters may change over time, but the integration itself won't need to be updated. This makes the whole process evolutionary and transparent for everyone.

# View Notification

Example of a view notification (only for banner ads) below:

### Request

```http HTTP
POST https://events-api.ads.vtex.com/v1/beacon/view/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1 HTTP/1.1
accept: application/json
content-type: application/json

{
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499"
}
 
```

### Response

The request response will have HTTP status code 202

```
{
	"messages": [
		"view will be processed soon"
	]
}
```

> The error response will have HTTP status code 422  
>  
> The error format follows RFC 8927 https://datatracker.ietf.org/doc/rfc8927/

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
