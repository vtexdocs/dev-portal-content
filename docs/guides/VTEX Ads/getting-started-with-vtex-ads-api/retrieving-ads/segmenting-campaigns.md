---
title: "Segmenting campaigns"
slug: "segmenting-campaigns"
excerpt: "Use customer data and contexts to serve personalized campaigns through VTEX Ads API."
hidden: false
createdAt: "2025-05-21T22:18:24.684Z"
updatedAt: "2025-05-21T22:18:24.684Z"
---

Campaign targeting allows meta-information to be provided during an ad query, which can be used in real time to prioritize campaigns aimed at that specific audience.

> 🚧 Campaigns with targeting will have higher priority during the query process, meaning they are considered more relevant to the audience they were directed to. However, the presence of targeting does not prevent non-targeted campaigns from also being displayed.

## Targeting attributes

Attributes are the types of information that the audience can have and consequently that a campaign can have during its creation.

Learn more about targeting attributes on `POST` [Get ads](https://developers.vtex.com/docs/api-reference/vtex-ads-api#post-/v1/rma/-publisher_id-).

## Ad search with targeting

During the ad request, targeting information can be sent in two ways: directly in the request body or based on the audiences associated with a `user_id`.

### Sending targeting in the request body (segmentation)

In this approach, targeting information is sent directly in the request body, in the "segmentation" field. This data is prioritized over information that could be obtained based on the user_id, allowing for more detailed and temporary personalization according to the conditions of the ad query.

Request example:

```json
POST https://api.ads.vtex.com/v1/rma/:publisher_id HTTP/1.1
Content-Type: application/json

{
    "context": "search",
    "term": "desodorante",
    "session_id": "f361661f-5986-4779-9009-a34562f18347",
    "tags": ["Mega Maio"],
    "placements": {
        "nomePlacement1": { "quantity": 3, "size": "desktop", "types": ["banner"] }
    },
    "segmentation": [
        {
            "key": "AGE",
            "values": ["22"]
        },
        {
            "key": "STATE",
            "values": ["SP"]
        }
    ]
}
```

### Targeting based on `user_id`

In this approach, targeting information is obtained based on the audiences associated with the `user_id`. These audiences must have been previously imported into the system.

> 🚧 When using this approach, don't send data in the `segmentation` field, since this field would take priority over `user_id`. The system will automatically fetch the audiences associated with the `user_id`.

Request example:

```json
POST https://api.ads.vtex.com/v1/rma/:publisher_id HTTP/1.1
Content-Type: application/json

{
    "context": "search",
    "term": "desodorante",
    "user_id": "6a746448-cf59-42bc-aa3d-a426844ad115",
    "session_id": "f361661f-5986-4779-9009-a34562f18347",
    "tags": ["Mega Maio"],
    "placements": {
        "nomePlacement1": { "quantity": 3, "size": "desktop", "types": ["banner"] }
    }
}
```
