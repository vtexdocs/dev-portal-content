---
title: "Policies from License Manager"
slug: "vtex-io-documentation-policies-from-license-manager"
hidden: false
createdAt: "2024-03-20T11:51:00.000Z"
updatedAt: "2024-03-20T11:51:00.000Z"
excerpt: "Discover the policies a VTEX IO app can use from License Manager resources."
---
In order for a  VTEX IO app to access external resources, it requires authorization through policies declared in its [`manifest.json` file](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest). One type of external resource available is the [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3), which can be authorized to access by declaring the resource’s **Key** in the `policies` list of the app. For instance, by adding `Sku.aspx` to the `policies` list,  your app gains permission to read SKUs from the Catalog.

```json
{
  "$schema": "https://raw.githubusercontent.com/vtex/node-vtex-api/master/gen/manifest.schema",
  "name": "app-name",
  "vendor": "vendor",
  "version": "0.0.0",
  "title": "VTEX IO App",
  "description": "",
  "dependencies": {},
  "builders": {...},
  "scripts": {...},
  "policies": [
    {
      "name": "Sku.aspx"
    },
    {
      "name": "outbound-access",
      "attrs": {
        "host": "{{account}}.vtexcommercestable.com.br",
        "path": "/arquivos/favicon.ico"
      }
    }
  ]
}
```

>ℹ Note that License Manager policies are declared in a different way than outbound-access policies. While outbound-access policies require the explicit host and path for each resource, License Manager policies operate based on predefined roles.

Below is a table listing the role-based VTEX IO policies for the License Manager resources. The table indicates which [Client](https://developers.vtex.com/docs/guides/vtex-io-documentation-clients) the policy is associated with.

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Key</th>
      <th>Description</th>
      <th>Client</th>
      <th>Resources</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Product management</td>
      <td><code>ProdutoForm.aspx</code></td>
      <td>View the registration screen and product change.</td>
      <td><code>catalog</code></td>
      <td>
        <ul>
          <li><code>{{account}}.vtexcommercestable.com.br/api/catalog_system/pvt/products/*</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Product and SKU Management</td>
      <td><code>ManterFormularioProdutoSku</code></td>
      <td>Change and inclusion of product and SKU.</td>
      <td><code>catalog</code></td>
      <td>
        <ul>
          <li><code>{{account}}.vtexcommercestable.com.br/api/catalog_system/pvt/products/*</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Brands</td>
      <td><code>Marca.aspx</code></td>
      <td>List all registered brands.</td>
      <td><code>catalog</code></td>
      <td>
        <ul>
          <li><code>{{account}}.vtexcommercestable.com.br/api/catalog_system/pvt/brand/list</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>SKUs</td>
      <td><code>Sku.aspx</code></td>
      <td>Lists all registered SKUs.</td>
      <td><code>catalog</code></td>
      <td>
        <ul>
          <li><code>{{account}}.vtexcommercestable.com.br/api/catalog_system/pvt/sku/*</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Orders Full Access</td>
      <td><code>AcessaTodosPedidos</code></td>
      <td>Reading and writing for all requests via Checkout API. It does not allow access to requests for the flow of
        the order management module.</td>
      <td><code>checkout</code></td>
      <td>
        <ul>
          <li><code>{{account}}.vtexcommercestable.com.br/api/oms/pvt/orders/*</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Order Cancellation</td>
      <td><code>CancelaPedidos</code></td>
      <td>Cancel orders.</td>
      <td><code>checkout</code></td>
      <td>
        <ul>
          <li><code>/api/oms/pvt/orders/{{orderId}}/cancel</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Save OrderForm Configuration</td>
      <td><code>SaveOrderFormConfiguration</code></td>
      <td>Save the configuration of shopping carts.</td>
      <td><code>checkout</code></td>
      <td>
        <ul>
          <li><code>/api/checkout/pvt/configuration/orderform</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Read Shopping Cart</td>
      <td><code>GetOrderForm</code></td>
      <td>Reading and listing all shopping carts. It does not allow access to non-masked cart data.</td>
      <td><code>checkout</code></td>
      <td>
        <ul>
          <li><code>/api/checkout/pub/orderform/{{orderFormId}}</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Get account by identifier</td>
      <td><code>Get_Account_By_Identifier</code></td>
      <td>Consultation that returns accounts for the identifier, which may be the account ID, host, or name of the
        account application.</td>
      <td><code>licenseManager</code></td>
      <td>
        <ul>
          <li><code>/api/license-manager/account</code></li>
          <li><code>/api/license-manager/pvt/accounts/\*</code></li>
          <li><code>/api/pvt/accounts/\*</code></li>
          <li><code>/api/site/pvt/accounts/\*</code></li>
          <li><code>/api/license-manager/site/pvt/accounts/\*</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Master Data administrator</td>
      <td><code>ADMIN_DS</code></td>
      <td>Manage Master Data.</td>
      <td><code>masterData</code></td>
      <td>
        <ul>
          <li><code>{{account}}.vtexcommercestable.com.br/*</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Vbase Read Only</td>
      <td><code>vbase-read-only</code></td>
      <td>Read-only access to VBase.</td>
      <td><code>vbase</code></td>
      <td>
        <ul>
          <li><code>/buckets/*</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Vbase Read Write</td>
      <td><code>vbase-read-write</code></td>
      <td>Read and write access to VBase.</td>
      <td><code>vbase</code></td>
      <td>
        <ul>
          <li><code>/buckets/*</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>List Orders</td>
      <td><code>ListOrders</code></td>
      <td>List all orders from the given account.</td>
      <td><code>OMS</code></td>
      <td>
        <ul>
          <li><code>/api/oms/pvt/orders</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

>ℹ If you know about a policy that needs to be described in the table and wants it to be documented, open a request using our [feedback form](https://docs.google.com/forms/d/e/1FAIpQLSfmnotPvPjw-SjiE7lt2Nt3RQgNUe10ixXZmuO2v9enOJReoQ/viewform).
