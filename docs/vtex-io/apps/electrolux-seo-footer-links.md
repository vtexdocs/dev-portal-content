---
title: "SEO Footer Links"
slug: "electrolux-seo-footer-links"
excerpt: "electrolux.seo-footer-links@0.2.0"
hidden: true
createdAt: "2022-07-06T20:08:36.572Z"
updatedAt: "2022-07-06T20:08:36.572Z"
---
This app aim's display a category tree on the application, orinagily intended to be displayed at the footer, but you can use the block in whenever place you want on the store.

This app renders on the server side, doesnot make any requests to the backend and relies only on information provided by the site editor, which is the site domain and a valid javascript object cointaining the store category tree, aditionaly for this app achieve its goals its necessary to declare its block before a fold or disable footer lazy loading on the store admin.

This ensure that the html will render on the server side and the content be delivered to the client on the first render and so be indexed by search engines.

If no valid data be provided the component wil not be rendered.

![rendered-component](./img/ADICIONAR_IMAGEM)

## Configuration 

1. Adding the app as a theme dependency in the `manifest.json` file;
2. Declaring the app's main block in a given theme template or inside another block from the theme.
3. If the block is declared on the footer be sure that the footer lazy loading is disable, otherwise just be sure ther block is declared before any fold block and go to step 6.
4. On the store admin, go to Store Setup / CMS / Store and select "Advanced" tab.
5. Go to "Enable lazy rendering of the page footer" option, select disable and save.
6. Now we need the categories tree data, go to the GraphQL IDE on the store setup and select `vtex.store-graphql@X.X.X` 
7. Then paste the following query on the IDE: 
```javascript
query {
  categories {
    id
    name
    href
    children {
      id
      name
      href
      children {
        id
        name
        href
      }
    }
  }
}
```
8. Copy the response to some text editor. ![graphql-ide-response](./img/ADICIONAR_IMAGEM)
7. Now, go to the site editor and select the "SEO Footer Links" block. You gonna need to repeat the following steps for every block declared, such as mobile and desktop layouts. ![site-editor-form](./img/ADICIONAR_IMAGEM)
8. Fill the "Store Domain" input accordinfgly and paste the graphql query response on the "Categories Tree JavaScript Object" input and save.
9. This should render the component on the store.

### `seo-footer-links` props

| Prop name         | Type            | Description                                                       | Default value   |
| ----------------- | --------------- | ----------------------------------------------------------------- |---------------- |
| `domain`          | `string`        | Store production domain. Ex: store.com                            | `null`          |
| `categoriesTree`  | `string`        | Valid JS object such as response from the graphQL IDE stringfyed  | `null`          |


### About the expected JS object

Expected category type: 
```typescript
Category = {
  id: number
  name: string
  href: string
  children?: Category[]
}
```

Simple valid object example
```json
{
  "data": {
    "categories": [
      {
        "id": 1,
        "name": "department 1, this level will render as a H2 html tag",
        "href": "/department1",
        "children": []
      },
      {
        "id": 2,
        "name": "department 2, this level will render as a H2 html tag",
        "href": "/department2",
        "children": [
          {
            "id": 21,
            "name": "category1, this level will render as a H3 html tag",
            "href":  "/department2/category1",
            "children": [
              {
                "id": 211,
                "name": "subCategory1, this level will render as a H4 html tag",
                "href":  "/department2/category1/subcategory1",
              }
            ]
          }
        ]
      },
    ]
  }
}
```

Note that you dont need to be restrained to the graphQL response, you could build you own custom category tree object, just following the example above.

Just remind the top level of the object will be rendered as a H2 html tag and the followind children will raise the heading tag to the limit of H4, futher children lists will be rendered as a H4 tag.

There is a limit? In theory, no. SEO Footer Link is a recursive app, you can have as much nested list as you want as long you follow the expected strutured.



Remember to also use this Configuration section to  **showcase any necessary disclaimer** related to the app and its blocks, such as the different behavior it may display during its configuration. 

## Modus Operandi *(not mandatory)*

There are scenarios in which an app can behave differently in a store, according to how it was added to the catalog, for example. It's crucial to go through these **behavioral changes** in this section, allowing users to fully understand the **practical application** of the app in their store.

If you feel compelled to give further details about the app, such as it's **relationship with the VTEX admin**, don't hesitate to use this section. 

## Customization

The first thing that should be present in this section is the sentence below, showing users the recipe pertaining to CSS customization in apps:

`In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).`

Thereafter, you should add a single column table with the available CSS handles for the app, like the one below. Note that the Handles must be ordered alphabetically.

| CSS Handles |
| ----------- | 
| `XXXXX` | 
| `XXXXX` | 
| `XXXXX` | 
| `XXXXX` | 
| `XXXXX` |


If there are none, add the following sentence instead:

`No CSS Handles are available yet for the app customization.`

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->

---- 

Check out some documentation models that are already live: 
- [Breadcrumb](https://github.com/vtex-apps/breadcrumb)
- [Image](https://vtex.io/docs/components/general/vtex.store-components/image)
- [Condition Layout](https://vtex.io/docs/components/all/vtex.condition-layout@1.1.6/)
- [Add To Cart Button](https://vtex.io/docs/components/content-blocks/vtex.add-to-cart-button@0.9.0/)
- [Store Form](https://vtex.io/docs/components/all/vtex.store-form@0.3.4/)