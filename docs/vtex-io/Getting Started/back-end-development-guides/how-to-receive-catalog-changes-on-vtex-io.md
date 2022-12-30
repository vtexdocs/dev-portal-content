---
title: "Receiving Catalog Changes on VTEX IO"
slug: "how-to-receive-catalog-changes-on-vtex-io"
hidden: false
createdAt: "2020-10-08T02:23:55.696Z"
updatedAt: "2021-03-25T14:46:35.907Z"
---
## Recipe
1. Clone the app [https://github.com/vtex-apps/events-example](https://github.com/vtex-apps/events-example)
    - This example app also exports some service routes, but we're not gonna use it. Feel free to remove it, or integrate just the **events** section into another app. Every IO app is able to handle events with a `node` service.

2. On `node/service.json`, change the event handler name and the `keys`. You can ditch the `sender` field as well. The final `events` section should be like so:

    ```json
    "events": {
    	"skuChange": {
    		"keys": ["broadcaster.notification"]
    	}
    },
    ```

    - The name `skuChange` you're free to change as well. This will be used to create the code to handle that event later on.

3. After saving the `node/service.json`, let's edit the `node/index.ts` file, creating the **handler function** for our event. We are gonna use the key `skuChange` to that.

    ```ts
    export default new Service<IOClients, State, ParamsContext>({
      clients: {
        options: {
          events: {
            exponentialTimeoutCoefficient: 2,
            exponentialBackoffCoefficient: 2,
            initialBackoffDelay: 50,
            retries: 1,
            timeout: TREE_SECONDS_MS,
            concurrency: CONCURRENCY,
          },
        },
      },
      events: {
        skuChange: (ctx: any) => {
    			console.log('Received SKU changed event')
    			console.log(ctx.body)
    		},
      },
      routes: {
        hcheck: (ctx: any) => {
          setCacheContext(ctx)
          ctx.status = 200
          ctx.body = 'ok'
        },
      },
    })
    ``` 
4. Now, to test it on a workspace, follow the steps [here](https://github.com/vtex-apps/broadcaster/tree/0856c6e2952c374ab34cc8d86de8bfb647fb41be#testing)