---
title: "qaolimpica Change Seller"
slug: "qaolimpica-change-seller"
excerpt: "qaolimpica.change-seller@0.6.0"
hidden: true
createdAt: "2022-07-15T14:27:15.786Z"
updatedAt: "2022-08-09T14:27:07.753Z"
---
This application allows to transfer orders from a seller __white label__ to another one.

![Principal module](https://user-images.githubusercontent.com/60228986/169353787-ab628471-6f58-4068-bc8d-3d086f334c59.png)
![Order details](https://user-images.githubusercontent.com/60228986/169354451-d401892d-6461-4671-af64-959adfedd9b7.png)

## Configuration 

The main steps to enable __change order seller__ app into your admin modules are: 

1. From CLI login into your account by running ```vtex login {{accountName}}``` 
2. Intall application ```vtex install qaolimpica.change-seller```

Finally you need to add some configurations from master data, to do that please follow the next steps:

>**Important:** Behind the scenes this application validates the order's payment methods allowed to transfer, to do that it consults to _master data table_ that contain these _payment methods names_ ej. *Promissory* and a boolean value (true or false) that indicates if its correspondent payment method could be transfer or not. If you dont create or configurate this entity and table, the change order seller module wont allow users to transpher any order, it will block the simulation button and the transpher process.

1. Go to your admin module _https://{{accountName}}.myvtex.com/admin_
2. Click on _Master data_ Tab
3. Create a new entity, to get more information about how to create entities check [this vtex's tutorial](https://help.vtex.com/tutorial/creating-data-entity--tutorials_1265). To create the __entity__ take account recomendations below:

  - **Acronym:** PA (It must have this value("PA") because change seller app is setting to search this acronym to read allowed payment methods)
  - **Name:** paymentMethodAllowed
  - **Fields:** Next are mandatory names, types, and settings
    - ⚙️isAllowed [Boolean]
      - [x] is nullable 
      - [x] Make readable without credential
      - [ ] Allow editing without credential (It isn't necessary to check)
      - [x] Allow filter without credential
      - [x] Is searchable?
      - [x] Is filterable?
    - ⚙️paymentSystemName [Text]
      - [x] is nullable 
      - [x] Make readable without credential
      - [ ] Allow editing without credential (It isn't necessary to check)
      - [x] Allow filter without credential

    >**Note:** Be sure that fields have the correspondent settings and finally remember to __save__, __publish__ and __index__ the entity

4. Now you are able to create a __table__, which will contain the allowed payment method names, to do that follw [this vtex tutorial](https://help.vtex.com/tutorial/creating-form-in-master-data--tutorials_1047#) or [![watch this video]()](https://assets.contentful.com/alneenqid6w5/7oRARnBsVamuk8iQ0mogQa/438e55214f38f7f16634da4fbc238d68/CriandoFormulario-1.mp4?_=3)

    - At __data entity__ field be sure to select the created at previous step