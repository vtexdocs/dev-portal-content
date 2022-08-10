---
title: "Stock export endpoints"
slug: "elefantqa2-intershop-integration-stock"
excerpt: "elefantqa2.intershop-integration@0.6.7"
hidden: true
createdAt: "2022-07-27T13:53:09.440Z"
updatedAt: "2022-07-28T13:04:01.485Z"
---
> All endpoints require the `token` authentication header with the value found in the app settings

## Stock update
Exports all new stock offers.

* **URL:** `/_v/intershop/stock/update`

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

* **Sample Call:**
  ```shell
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/stock/update' -H 'token: {{intershop-token}}'
  ```


## Stock export
Exports all stock offers.

* **URL:** `/_v/intershop/stock/export`

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

* **Sample Call:**
  ```shell
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/stock/export' -H 'token: {{intershop-token}}'
  ```

## Stock export with start id
Exports all stock offers for SKUs with their `id` bigger or equal than `startId`.

* **URL:** `/_v/intershop/stock/export/start/:startId`

* **Method:** `POST`

* **URL Params:** 
  * **Required**:
    * `startId=[integer]`: The id of the first SKU to include in the export
* **Query Params:** None
* **Data Params:** None

* **Success Response:**

  * **Code:** 200
  * **Content:** None

* **Error Response:**
  * **Code:** 401 UNAUTHORIZED
  * **Content:** None

* **Sample Call:**
  ```shell
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/stock/export/start/2513' -H 'token: {{intershop-token}}'
  ```

## Stock offer export with seller id
Exports only stock offers from the specified seller id .

* **URL:** `/_v/intershop/stock/export/seller/:sellerId`

* **Method:** `POST`

* **URL Params:**
  * **Required**:
    * `sellerId=[integer]`: The id of the seller
* **Query Params:** None
* **Data Params:** None

* **Success Response:**

  * **Code:** 200
  * **Content:** None

* **Error Response:**
  * **Code:** 401 UNAUTHORIZED
  * **Content:** None

* **Sample Call:**
  ```shell
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/stock/export/seller/1' -H 'token: {{intershop-token}}'
  ```

## Stock offer time delta export
Exports only stock offers generated in the specified time delta.

Ex: The value `60` for the `minutes` param will export all stock offers generated in the last hour.

* **URL:** `/_v/intershop/stock/export/time/:minutes`

* **Method:** `POST`

* **URL Params:**
  * **Required**:
    * `minutes=[integer]`: Minutes to subtract from the current time
* **Query Params:** None
* **Data Params:** None

* **Success Response:**

  * **Code:** 200
  * **Content:** None

* **Error Response:**
  * **Code:** 401 UNAUTHORIZED
  * **Content:** None

* **Sample Call:**
  ```shell
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/stock/export/time/180' -H 'token: {{intershop-token}}'
  ```

## Stock offer export with seller id and time delta
Combines the time delta and seller id filters

* **URL:** `/_v/intershop/stock/export/seller/:sellerId/time/:minutes`

* **Method:** `POST`

* **URL Params:**
  * **Required**:
    * `sellerId=[integer]`: The id of the seller
    * `minutes=[integer]`: Minutes to subtract from the current time
* **Query Params:** None
* **Data Params:** None

* **Success Response:**

  * **Code:** 200
  * **Content:** None

* **Error Response:**
  * **Code:** 401 UNAUTHORIZED
  * **Content:** None

* **Sample Call:**
  ```shell
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/stock/export/seller/1/time/180' -H 'token: {{intershop-token}}'
  ```