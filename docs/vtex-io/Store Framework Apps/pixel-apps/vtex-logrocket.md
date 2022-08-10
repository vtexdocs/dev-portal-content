---
title: "LogRocket"
slug: "vtex-logrocket"
excerpt: "vtex.logrocket@1.0.1"
hidden: false
createdAt: "2020-06-03T15:19:09.791Z"
updatedAt: "2020-06-03T15:19:09.791Z"
---
# LogRocket

VTEX LogRocket first-party app

## How to install

Open a terminal and type:

```sh
vtex install vtex.logrocket@1.x
```

Open your admin in the Apps section:

https://YOURSTORENAME.myvtex.com/admin/apps/vtex.logrocket@1.0.0/setup


Fill in your LogRocket's Account ID and click save.

### Setup in Cart and Checkout page

**This step will not be needed in a couple of months!**

Open your admin in the Checkout section in the `checkout6-custom.js`:

https://ACCOUNT.myvtexdev.com/admin/portal/#/sites/default/code/files/checkout6-custom.js

Add the following snippet in the file:

```js
// LogRocket
(function() {
  var accountId = 'YOURACCOUNTID';
  var b=document.createElement("script");b.onload=function(){window.LogRocket && window.LogRocket.init(accountId);};b.type="text/javascript";b.crossOrigin="anonymous";b.src="https://cdn.lr-ingest.io/LogRocket.min.js";a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(b,a);
})();
```

Click Save.