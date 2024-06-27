---
title: "Unifying login for different accounts"
slug: "unifying-login-for-different-accounts"
hidden: false
createdAt: "2022-09-08T20:12:30.680Z"
updatedAt: "2022-09-08T20:27:41.235Z"
---

Diverse ecommerce operations may require different account structures according to their business needs, such as different stores belonging to the same group. When using multiple accounts, you can unify customer login to reduce friction and provide a smoother shopping experience.

In this guide, you will learn how to unify login for different VTEX accounts. This method enables you to use the VTEX ID authentication of a given store to authenticate shoppers accessing other stores with [OAuth 2.0](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2).

## Implementation

To unify login for different accounts, you must choose one account that will be the **primary account**. This means it will be the [OAuth identity provider](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#oauth2). Other accounts will be able to use the **primary account’s** login by acting as the service provider in the [OAuth flow of information](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#oauth2). These are referred to as **secondary accounts** in this tutorial.

> ℹ️ Learn more with the [OAuth specification document](https://www.rfc-editor.org/rfc/rfc6749) and [Store OAuth 2.0 integration guide](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2).

To implement this connection, you must:

- [Set up OAuth Provider in the primary account](#set-up-oauth-provider-in-the-primary-account)
- [Set up OAuth connection in the secondary account](#set-up-oauth-connection-in-the-secondary-account)

### Set up OAuth Provider in the primary account

To set up your OAuth Provider, follow these steps:

1. Use the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) to log in to your **primary account** by running the following command:

   ```shell
   vtex login {accountName}
   ```

2. Run this command to install the [OAuth Provider](https://github.com/vtex/oauth-provider) app:

   ```shell
   vtex install vtex.oauth-provider-admin
   ```

3. On the Admin panel of your **primary account**, go to **Apps > Installed apps > OAuth Provider**. This will take you to the [OAuth Provider](https://github.com/vtex/oauth-provider) app settings page.
4. Click `ADD OAUTH CLIENT`.
5. Fill in the new OAuth client information, which is the **secondary account**.

   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/unifying-login-for-different-accounts-1.PNG)

   - **Name**: this identifies the OAuth client. For instance, you may use the name of the corresponding **secondary account**.
   - **Allowed URI’s**:

      ```
      https://vtexid.vtex.com.br/VtexIdAuthSiteKnockout/ReceiveAuthorizationCode.ashx
      ```

   - **Credential Type**: `Web Store`.
   - **Login URL**:

      ```
      /login?returnUrl=
      ```

6. Click `SAVE`.
7. Once you have saved your new OAuth client, you will be able to see it on the OAuth Provider Admin tab. Click on the client’s name to see its details.
   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/unifying-login-for-different-accounts-2.PNG)
8. Copy the client ID and secret. You will need these credentials to set up the OAuth connection in the **secondary account**.
   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/unifying-login-for-different-accounts-3.PNG)

### Set up OAuth connection in the secondary account

Now that you have set an OAuth identity provider in your **primary account** and registered your **secondary account** as an OAuth client, you must head to the Admin panel of your **secondary account** and set up the connection between the accounts according to the [custom OAuth integration guide](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#integration).

For the purpose of this method, there is some custom OAuth configuration information that you must fill in specific ways. See the specification below to learn how to fill in this information for each configuration step of the [custom OAuth integration guide](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#integration).

>⚠️ The information below is meant for VTEX accounts using VTEX ID as identity providers. If you want to use a custom OAuth identity provider, see the  [custom OAuth integration guide](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#integration).

#### 1. Provider Details

| **Field** | **Specification** |
| - | - |
| **Client ID** key | `client_id` |
| **Client ID** value | `client_secret` |

#### 2. Authorization Code

| **Field** | **Specification** |
| - | - |
| **URL** | `https://{primaryAccountHost}/api/io/_v/oauth2/auth` |
| Custom query string parameter | `response_type`: `code` |
| **Callback Request Information** authorization code query string parameter key  | `code` |

> ℹ️ The **URL** above requires your account host. Learn more about how to set your [account host](https://help.vtex.com/tutorial/configuring-the-store-domain--tutorials_2450#registering-a-new-host).

#### 3. Access Token Exchange

| **Field** | **Specification** |
| - | - |
| **URL** | `https://{primaryAccountHost}/api/io/_v/oauth2/token` |
| **Set Content-Type** | `application/x-www-form-urlencoded` |
| **Authorization code** parameter key | `code` |
| Custom request query string parameter | `grant_type`: `authorization_code` |
| Response **access token** parameter key | `access_token` |
| Response **expires in** parameter key | `expires_in` |

> ℹ️ The **URL** above requires your account host. Learn more about how to set your [account host](https://help.vtex.com/tutorial/configuring-the-store-domain--tutorials_2450#registering-a-new-host).

#### 4. Get User Info

| **Field** | **Specification** |
| - | - |
| **URL** | `https://{primaryAccountHost}/api/io/_v/oauth2/userinfo/` |
| **Where to send Access Token** - **Send on query string** toggle | `Disabled |
| Response **User e-mail** parameter key | `email` |
| Response **User ID** parameter key | `userId` |
| Response **User name** parameter key | `username` |

> ℹ️ The **URL** above requires your account host. Learn more about how to set your [account host](https://help.vtex.com/tutorial/configuring-the-store-domain--tutorials_2450#registering-a-new-host).
