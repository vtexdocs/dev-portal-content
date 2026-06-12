---
title: "Granular permissions for Seller Register API and Marketplace Network"
slug: "2025-12-23-granular-permissions-seller-marketplace-api"
type: "improved"
createdAt: "2025-12-23T11:00:00.000Z"
excerpt: "New explicit permissions model for Seller Register API requires specific resources in access profiles."
tags:
    - "Marketplace"
    - "Sellers"
---

We have implemented an explicit permissions validation model for Seller and Marketplace Network services, replacing the previous implicit authorization model based on account level. This change is available to all platform users.

>⚠️ You must complete the permission configuration by **March 1, 2026**. After this date, requests without the proper permissions will be blocked.

## What changed?

Previously, any authenticated user with basic account access had implicit permission to operate the Seller and Marketplace Network modules through the API. With this update, the system requires the user or application key (`appKey`) to have specific access resources associated with their profile to interact with API endpoints.

### New access resources

| Service | Resource | Description |
| :---- | :---- | :---- |
| Seller Register | `View Seller` | Allows querying seller data (GET endpoints) |
| Seller Register | `Save Seller` | Allows creating and editing sellers (POST/PUT/PATCH endpoints) |
| Marketplace Network | `Access the Marketplace Network` | Allows full access to the module |

### Impact on integrations

Automated requests (ERPs, middlewares, custom integrations) using `appKeys` that do not receive the new permissions will return:

```txt
HTTP 403 Forbidden
```

### Affected endpoints

All [Seller Register API](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/seller-register/pvt/sellers) endpoints now require `View Seller` or `Save Seller` resources depending on the operation:

- **GET requests:** Require `View Seller`
- **POST/PUT/PATCH requests:** Require `Save Seller`

## Why did we make this change?

To align the modules with the security principle of Least Privilege, raising the platform's level of governance and security. Key benefits:

- **Permission segregation:** Clear distinction between users who only query data and users who can modify configurations.
- **Granular control:** Administrators can configure specific access profiles for each use case.
- **Reduced operational risk:** Prevention of accidental or unauthorized changes to critical seller configurations.

## What needs to be done?

### For application keys (appKeys)

1. Go to **Account Settings > User Roles** in the VTEX Admin.
2. Identify the profiles linked to `appKeys` that make calls to the Seller Register API.
3. Edit the profile and add the necessary resources:
   - `View Seller` (under "Seller Register") for read operations
   - `Save Seller` (under "Seller Register") for write operations
   - `Access the Marketplace Network` (under "Channels") if applicable
4. Save and perform test calls to validate.

### For Admin users

1. Go to **Account Settings > User Roles**.
2. Identify the profiles of users who interact with sellers.
3. Add resources according to the required access level.
4. Validate access to modules in the VTEX Admin.

### API validation example

```bash
curl --request GET \
  --url https://{accountName}.vtexcommercestable.com.br/api/seller-register/pvt/sellers \
  --header 'Accept: application/json' \
  --header 'X-VTEX-API-AppKey: {appKey}' \
  --header 'X-VTEX-API-AppToken: {appToken}'
```

If the response is `403 Forbidden`, the `appKey` does not have the required permissions.

For more information, see the [User Roles documentation](https://help.vtex.com/en/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc) and the [Seller Register API Reference](https://developers.vtex.com/docs/api-reference/marketplace-apis).
