---
title: "Engineering best practices"
slug: "vtex-io-documentation-engineering-guidelines"
hidden: false
createdAt: "2021-07-22T14:20:04.345Z"
updatedAt: "2022-12-13T20:17:44.370Z"
---
Refer to the following guidelines to guarantee the quality and usability of your VTEX IO app during development.

>⚠️ Notice that you must respect these guidelines if you aim to publish your app at the VTEX App Store.

## Scalability and performance

Use the [VTEX IO](https://developers.vtex.com/docs/guides/vtex-io-documentation-what-is-vtex-io) infrastructure to build and deploy your extensions. The VTEX IO development platform uses cloud computing to ensure that your app runs without bottlenecks 24/7.

### Using APIs efficiently

Efficiently utilizing APIs is paramount for optimal performance in your application. Whenever possible, leverage our pre-built [VTEX IO Clients](https://github.com/vtex/io-clients) to harness the following advantages:

- **Standardized code:**  VTEX IO Clients streamline interfacing with various services, providing standardized code across all applications.
- **Automatic updates:** VTEX consistently updates VTEX IO Clients, delivering new features, resolving bugs, and ensuring compatibility with the latest technologies.
- **Simplified maintenance:** By relying on VTEX IO Clients, you eliminate the need for extensive code maintenance.

Avoid unnecessary or excessive API calls and ensure they are fast and scalable. Excessive API calls can degrade your app's performance, increasing response times. Unnecessary API calls or lack of proper use of our Clients can lead to security issues. For more information, see our [Clients](https://developers.vtex.com/docs/guides/vtex-io-documentation-how-to-create-and-use-clients) documentation.

>ℹ️ **Performance of external systems**
>
>When you offer your app on the VTEX App Store, your app may become available to brands of all sizes across different time zones and business calendars. In this context, relying on a manual system with on-demand scalability can become a huge risk in terms of performance.

### Using the latest builders

[Builders](https://developers.vtex.com/docs/guides/vtex-io-documentation-builders) work as an API responsible for configuring other IO services in your app.
For developing and publishing apps for the VTEX App Store, the following builders must be up-to-date in your app's code:

- Node builder - version 7.x.
- React builder - version 3.x.
- Admin builder - version 1.x.
- Messages builder - version 1.x.
- Docs builder- version 0.x.
- Graphql builder -version 1.x.

## Versioning

When releasing a new version of your app, it's crucial to adhere to best practices. There are various types of versions to consider, including major, minor, and patch, as well as stable and beta releases. Select the appropriate version type based on the nature of the implemented changes. Special attention is required for breaking changes, which should always result in a new major version.

For more information, refer to the [SemVer standard](https://semver.org/) and our guide on [Releasing a new app version](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version).

## Security

To ensure that all points of contact between our retailers, their customers, and other parts of the ecosystem are protected and secure, we test if your app respects regulations on data traffic, usage, and storage worldwide.

### Handling security breaches

Nevertheless, if you identify any security breaches after publishing your app, take the following measures:

1. [Open a ticket](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) requesting to remove your app from the VTEX App Store and avoid further installations of the unstable version.
2. [Open a support ticket](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM) and notify us of the issue so that we can support retailers operating with this version and guide them on removing it from their stores.
3. Fix the security flaw and resubmit your application for homologation.

Once the new version is approved, the app will be available again in the VTEX App Store.

### Hardcoding VTEX appKey/appToken

Having an appKey/appToken exposed in your code can cause serious security issues, like unwanted access. Instead of using a VTEX appKey/appToken pair, apps should use the existing tokens (`ctx.authToken`,  `ctx.vtex.storeUserAuthToken` or `ctx.vtex.adminUserAuthToken`). For more information, see [Connecting to VTEX Core Commerce APIs](https://developers.vtex.com/docs/guides/how-to-connect-with-vtex-core-commerce-apis-using-vtex-io#steps).

### Using an app token for a user-initiated action

For user-initiated actions, apps should use either `ctx.vtex.storeUserAuthToken` or `ctx.vtex.adminUserAuthToken` (as opposed to `ctx.authToken`). For more information, see [Connecting to VTEX Core Commerce APIs](https://developers.vtex.com/vtex-developer-docs/docs/how-to-connect-with-vtex-core-commerce-apis-using-vtex-io#steps).

### Declaring broad policies

Outbound access policies (`outbound-access`) to VTEX resources should follow the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege). In short, you only give access to what is really needed. For instance, the `path` should not be configured as `*`. See an example [here](https://github.com/vtex-apps/store-graphql/blob/684dcbbbd6e9cdbd121afd7802200856cb952d2b/manifest.json#L107-L112) of how it should be done.

### Do not expose private information through public routes

As the name suggests, public routes do not require authentication when accessed from the frontend. Consequently, they should never reveal data sourced from private APIs, such as displaying a list of orders directly to the frontend. In this sense, a common mistake is failing to restrict routes intended exclusively for Admin usage. Additionally, keep in mind that GraphQL APIs are public by default, necessitating cautious schema design to avoid queries that inadvertently expose confidential information.

Access to REST APIs should be restricted using [policies](https://developers.vtex.com/docs/guides/vtex-io-documentation-policies#resource-based-policies). Access to GraphQL APIs should be restricted using directives, either [@auth](https://github.com/vtex/node-vtex-api/blob/08ea11d380997f5abf02455487b342caa74b2001/src/service/worker/runtime/graphql/schema/schemaDirectives/Auth.ts#L66-L75) or a custom-made one.

### Isolate data between tenants

Single-tenant external systems should be used carefully. Data from one tenant must always be isolated from data from another tenant to prevent leakage and unwanted access. The isolation method will depend on the external system. One possible solution is to use the name (or other identifier) of the tenant in routes or as a parameter for access control or to define how the data is managed.

## Data privacy

### Persisting PII within VTEX

If using Master Data or VBase to store Personal Identifiable Information (PII), a mechanism must be in place to ensure compliance with the [Right to be Forgotten](https://en.wikipedia.org/wiki/Right_to_be_forgotten) or other similar data-protection practices. Possible solutions are to provide an option or endpoint in the app that erases the data, for instance, by using a delete operation with our Clients ([Master Data](https://developers.vtex.com/docs/guides/create-master-data-crud-app#delete), [VBase](https://github.com/vtex/node-vtex-api/blob/1b3c54976aa974619d0728fae4ed2fe076dbb551/src/clients/infra/VBase.ts#L178)) or through the API ([Master Data v1](https://developers.vtex.com/docs/api-reference/masterdata-api#delete-/api/dataentities/-acronym-/documents/-id-), [Master Data v2](https://developers.vtex.com/docs/api-reference/master-data-api-v2#delete-/api/dataentities/-dataEntityName-/documents/-id-)).

### Sending PII to external service

We should ensure that all PII being shared externally is strictly necessary for the app to work. If you have any questions, reach out to us [via ticket](https://help.vtex.com/en/tutorial/opening-tickets-to-vtex-support--16yOEqpO32UQYygSmMSSAM).

## Usability

### Implementing internationalization (i18n) correctly

Ensure that all messages are [internationalized](https://developers.vtex.com/docs/guides/vtex-io-multi-language-stores#storefront-content-internationalization) using the `messages` builder. Also, i18n keys should start with the domain (`store/` for storefront and `admin/` for Admin) where they are used. Otherwise, they will not render properly. For more information, see our [reference](https://developers.vtex.com/docs/guides/vtex-io-documentation-8-translating-the-component) for translating components.

### Avoid declaring routes with collision-prone paths

When declaring [routes](https://developers.vtex.com/docs/guides/vtex-io-documentation-routes), generic paths (e.g., `/_v/orders/`, `/_v/settings`) should be avoided to reduce chances of collision with other apps.

To mitigate this risk, consider adopting a naming convention that includes a distinctive prefix, typically the name of your app, when defining routes. This simple practice effectively reduces the chances of conflicts and ensures that your app's routes remain uniquely identifiable and isolated from others.

### Creating custom Admin settings form

Our primary recommendation for defining the Admin settings form of your app is to leverage the [`settingsSchema`](https://developers.vtex.com/docs/guides/vtex-io-documentation-manifest#settingsschema) structure, as it caters to the majority of use cases effectively.

However, for more specific cases where the schema is insufficient, you can create your form as a page of an [Admin app](https://learn.vtex.com/docs/course-admin-lang-en). In such cases, our team will evaluate your requirements during the homologation process.

## Plug&Play

For homologation approval, your app must be plug-and-play. Those interested in your app should:

- Be able to install and configure it using only the VTEX Admin panel.
- Not considered external assistance to support the app implementation process.

## Support channel

Every app in the VTEX App Store must:

- Provide a direct support channel for retailers who install it, such as email, phone, ticketing tool, or a combination of these options.
- Have the first response time up to eight business hours in the developer's time zone. This requirement aims to ensure that store operations will not be affected by errors in third-party applications.

## Documentation

While [developing your app](https://developers.vtex.com/docs/guides/vtex-io-documentation-developing-an-app) and [preparing the app for distribution](https://developers.vtex.com/docs/guides/vtex-io-documentation-preparing-your-app-distribution), make sure to provide official documentation that supports future users in implementing and understanding your app.

The app documentation should include:

- Technical and commercial requirements for the app's operation.
- Installation and configuration guides.
- Answers to frequently asked questions.

For more information on the best practices for creating documentation, refer to [Documentation guidelines](https://developers.vtex.com/docs/guides/vtex-io-documentation-docs-guidelines).
