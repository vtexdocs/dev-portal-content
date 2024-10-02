---
title: "4. Writing the head and body scripts"
slug: "vtex-io-documentation-5-writingtheheaderandbodyscripts"
hidden: false
category: "App Development"
seeAlso:
- "/docs/guides/vtex-io-documentation-6-listeningtostoreevents"
createdAt: "2020-11-03T18:19:23.999Z"
updatedAt: "2022-12-13T20:17:44.369Z"
---

Now, it is time to define the scripts that your Pixel app will run on the store website. You can specify scripts that execute inside the `<head>` and/or `<body>` tags.

Adding a script to the `<head>` ensures that it will be executed before any other HTML element is rendered on the page. Although this may affect store performance, it is a good option if your Pixel app relies on the interaction between users and store components. On the other hand, adding a script to the store `<body>` tag will probably reduce the impact on performance scores. However, this may come at the cost of losing user data. Choose wisely based on the functionality of your Pixel app.

## Instructions

1. Open the `pixel/head.html` file and replace the provided function with your own.

    > ℹ️ If you choose to execute your script inside the `<body>` tag, rename the `head.html` file to `body.html`.

2. Use the `settingsSchema` identification key previously defined where applicable. See the following example:

    ```html
    <script>
      // Using via JavaScript
      var appId = "{{settings.gtmId}}";
    </script>
    
    <!-- Using directly in an HTML tag -->
    <script src="//foobar.com?gtmId={{settings.gtmId}}"></script>
    ```
