---
title: "Tab Layout"
slug: "vtex-tab-layout"
excerpt: "vtex.tab-layout@0.4.4"
hidden: false
createdAt: "2020-06-03T15:19:35.560Z"
updatedAt: "2022-02-24T13:00:12.534Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

The Tab Layout app provides you the needed structure to create different layouts within the store's main one from the use of *tabs*.

![tab-layout](https://user-images.githubusercontent.com/52087100/66661201-fc70c880-ec1c-11e9-8387-3fea98f59e3c.png)
*Example of an brazilian VTEX store with tabs (`Perfumes até 40%off`, `Presentes`, and `Best Sellers`) displaying different content for users.* 

## Configuration

1. Add the Tab Layout app to your theme's dependencies in the `manifest.json` file:

```diff
 "dependencies": {
+  "vtex.tab-layout": "0.x"
 }
```

Now, you are able to use all the blocks exported by the `tab-layou` app. Check out the full list below:

| Block name   | Description                |
| :----------: | :------------------------: |
| `tab-layout` |  ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Parent block that merely defines the logic (via its children blocks) for the layout structure, declaring the desired list of tabs and its content. |
| `tab-list`   |  ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Defines the list of tabs to be rendered. It only accepts the `tab-list.item` block as child. | 
| `tab-list.item` | ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Defines the rendering for a given tab. Notice that it does not define the tab content, which is handled by the `tab-content.item` block.  |
| `tab-list.item.children` | Flexible alternative to `tab-list.item`. Defines the rendering for a given tab and also accepts any array of blocks as its children. |
| `tab-content` |  ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Defines the list of content to be rendered in each tab. It only accepts the `tab-content.item` block as child. |
| `tab-content.item` |  ![https://img.shields.io/badge/-Mandatory-red](https://img.shields.io/badge/-Mandatory-red) Defines the content for a given tab. | 

2. In the desired page tempate, such as `store.home`, add the `tab-layout` block:

```json
"store.home": {
  "blocks": [
    "tab-layout#home
  ]
},
```

3. Declare the `tab-list` and the `tab-content` blocks as `tab-layout`'s children. Do not forget to use the `tab-layout`'s props, for example:

```diff
  "store.home": {
    "blocks": [
      "tab-layout#home
    ]
  },
+ "tab-layout#home": 
+   "children": [
+     "tab-list#home",
+     "tab-content#home"
+   ],
+   "props": {
+     "blockClass": "home",
+     "defaultActiveTabId": "home1"
+   }
+ },
```  

4. Add and then declare the desired `tab-list.item` blocks as `tab-list`'s children:

```diff
  "store.home": {
    "blocks": [
      "tab-layout#home
    ]
  },
  "tab-layout#home": 
    "children": [
      "tab-list#home",
      "tab-content#home"
    ],
    "props": {
      "blockClass": "home",
      "defaultActiveTabId": "home1"
    }
  },
+ "tab-list#home": {
+   "children": [
+     "tab-list.item#home1",
+     "tab-list.item#home2"
+   ]
+ },
+ "tab-list.item#home1": {
+   "props": {
+     "tabId": "home1",
+     "label": "Home 1",
+     "defaultActiveTab": true
+   }
+ },
+ "tab-list.item#home2": {
+   "props": {
+     "tabId": "home2",
+     "label": "Home 2"
+   }
+ },
```
  
5. Add and then declare the desired `tab-content.item` blocks as `tab-content`'s children:

```diff
  "store.home": {
    "blocks": [
      "tab-layout#home
    ]
  },
  "tab-layout#home": 
    "children": [
      "tab-list#home",
      "tab-content#home"
    ],
    "props": {
      "blockClass": "home",
      "defaultActiveTabId": "home1"
    }
  },
  "tab-list#home": {
    "children": [
      "tab-list.item#home1",
      "tab-list.item#home2"
    ]
  },
  "tab-list.item#home1": {
    "props": {
      "tabId": "home1",
      "label": "Home 1",
      "defaultActiveTab": true
    }
  },
  "tab-list.item#home2": {
    "props": {
      "tabId": "home2",
      "label": "Home 2"
    }
  },
+ "tab-content#home": {
+   "children": [
+     "tab-content.item#home1",
+     "tab-content.item#home2"
+   ]
+ },
+ "tab-content.item#home1": {
+   "children": [
+     "carousel#home"
+   ],
+   "props": {
+     "tabId": "home1"
+   }
+ },
+ "tab-content.item#home2": {
+   "children": [
+     "shelf#home",
+     "info-card#home",
+     "rich-text#question",
+     "rich-text#link",
+     "newsletter"
+   ],
+   "props": {
+     "tabId": "home2"
+   }
+ }
```

> ⚠️ *Do not forget to also declare the `tab-content.item`'s children blocks in order to properly render the tab content.*

### `tab-layout` props

| Prop name      | Type         | Description                                        | Default value   |
| :------------: | :----------: | :------------------------------------------------: | :-------------: |
| `defaultActiveTabId` | `string` | ID of the desired tab to be rendered as the default one. If no value is provided, the first tab declared in the theme will be used as default. | `undefined` |
| `blockClass` | `string` | Block ID of your choosing to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).  | `undefined` |

### `tab-list` props

| Prop name      | Type         | Description                                        | Default value   |
| :------------: | :----------: | :------------------------------------------------: | :-------------: |
| `blockClass`   | `string`     | Block ID of your choosing to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization). | `undefined` |

### `tab-list.item` props

| Prop name      | Type         | Description                                        | Default value   |
| :------------: | :----------: | :------------------------------------------------: | :-------------: |
| `blockClass` | `string` | Block ID of your choosing to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization). | `undefined` |
| `tabId` | `string` | Tab ID of your choosing. It will be used to match the tab to its content (defined by the `tab-content.item` block).  | `undefined` |
| `label` | `string` | Defines the tab's text label. | `undefined` |
| `defaultActiveTab` | `boolean` | Defines the item as the default active tab. | `false` |

### `tab-list.item.children` props

| Prop name      | Type         | Description                                        | Default value   |
| :------------: | :----------: | :------------------------------------------------: | :-------------: |
| `blockClass` | `string` | Block ID of your choosing to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization). | `undefined` |
| `tabId` | `string` | Tab ID of your choosing. It will be used to match the tab to a given content (defined by the `tab-content.item` block). | `undefined` |

### `tab-content` props

| Prop name      | Type         | Description                                        | Default value   |
| :------------: | :----------: | :------------------------------------------------: | :-------------: |
| `blockClass`   | `string`     | Block ID of your choosing to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).  | `undefined`  |

### `tab-content.item` props

| Prop name      | Type         | Description                                        | Default value   |
| :------------: | :----------: | :------------------------------------------------: | :-------------: |
| `blockClass` | `string` | Block ID of your choosing to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization). | `undefined` |
| `tabId` | `string` | Tab ID of your choosing. It will be used to match the content to a given tab (defined by the `tab-list.item` / `tab-list.item.children`  blocks). | `undefined` |

> ⚠️ *Pay attention to the chosen tab ID declared in both `tab-list.item` and `tab-content.item` blocks, once it is the key to link a given tab to its content.

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handle |
| ---------- |
| `container`  |
| `contentContainer`  |
| `contentItem`  |
| `listContainer`  |
| `listItem`  |
| `listItemActive`  |
| `listItemChildren` |
| `listItemChildrenActive` |

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/JNussens"><img src="https://avatars0.githubusercontent.com/u/7662734?v=4" width="100px;" alt=""/><br /><sub><strong>Jean Nussenzveig</strong></sub></a><br /><a href="https://github.com/vtex-apps/tab-layout/commits?author=JNussens" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/lucasayb"><img src="https://avatars2.githubusercontent.com/u/17356081?v=4" width="100px;" alt=""/><br /><sub><strong>Lucas Yamamoto</strong></sub></a><br /><a href="https://github.com/vtex-apps/tab-layout/commits?author=lucasayb" title="Code">💻</a></td>
    <td align="center"><a href="https://acct.global/"><img src="https://avatars0.githubusercontent.com/u/38354801?v=4" width="100px;" alt=""/><br /><sub><strong>weslybrandao</strong></sub></a><br /><a href="https://github.com/vtex-apps/tab-layout/commits?author=weslybrandao" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

<!-- DOCS-IGNORE:end -->