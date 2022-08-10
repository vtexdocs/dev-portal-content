---
title: "Create User"
slug: "createuser"
hidden: false
createdAt: "2019-12-20T02:25:41.947Z"
updatedAt: "2020-01-13T17:19:05.296Z"
---
Allows you to create a user by providing an e-mail (mandatory) and name (optional). The e-mail must be in a valid format. The success response will contain the generated userId for that user.

### Response codes:
201: Success - Returns id, email and name.\
400: BadRequest - An invalid or null e-mail generates a BadRequest response.