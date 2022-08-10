---
title: "HOW TO USE"
slug: "vtex-image-protocol-example-howtouse"
excerpt: "vtex.image-protocol-example@0.5.2"
hidden: true
createdAt: "2022-07-29T11:41:23.880Z"
updatedAt: "2022-08-02T07:41:18.920Z"
---
## Required apps to install in the workspace:

- store-image version 0.14.3-beta3.hkignore
- store-components version 3.161.28-beta4.hkignore
- image-protocol version 1.0.3
- image-protocol-example version 0.3.2

## First steps

Once these apps have been installed the first step is to configure the API endpoint and token in the Admin, inside Apps > My apps > Image Protocol App:

![Settings](../public/metadata/images/howtouse/image-protocol-settings.png)

> **NOTE**: This endpoint is defined in the image-protocol-example app (http://{workspace}--{account}.myvtex.com/\_v/image-protocol-example/get-url)
> To specify which element will render the content it’s required to access the Site Editor section and add a value for the image protocol id:

To illustrate an example: the first image of the Image List is selected and the image protocol id property is set to ‘beta’.

![Site Editor](../public/metadata/images/howtouse/site-editor1.png)

![Site Editor](../public/metadata/images/howtouse/site-editor2.png)

In case the personalization would be based on the customer class, this information can be accessed through the Master Data in the clients section:

![Access Masterdata](../public/metadata/images/howtouse/masterdata1.png)

![Masterdata](../public/metadata/images/howtouse/masterdata.png)

> **NOTE**: If you don’t see the customer class field, check this tutorial:
> https://drive.google.com/file/d/14fmqwQqyMwEr3IXVUDQZ1kgZMbki_knm/view?usp=sharing

In case the personalization would be based on the geolocation, this information can be accessed through the Geolocation Shipping section.

![Geolocation Shipping](../public/metadata/images/howtouse/geolocation.png)

> **NOTE**: If a new polygon is needed check this tutorial to create it: https://help.vtex.com/tutorial/registering-geolocation--tutorials_138

## Priorities

The personalization can be based on both (customer class and geolocation independently or in conjunction).
Priorities can be specified inside Apps > My apps section for the Image Protocol Example App:

![Priorities](../public/metadata/images/howtouse/priorities.png)

> **NOTE**: Customer class would be set highest priority by default

## Save content

To save the personalized content based on one or both conditions access the Image Protocol section and fill the form:

![Create new](../public/metadata/images/howtouse/create.png)

![Form](../public/metadata/images/howtouse/fill-form.png)

Data will be saved and displayed in a table (there are edit/delete options)

![Edit/Delete](../public/metadata/images/howtouse/edit-delete.png)

## Check the result

Once the user is logged in and allowed to share the location, the images displayed will be the ones saved for that specific customer class and location.

Desktop view:

![Desktop](../public/metadata/images/howtouse/result-desktop.png)

Mobile view:

![Mobile](../public/metadata/images/howtouse/result-mobile.png)

If the user is logged in but has not allowed to share the location the images displayed will be the default ones.

![Location denied](../public/metadata/images/howtouse/no-location.png)

If the user has not logged in the images displayed will be also the default ones.

![Not logged in](../public/metadata/images/howtouse/no-logged.png)