---
title: "useExtension hook"
slug: "useextension-hook"
hidden: true
createdAt: "2026-03-11T17:08:52.219Z"
updatedAt: "2026-03-11T17:08:52.219Z"
excerpt: ""
---

> ⚠️ This feature is only available for stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available to selected accounts.

The `useExtension` hook allows you to access information about the current account and the extension point in which your extension is running.

## Usage

```js
import { useExtension } from '@vtex/checkout';

const ExtensionInfo = () => {
  const { account, extensionPoint } = useExtension();

  return (
    <div>
      <p>Account: {account}</p>
      <p>Extension Point: {extensionPoint}</p>
    </div>
  );
};
```

## Parameters

The `useExtension` hook does not accept any parameters.

## Returns

The `useExtension` hook returns an object with the following properties:

### account

- `account: string`

The current account name where the extension is running.

### extensionPoint

- `extensionPoint: ExtensionPoints`

The name of the extension point where your extension is hooked into.

### orderFormId

- `orderFormId: string`

The `orderFormId` for the active cart in Checkout.

## Extension Points

This hook is available across all [Checkout extension points](https://developers.vtex.com/docs/guides/checkout-extension-points).
