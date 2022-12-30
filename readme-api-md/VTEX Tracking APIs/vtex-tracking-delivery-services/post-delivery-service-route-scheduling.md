---
title: "Post Delivery Service With Route Scheduling"
slug: "post-delivery-service-route-scheduling"
excerpt: "Creates a delivery service in your Tracking system. It allows the user to configure the Route Scheduling services, with the Delivery Person and Route date already defined."
hidden: false
createdAt: "2020-07-03T16:01:11.744Z"
updatedAt: "2020-09-21T18:13:57.481Z"
---
[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "[\n\t{\n\t\t\"deliveryServiceRoute\": {\n\t\t\t\"deliveryServiceDate\": \"2020-09-28\",\n\t\t\t\"displacementType\": \"Caminhão\",\n\t\t\t\"carrier\": {\n\t\t\t\t\"username\": \"empresa-joao.silva\"\n\t\t\t},\n\t\t\t\"vehicle\": {\n\t\t\t\t\"registrationPlate\": \"XPT-0123\"\n\t\t\t},\n\t\t\t\"addressStart\": {\n\t\t\t\t\"addressStreet\": \"Avenida das Américas\",\n\t\t\t\t\"addressNumber\": \"5000\",\n\t\t\t\t\"addressCity\": \"Rio de Janeiro\",\n\t\t\t\t\"postalCode\": \"22640102\",\n\t\t\t\t\"state\": \"RJ\"\n\t\t\t}\n\t\t},\n\t\t\"deliveryService\": [\n\t\t\t{\n\t\t\t\t\"deliveryServiceType\": \"Entrega\",\n\t\t\t\t\"shipperCustomer\": {\n\t\t\t\t\t\"legalType\": \"PJ\",\n\t\t\t\t\t\"companyName\": \"COMP. BRAS. DE TECN. PARA E-COMMERCE\",\n\t\t\t\t\t\"cnpj\": \"05314972000174\",\n\t\t\t\t\t\"addressStreet\": \"Rua Praia de Botafogo\",\n\t\t\t\t\t\"addressNumber\": \"300\",\n\t\t\t\t\t\"addressComplement\": \"SL\",\n\t\t\t\t\t\"addressNeighborhood\": \"Botafogo\",\n\t\t\t\t\t\"addressCity\": \"Rio de Janeiro\",\n\t\t\t\t\t\"postalCode\": \"22250040\",\n\t\t\t\t\t\"state\": \"RJ\",\n\t\t\t\t\t\"phoneAreaCode\": \"21\",\n\t\t\t\t\t\"phoneNumber\": \"999999999\"\n\t\t\t\t},\n\t\t\t\t\"invoiceOrderOfService\": \"123456\",\n\t\t\t\t\"invoiceOrderOfServiceSerie\": \"2\",\n\t\t\t\t\"orderNumber\": \"987654321\"\n\t\t\t},\n\t\t\t{\n\t\t\t\t\"deliveryServiceType\": \"Entrega\",\n\t\t\t\t\"shipperCustomer\": {\n\t\t\t\t\t\"legalType\": \"PF\",\n\t\t\t\t\t\"firstName\": \"Pedro\",\n\t\t\t\t\t\"lastName\": \"Silva\",\n\t\t\t\t\t\"cpf\": \"90498365778\",\n\t\t\t\t\t\"addressStreet\": \"Rua Praia de Botafogo\",\n\t\t\t\t\t\"addressNumber\": \"300\",\n\t\t\t\t\t\"addressComplement\": \"SL\",\n\t\t\t\t\t\"addressNeighborhood\": \"Botafogo\",\n\t\t\t\t\t\"addressCity\": \"Rio de Janeiro\",\n\t\t\t\t\t\"postalCode\": \"22250040\",\n\t\t\t\t\t\"state\": \"RJ\",\n\t\t\t\t\t\"phoneAreaCode\": \"21\",\n\t\t\t\t\t\"phoneNumber\": \"999999999\"\n\t\t\t\t},\n\t\t\t\t\"invoiceOrderOfService\": \"123457\",\n\t\t\t\t\"invoiceOrderOfServiceSerie\": \"2\",\n\t\t\t\t\"orderNumber\": \"987654322\"\n\t\t\t}\n\t\t]\n\t}\n]",
      "language": "text",
      "name": "Request body example"
    }
  ]
}
[/block]