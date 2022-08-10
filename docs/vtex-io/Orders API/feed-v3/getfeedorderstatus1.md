---
title: "Retrieve feed order status"
slug: "getfeedorderstatus1"
excerpt: "Lists feed order events."
hidden: false
createdAt: "2019-12-11T00:42:27.604Z"
updatedAt: "2020-08-26T22:21:47.619Z"
---
Learn more about [Feed v3 in VTEX Help](https://help.vtex.com/pt/tutorial/feed-v3-de-gerenciamento-de-pedidos)

## Request has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `accountName` | string | Account Name |
| `maxLot` | integer |  Lot quantity, maximum accept value is 10 |

## Response object has the following properties:

| Attribute    | Type        | Description |
| --------------- |:---------:| --------------------------------------:|
| `eventId` | string | Feed event ID |
| `handle` | string |  Event handle, used in Confirm Item Feed |
| `domain` | integer |  Order Source |
| `state` | integer |  Feed event state |
| `orderId` | string |  Order ID |
| `lastChange` | date |  Date for last change |
| `currentChange` | date | Date of change of current status|

The event will be removed if the message "send retry" is equal to, or greater than the maximum retention period.
[block:callout]
{
  "type": "warning",
  "body": "This API will return **404 Not Found** if there is no Feed Configuration available for the given X-VTEX-API-AppKey.",
  "title": "Feed Configuration is required"
}
[/block]

[block:api-header]
{
  "title": "Request body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl --location --request GET 'https://{{accountName}}.vtexcommercestable.com/api/orders/feed?maxlot=10' \\\n--header 'Accept: application/json' \\\n--header 'Content-Type: application/json' \\\n--header 'X-VTEX-API-AppToken: {{X-VTEX-API-AppToken}}' \\\n--header 'X-VTEX-API-AppKey: {{X-VTEX-API-AppKey}}'",
      "language": "text",
      "name": "Request example"
    }
  ]
}
[/block]

[block:api-header]
{
  "title": "Response body example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "[\n  {\n    \"eventId\": \"ED423DDED4C1AE580CADAC1A4D02DA3F\",\n    \"handle\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoidnRleGFwcGtleS1wYXJ0bmVyc2xhdGFtLVJNQkpNUyIsIkFwcEtleSI6InZ0ZXhhcHBrZXktcGFydG5lcnNsYXRhbS1STUJKTVMiLCJBY2NvdW50IjoicGFydG5lcnNsYXRhbSIsIkhhbmRsZSI6IkFRRUIzbmtWR0piOXhhNGRjYlpkOTFVVWMyL2JObHc0Qnp3ZlNLV201Rjg2QXgrSGlRM053bEJkb2NwM2wvVytLdjFNQTZ4d3ZLcFYwYjlSeUttNVRpb3hrSVFMSG1Uck9xenB2aFlwU29uMzRrVmlNaWZHY2lnZFFqalBJdk00eWU4amVuaS9QKytaTmVxOFZWeFNGay81Yzg3YS84MTRjTFg2WGZPR2x2WitlTnVjTzA3S3UxK0xXaU5vQmJEY0cycGxKekxkRks3Qld3b1NTV3BmSWhrOGhmSFNkSzlzZVpJeG01QXFLbHFrUHNDNGk5emVaYVpBUVVrSi9aZWo3UjRrRDVRaXFjNmpjcnFheEdHc1lsNHMzUWM0ZmtWdmhYblJVQ2l2ZGdpMEtUYS8zcXlWWU9QTktIV2huTlZxMEZHNDNjME4vaWh6dDc0d1laNVl6aDFJRitHU2t1YTkrN1pCdnQ2VGs1cFRhZmVVclk0ckNPL2Fobnl1eXFLOG53ZkorVWxUTmt2ZVNFS29FdTNiUWQzSmc5R1lYWHlXOVVxRGo5dHJIZ1N5M3ZZa0dBWjd0MDZNZWUwQnBsdFBxWExaIiwiT3JkZXJJZCI6Ijk1MzcxMjAwNDEyNi0wMSIsIk1lc3NhZ2VJZCI6ImI5YjI4NDkwLTNjNzAtNDdjNi1hMTE3LWNhN2FjMTk2MDY1OSIsIkRvbWFpbiI6IkZ1bGZpbGxtZW50IiwiU3RhdGUiOiJyZWFkeS1mb3ItaGFuZGxpbmciLCJMYXN0U3RhdGUiOiJ3aW5kb3ctdG8tY2FuY2VsIiwiTGFzdENoYW5nZSI6IjA4LzEyLzIwMTkgMjA6NTQ6MDEiLCJDdXJyZW50Q2hhbmdlIjoiMDgvMTIvMjAxOSAyMDo1NDoyMyIsIkNyZWF0ZWRBdCI6IjA4LzEyLzIwMTkgMjE6MDE6MzAiLCJpc3MiOiJicm9hZGNhc3QtYXBpLnZ0ZXhjb21tZXJjZS5jb20uYnIiLCJhdWQiOiJwYXJ0bmVyc2xhdGFtX3Z0ZXhhcHBrZXktcGFydG5lcnNsYXRhbS1STUJKTVMifQ.7RQBZQb6pHhFhA_jMKTiSoJbDck7awgD3Xx7sdJcW6w\",\n    \"domain\": \"Fulfillment\",\n    \"state\": \"ready-for-handling\",\n    \"lastState\": \"window-to-cancel\",\n    \"orderId\": \"953712004126-01\",\n    \"lastChange\": \"2019-08-12T20:54:01.134057Z\",\n    \"currentChange\": \"2019-08-12T20:54:23.7153839Z\"\n  }\n]",
      "language": "text",
      "name": "200 - OK"
    },
    {
      "code": "//Please check your Feed Configuration.",
      "language": "text",
      "name": "404 - Not Found"
    }
  ]
}
[/block]