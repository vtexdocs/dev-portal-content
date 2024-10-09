---
title: "Node builder update to version 7.x and deprecation of previous builder versions"
slug: "2024-10-10-node-builder-update-to-version-7x-and-deprecation-of-previous-builder-versions"
type: "improved"
createdAt: "2024-10-10T10:00:00.000Z"
updatedAt: "2024-10-10T10:00:00.000Z"
hidden: false
excerpt: "Upgrade VTEX IO apps to the latest Node builder version for improved performance and security. Previous builder versions will be discontinued."
---

We are excited to announce the release of [Node builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-node-builder) version `7.x` for VTEX IO apps, effective October 10, 2024. This update is available for everyone using VTEX IO, and developers are encouraged to use it for both new and existing apps. Please be aware that versions 6.x and earlier will be deprecated.

## Deprecation schedule of legacy versions

The previous builder versions, `6.x` and below, will be deprecated as follows:

- **Node builder `4.x` deprecation date:** March, 2025
- **Node builder `6.x` deprecation date:** June, 2025

⚠️ We strongly recommend upgrading your node app to the latest Node builder before the deprecation of legacy Node builder versions. After deprecation, apps using a legacy builder version will continue to function, but it won't be possible to install, release, or publish new versions of the app. See the [What needs to be done? section](#what-needs-to-be-done) for details.

## Why did we make this change?

The Node builder `7.x` update comes with new Node.js engine and TypeScript versions. With the new builder, IO apps take advantage of improved performance and security, along with new features. For details about these changes, see the [Node.js](https://nodejs.org/en/about/previous-releases) and [TypeScript](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-5.html) documentation.

### Version compatibility

The table below maps each Node builder version with the corresponding Node.js engine, [`@types/node` package](https://www.npmjs.com/package/@types/node) (TypeScript definitions for Node), and TypeScript versions.

|Builder version|Node.js|@types/node|TypeScript|
|-|-|-|-|
|4.x|[12.x](https://nodejs.org/en/blog/release/v12.0.0)|-|[3.9.7](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html)|
|6.x|[16.x](https://nodejs.org/en/blog/release/v16.0.0)|[12.0.0](https://www.npmjs.com/package/@types/node/v/12.0.0)|[3.9.7](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html)|
|7.x|[20.x](https://nodejs.org/en/blog/release/v20.0.0)|[20.0.0](https://www.npmjs.com/package/@types/node/v/20.0.0)|[5.5.3](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-5.html)|

## What needs to be done?

Required actions will vary based on the app’s vendor and status:

<table>
  <tr>
    <td><b>App status</b></td>
    <td><b>Required actions</b></td>
  </tr>
  <tr>
    <td><a href="#native-vtex-apps-in-production">Native VTEX apps in production</a></td>
    <td>No action is required. <br><br>VTEX will gradually update supported apps to the latest builder version.</td>
  </tr>
  <tr>
    <td><a href="#native-vtex-apps-in-production">Deprecated VTEX apps</a></td>
    <td>Consider finding alternative solutions to prevent future issues. <br><br>Deprecated VTEX apps do not receive updates, and using them may lead to conflicts if they are included as dependencies in other applications. Assess your app’s dependencies and explore current options to mitigate risks and enhance stability.</td>
  </tr>
  <tr>
    <td><a href="#new-apps-and-apps-in-development">New apps and apps in Development</a></td>
    <td>Use the updated boilerplates and the Node builder version <code>7.x</code> for new app development.</td>
  </tr>
  <tr>
    <td><a href="#proprietary-apps-in-production">Proprietary apps in production</a></td>
    <td>
      <ul>
        <li>Upgrade your app to Node builder <code>7.x</code> before the deprecation date of the current builder version.</li>
      </ul>
      <ul>
        <li>If keeping the current version, note that it will function normally until its deprecation date. However, you will not be able to create, install, or publish new versions after that date.</li>
      </ul>
    </td>
  </tr>
</table>

### Native VTEX apps in production

VTEX will gradually update supported apps to the latest builder version before the deprecation date. You can continue using these apps as usual.

Deprecated VTEX apps will remain available for installation and use, regardless of their builder version. However, these apps will not receive updates and may cause conflicts if used as dependencies in other Node apps.

### New apps and apps in development

If you are developing a new app or working on an app in development, we recommend using the updated boilerplates and the new [Node builder](https://developers.vtex.com/docs/guides/vtex-io-documentation-node-builder) version.

### Proprietary apps in production

If you have already published and deployed your app, we recommend releasing a new version of your app using the latest Node builder before the deprecation date of the current builder version.

If you choose to keep the current Node builder version, your app will work as usual until the legacy Node builder is deprecated. After this date, your app will still run on our platform, but you will not be able to link, install, and create new versions of the app with this builder version.

To update your app with Node builder `7.x`, follow the instructions in the [Node 7.x builder migration guide](https://developers.vtex.com/docs/guides/node-builder-7x-migration-guide).

⚠️ After making the changes, please test your app thoroughly to identify any potential issues, especially regarding dependencies and compatibility.

### Support

If you need help with any case related to the builder update, see the [troubleshooting section of our migration guide](https://developers.vtex.com/docs/guides/node-builder-7x-migration-guide#troubleshooting) or open a ticket with [VTEX support](https://help.vtex.com/en/support).
