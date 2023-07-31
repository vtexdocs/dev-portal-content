---
title: "Headless CMS Plugin v1.0.8: Improved sync command"
slug: "2023-07-31-improved-headless-cms-plugin"
type: "improved"
createdAt: "2023-07-31T10:28:00.000Z"
excerpt: "The latest version of the Headless CMS plugin, 1.0.8, brings enhancements to the vtex cms sync command feedback."
---

The latest version of the Headless CMS plugin, `1.0.8`, brings enhancements to the `vtex cms sync` command feedback. These improvements address user authentication and access permission issues. The terminal will now present precise error messages when faced with such scenarios, making it easier for developers to identify and resolve access-related problems that may arise during the synchronization process.

## What has changed?

The `vtex cms sync` command synchronizes changes made in a FastStore project, including modifications to new sections or content types for Headless CMS.

In the previous versions, when users attempted to run `vtex cms sync` command without the necessary permissions to access the Headless CMS or if they were logged out of their accounts, a misleading successful message would be displayed in the terminal, even if the changes were not synchronized in the Headless CMS interface.

Now, with the Headless CMS plugin `v1.0.8`, you can expect precise error messages to appear in the terminal when encountering authentication or insufficient permissions to sync changes in your FastStore project with Headless CMS. These error messages will help you quickly identify and resolve access-related problems.

- **User without permission to access the Headless CMS**
![no-permission-to-cms-message](https://vtexhelp.vtexassets.com/assets/docs/src/cms-error-message-permission___003887a63347ef3663d532cac01feb0a.png)

- **User that has been logged out of their account**
![logged-out-account-message](https://vtexhelp.vtexassets.com/assets/docs/src/cms-error-message-login___40a4de3dbf35aeb953e0f003ce083ee1.png)
Why are we making this change?
This update aims to enhance the developer experience during the `vtex cms sync` process. Providing better feedback and more accurate error messages for access issues helps reduce debugging time.

What needs to be done?
To benefit from the enhancements in the Headless CMS plugin version `1.0.8`, follow the steps below:




> ⚠️  Remember to replace the values between curly brackets according to your

> ⚠️  Remember to replace the values between curly brackets according to your
```bash
vtex login {account}
```

2. Update the `@vtex/cli-plugin-cms` to version `1.0.8` by running the following command:

```bash
vtex plugins update
```
3. Run `vtex cms sync` and check what you should do if the following messages display:

`Error: Permission denied`:
If applicable, ask the account’s administrators you are trying to make the sync to check your user role to the Headless CMS in VTEX Admin.  For more information, refer to [Roles](https://help.vtex.com/pt/tutorial/roles--7HKK5Uau2H6wxE1rH5oRbc).

`Error: You’ve been logged out`
Log back into the account you are trying to make the sync and run `vtex cms sync` again.
