---
title: "VTEX Pick and Pack Carrriers Integration Protocol"
slug: "vtex-pick-and-pack-carriers-integration-protocol"
hidden: false
createdAt: "2023-04-05T17:08:52.219Z"
updatedAt: "2023-04-12T17:08:52.219Z"
excerpt: "Learn how to integrate carriers with VTEX Pick and Pack API Protocol"
seeAlso:
 - "vtex-pick-and-pack"
 - "vtex-pick-and-pack-get-order-status-and-information-api"
hidePaginationPrevious: false
hidePaginationNext: false
---

All API access is over HTTPS and accessed from `https://api.pickingnpacking.com`. All data is sent and received as JSON.

Blank fields are included as `null` instead of being omitted.

All timestamps returned in UTC, ISO 8601 format: `YYYY-MM-DDTHH:mm:ss.sssZ`.

All distance measurements are in meters.

## Basic authentication

API keys available

```raw
**xxx**
```

### Steps to generate JWT

* * *

1. Create a token of authentication with service [/token](/API%20Carriers%20integration%20protocol.md).
2. Send in the headers of the request `Authorization` with the JWT generated in step 1.

```json
// Headers
{
  "Authorization": "JWT"
}
```

## Service endpoints

### Endpoint URLs

Endpoints are configurable when creating the carrier configuration

* * *

### Service creation

This is the information that VTEX will send to the carrier to create a service

- **URL:** Carrier configuration  
- **Method:** Carrier configuration  
- **Headers:** Carrier configuration  
- **Query:** Carrier configuration  

#### Schema

```graphql
{
  orderId: String!
  carrierId: String!
  seller: String!
  sender: {
    name: String
    phone: String
    email: String
    city: String!
    state: String!
    country: String!
    address: String!
    neighborhood: String
    number: String
    reference: String
    addressComplement: String
    location: {
      latitude: Float
      longitude: Float
    }
    pickupDate: AWSDateTime!
    deliveryWindow: {
      name: String
      initialDate: AWSDateTime
      finalDate: AWSDateTime
    }
    zipCode: String!
  }!
  receiver: {
    name: String!
    phone: String
    email: String
    city: String!
    state: String!
    country: String!
    address: String!
    neighborhood: String
    number: String
    reference: String
    addressComplement: String
    location: {
      latitude: Float
      longitude: Float
    }
    identification: String
    deliveryDate: AWSDateTime! # UTC iso 8601
    deliveryWindow: {
        name: String
        initialDate: AWSDateTime
        finalDate: AWSDateTime
    },
    contactName: String
    zipCode: String!
  }!
  packages: [
    {
      id: String!
      orderId: String!
      envelope: String
      description: String
      categories: [String]
      dimensions: {
        width: String
        height: String
        length: String
      }
      weight: String
      totalValue: Float
      items: [
        {
          id: String!
          name: String!
          ean: String!
          refId: String
          image: String
          type: String
          price: Float!
          weight: String
          quantity: Int!
        }
      ]
    }
  ]
  type: PICKUP | DELIVERY | PICKUP_DELIVERY | RETURN!
  carrierServiceType: NATIONAL | INTERNATIONAL | EXPRESS | SPECIALIZED | OTHERS!
  comments: String
  paymentMethod: ONLINE | CASH_ON_DELIVERY | PIN_PAD!,
  settings: [
    {
      label: String
      value: String
      "key": String
    }
  ]
  timezone: {
    offset: Float!
    value: String!
  }!
}


```

#### Body Example

```json
{
  "orderId": "SLR-29384924-01",
  "carrierId": "servientrega-50461c9f3335",
  "seller": "qaolimpica",
  "sender": {
    "name": "Tabitha Sears",
    "phone": "+57 2305781612",
    "email": "tabitha_sears@fortean.brother",
    "city": "Jenkinsville",
    "state": "Northern Mariana Islands",
    "country": "Brazil",
    "address": "77 Sullivan Place, Jenkinsville, Northern Mariana Islands",
    "addressComplement": "Labore sunt laboris reprehenderit nulla cupidatat irure labore sunt dolore est.",
    "number": "1029",
    "reference": "3",
    "location": {
      "latitude": -75.269008,
      "longitude": 137.499833
    },
    "pickupDate": "2022-04-25T18:06:41.202Z"
  },
  "receiver": {
    "name": "Pansy Graves",
    "phone": "+57 4240807147",
    "email": "pansy_graves@zentime.moda",
    "city": "Valle",
    "state": "Marshall Islands",
    "country": "Iceland",
    "neighborhood": "Billings",
    "number": "9840",
    "reference": "65C"
    "address": "63 Billings Place, Valle, Marshall Islands",
    "addressComplement": "In excepteur in Lorem id eu et id.",
    "location": {
      "latitude": -33.249891,
      "longitude": -135.052901
    },
    "identification": "9541933267",
    "deliveryDate": "2022-04-16T20:49:36.117Z",
    "contactName": "Savannah Porter",
    "deliveryWindow": {
        "name": "consectetur",
        "initialDate": "2022-04-25T22:50:41.209Z",
        "finalDate": "2022-05-05T21:50:41.210Z"
      }
  },
  "packages": [
    {
      "id": "6266df719ac55224b793ad36",
      "orderId": "SLR-1221800709659-01",
      "envelope": "Grande",
      "description": "Paquete delicado",
      "categories": ["Cellphone", "Technology"]
      "dimensions": {
        "width": "68",
        "height": "43",
        "length": "13"
      },
      "weight": "19",
      "totalValue": 5616.01,
      "items": [
        {
          "id": "6266df71a19ebe35637e1f42",
          "name": "Celular nokia AD1",
          "ean": "473390795673",
          "refId": "6266",
          "image": "https://static9.depositphotos.com/1628352/1107/i/600/depositphotos_11071361-stock-photo-tomato.jpg",
          "type": "Tech",
          "price": 774230.01,
          "weight": "4 kg",
          "quantity": 4
        },
        {
          "id": "6266df71803601c3bc4e2d99",
          "name": "Celular nokia AD2",
          "ean": "329949764612",
          "refId": "6266",
          "image": "https://static9.depositphotos.com/1628352/1107/i/600/depositphotos_11071361-stock-photo-tomato.jpg",
          "type": "Tech",
          "price": 23162,
          "weight": "14 kg",
          "quantity": 9
        }
      ]
    }
  ],
  "type": "PICKUP_DELIVERY",
  "carrierServiceType": "OTHERS",
  "comments": "Consectetur ex dolor adipisicing proident.",
  "paymentMethod": "CASH_ON_DELIVERY",
  "orderValue": 8000,
  "settings": [
    {
      "label": "Clave secreta",
      "value": "keysecret-0122",
      "key": "secrekey"
    }
  ],
  "timezone": {
    "offset": 300,
    "value": "America/Bogota"
  }
}

```

#### Expected response

```json
{
 "status": "PENDING", // PENDING | ASSIGNED | PICKED | ON_ROUTE | INCIDENT | RETURNED | DELIVERED | CANCELED | ON_HOLD
 "serviceId": "ASDF23324KDSF2", // Id devuelto por la transportadora
 "shippingPrice": 20000.09 // If not exists send `null`
 "metaData": {}, // Carrier additional information for example: {"anyKey": "anyValue", "propertyCustom": "anyValue", "anyArray": ["anyValue"], "errorKeyExample": "Show error trace exampel"}, if not exists send `null`
 "shippingEstimatedDate": "2022-05-29T22:36:37.589Z" // If not exists send `null`
}
```

### Status codes

| HTTP Status Code | Description         |
| -------------------- | ----------------------- |
| 200                  | Ok                      |
| 401                  | Required authentication |
| 400                  | Bad request             |
| 404                  | Resource not found      |
| 500                  | Internal error          |

>ℹ️ Note: There is a 5 seconds timeout before the service creation is confirmed. After that, is possible to use any of the endpoints below.

## Cancel service

In the case that a user or the application needs to cancel a service, this will be sent to the carrier configurated endpoints

- **URL:** Carrier config  
- **Method:** Carrier config  
- **Headers:** Carrier config  
- **Query:** Carrier config  

### Schema

```graphql
{
  serviceId: String!
  carrierId: String!
  reason: String
}
```

### Example

```json
{
  "serviceId": "apknieot924892jaf-1231",
  "carrierId": "servientrega9234jaf",
  "reason": "La dirección de entrega esta mal registrada"
}
```

### Response

```json
{
  "message": "Service executed successfully",
  "data": {
    "serviceId": "apknieot924892jaf-1231",
    "carrierId": "servientrega9234jaf",
    "reason": "En el lugar de residencia no hay quien reciba el paquete"
  }
}
```

### Status codes

| **HTTP Status Code** | **Description**         |
| -------------------- | ----------------------- |
| 200                  | Ok                      |
| 401                  | Requires authentication |
| 400                  | Bad request             |
| 404                  | Resource not found      |
| 500                  | Internal error          |

* * *

## Pause service

In the case that a user or the application needs to pause/continue a service, this will be sent to the carrier configurated endpoints
- **URL**: Carrier config  
- **Method:** Carrier config  
- **Headers:** Carrier config  
- **Query:** Carrier config  


### Schema

```graphql
{
  serviceId: String!
  carrierId: String!
  pause: Boolean!
  reason: String
}
```

### Example

```json
{
  "serviceId": "apknieot924892jaf-1231",
  "carrierId": "servientrega9234jaf",
  "pause": false,
  "reason": "En el lugar de residencia no hay quien reciba el paquete"
}
```

### Response

```json
{
  "message": "Service executed successfully",
  "data": {
    "serviceId": "apknieot924892jaf-1231",
    "carrierId": "servientrega9234jaf",
    "cancel": true,
    "reason": "En el lugar de residencia no hay quien reciba el paquete"
  }
}
```

**Status codes**

| **HTTP Status Code** | **Description**         |
| -------------------- | ----------------------- |
| 200                  | Ok                      |
| 401                  | Requires authentication |
| 400                  | Bad request             |
| 404                  | Resource not found      |
| 500                  | Internal error          |

* * *

## Shipping services updates

This endpoint will allow the carriers to update an ongoing shipping service.

### Endpoint URLs

REST API endpoints are prefixed with the following URLs:

**Dev**

`https://api.pickingnpacking.com/dev/v1`

**Prod**

`https://api.pickingnpacking.com/prod/v1`


### Get service

he following endpoint returns information about a service, which can be queried by providing the carrier ID and the corresponding service ID as query parameters. The response returned by the endpoint will contain the requested information.

- **GET:** `/tracking/hook/{carrierId}/{serviceId}`
- **Authentication:** [API_KEY_PUBLIC](/API%20Carriers%20integration%20protocol.md)


### Schema

```graphql
type ServiceResponseDto {
  id: ID!
  orderId: String!
  carrierId: String!
  serviceId: String # '{carrierId}&{serviceIdFromCarrier}'
  carrierLogo: String
  carrierName: String!
  seller: String!
  status: ServiceStatus!
  labels: [ServiceLabel]!
  trackingUrl: String
  comments: String
  evidences: [ServiceEvidence]!
  packages: [PackageService]!
  timeline: [TrackingTimeline]!
  type: ServiceType!
  notes: [ServiceNotes]!
  paymentMethod: String
  carrierServiceType: String
  shippingPrice: Float
  shippingEstimatedDate: AWSDateTime
  shippingFinishedDate: AWSDateTime
  metaData: AWSJSON
  timezone: CTimezone
  tags: [String]!
}

enum ServiceStatus {
  CREATED
  PENDING
  ASSIGNED
  PICKED
  ON_ROUTE
  INCIDENT
  RETURNED
  DELIVERED
  CANCELED
  ON_HOLD
}

type ServiceLabel {
  id: ID!
  url: String!
  name: String!
  type: ServiceLabelType!
}

enum ServiceLabelType {
  PDF
  BASE64
  TEXT
  ZPL
}

type ServiceEvidence {
  type: ServiceEvidenceType!
  content: String
  date: AWSDateTime!
  author: String
}

enum ServiceEvidenceType {
  TEXT
  IMAGE
}

type PackageService {
  id: ID!
  orderId: String!
  envelope: String
  dimensions: ServiceDimensionsPacking
  weight: String
  totalValue: Float
  items: [ServiceItemsPackage]!
  categories: [String]!
  description: String
}

type ServiceDimensionsPacking {
  width: String
  height: String
  length: String
}

type ServiceItemsPackage {
  id: ID!
  name: String!
  ean: String!
  refId: String
  image: String
  type: String
  price: Float!
  weight: String
  quantity: Int!
}

type TrackingTimeline {
  id: ID!
  type: TrackingTimelineType!
  date: AWSDateTime!
  description: String
  author: String
  metaData: AWSJSON
}

enum TrackingTimelineType {
  STATUS
  EVIDENCE
  NOTE
  LABEL
  OTHER
}

enum ServiceType {
  PICKUP
  DELIVERY
  PICKUP_DELIVERY
  RETURN
}

type ServiceNotes {
  type: ServiceNotesType!
  date: AWSDateTime!
  content: String!
  author: String
}

enum ServiceNotesType {
  COMMENT
  ERROR
}

type CTimezone {
  offset: Float # (-5, -3, ...)
  value: String # ("America/Bogota", ...)
  label: String
}
```

### Response

```json
{
  "message": "success",
  "data": {
    "id": "d9dc0d2c-5f49-4254-ad05-5551be273a2c",
    "orderId": "1313160501383-01",
    "carrierId": "627eb3b93a19fdc0cf5fe087",
    "serviceId": "627eb3b93a19fdc0cf5fe087&470083180050116775042433920287",
    "carrierName": "Blue Express",
    "seller": "exito96",
    "status": "DELIVERED",
    "type": "PICKUP_DELIVERY",
    "labels": [],
    "evidences": [
      {
        "type": "IMAGE",
        "date": "2023-02-27T13:25:08.538Z",
        "content": "https://tookan.s3.amazonaws.com/acknowledgement_images/1677504302764669967113822-470083180Signature.jpg",
        "author": "Juan C Testing P"
      },
      {
        "type": "IMAGE",
        "date": "2023-02-27T13:26:22.799Z",
        "content": "https://tookan.s3.amazonaws.com/acknowledgement_images/16775043776540952751646343-470083181Signature.jpg",
        "author": "Juan C Testing P"
      }
    ],
    "packages": [
      {
        "id": "1677504239859",
        "orderId": "1313160501383-01",
        "envelope": "Box",
        "dimensions": {
          "height": "2",
          "length": "2",
          "width": "2"
        },
        "weight": "2",
        "totalValue": 40000,
        "items": [
          {
            "id": "60",
            "name": "Neutrogena Hydro Boost Water Gel X 50 Gr",
            "ean": "EAN159",
            "quantity": 2,
            "price": 20000,
            "refId": "60",
            "image": "https://blueExpress.vteximg.com.br/arquivos/ids/155747-55-55/60.jpg?v=637917088184130000",
            "type": "PRODUCT",
            "weight": "1"
          },
          {
            "id": "59",
            "name": "Shampo Sin Sal + Mascarilla French Gold",
            "ean": "EAN158",
            "quantity": 2,
            "price": 20000,
            "refId": "59",
            "image": "https://blueExpress.vteximg.com.br/arquivos/ids/155746-55-55/59.jpg?v=637917087644630000",
            "type": "PRODUCT",
            "weight": "1"
          }
        ],
        "categories": ["Personal Care"],
        "description": "-"
      }
    ],
    "timeline": [
      {
        "id": "d8ecc1d7-52c9-4c1f-81ee-5524a66cc276",
        "date": "2023-02-27T13:25:09.749Z",
        "createdAt": "2023-02-27T13:25:09.749Z",
        "updatedAt": "2023-02-27T13:25:09.749Z",
        "type": "STATUS",
        "description": "Courier on route",
        "author": "System",
        "metaData": {
          "rating": 5,
          "totalDistanceTraveled": 0,
          "trackingUrl": "https://blueExpress.northlatam.com/tracking/index.html?jobID=41903e23c5157de2a3961c05cafc6e5b",
          "status": "ON_ROUTE"
        }
      },
      {
        "id": "27e6fe70-9a8e-4ca3-8454-d491bb1fe828",
        "date": "2023-02-27T13:26:22.809Z",
        "createdAt": "2023-02-27T13:26:22.809Z",
        "updatedAt": "2023-02-27T13:26:22.809Z",
        "type": "EVIDENCE",
        "description": "Added evidence",
        "author": "Juan C Testing P",
        "metaData": {
          "0": {
            "type": "IMAGE",
            "content": "https://tookan.s3.amazonaws.com/acknowledgement_images/16775043776540952751646343-470083181Signature.jpg",
            "author": "Juan C Testing P"
          }
        }
      },
      {
        "id": "3395c4b0-40fc-4681-8c13-f26119a1da16",
        "date": "2023-02-27T13:25:52.841Z",
        "createdAt": "2023-02-27T13:25:52.841Z",
        "updatedAt": "2023-02-27T13:25:52.841Z",
        "type": "STATUS",
        "description": "Courier on route",
        "author": "System",
        "metaData": {
          "rating": 5,
          "totalDistanceTraveled": 0,
          "trackingUrl": "https://blueExpress.northlatam.com/tracking/index.html?jobID=41903e23c5157de2a3961c05cafc6e5b",
          "status": "ON_ROUTE"
        }
      },
      {
        "id": "3d778bfa-dbd3-40de-a23e-03f6e1aa84ea",
        "date": "2023-02-27T13:24:45.684Z",
        "createdAt": "2023-02-27T13:24:45.684Z",
        "updatedAt": "2023-02-27T13:24:45.684Z",
        "type": "STATUS",
        "description": "Service pending",
        "author": "System",
        "metaData": {
          "rating": 5,
          "totalDistanceTraveled": 0,
          "trackingUrl": "https://blueExpress.northlatam.com/tracking/index.html?jobID=98cb758cc7049b956d13c15e67e5fd87",
          "status": "PENDING"
        }
      },
      {
        "id": "25b9dba7-4e65-4a10-b0b5-27f98997422a",
        "date": "2023-02-27T13:26:22.985Z",
        "createdAt": "2023-02-27T13:26:22.985Z",
        "updatedAt": "2023-02-27T13:26:22.985Z",
        "type": "NOTE",
        "description": "A new note has been added",
        "author": "Juan C Testing P",
        "metaData": {
          "0": {
            "type": "COMMENT",
            "note": "Entregado",
            "author": "Juan C Testing P"
          },
          "1": {
            "type": "COMMENT",
            "note": "Entregado a porteria",
            "author": "Juan C Testing P"
          }
        }
      },
      {
        "id": "a27af5ba-a765-4941-bde8-21f7795473cd",
        "date": "2023-02-27T13:24:03.496Z",
        "createdAt": "2023-02-27T13:24:03.496Z",
        "updatedAt": "2023-02-27T13:24:03.496Z",
        "type": "STATUS",
        "description": "Service creation",
        "author": "System",
        "metaData": null
      },
      {
        "id": "4cd358ff-c79b-421d-a0a1-bcdb70622886",
        "date": "2023-02-27T13:25:08.691Z",
        "createdAt": "2023-02-27T13:25:08.691Z",
        "updatedAt": "2023-02-27T13:25:08.691Z",
        "type": "NOTE",
        "description": "A new note has been added",
        "author": "Juan C Testing P",
        "metaData": {
          "0": {
            "type": "COMMENT",
            "note": "Recogido",
            "author": "Juan C Testing P"
          }
        }
      },
      {
        "id": "5c4137a5-c6db-479c-98ab-b40b9adc22dc",
        "date": "2023-02-27T13:25:08.547Z",
        "createdAt": "2023-02-27T13:25:08.547Z",
        "updatedAt": "2023-02-27T13:25:08.547Z",
        "type": "EVIDENCE",
        "description": "Added evidence",
        "author": "Juan C Testing P",
        "metaData": {
          "0": {
            "type": "IMAGE",
            "content": "https://tookan.s3.amazonaws.com/acknowledgement_images/1677504302764669967113822-470083180Signature.jpg",
            "author": "Juan C Testing P"
          }
        }
      },
      {
        "id": "912f2d4a-00d6-4ba0-a380-4bf0fa593d6e",
        "date": "2023-02-27T13:24:39.847Z",
        "createdAt": "2023-02-27T13:24:39.847Z",
        "updatedAt": "2023-02-27T13:24:39.847Z",
        "type": "STATUS",
        "description": "Assigned courier",
        "author": "System",
        "metaData": {
          "rating": 5,
          "totalDistanceTraveled": 0,
          "trackingUrl": "https://blueExpress.northlatam.com/tracking/index.html?jobID=98cb758cc7049b956d13c15e67e5fd87",
          "status": "ASSIGNED"
        }
      },
      {
        "id": "b44f7442-e7b5-4d87-8dc3-9c9ec480a269",
        "date": "2023-02-27T13:24:03.471Z",
        "createdAt": "2023-02-27T13:24:03.471Z",
        "updatedAt": "2023-02-27T13:24:03.471Z",
        "type": "STATUS",
        "description": "Service pending in PROD",
        "author": "System",
        "metaData": {
          "shippingEstimatedDate": null,
          "metaData": null,
          "serviceId": "470083180050116775042433920287",
          "shippingPrice": null,
          "status": "PENDING"
        }
      },
      {
        "id": "b992c08d-3b6c-4e95-9c87-9b41b82abc27",
        "date": "2023-02-27T13:25:07.834Z",
        "createdAt": "2023-02-27T13:25:07.834Z",
        "updatedAt": "2023-02-27T13:25:07.834Z",
        "type": "STATUS",
        "description": "Courier picked the package",
        "author": "System",
        "metaData": {
          "rating": 5,
          "totalDistanceTraveled": 0,
          "trackingUrl": "https://blueExpress.northlatam.com/tracking/index.html?jobID=98cb758cc7049b956d13c15e67e5fd87",
          "status": "PICKED"
        }
      },
      {
        "id": "23a4bd15-e33d-441c-a699-c0c20dda6a7a",
        "date": "2023-02-27T13:26:22.160Z",
        "createdAt": "2023-02-27T13:26:22.160Z",
        "updatedAt": "2023-02-27T13:26:22.160Z",
        "type": "STATUS",
        "description": "The package was delivered",
        "author": "System",
        "metaData": {
          "rating": 5,
          "totalDistanceTraveled": 0,
          "trackingUrl": "https://blueExpress.northlatam.com/tracking/index.html?jobID=41903e23c5157de2a3961c05cafc6e5b",
          "status": "DELIVERED"
        }
      }
    ],
    "notes": [
      {
        "type": "COMMENT",
        "date": "2023-02-27T13:25:08.682Z",
        "content": "Recogido",
        "author": "Juan C Testing P"
      },
      {
        "type": "COMMENT",
        "date": "2023-02-27T13:26:22.976Z",
        "content": "Entregado",
        "author": "Juan C Testing P"
      },
      {
        "type": "COMMENT",
        "date": "2023-02-27T13:26:22.976Z",
        "content": "Entregado a porteria",
        "author": "Juan C Testing P"
      }
    ],
    "timezone": {
      "offset": -300,
      "value": "America/Bogota",
      "label": null
    },
    "carrierLogo": "iVBORw0KGgoAAAANSUhEUgAAAhQAAAHICAYAAAAWbnMsA",
    "trackingUrl": "https://blueExpress.northlatam.com/tracking/index.html?jobID=41903e23c5157de2a3961c05cafc6e5b",
    "comments": "-",
    "paymentMethod": "ONLINE",
    "carrierServiceType": "EXPRESS",
    "shippingPrice": null,
    "shippingEstimatedDate": null,
    "shippingFinishedDate": null,
    "metaData": {
      "jobCapacityTest": true,
      "test": "This is field custom",
      "name": "Last Mile Test"
    }
  }
}
```

## Update service (via webhook)

Service that allows updating the details of the tracking service via webhook

- **PATCH:**  `/tracking/hook/{carrierId}/{serviceId}`
- **Authentication:** [API_KEY_PUBLIC](/API%20Carriers%20integration%20protocol.md)

### Parameters

| Name            | Type   | In     | Description                                                                      |
| --------------- | ------ | ------ | -------------------------------------------------------------------------------- |
| `carrierId`     | string | path   | Carrier ID                                                                       |
| `serviceId`     | string | path   | Id generated by the service                                                      |
| `Authorization` | string | header | JWT generated with [API KEY PUBLIC](/API%20Carriers%20integration%20protocol.md) |

### Schema

```graphql
{
  status: PENDING | ASSIGNED | PICKED | ON_ROUTE | INCIDENT | RETURNED | DELIVERED
  agent: {
    id: String!
    name: String!
    identification: String
    phone: String
    email: String
    vehicle: SCOOTER | VAN | CAR | TRUCK | BIKE | WALK | DRONE
  }
  trackingUrl: String
  totalDistanceTraveled: Int
  rating: Float # 1-5
  shippingPrice: Float
  shippingEstimatedDate: String
}
```

### Example

```json
{
  "status": "PENDING",
  "agent": {
    "id": "pedro1",
    "name": "Pedro!",
    "identification": "89082480",
    "phone": "242424234",
    "email": "pedro@gmailc.om",
    "vehicle": "SCOOTER"
  },
  "trackingUrl": "https://localhost.com",
  "totalDistanceTraveled": 2,
  "rating": 5,
  "shippingPrice": 150000,
  "shippingEstimatedDate": "2022-04-27T20:25:45.067Z"
}
```

### Response

```json
{
  "message": "Service updated successfully",
  "data": {
    "status": "PENDING",
    "agent": {
      "id": "pedro1",
      "name": "Pedro!",
      "identification": "89082480",
      "phone": "242424234",
      "email": "pedro@gmailc.om",
      "vehicle": "SCOOTER"
    },
    "trackingUrl": "https://localhost.com",
    "totalDistanceTraveled": 2,
    "rating": 5,
    "shippingPrice": 150000,
    "shippingEstimatedDate": "2022-04-27T20:25:45.067Z"
  }
}
```

### Status codes

| HTTP Status Code | Description        |
| -------------------- | ----------------------- |
| 200                  | Ok                      |
| 401                  | Requires authentication |
| 400                  | Bad request             |
| 404                  | Resource not found      |
| 500                  | Internal error          |



## Create notes

Service that allows the carriers to add notes/information on services

- **POST:** `/tracking/hook/notes/{carrierId}/{serviceId}`  
- **Authentication:** [API_KEY_PUBLIC](/API%20Carriers%20integration%20protocol.md)

### Parameters

| Name            | Type   | In     | Description                                                                      |
| --------------- | ------ | ------ | -------------------------------------------------------------------------------- |
| `carrierId`     | string | path   | Carrier ID                                                                       |
| `serviceId`     | string | path   | Id generated by the service                                                      |
| `Authorization` | string | header | JWT generated with [API KEY PUBLIC](/API%20Carriers%20integration%20protocol.md) |

### Schema

```graphql
[
  {
    type: ERROR | COMMENT!
    note: String!
    author: String
  }
]
```

### Example

```json
[
  {
    "type": "ERROR"
    "note": "El paquete tarda en ser despachado",
    "author": "Oscar Rojas"
  },
  {
    "type": "COMMENT"
    "note": "El paquete fue recogido",
    "author": "Oscar Rojas"
  }
]

```

### Response

```json
{
 "message": "Notes saved successfully",
 "data": [
    {
      "type": "ERROR"
      "note": "El paquete tarda en ser despachado",
      "author": "Oscar Rojas"
    },
    {
      "type": "COMMENT"
      "note": "El paquete ha fue recogido",
      "author": "Oscar Rojas"
    }
  ]
}

```

### Status codes

| HTTP Status Code | Description         |
| -------------------- | ----------------------- |
| 200                  | Ok                      |
| 401                  | Requires authentication |
| 400                  | Bad request             |
| 404                  | Resource not found      |
| 500                  | Internal error          |



## Create evidence

Service that allows the carrier to add evidence like proof of delivery or pickup to the shipping service, photos, text, others

- **POST:** `/tracking/hook/evidences/{carrierId}/{serviceId}`
- **Authentication:** [API_KEY_PUBLIC](/API%20Carriers%20integration%20protocol.md)

### Parameters

| Name            | Type   | In     | Description                                                                      |
| --------------- | ------ | ------ | -------------------------------------------------------------------------------- |
| `carrierId`     | string | path   | Carrier ID                                                                       |
| `serviceId`     | string | path   | Id generated by the service                                                      |
| `Authorization` | string | header | JWT generated with [API KEY PUBLIC](/API%20Carriers%20integration%20protocol.md) |

### Schema

```graphql
[
  {
    type: IMAGE | TEXT!
    content: String!
    author: String
  }
]
```

### Example

```json
[
  {
    "type": "IMAGE",
    "content": "https://parkers-images.bauersecure.com/wp-images/18727/courier-van-insurance-01.jpg",
    "author": "Felipe Cardenas"
  },
  {
    "type": "TEXT",
    "content": "El paquete fue entregado",
    "author": "Felipe Cardenas"
  }
]
```

### Response

```json
{
  "message": "Evidences saved successfully",
  "data": [
    {
      "type": "IMAGE",
      "content": "https://parkers-images.bauersecure.com/wp-images/18727/courier-van-insurance-01.jpg",
      "author": "Felipe Cardenas"
    },
    {
      "type": "TEXT",
      "content": "El paquete fue entregado",
      "author": "Felipe Cardenas"
    }
  ]
}
```

### Status codes

| HTTP Status Code | Description         |
| -------------------- | ----------------------- |
| 200                  | Ok                      |
| 401                  | Requires authentication |
| 400                  | Bad request             |
| 404                  | Resource not found      |
| 500                  | Internal error          |



## Create labels

Service that allows the carrier to add the shipping labels.

- **POST:** `/tracking/hook/labels/{carrierId}/{serviceId}`
- **Authentication:** [API_KEY_PUBLIC](/API%20Carriers%20integration%20protocol.md)

### Parameters

| Name            | Type   | In     | Description                                                                      |
| --------------- | ------ | ------ | -------------------------------------------------------------------------------- |
| `carrierId`     | string | path   | Carrier ID                                                                       |
| `serviceId`     | string | path   | Id generated by the service                                                      |
| `Authorization` | string | header | JWT generated with [API KEY PUBLIC](/API%20Carriers%20integration%20protocol.md) |

### Schema

```graphql
{
  id: String!
  url: String!
  name: String!
  type: PDF | BASE64 | TEXT | ZPL!
}
```

if the label is type **BASE64 **or** TXT**, the max size that we allow is **180kb**

### Example

```json
{
  "id": "AS23424ADASFG",
  "url": "http://s3://mybucket-alpha/orc/2013-10-04-custdata/label-pickup.pdf",
  "name": "Etiqueta de entrega",
  "type": "PDF"
}
```

### Response

```json
{
  "message": "Label saved successfully",
  "data": {
    "id": "AS23424ADASFG",
    "url": "http://s3://mybucket-alpha/orc/2013-10-04-custdata/label-picup.pdf",
    "name": "Etiqueta de entrega",
    "type": "PDF"
  }
}
```

### Status codes

| HTTP Status Code | Description        |
| -------------------- | ----------------------- |
| 200                  | Ok                      |
| 401                  | Requires authentication |
| 400                  | Bad request             |
| 404                  | Resource not found      |
| 500                  | Internal error          |


## Cancel service

Service that will cancel an ongoing shipping service

- **POST:** `/tracking/hook/cancel/{carrierId}/{serviceId}`
- **Authentication:** [API_KEY_PUBLIC](/API%20Carriers%20integration%20protocol.md)

### Parameters

| Name            | Type   | In     | Description                                                                      |
| --------------- | ------ | ------ | -------------------------------------------------------------------------------- |
| `carrierId`     | string | path   | Carrier ID                                                                       |
| `serviceId`     | string | path   | Id generated by the service                                                      |
| `Authorization` | string | header | JWT generated with [API KEY PUBLIC](/API%20Carriers%20integration%20protocol.md) |

### Schema

```graphql
{
  comment: String
  type: ERROR_CREATE_SERVICE  |  END_CLIENT_CANCELED  |  NO_THERE_DELIVERY_MAN_ASSIGN  |  OTHER!
}
```

### Example

```json
{
  "comment": "La direccion de entrega se cambio",
  "type": "END_CLIENT_CANCELED"
}
```

### Response

```json
{
  "message": "Service canceled successfully",
  "data": {
    "comment": "La direccion de entrega se cambio",
    "type": "END_CLIENT_CANCELED"
  }
}
```

### Status codes

| HTTP Status Code | Description        |
| -------------------- | ----------------------- |
| 200                  | Ok                      |
| 401                  | Requires authentication |
| 400                  | Bad request             |
| 404                  | Resource not found      |
| 500                  | Internal error          |



## On hold service

Service that allows a carrier to temporarily pause a shipping service

- **POST:** `/tracking/hook/on-hold/{carrierId}/{serviceId}`
- **Authentication:** [API_KEY_PUBLIC](/API%20Carriers%20integration%20protocol.md)

### Parameters

| Name            | Type   | In     | Description                                                                      |
| --------------- | ------ | ------ | -------------------------------------------------------------------------------- |
| `carrierId`     | string | path   | Carrier ID                                                                       |
| `serviceId`     | string | path   | Id generated by the service                                                      |
| `Authorization` | string | header | JWT generated with [API KEY PUBLIC](/API%20Carriers%20integration%20protocol.md) |

### Schema

```graphql
{
  comment: String # reason
  type: ERROR_CREATE_SERVICE  |  END_CLIENT_PAUSE  |  NO_THERE_DELIVERY_MAN_ASSIGN  |  OTHER!
}
```

### Example

```json
{
  "comment": "La direccion de entrega se cambio",
  "type": "END_CLIENT_PAUSE"
}
```

### Response

```json
{
  "message": "Service on hold successfully",
  "data": {
    "comment": "La direccion de entrega se cambio",
    "type": "END_CLIENT_PAUSE"
  }
}
```

### Status codes

| HTTP Status Code | Description       |
| -------------------- | ----------------------- |
| 200                  | Ok                      |
| 401                  | Requires authentication |
| 400                  | Bad request             |
| 404                  | Resource not found      |
| 500                  | Internal error          |

## Create token

Endpoint available to generate authentication JWT

_REST API endpoints are prefixed with the following URL:_

**Dev**

`https://auth.pickingnpacking.com/dev`

**Prod**

`https://auth.pickingnpacking.com/prod`

- **POST:** `/token`
- **Authentication:** None

### Schema

```graphql
{
    apiKey: String!
}
```

### Example

- **POST:** `https://auth.pickingnpacking.com/dev/token`

```json
{
  "apiKey": "db5a3cecfef9cb0a9815af7c2eb8f7d6:c400460c165cc9beb146ad4d757e3bb1a24ff15228c424a0bd7c37f0ac356c0f6230568705d93dd6ff68190c0eafe5a74cbb14229748f20d3e53cbcc790ba372"
}
```

### Response

```json
{
  "message": "success",
  "data": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ2.eyJob4N0bmFtZSI6Im5ld2J1c2luZXNzMDEiLCJpYXQiOjE2MzM3MjE1NzksImV4cCI6MTYzMzcyMjQ3OX0.7QRZpElg1HYgyJpE6QTNgE2IN3vXbzIfulBS0Bvyzds"
}
```

### Status codes

| HTTP Status Code | Description         |
| -------------------- | ----------------------- |
| 200                  | Ok                      |
| 401                  | Requires authentication |
| 400                  | Bad request             |
| 404                  | Resource not found      |
| 500                  | Internal error          |

          