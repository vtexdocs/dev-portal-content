---
title: "Troubleshooting: Abandoned cart webhook"
slug: "troubleshooting-abandoned-cart-webhook"
hidden: false
createdAt: "2026-08-28T00:00:00.000Z"
updatedAt: "2026-08-28T00:00:00.000Z"
excerpt: "Learn the most common errors when using VTEX CX Platform's abandoned cart webhook and how to troubleshoot them."
---

Troubleshoot common errors when integrating VTEX CX Platform's abandoned cart webhook in your store.

In the following table, see the most common symptoms and what to check for each one:

| Symptom | Likely causes and what to check |
| :----: | :---- |
| The call returns `200`, but the cart isn't registered. | The `name` field is missing or blank: It's required, and its absence makes payload validation fail without changing the response. Also check `order_form_id`, `phone`, and the phone format, with country code and digits only. |
| The request body appears to be ignored. | The URL was sent without the trailing slash, and the resulting redirect makes most HTTP clients drop the body. Also check that the `Content-Type: application/json` header is present. |
| The call fails or is blocked when made from the app or the browser. | Calls from end-user clients aren't supported. Requests with `Content-Type: application/json` originating from a browser or WebView trigger a Cross-Origin Resource Sharing (CORS) preflight check. The integration must originate from your backend. |
| The cart doesn't appear in the logs. | Check whether the verification period of the automation has already ended, as the entry only appears once it does. Invalid payloads generate no log at all. |
| The customer received two recovery messages. | The same `order_form_id` was sent with different phone numbers, creating two active records. Send only complete, validated phone numbers. |
| Cart response time in the store increased. | The notification is on the critical path of the operation. Make the call asynchronous. Reducing call volume mitigates the issue but doesn't eliminate it. |
| No message is triggered even though the cart was registered. | The order may have been completed within the verification period, or the cart may not meet the eligibility rules of the automation, such as minimum value, cooldown, or phone restrictions. These rules are configured in the automation and don't depend on the payload. |
