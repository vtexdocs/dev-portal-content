---
title: "Update Antifraud Transactions (optional)"
slug: "updateantifraudtransactionsoptional"
excerpt: "Receives a new transaction antifraud data. This step is performed only if all payments are authorized."
hidden: true
createdAt: "2020-05-13T21:52:02.370Z"
updatedAt: "2020-06-01T17:34:59.982Z"
---
VTEX expects that your antifraud provider process this request and retrieves the process result, VTEX
order flow will follow your response status in order to cancel or approve the transaction

#### REQUEST HEADERS

---

<table>
  <tr>
        <td><strong>Header</strong></td>
        <td><strong>Value</strong></td>
    </tr>
    <tr>
        <td><code>X-PROVIDER-API-AppKey</code></td>
        <td><strong>{{X-PROVIDER-API-AppKey}}</strong></td>
    </tr>
    <tr>
        <td><code>X-PROVIDER-API-AppToken</code></td>
        <td><strong>{{X-PROVIDER-API-AppToken}}</strong></td>
    </tr>
    <tr>
        <td><code>Content-Typen</code></td>
        <td><strong>application/json</strong></td>
    </tr>
</table>

#### REQUEST BODY

---

<table>
    <tr>
        <td><code>reference</code></td>
        <td><strong>string max 255 chars</strong></td>
        <td>VTEX order reference key. The key of the order (from VTEX OMS system) related with this payment</td>
    </tr>
    <tr>
        <td><code>transactionId</code></td>
        <td><strong>string max 255 chars</strong></td>
        <td>VTEX transaction ID. The ID of the transaction related with this payment.</td>
    </tr>
    <tr>
        <td><code>value</code></td>
        <td><strong>decimal ex 20.95</strong></td>
        <td>VTEX transaction order value</td>
    </tr>
    <tr>
        <td><code>ip</code></td>
        <td><strong>string ip format</strong></td>
        <td>The original ip addres <strong>from browser</strong></td>
    </tr>
    <tr>
        <td><code>deviceFingerprint</code></td>
        <td><strong>string optional</strong></td>
        <td>Device Finger print generated by the provider. this is generated by using Google Tag Manager that the provider implements. This field is optional, is sent only if received. See <strong> Implement Device FingerPrint </strong></td>
    </tr>
        <tr>
        <td><code>store</code></td>
        <td><strong>string</strong></td>
        <td>VTEX has a main Name for the store. This unique name is often used in url to access VTEX configurations.</td>
    </tr>
    <tr>
        <td><code>miniCart</code></td>
        <td><strong>object optional</strong></td>
        <td>Mini cart data</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;⇒&nbsp;<code>buyer</code> <strong>object</strong></td>
        <td><strong>object</strong></td>
        <td>Buyer data</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>id</code></td>
        <td><strong>string</strong></td>
        <td>VTEX buyer ID. The unique identifier of the buyer</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>firstName</code></td>
        <td><strong>string max 255</strong></td>
        <td>First name of the buyer</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>lastName</code></td>
        <td><strong>string max 255</strong></td>
        <td>Last name of the buyer</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>document</code></td>
        <td><strong>string max 255</strong></td>
        <td>Document number of the buyer</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>documentType</code></td>
        <td><strong>string max 255</strong></td>
        <td>Type of document of the buyer. It depends on the coutry. See <strong> Document Types by Country </strong></td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>email</code></td>
        <td><strong>string max 255</strong></td>
        <td>Email of the buyer</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>phone</code></td>
        <td><strong>string max 255</strong></td>
        <td>Phone number of the buyer</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>address</code></td>
        <td><strong>object</strong></td>
        <td>buyer address</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>country</code></td>
        <td><strong>string</strong></td>
        <td>Buyer address country</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>street</code></td>
        <td><strong>string</strong></td>
        <td>Buyer address street</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>number</code></td>
        <td><strong>string</strong></td>
        <td>Buyer address number</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>complement</code></td>
        <td><strong>string</strong></td>
        <td>Buyer address complement</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>neighborhood</code></td>
        <td><strong>string</strong></td>
        <td>Buyer address neighborhood</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>postalCode</code></td>
        <td><strong>string</strong></td>
        <td>Buyer address postal code</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>city</code></td>
        <td><strong>string</strong></td>
        <td>Buyer address city</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>state</code></td>
        <td><strong>string</strong></td>
        <td>Buyer address state</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;⇒&nbsp;<code>shipping</code></td>
        <td><strong>object</strong></td>
        <td>Shipping data</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>value</code></td>
        <td><strong>decimal</strong></td>
        <td>Shipping value with two decimal places</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>estimatedDate</code></td>
        <td><strong>date</strong> 2028-06-15T21:15:07</td>
        <td>Estimated shipping date ISO 8601</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>address</code></td>
        <td><strong>object</strong></td>
        <td>Shipping address</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>country</code></td>
        <td><strong>string</strong></td>
        <td>Shipping address country</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>street</code></td>
        <td><strong>string</strong></td>
        <td>Shipping address street</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>number</code></td>
        <td><strong>string</strong></td>
        <td>Shipping address number</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>complement</code></td>
        <td><strong>string</strong></td>
        <td>Shipping address complement</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>neighborhood</code></td>
        <td><strong>string</strong></td>
        <td>Shipping address neighborhood</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>postalCode</code></td>
        <td><strong>string</strong></td>
        <td>Shipping address postal code</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>city</code></td>
        <td><strong>string</strong></td>
        <td>Shipping address city</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒⇒&nbsp;&nbsp;<code>state</code></td>
        <td><strong>string</strong></td>
        <td>Shipping address state</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;⇒&nbsp;<code>items</code></td>
        <td><strong>array of object</strong></td>
        <td>List of items data, in the cart</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>id</code></td>
        <td><strong>string</strong></td>
        <td>VTEX product ID. The ID of the item</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>name</code></td>
        <td><strong>string</strong></td>
        <td>Item name</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>price</code></td>
        <td><strong>decimal</strong></td>
        <td>Item price</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>quantity</code></td>
        <td><strong>integer</strong></td>
        <td>Quantity of this item in the cart</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>deliveryType</code></td>
        <td><strong>string max 255</strong></td>
        <td>Type of delivery configured by the store. ex. Normal</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>deliverySlaInMinutes</code></td>
        <td><strong>integer</strong></td>
        <td>Each item can have a separate shipping sla in minutes</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>categoryId</code></td>
        <td><strong>integer</strong></td>
        <td>Category ID for the Item. Configured by each store</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>categoryName</code></td>
        <td><strong>string max 255</strong></td>
        <td>Category name for the Item. Configured by each store</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>discount</code></td>
        <td><strong>decimal</strong></td>
        <td>Discount applied on item(s) two decimal places</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;⇒&nbsp;<code>taxValue</code></td>
        <td><strong>decimal</strong></td>
        <td>Total tax value</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;⇒&nbsp;<code>listRegistry</code></td>
        <td><strong>object optional</strong></td>
        <td>List registry indicates the existence of a list, like wishList, giftList or any other defined by the store</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>name</code></td>
        <td><strong>string max 255</strong></td>
        <td>List name defined by the store</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⇒⇒&nbsp;&nbsp;<code>deliveryToOwner</code></td>
        <td><strong>boolean</strong></td>
        <td>Flag to mark if the order will be delivered to list creator or not.</td>
    </tr>
    <tr>
        <td><code>payments</code></td>
        <td><strong>array of object</strong></td>
        <td>Describes the payments used for the current order</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;⇒&nbsp;<code>id</code></td>
        <td><strong>string max 255</strong></td>
        <td>Payment ID unique identifier in VTEX</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;⇒&nbsp;<code>method</code></td>
        <td><strong>string max 255</strong></td>
        <td>Payment method used for the buyer.  See <strong> Payment Methods</strong> </td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;⇒&nbsp;<code>name</code></td>
        <td><strong>string max 255</strong></td>
        <td>Payment name used for the buyer. This name could be the brand card or the VTEX payment method ex. Visa </td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;⇒&nbsp;<code>value</code></td>
        <td><strong>decimal</strong></td>
        <td>Payment value. Two decimal places</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;⇒&nbsp;<code>instalments</code></td>
        <td><strong>integer</strong></td>
        <td>Number of installments</td>
    </tr>
    <tr>
        <td><code>hook</code></td>
        <td><strong>string</strong></td>
        <td>URL to be called when the payment has it's status changed</td>
    </tr>
</table>

#### RESPONSE BODY

---

<table>
    <tr>
        <td><code>id</code></td>
        <td><strong>string</strong></td>
        <td>VTEX transaction ID. The ID of this transaction must be in the response.</td>
    </tr>
    <tr>
        <td><code>tid</code></td>
        <td><strong>string</strong></td>
        <td>Provider transaction ID. The ID of this transaction must be in the response. The antifraud provider MUST
            generates an unique transaction Id.</td>
    </tr>
    <tr>
        <td><code>status</code></td>
        <td><strong>string</strong></td>
        <td>Transaction status from provider. Must be one of the values: <strong>received</strong></td>
    </tr>
    <tr>
        <td><code>score</code></td>
        <td><strong>decimal</strong></td>
        <td>The value of the risk score. 100.00 as max value means total fraud</td>
    </tr>
    <tr>
        <td><code>AnalysisType</code></td>
        <td><strong>string</strong></td>
        <td>Analysis type. Valid values are <strong>authomatic</strong> or <strong>manual</strong></td>
    </tr>
    <tr>
        <td><code>responses</code>&nbsp;(optional)</td>
        <td><strong>dictionary or string, string</strong></td>
        <td>Key Value dictionary to add custom responses from  analysis</td>
    </tr>
    <tr>
        <td><code>tid</code></td>
        <td><strong>string</strong></td>
        <td>Transaction ID in the provider. This is the transaction identifier that the provider assigns</td>
    </tr>
    <tr>
        <td><code>code</code>&nbsp;(optional)</td>
        <td><strong>string</strong></td>
        <td>Error code returned from provider. <strong>Will be logged in transaction interactions log</strong></td>
    </tr>
    <tr>
        <td><code>message</code>&nbsp;(optional)</td>
        <td><strong>string</strong></td>
        <td>Error message returned from provider. <strong>Will be logged in transaction interactions log</strong></td>
    </tr>
</table>

#### REQUEST EXAMPLES AND THEIR RESPONSES

---
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST '{{protocol}}://{{accountName}}.{{domain}}/api/pub/antifraud-provider/analyze' \\\n--header 'Content-Type: application/json' \\\n--data-raw '{\n  \"id\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n  \"reference\": \"v32478982vtx-01\",\n  \"value\": 10,\n  \"ip\": \"10.0.0.1\",\n  \"deviceFingerprint\": \"12ade389087fexd\",\n  \"miniCart\": {\n    \"buyer\": {\n      \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n      \"firstName\": \"John\",\n      \"lastName\": \"Doe\",\n      \"document\": \"012.345.678-90\",\n      \"documentType\": \"CPF\",\n      \"email\": \"john@doe.com\",\n      \"phone\": \"+5521987654321\",\n      \"address\": {\n        \"country\": \"BRA\",\n        \"street\": \"Rua Praia de Botafogo\",\n        \"number\": \"518\",\n        \"complement\": \"2o. andar\",\n        \"neighborhood\": \"Botafogo\",\n        \"postalCode\": \"22250-040\",\n        \"city\": \"Rio de Janeiro\",\n        \"state\": \"RJ\"\n      }\n    },\n    \"shipping\": {\n      \"value\": 8.41,\n      \"estimatedDate\": \"2017-08-02T14:46:47\",\n      \"address\": {\n        \"country\": \"BRA\",\n        \"street\": \"Rua Praia de Botafogo\",\n        \"number\": \"518\",\n        \"complement\": \"2o. andar\",\n        \"neighborhood\": \"Botafogo\",\n        \"postalCode\": \"22250-040\",\n        \"city\": \"Rio de Janeiro\",\n        \"state\": \"RJ\"\n      }\n    },\n    \"items\": [\n      {\n        \"id\": \"132981\",\n        \"name\": \"Some useful product\",\n        \"price\": 20.51,\n        \"quantity\": 2,\n        \"deliveryType\": \"Normal\",\n        \"categoryId\": \"111\",\n        \"categoryName\": \"Electronica\",\n        \"discount\": 1.99\n      },\n      {\n        \"id\": \"123242\",\n        \"name\": \"Some useless product\",\n        \"price\": 21.98,\n        \"quantity\": 1,\n        \"deliveryType\": \"Normal\",\n        \"categoryId\": \"123\",\n        \"categoryName\": \"Lar\",\n        \"discount\": 1.01\n      }\n    ],\n    \"taxValue\": 5.58,\n    \"giftData\": {\n      \"description\": \"Minha lista Presente\"\n    }\n  },\n  \"payments\": [\n    {\n      \"id\": \"2D00FEBB5D7A43D598A99CFC43ADF158\",\n      \"method\": \"CreditCard\",\n      \"name\": \"Visa\",\n      \"value\": 63.98,\n      \"installments\": 3,\n      \"creditCard\": {\n        \"bin\": \"507860\",\n        \"lastDigits\": \"2798\",\n        \"holder\": \"John Doe\",\n        \"address\": {\n          \"country\": \"BRA\",\n          \"street\": \"Rua Praia de Botafogo\",\n          \"number\": \"518\",\n          \"complement\": \"2o. andar\",\n          \"neighborhood\": \"Botafogo\",\n          \"postalCode\": \"22250-040\",\n          \"city\": \"Rio de Janeiro\",\n          \"state\": \"RJ\"\n        }\n      }\n    },\n    {\n      \"id\": \"04D430E517B2494FBC3DF7721CCDACC7\",\n      \"method\": \"GiftCard\",\n      \"value\": 10.01,\n      \"installments\": 1\n    }\n  ],\n  \"callbackUrl\": \"https://vtexhook.notifyStatus.com\"\n}'",
      "language": "curl",
      "name": "Approve Antifraud Analysis Response"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"id\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n  \"status\": \"approved\",\n  \"fraudRiskPercentage\": 0,\n  \"analysisType\": \"authomatic\",\n  \"responses\": null\n}",
      "language": "curl",
      "name": "200 - OK"
    }
  ]
}
[/block]
