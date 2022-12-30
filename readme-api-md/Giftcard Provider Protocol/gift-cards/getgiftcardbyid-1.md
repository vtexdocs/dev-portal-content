---
title: "Get GiftCard by ID"
slug: "getgiftcardbyid-1"
excerpt: "Returns a specific giftcard with details."
hidden: false
createdAt: "2019-12-25T15:13:56.093Z"
updatedAt: "2021-04-03T23:08:00.862Z"
---
Returns a specific giftcard with details.

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
        <td><code>id</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Gift card <code>id</code></td>
    </tr>
    <tr>
        <td><code>redemptionToken</code></td>
        <td>string</td>
        <td>No</td>
        <td>Gift card <code>redemptionToken</code></td>
    </tr>
    <tr>
        <td><code>redemptionCode</code></td>
        <td>string</td>
        <td>No</td>
        <td>Gift card <code>redemptionCode</code></td>
    </tr>
    <tr>
        <td><code>balance</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>Gift card current <code>balance</code></td>
    </tr>
    <tr>
        <td><code>relationName</code></td>
        <td>string</td>
        <td></td>
        <td>Represents the relationship between the client and the store</td>
    </tr>
    <tr>
        <td><code>emissionDate</code></td>
        <td>string</td>
        <td>Yes</td>
        <td><strong>Important: </strong>It must be in the format <code>YYYY-MM-DDThh:mm:ss.fff</code></td>
    </tr>
    <tr>
        <td><code>expiringDate</code></td>
        <td>string</td>
        <td>Yes</td>
        <td><strong>Important: </strong>It must be in the format <code>YYYY-MM-DDThh:mm:ss.fff</code></td>
    </tr>
    <tr>
        <td><code>caption</code></td>
        <td>string</td>
        <td></td>
        <td>The <code>caption</code> of the card</td>
    </tr>
    <tr>
        <td><code>provider</code></td>
        <td>string</td>
        <td>Yes</td>
        <td><code>provider</code> name</td>
    </tr>
    <tr>
        <td><code>groupName</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>transaction</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>href</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Resource URL</td>
    </tr>
</table>