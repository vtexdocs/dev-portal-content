---
title: "My store translation is not behaving as expected"
slug: "my-store-translation-is-not-behaving-as-expected"
excerpt: "My store is being translated when it shouldn't."
hidden: false
createdAt: "2025-01-30T14:25:00.00Z"
updatedAt: "2025-01-30T14:25:00.00Z"
tags:
    - translation
---

**Keywords:** Translation

If your store translation is not behaving as expected, follow the instructions below.

## Checking the default locale

Access the API `GET http://portal.vtexcommercestable.com.br/api/tenant/tenants?q={accountName}` and check the `defaultLocale` property.

>ℹ️ Replace the `{accountName}` with your VTEX account name.

If the `defaultLocale` value doesn't match your store locale, [open a support ticket](https://support.vtex.com/hc/en-us/requests) to report the issue.
