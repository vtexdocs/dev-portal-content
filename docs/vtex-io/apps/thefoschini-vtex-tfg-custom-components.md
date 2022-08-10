---
title: "VTEX TFG CUSTOM COMPONENTS"
slug: "thefoschini-vtex-tfg-custom-components"
excerpt: "thefoschini.vtex-tfg-custom-components@1.1.82"
hidden: true
createdAt: "2022-07-09T09:08:54.593Z"
updatedAt: "2022-08-05T12:52:33.301Z"
---
This repo contains all custom blocks that are used inside of the vtex shop 

### Setup, Linking and Uninstalling Notes
- When making changes to your component types, in order register these changes in the generate typing files it is important to run `vtex setup` before `vtex link`
- When you have made changes to this repo, and you get errors in `vtex-shop` when linking, your changes are not reflecting in `vtex-shop`: It is important to run `vtex-setup` in the **vtex-shop** repo 
- Often if you have reset your workspace or are in the test workspace `vtex-tfg-custom-components` will be **installed**, you can test this by running `vtex ls` and check under the installed apps if it is listed. Before you can link your `vtex-tfg-custom-components` you need to **uninstall the existing app** using the command `vtex uninstall thefoschini.vtex-tfg-custom-components.{app-number}`. You should now be able to link your app without issue


## Interface.json File
Please export your blocks from the interface.json file located at `store/interfaces.json`. All block names should conform to the to the format **tfg-{kebab-case-component-name}**

Example
```
  "tfg-common-blocks": {
    "component": "TFGCommonBlocks",
    "composition": "children"
  }
```

## React Directory Top Level
- Only keep components in the top level directory that will be exported via `interfaces.json`
- All components at the top level must be prefixed with **TFG** Example: `TFGProductWidget`

## React Directory Components : `react/components`
- All components that are not exported via `interfaces.json` need to be place in the components directory
- Please  name sub directories after their relevant exported components. Example: if we are exporting `TFGProductWidget`, its subcomponents should be placed in the directory `react/components/tfg-product-widget`

## CSS Directory
- The css directory can be used to house `.css` and `.module.css` files which can be imported directly into your React Component.
-  **Please using this sparingly, avoid styling your components this way if you can as this prevents us from using the  scss variables via `vtex shop`**

## CSS Handles
- css handles are used to add classes to html elements so we can target them via `vtex-shop`
- documentation on how to use these can be found here https://github.com/vtex-apps/css-handles
- **ALL** elements need have a css handle added to them e.g. `<div className={handles.productWidgetWrapper}>`
- Naming of css handles: choose names that will not conflict with others in the app : if file **A**: contains a handle `handles.product` and file **B**: contains the same handle `handle.product`, these two handles will produce the same css class and will conflict 


## Use JS Doc Strings to document all components
Example
```
/**
 * TFGPLPBrandHeaderWrapper
 * A data wrapper for the TFGPLPBrandHeader component.
 * Will not show if there are zero or more than 1 brands.
 *
 * @returns TFGPLPBrandHeader component
 */
```

## Important Libraries 
- Context Apis provide data to components in the vtex store: https://github.com/vtex-apps?q=context&type=all&language=&sort=
- The most important context is the https://github.com/vtex-apps/product-context as it provides product data to a react component.

Usage of the Product Context
```
import type { ProductTypes } from 'vtex.product-context'
import { useProduct } from 'vtex.product-context'

const MyComponent = () => {
 const { product, selectedItem } = useProduct() ?? {}
 
 return <p>In Vino Veritas</p>
}

```