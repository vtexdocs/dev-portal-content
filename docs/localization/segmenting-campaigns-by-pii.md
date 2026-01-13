---
title: "Segmenting campaigns by PII"
slug: "segmenting-campaigns-by-pii"
excerpt: "Create targeted campaigns using personally identifiable information through secure CSV file integration."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2025-10-14T00:00:00.000Z"
---
PII segmentation must be done via CSV and will allow the creation of campaigns with users known by the advertiser.

## Audience file

The integration file will be a **CSV** file in **UTF-8** encoding.

### Attributes

Most attributes are not required; however, the more complete this information is, the better the relevance will be.

| Column            | Type   | Required | Description                                  |
| :---------------- | :----- | :------- | :------------------------------------------- |
| CUSTOMER_ID       | String | Yes      | Unique customer identifier                   |
| EMAIL_HASHED      | String | No       | PII based on customer email                  |
| PHONE_HASHED      | String | No       | PII based on customer primary phone number   |
| SOCIAL_ID_HASHED  | String | No       | PII based on customer CPF (tax ID)          |
| FIRST_NAME_HASHED | String | No       | PII based on customer first name             |
| LAST_NAME_HASHED  | String | No       | PII based on customer last name              |

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

### File delivery

The file must be sent as a ZIP file via email to your Newtail contact.
