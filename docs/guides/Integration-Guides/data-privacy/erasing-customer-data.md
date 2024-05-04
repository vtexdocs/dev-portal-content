---
title: "Erasing customer data"
slug: "erasing-customer-data"
hidden: true
createdAt: "2023-05-16T09:38:36.446Z"
updatedAt: "2023-05-16T09:38:36.446Z"
seeAlso:
 - "/docs/guides/data-protection-plus"
 - "/docs/guides/pii-data-architecture-specifications"
 - "/docs/guides/profile-system"
 - "/docs/guides/changes-in-vtex-features-behavior-to-handle-pii-data"
 - "/docs/guides/limitations-of-the-pii-data-architecture-during-closed-beta"
 - "/docs/guides/data-residency"
---

>⚠️ **Closed beta:** [Data Protection Plus](https://developers.vtex.com/docs/guides/data-protection-plus) is in closed beta and is only available in select regions.
>
> This flow to erase customer data is in **alpha** testing stage, available only for select clients. Do not share this documentation with people outside of your company. If you do not have access yet, please refer to the [Erasing customer data](https://help.vtex.com/en/tutorial/erasing-customer-data--1R9Fn7A06Ifj4R9YD4JTKU) guide instead.

>❗ This feature is part of [VTEX Shield](https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh), meaning *additional fees may apply.* 
> 
> If you are already a VTEX customer and want to adopt VTEX Shield for your business, please contact [Commercial Support](https://help.vtex.com/en/tracks/support-at-vtex--4AXsGdGHqExp9ZkiNq9eMy/3KQWGgkPOwbFTPfBxL7YwZ).
>
> If you are not yet a customer but are interested in this solution, please complete our [contact form](https://vtex.com/us-en/contact/). 

According to data protection policies, such as [GDPR and LGPD](https://vtex.com/us-en/privacy-and-agreements/vtex-commitment/), companies using customer personal data are required to delete collected information upon the customer's request. Data Subject Rights API allows stores using the [PII data architecture](https://developers.vtex.com/docs/guides/pii-data-architecture) to erase user data collected by Checkout, Orders, VTEX ID and Profile System, without depending on the VTEX Support flow described in the [Erasing customer data](https://help.vtex.com/en/tutorial/erasing-customer-data--1R9Fn7A06Ifj4R9YD4JTKU) guide.

To begin the data erasing process, make a `POST` request to the [Erase customer data](https://developers.vtex.com/docs/api-reference/data-subject-rights-api#post-/api/user-rights/createAndProcessDeleteUserData) endpoint from the [Data Subject Rights API](https://developers.vtex.com/docs/api-reference/data-subject-rights-api). This action deletes a given customer's data collected in your store by Checkout, Orders, VTEX ID and Profile System.

>❗ Only orders with `invoiced` or `canceled` status are erased in this request.

A successful response is `200 OK` with `Completed` status, and all items in the applications array should have the `Deleted` status.

## Request body example

```json
{
  "email": "john@mail.com"
}
```

## Response body example

```json
{
  "uuid": "3e2f53dc-b099-4dc8-9727-581b2a97f39c",
  "requestType": "Removal",
  "email": "john@mail.com",
  "status": "Completed",
  "dataResponse": "{\r\n  \"VTEX  Checkout\": [],\r\n  \"orders\": {\r\n    \"dataStatus\": {\r\n      \"status\": \"anonymized\",\r\n      \"reason\": \"Sensitive information was anonymized rather than deleted to preserve the store metrics.\",\r\n      \"evidence\": \"Anonymized [0] orders\",\r\n      \"dryRun\": true\r\n    },\r\n    \"orders\": []\r\n  },\r\n  \"Profile System PII API\": {},\r\n  \"VTEX ID\": {\r\n    \"type\": \"https://tools.ietf.org/html/rfc7231#section-6.5.4\",\r\n    \"title\": \"Not Found\",\r\n    \"status\": 404,\r\n    \"traceId\": \"00-65d5abf9263b07eb185beee49e2075dc-b67b373e2e93dcf8-00\"\r\n  }\r\n}",
  "requestTime": "2023-09-05T17:19:33.1969022-03:00",
  "applications": [
    {
      "application": "chk",
      "status": "Deleted",
      "errorDetail": "",
      "updateAt": "2023-09-05T20:20:23"
    },
    {
      "application": "orders",
      "status": "Deleted",
      "errorDetail": "",
      "updateAt": "2023-09-05T20:20:25"
    },
    {
      "application": "profileSystemV2",
      "status": "Deleted",
      "errorDetail": "",
      "updateAt": "2023-09-05T20:20:26"
    },
    {
      "application": "vid",
      "status": "Deleted",
      "errorDetail": "",
      "updateAt": "2023-09-05T20:20:29"
    }
  ]
}
```
