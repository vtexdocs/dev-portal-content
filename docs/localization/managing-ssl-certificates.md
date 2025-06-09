---
title: "Managing SSL certificates"
slug: "managing-ssl-certificates"
excerpt: "Learn how to manage custom SSL certificates with VTEX Shield."
hidden: false
createdAt: "2025-05-21T10:18:55.338Z"
updatedAt: "2025-05-21T10:18:55.338Z"
---

>ℹ️ This feature is part of [VTEX Shield](https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh). If you're a current VTEX customer and want to adopt VTEX Shield for your business, please contact [Commercial Support](https://help.vtex.com/en/tracks/support-at-vtex--4AXsGdGHqExp9ZkiNq9eMy/3KQWGgkPOwbFTPfBxL7YwZ). Additional fees may apply. If you're not a customer yet but are interested in this solution, please complete our [contact form](https://vtex.com/en-us/contact/).

VTEX automatically manages SSL certificates for stores by default, but merchants may need to use their own certificates for specific compliance reasons, internal security requirements, or certification entities that offer additional warranties.

To give them a flexible and secure way to upload their certificates to our infrastructure, we offer the [SSL Certificates API](https://developers.vtex.com/docs/api-reference/ssl-certificates-api) and the [SSL certificates](https://help.vtex.com/tutorial/custom-ssl-certificates--1hoaDEbU50PDZSe6AYep9q) page in the Admin.

This guide explains how to use the API for managing certificates.

The SSL Certificates API allows users to list their custom SSL certificates, get a specific certificate by ID, and install or renew a certificate.

## Before you begin

Make sure you meet the following prerequisites to manage SSL certificates:

* You must have the [Custom SSL certificates](https://help.vtex.com/tutorial/custom-ssl-certificates--1hoaDEbU50PDZSe6AYep9q) feature from [VTEX Shield](https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh).
* You must have a user or API key associated with a [role](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) that contains the following [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3):
* **Product:** *CDN API*
* **Category:** *Certificate management*
* **Resources:** *Update certificate* and *View certificate*

## Installing or renewing an SSL certificate

To install a certificate, you can send its information through an [Install or renew SSL certificate](https://developers.vtex.com/docs/api-reference/ssl-certificates-api#put-/api/edge/certificates) `PUT` request, using *multipart/form-data* or *application/json*. The process of renewing a certificate is the same as the process of installing one.

#### Request example \- multipart/form-data

```shell
curl --request PUT 'https://{{accountName}}.vtexcommercestable.com.br/api/edge/certificates' \
--header 'VtexIdclientAutCookie: {{VtexIdclientAutCookie}}' \
--form 'Hosts="{{MY_HOST}}"' \
--form 'Certificate=@"{{CERTIFICATE_PATH}}"' \
--form 'PrivateKey=@"{{PRIVATE_KEY_PATH}}"'
```

For the example account `myaccountname` and host `mystore.com`, the request should look like this:

```shell
curl --request PUT 'https://myaccountname.vtexcommercestable.com.br/api/edge/certificates' \
--header 'VtexIdclientAutCookie: {{VtexIdclientAutCookie}}' \
--form 'Hosts="mystore.com"' \
--form 'Certificate=@"/path/to/certificate.crt"' \
--form 'PrivateKey=@"/path/to/private.key"'

```

#### Request example \- application/json

```shell
curl --request PUT 'https://{{accountName}}.vtexcommercestable.com.br/api/edge/certificates' \
--header 'VtexIdclientAutCookie: {{VtexIdclientAutCookie}}' \
--header 'Content-Type: application/json' \
--data '{
    "hosts": ["{{MY_HOST}}"],
    "certificate": "{{BASE64_ENCODED_CERTIFICATE}}",
    "privateKey": "{{BASE64_ENCODED_PRIVATE_KEY}}"
}'
```

For the example account `myaccountname` and host `mystore.com`, the request should look like this:

```shell
curl --request PUT 'https://myaccountname.vtexcommercestable.com.br/api/edge/certificates' \
--header 'VtexIdclientAutCookie: {{VtexIdclientAutCookie}}' \
--header 'Content-Type: application/json' \
--data '{
    "hosts": ["mystore.com"],
    "certificate": "LS0tLS1CRUd...S0tLS0K",
    "privateKey": "LS0tLS1CRUd...LS0NCg=="
}'
```

### Response example

In both cases, whether installing or renewing a certificate, the response should look like this:

```json
[
    {
        "id": "3421b2ea-94b1-55ac-67ea-e517018fbatc",
        "account": "myaccountname",
        "host": "mystore.com",
        "serialNumber": "99C468B5853EF5549E40A44526720C71GT",
        "subjectDistinguishedName": "CN=mystore.com",
        "subjectCommonName": "mystore.com",
        "subjectOrganization": null,
        "issuerDistinguishedName": "CN=ZeroSSL RSA Domain Secure Site CA, O=ZeroSSL, C=AT",
        "issuerCommonName": "ZeroSSL RSA Domain Secure Site CA",
        "issuerOrganization": "ZeroSSL",
        "installDate": "2025-04-24T20:15:51.7903622Z",
        "startDate": "2025-03-20T00:00:00Z",
        "expiryDate": "2025-06-18T23:59:59Z",
        "signatureAlgorithm": "sha384RSA",
        "x509Version": "3",
        "installedBy": "22b312e1-f863-43t7-8c59-5n2f9ll0d09x",
        "createdAt": "2025-03-20T13:20:34.40938Z",
        "updatedAt": "2025-04-24T20:15:51.7903892Z",
        "status": "Installing"
    }
]
```

>ℹ️ Find more details about each field in the [Install or renew SSL certificate](https://developers.vtex.com/docs/api-reference/ssl-certificates-api#put-/api/edge/certificates) `PUT` reference.

## Listing SSL certificates

You can list your certificates with the [List SSL certificates](https://developers.vtex.com/docs/api-reference/ssl-certificates-api#get-/api/edge/certificates) `GET` endpoint, as shown below. Remember to replace the `accountName` and `VtexIdclientAutCookie` placeholders.

### Request example

```shell
curl 'https://{{accountName}}.vtexcommercestable.com.br/api/edge/certificates' \
--header 'VtexIdclientAutCookie: {{VtexIdclientAutCookie}}'
```

For the example account `myaccountname`, the request should look like this:

```shell
curl 'https://myaccountname.vtexcommercestable.com.br/api/edge/certificates' \
--header 'VtexIdclientAutCookie: 1234'
```

### Response example

```json
[
    {
        "id": "8c66122e-85cd-4bff-885d-aa9846e97541",
        "account": "myaccountname",
        "host": "mystore.com",
        "serialNumber": "05C51F848EDBAC18E91D9AE43D8F6728D4F8",
        "subjectDistinguishedName": "CN=mystore.com",
        "subjectCommonName": "mystore.com",
        "subjectOrganization": null,
        "issuerDistinguishedName": "CN=R10, O=Let's Encrypt, C=US",
        "issuerCommonName": "R10",
        "issuerOrganization": "Let's Encrypt",
        "installDate": "2025-04-22T16:24:58.768939Z",
        "startDate": "2024-08-29T01:43:25Z",
        "expiryDate": "2024-11-27T01:43:24Z",
        "signatureAlgorithm": "sha256RSA",
        "x509Version": "3",
        "installedBy": "22b312e1-f863-43t7-8c59-5n2f9ll0d09x",
        "createdAt": "2024-10-25T17:51:51.222052Z",
        "updatedAt": "2025-04-22T16:24:58.768939Z",
        "status": "Active"
    }
]
```

>ℹ️ Find more details about each field in the [List SSL certificates](https://developers.vtex.com/docs/api-reference/ssl-certificates-api#get-/api/edge/certificates) `GET` reference.

## Getting an SSL certificate by its ID

To get a specific certificate, you can use the [Get SSL certificate by ID](https://developers.vtex.com/docs/api-reference/ssl-certificates-api#get-/api/edge/certificates/-certificateId-) GET` request. Remember to replace the `accountName` and `VtexIdclientAutCookie` placeholders.

### Request example

```shell
curl 'https://{{accountName}}.vtexcommercestable.com.br/api/edge/certificates/{{certificateId}}' \
--header 'VtexIdclientAutCookie: {{VtexIdclientAutCookie}}'
```

For the example account `myaccountname` and certificate ID `8c66122e-85cd-4bff-885d-aa9846e97541`, the request should look like this:

```shell
curl 'https://myaccountname.vtexcommercestable.com.br/api/edge/certificates/8c66122e-85cd-4bff-885d-aa9846e97541' \
--header 'VtexIdclientAutCookie: 1234'
```

### Response example

```json
{
    "id": "8c66122e-85cd-4bff-885d-aa9846e97541",
    "account": "myaccountname",
    "host": "mystore.com",
    "serialNumber": "05C51F848EDBAC18E91D9AE43D8F6728D4F8",
    "subjectDistinguishedName": "CN=mystore.com",
    "subjectCommonName": "mystore.com",
    "subjectOrganization": null,
    "issuerDistinguishedName": "CN=R10, O=Let's Encrypt, C=US",
    "issuerCommonName": "R10",
    "issuerOrganization": "Le
t's Encrypt",
    "installDate": "2025-04-22T16:24:58.768939Z",
    "startDate": "2024-08-29T01:43:25Z",
    "expiryDate": "2024-11-27T01:43:24Z",
    "signatureAlgorithm": "sha256RSA",
    "x509Version": "3",
    "installedBy": "22b312e1-f863-43t7-8c59-5n2f9ll0d09x",
    "createdAt": "2024-10-25T17:51:51.222052Z",
    "updatedAt": "2025-04-22T16:24:58.768939Z",
    "status": "Active"
}
```

>ℹ️ Find more details about each field in the [Get SSL certificate by ID](https://developers.vtex.com/docs/api-reference/ssl-certificates-api#get-/api/edge/certificates/-certificateId-) `GET` reference.
