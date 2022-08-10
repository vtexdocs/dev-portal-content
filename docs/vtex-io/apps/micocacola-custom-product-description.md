---
title: "CUSTOM PRODUCT DESCRIPTION"
slug: "micocacola-custom-product-description"
excerpt: "micocacola.custom-product-description@0.0.7"
hidden: true
createdAt: "2022-07-29T17:24:27.919Z"
updatedAt: "2022-07-29T17:24:27.919Z"
---
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

Shows the product description with its attributes in the PDP. 

You can also display the nutritional information of the product in the same format as the description.

![Media Placeholder](./custom-product-description.jpg)

![Media Placeholder](./custom-product-nutri-info.jpg)

## Installation 
1. Clone the repository and change the app manifest:
```
{
  "vendor": "<your-vendor>",
  "name": "custom-product-description",
  .
  .
  .
}
```
2. Login to your vtex account:
```
> vtex login <development-environment>
```
3. Select your workspace and use `vtex link`:
```
> vtex use <workspace>
> vtex link
```

## Block ⚙
1. Adding the app as a theme dependency in the `manifest.json` file:
```
<your-vendor>.custom-product-description: "0.x"
```
2. Create a new file named `<your-vendor>.custom-product-description.css` in the css folder and add the following basic styles.
```
.container{
    margin: 1rem 0px;
}

.titleContainer {
    border-radius: 12px;
    cursor: pointer;
    box-shadow: 0 1px 3px rgb(0 0 0 / 12%), 0 1px 2px rgb(0 0 0 / 24%);
}

.textTitle {
    display: inline-flex;
}

.arrow {
    align-self: flex-end;
    height: max-content;
    padding: 0;
    margin: 0;
    display: inline-block;
    margin-left: auto;
    font-size: 1rem;
}

.arrow--isClosed::before{
    content: url("data:image/svg+xml; utf8, <svg xmlns='http://www.w3.org/2000/svg' width='13.542' height='13.247' viewBox='0 0 10.542 6.247'><path style='fill:red;' class='a' d='M17,9.17a1,1,0,0,0-1.41,0L12,12.71,8.46,9.17a1,1,0,1,0-1.41,1.42l4.24,4.24a1,1,0,0,0,1.42,0L17,10.59a1,1,0,0,0,0-1.42Z' transform='translate(-6.754 -8.879)'/></svg>");
}

.arrow--isOpen::after{
    content: url("data:image/svg+xml; utf8, <svg xmlns='http://www.w3.org/2000/svg' width='13.542' height='13.247' viewBox='0 0 10.542 6.247'><path style='fill:red;' class='a' d='M17,9.17a1,1,0,0,0-1.41,0L12,12.71,8.46,9.17a1,1,0,1,0-1.41,1.42l4.24,4.24a1,1,0,0,0,1.42,0L17,10.59a1,1,0,0,0,0-1.42Z' transform='translate(-6.754 -8.879)'/></svg>");
    transform: rotate(180deg);
    display: inline-flex;
}

.descriptionContainer {
    padding: 0 1.3rem;
    background-color: rgb(238 238 238/65%);
    border-radius: 10px;
    overflow: hidden;
    height: auto;
}

.descriptionContainer--isClosed {
    max-height: 0px;
    transition: max-height .2s ease-out;
}

.descriptionContainer--isOpen {
    max-height: 850px;
    transition: max-height .2s ease-in;
}
 
```

3. Declare the main application block in a given theme template or within another theme block.
You can show the product description with its attributes with the block `"custom-product-description#description"` or show another block with the nutritional information `"custom-product-nutritional-info#nutri-info"`.
```
{
   "flex-layout.row#custom-product-description": {
        "children": [
            "custom-product-description#description",
            "custom-product-nutritional-info#nutri-info"
        ]
    },
    "custom-product-description#description": {
        "title": "Product description with atributes"
    },
    "custom-product-nutritional-info#nutri-info": {
        "title": "Nutritional information"
    }
}
```
## Modus Operandi
The component uses the product context ('vtex.product-context') and uses its properties to represent the description with its attribute table and nutritional information.

The main div that contains the component's title (titleContainer), is responsible for executing a function every time it is clicked. This function injects the class --isOpen or --isClosed to determine if the div with the information should be displayed or not.

## Customization

| CSS Handles |
| ----------- |
| `container` |
| `titleContainer` |
| `textTitle` |
| `arrow` |
| `arrow--isOpen` |
| `arrow--isClosed` |
| `descriptionContainer` |
| `descriptionContainer--isOpen` |
| `descriptionContainer--isClosed` |
| `textDescription` |
| `tableContainer` |
| `table` |
| `tableTh` |
| `tableTr` |
| `tableTd` |
| `even` |
| `odd` |


## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- **Fabian Toro**