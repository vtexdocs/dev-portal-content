---
title: "My Account - Provider - Plug In"
slug: "lyracons-my-account-provider"
excerpt: "lyracons.my-account-provider@0.1.9"
hidden: true
createdAt: "2022-07-28T13:26:28.661Z"
updatedAt: "2022-07-28T13:26:28.661Z"
---
The **My Account - Provider - Plug In** application is responsible to lists all customer provider loaded on master data v1, and all the providers who are not yet suppliers to the customer

## Mobile Screen Shots

## Desktop Screen Shots

## Configuration

1. Install and Adding the app as a theme peerDependencies in the `manifest.json` file:

`vtex install lyracons.my-account-provider@0.x`

```diff
 "peerDependencies ": {
+  "lyracons..my-account-provider": "0.x"
 }
```

It is also important to run the attached postman collection in the "Postman" folder, as it will create and publish the corresponding entities for this application to work.

Sellers Entity: it will be where the information of the SWL configured in VTEX is loaded for the second time

Provider Entity: It will be in charge of having the information of which seller attends to which customer in which address (Point of Sale)


**That is all**

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

### CSS Handles

|       CSS Handles           |
|         :----               |
|   "providers"               |
|   "wrapperSpinner"          |
|   "spinner"                 |
|   "wrapperMessage"          |
|   "msjWarning"              |
|   "wrapperProviders"        |
|   "providerCard"            |
|   "providerCardContainer"   |
|   "wrapperImage"            |
|   "image"                   |
|   "wrapperInfo"             |
|   "info"                    |
|   "wrapperSeller"           |
|   "seller"                  |
|   "wrapperAddressName"      |
|   "addressName"             |
|   "wrapperSellerId"         |
|   "sellerId"                |
|   "wrapperVendorCustomerId" |
|   "vendorCustomerId"        |
|   "wrapperActions"          |
|   "actions"                 |
|   "wrapperWaitPage"         |
|   "wrapperWaitImage"        |
|   "waitImage"               |
|   "waitTitle"               |
|   "waitText"                |
|   "callToAction"            |
|   "wrapperModal"            |
|   "wrapperCallToAction"     |
|   "secondaryButton"         |
|   "wrapperModalContent"     |
|   "modalContent"            |
|   "wrapperTitle"            |
|   "title"                   |
|   "wrapperText"             |
|   "text"                    |
|   "wrapperIcon"             |
|   "iconDocument"            |
|   "wrapperInputs"           |
|   "wrapperInput"            |
|   "disabled"                |
|   "wrapperErrorPage"        |
|   "wrapperErrorImage"       |
|   "errorImage"              |
|   "errorTitle"              |
|   "errorText"               |
|   "disable"                 |
|   "danger"                  |
|   "warning"                 |
|   "success                  |


<!-- DOCS-IGNORE:start -->

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/chrisar45"><img src="https://avatars3.githubusercontent.com/u/19915537?v=4" width="100px;" alt=""/><br /><sub><b>Chris</b></sub></a><br /><a href="#" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

<!-- DOCS-IGNORE:end -->