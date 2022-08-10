---
title: "Macromex Front Organizations"
slug: "macromex-front-organizations"
excerpt: "macromex.front-organizations@1.0.49"
hidden: true
createdAt: "2022-08-09T13:23:12.473Z"
updatedAt: "2022-08-09T13:23:12.473Z"
---
## Installation Guide

- Add the application in your 
- Open the VTEX App Store and install this app on your store, or run the following command on VTEX toolbelt:

> vtex install macromex.front-organizations@1.x

- Add the app to your theme's manifest.json file inside peerDependencies as shown below:
  
 ```
  "peerDependencies": {
   "macromex.front-organizations": "1.x"
  }
```

### Usage

Add the `salesman-phone` block into your template.

```
"children": [
  ...
  "salesman-phone",
  ...
]


"salesman-phone": {
    "props": {
      "blockClass": "someClass",
      "phoneDefault": "0720 000 000"
    }
  },
```


### Props


| Name | Required | Type | Default | Description |
| --- | --- | --- | --- | --- |
|`iconDisplay`| `No` | boolean | `true` | Determine if the icon will be displayed (`true`) or not (`false`). |
|`iconId`| `No` | string | `headerPhoneIcon` | Icon id |
|`iconSize`| `No` | number | `15`| Icon size (px) |
|`iconViewBox`| `No` | number | `15` | Icon viewBox |
|`iconIsActive`| `No` | boolean | `true` | Determine if icon is active.  |
|`iconActiveClassName`| `No` | string | `vtex-rich-text-0-x-container--headerTopIcon` | Icon active class name. Will be rendered if `iconIsActive` is `true` |
|`iconMutedClassName`| `No` | string | `""` | Icon muted class name. Will be rendered if `iconIsActive` is `false` |
|`phoneDefault`| `No` | string | `""` | Default phone number. Will be displayed if there is no phone number in orgnaization |
|`phoneLink`| `No` | boolean |`true`| Determine if the phone number is a hyperlink (`true`) or not (`false`) |


### Css Classes

||
|---|
|`salesmanPhoneContainer`|
|`salesmanPhoneText`|
|`salesmanPhoneNumber`|
|`salesmanPhoneLink`|

## `hexagon-specs` Block

This block with display up to 5 specifications and can be used on product page.

### Usage

Add the `hexagon-specs` block into your template.

```
"children": [
  ...
  "hexagon-specs",
  ...
]


"hexagon-specs": {
    "props": {
      "blockClass": "hexagonSpecs",
      "maxToDisplay": 5
    }
  },
```

### Props

| Name | Required | Type | Default | Description |
| --- | --- | --- | --- | --- |
|`blockClass`| `No` | boolean | `` | Custom css class |
|`maxToDisplay`| `No` | number | `5` | Number of specifications to be displayed. |
|`allowedSpecs`| `Yes` | array |  | Array of specifications to be displayed. |


### Css Classes

||
|---|
|`specsContainer`|
|`hexagonColumn`|
|`hexagon`|
|`hexagonContent`|
|`hexagonSpecLabel`|
|`hexagonSpecValue`|