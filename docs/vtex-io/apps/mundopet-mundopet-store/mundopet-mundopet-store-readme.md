---
title: "App Messages Translations"
slug: "mundopet-mundopet-store-readme"
excerpt: "mundopet.mundopet-store@0.43.7"
hidden: true
createdAt: "2022-07-04T22:14:39.873Z"
updatedAt: "2022-08-09T14:48:44.494Z"
---
## VTEX Oficial Documentation

https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-overwriting-the-messages-app#app-messages-translations

## Mutation 

```
mutation Save($saveArgs: SaveArgsV2!) {
  saveV2(args: $saveArgs)
}
```

## Query Variables 

```
{
  "saveArgs": {
    "to": "pt-BR",
    "messages": [
      {
        "srcLang": "en-DV",
        "srcMessage": "shippingEstimatePickup-h",
        "context": "vtex.shipping-estimate-translator@2.x",
        "targetMessage": "{timeAmount, plural, =0 {Em alguns instantes} one {A partir de # hora} other {A partir de # horas}}"
      },
      {
        "srcLang": "en-DV",
        "srcMessage": "shippingEstimate-h",
        "context": "vtex.shipping-estimate-translator@2.x",
        "targetMessage": "{timeAmount, plural, =0 {Em alguns instantes} one {A partir de # hora} other {A partir de # horas}}"
      },
      {
        "srcLang": "en-DV",
        "srcMessage": "LoginSessionsScreen.backButton",
        "context": "vtex.my-authentication@1.x",
        "targetMessage": "Segurança"
      },
      {
        "srcLang": "en-DV",
        "srcMessage": "AuthenticationScreen.title",
        "context": "vtex.my-authentication@1.x",
        "targetMessage": "Segurança"
      },
      {
        "srcLang": "en-DV",
        "srcMessage": "ExtensionLinks.authentication",
        "context": "vtex.my-authentication@1.x",
        "targetMessage": "Segurança"
      }
    ]
  }
}
```