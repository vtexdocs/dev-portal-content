---
title: 'Issues when using FastStore hooks'
slug: "issues-when-using-faststore-hooks"
hidden: false
createdAt: "2026-05-19T00:00:00.000Z"
updatedAt: "2026-05-27T00:00:00.000Z"
excerpt: "Common issues when using FastStore hooks in your store project, including import errors, context errors, stale data, performance issues, and TypeScript errors."
domainFilters:
  - FastStore
symptomFilters:
  - Performance degradation
  - Publishing failure
  - Rendering mismatch
---

**Keywords:** FastStore | Hooks | React | Context errors | Performance | TypeScript

[FastStore hooks](https://developers.vtex.com/docs/guides/faststore/developer-tools-hooks-overview) give you access to built-in store features and state. During implementation, you may encounter issues such as import errors, context errors, stale data, performance regressions, or type mismatches.

Use the table below to identify your issue and follow the corresponding solution.

| Issue | Troubleshooting instructions |
| ----- | ---------------------------- |
| Import error, or the hook returns `undefined` when used in a component. | [Hook not available](#hook-not-available) |
| The error `Hook must be used within Provider` is displayed when calling the hook. | [Context errors](#context-errors) |
| A hook returns outdated information that doesn't reflect the latest state. | [Stale data](#stale-data) |
| Hooks cause unnecessary re-renders or noticeably slow down your store. | [Performance issues](#performance-issues) |
| Type mismatches or missing type definitions when using a hook. | [TypeScript errors](#typescript-errors) |

## Solutions

### Hook not available

If you see an import error or the hook returns `undefined` when used in a component, the corresponding package may not be installed correctly, or the hook may be imported from the wrong source.

To solve this issue, follow these steps:

1. Check if the corresponding package is installed in your project (`@faststore/components` for UI hooks or `@faststore/core` for analytics and experimental hooks).
2. Confirm that the installed package version is compatible with your FastStore version.
3. Make sure your app is wrapped with `UIProvider` if you're using UI hooks (such as `useUI` or `useSearch`).
4. Make sure you're importing the hook from the correct package.

### Context errors

If you see the error `Hook must be used within Provider`, the hook is being called outside the context provider it depends on.

To solve this issue, follow these steps:

1. Wrap the component tree with the required provider, depending on the hook in use:
   - `UIProvider` for `useUI` and `useSearch`.
   - `SKUMatrixProvider` for `useSKUMatrix`.
   - `ProductComparisonProvider` for `useProductComparison`.
2. Make sure the provider is placed high enough in the component tree to wrap all components that consume the hook.
3. Make sure the provider isn't rendered conditionally, since this can break the context during re-renders.

### Stale data

If a hook returns outdated information that doesn't reflect the latest state of your store, the issue is usually related to React dependency arrays, store subscriptions, or cached GraphQL data.

To solve this issue, follow these steps:

1. Review the dependencies of any `useEffect` calls that rely on the hook output to ensure they include all relevant values.
2. Verify that your store subscriptions are correctly set up and not being unsubscribed unexpectedly.
3. If you're using GraphQL hooks, clear the cache to force a fresh data fetch.
4. Look for issues with `useMemo` or `useCallback` dependencies that may be preserving stale references.

### Performance issues

If hooks are causing unnecessary re-renders or noticeably slowing down your store, the most common causes are missing memoization or unbounded updates from search and filter hooks.

To solve this issue, follow these steps:

1. Wrap expensive computations with `useMemo` to avoid recalculating them on every render.
2. Wrap event handlers with `useCallback` to prevent unnecessary re-creation of functions.
3. Apply debouncing to search and filter hooks to limit the frequency of updates.
4. Use `useDelayedFacets_unstable` and `useDelayedPagination_unstable` on high-traffic product listing pages.
5. Lazy-load content using visibility hooks (such as `useSlideVisibility`) to reduce initial render cost.

### TypeScript errors

If you see type mismatches or missing type definitions when using FastStore hooks, the issue is typically related to missing `@types` packages, incorrect imports, or outdated FastStore versions.

To solve this issue, follow these steps:

1. Install the corresponding `@types` packages, if available, for any third-party dependencies used alongside the hook.
2. Import the required types directly from the FastStore hook package.
3. Use type assertions only when necessary, and prefer narrowing the type via runtime checks when possible.
4. Confirm that your FastStore version is up to date, since type definitions may evolve between releases.

> ⚠️ If the issue continues after following these steps, [open a ticket with VTEX Support](https://help.vtex.com/support).
