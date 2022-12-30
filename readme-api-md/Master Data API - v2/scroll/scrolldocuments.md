---
title: "Scroll documents"
slug: "scrolldocuments"
excerpt: "In the first request, the `X-VTEX-MD-TOKEN` token will be returned in the header. This token must be passed to the next request in the query string `_token` parameter. The token has a timeout of 10 minutes, which refreshes after each request.\r\n\r\nAfter the token is obtained it is no longer necessary to send the filter or document size per page parameters. You only need to resend the token until the document collection is empty.\n\r\n\r> Avoid sending too many requests with wildcards (`*`) in the search parameters or that use the `keyword` parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code `429`.\r\n\r\n## Request examples\r\n\r\nFirst request:\r\n```\r\n/dataentities/Client/scroll?isCluster=true&_size=250&_fields=email,firstName\r\n```\r\n\r\nRetrieve the token in the header `X-VTEX-MD-TOKEN` from the first request's response and use it to make the next requests.\r\n\r\nSubsequent requests:\r\n```\r\n/dataentities/Client/scroll?_token={tokenValueExample}\r\n```"
hidden: false
createdAt: "2019-12-16T06:09:28.493Z"
updatedAt: "2022-12-01T20:20:17.092Z"
---
