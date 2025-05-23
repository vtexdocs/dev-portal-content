---
title: "Clicks"
slug: "clicks"
excerpt: "Track ad clicks."
hidden: false
createdAt: "2023-03-01T15:46:03.000Z"
updatedAt: "2024-06-28T12:53:27.000Z"
---

> 🚧 The event URL must not be "constructed"; always use the URL that comes from the ad request response.  
>  
> This is very important to ensure long-term integration stability. The parameters of the event URL may change over time, but the integration itself does not need to be modified. This makes the entire process evolutionary and transparent for everyone.

# Click Notification

Example of sending an impression below:

### Request

```http
POST https://events-api.ads.vtex.com/v1/beacon/click/4a94bc6e-7db1-425f-8430-cb4d17488b3b?pos=1 HTTP/1.1
accept: application/json
content-type: application/json

{
  "user_id": "6f92d1e9-00b6-4f8b-9645-faeab321e1cc",
  "session_id": "5898b8d1-c250-4bb5-931b-8b9d0ee7b499"
}
 
```

### Response

The request will be returned with HTTP code 202

```json
{
	"messages": [
		"click will be processed soon"
	]
}
```

> Request failure return will have HTTP code 422
>
> Error return implements RFC 8927 https://datatracker.ietf.org/doc/rfc8927/

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
