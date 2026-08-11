---
title: "Troubleshooting"
hidden: false
slug: "cms-troubleshooting"
createdAt: "2026-07-08T12:50:00.813Z"
updatedAt: "2026-07-08T09:00:00.813Z"
excerpt: "Troubleshoot common errors during CMS schema generation, upload, and Admin access, including permission issues, FastStore CLI detection failures, and missing components in the section picker."
---

Troubleshoot common errors during CMS schema generation, upload, and Admin access.

**Keywords:** CMS, FastStore, CLI, schema, sync, content plugin

Developers may encounter the following errors when working with CMS schemas locally, particularly when running `faststore cms-sync`, `vtex content generate-schema`, or `vtex content upload-schema`.

| Error message | Possible cause | Solution |
| :---- | :---- | :---- |
| `Error: Permission denied` | The user role doesn't have the required CMS permissions. | [Grant user CMS access](#grant-user-cms-access) |
| `Could not detect the @faststore/cli version` | The command is running outside the storefront project root, or the FastStore CLI package is not in `package.json`. | [Fix FastStore CLI detection](#fix-faststore-cli-detection) |
| Component doesn't appear in the section picker after upload | The store ID is mismatched, or the content type doesn't reference the component. | [Fix missing component in section picker](#fix-the-missing-component-in-the-section-picker) |

## Solutions

### Grant user CMS access

Use this path when the error is related to permissions in the CMS Admin or during schema upload.

1. Open the VTEX Admin and go to **Account Settings \> User Roles**.  
2. Select the role associated with the affected user.  
3. In **Products and Resources**, click **CMS**.  
4. Make sure the required CMS permissions are checked, including **See CMS menu on the top-bar** and **Settings**.  
5. In the **Users** section, confirm the user's email is added to the role.  
6. Click **Save**.  
7. Ask the user to run the sync command again and verify that the error no longer appears.

For more details on CMS permissions, see [Roles - License Manager](https://help.vtex.com/en/tutorial/roles--7HKbd9jg39YZlsqhqZPHbR).

### Fix FastStore CLI detection

Use this path when `generate-schema` exits with a message that it couldn't detect the FastStore CLI version.

#### Verify your working directory

1. Open the terminal.  
2. Make sure you are in the root of your storefront project, the directory that contains `package.json`.  
3. Run the sync command again.

#### Pass the version manually

If the error persists after confirming your working directory, pass the base version flag explicitly:

```shell
vtex content generate-schema --base vtex.faststore@3
```

or

```shell
vtex content generate-schema --base vtex.faststore@4
```

Replace the version number with the FastStore major version your project uses.

### Fix the missing component in the section picker

Use this path when the schema upload succeeds, but the new component does not appear in the CMS Admin section picker.

#### Verify the store ID

1. Open the terminal output from the sync command.  
2. Check the store ID that was used during upload (e.g., `cmsdev.faststore`).  
3. In the CMS Admin, confirm you are viewing a page that belongs to the same store.  
4. If the store IDs don't match, re-run the sync command and enter the correct store ID when prompted.

#### Check the content type configuration

1. Navigate to the `cms/{storeId}/pages/` directory in your project.  
2. Open the content type file for the page where you expect the component to appear (e.g., `cms_content_type__landingPage.jsonc`).  
3. Check the `sections` property. It must either:  
   * Reference `#/$defs/$ALLOW_ALL_COMPONENTS` to allow all components, or  
   * Explicitly list your component's `$componentKey`.  
4. If the content type does not reference your component, add it, then re-generate and re-upload the schema.

#### Re-sync after changes to pages

Any change to files in the `pages/` directory requires a full re-sync. Run the sync command again after modifying content type definitions to ensure the CMS Admin reflects the updated configuration.
