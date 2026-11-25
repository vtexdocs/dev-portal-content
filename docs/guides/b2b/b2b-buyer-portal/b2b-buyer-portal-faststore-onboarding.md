---
title: "Onboarding FastStore for B2B Buyer Portal"
slug: "b2b-buyer-portal-faststore-onboarding"
hidden: false
createdAt: "2026-11-23T00:00:00.000Z"
updatedAt: "2026-11-23T00:00:00.000Z"
excerpt: "Learn how to set up a FastStore store for B2B Buyer Portal, from WebOps and domains to the shopper entity, plugin, and optional internationalization."
---

> ⚠️ This guide applies only to stores using [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal), which is currently available to selected accounts.

This guide walks you through the process of setting up a **[FastStore](https://developers.vtex.com/docs/guides/faststore/docs-what-is-faststore)** store that runs **B2B Buyer Portal**. Each step builds on the previous one, so complete the required steps in the order presented.

The setup involves the following components:

- **WebOps**: deploys the **FastStore** store from its GitHub repository and starts a new deployment with every push.
- **FastCheckout**: the checkout used with **B2B Buyer Portal** on **FastStore**.
- The **B2B Buyer Portal** plugin (`@vtex/faststore-plugin-buyer-portal`): adds the **Organization Account** pages to the store.

These are the implementation steps that are detailed below:

| Step                                                                                                                | What you do                                                                         | Who does it                              | Required |
| :------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------- | :--------------------------------------- | :------- |
| [1. Set up the FastStore store](#step-1---set-up-the-faststore-store)                                               | Create the **WebOps** project, connect GitHub, and configure `discovery.config.js`. | You                                      | Yes      |
| [2. Configure domains](#step-2---configure-domains)                                                                 | Move the store to your final domain.                                                | You, with VTEX Support for some requests | Yes      |
| [3. Configure FastCheckout](#step-3---configure-fastcheckout)                                                       | Request the **FastCheckout** enablement.                                            | You, with VTEX Support                   | Yes      |
| [4. Configure the shopper entity, plugin, and `nohoist`](#step-4---configure-the-shopper-entity-plugin-and-nohoist) | Install the plugin and give the store access to shopper data.                       | You                                      | Yes      |
| [5. Request the customer experience configuration](#step-5---request-the-customer-experience-configuration)         | Ask VTEX to configure the checkout experience for B2B.                              | VTEX, at your request                    | Yes      |
| [6. Request the FastCheckout UI configuration](#step-6---request-the-fastcheckout-ui-configuration)                 | Ask VTEX to apply your logo and primary color to **FastCheckout**.                  | VTEX, at your request                    | Yes      |
| [7. Configure internationalization (optional)](#step-7---configure-internationalization-optional)                   | Offer more than one language, region, or currency.                                  | You, with VTEX Support                   | No       |

## Before you begin

Before you start, make sure that you meet the following prerequisites:

- You have the **Owner (Admin Super)** role on the account in the VTEX Admin.
- The account has a catalog with products. Without a catalog, you can't test listing, search, and checkout.
- You have a GitHub account or organization with administrator access.

## Instructions

### Step 1 - Set up the FastStore store

In this step, you create the **FastStore** project in **WebOps** and configure the values that **B2B Buyer Portal** requires. By the end, the store runs on the provisional `{accountName}.vtex.app` domain and is ready for the plugin.

#### Create the project and connect GitHub

Follow the instructions in [Starting the project](https://developers.vtex.com/docs/guides/faststore/getting-started-2-starting-the-project) to create the project. Keep the following in mind:

- Open **Storefront** > **FastStore WebOps** in the VTEX Admin and click `Start Project`.
- Create the store with the standard **FastStore** starter.
- When you click `Connect with GitHub`, choose your own GitHub organization. Don't choose the `vtex` organization. You choose the organization once during onboarding, and you can't change it afterward. If you create the project in the wrong organization, see [Moving your FastStore project to a new GitHub repository](https://developers.vtex.com/docs/guides/faststore/webops-moving-your-faststore-project-to-a-new-github-repository).
- If you select `Only select repositories` under **Repository access**, include the repository that will receive the store. Otherwise, **WebOps** doesn't receive push events and deploys don't run.
- **WebOps** support for GitHub Enterprise organizations with a custom domain is in open beta. Ask [VTEX Support](https://help.vtex.com/en/support) to enable it before you start.

The first deploy is complete when all of the following are true:

- The **Deploy Summary** screen shows the repository and the dashboard link.
- The **WebOps** dashboard shows at least one successful deploy. For more information, see [FastStore WebOps - Dashboard](https://developers.vtex.com/docs/guides/faststore/webops-dashboard).
- The store is accessible over HTTPS at `https://{accountName}.vtex.app/`.

#### Configure `discovery.config.js`

Clone the repository and open `discovery.config.js` at the project root. In a monorepo, the file is in `packages/discovery/`. Set the store values and the `experimental` options as follows:

```js discovery.config.js
module.exports = {
  // ...

  api: {
    storeId: "{accountName}",
    workspace: "master",
    environment: "vtexcommercestable",
  },

  storeUrl: "https://{accountName}.vtex.app",
  secureSubdomain: "https://{accountName}.vtex.app",
  checkoutUrl: "https://{accountName}.vtex.app/checkout",
  loginUrl: "https://{accountName}.vtex.app/api/io/login",
  accountUrl: "https://{accountName}.vtex.app/api/io/account",

  // ...

  experimental: {
    enableFaststoreMyAccount: true,
    refreshToken: true,
  },
};
```

Replace `{accountName}` with your [VTEX account name](https://help.vtex.com/docs/tutorials/what-is-an-account-name) and leave the other properties as the starter generated them.

| Property | What it does |
| :---- | :---- |
| `api.storeId` | VTEX account name of the store. If it's wrong, the store can't find catalog, price, or session data. |
| `storeUrl`, `checkoutUrl`, `loginUrl`, `accountUrl` | Addresses of the storefront, checkout, login, and customer account. For now, use the provisional domain. You replace them with the final domain in [step 2](#step-2---configure-domains). |
| `secureSubdomain` | Same domain as the store. Don't use a separate `secure` host. |
| `experimental.enableFaststoreMyAccount` | Turns on **My Account**, the customer account pages under `/pvt/account` that **B2B Buyer Portal** requires. |
| `experimental.refreshToken` | Renews the shopper session automatically. |

> ⚠️ `enableFaststoreMyAccount` is an experimental feature available only for B2B stores and selected accounts. It must be set inside the `experimental` object. At the root of the file, it has no effect. With the setting enabled, users who access `/pvt/account` are redirected to `/pvt/account/profile`, and the setting overrides `accountUrl`. For the full procedure, see [Enabling My Account for B2B stores](https://developers.vtex.com/docs/guides/faststore/my-account-enablement).

With `refreshToken` enabled, the **FastStore** SDK renews the session without further code. For details, see [Enabling refresh token on FastStore](https://developers.vtex.com/docs/guides/faststore/session-enabling-refresh-token).

Commit and push the change to the `main` branch. **WebOps** starts a new deployment with every push.

#### Verify the setup

1. In the **WebOps** dashboard, confirm that the deploy for your last commit succeeded.
2. Confirm that the store is accessible over HTTPS.
3. Sign in and go to `/pvt/account`. The page must redirect to `/pvt/account/profile`. If it redirects elsewhere, `enableFaststoreMyAccount` isn't active in the deployed version.

#### Troubleshooting

- **The deploy doesn't start after a push.** **WebOps** runs only when it receives the GitHub push event. In GitHub, open the **FastStore WebOps** app, click `Configure`, choose the organization, and confirm that the store repository is listed under **Repository access**.
- **You can't complete the WebOps onboarding.** If you already installed the app in the organization, open a ticket with [VTEX Support](https://help.vtex.com/en/support) and include the account name, the repository link, the app `installationId`, and the repository ID.
- **The `Start Project` button doesn't work.** Confirm that you have the **Owner (Admin Super)** role on the account and administrator access in the GitHub organization.
- **WebOps is installed in an environment other than `master`.** **WebOps** works only in production. Install the app in the `master` environment of the account.

### Step 2 - Configure domains

In this step, you move the store from the provisional domain to your final domain. By the end, the store is accessible over HTTPS on the final domain, with login and checkout on the same domain.

#### Use a single domain

The store must use one domain for the storefront, login, customer account, and checkout. A separate `secure` host is no longer needed. For more information, see [FastStore: Simplified domain configuration](https://developers.vtex.com/updates/release-notes/2025-11-14-faststore-single-domain-configuration).

**FastCheckout** identifies the buyer through the `vtex_session` and `vtex_segment` cookies, which are set on the storefront domain. If checkout runs on another domain or subdomain, the cookies don't reach it. Checkout doesn't show an error. It treats the shopper as a non-B2B buyer, and the buyer's [contract and organizational unit](https://developers.vtex.com/docs/guides/b2b-buyer-portal-integration-overview), along with the contract custom fields, don't appear. Therefore:

- Don't use `secure.{yourdomain}` or any other subdomain for checkout or login.
- Don't leave `secureSubdomain` pointing to another domain in `discovery.config.js`.
- Use the same domain in all production addresses.

#### Move the store to the final domain

Complete the following steps in order:

1. **Point your domain to FastStore.** In your DNS provider, create the `CNAME` record for the `www` host and redirect the root domain to `www`. Follow [Configuring external DNS](https://developers.vtex.com/docs/guides/faststore/go-live-1-configuring-external-dns). DNS propagation can take up to 48 hours.
2. **Activate the account in production.** In the VTEX Admin, click your profile avatar, open **Account Settings** > **Account**, click `Activate in production`, and confirm. VTEX serves the store on a custom domain only after the account is active in production. For more information, see [Account settings](https://help.vtex.com/en/docs/tracks/settings).
3. **Add the domain to the store hosts.** The store hosts are registered in the **License Manager** module. In **Account Settings** > **Account**, open the **Stores** tab. In the **Hosts** table, edit the host list and add both `www.{yourdomain}` and `{yourdomain}`. If a host is missing, checkout doesn't work. For more information, see [Configuring the store domain](https://help.vtex.com/en/docs/tutorials/configuring-the-store-domain).
4. **Update `discovery.config.js`.** Replace the production addresses with the final domain, commit, and deploy to `main`:

   ```js discovery.config.js
   storeUrl: "https://www.{yourdomain}",
   secureSubdomain: "https://www.{yourdomain}",
   checkoutUrl: "https://www.{yourdomain}/checkout",
   loginUrl: "https://www.{yourdomain}/api/io/login",
   accountUrl: "https://www.{yourdomain}/api/io/account",
   ```

   Login and checkout on the provisional `{accountName}.vtex.app` domain may not work after this deployment because these URLs point to the final domain. Continue with the remaining steps to complete the migration.
5. **Add the domain in WebOps.** In **Storefront** > **FastStore WebOps**, open the **Settings** tab, choose the domain in the **Host** field, click `Add`, and confirm it appears under **Current Domains**. Do this before the domain migration, which makes the final domain the main address of the store instead of `{accountName}.vtex.app` and applies the CDN configuration. Otherwise, the migration fails. For more information, see [FastStore WebOps self-service domain setup](https://developers.vtex.com/updates/release-notes/2025-04-08-faststore-webops-self-service-domain-setup-now-available).
6. **Request the domain migration.** Before you request it, return to **Account Settings** > **Account** and click `Save` in the **Hosts** table. Then open a ticket with [VTEX Support](https://help.vtex.com/en/support), include the account name and the final domain, and state that the store uses **FastStore** with **FastCheckout**.
7. **Set the auth cookie root domain.** Follow Step 2 of [Integrating the VTEX Login](https://developers.vtex.com/docs/guides/faststore/go-live-2-integrating-the-vtex-login) to request the auth cookie root domain for your store domain through VTEX Support.

Request the domain migration again in these cases:

- The store previously used a `secure` domain. After you adjust `discovery.config.js`, request the migration again.
- The store starts using multiple languages (see [step 7](#step-7---configure-internationalization-optional)). Without a new migration, language-prefixed routes such as `/pt-BR` can return a `404` error or redirect to the home page.

#### Verify that the store is live

The store is live when all of the following are true:

- `https://www.{yourdomain}` loads with a valid HTTPS certificate and doesn't redirect to `vtex.app`.
- The command `curl -sI https://www.{yourdomain} | head -1` returns `200`.
- The login button leads to a page on `www.{yourdomain}`, and after login the shopper returns to the same domain.
- `https://www.{yourdomain}/checkout` loads on the same domain and shows the contract of the signed-in buyer.
- In **WebOps**, the domain appears under **Current Domains** and the last deploy succeeded.

### Step 3 - Configure FastCheckout

This onboarding requires **FastCheckout**. B2B checkout requires a signed-in buyer, because the checkout needs the buyer's contract and organizational unit. Guest checkout isn't available to B2B buyers.

**FastCheckout** enablement isn't self-service. Request it through [VTEX Support](https://help.vtex.com/en/support) and include the account name, the final store domain, and the store repository. Then complete [step 5](#step-5---request-the-customer-experience-configuration) and [step 6](#step-6---request-the-fastcheckout-ui-configuration). For instructions on setting up the **FastCheckout** project, see [Setting up Buyer Portal Checkout](https://developers.vtex.com/docs/guides/setting-up-buyer-portal-checkout).

### Step 4 - Configure the shopper entity, plugin, and `nohoist`

In this step, you install the plugin and give **FastStore** read access to the shopper entity, which stores shopper data such as names and phone numbers. If your repository is a monorepo, you also use the `nohoist` option to keep the plugin inside the store package. By the end, the plugin is active and the **My Account** pages show data such as the **Ordered by** card.

#### Prerequisites for this step

To proceed with this step, make sure that these requirements are satisfied:

- The store from [step 1](#step-1---set-up-the-faststore-store) is deployed and `enableFaststoreMyAccount` is set to `true` inside the `experimental` object.
- In the VTEX Admin, you have the **User Administrator - RESTRICTED** role, which lets you create roles and API keys.
- You also have a role that includes the **Dynamic Storage** product, which controls access to the shopper entity. You need it to add **Dynamic Storage** to the new role.
- In **WebOps**, you have the **View Secrets** and **Edit Secrets** permissions (**FastStore** product, **Secrets** category).

#### Install the plugin

The plugin package is `@vtex/faststore-plugin-buyer-portal`. Declare it in two places.

1. In `discovery.config.js`, add the package to the `plugins` list:

   ```js discovery.config.js
   module.exports = {
     // ...
     platform: "vtex",
     plugins: [
       "@vtex/faststore-plugin-buyer-portal",
     ],
     // ...
   };
   ```

2. In `package.json`, add the package to `dependencies`. In a monorepo, use `packages/discovery/package.json`.

   ```json package.json
   {
     "dependencies": {
       "@vtex/faststore-plugin-buyer-portal": "{version}"
     }
   }
   ```

3. Install the dependencies with `yarn install`.

#### Declare `nohoist` (monorepos only)

Complete this step only if the same repository contains **FastStore** and **FastCheckout**, each in its own package, for example:

```text
packages/
  discovery/   (the FastStore store)
  checkout/    (the FastCheckout project)
```

If your project has a single package, skip this step.

The **FastStore** CLI looks for plugins only in the `node_modules` folder of the `discovery` package. In a monorepo, the package manager often moves dependencies to the root `node_modules`, where the CLI can't find the plugin. The `nohoist` option keeps the plugin inside `packages/discovery/node_modules`.

1. In the root `package.json`, declare `nohoist`. For the base `workspaces` setup, see [Setting up Buyer Portal Checkout](https://developers.vtex.com/docs/guides/setting-up-buyer-portal-checkout).

   ```json package.json
   "workspaces": {
     "packages": [
       "packages/*"
     ],
     "nohoist": [
       "**/@vtex/faststore-plugin-buyer-portal",
       "**/@vtex/faststore-plugin-buyer-portal/**"
     ]
   }
   ```

2. In `packages/discovery/package.json`, declare the plugin as a dependency of the package, as in [Install the plugin](#install-the-plugin).
3. Run `yarn install` and deploy.

If you forget `nohoist`, the local build passes but the **WebOps** deploy fails, and the build log shows `Cannot find module` with few details.

#### Verify the plugin

To confirm that the plugin loaded, complete the following checks:

1. Check that the package exists in `node_modules/@vtex/faststore-plugin-buyer-portal`. In a monorepo, check `packages/discovery/node_modules/@vtex/faststore-plugin-buyer-portal`.
2. Run `yarn dev` and confirm the project starts without plugin or module errors.
3. Sign in with a user that belongs to an organizational unit and go to `/pvt/organization-account`. If the page loads, the plugin is active. A `404` error means the plugin didn't load.
4. After deploying, confirm that the **WebOps** build succeeds.

#### Configure shopper entity credentials

**FastStore** reads the shopper entity to display who placed an order, who created each quote, and the name and phone of the signed-in user. For that, the project needs an API key with read permission on **Dynamic Storage**. Without it, those queries fail with `No authentication AppKey and AppToken passed.`

Follow [Configuring Shopper entity access](https://developers.vtex.com/docs/guides/faststore/my-account-configuring-shopper-entity-access) to create the role, generate the API key, and add the credentials. To store them in **WebOps**, see [Managing variables and secrets](https://developers.vtex.com/docs/guides/faststore/webops-managing-variables-and-secrets). Add them as the following secrets and redeploy:

| Type | Key | Value |
| :---- | :---- | :---- |
| `secret` | `FS_DISCOVERY_APP_KEY` | The generated App Key |
| `secret` | `FS_DISCOVERY_APP_TOKEN` | The generated App Token |

> ⚠️ Never commit the App Key or App Token to the repository. Keep them only in **WebOps** secrets and, for local tests, in terminal variables or an untracked `vtex.env` file listed in `.gitignore`.

These key names are fixed in **FastStore**, so a store has only one key pair. If you also configure [internationalization](#step-7---configure-internationalization-optional), use a single API key for both and give its role the permissions that both guides require.

To validate the key before go-live, run the same query that **FastStore** makes, with the credentials exported in your terminal:

```bash
curl -s -o /dev/null -w "%{http_code}\n" \
  -H "X-VTEX-API-AppKey: $FS_DISCOVERY_APP_KEY" \
  -H "X-VTEX-API-AppToken: $FS_DISCOVERY_APP_TOKEN" \
  -H "Accept: application/json" \
  "https://{accountName}.vtexcommercestable.com.br/api/dataentities/shopper/search?_fields=id&_schema=v1"
```

A `200` response means the key works. A `401` or `403` response means the key lacks permission, so check that its role has **Read only documents** on **Dynamic Storage**.

Then run `yarn dev` in the same terminal, sign in with a user that belongs to an organizational unit, view an order detail in **My Account**, and confirm that the **Ordered by** card shows who placed the order. Repeat the test on the published store after the redeploy.

### Step 5 - Request the customer experience configuration

VTEX configures the checkout experience settings that **B2B Buyer Portal** needs on your account. This configuration isn't self-service.

1. Open a ticket with [VTEX Support](https://help.vtex.com/en/support).
2. State that the request is the customer experience configuration for **B2B Buyer Portal** checkout on a **FastStore** store with **FastCheckout**.
3. Provide the account name and whether your project uses **Quotes**.
4. Wait for VTEX to confirm that the configuration is active before you continue.

The configuration enables the B2B checkout behavior: required sign-in (see [step 3](#step-3---configure-fastcheckout)), custom fields, multiple deliveries, and, when your project needs it, **Quotes**.

### Step 6 - Request the FastCheckout UI configuration

VTEX applies the **FastCheckout** UI configuration for your account. This is a required step, and it isn't self-service. Without it, **FastCheckout** can show an error screen instead of the cart. Request it through support after the customer experience configuration from [step 5](#step-5---request-the-customer-experience-configuration) is active.

1. Prepare the following inputs:
   - Your logo as a PNG file published at a public URL on `vtexassets.com`.
   - The primary color as a hexadecimal code that contrasts with a white background. `#fff` doesn't work, because the **FastCheckout** background is already white.
2. Open a ticket with [VTEX Support](https://help.vtex.com/en/support).
3. State that the request is the **FastCheckout** UI configuration for your account and provide the account name, the logo URL, and the primary color.
4. Wait for VTEX to confirm that the configuration is applied.

### Step 7 - Configure internationalization (optional)

Complete this step only if your project needs more than one language, region, or currency.

> ⚠️ The **Localization** feature is in Closed Beta. To use it in your store, contact [VTEX Support](https://help.vtex.com/en/support).

Before you start, make sure that:

- The **CMS** is installed and enabled in the account. **Headless CMS (legacy)** doesn't support this feature.
- The store uses the **Catalog Multi-Language API**.
- The project is upgraded to **FastStore** v4.

The procedure is the same as in [Handling internationalization with the Localization feature](https://developers.vtex.com/docs/guides/faststore/localization-feature-handling-internationalization-with-the-localization-feature). Keep the following **B2B Buyer Portal** points in mind:

- The feature uses the same `FS_DISCOVERY_APP_KEY` and `FS_DISCOVERY_APP_TOKEN` secrets that you created in [step 4](#step-4---configure-the-shopper-entity-plugin-and-nohoist). Don't create a second key pair. Make sure the role of that key includes the permissions of both features.
- [Bindings](https://help.vtex.com/en/docs/tutorials/what-is-binding), which associate each domain with a locale and currency, are requested through VTEX Support. In the ticket, include the account name, the URL of each domain, the sales channel and currency of each domain, and the locale of each domain.
- After the store starts using multiple languages, request the domain migration again, as described in [step 2](#step-2---configure-domains).

## Next steps

- [B2B Buyer Portal integration overview](https://developers.vtex.com/docs/guides/b2b-buyer-portal-integration-overview)
- [B2B user provisioning](https://developers.vtex.com/docs/guides/b2b-user-provisioning)
- [Setting up Buyer Portal Checkout](https://developers.vtex.com/docs/guides/setting-up-buyer-portal-checkout)
- [Buyer Portal Checkout](https://help.vtex.com/en/docs/tutorials/buyer-portal-checkout)
- [B2B Buyer Portal](https://help.vtex.com/en/docs/tutorials/b2b-buyer-portal)
