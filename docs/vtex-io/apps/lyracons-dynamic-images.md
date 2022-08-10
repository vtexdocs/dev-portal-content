---
title: "Dynamic Images"
slug: "lyracons-dynamic-images"
excerpt: "lyracons.dynamic-images@0.0.1"
hidden: true
createdAt: "2022-07-06T15:19:29.008Z"
updatedAt: "2022-07-06T15:19:29.008Z"
---
This customApp extends the `vtex.list-context.image-list` component, but allows the user to input sellers in which they want to hide the image. This allows for images to be dynamic based on where the user is regionalized. 

The app adds two inputs to the `vtex.list-context.image-list`  component: 

- Regionalization Method (Global Setting): Select if the regionalization will be selected by postalCode or geoCoordinates

- Sellers To Hide: Text input in which the user can add the sellers in which the image will not be shown (Separated by comas)



# Configuration

1. Add the `dynamic-images` app to your theme's dependencies in the `manifest.json`, for example:

```diff
 "dependencies ": {
+  "lyracons.dynamic-images": "0.x"
 }
```

2. Add the `dynamic-image-list` wherever you want. Here's an example:

```
	"flex-layout.row#slider-banner-principal": {
		"title": "home-slider-banner-Banner principal",
		"props": {
			"blockClass": "slider-banner-principal",
			"fullWidth": true
		},
		"children": [
			"dynamic-image-list#main-banner"
		]
	},
	"dynamic-image-list#main-banner": {
		"children": ["slider-layout#main-banner-slider"],
		"props": {
			"preload": true,
			"images": [
				{
					"image": "assets/content/main-banner-desktop.jpg",
					"mobileImage": "assets/content/main-banner-mobile.jpg",
					"description": "Description",
					"width": "100%",
					"maxHeight": 1000,
					"link": {
						"url": "/",
						"title": "home-Home"
					}
				}
			]
		}
	},
```