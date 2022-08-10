---
title: "CUSTOM SUGGESTION GRID"
slug: "lyracons-custom-suggestion-grid"
excerpt: "lyracons.custom-suggestion-grid@0.0.0"
hidden: true
createdAt: "2022-07-05T18:26:42.732Z"
updatedAt: "2022-07-05T18:26:42.732Z"
---
Static page that shows specific products previously fetched from a service.

![Screenshot from 2022-07-05 04-35-46](https://user-images.githubusercontent.com/92390151/177275020-c8f65a71-3635-4377-9023-d0200bf8494b.png)


## Installation guide 

Install and Add the app as a theme peerDependencies in the manifest.json file:

 "peerDependencies ": {
+  "lyracons.custom-suggestion-grid": "0.x"
 }


## Declaring the app's blocks in your store theme

custom-suggestion-provider: provides children with a context to use Custom Data 

custom-suggestion-grid - Block that shows products displayed in a grid

## Customization

| CSS Handles              |
| -----------              |
| `main`                   | 
| `productsLoaded`         | 
| `mainSpinner`            | 
| `loadingProductsSpinner` | 
| `productListWrapper`     |
| `productItemContainer`   |