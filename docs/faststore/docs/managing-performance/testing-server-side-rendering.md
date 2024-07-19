---
title: "Testing server-side rendering"
---

JavaScript handles data fetching, templating, and routing on the client-side rather than on the server-side. However, the amount of JavaScript shipped to the browser tends to increase as the complexity of an application grows. As a result, JavaScript code competes for processing power and delays the rendering task because it keeps trying to be processed before the browser finishes rendering the page content.

To ensure your server-side rendering (SSR) HTML is functional and free of bugs, it is important to check how your web page looks and behaves when JavaScript is disabled.

## Instructions

1. Check the documentation of your web browser and search for how to disable JavaScript. For example, if you are using Google Chrome, check Google's documentation on [Disabling JavaScript](https://developers.google.com/web/tools/chrome-devtools/javascript/disable).

2. Access your store website and check if its [core features](https://developers.vtex.com/docs/guides/getting-started#vtex-core-services), such as product searching, shopping cart, and checkout process are working as expected. Your store will not function exactly as planned, but check below which are the expected and undesired behaviors when disabling JavaScript:

    - **Undesired behaviors**
        - The page does not render anything.
        - Instead of updating only the different content, the page is fully refreshed when navigating to another page.
        - Misplaced layout.

    - **Expected behaviors**
        - Simpler design, displaying basic layout similar to a static webpage.
        - Animations and interactive menus do not work.
        - The below-the-fold content does not render.
