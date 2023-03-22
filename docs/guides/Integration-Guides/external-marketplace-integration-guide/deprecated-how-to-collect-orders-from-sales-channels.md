---
title: "[Deprecated] How to collect orders from sales channels"
slug: "deprecated-how-to-collect-orders-from-sales-channels"
hidden: true
createdAt: "2022-06-09T21:22:22.023Z"
updatedAt: "2022-06-10T16:12:54.251Z"
---

[block:callout]
{
  "type": "warning",
  "body": "We have released a new method for integrating orders from external marketplaces, as a part of our Marketplace Protocol. If you used this previous method for integrating orders, you can still find their documentation in [Order Logs](https://developers.vtex.com/vtex-rest-api/docs/deprecated-order-logs) and [How to collect orders from sales channels](https://developers.vtex.com/vtex-rest-api/docs/deprecated-how-to-collect-orders-from-sales-channels). These previous methods, however, will not be maintained. If you are integrating orders for the first time, we recommend you use the instructions in our [New Order Integration](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-collect-orders) guide.",
  "title": "New method for integrating orders"
}
[/block]
Orders in an integration fit into two different categories:

**Paid orders:** the marketplace only makes orders available for the integration once they are paid by the customer.

![MarketplaceConnections](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/deprecated-how-to-collect-orders-from-sales-channels-0.jpg)

**Orders to be paid:** the marketplace makes orders that have not been paid by the customer available for the integration.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/deprecated-how-to-collect-orders-from-sales-channels-1.jpg)
Right after the payment confirmation by the marketplace, the flow goes as the image below describes it:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/deprecated-how-to-collect-orders-from-sales-channels-2.jpg)

## How orders reach the connector

A marketplace order can reach the connector by either a:

1. **Notification sent by the marketplace:** when the marketplace informs the connector about the existence of an order, and the connector, after receiving the notification, goes to the marketplace to get order details.

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/deprecated-how-to-collect-orders-from-sales-channels-3.jpg)

2. **Polling request made by the connector:** when the connector checks the marketplace from time to time, to collect new orders.
   ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/deprecated-how-to-collect-orders-from-sales-channels-4.jpg)

## Integrating orders

Follow the steps below, to integrate orders from external marketplaces:

1. Collect order details from the endpoint provided by the marketplace.

2. Create a request on the [Place fulfillment order](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/fulfillment/pvt/orders) endpoint.

3. [Simulate fulfillment](#fulfillment-simulation), to check if the SKU is available in VTEX.

4. For each SKU retrieved, the connector must call the [Get SKU and Context endpoint](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-context) and:

   a. Validate if the SKU is active through the `isActive` property.

   b. Validate if the SKU is associated to the sales channel used in the integration through the `salesChannel` property.

5. In case step 4 retrieves all SKUs that compose the order with their respective inventory levels and prices, the connector should insert the order through the [Order Placement](https://developers.vtex.com/vtex-rest-api/reference/order-placement) endpoint.

- In the `marketplaceServicesEndpoint` field, the endpoint will be used by VTEX to inform the connector of the changes in order status, inserting tracking code and invoice. For more information check out [Sending invoice and tracking code to the marketplace](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-invoice-tracking).

6. In case step 5 returns success and creates the order within the VTEX platform, authorize the dispatch by the seller through the [Authorize dispatch for fulfillment order](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/fulfillment/pvt/orders/-orderId-/fulfill) endpoint.
7. Check the [Recommendations](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-recommendations) page to follow integration best practices.
8. Check out the [Order logs](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-order-logs) page to create appropriate error messages.

If all validations pass, the order is sent to VTEX and the operation is logged according to information described in the [Order logs](https://developers.vtex.com/docs/guides/deprecated-order-logs).

After VTEX OMS returns `success`, if the IDs between VTEX and the marketplace differ, the connector should store the mapping of the order (VTEX ID and Marketplace ID). This information will be used for [order status update operations](https://developers.vtex.com/docs/guides/external-marketplace-update-order-status#api-reference-update-order-status).

[block:callout]
{
  "type": "warning",
  "body": "Be mindful to make all validations at once. In case there's an error detected, the connector presents the seller a list of actions to correct. This way we can avoid the correct - publish - correct cycle. If orders do not apply to the steps above, an [error log](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-order-logs) must be filed.",
  "title": "Validations and logs"
}
[/block]

## API Reference

Use the endpoints described below to perform this step. It is important to note that when consuming this API, the connector must have a valid VTEX App Key and App Token. The diagram illustrates the endpoints used in the integration:

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/deprecated-how-to-collect-orders-from-sales-channels-5.jpg)

[block:callout]
{
  "type": "info",
  "body": "All parameters in the endpoints below must be declared in the request. In case one of the parameters does not have a value, you must still send it as `null`.",
  "title": "Request bodies for POST calls"
}
[/block]

### Fulfillment simulation

Use the curl example below to perform the fulfillment Simulation.

```curl
curl --location --request POST 'https://{{accountName}}.vtexcommercestable.com.br/api/checkout/pub/orderForms/simulation?affiliateId={{affiliateId}}={{salesChannelId}}' \
--header 'Accept: application/vnd.vtex.checkout.debug.v1+json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "items": [
        {
            "id": "13",
            "quantity": 1,
            "seller": "1"
        }
    ],
    "marketingData": null,
    "postalCode": "04321-100",
    "country": "BRA",
    "selectedSla": null,
    "clientProfileData": null,
    "geoCoordinates": [],
    "isCheckedIn": false,
    "storeId": null
}'
```

### Shopping cart simulation

Use the request example below to perform the Shopping Cart Simulation. Check out our  [Shopping cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation) API Reference to know more details.

```json
{
"items":[
{...}
]
"ratesAndBenefitsData":{
"rateAndBenefitsIdentifiers":[]
"teaser":[]
}
"paymentData":{
"installmentOptions":[...]
"paymentSystems":[...]
"payments":[]
"giftCards":[]
"giftCardMessages":[]
"availableAccounts":[]
"availableTokens":[]
}
"selectableGifts":[]
"marketingData":NULL
"postalCode":NULL
"country":"BRA"
"logisticsInfo":[
{...}
]
"messages":[]
"purchaseConditions":{
"itemPurchaseConditions":[...]
}
"pickupPoints":[]
"subscriptionData":NULL
"totals":[
{...}
]
"itemMetadata":NULL
}
```

### Place fulfillment order

Use the request example below to place fulfillment order. Check out our [Place fulfillment order](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/fulfillment/pvt/orders) API Reference to know more details.

```json
[
  {
    "items": [
        {
            "id": "1",
            "price": 900,
            "quantity": 1,
            "seller": "1"
        }
    ],
    "isCreatedAsync": true,
    "marketplaceOrderGroup" : "794901324",
    "marketplaceOrderId": "2630580124",
    "marketplacePaymentValue": 1100,
    "marketplacePaymentReferenceValue": 1100,
    "marketplaceServicesEndpoint": "http://skyhubintegration.vtexinternal.com/api/skyhubintegration/commercialcondition?an=grocery1",
    "clientProfileData": {
        "CorporateDocument": null, //Cnpj
        "CorporateName": null, //nome da empresa
        "CorporatePhone": null, // ddd+telefone
        "Document": "14310315771", //cpf
        "DocumentType": null, //se pessoa fisica, colocar CPF, senão CNPJ
        "Email": "conta@dominio.com.br",
        "FirstName": "Nome",
        "IsCorporate": false, //caso pessoa juridica o valor deve ser true
        "LastName": "Sobrenome",
        "Phone": "41998718616",
        "StateInscription": null, //inscrição estadual
        "TradeName": null,
        "UserProfileId": null //utilizado somente com pedidos VTEX
    },
    "shippingData": {
        "address": {
            "addressId": "Casa",
            "addressType": "Residencial",
            "receiverName": "Marcelo",
            "city": "Curitiba",
            "complement": null,
            "country": "BRA",
            "geoCoordinates": [],
            "neighborhood": "Novo Mundo",
            "number": "4000",
            "postalCode": "81020230",
            "reference": null,
            "state": "PR",
            "street": "Rua Eduardo Carlos Pereira"
        },
        "logisticsInfo": [
            {
                    "itemIndex": 0,
                    "price": 200,
                    "selectedDeliveryChannel":"delivery",
                    "selectedSla": null,
                    "lockTTL": "1d", //tempo para reserva do estoque do pedido
                    "shippingEstimate":"1d" //tempo de entrega do pedido
            }
        ],
        "selectedAddresses":[
          {
            "addressType": "Residencial",
            "receiverName": "Henrique Vianna",
            "addressId": "2",
            "postalCode": "81020-235",
            "city": "Curitiba",
            "state": "PR",
            "country": "BRA",
            "street": "Rua Eduardo Carlos Pereira",
            "number": "4125",
            "neighborhood": "Portão",
            "complement": "",
            "reference": null,
            "geoCoordinates": [
                -49.2892059,
                -25.4826319
            ]
        }],
        "isFob": false //se entrega feita pelo lojista coloque false, senão true
    },
    "customData": {
		"customApps": [{
			"fields": {
				"orderIdMarketplace": "2630580148",
				"paymentIdMarketplace": "8191598627"
			},
			"id": "marketplace-integration",
			"major": 1
		}]
	},
    "openTextField": {
         "value": "{\"Phones\":[\"21998718616\"]}"
    }
  }
]
```

### Authorize dispatch

Use the request example below to authorize dispatch. Check out our [Authorize Dispatch](https://developers.vtex.com/docs/api-reference/marketplace-protocol-external-marketplace-orders#post-/api/fulfillment/pvt/orders/-orderId-/fulfill)
 API Reference to know more details.

```json
[
  {
    "marketplaceOrderId": "956"
  }
]
```

## Scenario 1: orders with price divergence in items between marketplace and VTEX

When to perform: after attempting to integrate an order in VTEX platform, the process  returns an error `FMT007` - signaling price divergence.

Connectors should:

1. In case the call is successful (200 OK), signaling the creation of prive divergence rule, the order should be queued in VTEX.
2. In case the call returns a bad request (400), signaling that the order could not be inserted for infringing price divergence rules, file an error log, following the error code x.
3. In case the call returns an unauthorized request (500), signaling that the price divergence rule failed due to error in system communication, the order should be queued on the connector’s flow to perform a retry.

## Scenario 2: inventory level divergence

When to perform: after attempting to integrate an order in VTEX platform, the process  returns an error `ORDER027` - signaling inventory error.

Connectors should:

1. Generate an error log, according to the item x.
2. Validate if the order status in the marketplace was altered to `canceled`. If so, generate the error log message x, and remove the order from the retry queue.
3. If the order was not canceled, submit the order to be reprocessed.
4. In case the call is successful (200 OK), signaling the creation of the order, connectors should log the operation according to x.
5. In case the call returns a bad request (400), signaling that the order could not be inserted for infringing stock rules, file an error log, following the error code x.
6. In case the call returns an server error (500), signaling that the order creation failed due to error in system communication, the order should be queued on the connector’s flow to perform a retry.

## Scenario 3: SLA errors - no carriers to deliver the order

When to perform: after attempting to integrate an order in VTEX platform, the process  returns an error `ORDER027` - signaling that there are no carriers to attend that order.

Connectors should:

1. Generate an error log, according to the item x.
2. Validate if the order status in the marketplace was altered to `canceled`. If so, generate the error log message x, and remove the order from the retry queue.
3. If the order was not canceled, submit the order to be reprocessed.
4. In case the call is successful (200 OK), signaling the creation of the order, connectors should log the operation according to x.
5. In case the call returns a bad request (400), signaling that the order could not be inserted for infringing carriers’ rules, file an[ error log](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-order-logs), following the error code x.
6. In case the call returns a server error (500), signaling that the order creation failed due to error in system communication, the order should be queued on the connector’s flow to perform a retry.

## Scenario 4: SLA errors - no pickup points to attend the order

When to perform: after attempting to integrate an order in VTEX platform, the process  returns an error `ORDER027` - signaling that there are no pickup points for the end customer to retrieve their order.

Connectors should:

1. Generate an error log, according to the item x.
2. Validate if the order status in the marketplace was altered to `canceled`. If so, generate the error log message x, and remove the order from the retry queue.
3. If the order was not canceled, submit the order to be reprocessed.
4. In case the call is successful (200 OK), signaling the creation of the order, connectors should log the operation according to x.
5. In case the call returns a bad request (400), signaling that the order could not be inserted for infringing pickup points’ rules, file an [error log](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-order-logs), following the error code x.
6. In case the call returns an unauthorized request (500), signaling that the order creation failed due to error in system communication, the order should be queued on the connector’s flow to perform a retry.

## Scenario 5: order is canceled by the marketplace

When to perform: when the order is canceled by the marketplace.

Connectors should:

1. Verify if the order exists in the VTEX platform, by either:
   a. Checking the order ID relation between VTEX and the marketplace in their environment.
   b. Checking if the order exists through the [Get Order](https://developers.vtex.com/vtex-rest-api/reference/getorder) endpoint.

2. Validate the order status.

3. If the order exists in VTEX, call the [Cancel Order](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/cancel) endpoint.
4. If the order exists in VTEX, and the order status is `invoiced`, call the [Order Invoice notification](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/oms/pvt/orders/-orderId-/invoice) endpoint.

5. In case the call is successful (200 OK), signaling the cancelling of the order, connectors should log the operation according to x.
6. In case the call returns a bad request (400), signaling that the order could not be canceled, file an [error log](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-order-logs), following the error code x.
7. In case the call returns an unauthorized request (500), signaling that the order cancelling failed due to error in system communication, the order should be queued on the connector’s flow to perform a retry.

[block:callout]
{
  "type": "warning",
  "body": "Make sure that all steps are logged as either success or failure, to offer the operation’s full traceability. Check out the [Order logs](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-order-logs) page to learn more.",
  "title": "Error logs"
}
[/block]
