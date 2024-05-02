---
title: "Iframe"
slug: "vtex-iframe"
hidden: false
createdAt: "2020-06-03T15:19:18.838Z"
updatedAt: "2022-03-10T18:31:22.068Z"
---

An app that makes it possible to render external iframes on a store.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-iframe-0.png)

## Configuration - standard Iframe

1. Add the `vtex.iframe` to the theme's dependencies on the `manifest.json`
```json
"dependencies": {
 "vtex.iframe": "0.x"
}
```
 
 2. Add the interface `iframe` to any **custom page** (Iframes are not allowed outside custom pages).
 
```json
{
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
  }
}
```

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `src` | String | Source address the iframe should render | `null`
| `width` | Number | Width attribute of the iframe | `null`
| `height` | Number | Height attribute of the iframe | `null`
| `allow` | String | allow attribute of the iframe | `null`

## Configuration - dynamic Iframe

1. Add the `vtex.iframe` to the theme's dependencies on the `manifest.json`

```json
"dependencies": {
  "vtex.iframe": "0.x"
}
```

2. Add the dynamicIframe block and its properties to the blocks.json file

```json
{
  "store.custom#locationPage":{
    "children":[
      "iframe.dynamic-src"
    ]
  },
  "iframe.dynamic-src":{
    "props": {
      "dynamicSrc": "https://www.test.com/exampleStaticPathName/{dynamicParam1}/{dynamicParam2}/exampleStaticPageName",
      "width": "1920",
      "height": "1000",
      "title": "exampleStaticPageName iframe wrapper for {account}",
      "allow": "geolocation"
    }
  }
}
```
3. register your new page in routes.json with appropriate parameters passed into the page url

```json
{
  "store.custom#locationPage":{
    "path": "/:param1/:param2/pagename"
  }
}
```

| Prop name | Type | Description | Default value |
|--------------|--------|--------------| --------|
| `dynamicSrc` | String | iframe src with dynamic parameters from page URL enclosed in '{}' | `null`
| `width` | Number | Width attribute of the iframe | `null`
| `height` | Number | Height attribute of the iframe | `null`
| `title` | String | title attribute of the iframe | `null`
| `allow` | String | allow attribute of the iframe | `null`

## Customization

There is a `.container` handle that wraps the iframe, it's also possible to use `blockClass`.
