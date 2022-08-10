---
title: "Jeffers Store Theme"
slug: "jefferspet-jefferspet-theme"
excerpt: "jefferspet.jefferspet-theme@6.2.2"
hidden: true
createdAt: "2022-07-11T08:40:02.919Z"
updatedAt: "2022-08-05T12:52:56.089Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Jeffers Store Theme is basic store front model based on the VTEX IO Store Framework.

## Preview

![store-theme-default](https://user-images.githubusercontent.com/61438477/143265300-eb90f7b2-489d-46ec-a1e4-178ae9ac2e76.png)

## Configuration

### Step 1 - Basic setup

Access the VTEX IO [basic setup guide](https://vtex.io/docs/getting-started/build-stores-with-store-framework/1) and follow all the given steps.

By the end of the setup, you should have the VTEX command line interface (Toolbelt) installed along with a developer workspace you can work in.

### Step 2 - Cloning the Jeffers Store Theme repository

[Use this template](https://github.com/ITGlobers/jeffers-theme-IO.git) repository to your local files to be able to effectively start working on it.

Then, access the repository's directory using your terminal.

### Step 3 - Editing the `Manifest.json`

Once in the repository directory, it is time to edit the Jeffers-Theme-io `manifest.json` file.

Once you are in the file, you must replace the `vendor` and `account` values. `vendor` is the account name you are working on and `account` is anything you want to name your theme. For example:

```json
{
  "vendor": "jefferspet",
  "name": "jefferspet-theme"
}
```

### Step 4 - Installing required apps

In order to use Store Framework and work on your store theme, it is needed to have both `vtex.store-sitemap` and `vtex.store` installed.

Run `vtex list` and check whether those apps are already installed.

If they aren't, run the following command to install them: `vtex install vtex.store-sitemap vtex.store -f`

### Step 5 - Uninstalling any existing theme

By running `vtex list`, you can verify if any theme is installed.

It is common to already have a `vtex.store-theme` installed when you start the store's front development process.

Therefore, if you find it in the app's list, copy its name and use it together with the command `vtex uninstall`. For example:

```json
vtex uninstall vtex.store-theme
```

### Step 6- Run and preview your store

Then time has come to upload all the changes you made in your local files to the platform. For that, use the `vtex link` command.

If the process runs without any errors, the following message will be displayed: `App linked successfully`. Then, run the `vtex browse` command to open a browser window having your linked store in it.

This will enable you to see the applied changes in real time, through the account and workspace in which you are working.

## Dependencies

All store components that you see on this document are open source too. Production ready, you can found those apps in this GitHub organization.

Store framework is the baseline to create any store using _VTEX IO Web Framework_.

- [Store](https://github.com/vtex-apps/store/blob/master/README.md)

Store GraphQL is a middleware to access all VTEX APIs.

- [Store GraphQL](https://github.com/vtex-apps/store-graphql/blob/master/docs/README.md)

### Store Component Apps

- [Header](https://github.com/vtex-apps/store-header/blob/master/docs/README.md)
- [Footer](https://github.com/vtex-apps/store-footer/blob/master/docs/README.md)
- [Slider Layout](https://github.com/vtex-apps/slider-layout/blob/master/docs/README.md)
- [Shelf](https://github.com/vtex-apps/shelf/blob/master/docs/README.md)
- [Telemarketing](https://github.com/vtex-apps/telemarketing/blob/master/docs/README.md)
- [Menu](https://github.com/vtex-apps/menu/blob/master/docs/README.md)
- [Login](https://github.com/vtex-apps/login/blob/master/docs/README.md)
- [Minicart](https://github.com/vtex-apps/minicart/blob/master/docs/README.md)
- [Category Menu](https://github.com/vtex-apps/category-menu/blob/master/docs/README.md)
- [Product Summary](https://github.com/vtex-apps/product-summary/blob/master/docs/README.md)
- [Breadcrumb](https://github.com/vtex-apps/breadcrumb/blob/master/docs/README.md)
- [Search Result](https://github.com/vtex-apps/search-result/blob/master/docs/README.md)
- [Product Details](https://github.com/vtex-apps/product-details/blob/master/docs/README.md)
- [Store Components](https://github.com/vtex-apps/store-components/blob/master/docs/README.md)
- [Order Placed](https://github.com/vtex-apps/order-placed/blob/master/docs/README.md)
- [Wordpress Integration](https://github.com/vtex-apps/wordpress-integration/blob/master/docs/README.md)

### Store Pixel Apps

- [Facebook Pixel](https://github.com/vtex-apps/facebook-pixel/blob/master/docs/README.md)
- [Google Tag Manager](https://github.com/vtex-apps/google-tag-manager/blob/master/docs/README.md)

<!-- ## Contributing

Check it out [how to contribute](https://github.com/vtex-apps/awesome-io#contributing) with this project. -->

## Custom Apps

We need some custom APPs to run this workspace.

- [Countdown App](https://github.com/ITGlobers/jeffers-countdown-app)
- [Custom Categories](https://github.com/ITGlobers/jeffers-custom-category-app)
- [Department Banner](https://github.com/ITGlobers/jeffers-department)
- [General Apps](https://github.com/ITGlobers/jeffers-general-apps)
- [My pets app](https://github.com/ITGlobers/-jefferspet-my-pets)
- [Live Chat](https://github.com/ITGlobers/jeffers-pixel-live-chat)
- [Live Chat Button](https://github.com/ITGlobers/jeffers-livechat)
- [Mega menú](https://github.com/ITGlobers/jefferspet-mega-menu)
- [Modal Product Content](https://github.com/ITGlobers/jeffers-modal-product-content)
- [More Options App](https://github.com/ITGlobers/jeffers-button-see-more)
- [My vets App](https://github.com/ITGlobers/jefferspet-my-vets)
- [Newsletter App](https://github.com/ITGlobers/jeffers-newsletter-app-custom)
- [Not Found Text](https://github.com/ITGlobers/jeffers-not-found-text)
- [Order Status](https://github.com/ITGlobers/jeffers-order-status)
- [Specification Product](https://github.com/ITGlobers/jeffers-product-specification)
- [Quick Order](https://github.com/ITGlobers/jeffers-quick-order)
- [Search List App](https://github.com/ITGlobers/search-list-app-jeffers)
- [Custom Wishlist](https://github.com/ITGlobers/jefferspet-wishlist)
- [Dropdown Wrapper](https://github.com/ITGlobers/jeffers-dropdown-wrapper)
- [Orders More Details](https://github.com/ITGlobers/jeffers-orders-more-details)
- [Fixed Prices App](https://github.com/ITGlobers/jefferspet-fixed-prices)
- [Address Validator](https://github.com/ITGlobers/jefferspet-address-validator/blob/main/manifest.json)
- [Custom Account](https://github.com/ITGlobers/jeffers-custom-account)
- [Checkout Address Validation](https://github.com/ITGlobers/jefferspet-checkout-address-validation)
- [Checkout Shipping Restriction](https://github.com/ITGlobers/jefferspet-checkout-shipping-restrictions)
- [Checkout Availability App](https://github.com/ITGlobers/jefferspet-checkout-availability-app)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!