---
title: "VTEX Telemarketing"
slug: "vtex-telemarketing"
excerpt: "vtex.telemarketing@2.11.1"
hidden: false
createdAt: "2020-06-03T15:20:24.277Z"
updatedAt: "2022-05-19T15:53:32.347Z"
---
## Description

The VTEX Telemarketing app is a store component that enables a call center operator impersonate a customer in the store, and this app is used by store theme.

:loudspeaker: **Disclaimer:** Don't fork this project, use, contribute, or open issue with your feature request.

## Release schedule

| Release |       Status        | Initial Release | Maintenance LTS Start | End-of-life | Store Compatibility |
| :-----: | :-----------------: | :-------------: | :-------------------: | :---------: | :-----------------: |
|  [2.x]  | **Current Release** |   2018-11-08    |                       |             |         2.x         |
|  [1.x]  | **Maintenance LTS** |   2018-08-15    |      2018-11-08       | March 2019  |         1.x         |

See our [LTS policy](https://github.com/vtex-apps/awesome-io#lts-policy) for more information.

## Table of Contents

- [Usage](#usage)
  - [Blocks API](#blocks-api)
    - [Configuration](#configuration)
  - [Styles API](#styles-api)
    - [CSS namespaces](#css-namespaces)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Tests](#tests)

## Usage

This app uses our store builder with the blocks architecture. To know more about the Store Builder [click here](https://help.vtex.com/en/tutorial/understanding-storebuilder-and-stylesbuilder#structuring-and-configuring-our-store-with-object-object).

We add the telemarketing as a block in our [Store Header](https://github.com/vtex-apps/store-header/blob/master/store/interfaces.json).

To configure or customize this app, you need to import it in your dependencies in `manifest.json`.

```json
  dependencies: {
    "vtex.telemarketing": "2.x"
  }
```

Then, add `telemarketing` block into your app theme as we do in our [Store theme app](https://github.com/vtex-apps/store-theme/blob/master/store/blocks.json).

:loudspeaker: **Disclaimer:** This component will only be displayed for the users that have the role of `2 - Televendas (Call center operator)` in their access profile.

To give an user the permission of call center operator you need to follow these steps on VTEX admin management page:

- Access the page: Account Management -> Access Profiles -> Click in New Profile -> Select `2 - Televendas (Call center operator)`
- Add the email of the users that are responsable for impersonating customers(call center operators).

### Blocks API

When implementing this app as a block, various inner blocks may be available. The following interface lists the available blocks within telemarketing and describes if they are required or optional.

```json
{
  "telemarketing": {
    "component": "index"
  }
}
```

As you can see, this app has no required or optional block.

#### Configuration

This app has no configuration yet.

### Styles API

This app provides some CSS classes as an API for style customization.

To use this CSS API, you must add the `styles` builder and create an app styling CSS file.

1. Add the `styles` builder to your `manifest.json`:

```json
  "builders": {
    "styles": "1.x"
  }
```

2. Create a file called `vtex.telemarketing.css` inside the `styles/css` folder. Add your custom styles:

```css
.container {
  margin-top: 10px;
}
```

#### Customization

| CSS Handles               |
| ------------------------- |
| `container`               |
| `popoverArrowUp`          |
| `popoverBox`              |
| `popoverContentContainer` |
| `popoverContainer`        |
| `login`                   |
| `loginForm`               |
| `loginFormMessage`        |
| `emailInput`              |
| `clientName`              |
| `clientNameBar`           |
| `logout`                  |
| `logoutForm`              |
| `popoverHeaderIcon`       |
| `popoverHeaderEmail`      |
| `loginButton`             |
| `loginAsText`             |
| `popoverHeader`           | 
| `loginFormContainer`      | 
| `logoutInfoContainer`     |
| `emailContainer`          |
| `emailField`              |
| `emailValue`              |
| `documentContainer`       |
| `documentField`           |
| `documentValue`           |
| `phoneContainer`          |
| `phoneField`              |
| `phoneValue`              |
| `logoutButtonsContainer`  |
| `wrapper`                 |
| `telemarketingBar`        |
| `attendantContainer`      |
| `attendantEmail`          |

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization)

## Troubleshooting

You can check if others are passing through similar issues [here](https://github.com/vtex-apps/telemarketing/issues). Also feel free to [open issues](https://github.com/vtex-apps/telemarketing/issues/new) or contribute with pull requests.

## Contributing

Check it out [how to contribute](https://github.com/vtex-apps/awesome-io#contributing) with this project. 

## Tests

To execute our tests go to `react/` folder and run `yarn test`

### Travis CI

[![Build Status](https://travis-ci.org/vtex-apps/telemarketing.svg?branch=master)](https://travis-ci.org/vtex-apps/telemarketing)
[![Coverage Status](https://coveralls.io/repos/github/vtex-apps/telemarketing/badge.svg?branch=master)](https://coveralls.io/github/vtex-apps/telemarketing?branch=master)