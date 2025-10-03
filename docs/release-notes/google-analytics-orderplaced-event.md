---
title: Google Analytics `orderPlaced` event
excerpt: "Make your Google Analytics metrics more reliable with the `orderPlaced` event trigger improvement."
createdAt: "2019-09-13T14:47:00.000Z"
type: 'info'
---
 Google Analytics `orderPlaced` event is no longer triggered twice when the Order Placed page is reloaded. 
 
## What has changed

The `orderPlaced` event, triggered when users access a store's Order Placed page, was triggering twice when reloading the page. For example: if the user would refresh the page, the event would be triggered again. 

With this improvement, the event is no longer triggered upon page reload or refresh. Instead, another event is triggered: the `orderPlacedTracked`. 

## Main advantages 

Triggering this event twice would mislead the retailer by changing Analytics data as if more page access had occurred that was in fact the case.

Improving the trigger makes your store's Google Analytics data more **reliable** and **consistent**.

## What you need to do

Don't worry: this improvement is already available to everyone!
