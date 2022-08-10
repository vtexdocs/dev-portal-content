---
title: "OpenGraph"
slug: "hibrido-components-opengraph"
excerpt: "hibrido.components@0.0.8"
hidden: true
createdAt: "2022-07-14T18:53:07.470Z"
updatedAt: "2022-07-29T12:20:11.763Z"
---
Conjunto de Blocos para adicionar suporte ao [OpenGraph(Embed)](https://ogp.me/) em várias áreas do site (Home, Busca e PDP).
Os blocos precisam ser adicionados em lugares específicos para funcionarem de maneira apropriada.

Esse componente serve apenas para termos um bloco de OpenGraph que possa ser utilizado, sendo que ele apenas exporta os componentes [OG Nativos](https://github.com/vtex-apps/open-graph) da Vtex.

## Exemplos:

Para adicionar o OpenGraph a `Home` é necessário inserir diretamente nos blocos do `store.home`:

```json
"store.home": {
    "blocks": [
        "home-open-graph"
    ]
}
```

Para adicionar o OpenGraph na busca é necessário inserir nos blocos do `store.search`:

```json
"store.search": {
    "blocks": [
        "search-open-graph"
    ]
}
```

E para adicionar no PDP é necessário inserir diretamente no bloco do `store.product`:

```json
"store.product": {
    "blocks": [
        "product-open-graph"
    ]
}
```


## Propriedades:

Esse componente não possui nenhuma propriedade.