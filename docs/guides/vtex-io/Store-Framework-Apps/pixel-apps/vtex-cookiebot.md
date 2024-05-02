---
title: "Cookiebot"
slug: "vtex-cookiebot"
hidden: false
createdAt: "2020-06-03T15:19:30.787Z"
updatedAt: "2021-09-28T13:22:41.852Z"
---

This is a Cookiebot first party integration app. The [solution](https://www.cookiebot.com/) helps make your use of cookies and online tracking compliant.

![Cookie dialog](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-cookiebot-0.png)

## Configuration

1. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app/) the `vtex.cookiebot` app;
2. In your VTEX account's admin, open the **App** section and select the Cookiebot App box;
3. Fill in your **Domain Group ID**. You can find yours at the [Cookiebot Settings page](https://manage.cookiebot.com/en/manage);

![Cookiebot Domain ID](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-cookiebot-1.png)

4. On the [Settings page](https://manage.cookiebot.com/en/manage), make sure you use **Active Consent**;

<br/> <img width="500" src="https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/images/vtex-cookiebot-3.png" />

5. On the [Cookies page](https://manage.cookiebot.com/en/cookies), run a Scan. After the scan is complete, make sure the following cookies are categorized as **Necessary**: `ASPXAUTH`, `checkout.vtex.com`, `CookieConsent`, `device`, `vtex_segment`, `vtex_session`, `VtexFingerPrint`, `VtexRCMacIdv7`, `VtexRCRequestCounter`, `VtexRCSessionIdv7`, `VtexWorkspace`;
6. Save your changes.

This pixel app also creates the page `/cookie-declaration` in your store with Cookiebot's Cookie declaration:

![Cookie declaration page](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-cookiebot-2.png)

You can edit the new page using the admin's Site Editor.
