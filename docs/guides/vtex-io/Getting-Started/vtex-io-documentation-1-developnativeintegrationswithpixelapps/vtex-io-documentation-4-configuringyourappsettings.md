---
title: "3. Configuring your app settings"
slug: "vtex-io-documentation-4-configuringyourappsettings"
hidden: false
category: "App Development"
seeAlso:
  - "/docs/guides/vtex-io-documentation-5-writingtheheaderandbodyscripts"
createdAt: "2020-11-03T18:19:23.222Z"
updatedAt: "2022-12-13T20:17:44.408Z"
---

When developing a Pixel app, you must define a way to identify if a VTEX account has the necessary permissions to communicate with the third-party solution in question. Otherwise, sharing data between the store and the solution will not be possible.

This verification is generally performed via a user identification issued by the third-party solution. The user identification is an individual and nontransferable value that identifies if you have the required permissions to use that solution. Think of the Google Tag Manager Pixel app — you must provide a previously issued user identification, in order to use it.

In the following steps, you will learn how to make your Pixel app read the user identification and determine if a user is allowed.

## Instructions

1. Open the `manifest.json` file.
2. Change the `vendor` field value (`vtex`) to the name of the VTEX account in which you are working.
3. Change the `name` and `title` field values with the name you want to give your app. Please see our [app naming guidelines](https://developers.vtex.com/docs/guides/vtex-io-documentation-filling-the-application-form-for-development/#guidelines).
4. Declare the `settingsSchema` field. This field will be used to receive the user identification information.
5. Inside the `settingsSchema` object, declare a JSON Schema containing the following fields:

- `title` - Pixel app name.
- `type` - JSON Schema type (this must always be completed as `object`).
- `description` *(Optional)*  - Description of the `settingsSchema` field.
- `properties` - Key-value pairs that define the user identification. Possible keys for `properties` are: `title` (user identification title), `description` (user identification description), and `type` (property type to define how users should input their identification). Note that these keys will be displayed to the app users.

```json
"settingsSchema": {
  "title": "YOUR APP NAME",
  "type": "object",
  "properties": {
    "gtmId": {
      "title": "SAMPLE FIELD",
      "description": "Enter your Google Tag Manager ID (GTM-XXXX)",
      "type": "string"
    }
  }
},
```

If necessary, you can also use the `properties` object to read the user preferences. Check the following example:

```json
"settingsSchema": {
  "title": "YOUR APP NAME",
  "type": "object",
  "properties": {
    "gtmId": {
      "title": "SAMPLE FIELD",
      "description": "Enter your Google Tag Manager ID (GTM-XXXX)",
      "type": "string"
    },
    "allowCustomHtmlTags": {
        "title": "Allow custom HTML tags",
        "description": "Keep in mind that using custom HTML tags can drastically impact store performance",
        "type": "boolean"
    }
  }
},
```

> ℹ️ Please read the [JSON Schema documentation](http://json-schema.org/understanding-json-schema/) while building the `settingSchema` field of your app.
