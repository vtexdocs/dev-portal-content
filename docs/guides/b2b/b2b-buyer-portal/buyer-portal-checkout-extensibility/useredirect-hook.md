---
title: "useRedirect hook"
slug: "useredirect-hook"
hidden: true
createdAt: "2026-03-11T17:08:52.219Z"
updatedAt: "2026-03-11T17:08:52.219Z"
excerpt: "Learn how to use the useRedirect hook to programmatically redirect users to different pages in your Checkout extension."
---

> ⚠️ This feature is only available for stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available to selected accounts.

The `useRedirect` hook allows an extension to redirect the user to another page.

> ℹ️ This hook is only available in some extension points.

## Usage

```js
const CustomButton = () => {
  const { redirect } = useRedirect();

  const handleClick = () => {
    redirect("https://www.example.com");
  };

  return (
    <button onClick={handleClick}>
      My Button
    </button>
  );
};
```

## Parameters

The `useRedirect` hook does not accept any parameters.

## Returns

The `useRedirect` hook returns an object with the following property:

- `redirect: (url: string) => Promise<void>`

The `url` is the destination URL. It must be a complete URL, such as `https://www.example.com`.

## Extension Points

This hook is available in the following [Checkout extension point](https://developers.vtex.com/docs/guides/checkout-extension-points):

- `punchout.order-summary.cta`
