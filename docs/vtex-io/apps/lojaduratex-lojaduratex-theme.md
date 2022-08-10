---
title: "Dùvidas Iniciais de Start do Projeto"
slug: "lojaduratex-lojaduratex-theme"
excerpt: "lojaduratex.lojaduratex-theme@1.10.42"
hidden: true
createdAt: "2022-07-07T19:34:14.958Z"
updatedAt: "2022-08-03T16:56:53.201Z"
---
instalação do CLI Toolbet

```
 yarn global add vtex
```

Fazendo login na conta

```
 vtex login {account}
```

Criando a workspace para trabalhar

```
$ vtex use {newstore}
```

## Dúvidas pertinentes aos módulos

Neste Issue podemos tirar dúvidas pertinentes ao IO

[store-discussion](https://github.com/vtex-apps/store-discussion)
[documentation-vtex.io](https://vtex.io/docs/getting-started/build-stores-with-vtex-io/3)

https://github.com/vtex-apps

## Módulos primordiais para não ter problemas ao rodar o projeto

Devido a alguns problema com o layout, foi necessário rodar a instalação de alguns componentes na mão.

vtex update

-   vtex install vtex.store-sitemap vtex.store vtex.rewriter --force vtex.admin-pages vtex.colossus-legacy-proxy@2.x
-   vtex install vtex.store
-   vtex install vtex.rewriter --force
-   vtex install vtex.admin-pages
-   vtex install vtex.colossus-legacy-proxy@2.x // este então principalmente se não nenhuma das outras páginas será renderizada

vtex install vtex.ab-tester@0.x vtex.admin-graphql-ide@3.x vtex.admin-search@1.x vtex.messages@1.x vtex.order-placed@1.x vtex.search-graphql@0.x vtex.social-selling@0.x
    vtex install vtex.store-sitemap vtex.store vtex.rewriter --force vtex.admin-pages vtex.colossus-legacy-proxy@2.x vtex.builder-hub

vtex install vtex.admin-search vtex.search-resolver@1.x

fonte: https://vtex.io/docs/getting-started/build-stores-with-vtex-io/3

## Estilização CSS

A premissa é ter instalado:

-   vtex.stack-layout,
-   vtex.rich-text
-   vtex.store-footer

como tudo é pensado como componente a regra para css também é a mesma.
exemplo debugando um elemento do Dom: colocar ao final da url o seguinte parametro **?\_\_inspect**

**vtex-rich-text-0-x-paragraph--description**
**vtex-rich-text** é o nome do arquivo/component que precisa estar na pasta css.

> css/vtex-rich.text.css

e dentro dele precisamos ter uma chamada para

```
.paragraph--description{
color: white
}
```

**fonts personalizadas**
Com relação a edição de fontes este é feito por dentro do cms
exemplo : https://store2--fensacl.myvtex.com/admin/cms/styles

e a chamada é feita dentro do projeto dentro style/configs/syle.json

## Plus - Edição do Readme.md

[https://stackedit.io/app#](https://stackedit.io/app#)

## Ambiente de Desenvolvimento

Prettier - Padronização da formatação do projeto

npm install prettier -D

No VScode dar Ctrl+ shift+ P
Buscar o comando por "Prettier Configure File" e criar este arquivo na pasta do projeto

Buscar novamente no Vscode por Preferences Open Settings(Json)

Adiconar a seguinte linha a baixo

{
"editor.defaultFormatter": "esbenp.prettier-vscode",
"editor.formatOnSave": true
}

Referencia : https://glebbahmutov.com/blog/configure-prettier-in-vscode/