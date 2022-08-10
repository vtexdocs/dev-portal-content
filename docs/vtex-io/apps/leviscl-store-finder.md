---
title: "Iframe"
slug: "leviscl-store-finder"
excerpt: "leviscl.store-finder@0.1.15"
hidden: true
createdAt: "2022-07-28T22:32:50.399Z"
updatedAt: "2022-07-28T22:32:50.399Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<div class="alert alert-warning">  
📢 Don't fork this project. Use, contribute, or open issues using your feature request.
</div>

![image](https://user-images.githubusercontent.com/18701182/67055752-abcb0500-f11f-11e9-8c24-50234214d474.png)

An app that makes it possible to render external iframes on a store 

## Configuration - standard Iframe

1. Add the `vtex.iframe` to the theme's dependencies on the `manifest.json`
```
...
"dependencies": {
 ...
 "vtex.iframe": "0.x"
 ...
}
...
```
 
 2. Add the interface `iframe` to any **custom page** (Iframes are not allowed outside custom pages).
 
 ```
 ...
"store.custom#about-us": {
    "blocks": [
      "flex-layout.row#about-us",
      "iframe"
    ]
  },

 "iframe": {
   "props": {
     "src": ""
   }
 },
 ...
 ```

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `src` | String | Source address the iframe should render | `null`
| `width` | Number | Width attribute of the iframe | `null`
| `height` | Number | Height attribute of the iframe | `null`

## Configuration - dynamic Iframe

1. Add the `vtex.iframe` to the theme's dependencies on the `manifest.json`

```json
"dependencies": {
 ...
  "vtex.iframe": "0.x"
}
...
```

2. Add the dynamicIframe block and its properties to the blocks.json file

```json
"store.custom#locationPage":{
    "children":[
      "iframe.dynamic-src"
    ]
  },
"iframe.dynamic-src":{
  "props":{
      "dynamicSrc":"https://www.test.com/exampleStaticPathName/{dynamicParam1}/{dynamicParam2}/exampleStaticPageName",
      "width":"1920",
      "height":"1000",
      "title":"exampleStaticPageName iframe wrapper for {account}"
    }
  }
```
3. register your new page in routes.json with appropriate parameters passed into the page url

```json
"store.custom#locationPage":{
    "path": "/:param1/:param2/pagename"
  },
```

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `dynamicSrc` | String | iframe src with dynamic parameters from page URL enclosed in '{}' | `null`
| `width` | Number | Width attribute of the iframe | `null`
| `height` | Number | Height attribute of the iframe | `null`
| `title` | String | title attribute of the iframe tag | `null`

## Customization

There is a `.container` handle that wraps the iframe, it's also possible to use `blockClass`

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!