---
title: "FastStore Release Notes — Version 4.10.2"
slug: "2026-11-03-faststore-release-notes-4-10-2"
type: improved
excerpt: "FastStore 4.10.2 improves B2B contract assortment, product access, contract switching, and session handling, and reduces CMS calls during page generation."
createdAt: "2026-11-03T00:00:00.000Z"
updatedAt: "2026-11-03T00:00:00.000Z"
hidden: true
tags:
  - FastStore
---

FastStore `v4.10.2` is a patch release with improvements for B2B Buyer Portal stores and CMS performance. B2B buyers see products allowed by their contract on product listing and product pages, and keep their selected contract after switching contracts or refreshing a token. The release also improves B2B buyer identification and reduces the number of repeated CMS calls during page generation. See the fixes below.

> ⚠️ Follow the instructions in [Updating the CLI package version](https://developers.vtex.com/docs/guides/faststore/developer-tools-updating-the-cli-package-version) to upgrade to `v4.10.2` and keep your store up-to-date with the following improvements.

## Bug fixes

### Preview hosts no longer log out pasted sessions (PR: [#3533](https://github.com/vtex/faststore/pull/3533))

With `experimental.refreshToken` on, pasting a `VtexIdclientAutCookie_<account>` into a WebOps preview made the first `ValidateSession` fail, the refresh call answered 405 because previews do not proxy VTEX ID, and `/api/fs/logout` deleted the pasted cookie. The refresh-token bypass that already existed for `localhost` now also covers hosts ending in `.preview.vtex.app` on both the browser and the server (via the `Host` and `x-forwarded-host` headers). `{account}.vtex.app` does not match, so the refresh flow continues.

Developers and QA teams can test logged-in areas in a WebOps preview by pasting the cookie, without editing IndexedDB or blocking `/api/fs/logout`. Production stores are unchanged.

---

## B2B Buyer Portal (Closed beta)

### B2B product listing pages respect the contract assortment (PR: [#3516](https://github.com/vtex/faststore/pull/3516))

The first page of a product listing page (PLP) is generated at build time without buyer context, and the client reused that page whenever the query variables matched. Because the contract assortment (`productClusterIds`) is stored only in the `vtex_segment` cookie, a B2B buyer never reloads the first page. FastStore now adds a cache-only `_contract` key to the variables used for that comparison, so a B2B session always refetches page 1 with the buyer's cookie. The key is not part of any GraphQL operation, and the cache key for anonymous and B2C sessions is unchanged.

B2B buyers whose contract restricts the assortment to a collection see a grid that matches the result counter rather than products outside the contract. The statically generated HTML is still built without buyer context, so buyers may briefly see the unfiltered grid until the session resolves. No action is required beyond upgrading.

### B2B product pages return a 404 for products outside the contract (PR: [#3517](https://github.com/vtex/faststore/pull/3517))

The Intelligent Search `products` request used by the product detail page (PDP) never carried the contract `productClusterIds`, so a product outside the contract could still be opened with its price and **Add to cart** button. `Query.product` in `@faststore/api` now reads the allowed and excluded collections from the `vtex_segment` cookie and returns a `NotFoundError` when the product is not in the assortment. In `@faststore/core`, the new `useProductNotFoundRedirect` hook sends the shopper to the store's `/404` page when the client refetch returns a `404`, and the PDP keeps its loading state until the redirect happens. Intelligent Search failures such as timeouts or 5xx errors no longer look like a missing SKU, so they no longer trigger the redirect.

Products outside a B2B contract are no longer reachable from their PDP. The redirect applies to every shopper whose `vtex_segment` excludes the product, and `useProductQuery` now settles with an `error` when the refetch fails, which customizations should account for. For regionalized stores with `hideUnavailableItems`, a product without stock in the shopper's region now returns `/404`, matching the listings. The redirect does not run when `experimental.enableClientOffer` is on. The product name and images can show briefly before the redirect, and the static HTML still contains the product.

### B2B contract is kept across contract switch and token refresh (PR: [#3525](https://github.com/vtex/faststore/pull/3525))

After a switch through `/api/fs/switch-contract`, the browser held two `VtexIdclientAutCookie_<account>` cookies with different contracts: VTEX ID's cookie with a `Domain`, and a host-only copy written by the switch. Core, `@faststore/api`, and checkout each picked a different one, which could leave the `orderForm` with an empty `clientProfileData`. The auth cookies are now written with the same scope VTEX ID uses (`Domain=<request host>; Path=/; HttpOnly; Secure; SameSite=None`), so they replace the existing cookie, and leftover host-only and parent-domain copies are expired. When checkout runs on a sibling host defined by `secureSubdomain`, the token is also written on their shared parent domain. WebOps previews, local hosts, and IP hosts keep a single host-only cookie, and `/api/fs/logout` expires the auth cookies on the shared parent.

B2B sessions now refresh the token via `POST /api/authenticator/v1/refreshtoken/webstore`, which preserves the contract claims (`customerId`, `unitId`), rather than the legacy `/api/vtexid/refreshtoken/webstore` route. Other sessions continue to use the legacy route. `/api/fs/switch-contract` also relays the `vid_rt` cookie, and `/api/fs/logout` expires it on every path where it can be scoped. B2B buyers keep the selected contract in checkout and after each refresh, and no longer need to log in again to recover it. No action is required beyond upgrading.

### B2B buyers are identified by organizational unit and contract (PR: [#3559](https://github.com/vtex/faststore/pull/3559))

FastStore used the `isRepresentative` claim in the VTEX ID token to decide whether a shopper is a B2B buyer, but Buyer Portal identifies one by the organizational unit (`unitId`) plus a contract (`customerId`). `buildB2bSession` now returns `b2b` only when both exist, `validateSession` and `accountProfile` follow the same rule, and `getIsRepresentative` in `@faststore/core` becomes `getIsB2BBuyer`. The `isRepresentative` claim is no longer read, and the `isRepresentative` props in the account and navigation components are renamed to `isB2BBuyer`.

B2B buyers who have a unit and a contract but no `isRepresentative` flag now get PLP refetch, contract switching, token refresh, and the Quotes and Cards pages in My Account. This is not a breaking change: `StoreB2B.isRepresentative` (GraphQL) and `B2bInfo.isRepresentative` (`@faststore/sdk`) are deprecated and still return `true` whenever `b2b` is set, so check that `b2b` is not `null` instead. `OrganizationSignInButton_unstable` accepts the new `isB2BBuyer` prop and keeps `isRepresentative` as a deprecated alias. The deprecated fields will be removed in the next major version.

---

## Performance

### Fewer CMS calls during page generation (PR: [#3539](https://github.com/vtex/faststore/pull/3539))

FastStore now caches the global section lookups and single-content reads across page generations on CMS and Headless CMS (legacy) stores, with in-flight deduplication and a five-minute TTL per process. The new `createPromiseCache` helper does not cache failures, and fetches by hCMS `documentId`, `versionId`, or `releaseId` are cached only when the caller opts in. Previews and filtered listings, such as a landing page by slug, are not cached.

Build and cold page generation make far fewer CMS requests, reducing 502 and 504 bursts after a build on stores with many pages. A CMS publish still triggers a new build. Under `next dev`, each page has its own cache, so the effect appears under `next start` and in production. No action is required beyond upgrading.
