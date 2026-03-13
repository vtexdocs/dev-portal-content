---
title: "useRedirect hook"
slug: "useredirect-hook"
hidden: true
createdAt: "2026-03-11T17:08:52.219Z"
updatedAt: "2026-03-11T17:08:52.219Z"
except: ""
---

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

This hook is available in the following extension point:

- `punchout.order-summary.cta`
