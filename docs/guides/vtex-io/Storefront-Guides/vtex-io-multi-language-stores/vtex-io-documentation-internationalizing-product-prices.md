---
title: "Internationalizing product prices"
slug: "vtex-io-documentation-internationalizing-product-prices"
hidden: false
createdAt: "2020-06-03T16:02:44.310Z"
updatedAt: "2022-12-13T20:17:44.058Z"
excerpt: "Ensure seamless global shopping experiences by adopting ISO currency codes for international users."
---

As you expand your business globally, it becomes essential to properly internationalize your website's content to cater to users from different locales. One crucial aspect of internationalization is to ensure that users can easily understand product prices and make purchases without confusion caused by misleading currency conversions. To accomplish this, we will adopt the following approach: for international users, we will display prices according to the ISO standard of the currency code (e.g., `USD`), while for local users, we will use the country-specific commonly used currency symbol (e.g., `$`). This flexibility in displaying product prices will help create a user-friendly shopping experience for both local and international users.

## Before you begin

Before you start the internationalization process, it's essential to understand [trade policies](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV). Trade policies contain configurations for catalog, pricing, promotions, logistics, customer segmentation, and payments for different sales strategies. If your store operates in multiple sales channels with varying settings, you need to [create a new trade policy](https://help.vtex.com/tutorial/creating-a-trade-policy--563tbcL0TYKEKeOY4IAgAE) for each unique setup. Thus, before proceeding with this guide, ensure you have set up different trade policies that align with your store's operational requirements.

## Instructions

1. Access the Admin.
2. Go to **Store Settings > Channels > Trade Policies**.
3. Find the specific trade policy to which you want to apply the international pricing configurations and click the `Edit` button.
4. In the `Currency Code` field, select the currency code corresponding to the currency of the sales channel that uses this trade policy.
6. In the `Locale` field, select the locale where the sales channel is located.
7. Click `Save`.

> ℹ️ The `Currency Decimal Places` field is optional and should be used only when you want to overwrite the number of decimal places defined by the ISO standards.

Once you save your changes, your store will automatically recognize when a user's locale differs from the one set in the `Locale` field and display prices accordingly.

> ⚠️ The saved configuration will only apply to the selected trade policy. To replicate these configurations across all trade policies in your store, you must fill out the fields in each trade policy and save the changes.

Finally, let's take the following example. Imagine a retailer based in the United States with the following configurations:

- `Locale` field value: `United States (en-US)`
- `Currency Code` value: `US Dollar (USD)`

The outcome for different user groups will be as follows:

- **Local users (from the USA):** When a user's locale matches the `Locale` field (`United States (en-US)`), the currency symbol displayed for prices will be the commonly used symbol for the United States Dollar, which is `$`.
- **International users (outside the USA):** When a user's locale does not match the `Locale` field, the store will display product prices using the currency code specified in the `Currency Code` field, which is `USD`.
