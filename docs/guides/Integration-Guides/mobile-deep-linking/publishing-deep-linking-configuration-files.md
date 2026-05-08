---
title: "Publishing deep linking configuration files"
slug: "publishing-deep-linking-configuration-files"
hidden: false
excerpt: "Learn how to publish apple-app-site-association and assetlinks.json files in the /.well-known/ path for Universal Links and App Links."
createdAt: "2026-03-31T12:00:00.000Z"
updatedAt: "2026-04-13T12:00:00.000Z"
---

This guide describes how to publish the files required by Apple and Google in the **/.well-known/** path of your store's public domain using the VTEX API.

These special files are used to enable specific deep linking behaviors. In the Apple ecosystem (iOS), the feature is called Universal Links and uses the **apple-app-site-association** file. In the Google ecosystem (Android), the feature is called App Links and uses the **assetlinks.json** file. Despite their distinct names, both serve the same purpose: allowing an application to open directly instead of a web browser.

Once published, the files are accessible at the standard **/.well-known/{filename}** routes, as expected for this type of implementation:

* **Android — assetlinks.json**

  Route: `https://{{www.yourstore.com}}/.well-known/assetlinks.json`

* **iOS — apple-app-site-association**

  Route: `https://{{www.yourstore.com}}/.well-known/apple-app-site-association`

## Before you begin

Before getting started, ensure that:

* Your **public domain** is already correctly pointing to VTEX, for example:
  `https://www.yourstore.com`
* You have a valid [API key and API token](https://developers.vtex.com/docs/guides/api-authentication-using-api-keys) for your VTEX account with permission.
* You have the file provided by Apple or Google without any content modifications.

Always use HTTPS and the exact domain that will be configured with Apple or Google (including `www.` when applicable).

## iOS – Universal Links (apple-app-site-association)

The `apple-app-site-association` file is used for **Universal Links** (deep links on iOS).

### Example file

The file provided by Apple should be named `apple-app-site-association` (without extension) and contain valid JSON content similar to this:

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appIDs": ["TEAMID.com.yourcompany.app"],
        "paths": ["/", "/product/*"]
      }
    ]
  }
}
```

* `TEAMID.com.yourcompany.app` should contain your iOS app's Team ID + Bundle ID.
* `paths` must cover the URLs that should open the app.

>ℹ️ Use the file provided by Apple without modifications. The example above is for reference only to help you understand the expected format.

### Upload via cURL

The request body must be raw JSON (the same text as in your configuration file), with `Content-Type: application/json`.

```shell
curl --location --request POST \
  'https://www.yourstore.com/.well-known/raw/apple-app-site-association?persistent=true' \
  --header 'X-VTEX-API-AppKey: {YOUR_API_KEY}' \
  --header 'X-VTEX-API-AppToken: {YOUR_API_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data 'YOUR_JSON_FILE_CONTENT_HERE'
```

Replace `YOUR_JSON_FILE_CONTENT_HERE` with the exact JSON from your `apple-app-site-association` file (a single JSON object), pasted as the raw body.

The `?persistent=true` parameter indicates that the file should remain stored permanently.

### Endpoint validation

```shell
curl -i 'https://www.yourstore.com/.well-known/apple-app-site-association'
```

Verify that:

* The HTTP status is **200 OK**.
* The header includes `Content-Type: application/json`.
* There are no redirects (direct 200 response).
* The body contains the expected JSON.

## Android – App Links (assetlinks.json)

The `assetlinks.json` file is used for **Android App Links**, allowing you to associate the domain with your Android app.

### Example file

The file provided by Google should be named `assetlinks.json` and contain valid JSON content similar to this:

```json
[
  {
    "relation": ["delegate_permission/common.handle_all_urls"],
    "target": {
      "namespace": "android_app",
      "package_name": "com.yourcompany.app",
      "sha256_cert_fingerprints": [
        "AA:BB:CC:DD:EE:FF:..."
      ]
    }
  }
]
```

The `package_name` and `sha256_cert_fingerprints` values must contain your Android app's values.

>ℹ️ Use the file provided by Google without modifications. The example above is for reference only to help you understand the expected format.

### Upload via cURL

The request body must be raw JSON (the same text as in your `assetlinks.json` file), with `Content-Type: application/json`.

```shell
curl --location --request POST \
  'https://www.yourstore.com/.well-known/raw/assetlinks.json?persistent=true' \
  --header 'X-VTEX-API-AppKey: {YOUR_API_KEY}' \
  --header 'X-VTEX-API-AppToken: {YOUR_API_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data 'YOUR_JSON_FILE_CONTENT_HERE'
```

Replace `YOUR_JSON_FILE_CONTENT_HERE` with the exact JSON from your `assetlinks.json` file, pasted as the raw body.

The `?persistent=true` parameter indicates that the file should remain stored permanently.

### Endpoint validation

```shell
curl -i 'https://www.yourstore.com/.well-known/assetlinks.json'
```

Verify that:

* The HTTP status is **200 OK**.
* The header includes `Content-Type: application/json`.
* The body contains the expected JSON.
* There are no redirects in the response.

## Updating configuration files

To update any configuration file (for example, due to changes in Bundle ID, Team ID, certificate renewal, or path modifications), use the same `POST` request to `/.well-known/raw/{filename}?persistent=true` with the updated JSON in the request body, as described above.

The previous content will be automatically overwritten. For example, to update the iOS Universal Links configuration:

```shell
curl --location --request POST \
  'https://www.yourstore.com/.well-known/raw/apple-app-site-association?persistent=true' \
  --header 'X-VTEX-API-AppKey: {YOUR_API_KEY}' \
  --header 'X-VTEX-API-AppToken: {YOUR_API_TOKEN}' \
  --header 'Content-Type: application/json' \
  --data 'YOUR_JSON_FILE_CONTENT_HERE'
```

After updating, validate the endpoint using `GET` to confirm the new content is published correctly:

```shell
curl -i 'https://www.yourstore.com/.well-known/apple-app-site-association'
```

>⚠️ The `POST` method is the only supported way to publish or update these configuration files.
