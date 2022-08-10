---
title: "MZ - MY STORES"
slug: "panamericanaio-mz-mystores"
excerpt: "panamericanaio.mz-mystores@0.0.2"
hidden: true
createdAt: "2022-07-13T14:15:35.485Z"
updatedAt: "2022-07-13T14:15:35.485Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-green.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

Esse Aplicativo tem o intuito de mostrar de forma simples e intuitiva as lojas mais proximas usando o google maps e a localização atual do usuário. 

![Media Placeholder](https://user-images.githubusercontent.com/94864381/157300326-7c2c0df5-54b3-4319-89da-03f9d363c2e4.png)

Depois de instalado você poderá acessar a url https://{sualoja}.com/nossas-lojas

## Configuração 
Nosso aplicativo é baseado nos pontos de retirada (pickup points) cadastrados no admin, e serão exibimos independente se estiver ativo ou não, para saber mais sobre cadastro de pontos de retirada [acesse o link](https://help.vtex.com/pt/tutorial/cadasntro-de-pontos-de-retirada--2R5ClQiwe4KoSQgsuiOw4E), alem disso para conseguirmos usar o app, precisamos fazer as seguintes configurações, Vamos lá:

1. Liberar a [Restricting API keys](https://developers.google.com/maps/documentation/maps-static/get-api-key#console_1) do google (Restricting API keys é a liberação para usarmos o maps apenas com o dominio da nossa loja)

2. Acessar a pagina do aplicativo usando o admin da loja, e preencher os campos principais de **Vtex App Key** e **Vtex App Token**

Nosso app tem a possibilidade de você customizar os markers ![minimarket](https://user-images.githubusercontent.com/94864381/157514480-59fe1ae8-2453-49a2-a54f-500f7b64f4d8.png) e esconder algumas lojas especificas 

![nossa-lojas-configs](https://user-images.githubusercontent.com/94864381/157521509-c5851dbe-dc27-4dd8-9acf-2fec2f2314aa.png)

### descrição das configurações `props`

| Prop name                                         | Type            | Description                                                     | Default value |
| ------------------------------------------------  | --------------- | ----------------------------------------------------------------|---------------|
| `Pin de loja personalizada`                       | string        | url com o link do marker em png, recomendado que   sub a imagem na vtex e depois use o link gerado para esse campo |   null             |
| `Pin de local do usuario cor personalizada`       | string        | cores em hexadecimal                                            | null        |
| `Pin de loja cor personalizada`                   | string        | cores em hexadecimal                                            | null        |
| `Ids das Lojas Excludentes`                       | string        | ids dos pontos de retiradas separados por ponto e virgula(;)    | null        |
| `Vtex App Key`                                    | string        | Chave gerada pelo Administrador da conta                        | null        |
| `Vtex App Token`                                  | string        | Chave gerada pelo Administrador da conta                        | null        |


## Customization

Caso você queira estilizar a ferramenta, essas são as classes  de CSS Handles :

| CSS Handles           |
| ----------------------|
| `map`                 | 
| `mapBody`             | 
| `mapFilter`           | 
| `mapGoogle`           | 
| `mapSelectState`      |
| `mapSelectCity`       |
| `mapSelector`         |
| `mapFormSubTitleDiv`  |
| `mapStoresList`       |
| `mapFormSubTitle`     |
| `mapContainer`        |
| `selectFilter`        |
| `tooltipLabelText`    |
| `store`               |
| `storeName`           |
| `storeAdress`         |
| `storeCityState`      |
| `storeDesc`           |
| `mapFormTop`          |
| `mapFormTitle`        |
| `mapFormDescription`  |


<!-- DOCS-IGNORE:start -->

## Contributors ✨

Agradecemos aos brabos do desenvolvimento:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

<table>
  <tr>
    <td align="center"><a href="https://github.com/lucassto/"><img src="https://avatars.githubusercontent.com/u/94864381?v=4" width="100px;" alt=""/><br /><sub><b>Lucas Silva</b></sub></a><br /><a href="https://github.com/maeztra/MZ-MYSTORES/commits?author=lucassto" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/pratesrodrigo"><img src="https://avatars.githubusercontent.com/u/60141864?v=4" width="100px;" alt=""/><br /><sub><b>Rodrigo Prates</b></sub></a><br /><a href="https://github.com/maeztra/MZ-MYSTORES/commits?author=pratesrodrigo" title="Code">💻</a></td>  
  </tr>
</table>

<!-- DOCS-IGNORE:end -->