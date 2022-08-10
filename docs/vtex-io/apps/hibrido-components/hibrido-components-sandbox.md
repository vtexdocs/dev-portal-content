---
title: "Sandbox"
slug: "hibrido-components-sandbox"
excerpt: "hibrido.components@0.0.8"
hidden: true
createdAt: "2022-07-14T18:53:07.416Z"
updatedAt: "2022-07-29T12:20:11.781Z"
---
Bloco responsável por inserir HTML de maneira arbitrária no Site.

## Exemplo:

```json
"sandbox": {
    "props": {
        "where": "head",
        "element": "script",
        "elementProps": {
            "type": "text/javascript"
        },
        "content": "console.log('Hello World')"
    }
}
```

## Propriedades:

| Nome         | Tipo            | Descrição    | Valor padrão |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `where`        | `"head"` ou `"body"`      | Onde o elemento será inserido | `"body"` |
| `element`      | `string`                  | A tag que você deseja criar   | `undefined` |
| `elementProps` | `object`                  | Objeto com os atributos que o elemento deverá ter. Os atributos `data-id` e `innerHtml` não podem ser utilizados   | `undefined` |
| `content`      | `string`                  | Conteúdo da Tag, será inserido dentro da tag via `innerHtml`   | `""` |
| `blockClass`        | `string`     | Modificador para a classe | `""` |