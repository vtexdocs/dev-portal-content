---
title: "FastStore WebOps: Improved the integration with the Headless CMS"
slug: "2025-03-18-faststore-webops-improved-the-integration-with-the-headless-cms"
type: improved
excerpt: "FastStore WebOps now displays detailed content publishing information from the Headless CMS."
createdAt: "2025-03-18T13:44:15.362Z"
updatedAt: ""
hidden: false
---

We've improved how FastStore WebOps displays deployment details for content published through the Headless CMS. FastStore WebOps now accurately reflects publications made via the Headless CMS, making content updates clearer and easier to track.

## What has changed?

Previously, whenever a user updated content through the Headless CMS, a new deployment entry was displayed in FastStore WebOps. However, these entries repeated the same details — description, date, and author — from the last Git-based deployment. This could cause confusion, as the information didn't reflect the actual content update.

Now, deployments display more accurate details from the Headless CMS:

- For content updates to the live website, it displays `Publish now` followed by the release ID.

  ![publish-now](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/publish-now.png)

- For scheduled content updates related to a release, it displays the release name.

  ![add-a-release](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/add-a-release.png)

## What needs to be done?

No action is required. Users will automatically see the improved deployment information when publishing content through the Headless CMS.
