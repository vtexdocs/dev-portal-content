---
title: "Hotjar"
slug: "vtex-hotjar"
excerpt: "vtex.hotjar@0.1.6"
hidden: false
createdAt: "2020-06-03T15:19:17.355Z"
updatedAt: "2020-11-10T14:39:54.650Z"
---
# Hotjar

Open the VTEX APP Store and install the app on your store.

or

Run the following command:

```sh
vtex install vtex.hotjar@0.x
```

Next, open the app settings on your admin and fill the form with Site ID.

### Setup in Cart and Checkout page

Open your admin in the Checkout section in the `checkout6-custom.js`:

https://ACCOUNT.myvtex.com/admin/portal/#/sites/default/code/files/checkout6-custom.js

Add the following snippet in the file and replace `"YOURSITEID"` with your Site ID:

```js
// Hotjar
(function(h,o,t,j,a,r){
    var siteId = 'YOURSITEID';
    h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
    h._hjSettings={hjid:siteId,hjsv:6};
    a=o.getElementsByTagName('head')[0];
    r=o.createElement('script');r.async=1;
    r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
    a.appendChild(r);
})(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
```

Click Save.