---
title: "Create GiftCard Transaction Settlement"
slug: "creategiftcardtransactionsettlement"
excerpt: "Creates a settlement transaction to a giftcard."
hidden: false
createdAt: "2019-12-25T15:13:56.093Z"
updatedAt: "2020-02-27T17:48:11.808Z"
---
##### REQUEST BODY

---


<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>value</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>value to be settled from transaction</td>
    </tr>   
    <tr>
        <td><code>requestId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>unique <code>requestId</code> to guarantee idempotency</td>
    </tr>
</table>

<br>

##### RESPONSE BODY

---

SETTLEMENT INFO

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>oid</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>operation id</td>
    </tr>   
    <tr>
        <td><code>value</code></td>
        <td>number</td>
        <td>Yes</td>
        <td><code>value</code> of the transaction</td>
    </tr>
    <tr>
        <tr>
        <td><code>date</code></td>
        <td>string</td>
        <td>Yes</td>
        <td><code>date</code> of the event</td>
    </tr>      
</table>