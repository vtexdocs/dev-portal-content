---
title: "Categories export endpoints"
slug: "vtex-intershop-integration-categories"
excerpt: "vtex.intershop-integration@0.6.6"
hidden: true
createdAt: "2022-07-29T08:30:51.156Z"
updatedAt: "2022-07-29T08:30:51.156Z"
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