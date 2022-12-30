---
title: "Edit session"
slug: "editsession"
hidden: false
createdAt: "2019-12-20T00:49:56.335Z"
updatedAt: "2020-09-17T21:41:50.547Z"
---
This works exactly the same as the POST create session, but when the request is sent with a vtex_session cookie, it retrieves the session first and then applies the changes instead of generating a new one.

As with the POST method, only keys inside the public namespace on the body are considered, and querystrings are automatically added to the public namespace.
[block:callout]
{
  "type": "warning",
  "title": "Cookie Based API",
  "body": "The sessions API uses the `vtex_session` cookie to store the data required to identify the user and the session. This cookie is stored in the user's browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment."
}
[/block]