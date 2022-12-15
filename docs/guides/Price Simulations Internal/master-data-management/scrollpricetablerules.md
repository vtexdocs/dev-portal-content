---
title: 'Scroll Custom Price'
slug: 'scrollpricetablerules'
excerpt: 'Retrieves general information about a Custom Price'
hidden: true
createdAt: '2021-02-02T13:50:02.015Z'
updatedAt: '2021-02-03T20:45:46.580Z'
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

## Request Body

---

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>_schema</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Custom Price name</td>
    </tr>
    <tr>
        <td><code>_fields</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Criteria of the Custom Price you want to be retrieved</td>
    </tr>
    <tr>
        <td><code>_size</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Quantity of the retrieved information</td>
    </tr>
</table>

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

---

[block:code]
{
"codes": [
{
"code": "[\n {\n \"id\": \"65b1fc90\",\n \"resell\": null,\n \"pricetable\": \"example4\",\n \"email\": null,\n \"state\": \"RJ\"\n },\n {\n \"id\": \"d5c3cd9f\",\n \"resell\": null,\n \"pricetable\": \"for-email\",\n \"email\": \"api.example@vtex.com.br\",\n \"state\": null\n }\n]",
"language": "curl",
"name": "200 - OK"
}
]
}
[/block]
