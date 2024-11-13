---
title: "Managing application logs"
slug: "vtex-io-documentation-managing-application-logs"
hidden: false
createdAt: "2020-09-22T21:29:09.307Z"
updatedAt: "2022-12-13T20:17:44.453Z"
---
VTEX IO provides a logging service that allows developers to keep track of app errors, warnings, and informative events. The VTEX IO Logging Service collects data from the cloud infrastructure where VTEX applications run and delivers them via the VTEX IO CLI.

In the following section, you'll learn how to implement the VTEX IO Logging Service in your apps and how to retrieve their respective logs.

> ℹ️ The VTEX IO Logging Service is currently available for Node apps only.

---

## Before you begin

To follow this guide, you must have the VTEX IO CLI installed on your machine. For more information, please see [this document](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-install).

---

## Instructions

### Implementing the VTEX IO Logging Service

1. Open your Node app in the code editor of your choice.
2. Define an object with the `Context` interface as a parameter in a function where you want to provide logging messages. See the following example:

```ts
const helloWorld = (ctx: Context) => {
  const { vtex: { logger } } = ctx

  logger.info('Hello World!')
}
```

In this example, the `helloWorld` function receives an object with a [**Context**](https://github.com/vtex/node-vtex-api/blob/master/src/service/worker/runtime/typings.ts#L34) interface as a parameter.

> ℹ️ The `Context` interface contains many implementations inherent to the VTEX IO platform. One of those implementations is called `vtex` — an object containing all [VTEX IO infrastructure](https://github.com/vtex/node-vtex-api/blob/master/src/service/worker/runtime/typings.ts#L116) related metadata, such as `account`, `workspace`, `tenant`, `settings`, and some service implementations. In the previous example, we used the `logger` service, an implementation inside `vtex` that generates log messages.

3. [Destructure](https://www.typescriptlang.org/docs/handbook/variable-declarations.html#destructuring) the `logger` object from the `vtex` context and use its methods (`error`, `warn`, `info`, and `debug`) to provide error, warning, debugging, or informative messages in the log. See the following example:

```ts
const helloWorld = (ctx: Context) => {
  const { vtex: { logger } } = ctx

  logger.warn('Warning the world!')

  logger.error('Error!!!')

  logger.debug('Verbose debug message!')
}
```

> ℹ️ Every exception that happens in a VTEX IO service app is intercepted and automatically logged with a `logger.error` implementation.

### Retrieving app logs

Every log written by a running app with the VTEX IO Logging Service is collected and stored for later retrieval.

You can retrieve the logs using the [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-installation-and-command-reference) by following the steps:

1. Log in to your VTEX account.
2. Install the Logs plugin for the VTEX IO CLI by running the following command:

```sh
vtex plugins add logs
```

3. Check if the installation of the Logs plugin was successful by running `vtex logs --help`.
4. Retrieve logs from all apps installed in your account by running the following command:

```sh
vtex logs --all
```

The output should be a message similar to the following:

```sh
vtex logs --all
18:15:26.779 - info: Connecting to logs stream for store components
18:15:26.782 - info: Press CTRL+C to abort

18:15:43.856 - info: Listening to store components logs

  info: { status: 403,
  code: 'FORBIDDEN',
  name: 'ForbiddenError',
  level: 'error',
  message: 'This username is already registered with another email',
  stack:
   'ForbiddenError: This username is already registered with another email[ErrorStack...]
  routeId: 'login' }
```

> ℹ️ You can also retrieve logs from a specific app installed in your account by running the following command: `vtex logs {serviceAppExample}`. Replace `serviceAppExample` with the desired app name.

We suggest running `vtex logs --all > {mylogfile.logs}` to save the log messages in a local file. Replace `{mylogfile.logs}` with a name that fits your environment.

If you want to see log messages that you have previously retrieved, run `vtex logs --past`.

## Log storage and retention limits

VTEX limits the storage size and retention period of logs to guarantee the stability and performance of the platform. The limits are:

- Logs are stored for 7 days at most.
- Each app can have up to 1 GB of logs stored per account. If an app generates more than 1 GB of logs in one account in 7 days or less, the oldest logs are deleted.

If you need more than 1 GB of logs per week for an app, we recommend retrieving and storing your logs before they reach the storage limit. You can check the size of the logs from the size of the retrieved files in your local environment. See the instructions in the [Retrieving app logs](#retrieving-app-logs) section.

>⚠️ VTEX may change the storage limits of app logs without additional notice. Check this documentation for the updated limit values.
