---
title: "3. Using VTEX IO clients"
slug: "calling-commerce-apis-3-using-vtex-io-clients"
hidden: false
createdAt: "2023-12-11T15:40:00.000Z"
updatedAt: "2023-12-11T15:40:00.000Z"
---

Now equipped with knowledge on authenticating API calls in VTEX IO, let's dive into the practical aspect of calling VTEX Core Commerce APIs using native [Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients). In this guide, we'll specifically leverage the `Catalog` client to retrieve SKU details within the VTEX platform.

In VTEX IO, Clients act as abstractions for external services, simplifying external requests in backend services. We strogly recommend using pre-built Clients from the [@vtex/clients](https://github.com/vtex/io-clients) package for VTEX Core Commerce services and [developing custom Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-how-to-create-and-use-clients) for external providers (e.g., [Google Maps API](https://developers.google.com/maps/apis-by-platform)).

<CH.Scrollycoding>

## Installing the `@vtex/clients` package

The [`@vtex/clients`](https://github.com/vtex/io-clients) package is a TypeScript library featuring pre-configured Clients for accessing VTEX Core Commerce APIs' capabilities. To use it in your app, change to the `node` folder and install the `@vtex/clients` package by running the command presented in the right panel.

```sh Terminal
cd node && yarn add @vtex/clients
```

---

## Configuring the Catalog client

Update your app's client `node/clients/index.ts` by importing the `Catalog` Client from the `@vtex/clients` library and exporting it to your `Clients` object. From now on, any function in your app can use the `Catalog` Client via `ctx.clients.catalog`. Also, thanks to TypeScript typing capabilities, autocomplete will become available for the methods exported by the `Catalog` client.

```typescript node/clients/index.ts focus=1,12:14
import { IOClients } from '@vtex/api'
import { Catalog } from '@vtex/clients'

import Status from './status'

// Extend the default IOClients implementation with our own custom clients.
export class Clients extends IOClients {
  public get status() {
    return this.getOrSet('status', Status)
  }

  public get catalog() {
    return this.getOrSet('catalog', Catalog)
  }
}
```

![Client methods autocomplete](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/calling-commerce-apis-3-using-vtex-io-clients.jpeg)

---

## Using the Catalog client

Now, let's use the `getSkuById` method from the `Catalog` client to retrieve information from a Stock Keeping Unit (SKU) in the VTEX Catalog. To do so, we will update the `status` route logic to read the `code` parameter as an SKU ID and return SKU details. 

Open the `node/middlewares/status.ts` file and update it as in the following:

- Extract the `catalog` client from the `ctx` received in the middleware functions. Learn more about Destructuring on the [Mozilla docuentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).
- Extract the variable `code`, which will be used as the `code` parameter of our route (`/_v/status/:code`).
- Call the `getSkuById` method from the `Catalog` client. This method will internally call the necessary endpoints of the Catalog API, passing the `code` parameter as the SKU ID to be searched. Also, since this is an asynchronous call, ensure to use the `await` to wait for it.

```typescript node/middlewares/status.ts mark=3,4,7
export async function status(ctx: Context, next: () => Promise<any>) {
  const {
    state: { code },
    clients: { catalog },
  } = ctx

  const data = await catalog.getSkuById(code.toString())
  ctx.body = data

  await next()
}
```

---

## Declaring the necessary policies

Usually, native Clients are already automatically configured to make authenticated calls using the app token. Nevertheless, you still need to declare that your app will be making requests for some service.

To do so, open the `manifest.json` file and add the highlighted code in the right panel to the `policies` section. This will allow your app to make calls to the Catalog API.

```json manifest.json mark=19:25
{
  "name": "service-example",
  "vendor": "vtex",
  "version": "0.1.1",
  "title": "Service Example",
  "description": "Reference app for VTEX IO Services",
  "mustUpdateAt": "2018-01-04",
  "categories": [],
  "dependencies": {},
  "builders": {
    "node": "7.x",
    "docs": "0.x"
  },
  "scripts": {
    "prereleasy": "bash lint.sh"
  },
  "credentialType": "absolute",
  "policies": [
    {
      "name": "outbound-access",
      "attrs": {
        "host": "portal.vtexcommercestable.com.br",
        "path": "/api/catalog/*"
      }
    },
    {
      "name": "colossus-fire-event"
    },
    {
      "name": "colossus-write-logs"
    }
  ],
  "$schema": "https://raw.githubusercontent.com/vtex/node-vtex-api/master/gen/manifest.schema"
}
```

---

## Fetching the SKU data

With the app linked to your development workspace, copy and send a GET request to the public URL that your service is exposing. Paste in the address bar `https://{workspace}--{account}.myvtex.com/_v/status/1` to find information about the SKU ID `1`. The expected result should be a JSON with the SKU data, fetched from the Catalog API.

<CH.Code>

```sh Terminal mark=4
16:39:05.042 - info: Worker 26 is listening service-node@6.27.4 16:39:05.567 info: Runtime @vtex/api is: /usr/local/app/node_modules/@vtex/api/lib/index.js service-node@6.27.4
16:39:85.568 - info: Using @vtex/api from: /usr/local/data/service/node_modules/@vtex/api/lib/index.js service-node@6.27.4
16:39:05.929 - info: Available service routes:
https://myworkspace--myaccount.myvtex.com/_v/status/:code service-node@6.27.4
16:39:05.932 - info: App running service-node@6.27.4
16:39:85.956 - info: Debugger tunnel listening on :9229. Go to chrome://inspect in Google Chrome to debug your running application.
```

---

```json GET
{
  "Id": 1,
  "ProductId": 1,
  "IsActive": true,
  "ActivateIfPossible": true,
  "Name": "Tanque Duplo Tramontina Hera Duo Plus 2C 30 + 30 L em Aço Inox Acetinado 120 x 55 cm",
  "RefId": "94406117",
  "PackagedHeight": 1,
  "PackagedLength": 1,
  "PackagedWidth": 1,
  "PackagedWeightKg": 20000,
  "Height": null,
  "Length": null,
  "Width": null,
  "WeightKg": null,
  "CubicWeight": 1,
  "IsKit": false,
  "CreationDate": "2023-07-12T09:15:00",
  "RewardValue": null,
  "EstimatedDateArrival": null,
  "ManufacturerCode": "94406117",
  "CommercialConditionId": 1,
  "MeasurementUnit": "un",
  "UnitMultiplier": 1,
  "ModalType": "FURNITURE",
  "KitItensSellApart": false,
  "Videos": []
}
```

</CH.Code>

</CH.Scrollycoding>
