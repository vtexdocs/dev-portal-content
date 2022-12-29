---
title: "List Payment Methods"
slug: "paymentmethods"
excerpt: "Return all payment methods that your provider can handle. Please make sure you are returning only supported payment methods as listed below."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2022-07-15T14:55:38.053Z"
---
**Important:** this endpoint must be public, and should not require `X-VTEX-API-AppKey`/`X-VTEX-API-AppToken` headers.

<br>

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
        <td>array of strings</td>
        <td>Yes</td>
        <td>List of each payment method implemented</td>
    </tr>
</table>

<br>

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
</table>

<table>
    <tr>
        <th>Branded/Local Payment Methods</th>
    </tr>
    <tr>
        <td><code>PinCash</code>, <code>LevPay</code>, <code>PayMee</code>, <code>PicPay</code>, <code>Losango</code>, <code>PagoLivre</code>, <code>Pagomio</code>, <code>PagSeguro</code>, <code>PlaceToPay</code></td>
    </tr>
</table>

## Request examples and their responses
[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{providerApiEndpoint}}/payment-methods' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json'",
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
      "code": "{\n  \"paymentMethods\": [\n    \"Visa\",\n    \"Mastercard\",\n    \"Pix\",\n    \"American Express\",\n    \"BankInvoice\",\n    \"Privatelabels\",\n    \"Promissories\"\n  ]\n}",
      "language": "curl",
      "name": "200 - OK"
    }
  ]
}
[/block]