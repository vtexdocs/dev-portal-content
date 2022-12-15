---
title: "2. Redirect"
slug: "2redirect"
excerpt: "VTEX will redirect the store administrator to the Payment Provider Web Site."
hidden: false
createdAt: "2020-05-13T21:52:02.370Z"
updatedAt: "2020-05-18T23:12:15.247Z"
---
VTEX will redirect the store administrator to the Payment Provider Web Site using the <code>token</code> previously returned in the previous call.

At this point the Provider shows, the login/logon web site to the store administrator and he/she authorize to VTEX use your integration as a valid Payment Provider Processor. At this time
your server generate an <b>authorizationCode</b>.



#### REQUEST EXAMPLES AND THEIR RESPONSES
---
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET '{providerBaseUrl}/authorization/redirect?token={token}&applicationId=vtex' \\\n--data-raw ''",
      "language": "curl",
      "name": "2. Redirect"
    }
  ]
}
[/block]