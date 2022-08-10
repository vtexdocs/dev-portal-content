---
title: "Helmet Components"
slug: "frwhirlpool-helmet-components"
excerpt: "frwhirlpool.helmet-components@0.0.1"
hidden: true
createdAt: "2022-08-09T08:11:01.887Z"
updatedAt: "2022-08-09T08:11:01.887Z"
---
This custom app was developed in order to add meta tags or in general any other structured data so is a generic app that you can use to add other components. 
You can create a new component (ex: *Component.tsx*) in which you add a meta tag or structured data with Helmet. Then adding it in *interfaces.json* inside the *store* folder you can call the block directly from StoreTheme as a theme block and it will add structured data/meta tags in page <head>

## Configuration 

These are the main steps in order to add structured data/meta tags in page <head> with Helmet:
  - create a *.tsx* component inside the react folder
  - import *Helmet* directly from VTEX and use it to add structured data/meta tags
  - declare a block with this component in *interfaces.json*
  - call the block associated to your component in StoreTheme where you have to add that structured data/meta tags

## Example

For example you can check the component **HelmetHomepage.tsx**, it was developed in order to add a meta tag (<meta name={metaName} content={metaContent} />) useful for Facebook.