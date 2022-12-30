---
title: "Create GiftCard Transaction"
slug: "creategiftcardtransaction-2"
excerpt: "Creates a transaction to a giftcard."
hidden: false
createdAt: "2019-12-25T15:13:56.093Z"
updatedAt: "2020-02-27T17:48:11.271Z"
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
        <td><code>operation</code></td>
        <td>string</td>
        <td></td>
        <td>Possible values: {"Credit","Debit"}</td>
    </tr>
    <tr>
        <td><code>value</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>description</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>redemptionToken</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>redemptionCode</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>requestId</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>orderInfo</code></td>
        <td>object</td>
        <td></td>
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
        <td>See List all giftcards request for <code>cart</code> object reference</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>clientProfile</code></td>
        <td>object</td>
        <td></td>
        <td>See List all giftcards request for <code>clientProfile (client)</code> object reference</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>shipping</code></td>
        <td>string</td>
        <td></td>
        <td>See List all giftcards request for <code>shipping</code> object reference</td>
    </tr>
    <tr>
        <td><code>paymentRelatedSellerInfo</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>seller</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>sellerOrderId</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>sellerSequence</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>value</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
</table>

##### RESPONSE BODY

---

TRANSACTION SUMMARY

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>cardId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Gift card <code>cardId</code></td>
    </tr>
    <tr>
        <td><code>id</code></td>
        <td>string</td>
        <td>Yes</td>
        <td><code>id</code> of the transaction</td>
    </tr>
    <tr>
        <td><code>_self</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>href</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Resource URL (see example)</td>
    </tr>
</table>
