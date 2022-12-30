---
title: "List Payment Provider Manifest"
slug: "manifest-1"
excerpt: "Exposes provider manifest, a range of metadata settings, like payment methods, split configuration and custom fields."
hidden: false
createdAt: "2020-09-29T19:55:46.924Z"
updatedAt: "2022-09-28T14:44:08.935Z"
---
## Response body

---
<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>paymentMethods</code></td>
        <td>array of objects</td>
        <td>Yes</td>
        <td>Describes each payment method supported by payment provider and exposed its respective metadata.</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>name</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Payment method name.</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>allowsSplit</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Describes which transaction flow stage the connector should receive payment split data . Accepted values: <code>onAuthorize</code>, <code>onCapture</code>, <code>disabled</code>. Check more details on the <a href="https://developers.vtex.com/vtex-rest-api/docs/split-payouts-on-payment-provider-protocol" target="_blank">Split Payouts on the Payment Provider Protocol</a> article.</td>
    </tr>
    <tr>
        <td><code>customFields</code></td>
        <td>array of objects</td>
        <td>Yes</td>
        <td>Describes the customized fields supported by the connector.</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>name</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Custom field name.</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>type</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Custom field type. Accepted values: <code>text</code>, <code>select</code>.</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>options</code></td>
        <td>string</td>
        <td></td>
        <td>In case of <code>select</code> type, the possible params are <code>text</code> and <code>value</code>.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &#x21B3;<code>text</code></td>
        <td>object</td>
        <td></td>
        <td>Custom field description.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &#x21B3;<code>value</code></td>
        <td>string</td>
        <td></td>
        <td>Custom field value.</td>
    </tr>
    <tr>
        <td><code>autoSettleDelay</code></td>
        <td>number</td>
        <td></td>
        <td>Describes the allowed delay value for the auto settle capture. Accepted values: <code>minimum</code> and
            <code>maximum</code> in whole hours (decimals are not allowed). Check more details on the <a href="https://developers.vtex.com/vtex-rest-api/docs/custom-auto-capture-feature" target="_blank">Custom Auto Capture Feature</a> article.</td>
    </tr>
    <tr>
        <td>&#x21B3;<code>minimum</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Minimum amount of time to auto settle in hours.</td>
    </tr>
    <tr>
        <td>&#x21B3;<code>maximum</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Maximum amount of time to auto settle in hours.</td>
    </tr>
</table>

## Available payment methods

---

<table>
    <tr>
        <th>Payment Method</th>
        <th>Type</th>
        <th>Country</th>
    </tr>
    <tr>
        <td><code>Visa</code></td>
        <td>Credit Card</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Mastercard</code></td>
        <td>Credit Card</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>American Express</code></td>
        <td>Credit Card</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Discover</code></td>
        <td>Credit Card</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>JCB</code></td>
        <td>Credit Card</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Diners</code></td>
        <td>Credit Card</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Elo</code></td>
        <td>Credit Card</td>
        <td>Brazil</td>
    </tr>
    <tr>
        <td><code>Hipercard</code></td>
        <td>Credit Card</td>
        <td>Brazil</td>
    </tr>
    <tr>
        <td><code>Aura</code></td>
        <td>Credit Card</td>
        <td>Brazil</td>
    </tr>
    <tr>
        <td><code>Banricompras</code></td>
        <td>Credit Card</td>
        <td>Brazil</td>
    </tr>
    <tr>
        <td><code>Credz</code></td>
        <td>Credit Card</td>
        <td>Brazil</td>
    </tr>
    <tr>
        <td><code>VirtualDebitElo</code></td>
        <td>Debit Card</td>
        <td>Brazil</td>
    </tr>
    <tr>
        <td><code>Cabal</code></td>
        <td>Credit Card</td>
        <td>Argentina, Brazil, Uruguay, Paraguay</td>
    </tr>
    <tr>
        <td><code>Visa Electron</code></td>
        <td>Debit Card</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Maestro</code></td>
        <td>Debit Card</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Mastercard Debit</code></td>
        <td>Debit Card</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Cobranded</code></td>
        <td>Card</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Privatelabels</code></td>
        <td>Card</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Promissories</code></td>
        <td>Generic</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Cash</code></td>
        <td>Generic</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>BankInvoice</code></td>
        <td>Offline/Voucher</td>
        <td>Brazil (Boleto Bancário)</td>
    </tr>
    <tr>
        <td><code>Pix</code></td>
        <td>Online Transfer</td>
        <td>Brazil</td>
    </tr>
    <tr>
        <td><code>SPEI</code></td>
        <td>Online Transfer</td>
        <td>Mexico</td>
    </tr>
    <tr>
        <td><code>Safetypay</code></td>
        <td>Online Transfer</td>
        <td>Americas and Europe</td>
    </tr>
    <tr>
        <td><code>Bitcoin</code></td>
        <td>Cryptocurrency</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Venda Direta Credito</code></td>
        <td>Credit Card (Physical)</td>
        <td>Global</td>
    </tr>
    <tr>
        <td><code>Venda Direta Debito</code></td>
        <td>Debit Card (Physical)</td>
        <td>Global</td>
    </tr>
</table>

## Request examples and their responses

[block:code]
{
  "codes": [
    {
      "code": "curl --request GET \\\n  --url https://{{providerapiendpoint}}/manifest \\\n  --header 'accept: application/json'",
      "language": "curl",
      "name": "Success"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n\t\"paymentMethods\": [\n\t\t{\n\t\t\t\"name\": \"Visa\",\n\t\t\t\"allowsSplit\": \"onCapture\"\n\t\t},\n        { \n\t\t\t\"name\": \"Pix\",\n\t\t\t\"allowsSplit\": \"disabled\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"Mastercard\",\n\t\t\t\"allowsSplit\": \"onCapture\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"American Express\",\n\t\t\t\"allowsSplit\": \"onCapture\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"BankInvoice\",\n\t\t\t\"allowsSplit\": \"onAuthorize\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"Privatelabels\",\n\t\t\t\"allowsSplit\": \"disabled\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"Promissories\",\n\t\t\t\"allowsSplit\": \"disabled\"\n\t\t}\n\t],\n\t\"customFields\": [\n\t\t{\n\t\t\t\"name\": \"Merchant's custom field\",\n\t\t\t\"type\": \"text\"\n\t\t},\n\t\t{\n\t\t\t\"name\": \"Merchant's custom select field\",\n\t\t\t\"type\": \"select\",\n\t\t\t\"options\": [\n\t\t\t\t{\n\t\t\t\t\t\"text\": \"Field option 1\",\n\t\t\t\t\t\"value\": \"1\",\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\t\"text\": \"Field option 2\",\n\t\t\t\t\t\"value\": \"2\",\n\t\t\t\t},\n\t\t\t\t{\n\t\t\t\t\t\"text\": \"Field option 3\",\n\t\t\t\t\t\"value\": \"3\",\n\t\t\t\t}\n\t\t\t]\n\t\t}\n\t]\n    \"autoSettleDelay\": {\n            \"minimum\": \"0\",\n            \"maximum\": \"720\"\n  }\n}",
      "language": "curl",
      "name": "200 - OK"
    }
  ]
}
[/block]
