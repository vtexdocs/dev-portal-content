---
title: "Cookiebot"
slug: "arcaplanetqa-cookiebot"
excerpt: "arcaplanetqa.cookiebot@0.0.1"
hidden: true
createdAt: "2022-08-01T09:25:12.496Z"
updatedAt: "2022-08-01T09:25:12.496Z"
---
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

This is a Cookiebot first party integration app. The [solution](https://www.cookiebot.com/) helps make your use of cookies and online tracking compliant.

![Cookie dialog](https://user-images.githubusercontent.com/284515/77015180-d92c1100-6952-11ea-97e6-f2b94b900399.png)

## Configuration

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the `vtex.cookiebot` app;
2. In your VTEX account's admin, open the **App** section and select the Cookiebot App box;
3. Fill in your **Domain Group ID**. You can find yours at the [Cookiebot Settings page](https://manage.cookiebot.com/en/manage);

![Cookiebot Domain ID](https://user-images.githubusercontent.com/284515/77793196-6acd0a00-7048-11ea-9de5-0da4eb1c1917.png)

4. On the [Settings page](https://manage.cookiebot.com/en/manage), make sure you use **Active Consent**; 

<br/> <img width="500" src="https://user-images.githubusercontent.com/284515/78317146-de36b600-7537-11ea-885e-5b8a39d1db8c.png" />

5. On the [Cookies page](https://manage.cookiebot.com/en/cookies), run a Scan. After the scan is complete, make sure the following cookies are categorized as **Necessary**: `ASPXAUTH`, `checkout.vtex.com`, `CookieConsent`, `device`, `vtex_segment`, `vtex_session`, `VtexFingerPrint`, `VtexRCMacIdv7`, `VtexRCRequestCounter`, `VtexRCSessionIdv7`, `VtexWorkspace`;
6. Save your changes.
   
This pixel app also creates the page `/cookie-declaration` in your store with Cookiebot's Cookie declaration:

![Cookie declaration page](https://user-images.githubusercontent.com/284515/78317698-61a4d700-7539-11ea-9429-1a6275be1123.png)

You can edit the new page using the admin's Site Editor.

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