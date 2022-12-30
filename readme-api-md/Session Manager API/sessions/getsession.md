---
title: "Get Session"
slug: "getsession"
hidden: false
createdAt: "2019-12-20T00:49:56.335Z"
updatedAt: "2020-09-17T21:14:16.364Z"
---
Items are the keys of the values you wish to get. It follows the format `namespace1.key1,namespace2.key2`. So if you wish to recover the data sent on the previous request, it should be `public.country,public.postalCode`
[block:callout]
{
  "type": "warning",
  "title": "Cookie Based API",
  "body": "The sessions API uses the `vtex_session` cookie to store the data required to identify the user and the session. This cookie is stored in the user's browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment."
}
[/block]

[block:callout]
{
  "type": "info",
  "title": "",
  "body": "If you want to retrieve all keys from Session Manager, you can use the wildcard operator `*` in your request (i.e. `?items=*`)"
}
[/block]