---
title: "useExtension hook"
slug: "useextension-hook"
hidden: false
createdAt: "2026-05-26T00:00:00.000Z"
---

The `useExtension` hook allows you to access information about the current account and the extension point in which your extension is running.

This hook is available for all extension points. See the full list in the guide [VTEX Sales App extension points](https://developers.vtex.com/docs/guides/vtex-sales-app-extension-points).

## Usage

```typescript
import { useExtension } from '@vtex/sales-app';

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

The `useExtension` hook doesn't apply any parameters.

## Returns

The `useExtension` hook returns an object with the following structure:

### `account`

* **type:** `string`
* **description:** The current account name where the extension is running.

### `extensionPoint`

* **type:** [`ExtensionPointsType`](./extension-points)
* **description:** The name of extension point where your extension is hooked into.
