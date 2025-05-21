---
title: "Digital Signage"
slug: "digital-signage"
excerpt: "Deliver Retail Media experiences in physical stores via digital signage integration."
hidden: false
createdAt: "Thu Sep 05 2024 08:28:33 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Feb 10 2025 13:36:00 GMT+0000 (Coordinated Universal Time)"
---
The Digital Signage integration uses the same API that is used for retrieving ads for your digital platform.

API Documentation: [Retrieving ads](https://developers.vtex.com/docs/guides/retrieving-ads)

# Retrieving Ads for Generic Screens

> 📘 All ads that should be displayed will be returned.  
>
> Once all ads have been displayed, the API must be called again to retrieve the next batch of items to be shown.  
>
> **Can I display the same items twice?**  
>
> You shouldn’t, as display metrics will only be counted once.


**Example ad request**

```json
{
    "context": "digital_signage",
    "session_id": "random id",
    "device_id": "screen identifier",
    "store_name": "location identifier",
    "placements": {
        "name_of_the_location_where_the_screen_is": {
            "size": "1080x1920",
            "types": ["digital_signage"],
            "quantity": 1
        }
    },
    "segmentation": [
        {
            "key": "STATE",
            "values": [
                "RJ"
            ]
        },
        {
            "key": "CITY",
            "values": [
                "Rio de Janeiro"
            ]
        },
        {
            "key": "NEIGHBOURHOOD",
            "values": [
                "Cascadura",
                "Madureira"
            ]
        }
    ]
}
```

# Retrieving Ads During Checkout at the POS

In some cases, it is possible to identify the user making a purchase, typically during the payment process at the point of sale (POS).

Once the user is identified, you can request a personalized ad for that user.

> 📘 Segmentations
> 
> For segmented campaigns, an audience integration is required. [Audience Integration](#)

Example ad request

```json
{
    "context": "digital_signage",
    "user_id": "user identifier",
    "session_id": "random id",
    "device_id": "unique screen identifier",
    "store_name": "unique location identifier",
    "placements": {
        "name_of_the_location_where_the_screen_is": {
            "size": "1080x1920",
            "types": ["digital_signage"],
            "quantity": 5
        }
    },
    "segmentation": [
        {
            "key": "STATE",
            "values": [
                "RJ"
            ]
        },
        {
            "key": "CITY",
            "values": [
                "Rio de Janeiro"
            ]
        },
        {
            "key": "NEIGHBOURHOOD",
            "values": [
                "Cascadura",
                "Madureira"
            ]
        }
    ]
}
```

# Response

**Attributes**

| Attribute           | Description                                                                 | Type          |
|---------------------|------------------------------------------------------------------------------|---------------|
| `assets`            | URL and type of the campaign's image/video. One or more assets will be returned. | Array<Object> |
| `assets.#.url`      | URL of the object to be displayed                                            | String        |
| `assets.#.type`     | Type of the object<br><br>- image<br>- video                                 | String        |
| `assets.#.duration` | Duration of the asset                                                        | Integer       |
| `impression_url`    | Destination URL for the impression event                                     | String        |

**Payload**

```json
{
    "placement_name": [
        {
            "type": "digital_signage",

            "assets": [
                {
                   "type": "image|video",
                   "url": "image URL",
                   "duration": 30
                }
            ],

            "impression_url": "impression URL"
        }
    ]
}
```
