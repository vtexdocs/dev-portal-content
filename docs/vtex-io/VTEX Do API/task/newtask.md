---
title: "Create Task"
slug: "newtask"
excerpt: "Creates a new task in VTEX Do."
hidden: false
createdAt: "2019-12-30T19:34:01.284Z"
updatedAt: "2020-03-02T15:02:24.456Z"
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
      "code": "curl --location --request POST 'https://{{accountName}}.{{environment}}.com.br/api/do/tasks' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}' \\\n--data-raw '{\n \"target\": [{\n   \"id\": \"633730670642-01\",\n   \"type\": \"order\",\n   \"url\": \"https://recorrenciaqa.vtexcommercebeta.com.br/admin/checkout/orders/633730670642-01\"\n }],\n \"domain\":\"oms\",\n \"context\":\"Marketplace\",\n \"name\": \"pricing\",\n \"priority\":\"Critical\",\n \"surrogateKey\":\"505224-0\",\n \"description\": \"Ajudar na doc API para lancar no postman\",\n \"dueDate\": \"2016-03-01\",\n \"assignee\": {\n   \"id\": null,\n   \"name\": null ,\n   \"email\": \"frederico.santos@vtex.com.br\"\n },\n \"followers\": [\n   {\n     \"id\": null,\n     \"name\": null,\n     \"email\": \"alan.dantas@vtex.com.br\"\n   }\n ],\n \"parentTaskId\": null\n}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]