---
title: "3. Return to VTEX"
slug: "3returntovtex"
excerpt: "The PROVIDER will redirect the store administrator to the VTEX Web Site."
hidden: false
createdAt: "2020-05-13T21:52:02.370Z"
updatedAt: "2020-05-18T23:14:14.050Z"
---
The PROVIDER will redirect the store administrator to the VTEX Web Site using the `returnUrl` passed from VTEX to create token.

The returnUrl MUST be filled with your **authorizationCode**

You redirect the store administrator to the `returnUrl` previously sent, see that the url has an authorizationCode parameter in the Query string that you fill before redirect.

Example:  

If you receive an URL  `https://store.vtex.com/return?authorizationCode=&otherparams...`

and your **authorizationCode** was pro2018

Then you redirect the store administrator to:

`https://store.vtex.com/return?authorizationCode=pro2018&otherquerystringparameters`



#### REQUEST EXAMPLES AND THEIR RESPONSES
---
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET '{returnUrl}/?authorizationCode={providerAuthorizationCode}' \\\n--data-raw ''",
      "language": "curl",
      "name": "3. Return to VTEX"
    }
  ]
}
[/block]