---
title: "Mensajes cambiados"
slug: "clubsoftyspe-store-theme-mensajes-cambiados-22"
excerpt: "clubsoftyspe.store-theme@0.5.170"
hidden: true
createdAt: "2022-07-18T05:01:12.673Z"
updatedAt: "2022-07-18T05:01:12.673Z"
---
-------

Se han cambiado ciertos mensajes de la aplicación por orden del cliente, el cual comenta que la palabra "Ítem" debe ser reemplazada por "Producto".

Para esto se ha seguido la siguiente documentación: [overwriting-the-messages-app](https://vtex.io/docs/recipes/development/overwriting-the-messages-app/)

Una vez instalado `vtex.admin-graphql-ide@3.x` se debe ejecutar la query `Save` con las variables que se indican, tambien es posible comprobar el valor actual del mensaje con la query `GetTranslation` utilizando los mismos parámetros.

`query` y `mutation`

```graphql
    query GetTranslation($srcMessage: String!, $context: String!, $depTree: String!) {
        translateWithDependencies(args: {
            indexedByFrom: [
                {
                    from: "en-DV"
                    messages: [
                        {
                        content: $srcMessage
                        context: $context
                        }
                    ]
                }
            ]
            to: "es-PE"
            depTree: $depTree
        })
    }

    mutation Save($srcMessage: String!, $context: String!, $targetMessage: String!) {
        saveV2(args: {
            to: "es-PE"
            messages: [
                {
                    srcLang: "en-DV"
                    srcMessage: $srcMessage
                    context: $context
                    targetMessage: $targetMessage
                }
            ]
        })
    }
```

`query variables`

```json
    {
        "srcMessage": "store/add-to-cart.success",
        "context": "vtex.add-to-cart-button@0.x",
        "targetMessage": "Producto agregado a su carrito",
        "depTree": "[{\"id\": \"vtex.store-components@3.x\"}]"
    }
```

```json
    {
        "srcMessage": "store/minicart.go-to-checkout",
        "context": "vtex.minicart@2.x",
        "targetMessage": "Ir a pagar",
        "depTree": "[{\"id\": \"vtex.minicart@2.x\"}]"
    }
```

```json 
    {
        "srcMessage": "store/add-to-cart.label-unavailable",
        "context": "vtex.add-to-cart-button@0.x",
        "targetMessage": "No disponible",
        "depTree": "[{\"id\": \"vtex.add-to-cart-button@0.x\"}]"
    }
```