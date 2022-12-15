---
title: "Create Payment"
slug: "createpayment"
excerpt: "Creates a new payment and/or initiates the payment flow."
hidden: false
createdAt: "2019-12-30T03:21:07.203Z"
updatedAt: "2022-10-07T21:08:21.934Z"
---
For credit/debit card payments, or any sync payments, you're expected to execute the authorization.

For bank issued invoice, redirect, or any async payments, you're expected to return the required information to the customer.

The same request, for the same `paymentId`, can be executed several times, so you must handle it in a way to avoid recreating the payment, but returning the most updated status instead.

<br>

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
        <td><code>reference</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Merchant's order reference provided by VTEX Checkout.</td>
    </tr>
    <tr>
        <td><code>orderId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Merchant's order identifier provided by VTEX Checkout (also called order group).</td>
    </tr>
  <tr>
        <td><code>shopperInteraction</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Indicates which system the buyer interacted with (examples: e-commerce, instore, subscription).</td>
    </tr>
    <tr>
        <td><code>transactionId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX transaction ID related to this payment.</td>
    </tr>
    <tr>
        <td><code>paymentId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX payment ID that can be used as <b>unique identifier</b>.</td>
    </tr>
    <tr>
        <td><code>paymentMethod</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The payment method chosen for this payment. It must be one of the available payment methods offered by the provider, which can be obtained from the <a href="https://developers.vtex.com/vtex-rest-api/reference/paymentmethods" target="_blank">List Payment Methods endpoint</a> or <a href="https://developers.vtex.com/vtex-rest-api/reference/manifest-1" target="_blank">List Payment Provider Manifest endpoint</a>.</td>
    </tr>
    <tr>
        <td><code>paymentMethodCustomCode</code></td>
        <td>string</td>
        <td></td>
        <td>Configurable for <code>Cobranded</code> and <code>Privatelabels</code> payment methods.</td>
    </tr>
<tr>
        <td><code>verificationOnly</code></td>
        <td>boolean</td>
        <td></td>
        <td>Indicates whether this payment is just to validate the buyer's payment method information (for instance, validate the credit card information).</td>
    </tr>
    <tr>
        <td><code>merchantName</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX merchant name that will receive the payment.</td>
    </tr>
    <tr>
        <td><code>value</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td>Value amount of the payment.</td>
    </tr>
    <tr>
        <td><code>currency</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Currency code (ISO 4217 alpha-3).</td>
    </tr>
    <tr>
        <td><code>installments</code></td>
        <td>integer</td>
        <td></td>
        <td>Number of installments.</td>
    </tr>
<tr>
        <td><code>installmentsValue</code></td>
        <td>number</td>
        <td></td>
        <td>The value of each installment.</td>
    </tr>
<tr>
        <td><code>installmentsInterestRate</code></td>
        <td>number</td>
        <td></td>
        <td>The interest rate.</td>
    </tr>
    <tr>
        <td><code>deviceFingerprint</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>A hash that represents the device used to initiate the payment.</td>
    </tr>
   <tr>
        <td><code>ipAddress</code></td>
        <td>string</td>
        <td></td>
        <td>The IP Address of the buyer.</td>
    </tr>
    <tr>
        <td><code>card</code></td>
        <td>object</td>
        <td></td>
        <td>Card used in the payment. This parameter is required only with card payment methods (credit, debit or co-branded).</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>holder</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Card holder name (this field is <code>null</code> in case the provider uses the Secure Proxy).</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>number</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Card number (this field is <code>null</code> in case the provider uses the Secure Proxy).</td>
    </tr>
 <tr>
  <tr>
        <td>&#x21B3; <code>csc</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Card security code (this field is null in case the provider uses the Secure Proxy).</td>
    </tr>
        <td>&#x21B3; <code>holderToken</code></td>
        <td>string</td>
        <td></td>
        <td>A token representing the card holder (this field is absent in case the provider does not use the Secure Proxy).</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>bin</code></td>
        <td>string</td>
        <td></td>
        <td>First 6 digits of the card number (this field is absent in case the provider does not use the Secure Proxy).</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>numberToken</code></td>
        <td>string</td>
        <td></td>
        <td>A token representing the card security code (this field is absent in case the provider does not use the Secure Proxy).</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>numberLength</code></td>
        <td>number</td>
        <td></td>
        <td>The number of digits in the card's number (this field is absent in case the provider does not use the Secure Proxy).</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>cscToken</code></td>
        <td>string</td>
        <td></td>
        <td>The number of digits in the card's number (this field is absent in case the provider does not use the Secure Proxy).</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>cscLength</code></td>
        <td>number</td>
        <td></td>
        <td>The number of characters in the Card Security Code (this field is absent in case the provider does not use the Secure Proxy).</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>expiration</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>An object representing the card's expiration information.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>month</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Card expiration month (2-digits).</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>year</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Card expiration year (4-digits).</td>
    </tr>
  <tr>
        <td>&#x21B3; <code>document</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Card holder's document.</td>
    </tr>
    <tr>
        <td><code>miniCart</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>Object containing information about the shopper's cart and its products.</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>buyer</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>Object containing information about the buyer.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>id</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>A unique key to this Payment's buyer.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>firstName</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Buyer's first name.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>lastName</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Buyer's last name.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>document</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Buyer's document number.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>documentType</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Buyer's document type.</td>
    </tr>
 <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>corporateName</code></td>
        <td>string</td>
        <td></td>
        <td>Buyer's corporate name. This field is required if <code>isCorporate</code> is <code>true</code>.</td>
    </tr>
 <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>tradeName</code></td>
        <td>string</td>
        <td></td>
        <td>Buyer's trade name. This field is required if <code>isCorporate</code> is <code>true</code>.</td>
    </tr>
 <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>corporateDocument</code></td>
        <td>string</td>
        <td></td>
        <td>Buyer's corporate document number. This field is required if <code>isCorporate</code> is <code>true</code>.</td>
    </tr>
 <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>isCorporate</code></td>
        <td>boolean</td>
        <td>Yes</td>
        <td>Indicates whether or not the buyer is corporate. If <code>true</code>, the fields <code>corporateName</code>, <code>tradeName</code> and <code>corporateDocument</code> are required.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>email</code></td>
        <td>string</td>
        <td></td>
        <td>Buyer's email.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>phone</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Buyer's phone number.</td>
    </tr>
<tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>createdDate</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Buyer's create datetime in format "yyyy-MM-ddTHH:mm:ss".</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>shippingAddress</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>Object containing information about the shipping address.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>country</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Shipping address: country code (ISO 3166 alpha-3).</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>street</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Shipping address: street.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>number</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Shipping address: number.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>complement</code></td>
        <td>string</td>
        <td></td>
        <td>Shipping address: complement.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>neighborhood</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Shipping address: neighborhood.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>postalCode</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Shipping address: postal code.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>city</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Shipping address: city.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>state</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Shipping address: state/province.</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>billingAddress</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>Object containing information about the billing address.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>country</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Billing address: country code (ISO 3166 alpha-3).</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>street</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Billing address: street.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>number</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Billing address: number.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>complement</code></td>
        <td>string</td>
        <td></td>
        <td>Billing address: complement.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>neighborhood</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Billing address: neighborhood.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>postalCode</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Billing address: postal code.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>city</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Billing address: city.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>state</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Billing address: state/province.</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>items</code></td>
        <td>array</td>
        <td>Yes</td>
        <td>A list of the items in the buyer's cart.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>id</code></td>
        <td>string</td>
        <td></td>
        <td>Item identifier.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>name</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Item name.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>price</code></td>
        <td>decimal</td>
        <td>Yes</td>
        <td>Item price per unity.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>quantity</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>Item quantity.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>discount</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>Discount received for the item.</td>
    </tr>
    <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>deliveryType</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Item delivery type selected by the buyer.</td>
    </tr>
 <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>categoryId</code></td>
        <td>string</td>
        <td></td>
        <td>The item category Id.</td>
    </tr>
 <tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>sellerId</code></td>
        <td>string</td>
        <td></td>
        <td>In case of a marketplace transaction, this is the Id of the seller for this specific item. Otherwise, this is filled with a "1".</td>
    </tr>
<tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>taxRate</code></td>
        <td>decimal</td>
        <td></td>
        <td>Value of the sum of all Taxes applied to each item. Rates are in percentage, so 5% is represented as 0.05.</td>
    </tr>
<tr>
        <td>&nbsp;&nbsp;&nbsp;&nbsp; &#x21B3; <code>taxValue</code></td>
        <td>decimal</td>
        <td></td>
        <td>Total Tax value of the item (taxRate times value).</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>shippingValue</code></td>
        <td>decimal</td>
        <td></td>
        <td>Total shipping value.</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>taxValue</code></td>
        <td>decimal</td>
        <td></td>
        <td>Total tax value.</td>
    </tr>
 <tr>
        <td><code>recipients</code></td>
        <td>array</td>
        <td></td>
        <td>Array containing the information for the recipients of this payment in case the Payment Provider is configured to allow the split of payments.</td>
    </tr>
  <tr>
        <td>&#x21B3; <code>id</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Recipient identifier.</td>
    </tr>
  <tr>
        <td>&#x21B3; <code>name</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Recipient name.</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>documentType</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Recipient document type.</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>document</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Recipient document number.</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>role</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Indicates if the recipient is the seller or the marketplace.</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>chargeProcessingFee</code></td>
        <td>boolean</td>
        <td></td>
        <td>Indicates whether or not this recipient is charged for processing fees.</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>chargebackLiable</code></td>
        <td>boolean</td>
        <td></td>
        <td>Indicates whether or not this recipient is liable to chargebacks.</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>amount</code></td>
        <td>boolean</td>
        <td>Yes</td>
        <td>Amount due to this recipient.</td>
    </tr>
 <tr>
        <td><code>merchantSettings</code></td>
        <td>array</td>
        <td></td>
        <td>Custom fields (for the given Provider) which the Merchant must fill. Each element of this array is a key-value pair.</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>name</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The custom field name.</td>
    </tr>
 <tr>
        <td>&#x21B3; <code>value</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The custom field value.</td>
    </tr>
    <tr>
        <td><code>url</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The order URL from merchant's backoffice.</td>
    </tr>
    <tr>
        <td><code>callbackUrl</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The URL you need to call to send the callbacks (notification or retry) of payment status changes</td>
    </tr>
    <tr>
        <td><code>returnUrl</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The URL you need to redirect the end user back to merchant's store when using the redirect flow</td>
    </tr>
    <tr>
        <td><code>inboundRequestsUrl</code></td>
        <td>string</td>
        <td></td>
        <td><strong><code>BETA</code></strong> The URL you can use to forward external requests to your payment provider endpoint.</td>
    </tr>
 <tr>
        <td><code>secureProxyUrl</code></td>
        <td>string</td>
        <td></td>
        <td>The URL for the Secure Proxy to authorize the Payment (this field is absent in case the provider does not use the Secure Proxy).</td>
    </tr>
 <tr>
        <td><code>sandboxMode</code></td>
        <td>boolean</td>
        <td></td>
        <td>Indicates whether or not this request is being sent from a sandbox environment.</td>
    </tr>
<tr>
        <td><code>totalCartValue</code></td>
        <td>decimal</td>
        <td></td>
        <td>Total amount of the shopping cart that this payment is part of. It can be used together with the value to calculate the percentage that this payment represents of the total.</td>
    </tr>
</table>

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
        <td><code>paymentId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX identifier for this payment. The same sent in the request.</td>
    </tr>
    <tr>
        <td><code>status</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The Provider's status for this payment. Must be one of three values:
        	&bull; <code>approved</code>
        	&bull; <code>denied</code>
        	&bull; <code>undefined</code></td>
    </tr>
<tr>
        <td><code>authorizationId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's unique identifier for the authorization. Should be sent when the payment is authorized. In other statuses, it should be absent or <code>null</code>.</td>
    </tr>
<tr>
        <td><code>bankIssueInvoiceId</code></td>
        <td>string</td>
        <td></td>
        <td>This field is deprecated, please use <code>paymentUrl</code> instead. The bank invoice URL to be presented to the end user.</td>
    </tr>
 <tr>
        <td><code>paymentUrl</code></td>
        <td>string</td>
        <td></td>
        <td>When the payment is via bank invoice, this should be the invoice URL to be presented to the user. If the payment requires the redirection of the user, this should be the URL to redirect the user. If neither is the case, then this should be absent.</td>
    </tr>
    <tr>
        <td><code>paymentAppData</code></td>
        <td>object</td>
        <td></td>
        <td><Indicates the VTEX IO app which will handle the payment flow at Checkout</td>
    </tr>
    <tr>
        <td>&#x21B3; <code>appName</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Indicates the VTEX IO app which will handle the payment flow at Checkout.</td>
    </tr>
  <tr>
        <td>&#x21B3; <code>payload</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The payload that will be sent to your app, like a serialized JSON, for example</td>
    </tr>
   <tr>
        <td><code>identificationNumber</code></td>
        <td>string</td>
        <td></td>
        <td>The bank invoice unformatted identification number. Should only be present when the payment is made via bank invoice.</td>
    </tr>
    <tr>
        <td><code>identificationNumberFormatted</code></td>
        <td>string</td>
        <td></td>
        <td>The bank invoice formatted identification number that will be presented to the end user.</td>
    </tr>
    <tr>
        <td><code>barCodeImageType</code></td>
        <td>string</td>
        <td></td>
        <td>The bank invoice barcode image type. For instance, "i25" for Brazilian <em>Boleto Bancário</em>. Should only be present when the payment is made via bank invoice.</em></td>
    </tr>
    <tr>
        <td><code>barCodeImageNumber</code></td>
        <td>string</td>
        <td></td>
        <td>The bank invoice number to generate a barcode (must follow any regulations/specifications for targeted countries). Should only be present when the payment is made via bank invoice.</td>
    </tr>
   <tr>
        <td><code>tid</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's unique identifier for the transaction.</td>
    </tr>
    <tr>
        <td><code>nsu</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's unique sequential number for the transaction.</td>
    </tr>
 <tr>
        <td><code>acquirer</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Acquirer name (mostly used for card payments).</td>
    </tr>
  <tr>
        <td><code>redirectUrl</code></td>
        <td>string</td>
        <td></td>
        <td>This field is deprecated, please use <code>paymentUrl</code> instead. The URL the end user needs to be redirected to (external authentication, 3DS, etc).</td>
    </tr>
    <tr>
        <td><code>code</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's operation/error code to be logged.</td>
    </tr>
    <tr>
        <td><code>message</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's operation/error message to be logged.</td>
    </tr>
    <tr>
        <td><code>delayToAutoSettle</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>Total time (in seconds) before we make and automatic call to <code>/settlements</code> no mather if the payment was approved by merchant's antifraud or not. The maximum time allowed to wait for an auto capture is <strong>604800 seconds</strong>.</td>
    </tr>
    <tr>
        <td><code>delayToAutoSettleAfterAntifraud</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>Total time (in seconds) before we make and automatic call to <code>/settlements</code> after merchant's antifraud approval.</td>
    </tr>
    <tr>
        <td><code>delayToCancel</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>Total time (in seconds) to wait for an authorization and make and automatic call to <code>/cancellations</code> to cancel the payment. The minimum value is 600 (10 minutes).</td>
    </tr>
<td><code>maxValue</code></td>
        <td>number</td>
        <td></td>
        <td>The maximum value for this payment.</td>
    </tr>
</table>

<br>

## Pix response body
---

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>paymentId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>VTEX identifier for this payment. The same sent in the request.</td>
    </tr>
    <tr>
        <td><code>status</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>The Provider's status for this payment. Must be one of three values:
        	&bull; <code>approved</code>
        	&bull; <code>denied</code>
        	&bull; <code>undefined</code></td>
    </tr>
     <tr>
        <td><code>tid</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's unique identifier for the transaction.</td>
    </tr>
<tr>
        <td><code>authorizationId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's unique identifier for the authorization. Should be sent when the payment is authorized. In other statuses, it should be absent or <code>null</code>.</td>
    </tr>
    <tr>
        <td><code>nsu</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's unique sequential number for the transaction.</td>
    </tr>
      <tr>
        <td><code>code</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's operation/error code to be logged.</td>
    </tr>
<tr>
        <td><code>paymentAppData</code></td>
        <td>object</td>
        <td>Yes</td>
        <td>Object containing information about the payment app.</td>
    </tr>
    <tr>Pix Sucess Aprroved request example in the end of the page
        <td>&#x21B3; <code>payload</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>All the information needed to expose the QR Code in the SmartCheckout. Both <code>code</code> and <code>qrCodeBase64Image</code> are mandatory and should always be sent by the provider. Check the <code>serialized JSON String</code> on the <code>request example</code> in the end of the documentation. By default, the QRCode should have five minutes (300 seconds) expiration time. Also, the partner <strong>must</strong> respect the callback time (20 seconds).</td>
    </tr>
  <tr>
    <tr>
        <td><code>message</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Provider's operation/error message to be logged.</td>
    </tr>
    <tr>
        <td><code>delayToAutoSettle</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>Total time (in seconds) before we make and automatic call to <code>/settlements</code> no mather if the payment was approved by merchant's antifraud or not. The maximum time allowed to wait for an auto capture is <strong>604800 seconds</strong>.</td>
    </tr>
    <tr>
        <td><code>delayToAutoSettleAfterAntifraud</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>Total time (in seconds) before we make and automatic call to <code>/settlements</code> after merchant's antifraud approval.</td>
    </tr>
    <tr>
        <td><code>delayToCancel</code></td>
        <td>number</td>
        <td>Yes</td>
        <td>Total time (in seconds) to wait for an authorization and make and automatic call to <code>/cancellations</code> to cancel the payment. The minimum value is 600 (10 minutes).</td>
    </tr>
</table>

<br>

## Callbacks
---
[block:callout]
{
  "type": "warning",
  "body": "There are two possible uses for callbacks with the Create Payment endpoint. For integrations that do not use VTEX IO, use the **Notification** callback. For integrations developed using VTEX IO infrastructure, use the **Retry** callback."
}
[/block]
> **Notification:** If a payment returns with `undefined` status, you are expected to send us a callback/notification to update it later, sending a POST with an updated version of your response (same structure as above) to the `callbackUrl` we have provided.
> 
> **Retry:** If a payment returns with `undefined` status, you are expected to call the retry endpoint provided by the `callbackUrl` when the processing of the payment is completed, so we make another Create Payment request to update the status with the new value (`authorized` or `denied`).
> 
> This request should be authenticated using a Key and Token you can <a href="https://help.vtex.com/tutorial/criar-appkey-e-apptoken-para-autenticar-integracoes" target="_blank">generate from your VTEX partner account License Manager</a>. To do so, `POST` your request passing the `X-VTEX-API-AppKey` and `X-VTEX-API-AppToken` headers with your credentials. **Note:** do not mix up these credentials with the ones we send on behalf of the merchant when sending our requests.

<br>

### Callback URL

The `callbackUrl` field contains an URL that the payment provider uses to make a callback and inform our gateway of the final payment status: `approved` or `denied`. 

This URL has some query parameters, including the `X-VTEX-signature`. This parameter is mandatory and contains a signature token to identify that the request has been generated from VTEX as a security measure. The signature token has at most 32 characters. You can check an example of callback URL with the signature token below:

```
https://gatewayqa.vtexpayments.com.br/api/pvt/payment-provider/transactions/8FB0F111111122222333344449984ACB/payments/A2A9A25B11111111222222333327883C/callback?accountName=teampaymentsintegrations&X-VTEX-signature=R123456789aBcDeFGHij1234567890tk
```

In the [Transactions page of the Admin](https://help.vtex.com/en/tutorial/how-to-view-the-orders-details--tutorials_452), the signature token appears masked for security reasons, as in this example: `X-VTEX-signature=Rj******tk`.

When making the callback request, we recommend that payment providers use the callback URL exactly as received, which guarantees that all the parameters are included.

## Beta features 
---

> You can reach out to our team by openning a ticket to know more about any **`BETA`** features.
>
> `paymentAppData`<br>
> As an option to the redirect flow, we're offering a new way to allow payment providers to open a modal at the Checkout page to finish the payment process.
>
> `inboundRequestsUrl`<br>
> Allows to forward external requests back to your payment provider implementation, including the configured credentials (`X-VTEX-API-*` headers), and settings.

## Request examples and their responses 

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"reference\": \"618272\",\n    \"orderId\": \"1072430428324\",\n    \"shopperInteraction\": \"ecommerce\",\n    \"transactionId\": \"2F023FD5A72A49D48A8633252B7CCBD6\",\n    \"paymentId\": \"01693EB95BE443AC85874E395CD91565\",\n    \"paymentMethod\": \"Diners\",\n    \"merchantName\": \"mystore\",\n    \"card\": {\n        \"holder\": \"John Doe\",\n        \"number\": \"364901****2661\",\n        \"csc\": \"***\",\n        \"expiration\": {\n            \"month\": \"12\",\n            \"year\": \"2020\"\n        },\n        \"document\": \"39295416023\",\n        \"token\": null\n    },\n    \"value\": 31.90,\n    \"currency\": \"BRL\",\n    \"installments\": 1,\n    \"installmentsInterestRate\": 0.00,\n    \"installmentsValue\": 31.90,\n    \"deviceFingerprint\": \"75076388\",\n    \"ipAddress\": \"187.105.111.65\",\n    \"miniCart\": {\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"cpf\",\n            \"corporateName\": null,\n            \"tradeName\": null,\n            \"corporateDocument\": null,\n            \"isCorporate\": false,\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521999999999\",\n            \"createdDate\": \"2020-02-18T18:17:45\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"8\",\n                \"name\": \"Tenis Preto I\",\n                \"price\": 30.9,\n                \"quantity\": 1,\n                \"discount\": 0.0,\n                \"deliveryType\": \"Normal\",\n                \"categoryId\": \"5\",\n                \"sellerId\": \"1\"\n            }\n        ],\n        \"shippingValue\": 1.0,\n        \"taxValue\": 0.0\n    },\n    \"url\": \"https://admin.mystore.example.com/orders?q=1072430428324\",\n    \"callbackUrl\": \"https://api.mystore.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/1072430428324\",\n    \"inboundRequestsUrl\": \"https://api.mystore.example.com/checkout/order/1072430428324/inbound-request/:action\",\n    \"recipients\": [\n        {\n            \"id\": \"mymarketplace\",\n            \"name\": \"My Marketplace QA\",\n            \"documentType\": \"CNPJ\",\n            \"document\": \"99999999999999\",\n            \"role\": \"marketplace\",\n            \"chargeProcessingFee\": true,\n            \"chargebackLiable\": true,\n            \"amount\": 31.90\n        }\n    ],\n    \"merchantSettings\": [\n        {\n            \"name\": \"field1\",\n            \"value\": \"value1\"\n        },\n        {\n            \"name\": \"field2\",\n            \"value\": \"value2\"\n        }\n    ]\n}'",
      "language": "curl",
      "name": "Credit Card Success Approved"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"reference\": \"32478982\",\n    \"orderId\": \"v967373115140abc\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"paymentMethod\": \"Pix\",\n    \"paymentMethodCustomCode\": null,\n    \"merchantName\": \"mystore\",\n    \"value\": 4307.23,\n    \"currency\": \"BRL\",\n    \"installments\": 31,\n    \"deviceFingerprint\": \"12ade389087fe\",\n    \"card\": {\n        \"holder\": null,\n        \"number\": null,\n        \"csc\": null,\n        \"expiration\": {\n            \"month\": null,\n            \"year\": null\n        }\n    },\n    \"miniCart\": {\n        \"shippingValue\": 11.44,\n        \"taxValue\": 10.01,\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"CPF\",\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521987654321\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"132981\",\n                \"name\": \"My First Product\",\n                \"price\": 2134.90,\n                \"quantity\": 2,\n                \"discount\": 5.00\n            },\n            {\n                \"id\": \"123242\",\n                \"name\": \"My Second Product\",\n                \"price\": 21.98,\n                \"quantity\": 1,\n                \"discount\": 1.00\n            }\n        ]\n    },\n    \"url\": \"https://admin.mystore.example.com/orders/v32478982\",\n    \"callbackUrl\": \"https://api.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/v32478982\"\n}'",
      "language": "curl",
      "name": "Pix Success Approved"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"reference\": \"32478982\",\n    \"orderId\": \"v967373115140abc\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"paymentMethod\": \"Visa\",\n    \"paymentMethodCustomCode\": null,\n    \"merchantName\": \"mystore\",\n    \"value\": 4307.23,\n    \"currency\": \"BRL\",\n    \"installments\": 3,\n    \"deviceFingerprint\": \"12ade389087fe\",\n    \"card\": {\n        \"holder\": \"John Doe\",\n        \"number\": \"4682185088924788\",\n        \"csc\": \"021\",\n        \"expiration\": {\n            \"month\": \"06\",\n            \"year\": \"2029\"\n        }\n    },\n    \"miniCart\": {\n        \"shippingValue\": 11.44,\n        \"taxValue\": 10.01,\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"CPF\",\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521987654321\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"132981\",\n                \"name\": \"My First Product\",\n                \"price\": 2134.90,\n                \"quantity\": 2,\n                \"discount\": 5.00\n            },\n            {\n                \"id\": \"123242\",\n                \"name\": \"My Second Product\",\n                \"price\": 21.98,\n                \"quantity\": 1,\n                \"discount\": 1.00\n            }\n        ]\n    },\n    \"url\": \"https://admin.mystore.example.com/orders/v32478982\",\n    \"callbackUrl\": \"https://api.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/v32478982\"\n}'",
      "language": "curl",
      "name": "Success Undefined"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"reference\": \"32478982\",\n    \"orderId\": \"v967373115140abc\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"paymentMethod\": \"BankInvoice\",\n    \"paymentMethodCustomCode\": null,\n    \"merchantName\": \"mystore\",\n    \"value\": 4307.23,\n    \"currency\": \"BRL\",\n    \"installments\": 1,\n    \"deviceFingerprint\": \"12ade389087fe\",\n    \"card\": {\n        \"holder\": null,\n        \"number\": null,\n        \"csc\": null,\n        \"expiration\": {\n            \"month\": null,\n            \"year\": null\n        }\n    },\n    \"miniCart\": {\n        \"shippingValue\": 11.44,\n        \"taxValue\": 10.01,\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"CPF\",\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521987654321\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"132981\",\n                \"name\": \"My First Product\",\n                \"price\": 2134.90,\n                \"quantity\": 2,\n                \"discount\": 5.00\n            },\n            {\n                \"id\": \"123242\",\n                \"name\": \"My Second Product\",\n                \"price\": 21.98,\n                \"quantity\": 1,\n                \"discount\": 1.00\n            }\n        ]\n    },\n    \"url\": \"https://admin.mystore.example.com/orders/v32478982\",\n    \"callbackUrl\": \"https://api.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/v32478982\"\n}'",
      "language": "curl",
      "name": "Sucess Undefined BankInvoice"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"reference\": \"32478982\",\n    \"orderId\": \"v967373115140abc\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"paymentMethod\": \"FakePay\",\n    \"paymentMethodCustomCode\": null,\n    \"merchantName\": \"mystore\",\n    \"value\": 4307.23,\n    \"currency\": \"BRL\",\n    \"installments\": 1,\n    \"deviceFingerprint\": \"12ade389087fe\",\n    \"card\": {\n        \"holder\": null,\n        \"number\": null,\n        \"csc\": null,\n        \"expiration\": {\n            \"month\": null,\n            \"year\": null\n        }\n    },\n    \"miniCart\": {\n        \"shippingValue\": 11.44,\n        \"taxValue\": 10.01,\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"CPF\",\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521987654321\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"132981\",\n                \"name\": \"My First Product\",\n                \"price\": 2134.90,\n                \"quantity\": 2,\n                \"discount\": 5.00\n            },\n            {\n                \"id\": \"123242\",\n                \"name\": \"My Second Product\",\n                \"price\": 21.98,\n                \"quantity\": 1,\n                \"discount\": 1.00\n            }\n        ]\n    },\n    \"url\": \"https://admin.mystore.example.com/orders/v32478982\",\n    \"callbackUrl\": \"https://api.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/v32478982\"\n}'",
      "language": "curl",
      "name": "Success Undefined Redirect"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"reference\": \"32478982\",\n    \"orderId\": \"v967373115140abc\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"paymentMethod\": \"Visa\",\n    \"paymentMethodCustomCode\": null,\n    \"merchantName\": \"mystore\",\n    \"value\": 4307.23,\n    \"currency\": \"BRL\",\n    \"installments\": 3,\n    \"deviceFingerprint\": \"12ade389087fe\",\n    \"card\": {\n        \"holder\": \"John Doe\",\n        \"number\": \"4682185088924788\",\n        \"csc\": \"021\",\n        \"expiration\": {\n            \"month\": \"06\",\n            \"year\": \"2029\"\n        }\n    },\n    \"miniCart\": {\n        \"shippingValue\": 11.44,\n        \"taxValue\": 10.01,\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"CPF\",\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521987654321\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"132981\",\n                \"name\": \"My First Product\",\n                \"price\": 2134.90,\n                \"quantity\": 2,\n                \"discount\": 5.00\n            },\n            {\n                \"id\": \"123242\",\n                \"name\": \"My Second Product\",\n                \"price\": 21.98,\n                \"quantity\": 1,\n                \"discount\": 1.00\n            }\n        ]\n    },\n    \"url\": \"https://admin.mystore.example.com/orders/v32478982\",\n    \"callbackUrl\": \"https://api.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/v32478982\"\n}'",
      "language": "curl",
      "name": "Success Denied"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"reference\": \"32478982\",\n    \"orderId\": \"v967373115140abc\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"paymentMethod\": \"Visa\",\n    \"paymentMethodCustomCode\": null,\n    \"merchantName\": \"mystore\",\n    \"value\": 4307.23,\n    \"currency\": \"BRL\",\n    \"installments\": 3,\n    \"deviceFingerprint\": \"12ade389087fe\",\n    \"card\": {\n        \"holder\": \"John Doe\",\n        \"number\": \"4682185088924788\",\n        \"csc\": \"021\",\n        \"expiration\": {\n            \"month\": \"06\",\n            \"year\": \"2029\"\n        }\n    },\n    \"miniCart\": {\n        \"shippingValue\": 11.44,\n        \"taxValue\": 10.01,\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"CPF\",\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521987654321\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"132981\",\n                \"name\": \"My First Product\",\n                \"price\": 2134.90,\n                \"quantity\": 2,\n                \"discount\": 5.00\n            },\n            {\n                \"id\": \"123242\",\n                \"name\": \"My Second Product\",\n                \"price\": 21.98,\n                \"quantity\": 1,\n                \"discount\": 1.00\n            }\n        ]\n    },\n    \"url\": \"https://admin.mystore.example.com/orders/v32478982\",\n    \"callbackUrl\": \"https://api.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/v32478982\"\n}'",
      "language": "curl",
      "name": "Fail Generic Error"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"reference\": \"32478982\",\n    \"orderId\": \"v967373115140abc\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"paymentMethod\": \"Visa\",\n    \"paymentMethodCustomCode\": null,\n    \"merchantName\": \"mystore\",\n    \"value\": 4307.23,\n    \"currency\": \"ABC\",\n    \"installments\": 3,\n    \"deviceFingerprint\": \"12ade389087fe\",\n    \"card\": {\n        \"holder\": \"John Doe\",\n        \"number\": \"4682185088924788\",\n        \"csc\": \"021\",\n        \"expiration\": {\n            \"month\": \"06\",\n            \"year\": \"2029\"\n        }\n    },\n    \"miniCart\": {\n        \"shippingValue\": 11.44,\n        \"taxValue\": 10.01,\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"CPF\",\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521987654321\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"132981\",\n                \"name\": \"My First Product\",\n                \"price\": 2134.90,\n                \"quantity\": 2,\n                \"discount\": 5.00\n            },\n            {\n                \"id\": \"123242\",\n                \"name\": \"My Second Product\",\n                \"price\": 21.98,\n                \"quantity\": 1,\n                \"discount\": 1.00\n            }\n        ]\n    },\n    \"url\": \"https://admin.mystore.example.com/orders/v32478982\",\n    \"callbackUrl\": \"https://api.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/v32478982\"\n}'",
      "language": "curl",
      "name": "Fail Bad Request"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"reference\": \"32478982\",\n    \"orderId\": \"v967373115140abc\",\n    \"transactionId\": \"D3AA1FC8372E430E8236649DB5EBD08E\",\n    \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n    \"paymentMethod\": \"CustomPay\",\n    \"paymentMethodCustomCode\": null,\n    \"merchantName\": \"mystore\",\n    \"value\": 4307.23,\n    \"currency\": \"BRL\",\n    \"installments\": 1,\n    \"deviceFingerprint\": \"12ade389087fe\",\n    \"card\": {\n        \"holder\": null,\n        \"number\": null,\n        \"csc\": null,\n        \"expiration\": {\n            \"month\": null,\n            \"year\": null\n        }\n    },\n    \"miniCart\": {\n        \"shippingValue\": 11.44,\n        \"taxValue\": 10.01,\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"CPF\",\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521987654321\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"132981\",\n                \"name\": \"My First Product\",\n                \"price\": 2134.90,\n                \"quantity\": 2,\n                \"discount\": 5.00\n            },\n            {\n                \"id\": \"123242\",\n                \"name\": \"My Second Product\",\n                \"price\": 21.98,\n                \"quantity\": 1,\n                \"discount\": 1.00\n            }\n        ]\n    },\n    \"url\": \"https://admin.mystore.example.com/orders/v32478982\",\n    \"callbackUrl\": \"https://api.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/v32478982\",\n    \"inboundRequestsUrl\": \"https://mystore.api.example.com/some-path/inbound-request/:action\"\n}'",
      "language": "curl",
      "name": "Success Undefined Payment App + Inbound Requests"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"reference\": \"618272\",\n    \"orderId\": \"1072430428324\",\n    \"shopperInteraction\": \"ecommerce\",\n    \"transactionId\": \"2F023FD5A72A49D48A8633252B7CCBD6\",\n    \"paymentId\": \"01693EB95BE443AC85874E395CD91565\",\n    \"paymentMethod\": \"BankInvoice\",\n    \"merchantName\": \"mystore\",\n    \"card\": {\n        \"holder\": null,\n        \"number\": null,\n        \"csc\": null,\n        \"expiration\": {\n            \"month\": null,\n            \"year\": null\n        },\n        \"document\": null,\n        \"token\": null\n    },\n    \"value\": 31.90,\n    \"currency\": \"BRL\",\n    \"installments\": 1,\n    \"installmentsInterestRate\": 0.00,\n    \"installmentsValue\": 31.90,\n    \"deviceFingerprint\": \"98073964\",\n    \"ipAddress\": \"187.105.111.65\",\n    \"miniCart\": {\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"cpf\",\n            \"corporateName\": null,\n            \"tradeName\": null,\n            \"corporateDocument\": null,\n            \"isCorporate\": false,\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521999999999\",\n            \"createdDate\": \"2020-02-18T18:17:45\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"8\",\n                \"name\": \"Tenis Preto I\",\n                \"price\": 30.9,\n                \"quantity\": 1,\n                \"discount\": 0.0,\n                \"deliveryType\": \"Normal\",\n                \"categoryId\": \"5\",\n                \"sellerId\": \"1\"\n            }\n        ],\n        \"shippingValue\": 1.0,\n        \"taxValue\": 0.0\n    },\n    \"url\": \"https://admin.mystore.example.com/orders?q=1072430428324\",\n    \"callbackUrl\": \"https://api.mystore.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/1072430428324\",\n    \"inboundRequestsUrl\": \"https://api.mystore.example.com/checkout/order/1072430428324/inbound-request/:action\",\n    \"recipients\": [\n        {\n            \"id\": \"mymarketplace\",\n            \"name\": \"My Marketplace QA\",\n            \"documentType\": \"CNPJ\",\n            \"document\": \"99999999999999\",\n            \"role\": \"marketplace\",\n            \"chargeProcessingFee\": true,\n            \"chargebackLiable\": true,\n            \"amount\": 31.90\n        }\n    ],\n    \"merchantSettings\": [\n        {\n            \"name\": \"field1\",\n            \"value\": \"value1\"\n        },\n        {\n            \"name\": \"field2\",\n            \"value\": \"value2\"\n        }\n    ]\n}'",
      "language": "curl",
      "name": "Boleto - Success Approved"
    },
    {
      "code": "curl --location --request POST 'https://{{providerApiEndpoint}}/payments' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'Content-Type: application/json' \\\n--header 'Accept: application/json' \\\n--data-raw '{\n    \"reference\": \"618272\",\n    \"orderId\": \"1072430428324\",\n    \"shopperInteraction\": \"ecommerce\",\n\n    \"transactionId\": \"2F023FD5A72A49D48A8633252B7CCBD6\",\n    \"paymentId\": \"01693EB95BE443AC85874E395CD91565\",\n    \"paymentMethod\": \"RedirectPay\",\n    \"paymentMethodCustomCode\": null,\n    \"merchantName\": \"mystore\",\n    \"card\": {\n        \"holder\": null,\n        \"number\": null,\n        \"csc\": null,\n        \"expiration\": {\n            \"month\": null,\n            \"year\": null\n        },\n        \"document\": null,\n        \"token\": null\n    },\n    \"value\": 31.90,\n    \"currency\": \"BRL\",\n    \"installments\": 1,\n    \"installmentsInterestRate\": 0.00,\n    \"installmentsValue\": 31.90,\n    \"deviceFingerprint\": \"75076388\",\n    \"ipAddress\": \"187.105.111.65\",\n    \"miniCart\": {\n        \"buyer\": {\n            \"id\": \"c1245228-1c68-11e6-94ac-0afa86a846a5\",\n            \"firstName\": \"John\",\n            \"lastName\": \"Doe\",\n            \"document\": \"01234567890\",\n            \"documentType\": \"cpf\",\n            \"corporateName\": null,\n            \"tradeName\": null,\n            \"corporateDocument\": null,\n            \"isCorporate\": false,\n            \"email\": \"john.doe@example.com\",\n            \"phone\": \"+5521999999999\",\n            \"createdDate\": \"2020-02-18T18:17:45\"\n        },\n        \"shippingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Praia de Botafogo St.\",\n            \"number\": \"300\",\n            \"complement\": \"3rd Floor\",\n            \"neighborhood\": \"Botafogo\",\n            \"postalCode\": \"22250040\",\n            \"city\": \"Rio de Janeiro\",\n            \"state\": \"RJ\"\n        },\n        \"billingAddress\": {\n            \"country\": \"BRA\",\n            \"street\": \"Brigadeiro Faria Lima Avenue\",\n            \"number\": \"4440\",\n            \"complement\": \"10th Floor\",\n            \"neighborhood\": \"Itaim Bibi\",\n            \"postalCode\": \"04538132\",\n            \"city\": \"São Paulo\",\n            \"state\": \"SP\"\n        },\n        \"items\": [\n            {\n                \"id\": \"8\",\n                \"name\": \"Tenis Preto I\",\n                \"price\": 30.9,\n                \"quantity\": 1,\n                \"discount\": 0.0,\n                \"deliveryType\": \"Normal\",\n                \"categoryId\": \"5\",\n                \"sellerId\": \"1\"\n            }\n        ],\n        \"shippingValue\": 1.0,\n        \"taxValue\": 0.0\n    },\n    \"url\": \"https://admin.mystore.example.com/orders?q=1072430428324\",\n    \"callbackUrl\": \"https://api.mystore.example.com/some-path/to-notify/status-changes?an=mystore\",\n    \"returnUrl\": \"https://mystore.example.com/checkout/order/1072430428324\",\n    \"inboundRequestsUrl\": \"https://api.mystore.example.com/checkout/order/1072430428324/inbound-request/:action\",\n    \"recipients\": [\n        {\n            \"id\": \"mymarketplace\",\n            \"name\": \"My Marketplace QA\",\n            \"documentType\": \"CNPJ\",\n            \"document\": \"99999999999999\",\n            \"role\": \"marketplace\",\n            \"chargeProcessingFee\": true,\n            \"chargebackLiable\": true,\n            \"amount\": 31.90\n        }\n    ],\n    \"merchantSettings\": [\n        {\n            \"name\": \"field1\",\n            \"value\": \"value1\"\n        },\n        {\n            \"name\": \"field2\",\n            \"value\": \"value2\"\n        }\n    ]\n}'",
      "language": "curl",
      "name": "Redirect Success Approved"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n  \"status\": \"undefined\",\n  \"tid\": \"TID1578324421\",\n  \"authorizationId\": null,\n  \"nsu\": null,\n  \"code\": \"APP123\",\n  \"paymentAppData\": {\n    \"appName\": \"vendor.payment-auth-app\",\n    \"payload\": \"{\\\"backendUrl\\\":\\\"https://api.example.org/payments/F5C1A4E20D3B4E07B7E871F5B5BC9F91\\\",\\\"randomString\\\":\\\"78818C2C64264212B8D5771BDC7B1A\\\",\\\"randomBool\\\":false,\\\"timestamp\\\":\\\"2019-10-07 21:30:09Z\\\"}\"\n  },\n  \"message\": \"The customer needs to finish the payment flow\",\n  \"delayToAutoSettle\": 604800,\n  \"delayToAutoSettleAfterAntifraud\": 120,\n  \"delayToCancel\": 604800\n}",
      "language": "curl",
      "name": "200 - OK"
    },
    {
      "code": "{\n  \"paymentId\": \"F5C1A4E20D3B4E07B7E871F5B5BC9F91\",\n  \"status\": \"undefined\",\n  \"tid\": \"TID1578324421\",\n  \"authorizationId\": null,\n  \"nsu\": null,\n  \"code\": \"APP123\",\n  \"paymentAppData\": {\n    \"payload\": \"{\\\"code\\\":\\\"https://bacen.pix/pix/code\\\",\\\"qrCodeBase64Image\\\":\\\"iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAAABQGlDQ1BJQ0MgUHJvZmlsZQAAKJFjYGDiSSwoyGFhYGDIzSspCnJ3UoiIjFJgf8LAxSDMwMkgwiCZmFxc4BgQ4ANUwgCjUcG3awyMIPqyLsgspwWXFu+Xeyundb6w0WL33C5M9SiAKyW1OBlI/wHihOSCohIGBsYYIFu5vKQAxG4AskWKgI4CsqeA2OkQ9goQOwnC3gNWExLkDGRfALIFkjMSU4DsB0C2ThKSeDoSG2ovCLAZGZkbhBNwKKmgJLWiBEQ75xdUFmWmZ5QoOAJDJ1XBMy9ZT0fByMDIgIEBFNYQ1Z9vgMOQUYwDIZapzMBgmQEUfIQQSxNmYNiZzsDAU4UQU5/PwMBrxMBw5GJBYlEi3AGM31iK04yNIGzu7QwMrNP+//8M9Ca7JgPD3+v////e/v//32UMDMy3GBgOfAMA4+RdqZ9YRkcAAABWZVhJZk1NACoAAAAIAAGHaQAEAAAAAQAAABoAAAAAAAOShgAHAAAAEgAAAESgAgAEAAAAAQAAAAKgAwAEAAAAAQAAAAIAAAAAQVNDSUkAAABTY3JlZW5zaG900Fpo3gAAAdJpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iPgogICAgICAgICA8ZXhpZjpQaXhlbFhEaW1lbnNpb24+MjwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlVzZXJDb21tZW50PlNjcmVlbnNob3Q8L2V4aWY6VXNlckNvbW1lbnQ+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4yPC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+Cl89Cn4AAAASSURBVAgdY/wPBAxAwAQiQAAAPfgEAIAu9DkAAAAASUVORK5CYII=\\\"}\"\n  },\n  \"message\": \"The customer needs to finish the payment flow\",\n  \"delayToAutoSettle\": 604800,\n  \"delayToAutoSettleAfterAntifraud\": 120,\n  \"delayToCancel\": 300\n}",
      "language": "curl",
      "name": "Pix - 200 - OK"
    },
    {
      "code": "{\n    \"paymentId\": \"01693EB95BE443AC85874E395CD91565\",\n    \"status\": \"approved\",\n    \"authorizationId\": \"AUT-09DC5E8F03\",\n    \"nsu\": \"NSU-107521E866\",\n    \"tid\": \"TID-7B58BE1A08\",\n    \"acquirer\": \"TestPay\",\n    \"code\": \"2000\",\n    \"message\": null,\n    \"delayToAutoSettle\": 21600,\n    \"delayToAutoSettleAfterAntifraud\": 1800,\n    \"delayToCancel\": 21600\n}",
      "language": "curl",
      "name": "Credit Card - 200 - OK"
    },
    {
      "code": "{\n    \"paymentId\": \"01693EB95BE443AC85874E395CD91565\",\n    \"status\": \"undefined\",\n    \"authorizationId\": \"AUT-2E7CBF7290-ASYNC\",\n    \"paymentUrl\": \"https://example.org/boleto/gatewayqa/2F023FD5A72A49D48A8633252B7CCBD6/01693EB95BE443AC85874E395CD91565\",\n    \"identificationNumber\": \"23790504004199031316957008109209378300000019900\",\n    \"identificationNumberFormatted\": \"23790.50400 41990.313169 57008.109209 3 78300000019900\",\n    \"barCodeImageType\": \"i25\",\n    \"barCodeImageNumber\": \"23793783000000199000504041990313165700810920\",\n    \"nsu\": \"NSU-60F328ACD8-ASYNC\",\n    \"tid\": \"TID-F3FB9B3FDB-ASYNC\",\n    \"acquirer\": \"TestPay\",\n    \"code\": \"2000-ASYNC\",\n    \"message\": null,\n    \"delayToAutoSettle\": 21600,\n    \"delayToAutoSettleAfterAntifraud\": 1800,\n    \"delayToCancel\": 21600\n}",
      "language": "curl",
      "name": "Boleto - 200 - OK"
    },
    {
      "code": "{\n    \"paymentId\": \"01693EB95BE443AC85874E395CD91565\",\n    \"status\": \"undefined\",\n    \"authorizationId\": \"AUT-6929AD8429\",\n    \"paymentAppData\": {\n        \"appName\": \"vtex.payment\",\n        \"payload\": \"{\\\"approvePaymentUrl\\\":\\\"https://api.mystore.example.com/payments/F5C1A4E20D3B4E07B7E871F5B5BC9F91/callback-trigger/approved?url=https://api.mystore.example.com/transactions/D3AA1FC8372E430E8236649DB5EBD08E/payments/F5C1A4E20D3B4E07B7E871F5B5BC9F91/notification\\\",\\\"denyPaymentUrl\\\":\\\"https://api.mystore.example.com/payments/F5C1A4E20D3B4E07B7E871F5B5BC9F91/callback-trigger/denied?url=https://api.mystore.example.com/transactions/D3AA1FC8372E430E8236649DB5EBD08E/payments/F5C1A4E20D3B4E07B7E871F5B5BC9F91/notification\\\",\\\"orderId\\\":\\\"1072650953886\\\",\\\"transactionId\\\":\\\"D3AA1FC8372E430E8236649DB5EBD08E\\\",\\\"paymentId\\\":\\\"F5C1A4E20D3B4E07B7E871F5B5BC9F91\\\",\\\"timestamp\\\":\\\"2020-10-29 17:15:59Z\\\"}\"\n    },\n    \"nsu\": \"NSU-227AFD0BD2\",\n    \"tid\": \"TID-DBE4BFFB19\",\n    \"acquirer\": \"TestPay\",\n    \"code\": \"2001\",\n    \"message\": null,\n    \"delayToAutoSettle\": 21600,\n    \"delayToAutoSettleAfterAntifraud\": 1800,\n    \"delayToCancel\": 21600\n}",
      "language": "curl",
      "name": "Payment App - 200 - OK"
    },
    {
      "code": "{\n    \"paymentId\": \"7ee64e51-a0d3-4405-874c-d7497ab84572\",\n    \"status\": \"undefined\",\n    \"tid\": \"214c699cb408ce6a7110\",\n    \"paymentUrl\": \"http://php-connector.herokuapp.com/installments.php?paymentId=7ee64e51-a0d3-4405-874c-d7497ab84572\"\n}",
      "language": "curl",
      "name": "Redirect - 200 - OK"
    },
    {
      "code": "{\n    \"paymentId\": \"7ee64e51-a0d3-4405-874c-d7497ab84572\",\n    \"status\": \"approved\",\n    \"authorizationId\": \"3baafb4097d6c8ad3883\",\n    \"paymentUrl\": null,\n    \"nsu\": \"214c699cb408ce6a7110\",\n    \"tid\": \"214c699cb408ce6a7110\",\n    \"acquirer\": null,\n    \"code\": null,\n    \"message\": \"Payment with custom installments approved\",\n    \"delayToAutoSettle\": 21600,\n    \"delayToAutoSettleAfterAntifraud\": 1800,\n    \"delayToCancel\": 21600\n}",
      "language": "curl",
      "name": "Callback - 200 - OK"
    }
  ]
}
[/block]