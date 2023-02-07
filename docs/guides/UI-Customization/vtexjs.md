---
title: "vtex.js"
slug: "vtexjs"
hidden: false
createdAt: "2021-11-05T18:32:39.058Z"
updatedAt: "2021-11-05T19:00:06.696Z"
---
With vtex.js you can manipulate catalog and checkout data from the client's side, customizing the store template with additional information according to your business needs.

## Installation

vtex.js depends on jQuery, so make sure it is included in the page before vtex.js.

You may insert all the modules from vtex.js in your store:

```html
<script src="//io.vtex.com.br/vtex.js/2.0.0/vtex.min.js"></script>
```

Or you may insert the modules individually:
```html
<script src="//io.vtex.com.br/vtex.js/2.0.0/extended-ajax.min.js"></script>
<script src="//io.vtex.com.br/vtex.js/2.0.0/catalog.min.js"></script>
<script src="//io.vtex.com.br/vtex.js/2.0.0/checkout.min.js"></script>
```

Now you have access to various methods to use VTEX APIs through the objects `vtexjs.catalog` and `vtexjs.checkout`.


## Modules

vtex.js is made up of several modules, which contain functions that are used to communicate with VTEX services.

The modules reside in the global `vtexjs` object. When you include a module script, an object with all methods is created to access the APIs of that module. For example, by adding the Checkout module, you now have the `vtexjs.checkout` object, with several methods for accessing the Checkout API.

### Checkout module

The Checkout module handles customer purchase data.

Checkout adds different data needed to create an order: client profile data, address, shipping, items data, and others.

The `OrderForm` is the structure that contains this clustered data. It consists of several sections, each with useful information that can be accessed, manipulated, and (possibly) changed. To learn more, refer to the [orderForm documentation](https://developers.vtex.com/docs/guides/orderform-fields).

Check the complete documentation for all methods of this module [here](https://developers.vtex.com/vtex-rest-api/docs/vtexjs-for-checkout).


### Catalog module 

The Catalog module gets data related to your store's products.

Read the complete documentation for all methods of this module [here](https://developers.vtex.com/vtex-rest-api/docs/vtexjs-for-catalog).


## Development

In order to develop properly, clone the [vtex.js repository](https://github.com/vtex/vtex.js), install the dependencies, and run the command: 

```shell
sudo grunt
```
Now vtex.js can be linked to other repositories for development.
