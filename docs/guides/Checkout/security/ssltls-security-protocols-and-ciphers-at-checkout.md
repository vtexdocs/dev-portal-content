---
title: "SSL/TLS Security Protocols and Ciphers at Checkout"
slug: "ssltls-security-protocols-and-ciphers-at-checkout"
hidden: false
createdAt: "2022-08-16T17:58:01.088Z"
updatedAt: "2022-08-16T18:08:37.001Z"
---
VTEX performs integrations with external vendors through secure HTTPS connections, using the TLS 1.2 protocol.

For services performed in the Checkout module, where there is an exchange of data with sellers that are not part of VTEX (external fulfillment), the following ciphers are supported for the external seller, so that the flow of information occurs correctly.

>⚠️ TLS 1.0 and 1.1 integration protocols are not supported by VTEX.

| Cipher Suite Name (IANA)      | Name (OpenSSL)      |
| ---------- | ---------- |
|   TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384  |   ECDHE-RSA-AES256-SHA384    |
|   TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256  |   ECDHE-RSA-AES128-SHA256    |
|   TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA        |   ECDHE-RSA-AES256-SHA          |
|   TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA        |   ECDHE-RSA-AES128-SHA          |
|   TLS_DHE_RSA_WITH_AES_256_GCM_SHA384    |    DHE-RSA-AES256-GCM-SHA384         |
|   TLS_DHE_RSA_WITH_AES_128_GCM_SHA256    |    DHE-RSA-AES128-GCM-SHA256         |
|   TLS_RSA_WITH_AES_256_GCM_SHA384  |   AES256-GCM-SHA384    |
|   TLS_RSA_WITH_AES_128_GCM_SHA256  |   AES128-GCM-SHA256    |
|   TLS_RSA_WITH_AES_256_CBC_SHA256        |   AES256-SHA256          |
|   TLS_RSA_WITH_AES_128_CBC_SHA256       |   AES128-SHA256          |
|   TLS_RSA_WITH_AES_256_CBC_SHA    |    AES256-SHA         |
|   TLS_RSA_WITH_AES_128_CBC_SHA    |    AES128-SHA         |
|   TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384  |   ECDHE-ECDSA-AES256-GCM-SHA384    |
|   TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256  |   ECDHE-ECDSA-AES128-GCM-SHA256    |
|   TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384        |   ECDHE-ECDSA-AES256-SHA384          |
|   TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256       |   ECDHE-ECDSA-AES128-SHA256          |
|   TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA    |    ECDHE-ECDSA-AES256-SHA         |
|   TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA    |    ECDHE-ECDSA-AES128-SHA         |
|   LS_DHE_DSS_WITH_AES_256_CBC_SHA256  |   DHE-DSS-AES256-SHA256    |
|   TLS_DHE_DSS_WITH_AES_128_CBC_SHA256  |   DHE-DSS-AES128-SHA256    |
|   TLS_DHE_DSS_WITH_AES_256_CBC_SHA        |   DHE-DSS-AES256-SHA          |
|   TLS_DHE_DSS_WITH_AES_128_CBC_SHA       |   DHE-DSS-AES128-SHA          |
|   TLS_RSA_WITH_3DES_EDE_CBC_SHA    |    DES-CBC3-SHA         |
|   TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA    |    EDH-DSS-DES-CBC3-SHA         |
