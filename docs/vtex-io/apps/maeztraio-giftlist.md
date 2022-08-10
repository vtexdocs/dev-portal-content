---
title: "Giftlist"
slug: "maeztraio-giftlist"
excerpt: "maeztraio.giftlist@0.2.1"
hidden: true
createdAt: "2022-07-19T18:01:56.409Z"
updatedAt: "2022-07-19T18:01:56.409Z"
---
O app Giftlist é resposável por exibir as páginas do app de lista de presentes.

<!-- FALTA MEDIA PLACEHOLDER  -->

![Media Placeholder](https://user-images.githubusercontent.com/27385566/131178779-fdd7e2ff-6da3-470b-a3ee-886a59d2ba47.png)

## Configuração

### Step 1 - Adicionando o app Giftlist às suas dependencias do tema

No `manifest.json` do seu tema, adicione o Giftlist Edit page app como uma depêndencia:

```json
  "dependencies": {
    "maeztraio.giftlist": "0.x",
  }
```

Agora, você já pode usar todos os blocos exportados do app `giftlist`. Confira a lista abaixo:

| Block name              | Type          | Description                                                                |     |
| ----------------------- | ------------- | -------------------------------------------------------------------------- | --- |
| `giftlist-edit`         | `Obrigatório` | Bloco responsável por renderizar a página completa de edição               |
| `giftlist-manage`       | `Obrigatório` | Bloco responsável por renderizar a página completa de gerenciamento        |
| `giftlist-profile-edit` | `Obrigatório` | Bloco responsável por renderizar a página completa de editar o perfil      |
| `giftlist-my-lists`     | `Obrigatório` | Bloco responsável por renderizar a página completa de listas               |
| `giftlist-new-list`     | `Obrigatório` | Bloco responsável por renderizar a página completa de nova lista           |
| `giftlist-buy-page`     | `Obrigatório` | Bloco responsável por renderizar a página completa de produtos para compra |

### Step 2 - Criando as páginas do Giftlist

Para inserir o app `giftlist` em sua loja é necessário criar algumas páginas customizadas com o caminho `/giftlist/{page}` no arquivo routes.json, onde será usado os blocos do `giftlist`. Por exemplo:

```json
{
  "store.custom#mz-giftlist-edit": {
    "path": "/giftlist/edit"
  },
  "store.custom#mz-giftlist-manage": {
    "path": "/giftlist/manage"
  },
  "store.custom#mz-giftlist-profile-edit": {
    "path": "/giftlist/profile"
  },
  "store.custom#mz-giftlist-my-lists": {
    "path": "/giftlist"
  },
  "store.custom#mz-giftlist-new-list": {
    "path": "/giftlist/new-list"
  },
  "store.custom#mz-giftlist-buy-page": {
    "path": "/giftlist/list"
  }
}
```

### Step 3 - Adicionando o bloco à página

Após a página customizada estar definida, basta inserir o bloco `giftlist-edit` dentro dela. Por Exemplo:

```json
{
  "store.custom#mz-giftlist-edit": {
    "blocks": ["giftlist-edit"]
  },
  "store.custom#mz-giftlist-manage": {
    "blocks": ["giftlist-manage"]
  },
  "store.custom#mz-giftlist-profile-edit": {
    "blocks": ["giftlist-profile-edit"]
  },
  "store.custom#mz-giftlist-my-lists": {
    "blocks": ["giftlist-my-lists"]
  },
  "store.custom#mz-giftlist-new-list": {
    "blocks": ["giftlist-new-list"]
  },
  "store.custom#mz-giftlist-buy-page": {
    "blocks": ["giftlist-buy-page"]
  }
}
```

`Css Handles`

| CSS Handles                     |
| ------------------------------- |
| `Button`                        |
| `NewlistCardWrapper`            |
| `NewlistCard`                   |
| `NewlistCardRadio`              |
| `NewlistCardLabel`              |
| `editCategoryCard`              |
| `editCategoryCardContent`       |
| `editCategoriesTitle`           |
| `editCategoriesSubTitle`        |
| `dashboardPercent`              |
| `dashboardPercentValue`         |
| `dashboardPercentLabel`         |
| `dashboardBox`                  |
| `dashboardTitle`                |
| `dashboardGiftcardWrapper`      |
| `dashboardRow`                  |
| `dashboardContent`              |
| `profileEditDivider`            |
| `NewlistListWrapper`            |
| `NewlistList`                   |
| `NewlistListItem`               |
| `NewlistItemContent`            |
| `profileEditFormWrapper`        |
| `profileEditInput`              |
| `profileEditLabel`              |
| `headerCenterInfoTop`           |
| `headerNamesWrapper`            |
| `headerNames`                   |
| `headerList`                    |
| `headerDateWrapper`             |
| `headerDate`                    |
| `headerDateLabel`               |
| `headerPlaceholder`             |
| `headerProfileImage`            |
| `headerMyLists`                 |
| `headerCopyButton`              |
| `headerShareButton`             |
| `InputWrapper`                  |
| `Input`                         |
| `InputLabel`                    |
| `profileEditLink`               |
| `MyListsTitleLink`              |
| `MyListsLink`                   |
| `NewlistCircleWrapper`          |
| `NewlistCircle`                 |
| `dropdownWrapper`               |
| `BoughtProductLabel`            |
| `ProductListCardWrapper`        |
| `ProductListCardInfo`           |
| `ProductListCardImage`          |
| `ProductListCardNameWrapper`    |
| `ProductListCardName`           |
| `ProductListCardDetails`        |
| `ProductListCardQuantity`       |
| `ProductListCardPrice`          |
| `DeleteProductButton`           |
| `ProductListHeaderWrapper`      |
| `ProductListHeaderTitleWrapper` |
| `ProductListHeaderTitle`        |
| `ProductListHeaderSubtitle`     |
| `ProductListTabs`               |
| `ProductListTabsHeader`         |
| `ProductListTabsQuantity`       |
| `ProductListTabsQuantityLabel`  |
| `ProductListTabsQuantityNumber` |
| `ProductListCardWrapper`        |
| `ProductListCardWrapper`        |
| `ProductListSearchInput`        |
| `BuyProductsCard`               |
| `BuyProductsImageWrapper`       |
| `BuyProductsImage`              |
| `BuyProductsTitle`              |
| `BuyProductsButtonWrapper`      |
| `BuyProductsCard`               |
| `editCleanSideFilter`           |
| `editCollapsibleWrapper`        |
| `editDropdownWrapper`           |
| `editProductNotFound`           |
| `editProductCard`               |
| `editProductImage`              |
| `editProductImageWrapper`       |
| `editProductName`               |
| `editProductButtonWrapper`      |
| `editSelectedFilterLabel`       |
| `editMobileFilterTrigger`       |
| `editMobileFilter`              |
| `editMobileFilterHead`          |
| `editFilterTitle`               |
| `editMobileFilterTriggerClose`  |
| `NewlistProgressBar`            |
| `Subtitle`                      |
| `Title`                         |

## Contribuidores ✨

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/douglashbr"><img src="https://avatars.githubusercontent.com/u/27385566?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Douglas Dantas</b></sub></a><br /><a href="https://github.com/maeztra/MZ-GIFTLIST-VTEXIO-EDIT-HEADER/commits?author=douglashbr" title="Code">💻</a></td>
  </tr>
</table>