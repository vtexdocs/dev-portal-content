---
title: "Mutations"
---

## Cart

<table>
<thead>
<tr>
<th align="left">Field</th>
<th align="right">Argument</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" valign="top"><strong>validateCart</strong></td>
<td valign="top"><a href="#storecart">StoreCart</a></td>
<td>

Checks for changes between the cart presented in the UI and the cart stored in the ecommerce platform. If changes are detected, it returns the cart stored on the platform. Otherwise, it returns `null`.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">cart</td>
<td valign="top"><a href="#istorecart">IStoreCart</a>!</td>
<td>

Shopping cart input.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">session</td>
<td valign="top"><a href="#istoresession">IStoreSession</a></td>
<td>

Web session identifier.

</td>
</tr>
</thead>
</table>

## Session

<table>
<thead>
<tr>
<tr>
<td colspan="2" valign="top"><strong>validateSession</strong></td>
<td valign="top"><a href="#storesession">StoreSession</a></td>
<td>

Updates a web session with the specified values.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">session</td>
<td valign="top"><a href="#istoresession">IStoreSession</a>!</td>
<td>

Web session identifier.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">search</td>
<td valign="top"><a href="#string">String</a>!</td>
<td></td>
</tr>
<tr>
<td colspan="2" valign="top"><strong>subscribeToNewsletter</strong></td>
<td valign="top"><a href="#personnewsletter">PersonNewsletter</a></td>
<td>

Subscribes a new person to the newsletter list.

</td>
</tr>
<tr>
<td colspan="2" align="right" valign="top">data</td>
<td valign="top"><a href="#ipersonnewsletter">IPersonNewsletter</a>!</td>
<td></td>
</tr>
</tbody>
</table>
