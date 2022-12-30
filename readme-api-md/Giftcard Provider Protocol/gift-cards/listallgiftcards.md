---
title: "List All GiftCards"
slug: "listallgiftcards"
excerpt: "Request a list of all giftcards available for a given client/cart(request)."
hidden: false
createdAt: "2019-12-25T15:13:56.093Z"
updatedAt: "2021-09-27T15:21:11.609Z"
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
        <td><code>cart</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>id</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>grandTotal</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>relationName</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>redemptionCode</code></td>
        <td>string</td>
        <td></td>
        <td>Minimum of six characters</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>discounts</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>shipping</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>taxes</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>items</code></td>
        <td>array</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>productId</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>id</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>refId</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>name</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>price</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>sellingPrice</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>sellerId</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>quantity</code></td>
        <td>integer</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>totalShippingDiscount</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>totalDiscount</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>components</code></td>
        <td>object (item)</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>sellerChain</code></td>
        <td>array of string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>payments</code></td>
        <td>array</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>paymentSystem</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>name</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>referenceValue</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>value</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>bin</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>lastDigits</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>sc</code></td>
        <td>string</td>
        <td></td>
        <td>Sales channel</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>itemsTotal</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>shippingData</code></td>
        <td>object</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>receiverName</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>postalCode</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>city</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>state</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>country</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>street</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>number</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>neighborhood</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>complement</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>reference</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>client</code></td>
        <td>object</td>
        <td>Yes</td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>id</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>&#x21B3; <code>email</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&#x21B3; <code>name</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&#x21B3; <code>ip</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&#x21B3; <code>userAgent</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&#x21B3; <code>document</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&#x21B3; <code>documentType</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&#x21B3; <code>corporateName</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&#x21B3; <code>tradeName</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>  
    <tr>
        <td>&#x21B3; <code>corporateDocument</code></td>
        <td>string</td>
        <td></td>
        <td></td>
    </tr>
</table>

##### RESPONSE

---

###### RESPONSE HEADERS

<table>
    <tr>
        <th>Name</th>
        <th>Mandatory</th>
        <th>Example</th>
        <th>Obs</th>
    </tr>
    <tr>
        <td><code>REST-Content-Range</code></td>
        <td>Yes</td>
        <td><code>resources 0-1/5</code></td>
        <td>Must follow the format <code>resources {from}-{to}/{total}</code></td>
    </tr>
</table>

###### RESPONSE BODY (array of)

GIFT CARD SUMMARY OBJECTS

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
        <td><code>provider</code></td>
        <td>string</td>
        <td>Yes</td>
        <td><code>provider</code> name</td>
    </tr>
    <tr>
        <td><code>balance</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>Gift card current <code>balance</code></td>
    </tr>
    <tr>
        <td><code>totalBalance</code></td>
        <td>number</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><code>relationName</code></td>
        <td>string</td>
        <td></td>
        <td>Represents the relationship between the client and the store</td>
    </tr>
    <tr>
        <td><code>caption</code></td>
        <td>string</td>
        <td></td>
        <td>The <code>caption</code> of the card</td>
    </tr>
    <tr>
        <td><code>groupName</code></td>
        <td>string</td>
        <td></td>
        <td></td>
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
