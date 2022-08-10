---
title: "Container"
slug: "hibrido-components-container"
excerpt: "hibrido.components@0.0.8"
hidden: true
createdAt: "2022-07-14T18:53:07.322Z"
updatedAt: "2022-07-29T12:20:11.753Z"
---
Bloco que funciona como uma Div, podendo ser utilizada principalmente para englobar conteúdo.

## Exemplos:

### Sem Tag Custom:

```json
"container": {
    "children": [
        "outrosBlocos"
    ]
}
```

Resultado:
```html
<div class="hibrido-components-X-x-container">
    Outros blocos
</div>
```

### Com Tag custom

```json
"container": {
    "props": {
        "tag": "section"
    },
    "children": [
        "outrosBlocos"
    ]
}
```

Resultado:
```html
<section class="hibrido-components-X-x-container">
    Outros blocos
</section>
```

## Comportamento Responsivo

Quando o elemento está em uma tela Mobile ele adiciona 2 modificadores extras a sua classe, o primeiro modificador é o `--mobile` e o segundo é referente ao tipo de dispositivo podendo ser `--phone` ou `--tablet`.

Sendo assim quando estivermos utilizando o container em um celular ele terá as seguintes classes:

```css
.container
.container--mobile
.container--phone
```

## Propriedades:

| Nome         | Tipo            | Descrição    | Valor padrão |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `tag`        | Alguma Tag que possa ter conteúdo     | Tag utilizada para englobar os elementos | `"div"` |
| `blockClass`        | `string`     | Modificador para a classe | `""` |