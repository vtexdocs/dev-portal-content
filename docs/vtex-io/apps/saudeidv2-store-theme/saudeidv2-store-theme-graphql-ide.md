---
title: "Query da mutation"
slug: "saudeidv2-store-theme-graphql-ide"
excerpt: "saudeidv2.store-theme@0.7.10"
hidden: true
createdAt: "2022-08-09T13:22:46.345Z"
updatedAt: "2022-08-09T15:53:01.346Z"
---
mutation Save($saveArgs: SaveArgsV2!) {
  saveV2(args: $saveArgs)
}

# Tooltip pdp
{
  "saveArgs": {
    "to": "pt-BR",
    "messages": [
      {
        "srcLang": "en-DV",
        "srcMessage": "store/add-to-cart.success",
        "context": "vtex.add-to-cart-button@0.x",
        "targetMessage": "Item adicionado à sua cesta"
      }
    ]
  }
}

# Titulo Orderplaced
{
  "saveArgs": {
    "to": "pt-BR",
    "messages": [
      {
        "srcLang": "en-DV",
        "srcMessage": "store/header.thanks",
        "context": "vtex.order-placed@2.x",
        "targetMessage": "Agradecemos a sua compra!"
      }
    ]
  }
}

# Tipo de pagamento Orderplaced
{
  "saveArgs": {
    "to": "pt-BR",
    "messages": [
      {
        "srcLang": "en-DV",
        "srcMessage": "store/header.bankinvoice.header",
        "context": "vtex.order-placed@2.x",
        "targetMessage": "{paymentSystemName}: a pagar"
      }
    ]
  }
}

# Mensagem principal no Orderplaced
{
  "saveArgs": {
    "to": "pt-BR",
    "messages": [
      {
        "srcLang": "en-DV",
        "srcMessage": "store/header.email",
        "context": "vtex.order-placed@2.x",
        "targetMessage": "Você vai receber um e-mail com todos os detalhes no endereço: {userEmail}"
      }
    ]
  }
}

# Button Orderplaced 
{
  "saveArgs": {
    "to": "pt-BR",
    "messages": [
      {
        "srcLang": "en-DV",
        "srcMessage": "store/order.header.myorders.button",
        "context": "vtex.order-placed@2.x",
        "targetMessage": "Ir para pedidos"
      }
    ]
  }
}

# Maior valor
{
  "saveArgs": {
    "to": "pt-BR",
    "messages": [
      {
        "srcLang": "en-DV",
        "srcMessage": "store/ordenation.price.descending",
        "context": "vtex.search-result@3.x",
        "targetMessage": "Maior valor"
      }
    ]
  }
}

# Menor valor
{
  "saveArgs": {
    "to": "pt-BR",
    "messages": [
      {
        "srcLang": "en-DV",
        "srcMessage": "store/ordenation.price.ascending",
        "context": "vtex.search-result@3.x",
        "targetMessage": "Menor valor"
      }
    ]
  }
}