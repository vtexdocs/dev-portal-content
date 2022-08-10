---
title: "Inducascos store theme"
slug: "inducascos-store-theme"
excerpt: "inducascos.store-theme@5.0.6"
hidden: true
createdAt: "2022-07-22T12:59:16.617Z"
updatedAt: "2022-07-27T14:30:20.552Z"
---
VTEX IO store theme for inducascos ecommerce

## Project structure

The project was building with 4 principal builders:

- styles: Styles of the website
- store: The routes and blocks (components) in the principal sections (header, footer, home, product, search, login, account, etc)
- docs: For documentation
- assets: For aditional files
- messages: For change text in some components

## Installation

This template requires the installation of the following apps in your workspace:

- inducascos.components
- vtex.checkout-ui-custom
- vtex.reviews-and-ratings
- vtex.search-resolver@0.x
- vtex.social-selling
- vtex.store-graphql
- vtex.store-locator
- vtex.wish-list (search like wishlist in vtex app store)

## Forms configuration

There are 2 forms in the store. One is in the contact page and the other is in refund page.

Is necesary to create a data entity in masterdata and configure its schema for each one.

### Contact form configuration

In masterdata v1, create a new data entity with the next structure:

![Contact data entity](./images/contact-entity.png)

after that you need to create a schema sending this request according to your account name. It's suggested to send the request in the console of the admin page

```
fetch("/api/dataentities/CT/schemas/contacto", {
  method: "PUT",
  credentials: "same-origin",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    name: "contacto",
    type: "object",
    properties: {
      preferenciaContacto: {
        type: "string",
        maxLength: 50,
        title: "Como desea ser contactado",
        enum: ["Email", "Llamada", "Whatsapp"],
      },
      celular: {
        type: "string",
        title: "Numero de celular",
      },
      email: {
        type: "string",
        format: "email",
        title: "Correo electronico",
      },
      terminosCondiciones: {
        type: "boolean",
        title: "Acepta términos y condiciones",
      },
      comentario: {
        type: "string",
        title: "Comentario",
      },
    },
    required: [
      "preferenciaContacto",
      "celular",
      "email",
      "terminosCondiciones",
      "comentario",
    ],
    "v-security": {
      publicJsonSchema: true,
      allowGetAll: false,
      publicRead: ["fieldExemple"],
      publicWrite: ["fieldExemple"],
      publicFilter: ["fieldExemple"],
    },
  }),
})
  .then((res) => res.json())
  .then((jsonRes) => console.log(jsonRes));
```

### Refund form configuration

For the refund form you need to replicate the above process.

for the data entity

![refund data entity](./images/refund-entity.png)

And the request below.

```
fetch('https://{{accountName}}.myvtex.com/api/dataentities/DV/schemas/devoluciones',
  {
    method: 'PUT',
    credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: 'devoluciones',
      type: 'object',
      properties: {
        emailCliente: {
          type: 'string',
          format: 'email',
          title: 'Email del cliente',
        },
        cedula:{
          type: 'string',
          maxLength: 50,
          title: 'Nombre del cliente',
        },
        telefono:{
          type: 'string',
          maxLength: 50,
          title: 'Nombre del cliente',
        },
        asunto:{
          type: 'string',
          maxLength: 50,
          title: 'Nombre del cliente',
        },
        comentarios:{
          type: 'string',
          maxLength: 750,
          title: 'Nombre del cliente',
        },
        nombreCliente: {
          type: 'string',
          maxLength: 50,
          title: 'Nombre del cliente',
        },
        motivo: {
          type: 'string',
          maxLength: 100,
          title: 'Motivo de la solicitud',
          enum: ['Garantía', 'Devolucion', 'Cambio de color', 'otro'],
        },
        nombreProducto: {
          type: 'string',
          maxLength: 50,
          title: 'Nombre del producto',
        },
      },
      required: ['emailCliente', 'nombreCliente', 'motivo', 'nombreProducto','cedula','telefono','asunto','comentarios'],
      'v-security': {
        publicJsonSchema: true,
        allowGetAll: false,
        publicRead: ['fieldExemple'],
        publicWrite: ['fieldExemple'],
        publicFilter: ['fieldExemple'],
      },
    }),
  }
)
  .then((res) => res.json())
  .then((jsonRes) => console.log(jsonRes));
```

## Overwriting messagges in come apps

To overwrite texts in some components like the comparison drawer and my-account, it is necessary:

- Install the vtex.admin-graphql-ide app.
- Go to https://{{account}}.myvtex.com/admin/graphql-ide.
- From the dropdown list, choose the vtex.messages app.
- Write the following mutation command:

```
  mutation Save($saveArgs: SaveArgsV2!) {
    saveV2(args: $saveArgs)
  }
```

- Then click on Query Variables and create a json variables with ne next structure:

```
{
  "saveArgs": {
    "to": "es-CO",
    "messages": [
      {
        "srcLang": "en-DV",
        "context": "vtex.product-comparison@0.x",
        "srcMessage": "store/product-comparison.drawer.compare",
        "targetMessage": "Comparar"
      }
    ]
  }
}
```

The messages array must contains an object with the structure for each text that you want to overwrite. Search the srcMessage in the desired app message folder.

## Suggestions

Create a production workspace for testing, its can be called quality.
for example: `vtex use quality -p`.