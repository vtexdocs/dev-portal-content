# Setup Lazy Load for Pixel Apps

The Lazy Load for pixel apps consists of delaying the injection of the pixel script snippet via render-server or by the app itself. For more information about pixel apps, read this [doc](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-pixel-app).

> :warning: Lazily loading pixel apps can cause misbehavior on all pixel apps. So, after setup, make sure that all pixel apps are working properly.
>
> To do this setup, you will need to have access to an account and the [toolbelt](https://github.com/vtex/toolbelt#installing-the-toolbelt-with-yarn).

## Setting up the Lazy Load on an account

The setup consists of enabling the `experimentalLazyLoadAllPixels` setting on the *vtex.store* app and then enabling the `experimentalLazyLoad` setting for each pixel app.

| Setting | Description | Apply to | Values |
| ------- | ----------- | -------- | ------ |
| experimentalLazyLoadAllPixels | Enable or disable the lazy load feature for all pixel apps. | vtex.store | `true` - enable the lazy load <br> `false` - disable the lazy load. |
| experimentalLazyLoad | This setting allows overriding the `experimentalLazyLoadAllPixels` setting. | Any pixel app | `"never"` - never loads lazily the pixel snippet <br> `"default"` - load lazy according to experimentalLazyLoadAllPixels setting <br> `"always"` - always loads lazily the pixel snippet <br><br> If the value of this setting is empty, it behaves equally to `"default"`. |

> Each of these settings can also be used on its own.

To set a value for any of those settings, you can use this command:

```sh
vtex settings set <<vendor>>.<<appname>> <<value of this setting>>
```

Example setting up the value `true` to the `experimentalLazyLoadAllPixels` setting:

```sh
vtex settings set vtex.store experimentalLazyLoadAllPixels true
```

## Making the Pixel App load itself lazily

To make the pixel app load itself lazily, you need to add the `experimentalLazyLoad` property on the app [settingsSchema](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-4-configuringyourappsettings). By doing this, the _vtex.pixel-server_ app will create a local setting `experimentalHasOwnLazyLoad` with value `true`. 

> :warning: Don't add the `experimentalHasOwnLazyLoad` on app settingsSchema or set it via toolbelt. This is an internal setting.

The pixel app can access the `experimentalLazyLoad` [setting](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-5-writingtheheaderandbodyscripts) doing this:

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
| false | never | false | Apps load normally |
| false | never | true | A specific app loads normally, and all others load lazily |
| false | default | false | Apps load normally |
| false | default | true | All apps load lazily, including the specific app |
| false | always | false | A specific app loads lazily, and all others load normally |
| false | always | true | All apps load lazily |
| true | never | false | Apps load normally |
| true | never | true | A specific app loads normally, and all others load lazily |
| true | default | false | Apps load normally |
| true | default | true | A specific app loads itself lazily, and all others load lazily by render |
| true | always | false | A specific app loads itself lazily |
| true | always | true | A specific app loads itself lazily, and all others load lazily by render |
