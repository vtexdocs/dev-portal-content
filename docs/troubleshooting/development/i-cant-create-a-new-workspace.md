---
title: "I can't create a new workspace"
slug: "i-cant-create-a-new-workspace"
excerpt: "New workspaces can only be created if the Intelligent Search integration is enabled."
hidden: false
createdAt: "2025-01-30T14:25:00.00Z"
updatedAt: "2025-01-30T14:25:00.00Z"
tags:
    - workspace
---

**Keywords:** Workspace | Intelligent Search

If you can't [create a new workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage#creating-a-new-workspace), you might be receiving the following error:

```plaintext
Render fail when sender is vtex.menu. Request failed with status code 400.
```

This issue is related to the Intelligent Search integration. To solve it, follow the instructions below.

1. Access the Admin and go to **Store Settings** > **Intelligent Search** > **Integrations**.
2. Check if the search has been activated in the store.
3. Click the `Start integration` button to start integration.

The indexing process will start and you will see a link to the Indexing Status screen.

> ℹ️ The [Integration settings](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/6wKQgKmu2FT6084BJT7z5V) is responsible for the Catalog's initial indexing with VTEX Intelligent Search. After installing the application, this will be the first step to integrating it with the Catalog.

![start-integration](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/development-1.png)
