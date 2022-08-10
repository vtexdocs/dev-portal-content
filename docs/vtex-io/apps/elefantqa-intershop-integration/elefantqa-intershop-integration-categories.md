---
title: "Categories export endpoints"
slug: "elefantqa-intershop-integration-categories"
excerpt: "elefantqa.intershop-integration@0.6.6-graylog"
hidden: true
createdAt: "2022-07-27T13:09:31.848Z"
updatedAt: "2022-07-27T13:09:31.848Z"
---
> All endpoints require the `token` authentication header with the value found in the app settings

## Categories export
Export all categories.

* **URL:** `/_v/intershop/category/export`

* **Method:** `POST`

* **URL Params:** None
* **Query Params:** None
* **Data Params:** None

* **Success Response:**

  * **Code:** 201
  * **Content:** `Uploaded to SFTP`

* **Error Response:**
  * **Code:** 401 UNAUTHORIZED
  * **Content:** None

  > Errors will be sent by mail to the `adminEmail` field from settings

* **Sample Call:**
  ```shell
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/category/export' -H 'token: {{intershop-token}}'
  ```