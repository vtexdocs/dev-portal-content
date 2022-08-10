---
title: "Modular Landing Page"
slug: "codeby-landing-modular-app-store"
excerpt: "codeby.landing-modular-app-store@1.0.8"
hidden: true
createdAt: "2022-07-18T09:19:48.083Z"
updatedAt: "2022-07-18T09:19:48.083Z"
---
The modular landing Page is an app for facility the creation of landing pages being easy to add blocks of text and images and position them in your template

## Configuration

1. Install the app landing page modular with command

```cmd
vtex install codeby.landing-modular-app-store@1.x
```

2. Import the modular landing page app to your theme's peer dependencies in the `manifest.json`, for example:

```json
  "peerDependencies": {
    "codeby.landing-modular-app-store": "1.x"
  }
```

3. Add `landing-modular` block to your blocks files, in the place you want it to show up. For example:

```json
"landing-modular": {
  "title":"Landing Page Modular",
  "children": []
}
```

## Using Custom Components

If you want to use the custom block, you need to add your custom block in the children of landing-modular

Example of home page using landing-modular

```json{
{
  "store.home": {
    "blocks": [
      "landing-modular"
    ]
  },
  "landing-modular":{
    "title":"Landing Page Modular",
    "children":[
      "rich-text#example"
    ]
  },
  "rich-text#example": {
    "props":{
      "text":"**This is an example text**"
    }
  }
}
```

On site editor, add a new block, choose a custom option in components.
Add the name of the custom component you have add on children of landing-modular, in this example is `rich-text#example`

![plot](docs/images/custom-component.png)

Save your changes on site editor and you can see your custom block

## Advanced Options

- **Class Name:** You can add a custom class css for this block

- **Self Align:** You can change the position of the block in some situations

- **Width:** You can define a custom width for your block in percentage.
  If you don't put any number or put 0, the width of the block will be automatic defined by flex

- **Max width on Mobile:** If you enable this option, when your screen will be 768px of width or minor, the width you block will be 100%

![plot](docs/images/advanced-options.png)