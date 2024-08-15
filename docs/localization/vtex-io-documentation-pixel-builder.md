---
title: "Pixel builder"
slug: "vtex-io-documentation-pixel-builder"
hidden: false
createdAt: "2024-08-15T14:00:00.000Z"
updatedAt: ""
excerpt: "Learn how to use the VTEX IO Pixel builder."
---

The `pixel` builder allows the implementation of JavaScript scripts in HTML files. The scripts run in the header or body of every store page and can collect user data, respond to events, and connect with third-party services.

For details about creating Pixel apps, see the [Pixel apps tutorial](https://developers.vtex.com/docs/guides/vtex-io-documentation-1-developnativeintegrationswithpixelapps). Find examples of available apps using this builder in the [Pixel Apps section](https://developers.vtex.com/docs/guides/pixel-apps).

## Folder structure

The `pixel` builder uses a folder named `pixel` located in the app’s root folder.

```txt
pixel
 ┣ 📄body.html
 ┗ 📄header.html
```

- `body.html`: HTML file with the script that will run in the body of the store pages. Scripts running in the body can have a better performance, but some events might be missed, since the execution takes place while HTML elements are rendered.
- `header.html`: HTML file with the script that will run in the header of the store pages. Running scripts in the head can have a higher impact on performance, but ensures the detection of all events, since the execution takes place before HTML elements are rendered.

## Usage

1. **Start with a template:** Download the [pixel-app-template](https://github.com/vtex-apps/pixel-app-template/).
2. **Add the app settings in the manifest:** Open the `manifest.json` file in the app’s root folder and add the settings necessary to work with your script in the `settingsSchema` object. For instance, you can add a field to insert a Google Tag Manager ID. For more details, see [Creating an interface for your app settings](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-an-interface-for-your-app-settings).
3. **Implement the script:** Insert the script code in the `header.html` file or `body.html` file, depending on the desired implementation. The script will run in every page of the store. The choice of execution between header and body is a trade-off of page performance against ensurance of event detection and user data gathering. Below is an example of script.

```html
<script>
  (function() {
    var appId = "{{settings.gtmId}}";

    // Add script here
  })()
</script>
```

4. **Add scripts in specific pages or components (optional):** Besides running scripts with the `pixel` builder, you can add scripts in specific pages and components using React. You can see an example in the [Pixel apps tutorial](https://developers.vtex.com/docs/guides/vtex-io-documentation-6-listeningtostoreevents). For the definition of the available events, see the [pixel-app-template](https://github.com/vtex-apps/pixel-app-template/blob/master/react/typings/events.d.ts) repository.
5. **Testing:** [Link the app](https://developers.vtex.com/docs/guides/vtex-io-documentation-linking-an-app) to a development workspace for testing, then access the store in the development workspace to see the script in action. The url to access the store in the development workspace uses the format `{workspace}--{accountName}.myvtex.com`, where `{workspace}` is your workspace and `{accountName}` is your account name. You may need to perform the programmed actions to trigger the events set in your script, such as adding a product in the shopping cart.
