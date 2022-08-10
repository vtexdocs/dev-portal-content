---
title: "Seller offers export endpoints"
slug: "vtex-intershop-integration-seller-offers"
excerpt: "vtex.intershop-integration@0.6.6"
hidden: true
createdAt: "2022-07-29T08:30:51.123Z"
updatedAt: "2022-07-29T08:30:51.123Z"
---
> All endpoints require the `token` authentication header with the value found in the app settings

## Seller offer update
Exports all new seller offers.

* **URL:** `/_v/intershop/seller-offer/update`

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
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/seller-offer/update' -H 'token: {{intershop-token}}'
  ```


## Seller offer export
Exports all seller offers.

* **URL:** `/_v/intershop/seller-offer/export`

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
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/seller-offer/export' -H 'token: {{intershop-token}}'
  ```

## Seller offer export with start id
Exports all seller offers for SKUs with their `id` bigger or equal than `startId`.

* **URL:** `/_v/intershop/seller-offer/export/start/:startId`

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
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/seller-offer/export/start/2513' -H 'token: {{intershop-token}}'
  ```

## Seller offer export with seller id
Exports only seller offers from the specified seller id .

* **URL:** `/_v/intershop/seller-offer/export/seller/:sellerId`

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
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/seller-offer/export/seller/1' -H 'token: {{intershop-token}}'
  ```

## Seller offer time delta export
Exports only seller offers generated in the specified time delta.

Ex: The value `60` for the `minutes` param will export all seller offers generated in the last hour.

* **URL:** `/_v/intershop/seller-offer/export/time/:minutes`

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
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/seller-offer/export/time/180' -H 'token: {{intershop-token}}'
  ```

## Seller offer export with seller id and time delta
Combines the time delta and seller id filters

* **URL:** `/_v/intershop/seller-offer/export/seller/:sellerId/time/:minutes`

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
   curl -L -g -X POST 'https://{{accountName}}.myvtex.com/_v/intershop/seller-offer/export/seller/1/time/180' -H 'token: {{intershop-token}}'
  ```