---
title: "Revoking SSL private certificates when using Mutual Transport Layer Security (mTLS)"
excerpt: "Learn how to revoke SSL private certificates in VTEX when using mTLS, including how to extract the serial number and use the API to revoke compromised or unused certificates."
slug: "revoking-ssl-private-certificates-when-using-mtls"
hidden: false
createdAt: "2025-07-01T00:00:00.000Z"
updatedAt: "2025-07-01T00:00:00.000Z"
---

>ℹ️ This feature is part of [VTEX Shield](https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh). If you're already a VTEX client and would like to adopt VTEX Shield for your business, contact our [Commercial Support](https://help.vtex.com/en/tracks/support-at-vtex--4AXsGdGHqExp9ZkiNq9eMy/3KQWGgkPOwbFTPfBxL7YwZ). Additional fees may apply. If you're not yet a VTEX client but are interested in this solution, complete our [contact form](https://vtex.com/us-en/contact/).

For security reasons, when using [mTLS](https://help.vtex.com/en/tutorial/mutual-transport-layer-security-mtls--6YR3SoynJMfeEKGlY1Cqlo), you may need to revoke previously issued certificates if they're compromised or no longer needed. VTEX provides a `DELETE` [Revoke certificate](https://developers.vtex.com/docs/api-reference/mtls-api#delete-/api/edge/private-certificates/-serialNumber-) endpoint, which allows you to revoke a certificate using its serial number.

This guide provides step-by-step instructions for revoking certificates using this endpoint.

## Step 1 - Getting the certificate serial number

To revoke a certificate, you first need to retrieve its serial number, which uniquely identifies the certificate issued by VTEX’s Certificate Authority. This information is embedded in the certificate (`.crt`) file and can be extracted using OpenSSL.

There are two ways to extract the serial number, depending on how you intend to format the value in the revocation request. The VTEX API accepts both formats.

### Method 1 - Hex string without colons

Open a terminal and use the command below to extract the serial number in a plain hexadecimal format:

```shell
openssl x509 -noout -serial -in yourcertificate.crt | sed 's/serial=//'
```

Example output:

```shell
4D0A0A39360B2E1254DDB6CE57DBC940
```

### Method 2 – Colon-separated hexadecimal format

Alternatively, you can use the command below to extract the serial number with colon separators:

```shell
openssl x509 -in yourcertificate.crt -noout -text | grep "Serial Number" -A1 | tail -n 1
```

Example output:

```shell
4d:0a:0a:39:36:0b:2e:12:54:dd:b6:ce:57:db:c9:40
```

## Step 2 - Revoking the certificate

Send a revocation request to the `DELETE` [Revoke certificate](https://developers.vtex.com/docs/api-reference/mtls-api#delete-/api/edge/private-certificates/-serialNumber-) endpoint, including the certificate's serial number in the URL. Both serial number formats shown in the [Step 1 \- Getting the certificate serial number](#step-1-getting-the-certificate-serial-number) section are accepted.

### Required permission

The user or application must have the following License Manager resource to make this call. Otherwise, a 403 status code error will be returned.

| Product | Category | Resource |
| :---- | :---- | :---- |
| CDN API | Certificate management | Update certificate |

There are no predefined roles for these resources. To use this endpoint, you must create a custom role and add the above resource. Learn more about platform resources and roles in the [Roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) documentation.

### Request example

Using an authentication cookie:

```shell
curl --location --request DELETE 'https://{{account}}.vtexcommercestable.com.br/api/edge/private-certificates/{{serialNumber}}' \
--header 'VtexIdclientAutCookie: {{token}}'
```

Using API keys:

```shell
curl --location --request DELETE 'https://mystore.vtexcommercestable.com.br/api/edge/private-certificates/4D0A0A39360B2E1254DDB6CE57DBC940' \
--header 'X-VTEX-API-AppKey: appKey' \
--header 'X-VTEX-API-AppToken: appToken'
```

>ℹ️Learn more in the `DELETE` [Revoke certificate](https://developers.vtex.com/docs/api-reference/mtls-api#delete-/api/edge/private-certificates/-serialNumber-) API reference.
