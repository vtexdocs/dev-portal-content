---
title: "Change MiniCart Title"
slug: "useblu-theme-carttitle"
excerpt: "useblu.theme@1.0.18"
hidden: true
createdAt: "2022-07-25T17:25:32.667Z"
updatedAt: "2022-08-08T17:31:26.687Z"
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
          "srcMessage": "store/minicart.title",
          "context": "vtex.minicart@2.x",
          "targetMessage": "Meu Carrinho"
        }
      ]
    }
  }
```