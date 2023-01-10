The orderForm is the main object processed by VTEX checkout, and one of the most important data structures in the architecture of every VTEX store. It stores a lot of contextual information about the order which is important to the processing of the order: order items, client's personal data, delivery address, freight information, among others.

This guide will describe how to remove all messages from the `messages` field of the orderForm, leaving it empty.

# Removing all messages from the orderForm message field

To remove all messages from the orderForm `messages` field of the shopping cart, you need to use the [Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages) endpoint. The `orderFormId` information of the shopping cart must be sent through the URL request, as shown by the example below:

`https://{accountname}.{environment.com.br}/api/checkout/pub/orderForm/ede846222cd44046ba6c638442c3505a/messages/clear`

Additionally, you need to send the request body containing only two curly brackets, as shown below:

```json
{
  "codes": [
    {
      "code": "{}",
      "language": "json"
    }
  ]
}

After sending the request, the endpoint will return the response body containing the shopping cart information and the `messages` field empty, as shown in the example below:

```json
{
  "codes": [
    {
      "code": "{...\n\"messages\": [],\n...}",
      "language": "json"
    }
  ]
}

>ℹ️ For more information about the meaning of each of the fields available in the shopping cart, access the [orderForm](https://developers.vtex.com/vtex-rest-api/reference/orderform-fields) overview.

## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example (code 001)**: `"Bad Request"`. This message indicates that information other than `{}` was sent in the request body.

```json
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"001\",\n        \"message\": \"Bad request\",\n        \"exception\": null\n    },\n    \"operationId\": \"91b68251-1a60-4716-b846-c7c9c31fa565\"\n}",
      "language": "json"
    }
  ]
}

- **Message error example (code ORD002)**: `"Carrinho inválido"` (*Invalid Cart*). This message indicates that the `orderFormId` used in the request does not exist or is incorrect.

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"fields\": {},\n    \"error\": {\n        \"code\": \"ORD002\",\n        \"message\": \"Carrinho inválido\",\n        \"exception\": null\n    },\n    \"operationId\": \"5d37a185-bfe6-4686-9d92-aac9482cc63d\"\n}",
      "language": "json"
    }
  ]
}
[/block]

### 404 - Not Found

- **Message error example**: `"The requested URL was not found on the server"`: check that the URL data is correct.

[block:code]
{
  "codes": [
    {
      "code": "<body>\n\t<h1>404 Not Found</h1>\n\t<p>The requested URL was not found on this server.</p>\n</body>",
      "language": "json"
    }
  ]
}
[/block]