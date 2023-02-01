---
title: "Get price association by ID"
slug: "getpricerulebyid"
excerpt: "Retrieves price association for a shopping scenario by its ID"
hidden: true
createdAt: "2021-02-02T13:50:02.022Z"
updatedAt: "2021-02-03T20:48:37.681Z"
---
## Request Headers

---
<table>
<tr>
<td><strong>Header</strong></td>
<td><strong>Value</strong></td>
</tr>
<tr>
<td><code>Content-Type</code></td>
<td><strong>application/json</strong></td>
</tr>
<tr>
<td><code>Accept</code></td>
<td><strong>application/json</strong></td>
</tr>
</table>

<br>

## Response Body

---

<table>
<tr>
<th>Name</th>
<th>Type</th>
<th>Mandatory</th>
<th>Description</th>
</tr>
<tr>
<td><code>id</code></td>
<td>string</td>
<td>Yes</td>
<td>Price Association unique identifier</td>
</tr>
<tr>
<td><code>resell</code></td>
<td>string</td>
<td>Yes</td>
<td>Order type</td>
</tr>
<tr>
<td><code>pricetable</code></td>
<td>string</td>
<td>Yes</td>
<td>Name of the Price Table associated with the scenario</td>
</tr>
<tr>
<td><code>email</code></td>
<td>string</td>
<td>Yes</td>
<td>User's email</td>
</tr>
<tr>
<td><code>state</code></td>
<td>string</td>
<td>Yes</td>
<td>Delivery location</td>
</tr>
</table>

## Request examples and their responses

```json
{
  "id":1,
  "orderType": "Resale",
  "state": "ES",
  "pricetable": "pricetable1",
  "email": "email@email.com"
}
```
