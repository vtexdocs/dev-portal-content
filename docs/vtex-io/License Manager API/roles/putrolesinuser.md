---
title: "Put Roles in User/appKey"
slug: "putrolesinuser"
hidden: false
createdAt: "2019-12-20T02:25:41.947Z"
updatedAt: "2020-04-26T01:39:43.949Z"
---
Allows you to add roles to a particular user by specifying the list of id's of roles on the body of the request. Such id's can be looked up on the License Manager UI.

### Response codes:
204: Success - A no-content response, but the roles were added successfully.\
400: BadRequest - An invalid userId or role list format will result in a BadRequest response. The message on the body of the response will contain further information.\
404: UserNotFound - The userId is not present on the database.