---
title: "Custom Query"
slug: "lebiscuit-le-store-customquery"
excerpt: "lebiscuit.le-store@1.2.21"
hidden: true
createdAt: "2022-07-18T20:20:57.848Z"
updatedAt: "2022-08-08T21:35:41.667Z"
---
Esse artigo explica como utilizar o componente *Custom Query* e configurar as páginas customizadas
no site-editor da VTEX.


## Criação de uma página de resultados de pesquisa personalizada

[Documentação sobre custom query](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-creating-a-custom-search-results-page)

Código de exemplo: 
```
{
  "store.custom#colecao": {
    "children": ["search-result-layout.customQuery#colecao"]
  },
  "search-result-layout.customQuery#colecao": {
    "blocks": [
      "search-result-layout.desktop",
      "search-result-layout.mobile",
      "search-not-found-layout"
    ],
    "props": {
      "querySchema": {
        "maxItemsPerPage": 20,
        "queryField": "1326",
        "mapField": "productClusterIds",
        "simulationBehavior": "skip",
        "skusFilter": "ALL_AVAILABLE",
        "hideUnavailableItems": "true",
        "__unstableProductOriginVtex": true
      }
    },
    "title": "Coleção de produtos"
  }
}
```

Pontos importantes na configuração:
- [queryField](https://github.com/vtex-apps/search-result)
- [mapField](https://github.com/vtex-apps/search-result)


## Administrador da conta

Entre na `seção CMS` e depois clique em `páginas`

[Criar caminho das página customizada](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-creating-a-new-custom-page)


Você deve guardar o TITLE e a URL, iremos utilizar no próximo passo

Title: nomedotitulo

Padrão para URL: /colecao/*nomedotitulo*

Em templates selecione `store.custom#colecao`.

Exemplo: https://ibb.co/xMjSQPb


## Site Editor

Entre na `seção CMS` e depois clique em `Site Editor`

Pesquise na URL o nome da página que você criou no passo anterior e clique em coleção de produtos.
Imagem: https://prnt.sc/15elbbe

Portanto será apresentado várias opções para configuracão, altere a `query` para o `id da coleção` ou string conforme
as imagens abaixo.

Imagem: https://prnt.sc/15elksb

Query: https://prnt.sc/15em48x

Você pode localizar o id da coleção na plataforma VTEX em catálogo/coleções ou através da url no site. 

admin da VTEX: https://prnt.sc/15emo9g
site: https://prnt.sc/15embj4