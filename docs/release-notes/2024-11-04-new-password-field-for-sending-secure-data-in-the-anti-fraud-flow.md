---
title: "New password field for sending secure data in the anti-fraud flow"
slug: "2024-11-04-new-password-field-for-sending-secure-data-in-the-anti-fraud-flow"
type: "added"
excerpt: "The `password` field type has been added to the `customFields` array."
createdAt: "2024-11-04T00:00:00.000Z"
updatedAt: "2024-11-04T00:00:00.000Z"
---
Anti-fraud providers integrated with VTEX can now use a new custom field to send sensitive or security information in payment transactions processed through the VTEX gateway.

## What has changed?

The `password` type custom field was created within the framework of the [Anti-fraud Provider Protocol](https://developers.vtex.com/docs/guides/how-the-integration-protocol-between-vtex-and-antifraud-companies-works) and can be used to transmit confidential information.

See an example of a response body from the [List anti-fraud provider manifest endpoint containing](https://developers.vtex.com/docs/api-reference/antifraud-provider-protocol#get-/manifest) this new field:

```json
{
  …
  "customFields": [
   {
      "name": "Client secret",
      "type": "password"
    },
  …
  ]
}
```

## What needs to be done?

No action is required. You can now configure the `password` type custom field in your anti-fraud provider's manifest.
