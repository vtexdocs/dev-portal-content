---
title: "Google One-Tap Login"
slug: "google-one-tap-login"
hidden: false
createdAt: "2020-07-30T19:58:25.203Z"
updatedAt: "2025-11-12T20:00:32.997Z"
---

In this guide, you'll learn how to set up the Google One-tap login feature in your store.

Google One-tap authenticates users through a pop-up, creating a streamlined login experience. With this feature, a small pop-up appears, allowing returning users to sign in with a single click.

![google-one-tap](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-0.gif)

## Before you begin

<Steps>

### Have a store using Store Framework

Ensure your store has a Store Theme developed following the Storefront guide.

### Configure the Google OAuth 2.0 integration

The One-tap flow requires the store to have Google OAuth login set up. Learn more in the guide [Adding a Client Id and a Client Secret to log in with Google](https://help.vtex.com/docs/tutorials/adding-a-client-id-and-a-client-secret-to-log-in-with-google?locale=en).

</Steps>

## Instructions

### Step 1 - Setting up the Google OAuth 2.0 app

1. In the [Google Developers Console](https://console.developers.google.com/), go to the Google OAuth 2.0 configuration page.
2. Add all store domains to the **Authorized domains** list. Learn more in Google's guide [Authorized Domains](https://support.google.com/cloud/answer/15549257?visit_id=638985718078812310-3040234660&rd=1#authorized-domains).

 >ℹ️ Include both the website domain and the `{{accountName}}.myvtex.com` domain. The restricted `.myvtex.com` domain may be used for testing purposes.

    ![authorized-domains](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-1.png)

For more details on how to set up the Google OAuth app, refer to Google's documentation: [Configure your OAuth Consent Screen](https://developers.google.com/identity/one-tap/web/guides/get-google-api-clientid#configure_your_oauth_consent_screen) and [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849).

### Step 2 - Configuring One-tap on Site Editor

1. In the VTEX Admin, go to **Storefront > Site Editor**.
2. In the side menu, click the **Login** block. A new section for Google One-tap will be displayed.
3. Check the **Enable Google One-tap** on your store box.
4. Configure the following settings:
    - **Google One-tap alignment:** Choose which side of the page the pop-up appears on.
    - **Google One-tap top margin:** Set the top margin for the pop-up. This field accepts standard CSS [`top`](https://developer.mozilla.org/pt-PT/docs/Web/CSS/top) values (for example, `10px`, `2%`).
5. Click `Save`.

    ![one-tap-wiki-1](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-2.gif)

After following these steps, the Google One-tap feature will be active, and the pop-up will appear for signed-out users browsing your store.

## Google One-tap flow

Google One-tap flow is implemented by the [`vtex.login`](https://developers.vtex.com/docs/apps/vtex.login) app. The process is described below:

1. `vtex.login` checks if the user is logged in. The One-tap flow only starts for logged-out users.
2. `vtex.login` calls the [VTEX ID API](https://developers.vtex.com/docs/guides/login-integration-guide-webstore-oauth2#vtex-id) to get the store's OAuth `clientId`.
3. `vtex.login` triggers the One-tap pop-up.
4. The user clicks the **Continue as** button.
5. Google checks the user's identity and returns a JSON Web Token (JWT)  to `vtex.login`.
6. `vtex.login` POSTs a form containing the JWT and redirects the user to an endpoint at the VTEX ID API.
7. The API validates the JWT and redirects the user back to the website.

    ![google-one-tap](https://vtexhelp.vtexassets.com/assets/docs/src/google-one-tap___033c5242b3695b9dff2fa9aea304b959.png)
