---
title: "Change MiniCart checkout button"
slug: "useblu-theme-cartcheckoutbutton"
excerpt: "useblu.theme@1.0.18"
hidden: true
createdAt: "2022-07-25T17:25:32.601Z"
updatedAt: "2022-08-08T17:31:26.826Z"
---
> edit in `vtex.messages@1.65.0`

## Portuguese

### Mutation

```gql
  mutation Save($saveArgs: SaveArgsV2!) {
    saveV2(args: $saveArgs)
  }
```

### Query

```gql
  {
    "saveArgs": {
      "to": "pt-BR",
      "messages": [
        {
          "srcLang": "en-DV",
          "srcMessage": "store/minicart.go-to-checkout",
          "context": "vtex.minicart@2.x",
          "targetMessage": "Solicitar Cotação"
        }
      ]
    }
  }
```