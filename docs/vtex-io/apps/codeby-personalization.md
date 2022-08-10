---
title: "Personalization APP"
slug: "codeby-personalization"
excerpt: "codeby.personalization@2.0.12"
hidden: true
createdAt: "2022-07-07T06:04:21.936Z"
updatedAt: "2022-08-04T09:47:40.995Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

Este aplicativo permite uma maior possibilidade de customização para produtos personalizados na sua loja

![Personalization App](./example.png)

## Instalação

Para fazer a instalação do Personalization APP precisaremos fazer os seguintes pontos.

1. Criação das Entidades no masterdata
2. Criação do Attachment Personalization
3. Salvar o ID do Attachment Personalization no Masterdata
4. Instalar o APP Personalization
5. Adicionar Link Personalization na loja

## 1. Criação das Entidades no masterdata

o personalization app precisa de 3 entidades no masterdata para funcionar

- Personalization Order APP
  - Salva as imagens e texto de um pedido
- Personalization Product APP
  - Salva as informações de um produto personalizado
- Personaliztion Configuration APP
  - Salva a configuração do APP

### `Order Personalization APP`

Acronym: `AP`

Name: `Order Personalization App`

| Name               | Display Name         | Type             |
| ------------------ | -------------------- | ---------------- |
| `id`               | Document ID          | `Auto Increment` |
| `confirmPreview`   | Preview Confirmation | `Boolean`        |
| `finalImageHeight` | Final Image Height   | `Varchar (50)`   |
| `finalImageWidth`  | Final Image Width    | `Varchar (50)`   |
| `image`            | Image                | `File`           |
| `imageHeight`      | Image Height         | `Varchar (50)`   |
| `imagePositionX`   | Image Position X     | `Varchar (50)`   |
| `imagePositionY`   | Image Position Y     | `Varchar (50)`   |
| `imageRotation`    | Image Rotation       | `Varchar (50)`   |
| `imageWidth`       | Image Width          | `Varchar (50)`   |
| `orderId`          | Order ID             | `Varchar (750)`  |
| `preview`          | Preview              | `File`           |
| `text`             | Text                 | `Varchar (750)`  |
| `textAlign`        | Text Align           | `Varchar (50)`   |
| `textColor`        | Text Color           | `Varchar (50)`   |
| `textFont`         | Text Font            | `Varchar (50)`   |
| `textHeight`       | text Height          | `Varchar (50)`   |
| `textPositionX`    | Text Position X      | `Varchar (50)`   |
| `textPositionY`    | Text Position Y      | `Varchar (50)`   |
| `textRotation`     | Text Rotation        | `Varchar (50)`   |
| `textSize`         | Text Size            | `Varchar (50)`   |
| `textWidth`        | text Width           | `Varchar (50)`   |

### `Personalization Product APP`

Acronym: `PP`

Name: `Personalization Product App`

| Name               | Display Name       | Type             |
| ------------------ | ------------------ | ---------------- |
| `id`               | Document ID        | `Auto Increment` |
| `customAreaRotate` | Custom Area Rotate | `Decimal`        |
| `customAreaHeight` | Custom Area Height | `Decimal`        |
| `customAreaWidth`  | Custom Area Width  | `Decimal`        |
| `customPositionX`  | Custom Position X  | `Decimal`        |
| `customPositionY`  | Custom Position Y  | `Decimal`        |
| `defaultImage`     | Default Image      | `Varchar (750)`  |
| `hasImage`         | Has Image          | `Boolean`        |
| `hasText`          | Has Text           | `Boolean`        |
| `imageHeight`      | Image Height       | `Decimal`        |
| `imageWidth`       | Image Width        | `Decimal`        |
| `isActive`         | Active             | `Boolean`        |
| `serviceId`        | Service ID         | `Varchar (100)`  |
| `skuID`            | Sku ID             | `Varchar (100)`  |
| `skuName`          | Sku Name           | `Varchar (100)`  |

### `Product Personalization APP`

Acronym: `AP`

Name: `Product Personalization App`

| Name           | Display Name  | Type             |
| -------------- | ------------- | ---------------- |
| `id`           | Document ID   | `Auto Increment` |
| `attachmentID` | Attachment ID | `Varchar (100)`  |

- `propName` object:

| Prop name | Type     | Description | Default value |
| --------- | -------- | ----------- | ------------- |
| `XXXXX`   | `XXXXXX` | XXXXXXXX    | `XXXXXX`      |

## 2. Criação do Attachment Personalization

Na administração VTEX vá para area de anexos em `Catálogo > Anexos`, clique em Novo Anexo.

Em Nome coloque exatamente o nome `Personalization` e marque a opção Status para deixar ativado e clique em salvar

| ATENÇÃO! é importante que o nome do anexo seja exatamente o informado para o aplicativo funcionar |
| ------------------------------------------------------------------------------------------------- |

Após salvar clique na opção de modificar o Anexo que você criou

Adicione os seguintes campos com os devidos limites e depois clique em salvar

| Key Name     | Maximum Number of Characters |
| ------------ | ---------------------------- |
| `preview`    | 255                          |
| `image`      | 255                          |
| `text`       | 255                          |
| `color`      | 255                          |
| `fontSize`   | 255                          |
| `fontFamily` | 255                          |

## 3. Salvar o ID do Attachment Personalization no Masterdata

Com o Anexo `Personalization` criado verifique qual o id dele e adicione no masterdata na entidade `Config Personalization App`

## 4. Instalar o APP Personalization

Para instalar o app apenas execute o seguinte comando

```
vtex install codeby.personalization@0.x
```

Adicione no seu manifest o seguinte bloco

```javascript
{
  "peerDependencies": {
    "codeby.personalization": "0.x"
  }
}
```

## 5. Adicionar Link Personalization na loja

Para adicionar um link para a pagina de personalização basta você chamar o componente `personalization-link` e colocar como filho o layout que você quer para o seu botão, o link somente irá aparecer quando o produto for personalizado

```javascript
{
  "personalization-link": {
    "children": ["rich-text#text-link"]
  }
}
```

## Customização

Caso deseje alterar o layout da pagina de personalização você pode montar o layout do componente de acordo com sua preferencia usando o seguinte código de base

```javascript
{
  "store.personalization": {
    "blocks": ["personalization#main"]
  },
  "personalization#main": {
    "props": {
      "colors": [
        "#000000",
        "#ffffff",
        "#233D69",
        "#AD2F5E",
        "#DCCDBB",
        "#B61839"
      ],
      "fonts": ["Arial", "Verdane", "Poppins"]
    },
    "children": ["flex-layout.row#personalization-container"]
  },
  "flex-layout.row#personalization-container": {
    "props": {
      "blockClass": "default-personalization"
    },
    "children": [
      "flex-layout.col#personalization-product-image",
      "flex-layout.col#personalization-content"
    ]
  },
  "flex-layout.col#personalization-product-image": {
    "children": ["personalization-product-image"]
  },
  "flex-layout.col#personalization-content": {
    "props": {
      "blockClass": "product-info"
    },
    "children": [
      "flex-layout.row#product-name",
      "flex-layout.row#product-description",
      "flex-layout.col#custom",
      "personalization-total",
      "personalization-preview",
      "rich-text#personaliza-link"
    ]
  },
  "flex-layout.row#product-name": {
    "props": {
      "blockClass": ""
    },
    "children": ["product-name"]
  },
  "flex-layout.row#product-description": {
    "props": {
      "blockClass": ""
    },
    "children": ["product-description"]
  },
  "flex-layout.col#custom": {
    "props": {
      "blockClass": ""
    },
    "children": [
      "rich-text#personaliza",
      "personalization-custom-text",
      "rich-text#personaliza-image",
      "personalization-custom-image#demo"
    ]
  },
  "rich-text#personaliza": {
    "props": {
      "text": "Scegli la persona",
      "blockClass": "personaliza-text"
    }
  },
  "rich-text#personaliza-image": {
    "props": {
      "text": "IMMAGINE",
      "blockClass": "personaliza-image"
    }
  },
  "rich-text#personaliza-link": {
    "props": {
      "text": "[Termini e condizioni della personalizzazione](#)",
      "blockClass": "personaliza-link",
      "textAlignment": "RIGHT",
      "textPosition": "RIGHT"
    }
  },
  "personalization-custom-image#demo": {
    "props": {
      "images": ["assets/typeA1.png", "assets/typeA2.png", "assets/typeA3.png"]
    }
  },
  "personalization-preview": {}
}
```

### `personalization` props

| Prop name | Type    | Description              | Default value                                                   |
| --------- | ------- | ------------------------ | --------------------------------------------------------------- |
| `colors`  | `Array` | Lista de cores do texto  | `["#000000","#ffffff","#233D69","#AD2F5E","#DCCDBB","#B61839"]` |
| `fonts`   | `Array` | Lista de fontes do texto | `["Arial", "Verdane", "Poppins"]`                               |

### `personalization-custom-image` props

| Prop name | Type    | Description                   | Default value                                                     |
| --------- | ------- | ----------------------------- | ----------------------------------------------------------------- |
| `colors`  | `Array` | Lista de imagens predefinidas | `["assets/typeA1.png", "assets/typeA2.png", "assets/typeA3.png"]` |

| CSS Handles                      |
| -------------------------------- |
| `LoadingPageContainer`           |
| `LoadingPageTitle`               |
| `LoadingPageText`                |
| `LoadingPageSpinner`             |
| `NotFoundContainer`              |
| `NotFoundTitle`                  |
| `NotFoundText`                   |
| `PeviewModalBuyButton`           |
| `CustomImageContainer`           |
| `ProductImagePosition`           |
| `CustomImageBlock`               |
| `CustomImageLabel`               |
| `CustomImageOptions`             |
| `CustomImageOption`              |
| `CustomImageDropzone`            |
| `CustomImageDropzoneArea`        |
| `CustomImageDropzoneText`        |
| `CustomImageDropTrash`           |
| `CustomImageDropTrashButton`     |
| `CustomImageDropInfo`            |
| `CustomImageDropzoneInput`       |
| `CustomImageDropzoneInputText`   |
| `CustomImageOptionsTitle`        |
| `PreviewCanvas`                  |
| `ProductImageImage`              |
| `ProductImagePosition`           |
| `ProductImageContainer`          |
| `ProductImageRenderPreview`      |
| `PeviewModalHeader`              |
| `PeviewModalBottom`              |
| `PeviewModalBuyButton`           |
| `PeviewModalConfim`              |
| `PreviewButtonOpen`              |
| `TotalValueContainer`            |
| `TotalValueProduct`              |
| `TotalValueService`              |
| `TotalValueTotal`                |
| `PositionButtonsContainer`       |
| `PositionButtonsPlus`            |
| `PositionButtonsMinus`           |
| `PositionButtonsRotate`          |
| `PositionButtonsGoUp`            |
| `PositionButtonsGoRight`         |
| `PositionButtonsGoLeft`          |
| `PositionButtonsGoDown`          |
| `ProductImageCanvas`             |
| `ProductImageImage`              |
| `ProductImageContainer`          |
| `ProductImagePosition`           |
| `ProductImageRenderPreview`      |
| `ProductImageTextCustomOverflow` |
| `DRRWOverflow`                   |
| `DRRWMargin`                     |
| `DRRWrapper`                     |
| `DRRBox`                         |
| `DRRDot`                         |
| `DRRLeftTop`                     |
| `DRRLeftBottom`                  |
| `DRRTopMid`                      |
| `DRRBottomMid`                   |
| `DRRLeftMid`                     |
| `DRRRightMid`                    |
| `DRRRightBottom`                 |
| `DRRRightTop`                    |
| `DRRRotate`                      |
| `DRRRotateLink`                  |