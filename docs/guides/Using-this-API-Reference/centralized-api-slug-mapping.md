---
title: "Centralized API Slug Mapping in Developer Portal"
excerpt: "Learn about the centralized API slug mapping system in the VTEX Developer Portal and how it maps API display names to URL slugs."
category: "Using this API Reference"
---

# Centralized API Slug Mapping

## Overview

The VTEX Developer Portal uses a centralized mapping system to maintain the relationship between API display names (e.g., 'VTEX - Catalog API') and their corresponding URL slugs (e.g., 'catalog-api'). This mapping is essential for:

- Generating paths for API reference documentation
- Handling OpenAPI schema requests through the `/api/openapi/[slug]` endpoint
- Handling Postman collection requests through the `/api/postman/[slug]` endpoint

## How the Mapping System Works

The mapping system is centralized in a single file (`src/utils/api-slug-mapping.ts`) to ensure consistency across the platform and make maintenance easier.

When an API reference page is requested, the system:

1. Takes the slug from the URL (e.g., `catalog-api`)
2. Uses the mapping to find the corresponding API display name or OpenAPI schema filename
3. Retrieves the appropriate documentation, schema, or Postman collection

## API Slug Map Structure

The mapping is structured as a JavaScript object where:
- Keys are the API display names shown to users
- Values are the URL slugs used in the Developer Portal URLs

Example:

```typescript
export const apiSlugMap: { [key: string]: string } = {
  'VTEX - Catalog API': 'catalog-api',
  'VTEX - Orders API': 'orders-api',
  // ... other mappings
}
```

## Adding New APIs to the Documentation

When a new API is added to the Developer Portal, developers should:

1. Add the new API to the centralized mapping file
2. Upload the corresponding OpenAPI schema to the [openapi-schemas](https://github.com/vtex/openapi-schemas) repository
3. Create any necessary documentation pages

Example of adding a new API to the mapping:

```typescript
// Add to src/utils/api-slug-mapping.ts
'VTEX - New API': 'new-api-slug',
```

## Benefits of Centralized Mapping

The centralized mapping approach provides several advantages:

- **Single Source of Truth**: There's now a single place to update when adding, removing, or changing API mappings
- **Reduced Duplication**: Eliminates duplicate code in multiple files
- **Better Maintainability**: Future changes only need to be made in one place
- **Improved Organization**: Makes the code more modular and follows best practices for configuration data

## Related Documentation

- [Making Your First Request](https://developers.vtex.com/docs/guides/getting-started-making-your-first-request) - Learn how to use the API Reference
- [API Usage](https://developers.vtex.com/docs/guides/getting-started-api-usage) - Understand how to use VTEX APIs
- [Using Postman](https://developers.vtex.com/docs/guides/using-postman) - Work with VTEX APIs in Postman 