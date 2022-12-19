---
title: "Querying personal MasterData Information with SafeData"
slug: "vtex-safedata"
excerpt: "vtex.safedata@1.0.1"
hidden: false
createdAt: "2021-06-01T18:05:47.887Z"
updatedAt: "2022-09-15T20:59:44.867Z"
---
The SafeData app provides an easy to use, configurable middleware to retrieve and save MasterData (V1 & V2) information directly on the front-end, or through another back-end.

It works by acting as an validation layer on top of MasterData API to ensure the data being queried belongs to the user executing the action.

## Getting Started

You can install it through the app store or the command-line interface:

```
vtex install vtex.safedata@0.x
```

The base configurations for CL (Client) and AD (Address) entities are automatically configured but can be changed by using the app settings interface which is currently in progress.

Upon installing, some public routes will become instantly available to use.

## Syntax

SafeData respects the same MasterData routes which can be accessed by replacing `api/dataentities` for `safedata`:

For example, you need to query the address `AD` entity by the addressName (`addressName=12345`):

#### Path

To implement SafeData in a store, you need to insert the path `api/io` to your endpoint before `safedata`, for example:
`GET https://myaccount.myvtex.com/api/io/safedata/AD/search?_where=addressName=12345`

## Supported Routes

As of this writing, SafeData supports the following routes:

- Get document:
`GET /safedata/{entity}/documents/{documentId}`

- Search documents:
`GET /safedata/{entity}/search`

- Create document:
`POST /safedata/{entity}/documents`

- Create or update document:
`PATCH /safedata/{entity}/documents`

- Entire document update:
`PUT /safedata/{entity}/documents/{documentId}`

- Partial document update:
`PATCH /safedata/{entity}/documents/{documentId}`

All underscore query parameters are supported (_where, _fields, _schema and so on).

## GraphQL interface

SafeData also provides a `patchDocument` mutation in GraphQL which enables react components (IO) to create/update documents in MasterData. 

The schema is as follows:

![GraphQL](https://user-images.githubusercontent.com/1629129/127065235-fcf682d2-4b15-42d2-8d9b-b7b2df7d1d81.png)

`fields` is a Key/Value pair for each MD field.

This is still a work-in-progress, so for now only the `PATCH` functionality is available.

## Working with custom checkout fields

When a client is making their first purchase, the `CL` entity may be created preemptively if the store has specific customizations to include new fields in the checkout process, i.e., birth date. This could cause problems since SafeData forbids customers to change personal data when they are not logged in. To avoid this problem, you can add the query parameter `_orderFormId` so SafeData can ensure the customer can safely change their information since it's their first checkout. See the following example:

`PATCH /safedata/CL/documents?_orderFormId=7217c9c7413142dd93e3b715f95cd03d` with this payload:
```json
{
  "email": "my_email@domain.com",
  "birthDate": "1990-10-11T00:00:00"
}
```

When this request is called for the first time the user does not exist, so it is allowed to be created anonymously.

In subsequent calls, SafeData checks the `_orderFormId` to ensure the user was created in this checkout session, so they can update their information without asking for credentials.

This allows users to update their personal information during the checkout process without logging in, ONLY during the first purchase.

Once a purchase is finished, a complete profile is generated, and in order to update this information again the user has to log in (as expected by design)

Please be aware that currently ONLY the `PATCH /documents` route supports the `_orderFormId` parameter, and that it only works with entities that contain an `email` field in their schema.

## How does SafeData work?

The whole process is based on the `CL` entity, which is used as a guide to identify the user. First, we reach out to Vtex ID to confirm the `StoreUserAuthToken` is valid and get the user e-mail. Then we retrieve only the necessary fields on the `CL` entity to ensure the user is manipulating/obtaining only entities that belongs to them.

This is done through a field comparison between `CL` and whatever entity is being queried. For instance, when searching for documents of the `AD` entity, we compare their `userId` to the `id` found in the `CL` entity, and the action is only allowed if they match.

> ⚠️ *The comparison fields **must** be searchable. However, they do not have to be public, and we do not recommend making any fields public.*

It is possible to allow other MasterData entities to follow these rules by registering them on the app settings:

![SafeData Config](https://user-images.githubusercontent.com/1629129/119353802-b9405d80-bc79-11eb-95b2-9cbc5574fb0a.png)

*Please be aware that the field options are currently unavailable, and users are allowed to update any fields.*

## Performance Impact

Querying and updating information through SafeData is by definition slower than doing so directly on MasterData, because of all the extra security checks. However, preliminary tests have shown that:
- The median execution time for create/update operations stays below 200ms
- Search operations depend heavily on the queries, but the median execution time stays between 50-100ms
- Get operations are very fast and usually take around 25ms
- Obtaining the current user credentials takes around 15ms per request

## Roadmap

- Delete operation
- White-listing updateable fields
- Scroll operation