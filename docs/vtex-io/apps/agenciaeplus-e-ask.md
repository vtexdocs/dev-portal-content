---
title: "e-Ask"
slug: "agenciaeplus-e-ask"
excerpt: "agenciaeplus.e-ask@2.3.1"
hidden: true
createdAt: "2022-07-05T19:52:39.355Z"
updatedAt: "2022-07-07T14:36:50.522Z"
---
<!-- DOCS-IGNORE:start -->

[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

Uma ferramenta para **engajar** e **interagir** com clientes respondendo suas perguntas sobre produtos. O app do e-Ask da aos usuários uma maneira simples de fazer **perguntas** e elas a serem **respondidas**.

![Front end e-Ask](https://user-images.githubusercontent.com/86304065/123826934-96d3dc80-d8d6-11eb-9d3f-48abdc4351af.png)

## Configuração

1. Importe o app do e-Ask nas dependências do seu tema no `manifest.json`. Por exemplo:

```json
  "dependencies": {
    "agenciaeplus.e-ask": "0.x"
  }
```

2. Adicione o bloco do `e-ask` no template de produto. Por exemplo:

```json
 "store.product": {
    "children": [
      "flex-layout.row#product-breadcrumb",
      "flex-layout.row#product-main",
      "flex-layout.row#description",
      "shelf.relatedProducts",
      "product-reviews",
      "e-ask"
    ]
  },
```

### Props

| Nome                 | Título                               | Tipo     | Descrição                                                                     | Valor padrão                                                                              |
| -------------------- | ------------------------------------ | -------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `storeToken`         | Token da loja                        | `string` | Token e-Ask fornecido pela PluesLab                                           | `undefined`                                                                               |
| `mainTitle`          | Título principal                     | `string` | O primeiro título a aparecer no container do app                              | "Pergunte para a loja"                                                                    |
| `successMessage`     | Mensagem de succeso                  | `string` | Mensagem que aparecera no sucesso do envio da pergunta                        | "Pergunta enviada! :)"                                                                    |
| `failureMessage`     | Mensagem de erro                     | `string` | Mensagem que aparece qunado ha um erro no envio da pergunta                   | "Um erro ocorreu :("                                                                      |
| `mainColor`          | Cor de destaque                      | `string` | Cor dos elementos destacados no app                                           | "#0f3e99"                                                                                 |
| `messagePlaceHolder` | Placeholder para o campo de mensagem | `string` | Texto que ficara no `placeholder` no campo de texto no formulário de pergunta | "Faça uma pergunta ao vendedor"                                                           |
| `emailPlaceHolder`   | Placeholder para o campo de email    | `string` | Texto que ficara no `placeholder` no campo de email no formulário de pergunta | "seunome@provedor.com.br"                                                                 |
| `sendButtonText`     | Texto do botão                       | `string` | Texto do botão de enviar pergunta                                             | "Perguntar"                                                                               |
| description1         | Descrição 1                          | `string` | Primeiro texto após o formulário de pergunta                                  | "Fique tranquilo, seu e-mail será utilizado apenas para te notificar sobre sua resposta." |
| description2         | Descrição 2                          | `string` | Segundo texto após o formulário de pergunta                                   | "Não enviamos qualquer tipo de publicidade ou newsletter para sua caixa de menssagens."   |

![agencia-eplus-n-logo](https://user-images.githubusercontent.com/86304065/123873430-dae1d400-d90c-11eb-8cad-7ede510fcfec.png)