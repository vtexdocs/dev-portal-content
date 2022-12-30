---
title: "Create new session"
slug: "createnewsession"
hidden: false
createdAt: "2019-12-20T00:49:56.335Z"
updatedAt: "2020-09-17T21:43:55.556Z"
---
The response should contain a session cookie. Further POST or PATCH requests will edit the existing session rather than creating a new one. All parameters in the body that are not within the public namespace will be ignored. Querystring items will automatically be added to the public namespace. Cookies relevant to the session manager execution are also recorded.

[block:callout]
{
  "type": "warning",
  "title": "Cookie Based API",
  "body": "The sessions API uses the `vtex_session` cookie to store the data required to identify the user and the session. This cookie is stored in the user's browser when the session is created and sent automatically in every request to that domain. You will have to reproduce that in order for it to work outside of a browser environment."
}
[/block]