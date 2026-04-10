---
title: "User Rights API: Automated personal data erasure"
slug: "2026-05-21-user-rights-api-automated-personal-data-erasure"
hidden: false
type: "added"
createdAt: "2026-05-21T14:00:00.000Z"
excerpt: "The new User Rights API allows you to automate personal data erasure requests across VTEX applications."
---

The new [User Rights API](https://developers.vtex.com/docs/api-reference/user-rights-api) allows you to automate the deletion of a user's personal data across VTEX applications, in compliance with "Right to be Forgotten" regulations.

> ℹ️ This feature is in open beta.

> ⚠️ The user rights flows available in this API apply only to non-corporate shoppers. They don't apply to B2B buyers or Admin users.

## What has changed?

Previously, deleting a user's personal data required a manual process through Copilot, as described in [Erasing customer data](https://help.vtex.com/docs/tutorials/erasing-customer-data). Now, you can integrate with the User Rights API to handle these requests programmatically.

The API provides two endpoints:

- [Create data erasure job](https://developers.vtex.com/docs/api-reference/user-rights-api#post-/api/user-rights/forget/jobs): Submit a user's email to start the deletion process and receive a job ID.
- [Get data erasure job status](https://developers.vtex.com/docs/api-reference/user-rights-api#get-/api/user-rights/forget/jobs/-jobId-): Poll the job ID to track the deletion progress until it completes.

## Why did we make this change?

To provide merchants with a scalable, automated way to fulfill personal data erasure requests, eliminating the need for manual processing of each individual request.

## What needs to be done?

No action is required. The existing manual flow remains available.

To adopt the automated workflow, refer to the [User Rights API integration guide](https://developers.vtex.com/docs/guides/user-rights-data-erasure) for step-by-step implementation instructions.
