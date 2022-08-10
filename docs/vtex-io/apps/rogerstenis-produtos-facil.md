---
title: "Pharma Orders Admin"
slug: "rogerstenis-produtos-facil"
excerpt: "rogerstenis.produtos-facil@0.0.1"
hidden: true
createdAt: "2022-07-22T21:52:36.895Z"
updatedAt: "2022-07-22T21:52:36.895Z"
---
The Pharma Orders Admin app will allow you to manage your Pharma Orders. You can:

- See the orders with products of the category Medicamentos.
- See the prescription of the orders.
- See products of the orders
- Aprove, Cancel and confirm the Orders.

![Media Placeholder](https://user-images.githubusercontent.com/55905671/139487826-4fa4dcea-101e-486c-a106-acc8c3abd36a.gif)

---

## Configure

1. Using your terminal and the [VTEX IO Toolbelt](https://vtex.io/docs/recipes/development/vtex-io-cli-installment-and-command-reference), log into the desired VTEX account.
2. Run `vtex install vtexarg.pharma-orders-admin` on the account you're working on.

### Create Entity and Schema

Do a `[PUT]` on `https://:account.vtexcommercestable.com.br/api/dataentities/pharmaOrders/schemas/pharma-orders`

`HEADER: VtexIdClientAutCookie`

`BODY:`

```json
{
  "properties": {
    "orderId": {
      "type": "string",
      "maxLength": 50,
      "title": "orderId"
    },
    "status": {
      "type": "string",
      "maxLength": 50,
      "title": "status"
    },
    "invoiceNumber": {
      "type": "string",
      "maxLength": 50,
      "title": "invoiceNumber"
    }
  },
  "required": ["orderId", "status", "invoiceNumber"],
  "v-indexed": ["orderId", "status", "invoiceNumber"],
  "v-security": {
    "publicJsonSchema": true,
    "allowGetAll": false,
    "publicRead": ["orderId", "status", "invoiceNumber"],
    "publicWrite": ["orderId", "status", "invoiceNumber"],
    "publicFilter": ["orderId", "status", "invoiceNumber"]
  }
}
```

### App Setup

1. If you will work in a workspace, you need to redirect the orders flow to the workspace where you are working, you can do it here:
   `https://:account.myvtex.com/admin/apps/vtex.orders-broadcast/setup`
   ![image](https://user-images.githubusercontent.com/55905671/139486880-779613dc-8c6d-4420-b89c-81b17a751770.png)

2. You will need to add the `Id` of the `Category Medicamentos`, this is important because the app will only show the orders with products of this category.
   `https://:account.myvtex.com/admin/apps/vtexarg.pharma-orders-admin/setup`
   ![image](https://user-images.githubusercontent.com/55905671/139487357-e13ad3ac-59ba-4627-abbb-f632556a2d2e.png)