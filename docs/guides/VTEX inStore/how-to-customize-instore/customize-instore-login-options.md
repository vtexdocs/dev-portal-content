---
title: "Customize inStore login options"
slug: "customize-instore-login-options"
hidden: false
createdAt: "2021-08-11T17:18:29.656Z"
updatedAt: "2022-02-24T20:33:34.298Z"
---
To allow your [inStore](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc) sales associates to use custom login options, such as using their Google or Facebook accounts, follow the instructions in this guide.

## Prerequisites

Make sure you meet these requirements before you proceed with the customization:

1. When you [add a new sales associate to inStore](https://help.vtex.com/en/tracks/instore-getting-started-and-setting-up--zav76TFEZlAjnyBVL5tRc/5PSjRstg7UU4lOm0s8aqKN), you should register them with their Google email address — if you want them to log in with Google — or the email address registered on their Facebook account — if you want them to log in with Facebook.
2. It is necessary that you enable using Google or Facebook accounts as login options in your VTEX account, by following the instructions in [this article](https://help.vtex.com/en/tutorial/configuring-login-with-facebook-and-google--tutorials_513).

## Edit the `checkout-instore-custom.js` file

To set custom login options, you can copy the example code below and insert it in the [`checkout-instore-custom.js` file](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore), using different value combinations for the `auth` object properties: `showLoginAndPassword`, `showSaml`, and `oAuthProviderName`.
[block:code]
{
  "codes": [
    {
      "code": "window.INSTORE_CONFIG = {\n  auth: {\n    showLoginAndPassword: true,\n    showSaml: false,\n    oAuthProviderName: 'Google',\n  },\n}",
      "language": "javascript"
    }
  ]
}
[/block]
Read the description of each property before applying customizations:

[block:parameters]
{
  "data": {
    "h-0": "Name",
    "h-1": "Type",
    "h-2": "Description",
    "h-3": "Possible values",
    "0-0": "`showLoginAndPassword`",
    "1-0": "`showSaml`",
    "2-0": "`oAuthProviderName`",
    "0-1": "boolean",
    "1-1": "boolean",
    "2-1": "string",
    "0-2": "Always show the option to log in using email and password. By default, this option is set to `true`. Set to `false` to hide email and password form.",
    "1-2": "Always show the option to log in via SAML [if it is configured on VTEX ID](https://developers.vtex.com/vtex-rest-api/docs/login-integration-guide-admin-saml2). By default, this option is set to `true`. Set to `false` to hide the option to log in via SAML.",
    "2-2": "Always show the option to log in with either Google or Facebook, if the option is configured on VTEX ID.\n\nBy default, this option is set as `undefined`, that is, set not to show on the login page.\n\nSet it to a valid OAuth provider to VTEX ID knowledge and this login option will appear if there is no SAML login configured on VTEX ID and if the `showSaml` option is set to `false `also.",
    "0-3": "`true` or `false`",
    "1-3": "`true` or `false`",
    "2-3": "`Google` or `Facebook`"
  },
  "cols": 4,
  "rows": 3
}
[/block]
