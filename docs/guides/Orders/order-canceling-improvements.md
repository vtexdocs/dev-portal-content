---
title: "Order canceling improvements"
slug: "order-canceling-improvements"
hidden: false
createdAt: "2023-08-17T13:21:05.725Z"
updatedAt: "2024-12-11T13:17:33.816Z"
---

There are many scenarios where canceling an order is necessary, whether on behalf of sellers, marketplaces or shoppers. To cover multiple scenarios, we made the following improvements in order cancellation:

- [Cancel order requested by shopper](#cancel-order-requested-by-shopper): When the marketplace customer care service cancels an order after a shopper requests it, now the seller is notified about the cancellation reason and whether or not it was made on behalf of the shopper.
- [Deny cancel order](#deny-cancel-order): After the [cancellation window](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196) period – or grace period –, now the seller can deny cancellation requests.

In each case, both seller and marketplace will be notified about changes, have access to information about each other's reasons for canceling and/or denying a cancel request, and sellers will know when the shopper requested the cancellation.

For information about this feature in VTEX Admin, see [Declining order cancelation](https://help.vtex.com/en/tutorial/declining-order-cancelation--F2n0h1TeQ5td540Gjyff4).

> In this article, the term marketplace will refer to VTEX marketplace and seller to VTEX seller. For more information, see [Marketplace strategies at VTEX](https://help.vtex.com/en/tutorial/marketplace-strategies-at-vtex--tutorials_402).

## Permissions

Using the endpoints mentioned in this article requires having the `Cancel order` [resource](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) associated with the user or integration key. This resource is included in the following [predefined roles](https://help.vtex.com/en/tutorial/predefined-roles--jGDurZKJHvHJS13LnO7Dy):

For more information, see [users](https://help.vtex.com/en/tutorial/managing-users--tutorials_512) and [License Manager resources](https://help.vtex.com/en/tutorial/license-manager-resources--3q6ztrC8YynQf6rdc6euk3) at VTEX.

## Cancel order requested by shopper

With the [Cancel order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/cancel) endpoint, now it is possible to indicate if the canceling request was demanded by the shopper or not. This is possible because of the new request body field `requestedByUser`. This is useful for sellers to know when the marketplace cancels an order on behalf of the shopper.

A common scenario is when the shopper contacts the marketplaces customer care service via telephone, for example, and requests an order cancellation. In the cancellation request, the customer care now can inform both marketplace and seller that the cancellation was demanded by the shopper.

> The [order flow](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196) for canceling orders remains the same.

### Diagram

The following image shows the flow when canceling an order on behalf of the shopper:

![cancel_by_user](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Orders/cancel_by_user.png)

The step by step is the following:

1. The shopper contacts the marketplace customer care service to cancel an order.
2. The customer care cancels it using the [Cancel order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/cancel) endpoint. The request body contains the reason for order cancellation and indicates if it was requested by the shopper.
3. The cancel order request notifies the seller about the cancellation reason and if the request came from the shopper or not.
4. VTEX seller cancels the order.

### Cancel order endpoint

See below the [Cancel order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/cancel) endpoint, where `orderId` corresponds to the ID of the order been canceled:

**POST -** `https://{accountName}.{environment}.com.br/api/oms/pvt/orders/{orderId}/cancel`

**cURL**

```sh
curl --request post \
--url 'https://{accountname}.{environment}.com.br/api/oms/pvt/orders/{{orderId}}/cancel' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'X-VTEX-API-AppKey: ' \
--header 'X-VTEX-API-AppToken: ' \
--data '{
           "reason": "string",
           "requestedByUser": boolean
       }'
```

### Request body

See below a request body example:

```json
{
  "reason" : "reason for cancellation",
  "requestedByUser" : true
}
```

The following table presents the request body fields’ description:

| Field | Type | Description |
|:---:|:---:|:---|
| `reason` | string | Brief explanation of why the order is being canceled. |
| `requestedByUser` | boolean | When set as `true`, the cancellation was requested by the shopper, and when set as `false`, the cancellation was not canceled on behalf of the shopper. |

### Response body

See below a response body example:

```json
{
  "date": "2023-08-04T15:45:02.1306363+00:00",
  "orderId": "1351761719659-01",
  "receipt": "38e0e47da2934847b489216d208cfd91"
}
```

The following table presents the response body fields’ description:

| Field | Type | Description |
|:---:|:---:|:---|
| `date` | string | Date and time of when the platform processed the cancellation request.  The format is according to ISO 8601 `YYYY-MM-DDThh:mm:ssTZD`, meaning a complete date plus hours, minutes, seconds and a decimal fraction of a second. For example, `2023-08-04T15:45:02.1306363+00:00`. |
| `orderId` | string | ID that identifies the order being canceled. |
| `receipt` | string | Protocol code generated by the update. It may be `null`. |

### Response status codes

The possible response status codes are shown in the table below:

| Status Code | Description |
|:---:|:---|
| 200 OK | The order was successfully canceled. |
| 403 Forbidden | Unauthorized request. Update the credentials used in the request and try again. |
| 404 Not Found | The requested order was not found. Check the order ID and try again. |
| 429 Too Many Requests | We were unable to process the request due to the high volume of submissions. Wait a few minutes before trying again. |
| 500 Internal Server Error | An unexpected application error occurred. Review the request data and try again. |

### Order after cancellation

After the seller agrees to cancel the order, as requested by the marketplace on behalf of the shopper, it reaches the `canceled` [status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196). By using one of the endpoints below, both seller and marketplace can retrieve cancellation information:

- GET - [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-)
- GET - [Retrieve user order details](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/user/orders/-orderId-)

The information will be in the `cancellationData` object of the response body, as shown in the example below:

```json
"cancellationData": { 
        "requestedByUser": true,
        "reason": "cancelation reason",
        "cancellationDate": "2023-08-04T15:45:02.1306363Z",
        "cancellationRequestId": "85835ab408514b52aa139e4236ce0c33"
    }
```

> Seller and marketplace will get the same order cancellation information.

The fields’ description are shown below:

| Response body field | Type | Description |
|:---:|:---:|:---|
| `cancellationData` | object | Object with information about the order cancellation. |
| `requestedByUser` | boolean | When set as `true`, the cancellation was requested by the shopper, and when set as `false`, the cancellation was not canceled on behalf of the shopper. |
| `reason` | string | Explanation of why the order was canceled. |
| `cancellationDate` | string | Date and time of when the platform processed the cancellation request.  The format is according to [ISO 8601](https://www.w3.org/TR/NOTE-datetime) `YYYY-MM-DDThh:mm:ssTZD`, meaning a complete date plus hours, minutes, seconds and a decimal fraction of a second. For example, `2023-08-04T15:45:02.1306363+00:00`  It could also be `2023-08-04T15:45:02.1306363Z`, where `Z` stands for zone in Time Zone Designator (TZD). `Z` is equal to `+hh:mm` or `-hh:mm`. |
| `cancellationRequestId` | string | ID that identifies the cancellation operation. |

## Deny cancel order

In the order flow, there is a [cancellation window](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196) period – or grace period – in which an order can be automatically canceled by the shopper. Except for that period, now the seller can deny order cancel requests, regardless if the cancellation request came from the shopper or the marketplace.

A common scenario for using this endpoint is when the marketplace works with sellers whose products are made on demand by each purchase. If a shopper contacts the marketplace customer care service via telephone demanding the order cancellation, and the marketplace cancels the order, now the seller can deny the cancellation request.

>⚠️ To deny an order cancellation request, the order status in the marketplace and seller must be the following:<p><ul><li>**Marketplace status:** `waiting-for-seller-decision`.</li><li>**Seller status:** `cancellation-requested`.</li></ul></p>

### Diagram

The following image shows the flow of denying an order’s cancel request outside the cancellation window:

![deny_cancel_request](https://raw.githubusercontent.com/vtexdocs/dev-portal-content/main/docs/guides/Orders/deny_cancel_request.png)

The step by step is the following:

1. The shopper contacts the marketplace to cancel an order.
2. After receiving the request, the marketplace sends a cancellation request to the seller.
    > At this point, the [order status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196) for the marketplace is `waiting-for-seller-decision`.
3. If the order is within the cancellation window period, this order is automatically canceled, which is the platform  default behavior. The next steps are for when the order is no longer within the cancellation window.
4. The seller receives the cancel order request and decides to accept it or not. The next steps are for when the seller decides not to cancel the order.
5. The seller’s request to deny the order cancellation and that notifies the marketplace, with the reason included.
6. After the marketplace receives the denial request, the order moves on in the order workflow, from the status below:
    - **For the marketplace**: `payment-approved`.
    - **For the seller**: `ready-for-handling` or `handling`, depending on which was the status before the cancel request.
7. **Optional:** marketplace can, via webhook, notify a subscribed shopper about the order change in `payment-approved` and `cancellation-request-denied` status. It is also possible for some applications to collect the order cancellation denial reason given by the seller and inform the shopper.

### Deny cancel order endpoint

See below the endpoint deny order cancellation, where `orderId` corresponds to the ID of the order witches cancellation is being denied:

**POST -** `[https://{accountName}.{environment}.com.br/api/orders/pvt/document/{OrderId}/deny-cancellation-request](https://{accountName}.{environment}.com.br/api/orders/pvt/document/{OrderId}/deny-cancellation-request)`

**cURL**

```sh
curl --request post \
--url 'https://{accountname}.{environment}.com.br/api/oms/pvt/orders/{{orderId}}/deny-cancellation-request' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'X-VTEX-API-AppKey: ' \
--header 'X-VTEX-API-AppToken: ' \
--data '{
         "cancellationRequestId": "cancellationRequestId",
         "denyReason": "dIt isnandRIt isasOn"
      }'
```

### Request body

See below a request body example:

```json
{
  "cancellationRequestId": "85835ab408514b52aa139e4236ce0c33",
  "denyReason": "reason for seller giving deny"
}
```

The following table presents the request body fields’ description:

| Field | Type | Description | Mandatory |
|:---:|:---:|:---|:---:|
| `cancellationRequestId` | string | Unique identifier of an order requested to be canceled. This ID format is a sequence of numbers and letters. The `cancellationRequestId` is generated by the endpoint Cancel order, and can be found in the responses of the following endpoints: Get order Retrieve user order details | Yes |
| `denyReason` | string | Brief explanation of why the seller will deny order cancellation. | Yes |

### Response body

The endpoint does not return a response body in the successful `200 OK` response.

### Response status codes

The possible response status codes are shown in the table below:

| Status Code | Description |
|:---:|:---|
| 200 OK | The order cancellation was successfully denied. |
| 400 Bad Request | The request was not processed, some possible reasons are: Cancellation request ID not found. Order already canceled. Order workflow not found. Invalid order status. The acceptable status for the seller is `cancellation-requested` , and for the marketplace is `waiting-for-seller-decision`. |
| 403 Forbidden | Unauthorized request. Update the credentials used in the request and try again. |
| 404 Not Found | The requested order was not found. Check the order ID and try again. |
| 429 Too Many Requests | We were unable to process the request due to the high volume of submissions. Wait a few minutes before trying again. |
| 500 Internal Server Error | An unexpected application error occurred. Review the request data and try again. |

### Order after cancellation

After the seller denies the cancellation request made by the marketplace outside the cancellation window, the related information can be retrieved both by marketplace and seller using one of the endpoints below:

- GET - [Get order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-)
- GET - [Retrieve user order details](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/user/orders/-orderId-)

The information will be in the `cancellationRequests` array of the response body, as shown in the example below:

```json
"cancellationRequests": [
        {
            "id": "85835ab408514b52aa139e4236ce0c33",
            "reason": "Cancelation Reason",
            "cancellationRequestDate": "2023-07-24T19:44:59.6667459Z",
            "requestedByUser": true,
            "deniedBySeller": true,
            "deniedBySellerReason": "reason of deny",
            "cancellationRequestDenyDate": "2023-07-24T19:45:03.4550528Z"
        }
    ]
```

> Seller and marketplace will get the same denial cancellation information.

The fields’ description are shown below:

| Response body field | Type | Description |
|:---:|:---:|:---|
| `cancellationRequests` | array | Array with information regarding the order witches cancellation was denied. |
| `id` | string | ID that identifies the original cancellation operation made by the marketplaces or its customer care service using the [Cancel order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/cancel) endpoint. |
| `reason` | string | Explanation of why there was a request for canceling the order. |
| `cancellationRequestDate` | string | Date and time of when the platform processed the cancellation request.  The format is [ISO 8601](https://www.w3.org/TR/NOTE-datetime) `YYYY-MM-DDThh:mm:ssTZD`, a complete date plus hours, minutes, seconds and a decimal fraction of a second. For example, `2023-08-04T15:45:02.1306363+00:00`  It could also be `2023-08-04T15:45:02.1306363Z`, where `Z` stands for zone in Time Zone Designator (TZD), and `Z` is equal to `+hh:mm` or `-hh:mm`. |
| `requestedByUser` | boolean | When set as `true`, the cancellation was requested by the shopper, and when set as `false`, the cancellation was not canceled on behalf of the shopper. |
| `deniedBySeller` | boolean | When set as `true`, the seller denied the order cancellation, and when set as `false`, the seller did not deny it. |
| `deniedBySellerReason` | string | Reason given by the seller for denying order cancellation. |
| `cancellationRequestDenyDate` | string | Date and time of when the seller’s request to deny order cancellation was processed. The format is ISO 8601 `YYYY-MM-DDThh:mm:ssTZD`, a complete date plus hours, minutes, seconds and a decimal fraction of a second. For example, `2023-08-04T15:45:02.1306363+00:00`  It could also be `2023-08-04T15:45:02.1306363Z`, where `Z` stands for zone in Time Zone Designator (TZD), and `Z` is equal to `+hh:mm` or `-hh:mm`. |
