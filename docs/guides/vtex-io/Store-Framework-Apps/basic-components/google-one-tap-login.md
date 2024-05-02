---
title: "Google One-Tap Login"
slug: "google-one-tap-login"
hidden: false
createdAt: "2020-07-30T19:58:25.203Z"
updatedAt: "2020-07-30T20:02:10.211Z"
---

Google One-tap delivers a seamless experience with a small pop-up that can authenticate a user with a streamlined interface. The customer should be able to use this feature as follows:

1. Google One-tap pop-up is presented. [[1]](#bottom_note_1)
2. The User clicks on the *Continue as* button.
3. Google checks the user's identity.
4. The store refreshes itself or redirects the user (if on `/login` page) to the homepage.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-0.gif)

## Behavior

In VTEX stores, the One-tap flow is implemented by the `vtex.login` app. A more complete description of how that is done goes as follows:

1. `vtex.login` checks whether the user is logged in or not (it only starts the One-tap flow for unsigned users).
2. `vtex.login` calls our ID API to get the store's OAuth `clientId`.
3. `vtex.login` triggers the One-tap pop-up. [[2]](#bottom_note_2)
4. The User clicks on the *Continue as* button.
5. Google checks the user identity and returns a [JWT](https://tools.ietf.org/html/rfc7519) to `vtex.login`.
6. `vtex.login` executes a Form POST containing the [JWT](https://tools.ietf.org/html/rfc7519) and redirecting the user to an endpoint at our ID API.
7. The API validates the [JWT](https://tools.ietf.org/html/rfc7519) and redirects the user back to the website.

> <a name="bottom_note_1"></a>**1**: The pop-up that appears on non-login pages of the webstore can only be closed by clicking the x button on the top corner of the pop-up and will not auto-signin users.
>
> <a name="bottom_note_2"></a>**2**: If the user has already signed-up using One-tap once and is on the `/login` page, the One-tap `auto_select` option is turned on and the user is automatically signed-in and redirected.

## Setup

There are a few steps required to correctly configure One-tap in a store:

- Configuring the Google OAuth 2.0 integration.
- Setting up the Google OAuth 2.0 app
- Enabling the feature on VTEX ID.
- Setting up the Google One-tap pop-up on Site Editor.

## Configuring the Google OAuth 2.0 integration

The One-Tap flow requires the store to have Google OAuth login already set up. This can be done by following [this tutorial](https://help.vtex.com/tutorial/registering-a-client-id-and-a-client-secret-for-login-with-google--1lBgDmetUM4goie6mYEOK6?locale=en) on our help center.

## Setting up the Google OAuth 2.0 app

All web store domains must be added to the [*Authorized domains*](https://support.google.com/cloud/answer/6158849#authorized-domains) list on the Google OAuth 2.0 configuration page, inside [Google Developers Console](https://console.developers.google.com/).
![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-1.png)

> **Note**: We advise clients to add both their website domain and also the `{{accountName}}.myvtex.com` domain, as our restricted `.myvtex.com` domain can be used for testing.

You can check [Configure your OAuth Consent Screen](https://developers.google.com/identity/one-tap/web/guides/get-google-api-clientid#configure_your_oauth_consent_screen) and [Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849) for more details on how to set up the Google OAuth app.

## Enabling the store on VTEX ID

This is an experimental feature that requires special configuration inside VTEX ID, our authentication service. So, for it to work properly you need to ask your *Account Manager* to enable it or create a support ticket requesting it.

## Setting up One-tap on Site Editor

This step does not depend on the previous one, meaning it can be done before enabling the feature on VTEX ID, but it won't work properly.

As of `vtex.login@2.31.x` there's a new section on the Login submenu of the Site Editor

![one-tap-wiki-1](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/google-one-tap-login-2.gif)

Under this section, you can enable Google One-tap on their stores and also configure in which side of the page it appears in (*Google One-tap alignment*) and the top margin of the pop-up (*Google One-tap top margin*).

> **Note:** The *Google One-tap top margin* configuration accepts the same values as the CSS property [`top`](https://developer.mozilla.org/pt-PT/docs/Web/CSS/top) accepts.
