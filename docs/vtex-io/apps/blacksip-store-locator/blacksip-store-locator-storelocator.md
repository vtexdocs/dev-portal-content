---
title: "Store Locator"
slug: "blacksip-store-locator-storelocator"
excerpt: "blacksip.store-locator@2.0.1"
hidden: true
createdAt: "2022-08-03T13:31:43.588Z"
updatedAt: "2022-08-03T13:31:43.588Z"
---
The `store-locator` is the block responsible for showing the available physical stores and their information, it has a navigation by levels and shows the store location on a map

![image](https://user-images.githubusercontent.com/17678382/101309181-c081c500-3819-11eb-8927-c1db3dab5f96.PNG)

## Configuration

1. Import the `blacksip.store-locator` app to your theme's dependencies in the `manifest.json`, for example:

```json
{
    "dependencies": {
        "blacksip.store-locator": "0.x"
    }
}
```

2. Add the `store-locator` block to any block below `store.custom#storeLocator` (page custom template). For example:

```json
{
    "store.custom#storeLocator": {
        "blocks": ["flex-layout.row#storeLocator"],
        "flex-layout.row#storeLocator": {
            "children": ["blacksip.store-locator:store-locator"]
        }
    }
}
```

3. While the project is under development and the final delivery to the customer is not done, use the following API Key in the Google Maps API Key field found in the Checkout `AIzaSyB4wwZij7RCPD78w5Fgxbq0uUwvCEEiH20`

4. Add file `storeLocatorData.json` in checkout files
   ![image](https://user-images.githubusercontent.com/17678382/101668539-a7963100-3a1e-11eb-9e57-d75577058ac2.PNG)

```json
[
    {
        "name": "tienda1",
        "direction": "calle falsa 123",
        "phone": "2312312",
        "email": "jairdiaz@blacksip.com",
        "horary": "lunes a sabado de tal a tal",
        "images": [
            {
                "id": 1,
                "alt": "imagen",
                "url": "/arquivos/preview-image-store-locator.png"
            },
            {
                "id": 2,
                "alt": "imagen",
                "url": "/arquivos/preview-image-store-locator.png"
            },
            {
                "id": 3,
                "alt": "imagen",
                "url": "/arquivos/preview-image-store-locator.png"
            },
            {
                "id": 4,
                "alt": "imagen",
                "url": "/arquivos/preview-image-store-locator.png"
            },
            {
                "id": 5,
                "alt": "imagen",
                "url": "/arquivos/preview-image-store-locator.png"
            }
        ],
        "videos": [
            {
                "id": 1,
                "url": "/arquivos/preview-image-store-locator.png"
            },
            {
                "id": 2,
                "url": "/arquivos/preview-image-store-locator.png"
            }
        ],
        "level1": "Cundinamarca",
        "level2": "Bogotá",
        "level3": "suba",
        "level4": "tienda1",
        "lat": 4.696409591692454,
        "lgn": -74.08653110674076
    },
    {
        "name": "tienda2",
        "direction": "calle falsa 123 2",
        "phone": "2312312",
        "email": "jairdiaz@blacksip.com",
        "horary": "lunes a sabado de tal a tal",
        "description": "esta tienda es my bonita",
        "level1": "Cundinamarca",
        "level2": "Bogotá",
        "level3": "suba",
        "level4": "tienda2",
        "lat": 4.655090902985468,
        "lgn": -74.10979122626551
    },
    {
        "name": "tienda3",
        "direction": "calle falsa 123 3",
        "phone": "2312312",
        "email": "jairdiaz@blacksip.com",
        "horary": "lunes a sabado de tal a tal",
        "description": "esta tienda es my bonita",
        "level1": "Cundinamarca",
        "level2": "Bogotá",
        "level3": "chico",
        "level4": "tienda3",
        "lat": 4.685203178804706,
        "lgn": -74.11630515500919
    },
    {
        "name": "tienda4",
        "direction": "calle falsa 123 3",
        "phone": "2312312",
        "email": "jairdiaz@blacksip.com",
        "horary": "lunes a sabado de tal a tal",
        "description": "esta tienda es my bonita",
        "level1": "Antioquia",
        "images": [
            {
                "id": 1,
                "alt": "imagen",
                "url": "/arquivos/preview-image-store-locator.png"
            }
        ],
        "level2": "Medellin",
        "level3": "las vegas",
        "level4": "tienda1",
        "lat": 6.229614212489227,
        "lgn": -75.57095528824632
    }
]
```

| Prop name | Type     | Description                            | Default value     |
| --------- | -------- | -------------------------------------- | ----------------- |
| `levels`  | `Number` | Levels to show max 4                   | `2`               |
| `lat`     | `Number` | Default latitude                       | `4.6839895`       |
| `lgn`     | `Number` | Default length                         | `-74.0493608`     |
| `map`     | `Object` | Settings for the map                   | `Object *map*`    |
| `switch`  | `Object` | Settings for layout of the information | `Object *switch*` |

-   **`map` object**

| Prop name    | Type     | Description                     | Default value |
| ------------ | -------- | ------------------------------- | ------------- |
| `width`      | `String` | Map width                       | `100%`        |
| `height`     | `String` | Map height                      | `500px`       |
| `icon`       | `String` | Map icon                        | `Icon google` |
| `iconWidth`  | `String` | Icon width                      | `15px`        |
| `iconHeight` | `String` | Icon height                     | `15px`        |
| `zoomPoint`  | `Number` | Map zoom when selecting a point | `17`          |
| `ZoomLevel`  | `Number` | Map zoom when selecting a level | `5`           |

-   **`switch` object**

| Prop name       | Type      | Description                          | Default value |
| --------------- | --------- | ------------------------------------ | ------------- |
| `switchOption1` | `Boolean` | Show slider in the section of stores | `true`        |
| `switchOption2` | `Boolean` | Show infoWindow                      | `true`        |
| `switchOption3` | `Boolean` | Show slider in infoWindow            | `false`       |

## Customization

In order to apply CSS customizations in this and other blocks, follow the instructions given in the recipe on [Using CSS Handles for store customization](https://vtex.io/docs/recipes/style/using-css-handles-for-store-customization).

| CSS Handles                   |
| ----------------------------- |
| `globalContainer`             |
| `title`                       |
| `subtitle`                    |
| `description`                 |
| `containerInfo`               |
| `containerLevel1`             |
| `containerLevel2`             |
| `containerLevel3`             |
| `containerMap`                |
| `containerStoreInfo`          |
| `storeNameLabel`              |
| `storeDirectionLabel`         |
| `storePhoneLabel`             |
| `storeEmailLabel`             |
| `storeHoraryLabel`            |
| `storeDescriptionLabel`       |
| `storeName`                   |
| `storeDirection`              |
| `storePhone`                  |
| `storeEmail`                  |
| `storeHorary`                 |
| `storeDescription`            |
| `load`                        |
| `markerInfo`                  |
| `markerStoreNameLabel`        |
| `markerStoreDirectionLabel`   |
| `markerStorePhoneLabel`       |
| `markerStoreEmailLabel`       |
| `markerStoreHoraryLabel`      |
| `markerStoreDescriptionLabel` |
| `markerStoreName`             |
| `markerStoreDirection`        |
| `markerStorePhone`            |
| `markerStoreEmail`            |
| `markerStoreHorary`           |
| `markerStoreDescription`      |

## Custom translations

1. Install the `vtex.admin-graphql-ide@3.x` app using your terminal.
2. Access the **GraphQL admin IDE** section of the desired account. You may find it in the admin's side-bar menu:
   ![image](https://user-images.githubusercontent.com/52087100/66516950-95d29a00-eab8-11e9-8cea-080fbdab84d5.png)
3. From the dropdown list, choose the `vtex.messages` app.
4. Write the following mutation command in the text box that is displayed:

```JSON
mutation Save($saveArgs: SaveArgsV2!) {
  saveV2(args: $saveArgs)
}
```

5.  Then, click on **Query Variables** at the bottom of the page. Now, your screen may look like the following:
    ![image](https://user-images.githubusercontent.com/60782333/85610649-8e92f280-b62d-11ea-9a5e-aa7ced1a1549.png)
6.  Write the following statement in the **Query Variables** tab

```JSON
{
 "saveArgs": {
   "to": "en-US",  //Target translation locale.
   "messages": [
     {
       "srcLang": "en-DV", //Source message locale. Always must be en-DV.
       "srcMessage": "store/store-locator.title", //The id of your message string declared in the app's messages folder.
       "context": "blacksip.store-locator@0.x", //The name of the app in which the message is being overwritten.
       "targetMessage": "Store locator" //Translated message string.
     }
   ]
 }
}
```

7.  Click on the **run button**.

> ℹ️ **NOTE:** To better understand the full process of overwriting an app message translation, [click here](https://vtex.io/docs/recipes/development/overwriting-the-messages-app/)

## Id messages

| id                                               |
| ------------------------------------------------ |
| `store/store-locator.title`                      |
| `store/store-locator.subtitle`                   |
| `store/store-locator.description`                |
| `store/store-locator.labelLevel1`                |
| `store/store-locator.labelLevel2`                |
| `store/store-locator.labelLevel3`                |
| `store/store-locator.labelLevel4`                |
| `store/store-locator.infoLabel.labelName`        |
| `store/store-locator.infoLabel.labelDirection`   |
| `store/store-locator.infoLabel.labelPhone`       |
| `store/store-locator.infoLabel.labelEmail`       |
| `store/store-locator.infoLabel.labelHorary`      |
| `store/store-locator.infoLabel.labelDescription` |