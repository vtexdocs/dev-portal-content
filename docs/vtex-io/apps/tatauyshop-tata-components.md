---
title: "TaTa Components"
slug: "tatauyshop-tata-components"
excerpt: "tatauyshop.tata-components@0.15.2"
hidden: true
createdAt: "2022-08-09T10:48:12.666Z"
updatedAt: "2022-08-09T10:48:12.666Z"
---
This project was build with [VTEX IO](https://github.com/vtex-apps/store) and [React](https://reactjs.org/docs/getting-started.html)

## Cloning the repository

    https://gitlab.com/acct.global/acct.tata/tata-components.git

## Custom Components VTEX IO

Read this tutorial on how to create a custom component for VTEX IO

[Learn Custom Blocks VTEX IO](https://learn.vtex.com/docs/course-store-block-lang-en)

## Available Components

### Product Installments

Component used to list the Product Installments. Your blocks and props are:

#### `custom-product-installments` hasn't props

### Financial Promotion

Component used to display the promotion by using an specific financial condition. Your blocks and props are:

#### `financial-promotion` props

| Prop name            | Description                                       | Type     | Default value |
| -------------------- | ------------------------------------------------- | -------- | ------------- |
| `paymentSystemId`    | The ID of the payment system of promotion         | `string` | `""`          |
| `promotionName`      | The name promotion of pyament system of promotion | `string` | `""`          |
| `paymentSystemImage` | The logo of the payment system of promotion       | `string` | `""`          |
| `alternativeText`    | The alternative text of logo `paymentSystemImage` | `string` | `""`          |
| `view`               | Where the component will be renderized            | `string` | `"shelf"`     |

### Should Render

Component used to display blocks, controlled by local storage. Your blocks and props are:

#### `should-render` props

| Prop name           | Description                                                                           | Type     | Default value        |
| ------------------- | ------------------------------------------------------------------------------------- | -------- | -------------------- |
| `renderWhen`        | The rule to render some block. It can be `"not-localStorage"` or `"has-localStorage"` | `string` | `"not-localStorage"` |
| `localStorageItem`  | The key used to set or read the value in local storage                                | `string` | `""`                 |
| `localStorageValue` | The value to set in local storage, if nothing was found from `localStorageItem`       | `string` | `""`                 |

### Icon Minicart Quantity

Component used to display the quantity of products available. Your blocks and props are:

#### `icon-minicart-quantity` hasn't props

### Include Max Length

Component used to set a max length for an input. Your blocks and props are:

#### `include-max-length` props

| Prop name   | Description                                                       | Type     | Default value |
| ----------- | ----------------------------------------------------------------- | -------- | ------------- |
| `maxLength` | The maximum number of characters that will be passed to the input | `number` | ` `           |
| `inputId`   | The ID of the element that will receive the rule                  | `string` | `""`          |

### Menu Sidebar

Component used to display the sidebar drawer menu in the shop.. Your blocks and props are:

#### `menu-sidebar` props

| Prop name   | Description                                                                                                            | Type                  | Default value |
| ----------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------- |
| `children`  | The property to render a native child in the tata-theme. In this case it will render the go to market button.          | `children`            | `""`          |
| `menuItems` | The property that receives a list of items for the shop's featured menu. This list can be changed via the site editor. | `array [{name, url}]` | `""`          |

### Loyality Points (Pontos Plus)

Component used to display the points that can be accumulated for each product in the shop. Your blocks and props are:

#### `loyality-points` props

| Prop name | Description                                                              | Type     | Default value |
| --------- | ------------------------------------------------------------------------ | -------- | ------------- |
| `view`    | The view where the component will be displayed, can be 'shelf' or 'pdp'. | `string` | `"shelf"`     |


### Carrousel with timer 

Component used to display a timer with a carrousel with products when the offer is active.

Dependencies:
[react-countdown](https://www.npmjs.com/package/react-countdown)
Its used for the timer


Props can be seted from site-editor:
#### `carrousel-with-timer` props

| Prop name          | Description                                                       | Type     | Default value |
| ------------------ | ----------------------------------------------------------------- | -------- | ------------- |
| `headerText`       | The text over top of timer.                                       | `string` | `""`          |
| `endTime`          | Date the promotion ends                                           | `Date`   | `""`          |
| `maxRemainingTime` | Maximum remaining time of the promotion                           | `number` | `""`          |

## Available Scripts

In the project directory, you can run:

    yarn

To log into the project's vendor, use the following command

    vtex login tatauyqadev

Create a development workspace using the following command,  
where wsname is the name of your workspace

    vtex use wsname

To run the project run the command

    vtex link

Access the url according to the ws created

Example:

    https://wsname--tatauyqadev.myvtex.com/

To run the unit tests run the command

    vtex test

## Documentations

Developing storefront apps with React and VTEX IO
[Documentation](https://developers.vtex.com/vtex-developer-docs/docs/welcome)

To know the other commands, access the
[VTEX IO CLI documentation](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-vtex-io-cli-command-reference)