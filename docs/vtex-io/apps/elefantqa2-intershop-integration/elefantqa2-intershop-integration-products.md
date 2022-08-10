---
title: "Product export endpoints"
slug: "elefantqa2-intershop-integration-products"
excerpt: "elefantqa2.intershop-integration@0.6.7"
hidden: true
createdAt: "2022-07-27T13:53:09.491Z"
updatedAt: "2022-07-28T13:04:01.473Z"
---
> All endpoints require the `token` authentication header with the value found in the app settings

## Paginated export
Export products from the specified pages.

* **URL:** `/_v/intershop/products/export`

* **Method:** `POST`

* **URL Params:** None

* **Query Params:**
  * **Required:**
     * One of the following:
       * `page=[integer]`: exact page to export
       * `pageFrom=[integer]&pageTo=[integer]`: range to export
  * Optional:
    * `pageSize`:
      * number of products in one page
      * Default: **50**

* **Data Params:** None

* **Success Response:**

  * **Code:** 204
  * **Content:** None

* **Error Response:**
  * **Code:** 400 BAD REQUEST
  * **Content:** `Page query param must be a number!` OR  `Page query param must be > 0!`

  OR

  * **Code:** 401 UNAUTHORIZED
  * **Content:** None

  OR

  * **Code:** 404 NOT FOUND
  * **Content:** None
  

* **Sample Call:**
  ```shell
   curl -L -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/products/export?pageFrom=1&pageTo=10' -H 'token: {{intershop-token}}'
  ```


## Updates export
Export product updates. Will only export the differences since the last call.

* **URL:** `/_v/intershop/products/update`

* **Method:** `POST`
* **URL Params:** None
* **Query Params:** None
* **Data Params:** None

* **Success Response:**

  * **Code:** 200
  * **Content:** None

* **Error Response:**
  * **Code:** 401 UNAUTHORIZED
  * **Content:** None

  > Errors will be sent by mail to the `adminEmail` field from settings
* **Sample Call:**
  ```shell
   curl -L -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/products/update' -H 'token: {{intershop-token}}'
  ```