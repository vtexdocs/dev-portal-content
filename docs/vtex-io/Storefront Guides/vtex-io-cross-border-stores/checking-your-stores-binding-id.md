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

1. [Install](https://vtex.io/docs/recipes/store/installing-an-app) the `vtex.admin-graphql-ide@3.x` app using your terminal.

2. Access the **GraphQL admin IDE** section of the desired account. You may find it in the admin's side-bar menu:

![adminsidebarmenu](https://user-images.githubusercontent.com/52087100/66516950-95d29a00-eab8-11e9-8cea-080fbdab84d5.png)

3. From the dropdown list, choose the `vtex.tenant` app.
4. Write the following query command in the text box that is displayed:
[block:code]
{
  "codes": [
    {
      "code": "query{\n  tenantInfo{\n    bindings {\n      id,\n      canonicalBaseAddress,\n     defaultLocale\n    }\n  }\n}",
      "language": "text"
    }
  ]
}
[/block]
The expected response is a JSON object, as in:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"data\": {\n    \"tenantInfo\": {\n      \"bindings\": [\n        {\n          \"id\": \"706e9126-d0fc-46de-b12d-5f9649e61877\",\n          \"canonicalBaseAddress\": \"{account}.myvtex.com/admin\",\n          \"defaultLocale\": \"en-US\"\n        },\n        {\n          \"id\": \"706e9126-d0fc-47de-9o2d-5f9649e61877\",\n          \"canonicalBaseAddress\": \"{account}.myvtex.com/es\",\n          \"defaultLocale\": \"es-AR\"\n        },\n        {\n          \"id\": \"748aafcf-1674-456d-9ffc-7ddb3f26e43f\",\n          \"canonicalBaseAddress\": \"{account}.myvtex.com/en\",\n          \"defaultLocale\": \"en-US\"\n        }\n      ]\n    }\n  }\n}",
      "language": "json"
    }
  ]
}
[/block]
That's all! Save the returned response as this information might be useful when managing your VTEX account.