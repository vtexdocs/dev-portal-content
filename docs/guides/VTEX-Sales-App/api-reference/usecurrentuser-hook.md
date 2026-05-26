---
title: "useCurrentUser hook"
slug: "usecurrentuser-hook"
hidden: false
createdAt: "2026-05-26T00:00:00.000Z"
---

The `useCurrentUser` hook allows you to access current authenticated user data like name and email.

This hook is available in the following extension point:

* `menu.drawer-content`

See all available extension points in the guide [VTEX Sales App extension points](https://developers.vtex.com/docs/guides/vtex-sales-app-extension-points).

## Usage

```typescript src/index.tsx
import { useCurrentUser } from '@vtex/sales-app'

const CurrentUser = () => {
  const { name, email } = useCurrentUser()

  return <div>Current User: {name} - {email}</div>
}
```

## Parameters

The `useCurrentUser` hook does'nt accept any parameters.

## Returns

The `useCurrentUser` hook returns an object with the following properties:

### `name`

* **type:** `string`

### `email`

* **type:** `string`
