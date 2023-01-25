---
title: "Setting up Lazy Load for pixel apps"
slug: "setting-up-lazy-load-pixel-apps"
hidden: false
createdAt: "2023-01-18T15:28:45.242Z"
updatedAt: "2023-01-18T15:28:45.242Z"
---
# Setting up Lazy Load for pixel apps

Lazy Load for pixel apps consists of delaying the injection of the pixel script snippet via render-server or by the app itself. For more information about pixel apps, read this [doc](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-pixel-app).

> :warning: This feature is in beta. Lazily loading pixel apps can cause misbehavior on all pixel apps. So, after setup, ensure all pixel apps are working properly.
>
> To set this up, you must have access to a VTEX account and the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference).

## Setting up the Lazy Load on an account

The setup consists of enabling the `experimentalLazyLoadAllPixels` setting on the `vtex.store` app and then enabling the `experimentalLazyLoad` setting for each pixel app.

> ℹ️ All ecommerce stores build on VTEX IO use `vtex.store`. To get more information about this app, check our [repository](https://github.com/vtex-apps/store).

| Setting | Description | Apply to | Values |
| ------- | ----------- | -------- | ------ |
| experimentalLazyLoadAllPixels | Enable or disable the lazy load feature for all pixel apps. | vtex.store | `true` - enable the lazy load. <br> `false` - disable the lazy load. |
| experimentalLazyLoad | This setting allows overriding the `experimentalLazyLoadAllPixels` setting. | Any pixel app | `"never"` - never loads lazily the pixel snippet. <br> `"default"` - load lazy according to experimentalLazyLoadAllPixels setting. <br> `"always"` - always loads lazily the pixel snippet. If the value of this setting is empty, it behaves equally to `"default"`. |

> Each of these settings can also be used on its own.

To set a value for any of those settings, you can use this command:

```sh
vtex settings set {vendor}.{appname} {name of the setting} {value of this setting}
```

Example of setting up the value `true` to the `experimentalLazyLoadAllPixels` setting:

```sh
vtex settings set vtex.store experimentalLazyLoadAllPixels true
```

## Making the Pixel App load itself lazily

To make the pixel app load itself lazily, you must add the `experimentalLazyLoad` property on the app [settingsSchema](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-4-configuringyourappsettings). By doing this, the `vtex.pixel-server` app will create a local setting `experimentalHasOwnLazyLoad` with value `true`.

> :warning: Do not add the `experimentalHasOwnLazyLoad` setting on the app `settingsSchema`, nor set it via VTEX IO CLI. This is an internal setting.

The pixel app can access the `experimentalLazyLoad` [setting](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-5-writingtheheaderandbodyscripts) like in this code example:

```js
const experimentalLazyLoad = "{{settings.experimentalLazyLoad}}"
```

Example of how to do the lazy load:

```js
(function() {
  const experimentalLazyLoad = "{{settings.experimentalLazyLoad}}" === "always"

  function whatShouldBeLazyLoadHere() { ... }

  if (isLazyLoad) {
    function lazyTimeout() {
      setTimeout(whatShouldBeLazyLoadHere, 5000)
      window.removeEventListener('load', lazyTimeout)
    }

    if (document.readyState === 'complete') {
      lazyTimeout()
    } else {
      window.addEventListener('load', lazyTimeout)
    }

    return
  }

  whatShouldBeLazyLoadHere()
})()
```

## Combination of all settings

| experimentalHasOwnLazyLoad | experimentalLazyLoad | experimentalLazyLoadAllPixels | Result |
| -------------------------- | -------------------- | ----------------------------- | ------ |
| false | never | false | Apps load normally. |
| false | never | true | A specific app loads normally, and all others load lazily. |
| false | default | false | Apps load normally. |
| false | default | true | All apps load lazily, including the specific app. |
| false | always | false | A specific app loads lazily, and all others load normally. |
| false | always | true | All apps load lazily. |
| true | never | false | Apps load normally. |
| true | never | true | A specific app loads normally, and all others load lazily. |
| true | default | false | Apps load normally. |
| true | default | true | A specific app loads itself lazily, and all others load lazily by render. |
| true | always | false | A specific app loads itself lazily. |
| true | always | true | A specific app loads itself lazily, and all others load lazily by render. |

> ℹ️ Lazy loading is one of many actions you can take to optimize performance. To know more about other possible practices, check our [guide](https://developers.vtex.com/docs/guides/vtex-io-documentation-best-practices-for-optimizing-performance#lazy-loading-page-metadata).
