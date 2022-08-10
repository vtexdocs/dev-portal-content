---
title: "The North Face STORE FRAMEWORK"
slug: "timberlandmx-store-theme"
excerpt: "timberlandmx.store-theme@6.0.3"
hidden: true
createdAt: "2022-07-06T21:00:48.229Z"
updatedAt: "2022-08-09T20:03:22.979Z"
---
Repo for The North Face website develloped in VtexIO Store Framework

## VTEX IO Toolbelt

To install VTEX IO’s CLI, you need to ensure that Node.js and Yarn are installed on your machine.

`yarn global add vtex`

To confirm that the installation occurred as expected, you can execute the vtex command. This should display all available commands in a help text.

`vtex`

### Login

Once VTEX IO’s CLI is installed, you can login to your VTEX account with the following command. This would in turn open a browser window asking for your credentials.

`vtex login timberlandmx`

When you are logged in, you can use the `vtex whoami` command to uncover which account and workspace is being used by the terminal.

### Creating your own workspace

When using VTEX IO, any interaction with an account happens in a workspace. As you log into a store, you are automatically in its master workspace, meaning you are in the version available to the end user. Therefore, always remember to create a development workspace using the vtex use command whenever you want to test a new configuration.

`vtex use {examplename}`

> This changes your Toolbelt to a so-called examplename workspace and creates it if it doesn’t already exist.

Having created your own development workspace, you can go to your store by accessing:

`https://{workspace}--timberlandmx.myvtex.com`

Where {workspace} is the workspace that you've just created.

### Linking your local code to VTEX IO

> Run vtex whoami to be sure that you're in the right account and in a development workspace. Otherwise, Toolbelt will not accept the link directly with the master workspace.

`vtex link`

If the process runs without any errors, the following message will be displayed: `App linked successfully`. Then, run the `vtex browse` command to open a browser window having your linked store in it.

This will enable you to see the applied changes in real time, through the account and workspace in which you are working.

# Dependencies for this theme

```
vtex install vtex.admin-search@1.x
```

```
vtex install vtex.search-resolver@1.x
```

### Custom app dependencies

Some apps need to be installed for the store to function properly in your workspace.
We use a custom application called 'image grid'.

You need to install it:

```
vtex install timberlandmx.product-image-grid
```

```
vtex install timberlandmx.newsletter-signup-with-validation
```