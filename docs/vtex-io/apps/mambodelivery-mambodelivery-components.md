---
title: "Description"
slug: "mambodelivery-mambodelivery-components"
excerpt: "mambodelivery.mambodelivery-components@0.1.13"
hidden: true
createdAt: "2022-07-05T06:42:46.860Z"
updatedAt: "2022-08-02T14:41:49.173Z"
---
Gigadigital Apps

## Table of Contents

- [Usage](#usage)
- [Components Specs](#components-specs)
- [Pattern](#pattern)

## Usage

This app uses our store builder with the blocks architecture. To know more about Store Builder
[click here.](https://help.vtex.com/en/tutorial/understanding-storebuilder-and-stylesbuilder#structuring-and-configuring-our-store-with-object-object)

To use this app, you need to import in your dependencies on `manifest.json`.

```json
  "dependencies": {
    "gigadigital.gigadigital-components": "0.x"
  }
```

Then, you can add a component block into your app theme.
You can use all components declared at `interfaces.json`.

For example, now you can use the `fixed-prices` block that is in the gigadigital-apps. See an example of how to configure:

```json
	"flex-layout.row#fixed-prices-plus-btn": {
		"props": {
			"width": "100%",
			"blockClass": "fixed-prices"
		},
		"title": "Produto - Fixed prices",
		"children": ["fixed-prices#plus-add-to-cart"]
	},
	"fixed-prices#plus-add-to-cart": {
		"blocks": ["add-to-cart-button"]
	}
```

## Components Specs

Below we have a README for each component of this project that explains how to use them.

- [fixed-prices](fixed-prices.md)
- [unit-measures](unit-measures.md)
- [render-optin](render-optin.md)
- [add-region](add-region.md)
- [cart-category](cart-category.md)

## Pattern

- Files ending with JSX
- Dividing files by folders

<!-- DOCS-IGNORE:start -->

## Devs

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
  	<td><a href="https://gitlab.com/vitor.moran">Vitor Moran</a></td>
    <td><a href="https://gitlab.com/sebastian.vega1">Sebastian Sanchez Vega</a></td>
	<td><a href="https://gitlab.com/renato.bueno">Renato Bueno</a></td>
	<td><a href="https://gitlab.com/gustavo.vasconcellos">Gustavo Vasconcellos</a></td>
	<td><a href="https://gitlab.com/leandro.godoy">Leandro Godoy</a></td>
	<td><a href="https://gitlab.com/jose.ricardo">José Ricardo</a></td>
	<td><a href="https://gitlab.com/raissa.campos">Raissa Campos</a></td>
	<td><a href="https://gitlab.com/vinicius.paixao">Vinicius Paixão</a></td>
	<td><a href="https://gitlab.com/thiago.brito">Thiago Brito</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->