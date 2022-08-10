---
title: "Store theme"
slug: "decorcolorstintas-store-theme"
excerpt: "decorcolorstintas.store-theme@2.0.4"
hidden: true
createdAt: "2022-07-12T19:30:36.684Z"
updatedAt: "2022-07-26T13:25:31.565Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
Our boilerplate theme to create stores in the VTEX IO platform.

## Preview
![store-theme-default](https://user-images.githubusercontent.com/1354492/63937047-e8d81c80-ca37-11e9-86fc-61e88847bbfb.png)

## Tutorial
To understand how things work check our tutorial [Build a store using VTEX IO](https://vtex.io/docs/getting-started/build-stores-with-store-framework/1/)

## Dependencies
All store components that you see on this document are open source too. Production ready, you can found those apps in this GitHub organization.

Store framework is the baseline to create any store using _VTEX IO Web Framework_.
- [Store](https://github.com/vtex-apps/store/blob/master/README.md)

Store GraphQL is a middleware to access all VTEX APIs.
- [Store GraphQL](https://github.com/vtex-apps/store-graphql/blob/master/docs/README.md)

### Store Component Apps
- [Header](https://github.com/vtex-apps/store-header/blob/master/docs/README.md)
- [Footer](https://github.com/vtex-apps/store-footer/blob/master/docs/README.md)
- [Slider Layout](https://github.com/vtex-apps/slider-layout/blob/master/docs/README.md)
- [Shelf](https://github.com/vtex-apps/shelf/blob/master/docs/README.md)
- [Telemarketing](https://github.com/vtex-apps/telemarketing/blob/master/docs/README.md)
- [Menu](https://github.com/vtex-apps/menu/blob/master/docs/README.md)
- [Login](https://github.com/vtex-apps/login/blob/master/docs/README.md)
- [Minicart](https://github.com/vtex-apps/minicart/blob/master/docs/README.md)
- [Category Menu](https://github.com/vtex-apps/category-menu/blob/master/docs/README.md)
- [Product Summary](https://github.com/vtex-apps/product-summary/blob/master/docs/README.md)
- [Breadcrumb](https://github.com/vtex-apps/breadcrumb/blob/master/docs/README.md)
- [Search Result](https://github.com/vtex-apps/search-result/blob/master/docs/README.md)
- [Product Details](https://github.com/vtex-apps/product-details/blob/master/docs/README.md)
- [Store Components](https://github.com/vtex-apps/store-components/blob/master/docs/README.md)
- [Order Placed](https://github.com/vtex-apps/order-placed/blob/master/docs/README.md) 

### Store Pixel Apps

 - [Facebook Pixel](https://github.com/vtex-apps/facebook-pixel/blob/master/docs/README.md)
 - [Google Tag Manager](https://github.com/vtex-apps/google-tag-manager/blob/master/docs/README.md)

## Contributing

Check it out [how to contribute](https://github.com/vtex-apps/awesome-io#contributing) with this project.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="http://www.hugoccosta.com"><img src="https://avatars2.githubusercontent.com/u/20212776?v=4" width="100px;" alt=""/><br /><sub><b>Hugo Costa</b></sub></a><br /><a href="https://github.com/vtex-apps/store-theme/commits?author=hugocostadev" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

# Readme Deploy Vtex 

- Crie a sua workspace para desenvolvimento `vtex use {{ nome da workspace }}` e desenvolva sua feature

- Após finalizar sua feature, "commite" no repositorio e crie o PR de deploy para master

- Uma vez "mergeado" o deploy deve-se executar um dos seguintes comandos:

```
vtex release major stable
```
> Para lançar uma nova versão MAJOR estavel.

```
vtex release minor stable
```
> Para lançar uma nova versão MINOR estavel.

```
vtex release patch stable
```
> Para lançar uma nova versão PATCH estavel.

- Deverá aparer uma pergunta questionando se deseja publicar a versão na Vtex, caso responda sim, não é necessário rodar o comando abaixo.
Caso contrário, execute o comando abaixo: 

```
vtex publish
```
> Publica a release na infraestrutura da vtex 

- Após publicado a release, crie uma workspace de produção `vtex use {{nome da worskpace}} --production` 

- Após a criação da workspace, instale a release gerada no passo anterior: 

```
vtex install {appvendor}.{appname}@{appversion}
```
> Ex: vtex install decorcolorstintas.store-theme@1.0.1. Atente-se a appversion gerada na release

- Apos a instalação e validação de sua feature na workspace criada de produção, rode: 
```
vtex deploy {appvendor}.{appname}@{appversion}
```
> Ex: vtex deploy decorcolorstintas.store-theme@1.0.1 
> Utilize o parametro --force caso não queira aguardar 7 minutos de testes obrigatorios pela vtex

- Após o deploy, promova sua workspace para master
```
vtex workspace promote
```
> Esse é o comando que atualizará sua loja