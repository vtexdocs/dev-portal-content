---
title: "Profile System"
slug: "profile-system"
hidden: true
createdAt: "2022-02-22T22:28:50.366Z"
updatedAt: "2022-08-19T18:42:00.613Z"
---
>❗ This feature is in closed beta phase, meaning we are working to improve it. Do not share this documentation with people outside of your company.

VTEX’s Profile System provides APIs that enable stores to:
- Deal with a single source of truth for shoppers’ data.
- [Safely store](https://developers.vtex.com/docs/guides/data-privacy) PII and sensitive information.

Below you can learn more about some of the Profile System’s features and how to integrate with the APIs.

[block:callout]
{
  "type": "warning",
  "body": "Data stored in the new Profile System is not related to documents saved in Master Data v1 or v2. The API endpoints and features described in this article only apply to documents registered in the new Profile System."
}
[/block]

>❗ When implementing your integration:
>
> Do not forget to check the [Adaptations and limitations](https://developers.vtex.com/docs/guides/changes-and-limitations-pii-data-architecture) that impact other integrations.
>
> Note that, at the moment, Master Data triggers are not supported by the PII platform version Profile System.

## Permission

To use the Profile System features, ensure you have the appropriate [License Manager resources](https://help.vtex.com/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) enabled for that user.

| Product | Category | Resource | Description |
| ---- | ---- | ---- | ---- |
| Profile System | Documents | Get Item | Get items in Profile System entities |
| Profile System | Documents | Save and Update Item | Edit items from Profile System. |
| Profile System | Documents | Delete Item | Delete items from Profile System. |

[block:callout]
{
  "type": "info",
  "body": "Learn more about License Manager [roles](https://help.vtex.com/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) and [resources](https://help.vtex.com/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3)."
}
[/block]
## TTL

Profile System documents have a defined TTL, which means Time To Live. This means that whenever a customer creates a profile, it will be deleted after the TTL has passed from the time of its creation.

You may set a document's TTL, with the query parameter `ttl` allowed for requests that create or update documents.


## Alternative keys

Shopper profiles and addresses are accessible via API by a unique `profileId`. However, it is also possible to use alternative keys. Currently, there are two allowed alternative keys:
- `email`
- `document`
[block:callout]
{
  "type": "warning",
  "body": "Note that, in this context, the `document` field means the document number registered by the store customer."
}
[/block]
To do this, you must replace the `profileId` path parameter with the key of your choice and send the name of the field that will be used in the query parameter `alternativeKey`.


## Masked data

After registering customer information to the Profile System, such as profile and address, it will be returned as masked by the default `GET` requests.

There are specific endpoints from which to get unmasked data. When using those, mind this query parameter:

| Parameter    | Required | Type   | Description                                           |
|--------------|----------|--------|-------------------------------------------------------|
| `reason`     | Yes      | String | Reason for requesting unmasked data.                  |

### Examples

Masked profile

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

Unmasked profile

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


## API integration

There are several APIs you can integrate with in order to manage information regarding profiles and addresses. Below you can find some examples and links to the detailed API reference.


### Profiles

A profile is the main entity where a given customer’s data is stored. See the example below.

Example request body for profile creation

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

Example response when getting unmasked profile 

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

API endpoints:
- [Create client profile](https://developers.vtex.com/vtex-rest-api/reference/createclientprofile)
- [Get profile](https://developers.vtex.com/vtex-rest-api/reference/getprofile)
- [Update client profile](https://developers.vtex.com/vtex-rest-api/reference/updateclientprofile)
- [Delete client profile](https://developers.vtex.com/vtex-rest-api/reference/deleteclientprofile)
- [Get unmasked profile](https://developers.vtex.com/vtex-rest-api/reference/getunmaskedprofile)
- [Get profile by version](https://developers.vtex.com/vtex-rest-api/reference/getprofilebyversion)
- [Get unmasked profile by version](https://developers.vtex.com/vtex-rest-api/reference/getunmaskedprofilebyversion)


### Addresses

Addresses are linked to profiles and any profile can have as many addresses as it might need. This means that a valid `profileId` is necessary to perform any action regarding addresses.

Example request body for address creation

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

Example response when getting unmasked address

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

API endpoints:
- [Create client address](https://developers.vtex.com/vtex-rest-api/reference/createclientaddress)
- [Get client addresses](https://developers.vtex.com/vtex-rest-api/reference/getclientaddresses)
- [Get unmasked client addresses](https://developers.vtex.com/vtex-rest-api/reference/getunmaskedclientaddresses)
- [Get address](https://developers.vtex.com/vtex-rest-api/reference/getaddress)
- [Update client address](https://developers.vtex.com/vtex-rest-api/reference/updateclientaddress)
- [Delete address](https://developers.vtex.com/vtex-rest-api/reference/deleteaddress)
- [Get unmasked address](https://developers.vtex.com/vtex-rest-api/reference/getunmaskedaddress)
- [Get address by version](https://developers.vtex.com/vtex-rest-api/reference/getaddressbyversion)
- [Get unmasked address by version](https://developers.vtex.com/vtex-rest-api/reference/getunmaskedaddressbyversion)


### Prospects

API endpoints:
- [Create prospect](https://developers.vtex.com/vtex-rest-api/reference/createprospect)
- [Get prospect](https://developers.vtex.com/vtex-rest-api/reference/getprospect)
- [Update prospect](https://developers.vtex.com/vtex-rest-api/reference/updateprospect)
- [Delete prospect](https://developers.vtex.com/vtex-rest-api/reference/deleteprospect)
- [Get unmasked prospect](https://developers.vtex.com/vtex-rest-api/reference/getunmaskedprospect)


### Purchase information

API endpoints:
- [Create purchase information](https://developers.vtex.com/vtex-rest-api/reference/createpurchaseinformation)
- [Get purchase information](https://developers.vtex.com/vtex-rest-api/reference/getpurchaseinformation)
- [Update purchase information](https://developers.vtex.com/vtex-rest-api/reference/updatepurchaseinformation)
- [Delete purchase information](https://developers.vtex.com/vtex-rest-api/reference/deletepurchaseinformation)
- [Get unmasked profile information](https://developers.vtex.com/vtex-rest-api/reference/getunmaskedpurchaseinformation)