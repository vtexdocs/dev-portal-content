---
title: "Profile system"
slug: "profile-system"
hidden: true
createdAt: "2022-02-22T22:28:50.366Z"
updatedAt: "2022-04-28T13:44:01.231Z"
---
[block:callout]
{
  "type": "danger",
  "body": "This feature is in closed beta phase, meaning we are working to improve it. Do not share this documentation with people outside of your company.",
  "title": "Closed beta"
}
[/block]
VTEX’s Profile System provides APIs that enable stores to:
- Deal with a single source of truth for shoppers’ data.
- [Safely store](https://developers.vtex.com/vtex-rest-api/docs/data-privacy) PII and sensitive information.

Below you can learn more about some of the Profile System’s features and how to integrate with the APIs.

[block:callout]
{
  "type": "danger",
  "body": "When implementing your integration, do not forget to check the [Adaptations and limitations](https://developers.vtex.com/vtex-rest-api/docs/adaptations-and-limitations) that impact other integrations."
}
[/block]
## TTL

Profile system documents have a defined TTL, which means Time To Live. This means that whenever a customer creates a profile, it will be deleted after the TTL has passed from the time of its creation.

You may set a document's TTL, with the query parameter `ttl` allowed for requests that create or update documents.


## Alternate keys

Shopper profiles and addresses are accessible via API by a unique `profileId`. However, it is also possible to use alternate keys. Currently, there are two allowed alternate keys:
- `email`
- `document`

To do this, you must replace the `profileId` path parameter with the key of your choice and send the name of the field that will be used in the query parameter `alternateKey`.


## Masked data

After registering customer information to the profile system, such as profile and address, it will be returned as masked by the default `GET` requests.

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