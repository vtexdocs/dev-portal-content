---
title: "Order Placement"
slug: "order-placement"
excerpt: "Once the customer finishes their checkout, the marketplace needs to let the seller know there is a newly placed order. It does that by calling the **Order Placement** endpoint, which needs to be implemented by the seller.\n\nThe marketplace will send information such as the items contained in the cart, the client’s profile data, the shipping data, and the payment data. With all that, the seller will be able to create the order in their own store."
hidden: false
createdAt: "2020-09-01T13:10:10.116Z"
updatedAt: "2020-09-01T21:19:24.611Z"
---
## Request body example
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"marketplaceOrderId\": \"959311095\",\n    \"marketplaceServicesEndpoint\": \"https://marketplaceservicesendpoint/\",\n    \"marketplacePaymentValue\": 11080,\n    \"items\": [\n        {\n        \"id\": \"2002495\",\n        \"quantity\": 1,\n        \"Seller\": \"1\",\n        \"commission\": 0,\n        \"freightCommission\": 0,\n        \"price\": 9990,\n        \"bundleItems\": [],\n        \"itemAttachment\": {\n            \"name\": null,\n            \"content\": {}\n        },\n        \"attachments\": [],\n        \"priceTags\": [],\n        \"measurementUnit\": null,\n        \"unitMultiplier\": 0,\n        \"isGift\": false\n        }\n    ],\n    \"clientProfileData\": {\n        \"email\": \"32172239852@gmail.com.br\",\n        \"firstName\": \"John\",\n        \"lastName\": \"Smith\",\n        \"documentType\": null,\n        \"document\": \"3244239851\",\n        \"phone\": \"399271258\",\n        \"corporateName\": null,\n        \"tradeName\": null,\n        \"corporateDocument\": null,\n        \"stateInscription\": null,\n        \"corporatePhone\": null,\n        \"isCorporate\": false,\n        \"userProfileId\": null\n    },\n    \"shippingData\": {\n        \"address\": {\n        \"addressType\": \"Residencial\",\n        \"receiverName\": \"John Smith\",\n        \"addressId\": \"Home\",\n        \"postalCode\": \"13476103\",\n        \"city\": \"Americana\",\n        \"state\": \"SP\",\n        \"country\": \"BRA\",\n        \"street\": \"JOÃO DAMÁZIO GOMES\",\n        \"number\": \"311\",\n        \"neighborhood\": \"SÃO JOSÉ\",\n        \"complement\": null,\n        \"reference\": \"Bairro Praia Azul / Posto de Saúde 17\",\n        \"geoCoordinates\": []\n        },\n        \"logisticsInfo\": [\n        {\n            \"itemIndex\": 0,\n            \"selectedSla\": \"Regular\",\n            \"lockTTL\": \"8d\",\n            \"shippingEstimate\": \"7d\",\n            \"price\": 1090,\n            \"deliveryWindow\": null\n        }\n        ]\n    },\n    \"openTextField\": null,\n    \"marketingData\": {\n        \"utmSource\": \"buscape\",\n        \"utmMedium\": \"\",\n        \"utmCampaign\": \"freeshipping\",\n        \"utmiPage\": \"_\",\n        \"utmiPart\": \"BuscaFullText\",\n        \"utmiCampaign\": \"artscase for iphone 5\"\n    },\n    \"paymentData\": null\n}",
      "language": "json"
    }
  ]
}
[/block]
## Response body fields

The Order Placement response, sent by the seller to the marketplace, should contain the same fields that come in the request, plus two extra fields:

<table>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><code>orderId</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>A string that identifies the order inserted into the Seller.</td>
    </tr>
    <tr>
        <td><code>followUpEmail</code></td>
        <td>string</td>
        <td>Yes</td>
        <td>Email for sending order updates.</td>
    </tr>
</table>

## Response body example
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"marketplaceOrderId\": \"959311095\",\n  \"orderId\": \"123543123\",\n  \"followUpEmail\": \"75c70c09dbb3498c9b3bbdee59bf0687@ct.vtex.com.br\",\n  \"items\": [\n    {\n      \"id\": \"2002495\",\n      \"quantity\": 1,\n      \"Seller\": \"1\",\n      \"commission\": 0,\n      \"freightCommission\": 0,\n      \"price\": 9990,\n      \"bundleItems\": [],\n      \"priceTags\": [],\n      \"measurementUnit\": \"un\",\n      \"unitMultiplier\": 1,\n      \"isGift\": false\n    }\n  ],\n  \"clientProfileData\": {\n    \"email\": \"5c77abaea35f4cb6824b9326942c00e5@ct.vtex.com.br\",\n    \"firstName\": \"JONAS\",\n    \"lastName\": \"ALVES DE OLIVEIRA\",\n    \"documentType\": \"cpf\",\n    \"document\": \"32133239851\",\n    \"phone\": \"1592712979\",\n    \"corporateName\": null,\n    \"tradeName\": null,\n    \"corporateDocument\": null,\n    \"stateInscription\": null,\n    \"corporatePhone\": null,\n    \"isCorporate\": false,\n    \"userProfileId\": null\n  },\n  \"shippingData\": {\n    \"address\": {\n      \"addressType\": \"Residencial\",\n      \"receiverName\": \"JONAS ALVES DE OLIVEIRA\",\n      \"addressId\": \"Casa\",\n      \"postalCode\": \"13476103\",\n      \"city\": \"Americana\",\n      \"state\": \"SP\",\n      \"country\": \"BRA\",\n      \"street\": \"JOÃO DAMÁZIO GOMES\",\n      \"number\": \"121\",\n      \"neighborhood\": \"SÃO JOSÉ\",\n      \"complement\": null,\n      \"reference\": \"Bairro Praia Azul / Posto de Saúde 17\",\n      \"geoCoordinates\": []\n    },\n    \"logisticsInfo\": [\n      {\n        \"itemIndex\": 0,\n        \"selectedSla\": \"Normal\",\n        \"lockTTL\": \"8d\",\n        \"shippingEstimate\": \"5d\",\n        \"price\": 1090,\n        \"deliveryWindow\": null\n      }\n    ]\n  },\n  \"paymentData\": null\n}",
      "language": "json"
    }
  ]
}
[/block]