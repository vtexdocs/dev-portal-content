---
title: "Integrating audiences"
slug: "integrating-audiences"
excerpt: "Integrate customer audience data with VTEX Ads using a presigned S3 upload and PII hashing."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2026-06-03T00:00:00.000Z"
---

Audience integration lets you enrich **VTEX Ads** targeting with your own customer data, improving campaign segmentation and ad relevance. It is optional but highly recommended.

You deliver an audience file through a short-lived presigned Amazon S3 upload. First you request an upload URL from the VTEX Ads API, then you upload the file directly to Amazon S3 using the signed fields returned in the response. The backend builds the destination path from your authenticated publisher, so no per-publisher credentials or manual paths are required.

> ℹ️ If you do not integrate audiences, open a ticket with your account manager to request pre-population of segmentation information with base data (`STATE`, `CITY`, `GENDER`, and `AGE`). You can also provide a list of audiences to be registered, and keep them updated periodically.

## Before you begin

- **Authentication:** the upload URL request requires the `X-App-Id` and `X-Api-Key` headers. Contact [VTEX support](https://help.vtex.com/en/tutorial/how-does-vtex-support-work--2eAT5EyOvaLoHdIWDVaxC3) to obtain credentials.
- **File format:** `Parquet` with `Snappy` compression. Column names are case-sensitive (see [Audience file](#audience-file)).

> ℹ️ Delivery recommendation
> 
> On the first integration, send all data. You can split it across multiple files (a good size is around 1 million rows per file). After the first integration, send only the delta of rows that changed.

> ℹ️ FTP/SFTP integration is no longer supported for new projects. If you have a legacy SFTP integration, contact the VTEX Ads team to plan the migration to this flow.

## 1. Request an upload URL

Send an authenticated `POST` request to the `/audience/upload-url` endpoint. The endpoint returns a presigned Amazon S3 `POST` that is valid for `expires_in` seconds (900 by default, around 15 minutes).

Request example:

```bash
curl -X POST "https://api-retail-media.newtail.com.br/audience/upload-url" \
  -H "X-App-Id: {your_app_id}" \
  -H "X-Api-Key: {your_api_key}" \
  -H "Accept: application/json"
```

Response example:

```json
{
  "url": "https://newtail-data-clean-room.s3.amazonaws.com/",
  "fields": {
    "key": "0d675bf6-03f6-4b81-9617-e79dffddc3ab/audiences/2026/06/03/14/1780495200.parquet.snappy",
    "Content-Type": "application/octet-stream",
    "Policy": "eyJleHBpcmF0aW9uIjoiMjAyNi0wNi0wM1QxNDoxNTowMFoiLCJjb25kaXRpb25zIjpbXX0=",
    "X-Amz-Signature": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
  },
  "key": "0d675bf6-03f6-4b81-9617-e79dffddc3ab/audiences/2026/06/03/14/1780495200.parquet.snappy",
  "bucket": "newtail-data-clean-room",
  "expires_in": 900,
  "max_bytes": 2147483648,
  "upload": {
    "method": "POST",
    "enctype": "multipart/form-data"
  }
}
```

See the `POST` [Generate audience upload URL](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/audience/upload-url) endpoint for the full response schema. The following table describes the response fields:

| Field | Description |
| :--- | :--- |
| `url` | Amazon S3 endpoint to send the upload request to. |
| `fields` | Signed Amazon S3 form fields that must be sent with the upload, before the `file` field. |
| `key` | Object key the file will be stored under. Built by the backend from your authenticated publisher. |
| `bucket` | Amazon S3 bucket that receives the upload. |
| `expires_in` | Number of seconds the presigned `POST` remains valid. Defaults to `900`. |
| `max_bytes` | Maximum file size, in bytes, accepted by Amazon S3. Defaults to `2147483648` (2 GB). |
| `upload` | HTTP `method` and `enctype` to use for the upload request. |

## 2. Upload the file to Amazon S3

Upload the audience file with a multipart `POST` request directly to the `url` returned in the previous step. Send every entry from `fields` first and the `file` field last.

```bash
curl -X POST "{url}" \
  -F key={fields.key} \
  -F Content-Type=application/octet-stream \
  -F Policy={fields.Policy} \
  -F X-Amz-Signature={fields.X-Amz-Signature} \
  -F <remaining fields from the response, in order> \
  -F file=@my-audience.parquet.snappy
```

> ⚠️ The presigned `POST` expires after `expires_in` seconds. If it expires before the upload completes, request a new upload URL. Amazon S3 rejects files larger than `max_bytes` (2 GB by default).

## Audience file

### Attributes

Most attributes are not required. However, the more complete this information is, the better the relevance will be.

> ℹ️ Columns are case-sensitive
> 
> Keep the column names exactly as they are presented.

| Column            | Type   | Required | Description                                              |
| :---------------- | :----- | :------- | :------------------------------------------------------- |
| `CUSTOMER_ID`       | String | Yes      | Unique customer identifier                               |
| `EMAIL_HASHED`      | String | No       | PII based on customer email                              |
| `PHONE_HASHED`      | String | No       | PII based on customer primary phone number               |
| `SOCIAL_ID_HASHED`  | String | No       | PII based on customer CPF (tax ID)                      |
| `FIRST_NAME_HASHED` | String | No       | PII based on customer first name                         |
| `LAST_NAME_HASHED`  | String | No       | PII based on customer last name                          |
| `GENDER`            | String | No       | Customer gender: `F` (female), `M` (male), `O` (other), `NULL` (not identified) |
| `AGE`               | Int    | No       | Customer age                                             |
| `CEP`               | String | No       | Customer address postal code                             |
| `COUNTRY`           | String | No       | Customer country                                         |
| `STATE`             | String | No       | Customer state of residence                              |
| `CITY`              | String | No       | Customer city of residence                               |
| `NEIGHBORHOOD`      | String | No       | Customer neighborhood of residence                       |
| `AUDIENCES`         | String | No       | List of audiences using `;` as the separator            |
| `NBO_PRODUCTS`      | String | No       | List of product SKUs using `;` as the separator         |
| `NBO_CATEGORIES`    | String | No       | List of categories using `;` as the separator. Category lists can include category trees using ` > ` as separator. Example: `Tablets;Beverages > Non-Alcoholic Beverages;Books > Gastronomy > Bar and Restaurant Guides` |


### Field hashing

Confidential data must be encrypted before being sent using the SHA-256 algorithm.

- `EMAIL_HASHED`
- `PHONE_HASHED`
- `SOCIAL_ID_HASHED`
- `FIRST_NAME_HASHED`
- `LAST_NAME_HASHED`

> ℹ️ Before generating the data hash, you must remove all SPACES and convert values to **LOWERCASE**.

> ⚠️ For the `PHONE_HASHED` attribute, you must format it to the E.164 standard and include the country calling code.

#### E.164 format

1. Remove all non-numeric characters, such as spaces, dashes, parentheses, and symbols.
2. Add the country code with a plus sign (+) at the beginning. The country code is a 1 to 3-digit code that identifies the country of the phone number. You can find a list of country codes in the ISO 3166-1 standard.
3. Add the area code (if applicable) without the leading zero. For example, in the United States, the area code consists of three digits and should not start with zero.
4. Include the local phone number without the leading zero (if applicable).

Examples:

- A United States phone number with area code 212 and local number 555-1234 would be formatted as: +12125551234
- A Brazilian phone number with area code 11 and local number 98765-4321 would be formatted as: +5511987654321

#### Creating a hash of a formatted attribute using Python

```python
import re
import hashlib

hash_obj = hashlib.sha256()

def create_hash(x):
    cleaned = re.sub('\s+', '', x.lower())
    hash_obj.update(cleaned.encode('utf-8'))
    return hash_obj.hexdigest()

create_hash(' Allan ') #=> 8c01ade3cb71d3ac7c718ed5a0c565155a4c05a216d9e59013c5d7b49e916914
```

## Runtime alternative

If you choose not to integrate audiences through file upload, you can still apply segmentation at query time by sending the data in the `segmentation` field of the ad query request. For more details, see [Segmenting campaigns](https://developers.vtex.com/docs/guides/segmenting-campaigns).

## Next steps

- [Segmenting campaigns](https://developers.vtex.com/docs/guides/segmenting-campaigns)
- `POST` [Generate audience upload URL](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/audience/upload-url)
