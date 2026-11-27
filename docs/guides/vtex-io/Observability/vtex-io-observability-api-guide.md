---
title: "VTEX IO Observability API guide"
slug: "vtex-io-observability-api-guide"
hidden: false
createdAt: "2026-12-07T12:00:00.000Z"
updatedAt: "2026-12-07T12:00:00.000Z"
---

> ⚠️ VTEX IO Observability is currently in beta, which means that VTEX is working to
improve it. If you have any questions, contact [VTEX Support](https://supporticket.vtex.com/support).

The VTEX IO Observability API provides programmatic access to logs and metrics data from your VTEX IO apps. With this API, you can:

- **Query logs:** Retrieve app logs with flexible filtering and pagination (query endpoint).
- **Query metrics:** Access time-series metrics with filtering, aggregation, and pagination (query endpoint).
- **List apps:** Discover which apps have sent logs or metrics in a time range ([Get apps](#get-apps)).
- **Get available fields:** Discover queryable columns for logs ([Get logs fields](#get-logs-fields)) and metrics ([Get metrics fields](#get-metrics-fields)).
- **Get metric names:** List metric names for a specific app in a time range ([Get metric names](#get-metric-names)).
- **Get capabilities:** Retrieve API capabilities, supported operators, aggregations, and limits ([Get capabilities](#get-capabilities)).

All data is isolated per tenant (VTEX account), ensuring complete data security and separation.

This guide describes all API endpoints, with a focus on the query endpoints for logs and metrics: how to use filters, aggregations, ordering, and pagination, with individual examples for each use case.

## Before you begin

Before querying logs and metrics, make sure you have:

- A valid [VTEX API key and token](https://help.vtex.com/en/docs/tutorials/generated-keys) pair with a [role](https://help.vtex.com/docs/tutorials/roles) that includes the **Log Access - Read-only** [License Manager resource](https://help.vtex.com/docs/tutorials/license-manager-resources). For detailed instructions, see [Generating keys](https://help.vtex.com/docs/tutorials/generated-keys#generating-keys) and [Creating roles](https://help.vtex.com/docs/tutorials/creating-roles).
- Your [VTEX account name](https://help.vtex.com/en/docs/tutorials/what-is-an-account-name), which endpoints use as the `tenant` path parameter.

All requests must include the following authentication headers:

- `X-VTEX-API-AppKey`: Your API key (format: `vtexappkey-{accountName}-{suffix}`)
- `X-VTEX-API-AppToken`: Your API token

## Base URL

All endpoints use the following base URL:

```text
https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability
```

Replace `{accountName}` with your VTEX account name.

## Endpoints overview

The query endpoints (POST `/metrics/{tenant}/query` and POST `/logs/{tenant}/query`) are the main ones for retrieving logs and metrics, while the others support discovery and building queries. The VTEX IO Observability API provides the following endpoints:

| Endpoint name | Path | Method | Description |
| :---- | :---- | :---- | :---- |
| Query metrics | `/metrics/{tenant}/query` | POST | Filter, aggregate, and paginate metrics data. |
| Query logs | `/logs/{tenant}/query` | POST | Filter and paginate the log data. |
| Get metrics fields | `/metrics/{tenant}/fields` | GET | Get available fields (columns) for metrics queries. |
| Get metric names | `/metrics/{tenant}/{app}/names` | GET | List metric names for a specific app within a time range. |
| Get logs fields | `/logs/{tenant}/fields` | GET | Get available fields (columns) for log queries. |
| Get apps | `/{tenant}/apps` | GET | List apps that have sent logs or metrics within a time range. |
| Get capabilities | `/capabilities` | GET | Get API capabilities (operators, aggregations, limits, etc.). |

> ℹ️ Except for `/capabilities`, all endpoints accept the `tenant` path parameter (your VTEX account name).

### Query endpoints request body

The query endpoints accept a JSON request body with the following fields:

| Field | Type | Required | Default | Description |
| :---- | :---- | :-: | :---- | :---- |
| `columns` | array of strings | ❌ | All columns | Columns to include in the response. |
| `page` | integer | ❌ | `1` | Page number (1-indexed). |
| `pageSize` | integer | ❌ | `50` | Number of results per page (maximum: `1000`). |
| `filters` | array of objects | ❌ | `[]` | Filter conditions to narrow results. |
| `orders` | array of objects | ❌ | `[]` | Sorting criteria. Each object in the array defines the sort direction for the specified column. |
| `group_by` | object | ❌ | `null` | Grouping configuration for aggregations (metrics only). |
| `aggregations` | array of objects | ❌ | `[]` | Aggregation functions (metrics only). |
| `distinct` | boolean | ❌ | `false` | Whether to return only distinct values. |

### Get metrics fields

`GET /metrics/{tenant}/fields` — Returns available fields (columns) for metrics queries, including each field’s type, whether it is filterable, and whether it is aggregatable. Use this list when building the `columns` and `filters` for the [Query metrics](#query-endpoints-request-body) request body.

### Get metric names

`GET /metrics/{tenant}/{app}/names?fromTime={unix}&toTime={unix}` — Returns the list of metric names for the given app within the specified time range ([Unix timestamps](https://en.wikipedia.org/wiki/Unix_time) in seconds). Use these values for the `MetricName` filter in metrics queries. You can obtain the `app` path parameter from the [Get apps](#get-apps) endpoint.

### Get logs fields

`GET /logs/{tenant}/fields` — Returns available fields (columns) for log queries. Use this list when building the `columns` and `filters` for the [Query logs](#query-endpoints-request-body) request body.

### Get apps

`GET /{tenant}/apps?fromTime={unix}&toTime={unix}` — Returns `LogsApps` and `MetricsApps` arrays of app IDs that have sent telemetry in the given time range (Unix timestamps in seconds). Use these IDs as the `app` filter value in logs and metrics queries.

### Get capabilities

`GET /capabilities` — Returns API capabilities: available operations, available fields, supported operators, aggregation functions, maximum page size, default page size, and query timeout. Use this to discover valid values for filters and aggregations.

## Available columns

The columns you can use in `columns` and `filters` for query requests are listed in the following sections. You can also retrieve them at runtime: use the [Get metrics fields](#get-metrics-fields) endpoint for metrics and the [Get logs fields](#get-logs-fields) endpoint for logs.

### Metrics columns

The following table shows the available columns for metrics queries:

| Column | Type | Description | Filterable |
| :---- | :---- | :---- | :-: |
| `TimestampTime` | DateTime | Timestamp of the metric entry rounded to the minute in [RFC 3339 format](https://www.rfc-editor.org/info/rfc3339). | ✅ |
| `MetricName` | String | Name of the metric. | ✅ |
| `MetricType` | String | Metric type: `gauge`, `sum`, or `histogram`. | ✅ |
| `Value` | Float64 | Aggregated average value (for gauge). | ❌ |
| `Sum` | Float64 | Aggregated sum value. | ❌ |
| `Count` | UInt64 | Aggregated count. | ❌ |
| `app` | String | App ID (e.g., myvendor.myapp@1.0.0). | ✅ |
| `account` | String | VTEX account name. | ✅ |
| `workspace` | String | [Workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace) name. | ✅ |
| `production` | String | Indicates if the app is installed in a production workspace. Possible values: `"true"` or `"false"`. | ✅ |
| `ServiceName` | String | Service name. | ✅ |
| `Attributes` | Map | Custom attributes map. | ❌ |
| `tenant` | String | Tenant identifier. | ✅ |
| `tenant_level` | String | Tenant level. | ✅ |
| `BucketCounts` | AggregateFunction(sumForEach, Array(UInt64)) | List with the amount of items in each [bucket](https://signoz.io/guides/what-is-a-bucket-in-prometheus/#what-is-a-bucket-in-prometheus). Valid only for `histogram` type metrics. | ❌ |
| `ExplicitBounds` | AggregateFunction(any, Array(Float64)) | List with the bound values of [buckets](https://signoz.io/guides/what-is-a-bucket-in-prometheus/#what-is-a-bucket-in-prometheus). Valid only for `histogram` type metrics. | ❌ |

Metrics can have custom attributes stored in the `Attributes` map. Access them using bracket notation, such as `Attributes['status_code']`. To filter by a specific metric name, you can obtain the list of names from the [Get metric names](#get-metric-names) endpoint. For the `app` filter, use app IDs from the [Get apps](#get-apps) endpoint.

### Logs columns

The following table shows the available columns for log queries:

| Column | Type | Description | Filterable |
| :---- | :---- | :---- | :-: |
| `TimestampTime` | DateTime | Timestamp of the log entry in [RFC 3339 format](https://www.rfc-editor.org/info/rfc3339). | ✅ |
| `Timestamp` | DateTime64(9) | Timestamp of the log entry stored as a 64-bit integer with 9-digit precision. | ❌ |
| `level` | String | Log level: `debug`, `info`, `warn`, `error`. | ✅ |
| `app` | String | App ID. | ✅ |
| `account` | String | VTEX account name. | ✅ |
| `workspace` | String | [Workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-workspace) name. | ✅ |
| `production` | String | Indicates if the app is installed in a production workspace. Possible values: `"true"` or `"false"`. | ✅ |
| `data` | String | Log message body (escaped JSON or text). | ✅ |
| `operationId` | String | Operation identifier. | ✅ |
| `requestId` | String | Request identifier. | ✅ |
| `ServiceName` | String | Service name. | ✅ |
| `TraceId` | String | Distributed trace ID. | ✅ |
| `tenant` | String | Tenant identifier. | ✅ |
| `tenant_level` | String | Tenant level. | ✅ |

## Filters

Filters let you narrow query results. Each filter is an object with the available fields defined in the following table:

| Field | Type | Required | Description |
| :---- | :---- | :-: | :---- |
| `column` | string | ✅ | Column name to filter on. |
| `operator` | string | ✅ | Comparison operator. See the full set of supported operators in the [Available operators](#available-operators) section. You can also retrieve them from the [Get capabilities](#get-capabilities) endpoint. |
| `type` | string | ✅ | Value type: `string`, `number`, `timestamp`, or `boolean`. `timestamp` values can be provided in [RFC 3339 format](https://www.rfc-editor.org/info/rfc3339) as strings (e.g., `"2024-01-01T00:00:00Z"`) or [Unix timestamps](https://en.wikipedia.org/wiki/Unix_time) as integers (e.g., `1714857600000`). |
| `value` | any | ✅* | Value to compare.<br/>**Not required for `is_null` and `is_not_null` operators.* |

### Available operators

The following table shows the operators available to use with filters:

| Operator | Alias | Description |
| :---- | :---- | :---- |
| `=` | `eq` | Equal to. |
| `>` | `gt` | Greater than. |
| `<` | `lt` | Less than. |
| `>=` | `gte` | Greater than or equal. |
| `<=` | `lte` | Less than or equal. |
| `!=` | `ne` | Not equal. |
| `LIKE` | `like` | Contains pattern (substring match). |
| `NOT LIKE` | `not_like` | Does not contain the pattern. |
| `IN` | `in` | Value is in a given list. |
| `NOT IN` | `not_in` | Value is not in a given list. |
| `BETWEEN` | `between` | Value is between two bounds. |
| `IS NULL` | `is_null` | Value is null. |
| `IS NOT NULL` | `is_not_null` | Value is not null. |

## Aggregations

Aggregations are available only for metrics queries. Use the `aggregations` array to specify how to aggregate each metric using a function (e.g., average, sum). When using aggregations, specify the `group_by` columns to define how to group results. See the following request example:

```json
{
  ...
  "aggregations": [
    {
      "function": "avg",
      "column": "Value",
      "alias": "avg_duration"
    },
    {
      "function": "sum",
      "column": "Value",
      "alias": "duration_sum"
    }
  ],
  "group_by": {
    "columns": [
      "TimestampTime",
      "app",
      "MetricName",
      "MetricType",
      "ServiceName"
    ]
  }
}
```

### Aggregation functions

You can retrieve the supported aggregation functions from the [Get capabilities](#get-capabilities) endpoint. The following table lists these functions:

| Function | Description | Typical use case |
| :---- | :---- | :---- |
| `sum` | Sum of values. | Total requests, byte counts. |
| `avg` | Average of values. | Average response time. |
| `count` | Count of records. | Number of events. |

Each aggregation object has the following fields:

| Field | Type | Required | Description |
| :---- | :---- | :-: | :---- |
| `function` | string | ✅ | Aggregation function name (`sum`, `avg`, `count`). |
| `column` | string | ✅ | Column to aggregate. Use `Sum` for counter/histogram metrics and `Value` for gauge metrics. |
| `alias` | string | ❌ | Alias for the result column. |

## Ordering

Sort results using the `orders` array. Each order object has the following fields:

| Field | Type | Values | Description |
| :---- | :---- | :---- | :---- |
| `column` | string | Any column name | Column to sort by. |
| `dir` | string | `asc`, `desc` | Sort direction. |

If there is more than one object in the array, the ordering will follow the precedence of the items in the array. See the following request example:

```json
{
  ...
  "orders": [
    {
      "column": "TimestampTime",
      "dir": "desc"
    },
    {
      "column": "MetricName",
      "dir": "asc"
    }
  ]
}
```

In this example, the response will be sorted first by the column `TimestampTime` in descending order. Then, the metrics with the same `TimestampTime` will be sorted by the column `MetricName` in ascending order.

## Response format

All query responses follow the same structure:

```json
{
  "refId": "A",
  "name": "Metrics",
  "fields": [
    {
      "name": "TimestampTime",
      "type": "time",
      "values": [
        "2026-11-26T23:49:00Z",
        "2026-11-26T23:49:00Z",
        "2026-11-26T23:49:00Z",
        "2026-11-26T23:49:00Z"
      ]
    },
    {
      "name": "MetricName",
      "type": "string",
      "values": [
        "http_handler_requests_total",
        "http_handler_requests_total",
        "http_server_requests_closed_total",
        "http_server_requests_closed_total"
      ]
    }
  ],
  "meta": {
    "executedQueryString": "metrics query",
    "pagination": {
      "hasMore": true,
      "page": 1,
      "pageSize": 4,
      "total": 196908
    },
    "truncated": true
  }
}
```

Each item in the `fields` array corresponds to a column, with all row values for that column in the `values` array. The possible field types are:

- `time`: Timestamp values
- `string`: Text values
- `number`: Numeric values
- `boolean`: Boolean values
- `other`: Complex types (maps, arrays)

## Request examples

### Filtering logs by level and app

Retrieve error logs from a specific app within a time range. This example uses the `=` operator on the `level` and `app` columns combined with timestamp filters.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/logs/{accountName}/query`

**Request body:**

```json
{
  "columns": [
    "TimestampTime",
    "level",
    "app",
    "data",
    "requestId"
  ],
  "page": 1,
  "pageSize": 50,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T00:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T23:59:59.000Z"
    },
    {
      "column": "level",
      "operator": "=",
      "type": "string",
      "value": "error"
    },
    {
      "column": "app",
      "operator": "=",
      "type": "string",
      "value": "myvendor.myapp@1.0.0"
    }
  ],
  "orders": [
    {
      "column": "TimestampTime",
      "dir": "desc"
    }
  ]
}
```

**Response body:**

```json
{
  "refId": "A",
  "name": "Logs",
  "fields": [
    {
      "name": "TimestampTime",
      "type": "time",
      "values": [
        "2025-01-15T18:32:10Z",
        "2025-01-15T14:05:47Z"
      ]
    },
    {
      "name": "level",
      "type": "string",
      "values": [
        "error",
        "error"
      ]
    },
    {
      "name": "app",
      "type": "string",
      "values": [
        "myvendor.myapp@1.0.0",
        "myvendor.myapp@1.0.0"
      ]
    },
    {
      "name": "data",
      "type": "string",
      "values": [
        "{\"message\":\"Failed to fetch product catalog\",\"code\":\"CATALOG_UNAVAILABLE\"}",
        "{\"message\":\"Database connection timeout after 30s\",\"code\":\"DB_TIMEOUT\"}"
      ]
    },
    {
      "name": "requestId",
      "type": "string",
      "values": [
        "abc123456789def0123456789abcdef0",
        "fed0987654321abcdef0123456789abc"
      ]
    }
  ],
  "meta": {
    "executedQueryString": "logs query"
  },
  "pagination": {
    "hasMore": true,
    "page": 1,
    "pageSize": 50,
    "total": 1739544
  }
}
```

### Filtering apps with the LIKE operator

Use the `LIKE` operator in `filters` to search for a substring of the app ID. Instead of using the `=` operator in `filters` for an app with a specific vendor, name, and version, retrieve data from multiple apps that share a portion of the app ID. Due to the app ID structure (`{vendor}.{app-name}@{major}.{minor}.{patch}-{beta-name}`), you can filter by a specific app ID segment, changing only the `value` field.

Examples:

#### Filtering by apps from the same vendor

```json
{
  ...
  "filters": [
    {
      "column": "app",
      "operator": "LIKE",
      "type": "string",
      "value": "vtexventures."
    }
  ]
}
```

#### Filtering by all the versions of a specific app

```json
{
  ...
  "filters": [
    {
      "column": "app",
      "operator": "LIKE",
      "type": "string",
      "value": "vtex.broadcaster@"
    }
  ]
}
```

#### Filtering by all the versions of a specific app major

```json
{
  ...
  "filters": [
    {
      "column": "app",
      "operator": "LIKE",
      "type": "string",
      "value": "vtex.store-newsletter@1."
    }
  ]
}
```

#### Filtering by apps with beta versions

```json
{
  ...
  "filters": [
    {
      "column": "app",
      "operator": "LIKE",
      "type": "string",
      "value": "-beta"
    }
  ]
}
```

> ℹ️ For details about beta app versions, see [Understanding app versioning](https://developers.vtex.com/docs/guides/vtex-io-documentation-releasing-a-new-app-version#understanding-app-versioning).

### Searching logs by pattern with the LIKE operator

Find logs containing a specific substring in the `data` field. This search pattern is useful for locating error messages, stack traces, or any text pattern across your logs.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/logs/{accountName}/query`

**Request body:**

```json
{
  "columns": ["TimestampTime", "level", "app", "data"],
  "page": 1,
  "pageSize": 50,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T00:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T23:59:59.000Z"
    },
    {
      "column": "data",
      "operator": "LIKE",
      "type": "string",
      "value": "connection timeout"
    }
  ]
}
```

**Response body:**

```json
{
  "refId": "A",
  "name": "Logs",
  "fields": [
    {
      "name": "TimestampTime",
      "type": "time",
      "values": ["2025-01-15T09:12:33Z"]
    },
    {
      "name": "level",
      "type": "string",
      "values": ["error"]
    },
    {
      "name": "app",
      "type": "string",
      "values": ["myvendor.myapp@1.0.0"]
    },
    {
      "name": "data",
      "type": "string",
      "values": ["{\"message\":\"Redis connection timeout after 5000ms\",\"retries\":3}"]
    }
  ],
  "meta": {
    "executedQueryString": "logs query"
  }
}
```

### Filtering logs with the IN operator

Retrieve logs matching multiple log levels at once. The `IN` operator lets you match a column value against a list of values. This example filters by logs of types `"warn"` and `"error"`.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/logs/{accountName}/query`

**Request body:**

```json
{
  "columns": ["TimestampTime", "level", "app", "data"],
  "page": 1,
  "pageSize": 100,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T00:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T23:59:59.000Z"
    },
    {
      "column": "level",
      "operator": "IN",
      "type": "string",
      "value": [
        "warn",
        "error"
      ]
    },
    {
      "column": "app",
      "operator": "=",
      "type": "string",
      "value": "myvendor.myapp@1.0.0"
    }
  ],
  "orders": [
    {
      "column": "TimestampTime",
      "dir": "desc"
    }
  ]
}
```

**Response body:**

```json
{
  "refId": "A",
  "name": "Logs",
  "fields": [
    {
      "name": "TimestampTime",
      "type": "time",
      "values": [
        "2025-01-15T20:45:00Z",
        "2025-01-15T16:30:22Z",
        "2025-01-15T11:10:05Z"
      ]
    },
    {
      "name": "level",
      "type": "string",
      "values": [
        "error",
        "warn",
        "warn"
      ]
    },
    {
      "name": "app",
      "type": "string",
      "values": [
        "myvendor.myapp@1.0.0",
        "myvendor.myapp@1.0.0",
        "myvendor.myapp@1.0.0"
      ]
    },
    {
      "name": "data",
      "type": "string",
      "values": [
        "{\"message\":\"Unhandled exception in order processing\"}",
        "{\"message\":\"Slow query detected: 2800ms\"}",
        "{\"message\":\"Deprecated API method called: getProductV1\"}"
      ]
    }
  ],
  "meta": {
    "executedQueryString": "logs query"
  }
}
```

### Querying metrics with custom attributes

Access custom attributes stored in the `Attributes` map using bracket notation. This example retrieves HTTP request metrics broken down by status code and method.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/metrics/{accountName}/query`

**Request body:**

```json
{
  "columns": [
    "TimestampTime",
    "MetricName",
    "Attributes['status_code']",
    "Attributes['method']",
    "sumMerge(Sum) as Sum"
  ],
  "page": 1,
  "pageSize": 100,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T00:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T23:59:59.000Z"
    },
    {
      "column": "app",
      "operator": "=",
      "type": "string",
      "value": "myvendor.myapp@1.0.0"
    },
    {
      "column": "MetricName",
      "operator": "=",
      "type": "string",
      "value": "http_client_requests_total"
    }
  ],
  "orders": [
    {
      "column": "TimestampTime",
      "dir": "desc"
    }
  ]
}
```

**Response body:**

```json
{
  "refId": "A",
  "name": "Metrics",
  "fields": [
    {
      "name": "TimestampTime",
      "type": "time",
      "values": [
        "2025-01-15T12:00:00Z",
        "2025-01-15T12:00:00Z",
        "2025-01-15T12:01:00Z"
      ]
    },
    {
      "name": "MetricName",
      "type": "string",
      "values": [
        "http_client_requests_total",
        "http_client_requests_total",
        "http_client_requests_total"
      ]
    },
    {
      "name": "arrayElement(Attributes, 'status_code')",
      "type": "string",
      "values": [
        "200",
        "500",
        "200"
      ]
    },
    {
      "name": "arrayElement(Attributes, 'method')",
      "type": "string",
      "values": [
        "GET",
        "POST",
        "GET"
      ]
    },
    {
      "name": "Sum",
      "type": "number",
      "values": [
        1520,
        3,
        1489
      ]
    }
  ],
  "meta": {
    "executedQueryString": "metrics query"
  }
}
```

### Aggregating metrics with group by

Calculate aggregated statistics over time. This example computes the average response duration grouped by minute and app using the `aggregations` and `group_by` fields.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/metrics/{accountName}/query`

**Request body:**

```json
{
  "page": 1,
  "pageSize": 3,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T10:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T11:00:00.000Z"
    },
    {
      "column": "MetricName",
      "operator": "=",
      "type": "string",
      "value": "runtime_http_requests_duration_milliseconds"
    },
    {
      "column": "app",
      "operator": "=",
      "type": "string",
      "value": "myvendor.myapp@1.0.0"
    }
  ],
  "aggregations": [
    {
      "function": "avg",
      "column": "Value",
      "alias": "avg_duration"
    }
  ],
  "group_by": {
    "columns": [
      "TimestampTime",
      "app",
      "MetricName",
      "MetricType",
      "ServiceName"
    ]
  },
  "orders": [
    {
      "column": "TimestampTime",
      "dir": "asc"
    }
  ]
}
```

**Response body:**

```json
{
  "refId": "A",
  "name": "Metrics",
  "fields": [
    {
      "name": "TimestampTime",
      "type": "time",
      "values": [
        "2025-01-15T10:00:00Z",
        "2025-01-15T10:01:00Z",
        "2025-01-15T10:02:00Z"
      ]
    },
    {
      "name": "app",
      "type": "string",
      "values": [
        "myvendor.myapp@1.0.0",
        "myvendor.myapp@1.0.0",
        "myvendor.myapp@1.0.0"
      ]
    },
    {
        "name": "MetricName",
        "type": "string",
        "values": [
          "runtime_http_requests_duration_milliseconds",
          "runtime_http_requests_duration_milliseconds",
          "runtime_http_requests_duration_milliseconds"
        ]
    },
    {
        "name": "MetricType",
        "type": "string",
        "values": [
          "histogram",
          "histogram",
          "histogram"
        ]
    },
    {
      "name": "avg_duration",
      "type": "number",
      "values": [
        245,
        312,
        198
      ]
    }
  ],
  "meta": {
    "executedQueryString": "metrics query"
  }
}
```

### Summing counter metrics with group by

Calculate the total request counts, grouped by metric name, using the `sum` aggregation. This operation is suitable for counter-type (`sum`) metrics such as request totals.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/metrics/{accountName}/query`

**Request body:**

```json
{
  "page": 1,
  "pageSize": 3,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T00:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T23:59:59.000Z"
    },
    {
      "column": "MetricType",
      "operator": "=",
      "type": "string",
      "value": "sum"
    },
    {
      "column": "app",
      "operator": "=",
      "type": "string",
      "value": "myvendor.myapp@1.0.0"
    }
  ],
  "aggregations": [
    {
      "function": "sum",
      "column": "Sum",
      "alias": "total_requests"
    },
    {
      "function": "sum",
      "column": "Count",
      "alias": "total_count"
    }
  ],
  "group_by": {
    "columns": ["MetricName"]
  },
  "orders": [
    {
      "column": "total_requests",
      "dir": "desc"
    }
  ]
}
```

**Response body:**

```json
{
  "refId": "A",
  "name": "Metrics",
  "fields": [
    {
      "name": "MetricName",
      "type": "string",
      "values": [
        "http_client_requests_total",
        "http_server_requests_total",
        "cache_hits_total"
      ]
    },
    {
      "name": "total_requests",
      "type": "number",
      "values": [
        58320,
        42150,
        15780
      ]
    },
    {
      "name": "total_count",
      "type": "number",
      "values": [
        58320,
        42150,
        15780
      ]
    }
  ],
  "meta": {
    "executedQueryString": "metrics query"
  }
}
```

### Using direct merge functions in columns

For advanced use cases, you can use merge functions directly in the `columns` array instead of the `aggregations` field. This operation gives you more explicit control over how to merge pre-aggregated metric data.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/metrics/{accountName}/query`

**Request body:**

```json
{
  "columns": [
    "TimestampTime",
    "MetricName",
    "app",
    "sumMerge(Sum) as total",
    "avgMerge(Value) as average"
  ],
  "page": 1,
  "pageSize": 3,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T10:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T11:00:00.000Z"
    },
    {
      "column": "app",
      "operator": "=",
      "type": "string",
      "value": "myvendor.myapp@1.0.0"
    },
    {
      "column": "MetricName",
      "operator": "=",
      "type": "string",
      "value": "http_requests_total"
    }
  ],
  "orders": [
    {
      "column": "TimestampTime",
      "dir": "desc"
    }
  ]
}
```

**Response body:**

```json
{
  "refId": "A",
  "name": "Metrics",
  "fields": [
    {
      "name": "TimestampTime",
      "type": "time",
      "values": [
        "2025-01-15T10:59:00Z",
        "2025-01-15T10:58:00Z",
        "2025-01-15T10:57:00Z"
      ]
    },
    {
      "name": "MetricName",
      "type": "string",
      "values": [
        "http_requests_total",
        "http_requests_total",
        "http_requests_total"
      ]
    },
    {
      "name": "app",
      "type": "string",
      "values": [
        "myvendor.myapp@1.0.0",
        "myvendor.myapp@1.0.0",
        "myvendor.myapp@1.0.0"
      ]
    },
    {
      "name": "total",
      "type": "number",
      "values": [
        892,
        1045,
        763
      ]
    },
    {
      "name": "average",
      "type": "number",
      "values": [
        0.342,
        0.401,
        0.289
      ]
    }
  ],
  "meta": {
    "executedQueryString": "metrics query"
  }
}
```

### Filtering metrics by type

Query only a specific metric type (e.g., `histogram`) using the `MetricType` column. The platform supports three OpenTelemetry metric types: `gauge` (point-in-time values), `sum` (cumulative counters), and `histogram` (distributions).

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/metrics/{accountName}/query`

**Request body:**

```json
{
  "columns": [
    "TimestampTime",
    "MetricName",
    "MetricType",
    "app",
    "Count"
  ],
  "page": 1,
  "pageSize": 2,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T00:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T23:59:59.000Z"
    },
    {
      "column": "MetricType",
      "operator": "=",
      "type": "string",
      "value": "histogram"
    },
    {
      "column": "app",
      "operator": "=",
      "type": "string",
      "value": "myvendor.myapp@1.0.0"
    }
  ],
  "orders": [
    {
      "column": "TimestampTime",
      "dir": "desc"
    }
  ]
}
```

**Response body:**

```json
{
  "refId": "A",
  "name": "Metrics",
  "fields": [
    {
      "name": "TimestampTime",
      "type": "time",
      "values": [
        "2025-01-15T15:30:00Z",
        "2025-01-15T15:29:00Z"
      ]
    },
    {
      "name": "MetricName",
      "type": "string",
      "values": [
        "runtime_http_requests_duration_milliseconds",
        "runtime_http_requests_duration_milliseconds"
      ]
    },
    {
      "name": "MetricType",
      "type": "string",
      "values": [
        "histogram",
        "histogram"
      ]
    },
    {
      "name": "app",
      "type": "string",
      "values": [
        "myvendor.myapp@1.0.0",
        "myvendor.myapp@1.0.0"
      ]
    },
    {
      "name": "Count",
      "type": "number",
      "values": [
        1523,
        1487
      ]
    }
  ],
  "meta": {
    "executedQueryString": "metrics query"
  }
}
```

### Paginating through large result sets

Use the `page` and `pageSize` fields to paginate through results. The maximum `pageSize` is `1000`. Increment the `page` value to fetch subsequent pages.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/logs/{accountName}/query`

**Request body (page 1):**

```json
{
  "columns": ["TimestampTime", "level", "app", "data"],
  "page": 1,
  "pageSize": 10,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T00:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T23:59:59.000Z"
    },
    {
      "column": "app",
      "operator": "=",
      "type": "string",
      "value": "myvendor.myapp@1.0.0"
    }
  ],
  "orders": [
    {
      "column": "TimestampTime",
      "dir": "desc"
    }
  ]
}
```

**Request body (page 2):**

```json
{
  "columns": ["TimestampTime", "level", "app", "data"],
  "page": 2,
  "pageSize": 10,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T00:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T23:59:59.000Z"
    },
    {
      "column": "app",
      "operator": "=",
      "type": "string",
      "value": "myvendor.myapp@1.0.0"
    }
  ],
  "orders": [
    {
      "column": "TimestampTime",
      "dir": "desc"
    }
  ]
}
```

### Filtering logs by production workspace

Filter logs to show only entries from production or non-production workspaces using a boolean-style filter on the `production` column.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/logs/{accountName}/query`

**Request body:**

```json
{
  "columns": [
    "TimestampTime",
    "level",
    "app",
    "workspace",
    "production",
    "data"
  ],
  "page": 1,
  "pageSize": 1,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T00:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T23:59:59.000Z"
    },
    {
      "column": "production",
      "operator": "=",
      "type": "string",
      "value": "true"
    },
    {
      "column": "level",
      "operator": "=",
      "type": "string",
      "value": "error"
    }
  ],
  "orders": [
    {
      "column": "TimestampTime",
      "dir": "desc"
    }
  ]
}
```

**Response body:**

```json
{
  "refId": "A",
  "name": "Logs",
  "fields": [
    {
      "name": "TimestampTime",
      "type": "time",
      "values": ["2025-01-15T20:15:00Z"]
    },
    {
      "name": "level",
      "type": "string",
      "values": ["error"]
    },
    {
      "name": "app",
      "type": "string",
      "values": ["myvendor.myapp@1.0.0"]
    },
    {
      "name": "workspace",
      "type": "string",
      "values": ["master"]
    },
    {
      "name": "production",
      "type": "string",
      "values": ["true"]
    },
    {
      "name": "data",
      "type": "string",
      "values": ["{\"message\":\"Payment gateway returned HTTP 503\",\"gateway\":\"braintree\"}"]
    }
  ],
  "meta": {
    "executedQueryString": "logs query"
  }
}
```

### Excluding values with NOT IN and NOT LIKE operators

Exclude specific apps or patterns from your query results. This example excludes certain apps from the results using `NOT IN` and excludes log messages matching a pattern using `NOT LIKE`.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/logs/{accountName}/query`

**Request body:**

```json
{
  "columns": ["TimestampTime", "level", "app", "data"],
  "page": 1,
  "pageSize": 2,
  "filters": [
    {
      "column": "TimestampTime",
      "operator": ">=",
      "type": "timestamp",
      "value": "2025-01-15T00:00:00.000Z"
    },
    {
      "column": "TimestampTime",
      "operator": "<=",
      "type": "timestamp",
      "value": "2025-01-15T23:59:59.000Z"
    },
    {
      "column": "app",
      "operator": "NOT IN",
      "type": "string",
      "value": [
        "myvendor.debug-tool@1.0.0",
        "myvendor.test-app@0.1.0"
      ]
    },
    {
      "column": "data",
      "operator": "NOT LIKE",
      "type": "string",
      "value": "healthcheck"
    },
    {
      "column": "level",
      "operator": "=",
      "type": "string",
      "value": "error"
    }
  ],
  "orders": [
    {
      "column": "TimestampTime",
      "dir": "desc"
    }
  ]
}
```

**Response body:**

```json
{
  "refId": "A",
  "name": "Logs",
  "fields": [
    {
      "name": "TimestampTime",
      "type": "time",
      "values": [
        "2025-01-15T19:42:00Z",
        "2025-01-15T17:08:30Z"
      ]
    },
    {
      "name": "level",
      "type": "string",
      "values": [
        "error",
        "error"
      ]
    },
    {
      "name": "app",
      "type": "string",
      "values": [
        "myvendor.checkout-app@2.3.1",
        "myvendor.catalog-sync@1.5.0"
      ]
    },
    {
      "name": "data",
      "type": "string",
      "values": [
        "{\"message\":\"Failed to process order: insufficient inventory\"}",
        "{\"message\":\"Catalog sync failed for category 42\"}"
      ]
    }
  ],
  "meta": {
    "executedQueryString": "logs query"
  }
}
```

## Best practices

Use the following best practices to avoid errors and improve request usability:

- **Always filter by time:** Use `TimestampTime` filters to limit the amount of data scanned per query.
- **Be specific with filters:** Filter by `app` and `MetricName` whenever possible to narrow results efficiently.
- **Request only needed columns:** Specify only the columns you need in the `columns` array instead of returning all columns.
- **Paginate large results:** Use `page` and `pageSize` to fetch results in manageable chunks instead of requesting large datasets at once.
- **Match aggregation columns to metric types:** Use the `Sum` column for counter and histogram metrics and the `Value` column for gauge metrics.

## Data retention

The data retention period is three days by default.

> ℹ️ Metrics are pre-aggregated to 1-minute intervals for efficient storage and querying.

## Error codes

The following errors may appear in the response body as a message.

### 400 - Bad Request

Example responses for bad requests:

- **Message error example**: `"invalid request body"`. The JSON in the request body is malformed or contains invalid fields.

    ```json
    {
      "error": {
        "code": "400",
        "message": "invalid request body"
      },
      "timestamp": "2025-01-15T10:00:00Z"
    }
    ```

- **Message error example**: `"column 'X' is not allowed"`. The specified column does not exist or is not available for the query type.

    ```json
    {
      "error": {
        "code": "400",
        "message": "invalid request: column 'invalidColumn' is not allowed"
      },
      "timestamp": "2025-01-15T10:00:00Z"
    }
    ```

### 401 - Unauthorized

Example responses for unauthorized requests:

- **Message error example**: `"Missing app key or token"`. The authentication headers are missing from the request.

    ```json
    {
      "message": "Missing app key or token"
    }
    ```

- **Message error example**: `"Invalid token"`. The provided API key or token is incorrect.

    ```json
    {
      "message": "Invalid token"
    }
    ```

### 403 - Forbidden

**Message error example**: `"Forbidden"`. The `{accountName}` in the API key does not match the `tenant` in the request URL.

```json
{
  "message": "Forbidden"
}
```

### 408 - Request Timeout

**Message error example**: `"Query timeout"`. The query exceeded the 30-second timeout. Try narrowing your filters or reducing the time range.

```json
{
  "message": "Query timeout"
}
```

### 429 - Too Many Requests

**Message error example**: `"Quota exceeded"`. You have exceeded your account's rate limit. Wait before retrying.

```json
{
  "message": "Quota exceeded"
}
```
