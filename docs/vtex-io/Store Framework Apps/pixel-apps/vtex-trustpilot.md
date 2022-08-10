---
title: "Trustpilot"
slug: "vtex-trustpilot"
excerpt: "vtex.trustpilot@2.1.0"
hidden: false
createdAt: "2020-06-03T15:19:16.745Z"
updatedAt: "2021-08-02T18:16:14.401Z"
---
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

This is a Trustpilot first-party integration app. The [solution](https://www.trustpilot.com/) provides a review platform for your store.

## Configuration

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the `vtex.trustpilot` app in the VTEX account in which you are working;
2. In your VTEX account's admin, open the **App** section and select the Trustpilot App box;
3. Fill in your integration key, provided by Trustpilot, in the fields;
4. Save your changes.

### Using the Trustpilot's Widget component

The `trustpilot` app also enables Truspilot's widget component to be added to your store theme by adding the `trustpilot-micro-review-count` block in a template of your choosing.

1. Using a [Developer workspace](https://vtex.io/docs/recipes/development/creating-a-development-workspace/), open your store's theme directory in your code editor and add the `shop-review-interfaces` app as a dependency in the `manifest.json` file:

```diff
  "dependencies": {
+    "vtex.shop-review-interfaces": "0.x"
  }
```

2. Add the `shop-review-badge` block, exported by the `shop-review-interfaces`, in a template and block of your choosing, such as the Footer;
3. Save your changes and [link](https://vtex.io/docs/recipes/development/linking-an-app/) the store theme app;
4. Once your changes linked, access the admin's Site Editor using the same Developer workspace (`{workspaceName}-{accountName}.myvtex.com/admin/cms/site-editor`) and look for the `Trustpilot - Generic Widget` block;
5. When editing the block, add the widget's `template id` and `business unit id` value provided by the [Trustpilot's widget](https://widgets-trustboxinstructions.b2b.trustpilot.com/#/trustbox/eyJjb2RlSGVhZCI6IjwhLS0gVHJ1c3RCb3ggc2NyaXB0IC0tPlxuPHNjcmlwdCB0eXBlPVwidGV4dC9qYXZhc2NyaXB0XCIgc3JjPVwiLy93aWRnZXQudHJ1c3RwaWxvdC5jb20vYm9vdHN0cmFwL3Y1L3RwLndpZGdldC5ib290c3RyYXAubWluLmpzXCIgYXN5bmM%252BPC9zY3JpcHQ%252BXG48IS0tIEVuZCBUcnVzdEJveCBzY3JpcHQgLS0%252BIiwiY29kZUJvZHkiOiI8IS0tIFRydXN0Qm94IHdpZGdldCAtIE1pY3JvIFJldmlldyBDb3VudCAtLT5cbjxkaXYgY2xhc3M9XCJ0cnVzdHBpbG90LXdpZGdldFwiIGRhdGEtbG9jYWxlPVwiaXQtSVRcIiBkYXRhLXRlbXBsYXRlLWlkPVwiNTQxOWI2YThiMGQwNGEwNzY0NDZhOWFkXCIgZGF0YS1idXNpbmVzc3VuaXQtaWQ9XCI1ZTc0ZTJkYjYwMGQxYTAwMDFiZTE1ODlcIiBkYXRhLXN0eWxlLWhlaWdodD1cIjI0cHhcIiBkYXRhLXN0eWxlLXdpZHRoPVwiMTAwJVwiIGRhdGEtdGhlbWU9XCJsaWdodFwiPlxuICA8YSBocmVmPVwiaHR0cHM6Ly9pdC50cnVzdHBpbG90LmNvbS9yZXZpZXcvbWlyaWFkZS5jb21cIiB0YXJnZXQ9XCJfYmxhbmtcIiByZWw9XCJub29wZW5lclwiPlRydXN0cGlsb3Q8L2E%252BXG48L2Rpdj5cbjwhLS0gRW5kIFRydXN0Qm94IHdpZGdldCAtLT4iLCJ0cnVzdEJveE5hbWUiOiJNaWNybyBSZXZpZXcgQ291bnQiLCJsb2NhbGUiOiJpdC1JVCJ9);
6. Save your changes;
7. Access your store's website using the Developer workspace to check out the new component. If no more changes are desired, repeat the steps above in a [Production workspace](https://vtex.io/docs/recipes/development/creating-a-production-workspace/) and then [promote it to Master](https://vtex.io/docs/recipes/development/promoting-a-workspace-to-master).


:information_source: _The integration key must be provided by Trustpilot._

The `trustpilot` app also enables Truspilot's widgets to be added to your store theme by inserting the `shop-review-badge` interface in your layout and then using the `trustpilot-widget` block in a template of your choosing.

| Interface           | Block               | Description                             |
| ------------------- | ------------------- | --------------------------------------- |
| `shop-review-badge` | `trustpilot-widget` | Adds a Trustpilot widget in your store. |


## Block without badge

To use widget without `shop-review-badge` to landing pages, for example, you can use `trustpilot-widget`. Therefore, you need to add the following in the manifest.json file.

```diff
 "peerDependencies": {
+   "vtex.trustpilot": "1.x"
 }
```
## `trustpilot-widget` as props

```json
{
   "trustpilot-widget#home":{
      "title":"Widget TrustPilot",
      "props":{
         "width":"100%",
         "height":"240px",
         "theme":"light",
         "stars":"4,5",
         "businessUnitId":"597a23fwffdsfe05a793fe",
         "templateId":"5419b6a8b0d04a076446a9ad"
      }
   }
}
```

| Prop name |   Type   |                         Description                         | Default value |
| :-------: | :------: | :---------------------------------------------------------: | :-----------: |
|  `width`  | `string` | Change width of template |  `undefined`   |
|  `height`  | `string` | Change height of template |  `undefined`   |
|  `theme`  | `string` | Change theme of template `light` or `dark` |  `undefined`   |
|  `stars`  | `string` | Change stars stock of template |  `undefined`   |
|  `businessUnitId`  | `string` | Set your business code  |  `undefined`  |
|  `templateId`  | `string` | Set your template ID  | `5419b6a8b0d04a076446a9ad`  |

<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

<!-- DOCS-IGNORE:end -->