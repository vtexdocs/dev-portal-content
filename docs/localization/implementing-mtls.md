---
title: "Implementing Mutual Transport Layer Security (mTLS)"
excerpt: "Learn how to generate, request, and use certificates to securely authenticate with VTEX services using mTLS."
slug: "implementing-mtls"
hidden: false
createdAt: "2025-07-01T00:00:00.000Z"
updatedAt: "2025-07-01T00:00:00.000Z"
---

>ℹ️ This feature is part of [VTEX Shield](https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh). If you're already a VTEX client and would like to adopt VTEX Shield for your business, contact our [Commercial Support](https://help.vtex.com/en/tracks/support-at-vtex--4AXsGdGHqExp9ZkiNq9eMy/3KQWGgkPOwbFTPfBxL7YwZ). Additional fees may apply. If you're not a VTEX client yet but are interested in this solution, please complete our [contact form](https://vtex.com/us-en/contact/).

When making requests to VTEX services using [mTLS](https://help.vtex.com/en/tutorial/mutual-transport-layer-security-mtls--6YR3SoynJMfeEKGlY1Cqlo), VTEX validates whether the certificate was issued and signed by its internal Certificate Authority (CA). This guide walks you through the process of obtaining and managing certificates for mTLS authentication.

## Step 1 - Generating a Certificate Signing Request (CSR)

The first step is to generate a Certificate Signing Request (CSR) using [OpenSSL 3.0.0](https://openssl-library.org/news/openssl-3.0-notes/index.html) or higher. This process generates the CSR (`.csr`) and private key (`.key`) files.

Open a terminal and run the command below, replacing the values in `{{ }}` with your specific information:

```shell
openssl req -new -subj "/CN={{APP_NAME}}/OU={{TENANT}}/L={{CITY}}/ST={{STATE}}/C={{COUNTRY:2CHARS}}" -out APP_CERT_REQUEST.csr -nodes -sha512 -newkey rsa:2048 -keyout APP_CERT_PRIVATE_KEY.key
```

The fields `CN` (Common Name) and `OU` (Organizational Unit) are mandatory and must contain the application name and account name respectively.

Save both generated files (`.csr` and `.key`) for the next step.

## Step 2 - Issuing a certificate signed by VTEX

Once you have [generated the CSR](#step-1–generating-a-certificate-signing-request-csr), use the `POST` [Sign certificate](https://developers.vtex.com/docs/api-reference/mtls-api#post-/api/edge/private-certificates/sign) endpoint to request a certificate signed by VTEX's Certificate Authority. This request allows you to submit a CSR and receive a signed certificate.

### Required permission

To use this endpoint, your user or API key must have access to the following License Manager resource. Otherwise, they will receive a 403 status code error.

| Product | Category | Resource |
| :---- | :---- | :---- |
| CDN API | Certificate management | Update certificate |

There are no predefined roles for these resources. To use this endpoint, you must create a [custom role](https://help.vtex.com/en/tutorial/creating-roles--qGtNQpKSSAduX94l2WZBW#creating-custom-roles) and add the above resource to use this endpoint. Learn more roles and resources in the [Roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) documentation.

### Request example

The request body should contain the [previously generated CSR](#step-1–generating-a-certificate-signing-request-csr) as plain text:

```curl
curl --request post \
	--url https://apiexamples.vtexcommercestable.com.br/api/edge/private-certificates/sign \
	--header 'Content-Type: text/plain' \
	--header 'X-VTEX-API-AppKey: ' \
	--header 'X-VTEX-API-AppToken: ' \
	--data '-----BEGIN CERTIFICATE REQUEST-----
***
-----END CERTIFICATE REQUEST-----
'
```

>ℹ️ The account in the request must match the one specified in the `OU` field of the CSR.

### Response

If successful, the API responds with the certificate in plain text:

```crt
-----BEGIN CERTIFICATE-----
***
-----END CERTIFICATE-----
```

Save this content to a `.crt` file. You’ll use it along with the private key (`.key`) to authenticate requests.

>ℹ️ Learn more in the `POST` [Sign certificate](https://developers.vtex.com/docs/api-reference/mtls-api#post-/api/edge/private-certificates/sign) API reference.

## Step 3 - Making requests with the certificate

With the certificate issued, you can now authenticate your requests to VTEX using mTLS. See examples using [Postman](https://www.postman.com/) and cURL below.

### Using Postman

To test mTLS requests with Postman, you can attach your certificate and private key directly in the tool’s settings. Follow the steps below:

1. Open **Postman** and go to **Settings**.
2. Navigate to the **Certificates** tab.
3. Define the **Host** for the call.
4. In **CRT file**, add the certificate file (`.crt`).
5. In **KEY file**, add the private key (`.key` file generated earlier with the CSR).
6. Click **Add** to save the certificate configuration.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/postman-certificates.gif)

Once configured, any request made to the specified host will automatically include the certificate, allowing you to test mTLS-protected endpoints.

### Using cURL

If you prefer testing or integrating mTLS requests via the command line, you can use `cURL` to send requests with your certificate and private key.

Use the following example to authenticate a request with mTLS:

```curl
curl --location 'https://{{account}}.vtexcommercestable.com.br/api/vtexid/credential/validate' \
--cert {{client.crt}} \
--key {{client.key}} \
--header 'Content-Type: application/json' \
--data '{
  "token": "{{user_token}}"
}
'
```

>ℹ️ Replace `{{client.crt}}` and `{{client.key}}` with the paths to your certificate and private key files, and insert a valid token in the request body.
