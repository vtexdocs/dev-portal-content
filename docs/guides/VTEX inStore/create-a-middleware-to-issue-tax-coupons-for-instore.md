---
title: "Create a middleware to issue tax coupons for inStore"
slug: "create-a-middleware-to-issue-tax-coupons-for-instore"
hidden: true
createdAt: "2022-06-06T14:01:04.901Z"
updatedAt: "2022-06-06T14:06:38.857Z"
---
A middleware is a software that acts as a bridge connecting the module that issues the tax coupon with the inStore system. It is usually installed in the store's network and needs to contain the following endpoints to receive the information sent by VTEX servers:



* Endpoint to receive the orders from VTEX to invoice them.
* Endpoint to issue the return invoice.

These endpoints must be sent to [our Support](https://support.vtex.com/hc/en-us/requests) for the inStore team to configure them in the store that wants to install the middleware.


### Billing endpoints

The two billing endpoints required will either be on a machine with a fixed IP in the store itself or on an open `HTTPS` endpoint on the Internet.

When implementing the billing endpoint, ensure that it can receive requests for the `POST` method from VTEX. The body sent by VTEX will be equivalent to the [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder) response body, with the addition of the following information:

**Request body example** 


```json
{
  …
  "items": [...],
  "id": "1234568358",
  "type": "Input"
}
```



<table>
  <tr>
   <td><strong>Attribute</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td><code>type</code>
   </td>
   <td>Defines the type of the endpoint, if it is a billing ("<code>Output"</code>) or if it is a return (<code>"Input"</code>).
   </td>
  </tr>
  <tr>
   <td><code>items</code>
   </td>
   <td>If <code>"type": "Input"</code>, it shows which products were returned.
   </td>
  </tr>
  <tr>
   <td><code>id</code>
   </td>
   <td>If <code>"type": "Input"</code>, it indicates whether the return was successful.
   </td>
  </tr>
</table>


After this step, you must invoice the order with the _Receita Federal_ (brazilian equivalent of  IRS) using the response from the `POST` endpoint and send the tax coupon file and the coupon number within a JSON to VTEX in the following format:


```json
 {
    "invoiceNumber": "123456789",
    "invoiceUrl": "https://www.taxcoupon.com",
    "printUrl": "https://www.taxcoupon.com",
    "shouldPrintInvoice": true
 }
```



<table>
  <tr>
   <td><strong>Attribute</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>
<ul>

<li><code>invoiceNumber</code>
</li>
</ul>
   </td>
   <td>Tax coupon number. Mandatory field.
   </td>
  </tr>
  <tr>
   <td>
<ul>

<li><code>invoiceUrl</code>
</li>
</ul>
   </td>
   <td>Link following the <code>'https://'</code> protocol that identifies the tax coupon. It can be used to print the tax coupon if the field <code>printUrl</code> is not sent. Mandatory field.
   </td>
  </tr>
  <tr>
   <td>
<ul>

<li><code>printUrl</code>
</li>
</ul>
   </td>
   <td><code>'https://'</code> link or file path with the tax coupon that will be printed. If this field is sent empty the field <code>invoiceUrl</code> will be printed instead. 
   </td>
  </tr>
  <tr>
   <td>
<ul>

<li><code>shouldPrintInvoice</code>
</li>
</ul>
   </td>
   <td>Indicates to the inStore that it should print the file. This is a boolean an the default value is <code>true</code>.
   </td>
  </tr>
</table>


Once receiving the response for both billing and return scenarios, inStore saves the tax invoice in VTEX’s OMS and changes the order's status to the **Invoiced** status. 

When returning an error code - as ``4xx`` or ``5xx`` - together with the previous JSON (both for billing and return), inStore understands that there was a billing error and warns the seller to take appropriate action.


```json
{
  "message": "Contains an explanation of the invoice error"
}
```



#### Data required to issue the tax coupon

To issue the tax coupon with name and value of the product, type and receipt of card payments, NCM and ICMS of each product, customer's email and name, you must get the following information from the [Get order](https://developers.vtex.com/vtex-rest-api/reference/getorder) response body:



* ``items``
* ``paymentData.transactions.payments``
* ``customData.customApps.fields``
* ``TaxCode``
* ``clientProfileData``


[block:callout]
{
  "type": "info",
  "body": "It is possible that the customer makes the purchase anonymously. To confirm this, simply check if the `clientProfileData.firstName` field has the `isAnonymous` value in the order JSON. In this case, you cannot send the tax coupon by email."
}
[/block]
### inStore customization

To customize the inStore devices to send requests to the correct IP, you need to [edit inStore's JavaScript file](https://developers.vtex.com/vtex-rest-api/docs/how-to-customize-instore#edit-the-javascript-file).

At the beginning of the file, insert the following code by replacing the `IP_GLOBAL` variable's value with the printer IP:


```javascript
var IP_GLOBAL = 'XX.Y.ZZ.AA'

window.ORDER_PLACED_HOOK_GLOBAL = {
  url: 'http://' + IP_GLOBAL + ':6061/invoice-order',
  cancelUrl: 'http://' + IP_GLOBAL + ':6061/invoice-order',
  invoiceEndpoints: {
    Output: 'http://' + IP_GLOBAL + ':6060/api/vtex/order',
    Input: 'http://' + IP_GLOBAL + ':6060/api/vtex/cancela',
  },
}
```


Add a reference of the above configuration in the ``orderPlacedHook`` variable:


```javascript
window.INSTORE_CONFIG = {
  payments: window.PAYMENTS_FILTER_GLOBAL,
  orderPlacedHook: window.ORDER_PLACED_HOOK_GLOBAL,
}
```


With this customization, inStore will request the printing of the tax coupon with the integrated biller. 


### Device pairing

inStore does not require a fixed IP for the invoice, allowing inStore devices to communicate between themselves through pairing performed in [the inStore menu Configure device option](https://help.vtex.com/en/tracks/instore-using-the-app--4BYzQIwyOHvnmnCYQgLzdr/5UeqJA3sHp5goJacvHwPoS).

With this option to configure inStore billing, perform the same IP configuration, but the ``IP_GLOBAL`` value will always take precedence:


```javascript
 var IP_GLOBAL = 'localhost'
```


This means that it will always communicate with the biller through the same machine since the dispatch would be done between inStore devices. Check a [complete JSON example of a order](https://instore.vteximg.com.br/assets/vtex.instore/files/invoice-payload___ee4347c3d91fecf1da6a85a12d519494.json).