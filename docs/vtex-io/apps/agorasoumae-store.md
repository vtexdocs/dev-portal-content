---
title: "Agora Sou Mãe"
slug: "agorasoumae-store"
excerpt: "agorasoumae.store@2.0.25"
hidden: true
createdAt: "2022-07-05T18:25:37.861Z"
updatedAt: "2022-07-25T12:04:43.719Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
Boilerplate padrão para start de projeto.

## Como rodar?
Basta clonar o projeto e abrir em seu editor preferido.
Abre seu **terminal** e execute `vtex login account-name` (account-name é o nome da sua conta de trabalho).

Após realizar seu **login** crie um [workspace](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-workspace) para trabalhar, para isto rode o comando `vtex use workspace-name` (workspace-name é o nome que deseja atribuir para seu ambiente de desenvolvimento). 

Agora basta linkar sua aplicação para começar trabalhar, para isto rode o comando `vtex link`. (Este link ira gerar uma url de seu ambiente dev e você podera acompanhar as alterações em tempo real).

### Estrutura do projeto
Para criação de novos blocos respeitar a estrutura de pastas criada dentro de **store**:
- Declarar os blocos sempre em arquivos separados e organizados pelas pastas de suas respectivas `media queries`.

Para criação de estilos novos respeitar a estrutura de pastas criada dentro de **styles**.
- Declarar os novos estilos sempre em arquivos separados e organizados pelas pastas de suas respectivas `media queries`.

Novas imagens devem ser inseridas dentro da pasta **assets/imgs**:
- Como chama-las nos blocos? `assets/imgs/banners/banner-home-mobile.png`

Novas fontes devem ser inseridas dentro da pasta **assets/fonts**:
- As fonts devem conter extensão `ttf`.

### Componentes
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

### Componentes pixels

 - [Facebook Pixel](https://github.com/vtex-apps/facebook-pixel/blob/master/docs/README.md)
 - [Google Tag Manager](https://github.com/vtex-apps/google-tag-manager/blob/master/docs/README.md)