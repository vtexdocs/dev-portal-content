---
title: VTEX IO Closed Beta list 
excerpt: "VTEX IO now has a new workflow to require platform development permissions! Find out more about the change and about what you need to do when accessing the VTEX IO Closed Beta list file."
createdAt: "2020-03-16"
---

> ⚠️ (Edited on 2023-07-07) We no longer require app developers to fill out the application form to use VTEX IO builders as stated in [this latest announcement](https://developers.vtex.com/updates/release-notes/application-form-to-access-vtex-io-builders-is-no-longer-required).

As a closed beta solution, VTEX IO has a new workflow for platform development permissions: it is now required to submit a form with your project details to our product team. 

## What has changed?

Previously, VTEX IO platform development permissions were granted by account. 

The process was as follows: an account X would match the [prerequisites needed](https://developers.vtex.com/docs/guides/vtex-io-documentation-frequently-asked-questions) to develop on the platform and get in touch with our support team which, according to the project, would grant access to the builders needed. 

This concession is no longer granted by account. Instead, builder permissions will be linked to app majors. 

This means that an account wanting to develop on the platform will need to specify both the app and the major it intends to work on. The builder permissions will consequently be granted for that app's major, not for the account itself.

## Why did we make this change?

This change is mainly about transparency. As a team that is aware of the platform's continuous evolution, we want to be able to identify what is being developed on VTEX IO, improve the resilience and security of linking and deploying apps, and identify opportunities to serve recurrent use cases natively. 

Looking at the previous process, this greater visibility was not possible since the only data about what was being developed on the platform were the account name and builders to which it had access. 

## Side effects

This release does not affect any of the closed beta list accounts developing already published platform apps; it only affects apps that have yet to be published. 

Even if no permissions were requested for an app's major following the new workflow, VTEX IO CLI (during the linking or publishing process) will investigate whether the app's major on which the account is working was already published. 

If the app's major has already been published, it will then be automatically saved in the database for the account in question, which will effortlessly receive the necessary permissions (according to the new workflow for the app's major) to seamlessly develop and continue to evolve its project. 

However, if the app's major has never been published, the account will not be able to link or publish the app on which it is working, making its development on the platform impossible. 

## What needs to be done?

If your development process was interrupted by the new Closed Beta list workflow, it means that the app's major you're working on has not yet been published. 

In such a case, VTEX IO CLI won't be able to automatically grant your account permission to those apps' majors. You will then need to submit your project details to our product team by filling out the form, specifying the app's major you wish to work on.

Thus, our team will gain visibility over your project and be able to analyze each project individually to ensure that the required permissions are granted.
