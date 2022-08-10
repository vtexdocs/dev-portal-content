---
title: "SKU Bindings"
slug: "vtex-admin-sku-binding"
excerpt: "vtex.admin-sku-binding@0.4.7"
hidden: true
createdAt: "2022-07-05T00:20:52.966Z"
updatedAt: "2022-08-02T12:52:30.907Z"
---
SKU Bindings is an admin application in which you can view the relations between the seller SKUs and marketplace SKUs. In this app, you can also perform actions like activating, inactivating, deleting and reassociating these bindings.

## Installation

Use [VTEX Toolbelt](https://www.npmjs.com/package/vtex) to install the app.

```bash
$ vtex install vtex.admin-sku-binding@0.x
```

## Usage

Access the application at:

https://{{accountName}}.myvtex.com/admin/sku-binding

## Support

Team: Catalog

GitHub Team: @catalog-engineering-team

Slack Channel: #team-catalog

## Contributing

Anyone is welcome to contribute to this repository!

### Working on a development environment

```bash
# Clone this repository
$ git clone https://github.com/vtex/admin-sku-binding.git

# Go to the project folder
$ cd admin-sku-binding

# Install the project dependencies in root folder
$ yarn

# Go to react folder
$ cd react

# Install the project dependencies in react folder
$ yarn

# Login to a testing VTEX account (eg. basedevmkp, sandboxintegracao)
$ vtex switch {{accountName}}

# Create a new workspace or use an existing one
$ vtex use {{workspaceName}}

# Link the application
$ vtex link

# Open your browser at: https://{{workspaceName}}--{{accountName}}.myvtex.com/admin/sku-binding
```

### Tests

Please make sure to update tests as appropriate.

```bash
# Go to react folder
$ cd react

# Run tests
$ yarn test
```

### API Requests

This application uses [SWR](https://swr.vercel.app/) and the [JavaScript interface for API Fetch](https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API/Using_Fetch) to perform requests to the Rest API. It is important to highlight that the requests authorization is done automatically because we are only making requests to the same domain. Please note that we cannot make cross-domain requests through SWR or API Fetch if they require VTEX authorization.

_Recommendation: We recommend making your changes on a separate branch and when you're done open a PR to merge these changes into main._

Thanks for reading me! :heart: