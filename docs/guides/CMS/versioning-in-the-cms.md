---
slug: versioning-in-the-cms
title: Versioning in the CMS
hidden: false
excerpt: Learn how the CMS Schema Registry versions component schemas and Content Types, and how to reference a specific version when consuming a schema.
createdAt: 2026-05-11T12:00:00.000Z
updatedAt: 2026-05-11T12:00:00.000Z
---

The CMS [Schema Registry](https://developers.vtex.com/docs/guides/understanding-cms-architecture-and-schema-declarations#schema-registry) stores every component schema and Content Type definition available to your store. Each one is associated with a version, so storefronts and applications can pin to a known-good version or follow updates automatically within a range.

This guide explains how the versioning model works and how to reference a schema by version.

## Versioning model overview

A schema in the registry behaves much like a software package: it has a unique name and one or more versions you can reference. If you have used [npm](https://www.npmjs.com/), this model will feel familiar: schemas correspond to npm packages, with a few differences explained below.

In npm, a package is identified by its name (`react`, `lodash`) and you fetch a specific release with `react@18.2.0`, the latest stable version with `react@latest`, or a range like `react@1`. The Schema Registry follows the same pattern:

- The package name equivalent is `account.name` (for example, `vtex.faststore` or `mystore.catalog`).
- Versions use the same `@` separator: `vtex.faststore@1.2.3`.
- `@latest` and the bare form (no `@`) both mean "the most recent stable version."
- Pre-release versions (`1.2.3-beta.0`, `2.0.0-rc.1`) are supported and follow standard [semver](https://semver.org/) semantics: they are below their stable counterpart, excluded from range queries, and not returned as `@latest` while any stable version exists.
- Partial version specifiers like `@1` or `@1.2` act as range constraints and resolve to the highest matching stable version.

The range language is intentionally simpler than npm's: there are no `^`, `~`, or `>=` operators, and no [dist-tags](https://docs.npmjs.com/cli/v10/commands/npm-dist-tag) beyond `latest`.

## Schema ID format

Every schema is identified by a **schema ID** with the following grammar:

```sh
<account>.<name>[@<version>]
```

| Segment   | Format                          | Example                                       |
| --------- | ------------------------------- | --------------------------------------------- |
| `account` | Word characters and hyphens     | `vtex`, `mystore`, `my-brand`                 |
| `name`    | Word characters and hyphens     | `faststore`, `catalog`, `product-v2`          |
| `version` | See [Version syntax](#version-syntax) (optional) | `1.2.3`, `1.2.3-beta.0`, `1.2`, `1`, `latest` |

Both `account` and `name` are required. The `@version` suffix is optional when reading: omitting it is equivalent to `@latest`.

The `account` segment should be a valid VTEX account name and plays a role similar to an [npm scope](https://docs.npmjs.com/cli/v10/using-npm/scope). It is part of the schema's identity, not an access-control namespace, which means `vtex.faststore` and `mystore.faststore` are entirely separate schemas.

> ℹ️ The full canonical form of a stored schema is always `account.name@major.minor.patch`, optionally followed by a pre-release suffix (`-beta.0`, `-rc.1`, and so on).

## Version syntax

### Accepted version forms

| Input form                     | Interpretation                            | Example                       |
| ------------------------------ | ----------------------------------------- | ----------------------------- |
| `major.minor.patch`            | Exact stable version.                     | `vtex.faststore@1.2.3`        |
| `major.minor.patch-preRelease` | Exact pre-release version.                | `vtex.faststore@1.2.3-beta.0` |
| `major.minor`                  | Highest stable patch in that minor line.  | `vtex.faststore@1.2`          |
| `major`                        | Highest stable minor and patch for that major. | `vtex.faststore@1`       |
| `latest`                       | Most recent stable version.               | `vtex.faststore@latest`       |
| _(no `@`)_                     | Same as `@latest`.                        | `vtex.faststore`              |

The `latest` tag is case-insensitive: `@LATEST`, `@Latest`, and `@latest` are all equivalent.

Pre-release suffixes follow standard semver rules: dot-separated identifiers composed only of letters, digits, and hyphens (`[a-zA-Z0-9-]`).

### Rejected version forms

The following inputs are rejected with an error:

| Input                        | Reason                                                              |
| ---------------------------- | ------------------------------------------------------------------- |
| `account.name@`              | Empty version string after `@`.                                     |
| `account.name@stable`        | Non-numeric tag — no dist-tags beyond `latest` are supported.       |
| `account.name@1.2.3.4`       | Four segments — not supported.                                      |
| `account.name@1-beta`        | Pre-release requires all three of `major.minor.patch` first.        |
| `account.name@1.2-beta`      | Same — pre-release is not valid without a full base version.        |
| `account.name@1.2.3-beta..0` | Empty identifier in the pre-release string.                         |
| `account.name@^1.2`          | Range operators (`^`, `~`, `>=`) are not supported.                 |
| `.name@1.2.3`                | Empty `account` segment.                                            |
| `account.@1.2.3`             | Empty `name` segment.                                               |

## How versions resolve

When you reference a schema by ID, the registry resolves the version in one of three ways depending on how you wrote it.

### Exact

Input: `account.name@major.minor.patch` or `account.name@major.minor.patch-preRelease`

The registry looks up the exact version you requested. Pre-release versions are **only reachable by exact lookup** — they are excluded from `@latest` (when a stable version exists) and from range queries.

```sh
GET /vtex.faststore@1.2.3
GET /vtex.faststore@1.2.3-beta.0
```

### Latest

Input: `account.name` (no `@`) or `account.name@latest`

The registry returns the highest stable version available for that `account.name` pair. If no stable version has been published yet, it falls back to the highest pre-release version.

```sh
GET /vtex.faststore
GET /vtex.faststore@latest
```

> ⚠️ A pre-release is only resolved as `@latest` while no stable version exists for the schema. As soon as any stable version is published, `@latest` will always point to a stable version.

### Range

Input: `account.name@major` or `account.name@major.minor`

The registry returns the highest **stable** version that matches the constraint. Pre-release versions are excluded from range queries.

- **Major-only** (`@1`) resolves to the highest stable `1.x.x`.
- **Major and minor** (`@1.2`) resolves to the highest stable `1.2.x`.

```sh
GET /vtex.faststore@1     → highest stable 1.x.x (for example, 1.7.4)
GET /vtex.faststore@1.2   → highest stable 1.2.x (for example, 1.2.9)
```

If no stable version matches the constraint, the request returns `404`. For example, a schema that only has `1.0.0-beta.0` published will return `404` for `@1`; you must request it by its exact pre-release version.

## Comparison with npm

If you are coming from npm, the following tables summarize what carries over and what differs.

### What works the same way

| Concept                                       | npm                                  | CMS Schema Registry                                   |
| --------------------------------------------- | ------------------------------------ | ----------------------------------------------------- |
| Package identity                              | `package-name`                       | `account.name`                                        |
| Exact stable version                          | `pkg@1.2.3`                          | `account.name@1.2.3`                                  |
| Exact pre-release version                     | `pkg@1.2.3-beta.0`                   | `account.name@1.2.3-beta.0`                           |
| Latest stable version                         | `pkg@latest` or `pkg`                | `account.name@latest` or `account.name`               |
| Pre-release sorted below stable               | `1.2.3-beta < 1.2.3`                 | Same.                                                 |
| Pre-releases excluded from range queries      | `^1` does not match `1.2.3-beta`     | Same.                                                 |
| `@latest` skips pre-releases when stable exists | npm's `latest` dist-tag usually points to stable | The latest pointer is only set to a pre-release if no stable version exists. |
| Pinned major range                            | `pkg@1` (treated as `1.x.x`)         | `account.name@1`                                      |
| Pinned minor range                            | `pkg@1.2` (treated as `1.2.x`)       | `account.name@1.2`                                    |

### What differs

**The range language is simpler.** npm supports rich constraint expressions: `^1.2.3` (compatible with 1.x.x), `~1.2.3` (same minor), `>=1.0.0 <2.0.0`, and so on. The registry's range language is purely positional: a one-segment specifier pins the major; a two-segment specifier pins the major and minor. There are no operators, wildcards, or compound ranges.

**`@1` is resolved at request time, not pinned.** In npm, `^1.0.0` in a `package.json` resolves once and gets recorded in `package-lock.json`. In the registry, every request resolves fresh from the stored versions — there is no lockfile equivalent. The version you get for `@1` today may be different from the one you got yesterday if a new `1.x.x` was published in between.

**There are no dist-tags beyond `latest`.** npm allows arbitrary dist-tags like `next`, `beta`, or `canary`. The registry only understands `latest`. Pre-release channels (beta, rc, dev) are identified by the pre-release string in the version number itself, not by a separate tag.

## Examples

A few common scenarios to make the model concrete.

### Pinning to a stable major

Your store wants to follow all non-breaking updates of `vtex.faststore` major 2, but never auto-upgrade to a future major 3:

```sh
vtex.faststore@2
```

Each request resolves to the highest stable `2.x.x` available at that moment. When `2.5.0` is published, you get `2.5.0`; when `2.5.1` is published, you get `2.5.1`. A future `3.0.0` does not affect this resolution.

### Pinning to an exact version

Your store needs reproducible content rendering across deployments and does not want any schema change to leak in:

```sh
vtex.faststore@2.3.1
```

This always resolves to the same stored schema. New publications never affect this storefront.

### Following the latest stable version

You want to always render content using the most recent stable schema, regardless of major or minor:

```sh
vtex.faststore@latest
```

or, equivalently:

```sh
vtex.faststore
```

Pre-releases are skipped automatically as long as any stable version exists.

## Related guides

- [Understanding CMS architecture and schema declarations](https://developers.vtex.com/docs/guides/understanding-cms-architecture-and-schema-declarations)
- [Content plugin](https://developers.vtex.com/docs/guides/content-plugin)
- [Semantic Versioning specification](https://semver.org/)
