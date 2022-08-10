---
title: "Remove Role from User/appKey"
slug: "removerolefromuser"
excerpt: "Allows you to remove a role from a specific user or application key. This method only allows the removal of one role per request. The role's ID must be specified on the request path, not on the request body."
hidden: false
createdAt: "2019-12-20T02:25:41.947Z"
updatedAt: "2021-12-01T01:38:06.672Z"
---
Note that a successful response returns a 204 response with an empty body. **A deletion on a role or user that does not exist will also return a 204**. Thus, this method should not be used to verify the existence of a specific user or role.