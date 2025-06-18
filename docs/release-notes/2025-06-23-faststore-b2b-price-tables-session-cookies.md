---
title: "FastStore: Supports B2B Price Tables and personalized promotions"
slug: "2025-06-23-faststore-b2b-price-tables-session-cookies"
hidden: false
type: "improved"
createdAt: "2025-06-23T00:00:00.219Z"
updatedAt: "2025-06-23T00:00:00.219Z"
excerpt: "FastStore now enables B2B customer-specific pricing and promotions by automatically forwarding session cookies to Intelligent Search, ensuring personalized experiences for customers."
---

FastStore storefronts now integrate with [Price Tables](https://help.vtex.com/en/tutorial/creating-price-tables--58YmY2Iwggyw4WeSCGg24S) for B2B and [Intelligent Search](https://help.vtex.com/en/tutorial/intelligent-search-overview--5o8ixTpYIxx3uJD0B1xp3z?&utm_source=autocomplete), allowing B2B sellers to:

- Display custom prices by customer segment.
- Deliver targeted promotions based on store session context.
- Implement advanced pricing strategies with minimal configuration.

## What has changed?

Previously, FastStore did not forward session cookies (like `vtex_segment`) to Intelligent Search, preventing the system from applying the correct price table and trade policy for B2B clients. As a result, B2B clients were restricted to default pricing, regardless of their negotiated agreements.

FastStore now includes session cookies (like `vtex_segment`) in HTTP requests to Intelligent Search APIs via the `Cookie` header. This improvement allows Intelligent Search to apply the appropriate trade policy for each client, instead of returning prices from the default trade policy. This integration between Intelligent Search and FastStore also serves cluster-based promotions, enabling personalized discounts. This change ensures B2B customers receive accurate, customer-specific pricing and promotions, improving their shopping experience.

## What needs to be done?

To enable B2B price tables with cookie forwarding, first update your FastStore project to version `3.29.1` or higher. To do this, follow these steps:

1. Open your project in a code editor.
2. Open a terminal and run the following command to update the FastStore packages to the latest version:

    ```bash
    yarn upgrade -L --scope @faststore
    ```

No further configuration is required. Cookie forwarding is automatic once you upgrade your project version. To test if the cookies are being forwarded, you can do the following:

1. In the terminal, run `yarn dev`.
2. Access the localhost using the browser, and search for a product in the store.
3. Open your browser's Developer Tools and go to the **Application** tab.
4. Under the **Storage** section, open the **Cookies** menu, click the URL, and check the cookies being forwarded, including the `vtex_segment` cookie.

![b2b-cookies](https://vtexhelp.vtexassets.com/assets/docs/src/b2b-events___70e69c8494f863d0c6a59929349b3d34.gif)

> ℹ️ For more information about configuring B2B price tables, see the [Price tables documentation](https://help.vtex.com/en/tutorial/creating-price-tables--58YmY2Iwggyw4WeSCGg24S).
