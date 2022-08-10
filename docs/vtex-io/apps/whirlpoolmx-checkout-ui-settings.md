---
title: "Checkout UI Settings Template"
slug: "whirlpoolmx-checkout-ui-settings"
excerpt: "whirlpoolmx.checkout-ui-settings@0.0.63"
hidden: true
createdAt: "2022-07-06T16:24:48.858Z"
updatedAt: "2022-07-08T03:24:30.181Z"
---
The Checkout UI Settings app is responsible for **customizing your store's Checkout UI through scripts**.

See [the Vtex documentarion](https://developers.vtex.com/vtex-developer-docs/docs/vtex-checkout-ui-settings) or the [repository provided by Vtex](https://github.com/vtex-apps/checkout-ui-settings) for more info.

This template uses [Webpack](https://webpack.js.org/) to automate the development experience. In conjunction with the Vtex toolbelt, this provides a more seamless
experience for the developer.

Modify the files:

- `src/checkout6-custom.js`
- `src/checkout-instore-custom.js`
- `src/checkout-confirmation-custom.js`

to add custom scripts to the checkout template.

And modify the files:

- `src/checkout6-custom.scss`
- `src/checkout-instore-custom.scss`
- `src/checkout-confirmation-custom.scss`

to customize the appereance of the checkout page using [SASS](https://sass-lang.com/documentation/syntax) to build CSS files.

Additionally, you can load `.svg` files to the scripts by using ES6-style imports
```javascript
import MySvg from './route/to/svg/file.svg'
.
.
.
<div>
	</MySvg>
</div>

```

The code in this template emits two events especially for Vtex developers: `reactReady` and `vtexjsReady`. This way you dont have to write custom code everytime you have to wait for those libraries to finish loading. Just listen for the event `$(window).on('vtexjsReady', function(){})` and code away!

## Configuration

1.  Using your terminal and the [VTEX IO Toolbelt](https://vtex.io/docs/recipes/development/vtex-io-cli-installment-and-command-reference), log into the desired account;
2. Run `yarn install` or `npm install` if you prefer to use NPM.
3. The following scripts are available (execute `yarn run dev` or `npm run dev`, for example)
    - `dev` : Run webpack in watch mode, compiling development versions of the source.
    - `build`: Compile the source code into production-ready files.
    - `build:dev`: Compile into development versions
    - `dev:link`: Run webpack in watch mode and `vtex link` at the same time, updating the template everytime the source changes (you still have to refresh your browser)

You can modify the file `webpack.config.js` to add more file loaders or customizations to the template or the build process.

## Modus Operandi 

Once the app is deployed and installed in the account, every scripts contained in it will be automatically linked to your store and used to [build the templates](https://help.vtex.com/tutorial/configure-template-in-smartcheckout-update--ToTE5XB39t0SwtHgpgwSv?locale=en#configuring-templates-from-the-code-menu) to customize your Checkout.


:warning: **Scripts used by Checkout are linked to the Checkout UI Settings version that's installed in your store**. If a prior app version was already installed and your want to change the scripts linked to it, you'll need to repeat the already existing code and thereafter launch the app's new version containing the changes you just did. Housekeeper is responsible for updating app versions in the accounts it's installed in.