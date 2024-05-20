---
title: "PII Data Architecture specifications"
slug: "pii-data-architecture-specifications"
hidden: false
createdAt: "2023-05-16T09:38:36.446Z"
updatedAt: "2023-05-16T09:38:36.446Z"
seeAlso:
 - "/docs/guides/data-protection-plus"
 - "/docs/guides/data-residency"
 - "/docs/guides/profile-system"
 - "/docs/guides/limitations-of-the-pii-data-architecture-during-closed-beta"
 - "/docs/guides/changes-in-vtex-features-behavior-to-handle-pii-data"
---

>⚠️ [Data Protection Plus](https://developers.vtex.com/docs/guides/data-protection-plus) is in closed beta phase, only available in select regions.<br /><br />
> This feature is part of [VTEX Shield](https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh). If you are already a VTEX customer and want to adopt VTEX Shield for your business, please contact [Commercial Support](https://help.vtex.com/en/tracks/support-at-vtex--4AXsGdGHqExp9ZkiNq9eMy/3KQWGgkPOwbFTPfBxL7YwZ). Additional fees may apply. If you are not yet a customer but are interested in this solution, please complete our [contact form](https://vtex.com/us-en/contact/).

VTEX's comprehensive PII data architecture, available for stores using [Data Protection Plus](https://developers.vtex.com/docs/guides/data-protection-plus), incorporates a range of solutions and processes for managing personally identifiable information (PII). Here you can find detailed information about how this architecture works to ensure the protection of shoppers' data privacy.

Read the sections below to learn more about:

- [Profile system](#profile-system)
  - [Data entities](#data-entities)
  - [Communication with other VTEX modules](#communication-with-other-vtex-modules)
  - [Versioning](#versioning)
- [Encryption](#encryption)
- [Tokenization](#tokenization)
- [Default data masking](#default-data-masking)
- [Auditability](#auditability)
- [Marketplaces](#marketplaces)
  - [Scenario 1: Your store acts as a marketplace](#scenario-1-your-store-acts-as-a-marketplace)
  - [Scenario 2: Your store acts as a seller](#scenario-2-your-store-acts-as-a-seller)
- [Changes in VTEX features default behavior](#changes-in-vtex-features-default-behavior)
- [Limitations during closed beta](#limitations-during-closed-beta)

## Profile system

The [Profile System](https://developers.vtex.com/docs/guides/profile-system) is VTEX's single source of truth regarding shoppers' profile data, for stores using [Data Protection Plus](https://developers.vtex.com/docs/guides/data-protection-plus). Other modules, such as **Checkout** and **Order Management**, can request data from the **Profile System** when necessary.

This means that **Profile System** information is subject to specific data guidelines and processes, appropriate to handling PII. These specifications also apply whenever other VTEX modules communicate with the **Profile System**. In the following sections, you can learn more about these specifications.

You can integrate with the Profile System via its REST APIs, as described in the [Profile System integration guide](https://developers.vtex.com/docs/guides/profile-system).

>ℹ️ The **Profile System** does not hold credit card information. Instead, all credit card data, including billing addresses, is processed and stored in a [PCI-compliant](https://help.vtex.com/tutorial/what-is-the-pci-ssc--4jo3Vkox3amSO2w4qIWa0E) manner for all VTEX stores, regardless of any differences in data architecture. This ensures that VTEX adheres to the best practices of data protection regulations related to handling credit card PII. Learn more about [VTEX PCI certification](https://secure.vtex.com/?an=VTEX).

### Data entities

The Profile System has three data entities:

- **Prospect:** information entered by shoppers during cart and Checkout flow.
- **Profile:** prospect information can become a profile if the shopper creates a profile, which can happen via order placement, manual profile creation, or [single sign-on integrations](https://developers.vtex.com/docs/guides/authentication-overview#single-sign-on-integrations).
- **Address:** once a prospect or profile places an order, the shipping address information is saved and associated with the respective profile. Note that a single profile may be associated with multiple shipping addresses.

>ℹ️ The **address** data entity only stores shipping addresses. All credit card related PII, including billing addresses, is stored and processed in a [PCI compliant](https://help.vtex.com/tutorial/what-is-the-pci-ssc) manner for all VTEX stores, regardless of any differences in data architecture.

### Communication with other VTEX modules

Some VTEX modules may need to access PII data from the Profile System: Checkout, Order Management and Message Center's transactional emails. Consider, for instance, a shopper that wishes to see their previous order history, including addresses and payment methods used at your store. In this case, the Order Management module must be able to display their own PII to them.

>ℹ️ Although shopper data flows from Checkout to the Profile System, no data is stored by the Checkout module. The same applies to Order Management and Message Center's transactional emails, as these may access shopper data from the Profile System at times, but do not keep any of it.

The diagram below shows the information flow whenever another VTEX module requests unmasked PII from the Profile System.

```mermaid
sequenceDiagram
	VTEX module->>Profile System: Requester, shopper token, reason
	Profile System->>License Manager: Requester credentials, Shopper token, Reason
	License Manager-->>Profile System: Authorized
	Profile System->>Audit: Requester, shopper token, reason
	Profile System->>Profile System database: Shopper token
	Profile System database->>Profile System: PII
	Profile System->>VTEX module: PII
```

When another VTEX module needs [unmasked](#default-data-masking) information from the Profile System it may request it, while informing:

- Shopper [token](#tokenization).
- Requester credentials.
- Reason for requesting data.

Then the Profile System proceeds with the following actions:

1. Check whether the requester can access that data. If they do, it proceeds to the next steps.
2. Log [Audit](#auditability) event.
3. Retrieve [encryption key](#encryption) from the encryption key management system.
4. Decrypt information.
5. Return information to the requester.

These steps ensure access control with specific authorization and auditability of each access.

### Versioning

The Profile System works with versioning, meaning that each [token](#tokenization) may have multiple versions. Because of this, every change is safely stored and other modules' related information, such as order history is not compromised due to profile changes made by users.

## Encryption

All PII is encrypted with a unique key for each store. The [Profile System](#profile-system) uses AES GCM with an encryption key of 256 bits. VTEX does not share the encryption keys with any external entity, not even with the corresponding merchants.

>ℹ️ The encryption key management system is a separate system and can only be accessed by the Profile System.

## Tokenization

All PII is tokenized, meaning it is indexed under a token, which is a unique shopper ID internal to VTEX.

The diagram below exemplifies this communication in the case of a [Get order request](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) from the Payments module to Order Management.

```mermaid
sequenceDiagram
	Payments->>Order management: Get order
	Order management->>Payments: Order information with pseudonymised profile data
```

Modules may need to index PII information for purposes such as search. In this case, the data is hashed, meaning it can not be reversed. This minimizes requests to the [Profile System](#profile-system) and overall latency of the shopping experience.

See how the platform hashes this data in this case:

1. Concatenate information with an account specific salt.
2. Apply SHA256 to the resulting string.

This process is irreversible. So the information is safe even if the request indexer data becomes exposed.

## Default data masking

PII is masked by default. This means that when you access a shopper's order history in VTEX Admin panel or when you request their profile information via API, for example, any PII information returned will be masked.

However, unmasked data can be requested by modules, integrations, and store operators with the appropriate [permissions](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc).

See examples, as returned by [Profile System APIs](https://developers.vtex.com/docs/guides/profile-system#masked-data).

Masked profile:

```json
{
    "id": "70caf394-8534-447e-a0ca-1803c669c771",
    "meta": {
        "version": "abc",
        "author": "e40e0b6d-0605-4fa6-8176-1d69fbaf0818",
        "creationDate": "13/12/2021T00:00:00Z",
        "lastUpdate": "13/12/2021T00:00:00Z"
    },
    "document": {
        "firstName": "J***",
        "lastName": "D**",
        "email": "j***.d**@e******.c**",
        "birthDate": "1925-11-17",
        "document": "1**********",
        "documentType": "CPF"
    }
}
```

Unmasked profile:

```json
{
    "id": "70caf394-8534-447e-a0ca-1803c669c771",
    "document": {
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "birthDate": "1925-11-17",
        "document": "12345678911",
        "documentType": "CPF"
    },
    "meta": {
        "version": "abc",
        "author": "e40e0b6d-0605-4fa6-8176-1d69fbaf0818",
        "creationDate": "13/12/2021T00:00:00Z",
        "lastUpdate": "13/12/2021T00:00:00Z"
    }
}
```

>ℹ️ Learn more about retrieving unmasked data with the [Profile System integration guide](https://developers.vtex.com/docs/guides/profile-system#masked-data).

## Auditability

The VTEX platform enables stores to audit actions of store operators with the [Audit module](https://help.vtex.com/en/tutorial/searching-for-events-on-audit--5RXf9WJ5YLFBcS8q8KcxTA), including actions related to personal data and PII.

Every successful request to unmasked personal data and PII generates a log on [Audit](https://help.vtex.com/en/tutorial/searching-for-events-on-audit--5RXf9WJ5YLFBcS8q8KcxTA). This includes the Id of the store operator that requested this information.

You can see the [list of events available on Audit](https://help.vtex.com/en/tutorial/eventos-disponiveis-no-audit--6r1Mzcu5NmkmmDLJlz9CCZ), but stores using the PII data architecture also log Profile System events, which you can see in the [Profile System integration guide](https://developers.vtex.com/docs/guides/profile-system#auditability).

## Marketplaces

The VTEX platform enables your store to be a marketplace and a seller to other marketplaces at the same time. Data privacy processes may impact your store in different ways depending on the roles your operation assumes in this context.

### Scenario 1: Your store acts as a marketplace

Shopper data belongs to the marketplace. Hence, if your VTEX store acts as a [marketplace](https://help.vtex.com/en/tutorial/marketplace-strategies-at-vtex--tutorials_402#acting-as-a-marketplace), selling products from other sellers, all specifications described in this guide apply.

Moreover, fulfillment information is shared with the seller. Therefore, you must ensure that your associated sellers also comply with data privacy laws.

### Scenario 2: Your store acts as a seller

If your VTEX store acts as a [seller](https://help.vtex.com/en/tutorial/marketplace-strategies-at-vtex--tutorials_402#selling-on-marketplaces), offering products in marketplaces, the specifications described in this guide apply to the fulfillment data received by your store from each marketplace.

The marketplace is your data source, so you must guarantee that marketplaces associated with your store also comply with data privacy laws.

## Changes in VTEX features default behavior

The behavior of some VTEX features has been adapted to better communicate with the PII data architecture. There are some differences in implementation when compared to the standard data architecture, such as API contracts and how information is displayed on VTEX Admin. Read [Changes in VTEX features behavior to handle PII data](https://developers.vtex.com/docs/guides/changes-in-vtex-features-behavior-to-handle-pii-data). This document is constantly updated to reflect the evolution of the PII data architecture.

## Limitations during closed beta

During closed beta testing stage, there are limitations in certain features for stores using PII data architecture. See this article about [Limitations of the PII data architecture during closed beta](https://developers.vtex.com/docs/guides/limitations-of-the-pii-data-architecture-during-closed-beta). This document is constantly updated to reflect the evolution of the PII data architecture.
