---
title: "Headless profile management and order history"
slug: "headless-profile-management-and-order-history"
hidden: false
createdAt: "2021-03-31T21:21:53.940Z"
updatedAt: "2023-05-29T21:21:53.940Z"
---

Profile management is an important feature, that allows shoppers in your store to view and edit their personal information, as well as order history and other features.

VTEX's native storefront accomplishes this with the [My account page](https://help.vtex.com/pt/tutorial/how-my-account-works--2BQ3GiqhqGJTXsWVuio3Xh), but below you can learn how to use VTEX APIs to build the same features in your headless shopping experience.

## Profile management

Regarding profile management, your integration must be able to [access profile information](#access-profile-information), [edit profile information](#edit-profile-information) and also perform [password resets](#password-reset).

### Accessing profile information

The best way to retrieve shopper profile information on your headless storefront is to use this endpoint of the Checkout API:

- [Get client profile by email](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/profiles)

By default, this endpoint returns only complete profiles, but you may use the boolean query parameter `ensureComplete=false` to get incomplete profiles as well.

>ℹ️ A complete profile includes all information necessary to place an order: `email`, `firstName`, `lastName`, `phone`, `document`, and an associated address with all required fields.

### Editing profile information

VTEX uses [Master Data v1](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw) to store and manage shopper information. To manage profile data from your headless storefront, you must use the [SafeData app](https://developers.vtex.com/docs/apps/vtex.safedata), which provides a secure middleware layer for retrieving and storing Master Data information directly from the frontend.

>ℹ️ Learn more about [Master Data](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#versions-available) and its [basic components](https://help.vtex.com/en/tutorial/master-data--4otjBnR27u4WUIciQsmkAw#basic-components).

>⚠️ **Before you begin**: Install the SafeData app in your VTEX account. SafeData acts as a validation layer on top of Master Data API to ensure the data being queried or modified belongs to the user executing the action. For more information, refer to the [SafeData documentation](https://developers.vtex.com/docs/apps/vtex.safedata).

In Master Data v1, shopper profiles are documents in the `CL` data entity, while addresses are documents in the `AD` data entity. The SafeData app provides endpoints similar to Master Data endpoints, but with built-in security validation. See below the SafeData endpoints for managing documents:

- **Update partial document**: `PATCH /api/io/safedata/{entity}/documents/{id}`
- **Get document by ID**: `GET /api/io/safedata/{entity}/documents/{id}`

>ℹ️ The SafeData API uses the pattern `/api/io/safedata/{entity}/documents/{id}`, where `{entity}` is the data entity acronym (e.g., `CL` for customer profiles, `AD` for addresses) and `{id}` is the document ID.

**Example request to update a user profile:**

**Method:** `PATCH`

**Path:**
```
https://{{accountName}}.vtexcommercestable.com.br/api/io/safedata/CL/documents/{{documentId}}
```

**Body:**
```json
{
  "firstName": "John",
  "lastName": "Doe",
  "email": "john.doe@example.com",
  "phone": "+5511999999999"
}
```

If you prefer to search shopper information by other information, such as email address, instead of the document ID, you can use the Checkout API endpoint mentioned in the [Accessing profile information](#accessing-profile-information) section above.

### Password

Currently, there is no way to edit shoppers' passwords from a headless frontend. However, you can implement password expiration, so that your customers can then go to your store and create a new password.

To implement this feature, follow the instructions in the guide [Expiring a shopper's password](https://developers.vtex.com/docs/guides/expiring-a-shoppers-password).

>❗ This method of password expiration does not trigger any notification. You must notify the shopper that they must create a new password on your website. Learn more about [Shopper authentication for headless stores](https://developers.vtex.com/docs/guides/headless-commerce#authenticating-shopper-identity).

### News letter subscription

When shoppers go to the profile management section of your store, they may wish to manage their consent of newsletter subscription. For this purpose, note that this information is in the shopper profile, in the boolean field named `isNewsletterOptIn`.

## Order history

You can use the endpoints below to fetch order information related to a specific shopper.

- [Retrieve list of user's orders](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/user/orders)
- [Retrieve user order details](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/user/orders/-orderId-)

### Actions on existing orders

Some stores allow shoppers to request changes or even the cancellation of existing orders. For order cancelation, use this endpoint:

- [Cancel order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/cancel)

For requesting changes to an existing order, you can use the endpoint below, but see the [Change order guide](https://developers.vtex.com/docs/guides/change-order) to learn more about this process.

- [Register change on order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/changes)

## Learn more

See these other guides to learn more about building a headless shopping experience using VTEX:

- [Headless commerce overview](https://developers.vtex.com/docs/guides/headless-commerce)
- [Headless catalog and search](https://developers.vtex.com/docs/guides/headless-catalog)
- [Headless cart and checkout](https://developers.vtex.com/docs/guides/headless-cart-and-checkout)
