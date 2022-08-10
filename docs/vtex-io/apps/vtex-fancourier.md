---
title: "VTEX FanCourier"
slug: "vtex-fancourier"
excerpt: "vtex.fancourier@0.0.3"
hidden: true
createdAt: "2022-08-08T10:48:38.097Z"
updatedAt: "2022-08-08T10:48:38.097Z"
---
This application allows you to integrate shipping using FanCourier API.


## Installation Guide

- Open the VTEX App Store and install this app on your store, or run the following command on VTEX toolbelt:

> vtex install vtex.fancourier@0.x

### Application Settings

Go to `Admin > Apps > My Apps` and find the application
Fill out the form with your FanCourier username, password and client id.

### Request AWB

* Go to `Admin > FanCourier shipping list`
* Select an order ( the selected order should contain `Request awb` in status )
* Under the Order details section, select the Service
* Press the `Request AWB` button