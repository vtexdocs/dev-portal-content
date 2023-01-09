---
title: "Disclosure Layout"
slug: "vtex-disclosure-layout"
excerpt: "vtex.disclosure-layout@1.0.3"
hidden: false
createdAt: "2020-08-28T17:52:57.565Z"
updatedAt: "2020-09-15T20:55:00.326Z"
---
📢 Use this project, [contribute](https://github.com/vtex-apps/disclosure-layout) to it or open issues to help evolve it using [Store Discussion](https://github.com/vtex-apps/store-discussion).

The Disclosure Layout is an app responsible for creating a layout structure based on disclosure indicators.

![Disclosure Example](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-disclosure-layout-0.gif)
[Check example](https://github.com/vtex-apps/store-theme/pull/226)

## Configuration

### Step 1 - Adding the Disclosure Layout app to your theme's dependencies

In your theme's `manifest.json` file, add the Disclosure Layout app as a dependency:

```diff
  "dependencies": {
+   "vtex.disclosure-layout": "1.x"
  }
```

Now, you are able to use all the blocks exported by the `disclosure-layout` app. Check out the full list below:

| Block name                   | Description                                                                                                                                                                                                                                                  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `disclosure-layout`          | ![https://img.shields.io/badge/-Mandatory-red](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-disclosure-layout-1.png) Parent block that enables you to build the disclosure layout using its 3 children blocks: `disclosure-trigger`, `disclosure-content`, and `disclosure-state-indicator`. |
| `disclosure-trigger`         | Declares the blocks that will be rendered as disclosure triggers i.e. the blocks that when clicked on will open or close the disclosure content (defined by the `disclosure-content` block). |
| `disclosure-content`         | Declares the blocks that are responsible for displaying the desired content when the disclosure trigger is clicked on. |
| `disclosure-state-indicator` | Optional block responsible for rendering chevron or other UI elements that change when the disclosure is opened or closed.  |
| `disclosure-layout-group`    | Wraps many `disclosure-layouts` blocks at once. You may use this block to control when each one of them should be displayed, making it possible to have only one `disclosure-layout` open at a time. |
| `disclosure-trigger-group`   | Wraps many `disclosure-trigger` blocks at once. You may use this block to control when and how the `disclosure-layouts` blocks declared inside the `disclosure-layout-group` should be displayed. |

### Step 2 - Adding the Disclosure Layout' blocks to your theme's templates

According to your desire, copy one of the examples stated below and paste it in your theme's desired template, making the necessary changes. Remember to add the `disclosure-layout`block to the template's block list if needed.

- Simple example:

```json
{
  "disclosure-layout#simple": {
    "children": ["disclosure-trigger#simple", "disclosure-content#simple"]
  },
  "disclosure-trigger#simple": {
    "children": ["rich-text#question"]
  },
  "disclosure-content#simple": {
    "children": ["rich-text#answer"]
  },
  "rich-text#question": {
    "props": {
      "text": "How can I change my shipping address?"
    }
  },
  "rich-text#answer": {
    "props": {
      "text": "Call us at the number (212) 1234-1234"
    }
  }
}
```

- Example using the `disclosure-layout-group` block:

```json
{
  "disclosure-layout-group#group": {
    "children": ["disclosure-layout#first", "disclosure-layout#second"]
  },

  "disclosure-layout#first": {
    "children": ["disclosure-trigger#first", "disclosure-content#first"]
  },
  "disclosure-trigger#first": {
    "children": ["rich-text#question1"]
  },
  "disclosure-content#first": {
    "children": ["rich-text#answer1"]
  },
  "rich-text#question1": {
    "props": {
      "text": "How can I change my shipping address?"
    }
  },
  "rich-text#answer1": {
    "props": {
      "text": "Call us at the number (212) 1234-1234."
    }
  },

  "disclosure-layout#second": {
    "children": ["disclosure-trigger#first", "disclosure-content#first"]
  },
  "disclosure-trigger#second": {
    "children": ["rich-text#question1"]
  },
  "disclosure-content#second": {
    "children": ["rich-text#answer1"]
  },
  "rich-text#question2": {
    "props": {
      "text": "How can I track my order?"
    }
  },
  "rich-text#answer2": {
    "props": {
      "text": "After logging into your account, you can find this info at the link Orders."
    }
  }
}
```

- Example using the `disclosure-state-indicator` block:

```json
{
  "disclosure-state-indicator": {
    "props": {
      "Show": "icon-angle--down",
      "Hide": "icon-angle--up"
    }
  }
}
```

#### `disclosure-layout` props

| Prop name           | Type                  | Description                                                                                                                                                                                     | Default value                                  |
| ------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| `initialVisibility` | `enum`                | Defines the initial visibility of the layout content. Possible values are: `visible` (content initially open) or `hidden` (content is only displayed with user interaction).    | `hidden`   |
| `animated`          | `boolean` | Whether or not the layout content should have animations. When set as `true`, this prop will enable additional `data-\*` attributes on the content which you can use as selectors in CSS. It will also ensure that the element will get hidden once the transition has ended. | `false` |

#### `disclosure-trigger` props

| Prop Name    | Type     | Description                                                                                          | Default value |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------- | ------------- |
| `Show`       | `block`  | Name of the block that will be rendered when prompt to show the content. | `undefined`   |
| `Hide`       | `block`  | Name of the block that will be rendered when prompt to hide the content.    | `undefined`   |
| `as`         | `string` | HTML tag to be applied to the component when it is rendered on the UI. | `button`      |
| `children`   | `block`  | Name of the block that will be rendered in case no blocks are declared in the `Show` or `Hide` props. | `undefined`   |
| `blockClass` | `string` | Block ID of your choosing to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization#using-the-blockclass-property). | `undefined`   |

#### `disclosure-content` props

| Prop Name    | Type     | Description                                                                                          | Default value |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------- | ------------- |
| `blockClass` | `string` | Block ID of your choosing to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization#using-the-blockclass-property). | `undefined`   |
| `children`   | `[block]`  | List of blocks that will render the desired disclosure content. | `undefined`   |

#### `disclosure-state-indicator` props

| Prop Name | Type    | Description                                                 | Default value |
| --------- | ------- | ----------------------------------------------------------- | ------------- |
| `Show`    | `block` | Name of the block that will be rendered when prompt to show the content. | `undefined`   |
| `Hide`    | `block` | Name of the block that will be rendered when prompt to hide the content. | `undefined`   |

#### `disclosure-layout-group` props

| Prop Name    | Type   | Description                                                                                                                                                 | Default value |
| ------------ | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `maxVisible` | `enum` | Defines how many `disclosure-layout` blocks should be displayed at time. Possible values are: `one` (only one `disclosure-layout` block should have its content displayed at time) or `many` (different `disclosure-layout`'s contents can be displayed at time). | `one`  | 

#### `disclosure-trigger-group` props

| Prop Name    | Type     | Description                                                                                          | Default value |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------- | ------------- |
| `Show`       | `block`  | Name of the block that will be rendered when prompt to show the content.            | `undefined`   |
| `Hide`       | `block`  | Name of the block that will be rendered when prompt to hide the content.            | `undefined`   |
| `as`         | `string` | HTML tag to be applied to the component when it is rendered on the UI.              | `button`      |
| `children`   | `block`  | Name of the block that will be rendered in case no blocks are declared in the `Show` or `Hide` props.           | `undefined`   |
| `blockClass` | `string` | Block ID of your choosing to be used in [CSS customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization#using-the-blockclass-property). | `undefined`   |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles             |
| ----------------------- |
| `content`               |
| `content--visible`      |
| `content--hidden`       |
| `trigger`               |
| `trigger--visible`      |
| `trigger--hidden`       |
| `triggerGroup`          |
| `triggerGroup--visible` |
| `triggerGroup--hidden`  |

