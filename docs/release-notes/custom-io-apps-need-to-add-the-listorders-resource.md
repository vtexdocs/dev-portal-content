---
slug: "custom-io-apps-need-to-add-the-listorders-resource"
title: "Custom IO apps need to add the ListOrders resource"
createdAt: 2023-02-09T14:51:46.000Z
hidden: false
type: "improved"
excerpt: Starting March 15th, 2023, accounts with custom IO apps will need the ListOrders resource on the manifest.json file to be able to call list orders requests.
---

Recently, VTEX created the `ListOrders` [License Manager resource](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3), which gives permission to list orders from a given account. Before, the `OMSViewer` allowed both viewing and listing orders, but now each resource grants permission for a single action:

- **OMSViewer:** view orders.
- **ListOrders:** list orders.

The new `ListOrders` resource was automatically added to all authentications ([roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) and [appkeys](https://developers.vtex.com/docs/guides/getting-started-authentication)) that use the `OMSViewer` resource. In those cases, nothing needs to be done.

However, to work as before, in addition to the previous `OMSViewer` resource, accounts with custom IO apps need to add the `ListOrders` resource on their [manifest.json](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest) file. That way, they will be able to view orders and make [List Orders](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders) requests.

This change will be valid for all accounts starting on March 15th, 2023. If you need to make the update, go to the `manifest.json` file of your app project and add the `ListOrders` resource to the [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies) field, as shown in the example below:

```json
{ 
  "policies": [
    {
    "name": "OMSViewer"
    },
    {
    "name": "ListOrders"
    }
  ]
}
```
