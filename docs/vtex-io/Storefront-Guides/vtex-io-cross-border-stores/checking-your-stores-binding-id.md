---
title: "Checking your store's binding id"
slug: "checking-your-stores-binding-id"
hidden: false
createdAt: "2020-09-01T11:40:22.738Z"
updatedAt: "2020-10-07T14:32:47.618Z"
---

If your store is a [Multistore](https://help.vtex.com/en/tutorial/creating-multi-store-multi-domain--tutorials_510?locale=en) or a Cross-border one, it's important to know the `id` values of its related `bindings`'s.

Hence, for a step by step on how to access this information, check the following section.

## Step by step

1. [Install](https://developers.vtex.com/docs/guides/vtex-io-documentation-installing-an-app) the `vtex.admin-graphql-ide@3.x` app using your terminal.

2. Access the **GraphQL admin IDE** section of the desired account. You may find it in the admin's side-bar menu:

![adminsidebarmenu](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/checking-your-stores-binding-id-0.png)

3. From the dropdown list, choose the `vtex.tenant` app.
4. Write the following query command in the text box that is displayed:

```gql
query {
  tenantInfo {
    bindings {
      id,
      canonicalBaseAddress,
     defaultLocale
    }
  }
}
```

The expected response is a JSON object, as in:

```json
{
  "data": {
    "tenantInfo": {
      "bindings": [
        {
          "id": "706e9126-d0fc-46de-b12d-5f9649e61877",
          "canonicalBaseAddress": "{account}.myvtex.com/admin",
          "defaultLocale": "en-US"
        },
        {
          "id": "706e9126-d0fc-47de-9o2d-5f9649e61877",
          "canonicalBaseAddress": "{account}.myvtex.com/es",
          "defaultLocale": "es-AR"
        },
        {
          "id": "748aafcf-1674-456d-9ffc-7ddb3f26e43f",
          "canonicalBaseAddress": "{account}.myvtex.com/en",
          "defaultLocale": "en-US"
        }
      ]
    }
  }
}
```

That's all! Save the returned response as this information might be useful when managing your VTEX account.
