---
title: "Get GiftCard Transaction by ID"
slug: "getgiftcardtransactionbyid-2"
excerpt: "Returns a specific giftcard transaction."
hidden: false
createdAt: "2019-12-25T15:13:56.093Z"
updatedAt: "2020-06-17T23:33:17.568Z"
---
##### RESPONSE BODY

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
        <td></td>
    </tr>
    <tr>
        <td><code>description</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>redemptionCode</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>date</code></td>
        <td>dateTime</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>requestId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td><code>orderInfo</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>orderId</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>sequence</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>cart</code></td>
        <td>object</td>
        <td></td>
        <td>See <code>List all GiftCards</code> request for <code>cart</code> object reference</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>clientProfile</code></td>
        <td>object</td>
        <td></td>
        <td>See <code>List all GiftCards</code> request for <code>client</code> object reference</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>shipping</code></td>
        <td>string</td>
        <td></td>
        <td>See <code>List all GiftCards</code> request for <code>shipping</code> object reference</td>
    </tr>
    <tr>
        <td><code>settlement</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>_href</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>cancellation</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>_href</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>authorization</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>_href</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>operation</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Possible values: {"Credit","Debit"}</td>
    </tr>
</table>
