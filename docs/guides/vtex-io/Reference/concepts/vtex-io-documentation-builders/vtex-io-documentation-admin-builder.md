---
title: "Admin builder"
slug: "vtex-io-documentation-admin-builder"
excerpt: "Learn how to use the VTEX IO Admin builder."
hidden: false
createdAt: "2024-03-26T11:00:00.000Z"
updatedAt: "2024-03-26T11:00:00.000Z"
category: "App Development"
---

The `admin` builder is used to develop apps for the [VTEX Admin](https://help.vtex.com/en/tutorial/vtex-admin-start-here--531cHtUCUi3puRXNDmKziw) in combination with [React](https://react.dev). To understand better how to develop apps using this builder, access our [Admin Applications course](https://learn.vtex.com/docs/course-admin-lang-en).

## Folder structure

An app that uses the `admin` builder has an `admin` folder on its root, where are located the following files and directories:

```txt
admin
  ┣ 📄 navigation.json
  ┗ 📄 routes.json
```

- `navigation.json`: Defines the navigation in the Admin left panel for sections and pages. The file structure consists of an object or list of objects for each section, with a list of objects for the subsections (`"subSectionItens"` field).
- `routes.json`: Assigns the components to their corresponding routes (`"path"` field). The file structure consists of an object of objects, where each object defines a component with its route. The routes have to match the paths described in the `navigation.json` file. The names of the components (`"component"` field) have to match the React components in the `react` folder.

## Usage

To develop an app using the `admin` builder, refer to the following steps:

1. **Start with a template**: Download the [`admin-ui-example` template](https://github.com/vtex/admin-ui-example/tree/main) or create a new project using the [`vtex init` CLI command](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage#starting-a-new-project) and choose the `admin-example` option.
2. **Configure the navigation**: Edit the `navigation.json` file to define the structure of the sections and pages of the app in the Admin's left panel.
3. **Configure the routes**: Edit the `routes.json` file to define the components and associate them with the navigation.
4. **Implement the app's logic**: Add your frontend logic using React. Check the [Admin Applications course](https://learn.vtex.com/docs/course-admin-lang-en) for more details.
5. **Testing**: [Link the app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) to a development workspace for testing.

## Use case examples

Here are some app examples that use the `admin` builder:

- [checkout-ui-custom](https://github.com/vtex-apps/checkout-ui-custom)
- [storefront-permissions-ui](https://github.com/vtex-apps/storefront-permissions-ui)
- [admin-graphql-ide](https://github.com/vtex-apps/admin-graphql-ide)

As an example, check the file contents for this builder in the [Checkout UI Custom](https://developers.vtex.com/docs/apps/vtex.checkout-ui-custom):

### `navigation.json` file

In this example, there is a list of objects. It is also possible to have only a single object.

```json navigation.json
[
  {
    "section": "storeSetup",
    "titleId": "admin/checkout-ui.navigation.title",
    "path": "/admin/vtex-checkout-ui-custom/",
    "LMProductId": "27"
  },
  {
    "section": "storeSettings",
    "subSection": "storeFront",
    "adminVersion": 4,
    "LMProductId": "27",
    "subSectionItems": [
      {
        "labelId": "admin/checkout-ui.navigation.title",
        "path": "/admin/vtex-checkout-ui-custom/"
      }
    ]
  }
]
```

The properties in these objects are:

- `"adminVersion"`: Specifies the Admin version for the page. The presence of this property only in the second object indicates that the first one is for the Admin version `3.x` and the second one is for the [redesigned Admin](https://help.vtex.com/en/v4).
- `"section"` and `"subSection"`: indicate which section and subsection of the Admin the page will be, respectively. The first will be inside an existing section, `"storeSetup"`. The second object will be inside an existing section, `"storeSettings"`, and an existing subsection, `"storeFront"`.
- `"path"`: Contains the path in the URL to access the page, and correlates with the component defined in the `routes.json` file.
- `"subSectionItems"`: A list where each object represents a page in the subsection.
- `"titleId"` and `"labelId"`: Identifiers of the component. This will be used by the `messages` builder to map the navigation and the name of the app in each language.

### `routes.json` file

Here we have an object of objects, where each inner object maps a component to a path. The keys of the objects inside use the format `"admin.app.{routeName}"`, where `{routeName}` is an identifier to the route.

```json routes.json
{
  "admin.app.checkout-ui": {
    "component": "Admin",
    "path": "/admin/app/vtex-checkout-ui-custom"
  }
}
```

The properties of the inner object are:

- `"component"`: Name of the React component corresponding to the page in the route.
- `"path"`: Contains the path in the URL to access the page, and correlates with the component defined in the `navigation.json` file. Note that the path here only differs from the one in the `navigation.json` file by having a `/app` segment.

### Result

As we can see in the image of the app running in the Admin, the path in the address bar (`/admin/vtex-checkout-ui-custom/`) is the same as the one in the path property from the `navigation.json` file. In the Admin left navigation bar, we can see that the **Checkout UI Custom** app is inside the **Store Settings** section and the **STOREFRONT** subsection, as described by the `"section"`  and `"subSection"` properties.

![App using admin builder](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/admin-builder-app-example.jpg)
