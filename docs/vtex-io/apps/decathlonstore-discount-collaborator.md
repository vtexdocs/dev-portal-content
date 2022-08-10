---
title: "Welcome to Discount Collaborator 👋"
slug: "decathlonstore-discount-collaborator"
excerpt: "decathlonstore.discount-collaborator@0.3.9"
hidden: true
createdAt: "2022-07-19T15:30:22.349Z"
updatedAt: "2022-07-19T16:53:01.907Z"
---
> repository of the VTEX IO application that controls the cluster of collaborators. Processing data provided by Propay, this app updates daily and includes employees from the cluster daily.

## Api Propay

more information api propay: [Propay](http://connect.propay.com.br:8060/swagger/ui/index#/)


## Install 

this app follows a vtex io app structure, further information: [Vtex IO](https://vtex.io/docs/)

## Status

* to check the status of the application access: https://www.decathlon.com.br/discount-collaborator-health 

## Usage

* To add new active collaborators to the cluster: https://discountcollaborator--decathlonstore.myvtex.com/includeCollaborators

* To remove inactive collaborators in the cluster: https://discountcollaborator--decathlonstore.myvtex.com/removeCollaborators


#### Cron job was configured to access these routes daily, keeping the cluster always up to date. The cron service used was: [Cron Job](https://console.cron-job.org), further information [Info](https://edecathlon.atlassian.net/wiki/spaces/DECATHLON/pages/959741953/Cron+Job+Service).