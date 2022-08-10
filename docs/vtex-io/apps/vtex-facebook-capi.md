---
title: "Facebook Conversions Api"
slug: "vtex-facebook-capi"
excerpt: "vtex.facebook-capi@0.11.1"
hidden: true
createdAt: "2022-07-19T14:17:53.329Z"
updatedAt: "2022-08-09T18:44:24.733Z"
---
This app allows your store to send pixel events to Facebook through their Conversions API directly from VTEX back-end services.

This app is automatically installed and configured upon installing `vtex.facebook-fbe`

At the time of this writing, the only event supported by this app is `Purchase`. It currently listens to the `orderCreated` event fired by `vtex.orders-broadcast` to generate purchase events and send them to facebook.

### Installation
If you install this app manually, be sure to go to **Apps -> My Apps -> Facebook Conversions Api** and adjust the required settings:

**Pixel Id**: The Facebook pixel Id. You can find this information on Facebook, in the business configuration page.

**Access Token**: The Facebook access token to fire CAPI (Conversions API) events. You can generate one in the Events Manager on Facebook.

**Store Url**: The base url for your VTEX store (eg: www.myvtexstore.com)

### Example

This is an example of an event sent to facebook:

```
{
    "data": [
        {
            "event_name": "Purchase",
            "event_id": "1131820426878-01",
            "event_time": 1620914828,
            "event_source_url": "https://fbe--sandboxbrdevbrl/checkout/orderPlaced",
            "action_source": "website",
            "user_data": {
                "em": [
                    "4e83eede106157a3545f7d98177b3ff0c4c0986e5f33ea017ad0a6f16a145c32"
                ],
                "ph": [
                    "600950f359c78b6db644c81875f3e5138d3fa82a1ced70b4ab4d17279ae3618b"
                ],
                "client_ip_address": "189.120.75.186",
                "client_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
                "zp": "06c4a73ab1fad2b5bf21ffb2575830724ab598c79671b167c8b3ad98fbdcd9bf",
                "st": "0510eddd781102030eb8860671503a28e6a37f5346de429bdd47c0a37c77cc7d",
                "ct": "f5df373255b438aa9ef1d0864e7cb17890b5a16cb6b476ab14f2fbc1805185d0",
                "country": "885036a0da3dff3c3e05bc79bf49382b12bc5098514ed57ce0875aba1aa2c40d",
                "ge": "62c66a7a5dd70c3146618063c344e531e6d4b59e379808443ce962b3abd63c5a",
                "fn": "cd1a2cafc111c333beac923939675ec3388b9ccc488580d40ebe5b64e5eac1f4",
                "ln": "8261ed6d55c45baafd9b7fc4e88b5b9ebe558ee0e6b7f3140d682da631eb4d40",
                "db": "c891abdf111dcf8761921a5bbc4067510c92ca182417d1b21ac85977fc4aee05",
                "external_id": "7f044bca33272e9015d40b7bf21c6c6e4540b6434d7ac9b2480290faa2fb5988"
            },
            "custom_data": {
                "value": 119.26,
                "currency": "BRL",
                "content_ids": [
                    "8"
                ],
                "content_type": "product"
            }
        }
    ]
}
```

For 'client_user_agent', non-browser user agents such as 'axios' or 'postman' are discarded. Devices such as mobiles, smart tvs and wearables are regarded as valid and the user agent is sent as expected, as long as a web browser is used for those purchases.

You can find all information about sent events (including request/response and possible errors) on splunk.

### Action Sources

When the IP and UserAgent properties are readily available, and the purchase is not evaluated as being from a native mobile App or from a call center, the action source is set to `website`. If the Ip Address or the User Agent are not available, then the event is sent as `system_generated`. For now, events from native mobile apps and call centers are filtered out from Conversions API. This is done on purpose to follow Facebook's best practices, but will likely change in the future.

The rules for filtering out purchases from native mobile apps are based on marketing data and tags. Whenever the words "app", "android" or "iOS" are found in the marketing tags, separated by a dash, dot, underscore or in camelCase, as in "myApp", "appMyStore", or "myStore-android", the event is not sent to Conversions API.