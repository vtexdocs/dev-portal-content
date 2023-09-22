### Using Clients on implementations

VTEX IO Services exports functions that receive a _context_ object. These functions can be a resolver function to a GraphQL field, a middleware to an HTTP server or an event handler, and, in all of them, you receive a `ctx` object of type [`Context`](https://github.com/vtex/node-vtex-api/blob/master/src/service/worker/runtime/typings.ts), and it is inside of `ctx.clients` where you'll find each client.

    ```typescript
    export const authorize = async (ctx: Context) {
    const { clients: { licenseManager } } = ctx
    ...
    const data = await licenseManager.canAccessResource(/*...*/)
    }
    ```

## Step by step

> ℹ️ If you want to jump to an example, check how the _StatusClient_ is setup on [service-example](https://github.com/vtex-apps/service-example).

Let's suppose you've created the Github client we've described above!

1. Make sure you've exported the _client_ from its module. _(Either [default or named export](https://medium.com/@etherealm/named-export-vs-default-export-in-es6-affb483a0910))_
2. Create a `node/clients/index.ts` file.
3. Paste the following snippet on it. _(If you've used named export on Step 2, change the import clause)_

```typescript
import { IOClients } from "@vtex/api";
import GithubClient from "./github.ts";

export class Clients extends IOClients {
  public get status() {
    return this.getOrSet("github", GithubClient);
  }
}
```

4. Now, import the Clients class on `node/index.ts` (the service _entrypoint_).
5. Create or edit a `clients` object of type `ClientsConfig<Clients>` _(from @vtex/api)_ like so:

```typescript
const clients: ClientsConfig<Clients> = {
  implementation: Clients,
  options: {
    default: {
      retries: 2,
      timeout: 2000,
    },
  },
};
```

6. Use the `clients` variable on the Service exported:

```typescript
export default new Service<Clients, State>({
  clients,
  routes: {
    ...
  },
})
```

7. Optional: Place this type declaration on the same `node/index.ts` file. It helps you type the implementation functions.

```typescript
declare global {
  type Context = ServiceContext<Clients, State>;
}
```

8. That's it ✨! Now you can, on your functions, access your client from the `ctx`.

```typescript
export const authorize = async (ctx: Context) {
 const { clients: { github } } = ctx
 ...
 const data = await github.getUser(/*...*/)
}
```
