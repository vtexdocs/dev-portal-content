---
title: "useSettings hook"
slug: "usesettings-hook"
hidden: true
createdAt: "2026-03-11T17:08:52.219Z"
updatedAt: "2026-03-11T17:08:52.219Z"
excerpt: ""
---

> ⚠️ This feature is only available for stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available to selected accounts.

The `useSettings` hook provides access to various Checkout settings, such as branding data like logos and colors. These settings can be used to customize different aspects of your Checkout extensions, enabling more flexibility and personalization in the user experience.

## Usage

```js
import { useSettings } from '@vtex/checkout';

const CustomFooter = () => {
  const { branding } = useSettings();

  return (
    <footer>
      <img width={72} src={branding.logo} alt="Store Logo" />
      <p>© 2024 Store A Inc. All Rights Reserved.</p>
    </footer>
  );
};
```

## Parameters

The `useSettings` hook does not accept any parameters.

## Returns

The `useSettings` hook returns an object with the following field:

### branding

- `branding: Branding`

The `Branding` type is an object with the following structure:

```js
type Branding = {
   color?: string;
   logo?: string;
};
```

## Extension Points

This hook is available across all [Checkout extension points](https://developers.vtex.com/docs/guides/checkout-extension-points).
