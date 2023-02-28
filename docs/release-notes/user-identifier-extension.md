---
title: User Identifier Extension
excerpt: "No more forcing users to log in with their email address. With the User Identifier Extension, you can choose user identifiers at will."
createdAt: "2019-11-10T14:47:00.000Z"
---

The Login component just gained a new improvement: the User Identifier Extension. Through it, users can now log in using other user identifiers in your store, without these necessarily being their e-mails. 

## What has changed

Traditionally, the VTEX IO store's login form only accepted two inputs: e-mail (as user identifier) and password. 

**The** `User Identifier Extension` **now allows other user identifiers, apart from the e-mail, to also be used on the login form through an extension app**. This extension app's function is to interpret the user identifier chosen on the login form and send the system the email that's linked to that user. 


> ⚠️ The login improvement doesn't handle the extension app's development. This is up to you, according to your store's desired user identifier. The `User Identifier Extension` merely supports the extension app. 


## Main advantages

With the `User Identifier Extension`, the login component gained more **flexibility** to serve various store scenarios and users. After an extension app is created to support this new feature, there's no need to request email addresses from users during login anymore: they will be able to use whatever user identifier you choose. 

## What you need to do

This Login component improvement is available from version **2.16.0**. 

:eyes: Do not forget to check out the Login component [documentation](https://vtex.io/docs/app/vtex.login) to understand the new feature functionalities and limitations, in addition to seeing an example of an extension app for this scenario.
