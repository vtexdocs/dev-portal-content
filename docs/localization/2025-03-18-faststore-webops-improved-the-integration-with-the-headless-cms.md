---
title: "FastStore WebOps: Improved the integration with the Headless CMS"
slug: "2025-03-18-faststore-webops-improved-the-integration-with-the-headless-cms"
type: improved
excerpt: "FastStore WebOps now displays detailed content publishing information from the Headless CMS."
createdAt: "2025-03-18T13:44:15.362Z"
updatedAt: ""
hidden: false
---

We've improved how FastStore WebOps displays deployment details for content published through the Headless CMS. FastStore WebOps now accurately reflects Headless CMS publications, making content changes clearer.

## What has changed?

Previously, when a user updated content through the Headless CMS, a new deployment entry would appear in FastStore WebOps. However, this entry displayed repetitive information related to the integration between the Headless CMS and the GitHub repository. The description, date, and author of the last Git-based deployment were shown for all content updates, which could lead to confusion.

Now, deployments display more accurate details from Headless CMS:

- For content updates to the live website, it’s displayed `Publish now` followed by the release ID.

  ![publish-now](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/publish-now.png)

- For scheduled content updates related to a release, it’s displayed the release name.

  ![add-a-release](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/add-a-release.png)

## What needs to be done?

No action is required. Users will automatically see the improved deployment information when publishing content through the Headless CMS.
