---
title: "Architecture"
slug: "master-data-architecture"
hidden: false
metadata: 
  title: "Master Data - Architecture"
createdAt: "2021-04-08T20:20:59.105Z"
updatedAt: "2021-11-18T13:44:22.424Z"
---

This guide provides an overview of the Master Data architecture. A service is a program that performs automated tasks or responds to specific events, whether hardware-related or triggered by requests from other software.

The Master Data architecture is composed of four core services:
- API: Serves as the entry point for external systems to interact with Master Data.
- Worker: Manages backend processes, ensuring data consistency and enabling advanced operations.
- Storage: Serves as the central repository for documents.
- Search Engine: Provides advanced search and aggregation capabilities.

## Core services

### API service

The API service acts as the primary gateway for interacting with Master Data. It handles HTTP requests, providing endpoints to access and manipulate data stored in the system. Key features include:

- Access to endpoints for reading, writing, searching, and managing documents.
- Routing external requests to internal services like [Storage](#storage) and [Search Engine](#search-engine).
- Ensuring secure communication between client applications and Master Data.

The Master Data API endpoints can be found in our API reference:
- [Master Data V1](https://developers.vtex.com/docs/api-reference/masterdata-api)
- [Master Data V2](https://developers.vtex.com/docs/api-reference/master-data-api-v2).

> The API service does not process or store data directly. Instead, it routes requests to the appropriate services for execution.

### Worker service

The Worker service is responsible for ensuring data consistency and enabling advanced operations by automating and optimizing backend processes. Key features include:

- **Document indexing:** Sends Documents to the [Search Engine](#search-engine) for indexing, keeping data searchable and up-to-date.
- **Trigger execution:** Automates tasks triggered by specific events, such as updating fields or sending notifications (e.g., emailing a client when their Document is updated).
- **Bulk data operations:** Handles bulk imports or exports of Documents in CSV format for specific Data Entities.

The Worker service ensures data is consistently updated across all services, maintaining integrity and accessibility.

### Storage service

The Storage service functions as the central repository for your data. It is a secure, scalable database designed to store billions of documents for VTEX accounts. Key features include:

- **Document storage:** Documents are securely stored and can be retrieved individually via the Documents API.
- **Account-specific access:** Data access is account-specific. A store account can only access its own data, ensuring strict data isolation between accounts.

> **Tip:** For precise and secure data retrieval, use the Documents API, which retrieves one document per request.

### Search Engine service

The Search Engine service enables advanced filtering and aggregations, allowing users to filter, sort, and retrieve Documents. It indexes data from the Storage service, enabling the retrieval of multiple documents through filtering and scrolling.

> **Tip:** Use the Search and Scroll APIs to retrieve large sets of indexed data from the Search Engine with advanced filtering and pagination capabilities.

## Data consistency workflow

To ensure data consistency across its services, Master Data employs a synchronized workflow:

1. **Storage update:** When data is updated in Storage, a notification is triggered to inform other services.
2. **Worker execution:** The Worker processes the notification, executes any associated triggers, and forwards the updated Document to the Search Engine.
3. **Search Engine update:** The Search Engine indexes the updated document, making the latest version available for search and retrieval.

For more information, refer to the [Consistency Level](https://developers.vtex.com/docs/guides/master-data-consistency-level) article.

