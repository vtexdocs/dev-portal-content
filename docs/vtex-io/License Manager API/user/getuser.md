---
title: "Get User"
slug: "getuser"
hidden: false
createdAt: "2019-12-20T02:25:41.947Z"
updatedAt: "2020-01-13T17:17:18.187Z"
---
Allows you to get a user from the database, using the userId as the identifier.

### Response codes:<br />
200: Success - Returns id, email and name. <br/>
400: BadRequest - Userid is not in the appropriate format.<br />
404: UserNotFound - Returns a message displaying user could not be found.<br />
405: MethodNotAllowed - A null userId sends the request to a path that is not allowed.