---
title: "Remove Role from User/appKey"
slug: "removerolefromuser"
hidden: false
createdAt: "2019-12-20T02:25:41.947Z"
updatedAt: "2020-04-26T01:39:43.984Z"
---
Allows you to remove a role from a specific user. This method only allows the removal of one role per request, and it's id must be specified on the request address, not on the body.

### Response codes:
204: Success - A no-content response, but the role deletion was performed successfully. Keep in mind a deletion on a role or user that doesn't exist will also return a 204, as such this method shouldn't be used to verify the existance of a specific user or role.\
400: BadRequest - A userId or role in the wrong format will result in a BadRequest response. The message on the body of the response will contain further information.\
405: MethodNotAllowed - A null role sends the request to a path that is not allowed.