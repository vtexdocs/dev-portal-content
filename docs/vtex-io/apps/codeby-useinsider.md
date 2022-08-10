---
title: "UseInsider"
slug: "codeby-useinsider"
excerpt: "codeby.useinsider@1.0.22"
hidden: true
createdAt: "2022-07-20T16:52:09.019Z"
updatedAt: "2022-08-09T12:35:21.733Z"
---
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

UseInsider integrate vtex stores with Insider plataform.

## Configuration 1

1. [Install the app](https://vtex.io/docs/recipes/store/installing-an-app)

2. Add the app settings and add your partnerId and partnerName. You can find yours at the [Use Insider Main page](https://useinsider.com/).

## Configuration 2

Run the following command:
```bash
vtex install vtex.userinsider@1.x
```
Next, open the app settings on your admin and fill the form with Partner ID and Partner Name.

Setup in Cart and Checkout page
Open your admin in the Checkout section in the checkout6-custom.js:

https://ACCOUNT.myvtex.com/admin/portal/#/sites/default/code/files/checkout6-custom.js

Add the following snippet in the file and replace "YOURPARTNERID" and "YOUTPARNERNAME with your 
UseInsider "partnerId" and "partnerName": 

```javascript
  (function(window) {
    const partnerId = "YOUR-PARTNER-ID";
    const partnerName = "YOUR-PARTNER-NAME";

    const domainName = window.location.origin
    const insiderUrl = `${domainName}/insider/checkout-script?partnerId=${partnerId}&partnerName=${partnerName}`

    const xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", insiderUrl, false);
    xmlHttp.send(null);

    const importScript = document.createElement("script");
    importScript.type = "text/javascript";
    importScript.id = "insider-checkout";
    importScript.text = xmlHttp.responseText;
    document.head.appendChild(importScript);
  })(window)
```
Click Save.
## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):