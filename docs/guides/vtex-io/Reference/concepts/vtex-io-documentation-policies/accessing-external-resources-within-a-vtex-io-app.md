---
title: "Accessing external resources within a VTEX IO app"
slug: "accessing-external-resources-within-a-vtex-io-app"
excerpt: "Learn how apps gain access to external resources with policies."
hidden: false
createdAt: "2025-11-04T12:00:00.000Z"
updatedAt: "2025-11-04T12:00:00.000Z"
---

Apps may need to access resources that are external to the app itself. An external resource could be:

- An endpoint from another VTEX IO app (REST or GraphQL)
- A VTEX API
- An endpoint external to VTEX (e.g., a payment provider, an external marketplace, etc.)

To have access, apps must declare policies in the `policies` list of the [`manifest.json` file](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest).

The sections below show the types of policies an app can have to access external resources.

## When to declare policies

Apps need to declare policies to gain access to external resources, which include:

- Access to specific content (file, image, etc.)
- Access to VTEX APIs
- Access to resources exposed through role-based policies

> ℹ️Declaring policies is not required for resources exposed through [resource-based policies](?tab=t.0#heading=h.sszd0hc2sxz), since these policies already define which apps are allowed.

### Policies from License Manager

These policies have predefined names and are related to native VTEX resources. To declare a policy of this type in the manifest, use the policy name in the `"name”` field. See the example below:

```json
{
  "policies": [
    {
      "name": "Sku.aspx"
    }
  ]
}
```

You can find all available policy names in the **Key** column of the [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) table. For more details, see the [Policies from License Manager](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies-from-license-manager) article.

### Policies from VTEX IO apps (role-based)

These policies grant access to app routes exposed with [role-based policies](?tab=t.0#heading=h.a8px17wrz58r). This policy type is used to access [GraphQL queries exposed by IO apps](https://developers.vtex.com/docs/guides/developing-a-graphql-api-in-service-apps). To declare a policy of this type in the manifest, use the format `{vendor}.{app-name}:{policy-name}` in the `"name"` field. See the example below:

```json
{
  "policies": [
    {
      "name": "vtex.messages:graphql-translate-messages"
    }
  ]
}
```

To find out the names of the policies available in an app, you can see the app documentation or the `policies.json` file. Example: [Policies in the search-graph app](https://github.com/vtex-apps/search-graphql/blob/master/policies.json).

### Outbound-access policies

These policies should be used when none of the other types apply, with an explicit URL to the resource. Outbound-access policies are used to access resources external to VTEX.

To declare a policy of this type, use an object with the following structure:

- `"name"`: `"outbound-access"`.
- `"attrs"`: An object with two fields.
    - `"host"`: String with the first part of the URL, usually containing the host or domain name.
    - `"path"`: String with the last part of the URL, usually containing the path inside the domain name.

> ℹ️ `"host"` and `"path"` accept `{{account}}` as a variable and the `*` character as a wildcard.

Consider an app that needs access to the following resources:

- A VTEX API from the URL `{{account}}.vtexcommercestable.com.br/api/catalog_system/*`.
- The store's sitemap from the URL `{{account}}.vtexcommercestable.com.br/sitemap.xml`.
- An external resource from the URL `api.crowdin.com/api/project/*`.

For the app to gain access to these resources, declare the outbound-access policies as in the example below:

```json
{
  "policies": [
    {
      "name": "outbound-access",
      "attrs": {
        "host": "{{account}}.vtexcommercestable.com.br",
        "path": "/api/catalog_system/*"
      }
    },
    {
      "name": "outbound-access",
      "attrs": {
        "host": "{{account}}.vtexcommercestable.com.br",
        "path": "/sitemap.xml"
      }
    },
    {
      "name": "outbound-access",
      "attrs": {
        "host": "api.crowdin.com",
        "path": "/api/project/*"
      }
    }
  ]
}
```
