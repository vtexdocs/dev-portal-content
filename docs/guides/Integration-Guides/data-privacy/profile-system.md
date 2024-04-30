---
title: "Profile System integration"
slug: "profile-system"
hidden: false
createdAt: "2022-02-22T22:28:50.366Z"
updatedAt: "2022-08-19T18:42:00.613Z"
seeAlso:
 - "/docs/guides/data-protection-plus"
 - "/docs/guides/pii-data-architecture-specifications"
 - "/docs/guides/data-residency"
 - "/docs/guides/changes-in-vtex-features-behavior-to-handle-pii-data"
 - "/docs/guides/limitations-of-the-pii-data-architecture-during-closed-beta"
---

>⚠️ [Data Protection Plus](https://developers.vtex.com/docs/guides/data-protection-plus) is in closed beta phase, only available in select regions.<br /><br />
> This feature is part of [VTEX Shield](https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh). If you are already a VTEX customer and want to adopt VTEX Shield for your business, please contact [Commercial Support](https://help.vtex.com/en/tracks/support-at-vtex--4AXsGdGHqExp9ZkiNq9eMy/3KQWGgkPOwbFTPfBxL7YwZ). Additional fees may apply. If you are not yet a customer but are interested in this solution, please complete our [contact form](https://vtex.com/us-en/contact/).

The **Profile System** is VTEX's single source of truth regarding shoppers' profile data for stores using [Data Protection Plus](https://developers.vtex.com/docs/guides/data-protection-plus). Other modules, such as **Checkout** and **Order Management**, can request data from the **Profile System** when necessary.

The Profile System API enables stores to:

- Communicate with a single source of truth for shoppers' data.
- Safely store PII and sensitive information.

Below you can learn more about some of the Profile System's features and how to integrate with the APIs.

>⚠️ Data stored in the new Profile System is not related to documents saved in [Master Data v1](https://developers.vtex.com/docs/api-reference/masterdata-api) or [Master Data v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2). The API endpoints and features described in this article only apply to documents registered in the new Profile System designed to handle PII data architecture.

## Before you start

- Check the [changes in VTEX features behavior to handle PII data](https://developers.vtex.com/docs/guides/changes-in-vtex-features-behavior-to-handle-pii-data) that impact other integrations.
- Check the [current limitations related to PII data architecture](https://developers.vtex.com/docs/guides/limitations-of-the-pii-data-architecture-during-closed-beta). Note that, at the moment, [Master Data triggers](https://help.vtex.com/en/tutorial/creating-trigger-in-master-data--tutorials_1270) are not supported by the PII platform version Profile System, for example.

## Permission

To use the Profile System features, ensure you have the appropriate [License Manager resources](https://help.vtex.com/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) enabled for that user.

| Product | Category | Resource | Description |
| ---- | ---- | ---- | ---- |
| Profile System | Documents | Get Item | Get items in Profile System entities |
| Profile System | Documents | Save and Update Item | Edit items from Profile System. |
| Profile System | Documents | Delete Item | Delete items from Profile System. |

>ℹ Learn more about License Manager [roles](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) and [resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3).

## Auditability

You can use the [Audit app](https://help.vtex.com/tutorial/searching-for-events-on-audit--5RXf9WJ5YLFBcS8q8KcxTA) to check actions made using the Profile System in your account.

>ℹ️ Learn more about [how to audit actions in the VTEX platform](https://help.vtex.com/tutorial/searching-for-events-on-audit--5RXf9WJ5YLFBcS8q8KcxTA).

See the table below to learn more about the Profile System events available on Audit.

| **Action**                   | **Description**                                      | **Event details**                     |
|------------------------------|------------------------------------------------------|---------------------------------------|
| GetProfileVersionUnmasked    | Retrieval of an unmasked profile by ID and version.  | Profile ID and version ID.            |
| EmailRectification           | Change existing email address.                       | ID of user whose email was rectified. |

## TTL

Profile System documents have a defined TTL, which means Time To Live. This means that whenever a customer creates a profile, it will be deleted after the TTL has passed from the time of its creation.

You may set a document's TTL, with the query parameter `ttl` allowed for requests that create or update documents.

## Alternative keys

Shopper profiles and addresses are accessible via API by a unique `profileId`. However, it is also possible to use alternative keys. Currently, there are two allowed alternative keys:

- `email`
- `document`

>⚠️ Note that, in this context, the `document` field means the document number registered by the store customer.

To do this, you must replace the `profileId` path parameter with the key of your choice and send the name of the field that will be used in the query parameter `alternativeKey`.

## Masked data

After registering customer information to the Profile System, such as profile and address, it will be returned as masked by the default `GET` requests.

There are specific endpoints from which to get unmasked data. When using those, mind this query parameter:

| Parameter    | Required | Type   | Description                                           |
|--------------|----------|--------|-------------------------------------------------------|
| `reason`     | Yes      | String | Reason for requesting unmasked data.                  |

<details>
<summary>Masked profile example</summary>

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

</details>

<details>
<summary>Unmasked profile example</summary>

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

</details>

## Profile System API reference

There are several APIs you can integrate with in order to manage information regarding profiles and addresses. Below you can find some examples and links to the detailed API reference.

### Profiles

A profile is the main entity where a given customer’s data is stored.

- `POST` [Create client profile](https://developers.vtex.com/docs/api-reference/profile-system#post-/api/storage/profile-system/profiles)
- `GET` [Get profile](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-)
- `PATCH` [Update client profile](https://developers.vtex.com/docs/api-reference/profile-system#patch-/api/storage/profile-system/profiles/-profileId-)
- `DELETE` [Delete client profile](https://developers.vtex.com/docs/api-reference/profile-system#delete-/api/storage/profile-system/profiles/-profileId-)
- `GET` [Get unmasked profile](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-/unmask)
- `GET` [Get profile by version](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-/versions/-profileVersionId-)
- `GET` [Get unmasked profile by version](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-/versions/-profileVersionId-/unmask)

<details>
<summary>Example request body for profile creation</summary>

```json
{
    "firstName": "John",
    "lastName": "Doe",
    "email": "john.doe@example.com",
    "birthDate": "1925-11-17",
    "document": "12345678911",
    "documentType": "CPF"
}
```

</details>

<details>
<summary>Example response when getting unmasked profile</summary>

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

</details>

### Addresses

Addresses are linked to profiles and any profile can have as many addresses as it might need. This means that a valid `profileId` is necessary to perform any action regarding addresses.

- `POST` [Create client address](https://developers.vtex.com/docs/api-reference/profile-system#post-/api/storage/profile-system/profiles/-profileId-/addresses)
- `GET` [Get client addresses](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-/addresses)
- `GET` [Get unmasked client addresses](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-/addresses/unmask)
- `GET` [Get address](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-/addresses/-addressId-)
- `PATCH` [Update client address](https://developers.vtex.com/docs/api-reference/profile-system#patch-/api/storage/profile-system/profiles/-profileId-/addresses/-addressId-)
- `DELETE` [Delete address](https://developers.vtex.com/docs/api-reference/profile-system#delete-/api/storage/profile-system/profiles/-profileId-/addresses/-addressId-)
- `GET` [Get unmasked address](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-/addresses/-addressId-/unmask)
- `GET` [Get address by version](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-/addresses/-addressId-/versions/-addressVersionId-)
- `GET` [Get unmasked address by version](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-/addresses/-addressId-/versions/-addressVersionId-/unmask)

<details>
<summary>Example request body for address creation</summary>

```json
{
    "postalCode": "20200-000",
    "countryName": "Brasil",
    "countryCode": "BR",
    "administrativeAreaLevel1": "RJ",
    "locality": "Locality",
    "localityAreaLevel1": "locality area",
    "route": "51",
    "streetNumber": "999",
    "profileId": "70caf394-8534-447e-a0ca-1803c669c771"
}
```

</details>

<details>
<summary>Example response when getting unmasked address</summary>

```json
{
    "id": "bf82180e-cf9e-4089-9af6-ae1518555992",
    "document": {
        "postalCode": "20200-000",
        "countryName": "Brasil",
        "countryCode": "BR",
        "administrativeAreaLevel1": "RJ",
        "locality": "Locality",
        "localityAreaLevel1": "locality area",
        "route": "51",
        "streetNumber": "999",
        "profileId": "70caf394-8534-447e-a0ca-1803c669c771"
    },
    "meta": {
        "version": "c9c44895-4589-4d0d-a28d-e0e656ca1926",
        "author": "80aa79a3-aa89-4912-a20e-8ef69af19a6c",
        "creationDate": "2022-01-18T18:51:34.1293829+00:00",
        "lastUpdateDate": "2022-01-18T18:51:34.1293829+00:00"
    }
}
```

</details>

### Prospects

- `POST` [Create prospect](https://developers.vtex.com/docs/api-reference/profile-system#post-/api/storage/profile-system/prospects)
- `GET` [Get prospects](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/prospects)
- `GET` [Get unmasked prospects](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/prospects/unmask)
- `GET` [Get prospect](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/prospects/-prospectId-)
- `PATCH` [Update prospect](https://developers.vtex.com/docs/api-reference/profile-system#patch-/api/storage/profile-system/prospects/-prospectId-)
- `DELETE` [Delete prospect](https://developers.vtex.com/docs/api-reference/profile-system#delete-/api/storage/profile-system/prospects/-prospectId-)
- `GET` [Get unmasked prospect](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/prospects/-prospectId-/unmask)

### Purchase information

- `POST` [Create purchase information](https://developers.vtex.com/docs/api-reference/profile-system#post-/api/storage/profile-system/profiles/-profileId-/purchase-info)
- `GET` [Get purchase information](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-/purchase-info)
- `PATCH` [Update purchase information](https://developers.vtex.com/docs/api-reference/profile-system#patch-/api/storage/profile-system/profiles/-profileId-/purchase-info)
- `DELETE` [Delete purchase information](https://developers.vtex.com/docs/api-reference/profile-system#delete-/api/storage/profile-system/profiles/-profileId-/purchase-info)
- `GET` [Get unmasked purchase information](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/profiles/-profileId-/purchase-info/unmask)

### Schemas

A JSON Schema defines the structure of data stored in the Profile System. It determines, for example, which fields a profile has and their respective formats. Read [Working with schemas in the Profile System](https://developers.vtex.com/docs/guides/working-with-schemas-in-the-profile-system) for more information.

The following endpoints allow you to interact with the profile schema:

- `GET` [Get full schema](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/schemas/profileSystem)
- `PUT` [Create or delete custom fields](https://developers.vtex.com/docs/api-reference/profile-system#put-/api/storage/profile-system/schemas/profileSystem/custom)
- `GET` [Get custom fields](https://developers.vtex.com/docs/api-reference/profile-system#get-/api/storage/profile-system/schemas/profileSystem/custom)
