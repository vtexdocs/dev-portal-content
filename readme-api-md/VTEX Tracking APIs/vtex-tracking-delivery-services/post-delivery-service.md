---
title: "Post Delivery Service"
slug: "post-delivery-service"
excerpt: "Creates a delivery service in your Tracking system. It allows the user to configure the Route Scheduling services, without defining the Delivery Person or Route Date."
hidden: false
createdAt: "2020-11-09T19:57:54.322Z"
updatedAt: "2020-11-09T20:05:37.516Z"
---
[block:code]
{
  "codes": [
    {
      "code": "[\n    {\n        \"deliveryServiceType\": \"Entrega\",\n        \"shipperCustomer\": {\n            \"legalType\": \"PJ\",\n            \"companyName\": \"COMP. BRAS. DE TECN. PARA E-COMMERCE\",\n            \"cnpj\": \"05314972000174\",\n            \"addressStreet\": \"Rua Praia de Botafogo\",\n            \"addressNumber\": \"300\",\n            \"addressComplement\": \"SL\",\n            \"addressNeighborhood\": \"Botafogo\",\n            \"addressCity\": \"Rio de Janeiro\",\n            \"postalCode\": \"22250040\",\n            \"state\": \"RJ\",\n            \"phoneAreaCode\": \"21\",\n            \"phoneNumber\": \"999999999\"\n        },\n        \"invoiceOrderOfService\": \"123456\",\n        \"invoiceOrderOfServiceSerie\": \"2\",\n        \"orderNumber\": \"987654321\"\n    },\n    {\n        \"deliveryServiceType\": \"Entrega\",\n        \"shipperCustomer\": {\n            \"legalType\": \"PF\",\n            \"firstName\": \"Pedro\",\n            \"lastName\": \"Silva\",\n            \"cpf\": \"90498365778\",\n            \"addressStreet\": \"Rua Praia de Botafogo\",\n            \"addressNumber\": \"300\",\n            \"addressComplement\": \"SL\",\n            \"addressNeighborhood\": \"Botafogo\",\n            \"addressCity\": \"Rio de Janeiro\",\n            \"postalCode\": \"22250040\",\n            \"state\": \"RJ\",\n            \"phoneAreaCode\": \"21\",\n            \"phoneNumber\": \"999999999\"\n        },\n        \"invoiceOrderOfService\": \"123457\",\n        \"invoiceOrderOfServiceSerie\": \"2\",\n        \"orderNumber\": \"987654322\"\n    }\n]",
      "language": "text",
      "name": "Request body example"
    }
  ]
}
[/block]