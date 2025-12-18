---
title: "Integrating audiences"
slug: "integrating-audiences"
excerpt: "Integrate customer audience data with VTEX Ads using secure S3-based file delivery and PII hashing."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2025-10-14T00:00:00.000Z"
---
## Integration connection

> 📘 The integration connection will occur through:
> 
> - Periodic audience delivery as agreed between parties
> - Delivery to our S3 (access credentials must be requested from your Newtail contact)
> - Files must be sent in `Parquet` format with `Snappy` compression
> - Newtail will provide S3 credentials

> 🚧 Delivery recommendation
> 
> In the initial integration, it is essential that all data be sent. This data can be sent in multiple files (depending on the database size. A good number is 1 million rows per file).
> 
> After the first integration, ideally only the delta of rows that have been modified should be sent.

Files must be written following this directory pattern:

```
PREFIX/audiences/YYYY/mm/dd/TIMESTAMP.parquet.snappy
```

| Attribute | Description                                              | Example    |
| :-------- | :------------------------------------------------------- | :--------- |
| PREFIX    | The prefix will be provided by Newtail                  | xyz        |
| YYYY      | Generation year with 4 digits                           | 2023       |
| mm        | Generation month with two digits (January = 01, December = 12) | 09         |
| dd        | Generation day with two digits (from 01 to 31)          | 31         |
| TIMESTAMP | Timestamp is the number of seconds since 1970 (filename can be anything, timestamp is just a suggestion that will never repeat) | 1694812122 |


## Audience file

### Attributes

Most attributes are not required; however, the more complete this information is, the better the relevance will be.

> 📘 Columns are case sensitive
> 
> Keep the column names exactly as they are presented.

| Column            | Type   | Required | Description                                              |
| :---------------- | :----- | :------- | :------------------------------------------------------- |
| CUSTOMER_ID       | String | Yes      | Unique customer identifier                               |
| EMAIL_HASHED      | String | No       | PII based on customer email                              |
| PHONE_HASHED      | String | No       | PII based on customer primary phone number               |
| SOCIAL_ID_HASHED  | String | No       | PII based on customer CPF (tax ID)                      |
| FIRST_NAME_HASHED | String | No       | PII based on customer first name                         |
| LAST_NAME_HASHED  | String | No       | PII based on customer last name                          |
| GENDER            | String | No       | Customer gender: `F` (female), `M` (male), `O` (other), `NULL` (not identified) |
| AGE               | Int    | No       | Customer age                                             |
| CEP               | String | No       | Customer address postal code                             |
| COUNTRY           | String | No       | Customer country                                         |
| STATE             | String | No       | Customer state of residence                              |
| CITY              | String | No       | Customer city of residence                               |
| NEIGHBORHOOD      | String | No       | Customer neighborhood of residence                       |
| AUDIENCES         | String | No       | List of audiences separated by semicolon (;)             |
| NBO_PRODUCTS      | String | No       | List of product SKUs separated by semicolon (;)         |
| NBO_CATEGORIES    | String | No       | List of categories separated by semicolon (;). Category lists can include category trees using " > " as separator. Example: `Tablets;Beverages > Non-Alcoholic Beverages;Books > Gastronomy > Bar and Restaurant Guides` |


### Field hashing

Confidential data must be encrypted before being sent using the SHA256 algorithm.

- EMAIL_HASHED
- PHONE_HASHED
- SOCIAL_ID_HASHED
- FIRST_NAME_HASHED
- LAST_NAME_HASHED

> 📘 Before generating data hash, you must remove all SPACES and convert values to **LOWERCASE**.

> 🚧 For the PHONE_HASHED attribute, you must format it to the E.164 standard and include the country calling code.

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
