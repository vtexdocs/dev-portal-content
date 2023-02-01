---
title: "My Authentication"
slug: "vtex-my-authentication"
hidden: false
createdAt: "2021-07-28T18:23:47.807Z"
updatedAt: "2022-08-30T13:04:37.639Z"
---

This VTEX IO app extends the [MyAccount](https://github.com/vtex-apps/my-account) app to add authentication-related menu options (`Authentication` tab). It is installed by default in every VTEX account. Just like `MyAccount`, this can be used in either `IO` or `Portal` stores.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-my-authentication-0.png)

## Table of Contents

- [Usage](#usage)
  - [Visibility](#visibility)
- [Customization](#customization)
  - [IO Stores](#io-stores)
  - [Portal Stores](#portal-stores)
- [CSS Handles List](#css-handles-list)
- [Contributors](#contributors)

## Usage

### Visibility

By default, the `Authentication` tab is not visible in the left-side menu of the [MyAccount UI](https://github.com/vtex-apps/my-account).

To make it visible, go into

https://`{{accountName}}`.myvtex.com/admin/apps/

and search for `My Account` among the `installed` apps. Then click `Settings`.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-my-authentication-1.png)

Set `Authentication` option to :white_check_mark: `Visible`, then click `Save`.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-my-authentication-2.png)

📢 **Disclaimer:** in a close future, the `Authentication` tab visibility will become always true.

> ℹ️ **Before making this tab visible**, you should [customize](#customization) it to match your store visual identity

## Customization

### IO Stores

In order to apply CSS customizations to the app, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization) (you don't have to worry about `block` or `blockClass`).

A list of all `CSS Handles` is in [this section](#css-handles-list).

You can see the `Authentication` UI being customized in:

https://`{{workspaceName}}`--`{{accountName}}`.myvtex.com/account#/authentication

### Portal Stores

In order to customize the app, create a `.css` file with your own rules. Your class selectors should reference the UI's pre-existing classes.

A list of all `CSS Handles` is in [this section](#css-handles-list).

📢 **Avoid** using element or position-based selectors, as the customization may break in the face of the smallest UI changes.

To upload your `.css` file, go to the VTEX CMS (`/admin/a`) and open the `CMS/Files Manager/.css` file. Click `Add` and you'll be able to upload it. This file is accessible from [VTEX CMS storage](https://help.vtex.com/en/tutorial/ver-o-conteudo-dos-arquivos-css-da-loja--U5v7DXpRSee86uqiKQUQi).

Lastly, you should link that `.css` file to the Account Page HTML Head by [editing the "Account" CMS template](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/Y6dPEF6GzROQ8PuYKxrKe).

You can see the `Authentication` UI being customized in:

https://`{{accountName}}`.vtexcommercestable.com.br/\_secure/account#/authentication

(if you want to use IO workspaces, just add the query string "?workspace=`{{workspaceName}}`")

## CSS Handles List

> ℹ️ **If you're in a Portal Store**, append the prefix `vtex_my-authentication_` to each handle for your CSS class selectors.

| CSS Handles                         |
| ----------------------------------- |
| `box_container`                     |
| `box_header`                        |
| `box_headerSeparator`               |
| `box_content`                       |
| `box_footer`                        |
| `errorAlert_container`              |
| `warnAlert_container`               |
| `authenticationScreen_container`    |
| `authenticationScreen_passBox`      |
| `newPassInput_container`            |
| `passValidation_container`          |
| `passValidation_title`              |
| `passValidation_content`            |
| `passValidation_minLengthNumber`    |
| `passValidation_minLength`          |
| `passValidation_number`             |
| `passValidation_lowerUpper`         |
| `passValidation_lower`              |
| `passValidation_upper`              |
| `passValidation_iconSuccess`        |
| `passValidation_iconFailure`        |
| `savePassButton_container`          |
| `skeletonEditPassword_content`      |
| `skeletonEditPassword_button`       |
| `currPassInput_container`           |
| `createPassword_text`               |
| `codeInput_container`               |
| `resendCodeButton_container`        |
| `maskedPassword_title`              |
| `maskedPassword_content`            |
| `loginSessionsBox_title`            |
| `loginSessionsBox_content`          |
| `skeletonLoginSessions_content`     |
| `skeletonLoginSessions_button`      |
| `loginSessionsScreen_container`     |
| `loginSessions_skeleton`            |
| `loginSessions_error`               |
| `loginSessions_list`                |
| `loginSessions_box`                 |
| `skeletonLoginSessionsScreen_title` |
| `skeletonLoginSessionsScreen_text1` |
| `skeletonLoginSessionsScreen_text2` |
| `loginSession_currSession`          |
| `loginSession_currSessionIcon`      |
| `loginSession_currSessionText`      |
| `loginSession_device`               |
| `loginSession_lastAccess`           |
| `loginSession_originDetails`        |
| `loginSession_fullAddress`          |
| `loginSession_firstAccess`          |

