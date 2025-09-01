---
slug: "new-tls-security-protocol-cryptographic-cipher-suite-required-for-pci-dss-compliance-guidelines"
title: "New TLS security protocol cryptographic cipher suite required for PCI-DSS compliance guidelines"
createdAt: 2023-12-08T00:00:00.000Z
hidden: false
type: "added"
excerpt: "New cipher suite required for PCI-DSS compliance guidelines."
---
TLS (Transport Layer Security) is a security and privacy protocol applied to online data transfers. To meet the requirements of the [PCI-DSS security protocols](https://www.pcisecuritystandards.org/document_library/?category=pcidss&document=pci_dss), which regulate security best practices for processing credit and debit card data, you must update the TLS cryptographic cipher suite used by your payment or anti-fraud provider to communicate with VTEX.

## What changed?

After January 31, 2024, VTEX payment systems will only accept the TLS 1.2 communication protocol using the following cipher suites:

- TLS_AES_128_GCM_SHA256
- TLS_AES_256_GCM_SHA384
- TLS_CHACHA20_POLY1305_SHA256
- ECDHE-ECDSA-AES128-GCM-SHA256
- ECDHE-RSA-AES128-GCM-SHA256
- ECDHE-ECDSA-AES256-GCM-SHA384
- ECDHE-RSA-AES256-GCM-SHA384

> ⚠️ VTEX does not support the TLS 1.0 and 1.1 protocols. Also, the previous TLS 1.2 cryptographic cipher suite will no longer be supported after this update.

## What needs to be done?

You must update the cipher suite used by your payment or anti-fraud provider to communicate with VTEX payment systems to meet the requirements of the TLS 1.2 protocol by January 31, 2024.

> ⚠️ After January 31, 2024, all payment or anti-fraud providers that do not use the TLS 1.2 protocol with the above-mentioned cipher suites will have their communications with the VTEX payment gateway interrupted.
