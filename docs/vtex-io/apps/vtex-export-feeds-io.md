---
title: "User Manual"
slug: "vtex-export-feeds-io"
excerpt: "vtex.export-feeds-io@1.5.17"
hidden: true
createdAt: "2022-07-06T20:27:44.227Z"
updatedAt: "2022-08-08T10:52:12.217Z"
---
This app was designed to export feeds containing data from vtex (catalog, masterdata, solr).

## Supported feeds:
- Reveal Customers/Categories/Products/Orders

## Firsts things first:  Sync catalog with masterdata
As an end-user, if you want to export feeds containing products, the first thing you will have to do is sync your catalog with your masterdata. To do this, press the `3 vertical dots` button next to the `New` button, and select Sync. This will trigger a long process, and it would be advised to wait between 15-60 minutes (depending on how many products you have in your catalog), before generating a product feed.

## Generating a new feed
If you click the `New` Button, an add modal will appear. I will further explain what each of the fields represent: 
- Service Type -> represents what type of service the feed will be used for, and therefore, designates the template structure of the feed. ( the options are hardcoded at the moment, but we're searching for a way to dynamically create templates for Service Types)
- Feed name -> self exaplanatory, important to be unique
- Feed Format -> JSON or CSV at the moment
- Contained Data 
  - Full Data -> the feed will be generated once, with records last updated between the `Start Date` and `End Date` Fields. 
  - Updated Data -> the feed will updated persistently. 
    - Hour of Update -> represents the hour on which the feed will update.
    - Day Of Update -> represents the day of the month on which the feed will update. (If not selected, the feed will update daily at the selected hour))  

Note: After creating a new feed, it may take a while before it's fully generated, depending on how many records your date interval covered, and the updates will apear only at page refresh.

If you want to access a feed, you can click on the `Link` blue button, this will copy the feed URL to your clipboard. You can share this URL with the service you want to integrate with. 


## API Specs
Generating the feed could mean: 
1. Making a call to a core service called [vtex.reports](https://github.com/vtex/reports) which receives a mapping (definition of the output), a data entity from which to extract the data and a query. 
2. Making calls to catalog APIs to get category information (with a limit of 2500 records maximum)

# Instalation Process

## Schema Initialization

You have to manually create the schemas. To do this, press the `3 vertical dots` button next to the `New` button and select `Update Schemas`

# More configurations
## Product Updates
If you want the products in the masterdata to be updated automatically when they are updated in the catalog, you need to do the following steps:
- Go to Admin -> Orders -> Orders management > Settings > Select Tab Affiliates
- Click new affiliate the endpoint `https://{account}.myvtex.com/_v/feed/productUpdate` where {account} is your account name. The rest of the settings are not important.

## More information
- For a detailed documentation of the flow read [this document](https://docs.google.com/document/d/1gOeEUs_-JDrEYirtcCM5HSkj95RZfmAgJO4V1cJLXws/edit#heading=h.hbqxtz6megn)