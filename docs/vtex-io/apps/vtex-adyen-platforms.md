---
title: "Adyen Platforms"
slug: "vtex-adyen-platforms"
excerpt: "vtex.adyen-platforms@0.4.0"
hidden: true
createdAt: "2022-07-13T18:04:15.507Z"
updatedAt: "2022-08-01T14:31:45.067Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

This app integrates the [Adyen for Platforms](https://docs.adyen.com/platforms) service with your VTEX marketplace.

## Configuration

### Adyen Payment Setup

⚠️ Before you can use the Adyen Platforms app, the [Adyen Payment connector](https://github.com/vtex-apps/connector-adyen) must be installed and configured in you VTEX account.

### Contacting Adyen

Users must first contact Adyen to get their account enabled to use Adyen for Platforms. To check if Adyen for Platforms is activated, look for the presence of a `Platform` tab in the Adyen merchant account admin sidebar. Further information: [Adyen for Platforms Quick Start Guide](https://docs.adyen.com/platforms/quick-start)

### Installing the App

1. Install this app in the desired account using the CLI command `vtex install vtex.adyen-platforms`.
2. In your admin sidebar, search for `Adyen for Platforms`. This will bring you to the Adyen for Platforms settings page.
3. Select the `Settings` tab:
   - Enter your Platform API credentials. To find them, log in to Adyen's admin interface and do the following:
      - Switch from `Company` account to `Merchant` account
      - Under the **Developers** menu, select `API credentials`
      - Select the username that follows this format `ws\_[123456]@MarketPlace.[YourPlatformAccount]`, if there is no username in that format, see **Creating New Web Service User**
      - Use `Generate New API Key` to create a new key for Adyen and store it somewhere safe. This can be regenerated if lost
   - Enter your production Adyen for Platforms API endpoint. For testing, you can enter the test endpoint: `https://cal-test.adyen.com/cal/services`. This is also found under the **Developers** menu in your Adyen account.
   - Enter the URL sub-merchants will be directed to when they complete their onboarding. This is optional, see the Onboarding section for details on this process.

### Managing Seller Accounts

The Sellers tab in the Adyen for Platforms menu in your VTEX admin will display all Seller accounts in your VTEX marketplace.
- Users can `Create Adyen Account` for specific sellers
  1. Enter a unique Adyen Account Holder Code (this can be the seller account name within VTEX or another string of your choosing)
      - Note: To view any Adyen Account Holder Codes that are already in use:
        - Ensure you're on Adyen's `Merchant` account in Adyen's website
        - Under the `Platform` tab, select `Sub-merchants`
  2. Enter the Country, Entity Type, Business Name, and Business Email
  3. Set the desired payout schedule. See section `Payout Schedule` for more information
- Users can create a new `Onboarding Link` and use that link to onboard users.
  - Note: After onboarding, it may take awhile before the user is activated for use.

#### Onboarding New Sellers

If a seller has not yet been onboarded, you will have the option to create an Adyen account for the selected seller. This option creates a unique URL for that seller. The URL needs to be provided to the seller, which will direct them to the Adyen [hosted onboarding page](https://docs.adyen.com/platforms/hosted-onboarding-page).

You will be able to accept payment on behalf of a seller immediately after created a Adyen account for them, but payouts of collected payments will be disabled until the seller completes the Adyen onboarding process.

ℹ️ After completing the Adyen hosted onboarding, users will be redirecting to the URL you entered in the app settings. If no URL was entered, they are redirected back to a default onboarding success page that is provided when you install the app, `https://[Store]/marketplace/onboard-complete/`

#### Payout Schedule

The Adyen default payout schedule for a seller is `daily`. You can change this setting to the desired interval

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->