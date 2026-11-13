---
title: "VTEX IO Observability API guide"
slug: "vtex-io-observability-api-guide"
hidden: false
createdAt: "2026-02-26T00:00:00.000Z"
updatedAt: "2026-02-26T00:00:00.000Z"
---

> ⚠️ VTEX IO Observability is currently in beta, which means that VTEX is working to improve it. If you have any questions, contact [VTEX Support](https://supporticket.vtex.com/support).

The VTEX IO Observability API provides programmatic access to logs and metrics data from your VTEX IO apps. With this API you can:

- **Query logs** — Retrieve app logs with flexible filtering and pagination (query endpoint).
- **Query metrics** — Access time-series metrics with filtering, aggregation, and pagination (query endpoint).
- **List apps** — Discover which apps have sent logs or metrics in a time range ([Get apps](#get-apps)).
- **Get available fields** — Discover queryable columns for logs ([Get logs fields](#get-logs-fields)) and metrics ([Get metrics fields](#get-metrics-fields)).
- **Get metric names** — List metric names for a specific app in a time range ([Get metric names](#get-metric-names)).
- **Get capabilities** — Retrieve API capabilities, supported operators, aggregations, and limits ([Get capabilities](#get-capabilities)).

All data is isolated per tenant (VTEX account), ensuring complete data security and separation.

This guide describes all API endpoints, with a focus on the **query endpoints** for logs and metrics: how to use filters, aggregations, ordering, and pagination, with individual examples for each use case.

## Before you begin

Before querying logs and metrics, make sure you have:

- A valid [VTEX application key and token](https://help.vtex.com/en/tutorial/application-keys--2onstR7H68Y6meYKaMECGY) pair with the `colossus-read-logs` permission.
- Your VTEX account name, which will be used as the `tenant` path parameter.

All requests must include the following authentication headers:

| Header | Description |
| - | - |
| `X-VTEX-API-AppKey` | Your application key (format: `vtexappkey-{accountName}-{suffix}`). |
| `X-VTEX-API-AppToken` | Your application token. |

>⚠️ The `{accountName}` in your application key **must match** the `tenant` used in the request URL path. Cross-tenant access is blocked for security.

## Base URL

All endpoints use the following base URL:

`https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability`

Replace `{accountName}` with your VTEX account name.

## Endpoints overview

The Observability API provides the following endpoints. The **query endpoints** (POST `/metrics/{tenant}/query` and POST `/logs/{tenant}/query`) are the main ones for retrieving logs and metrics; the others support discovery and building queries.

>ℹ️ Except for `/capabilities`, all endpoints accept the `tenant` path parameter
(your VTEX account name).

| Endpoint | Method | Description |
| - | - | - |
| `/metrics/{tenant}/query` | POST | **Query metrics** — Filter, aggregate, and paginate metrics data. |
| `/logs/{tenant}/query` | POST | **Query logs** — Filter and paginate logs data. |
| `/metrics/{tenant}/fields` | GET | Get available fields (columns) for metrics queries. |
| `/metrics/{tenant}/{app}/names` | GET | List metric names for a specific app within a time range. |
| `/logs/{tenant}/fields` | GET | Get available fields (columns) for logs queries. |
| `/{tenant}/apps` | GET | List apps that have sent logs or metrics within a time range. |
| `/capabilities` | GET | Get API capabilities (operators, aggregations, limits, etc.). |

### Query endpoints request body

The **query endpoints** accept a JSON request body with the following fields:

| Field | Type | Required | Default | Description |
| - | - | :-: | - | - |
| `columns` | array of strings | ❌ | All columns | Columns to include in the response. |
| `page` | integer | ❌ | `1` | Page number (1-indexed). |
| `pageSize` | integer | ❌ | `50` | Number of results per page (maximum: `1000`). |
| `filters` | array of objects | ❌ | `[]` | Filter conditions to narrow results. |
| `orders` | array of objects | ❌ | `[]` | Sorting criteria. |
| `group_by` | object | ❌ | `null` | Grouping configuration for aggregations. |
| `aggregations` | array of objects | ❌ | `[]` | Aggregation functions (metrics only). |
| `distinct` | boolean | ❌ | `false` | Whether to return only distinct values. |

### Get metrics fields

`GET /metrics/{tenant}/fields` — Returns available fields (columns) for metrics queries, including each field’s type, whether it is filterable, and whether it is aggregatable. Use this list when building the `columns` and `filters` for the [Query metrics](#query-endpoints-request-body) request body.

### Get metric names

`GET /metrics/{tenant}/{app}/names?fromTime={unix}&toTime={unix}` — Returns the list of metric names for the given app within the specified time range (Unix timestamps in seconds). Use these values for the `MetricName` filter in metrics queries. The `app` path parameter can be obtained from the [Get apps](#get-apps) endpoint.

### Get logs fields

`GET /logs/{tenant}/fields` — Returns available fields (columns) for logs queries. Use this list when building the `columns` and `filters` for the [Query logs](#query-endpoints-request-body) request body.

### Get apps

`GET /{tenant}/apps?fromTime={unix}&toTime={unix}` — Returns `logs_apps` and `metrics_apps` arrays of app IDs that have sent telemetry in the given time range (Unix timestamps in seconds). Use these IDs as the `app` filter value in logs and metrics queries.

### Get capabilities

`GET /capabilities` — Returns API capabilities: supported operators, aggregation functions, maximum page size, default page size, and query timeout. Use this to discover valid values for filters and aggregations.

## Available columns

The columns you can use in `columns` and `filters` for query requests are listed below. You can also retrieve them at runtime: use the [Get metrics fields](#get-metrics-fields) endpoint for metrics and the [Get logs fields](#get-logs-fields) endpoint for logs.

### Metrics columns

| Column | Type | Description | Filterable | Aggregatable |
| - | - | - | :-: | :-: |
| `TimestampTime` | DateTime | Timestamp rounded to the minute. | ✅ | ❌ |
| `MetricName` | String | Name of the metric. | ✅ | ❌ |
| `MetricType` | String | Metric type: `gauge`, `sum`, or `histogram`. | ✅ | ❌ |
| `Value` | Float64 | Aggregated average value (for gauge). | ✅ | ✅ |
| `Sum` | Float64 | Aggregated sum value. | ✅ | ✅ |
| `Count` | UInt64 | Aggregated count. | ✅ | ✅ |
| `app` | String | Application ID. | ✅ | ❌ |
| `account` | String | VTEX account name. | ✅ | ❌ |
| `workspace` | String | Workspace name. | ✅ | ❌ |
| `production` | String | `"true"` or `"false"`. | ✅ | ❌ |
| `ServiceName` | String | Service name. | ✅ | ❌ |
| `Attributes` | Map | Custom attributes map. | ✅ | ❌ |
| `tenant` | String | Tenant identifier. | ✅ | ❌ |

Metrics can have custom attributes stored in the `Attributes` map. Access them using bracket notation, such as `Attributes['status_code']`. To filter by a specific metric name, you can obtain the list of names from [Get metric names](#get-metric-names) endpoint. For the `app` filter, use app IDs from the [Get apps](#get-apps) endpoint.

### Logs columns

| Column | Type | Description | Filterable |
| - | - | - | :-: |
| `TimestampTime` | DateTime | Timestamp of the log entry. | ✅ |
| `level` | String | Log level: `debug`, `info`, `warn`, `error`. | ✅ |
| `app` | String | Application ID. | ✅ |
| `account` | String | VTEX account name. | ✅ |
| `workspace` | String | Workspace name. | ✅ |
| `production` | String | `"true"` or `"false"`. | ✅ |
| `data` | String | Log message body (JSON or text). | ✅ |
| `operationId` | String | Operation identifier. | ✅ |
| `requestId` | String | Request identifier. | ✅ |
| `ServiceName` | String | Service name. | ✅ |
| `TraceId` | String | Distributed trace ID. | ✅ |
| `tenant` | String | Tenant identifier. | ✅ |

## Filters

Filters allow you to narrow down query results. Each filter is an object with the available fields defined in the table below.

| Field | Type | Required | Description |
| - | - | :-: | - |
| `column` | string | ✅ | Column name to filter on. |
| `operator` | string | ✅ | Comparison operator. The full set of supported operators is listed in [Available operators](#available-operators). You can also retrieve them from the [Get capabilities](#get-capabilities) endpoint. |
| `type` | string | ✅ | Value type: `string`, `number`, `timestamp`, or `boolean`. |
| `value` | any | ✅* | Value to compare.<br/>*Not required for `is_null` and `is_not_null` operators. |

### Available operators

| Operator | Alias | Description |
| - | - | - |
| `=` | `eq` | Equal to. |
| `>` | `gt` | Greater than. |
| `<` | `lt` | Less than. |
| `>=` | `gte` | Greater than or equal. |
| `<=` | `lte` | Less than or equal. |
| `!=` | `ne` | Not equal. |
| `LIKE` | `like` | Contains pattern (substring match). |
| `NOT LIKE` | `not_like` | Does not contain pattern. |
| `IN` | `in` | Value is in a given list. |
| `NOT IN` | `not_in` | Value is not in a given list. |
| `BETWEEN` | `between` | Value is between two bounds. |
| `IS NULL` | `is_null` | Value is null. |
| `IS NOT NULL` | `is_not_null` | Value is not null. |

## Aggregations

Aggregations are available for **metrics queries only**. When using aggregations, you should specify `group_by` columns to define how results are grouped. Supported aggregation functions are listed below; you can also retrieve them from the [Get capabilities](#get-capabilities) endpoint.

### Aggregation functions

| Function | Description | Typical use case |
| - | - | - |
| `sum` | Sum of values. | Total requests, byte counts. |
| `avg` | Average of values. | Average response time. |
| `count` | Count of records. | Number of events. |
| `min` | Minimum value. | Fastest response. |
| `max` | Maximum value. | Slowest response. |

Each aggregation object has the following fields:

| Field | Type | Required | Description |
| - | - | :-: | - |
| `function` | string | ✅ | Aggregation function name (`sum`, `avg`, `count`, `min`, `max`). |
| `column` | string | ✅ | Column to aggregate. Use `Sum` for counter/histogram metrics and `Value` for gauge metrics. |
| `alias` | string | ❌ | Alias for the result column. |

## Ordering

Sort results using the `orders` array. Each order object has the following fields:

| Field | Type | Values | Description |
| - | - | - | - |
| `column` | string | Any column name | Column to sort by. |
| `dir` | string | `asc`, `desc` | Sort direction. |

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
      "values": ["2025-01-01T10:00:00Z", "2025-01-01T10:01:00Z"]
    },
    {
      "name": "MetricName",
      "type": "string",
      "values": ["http_requests_total", "http_requests_total"]
    }
  ],
  "meta": {
    "executedQueryString": "metrics query"
  }
}
```

Each item in the `fields` array corresponds to a column, with all row values for that column in the `values` array. The possible field types are:

| Type | Description |
| - | - |
| `time` | Timestamp values. |
| `string` | Text values. |
| `number` | Numeric values. |
| `boolean` | Boolean values. |
| `other` | Complex types (maps, arrays). |

## Examples

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
      "values": ["error", "error"]
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
        "abc12345-6789-def0-1234-56789abcdef0",
        "fed09876-5432-1abc-def0-123456789abc"
      ]
    }
  ],
  "meta": {
    "executedQueryString": "logs query"
  }
}
```

### Searching logs by pattern with the LIKE operator

Find logs containing a specific substring in the `data` field. This is useful for locating error messages, stack traces, or any text pattern across your logs.

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
      "values": [
        "{\"message\":\"Redis connection timeout after 5000ms\",\"retries\":3}"
      ]
    }
  ],
  "meta": {
    "executedQueryString": "logs query"
  }
}
```

### Filtering logs with the IN operator

Retrieve logs matching multiple log levels at once. The `IN` operator lets you match a column value against a list.

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
      "value": ["warn", "error"]
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
      "values": ["error", "warn", "warn"]
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

### Filtering metrics with the BETWEEN operator

Query metric counts that fall within a specific numeric range. The `BETWEEN` operator takes a two-element array `[min, max]`.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/metrics/{accountName}/query`

**Request body:**

```json
{
  "columns": [
    "TimestampTime",
    "MetricName",
    "app",
    "Count"
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
      "column": "MetricName",
      "operator": "=",
      "type": "string",
      "value": "http_client_requests_total"
    },
    {
      "column": "Count",
      "operator": "BETWEEN",
      "type": "number",
      "value": [100, 500]
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
        "2025-01-15T10:01:00Z"
      ]
    },
    {
      "name": "MetricName",
      "type": "string",
      "values": [
        "http_client_requests_total",
        "http_client_requests_total"
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
      "values": [245, 312]
    }
  ],
  "meta": {
    "executedQueryString": "metrics query"
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
      "name": "Attributes['status_code']",
      "type": "string",
      "values": ["200", "500", "200"]
    },
    {
      "name": "Attributes['method']",
      "type": "string",
      "values": ["GET", "POST", "GET"]
    },
    {
      "name": "Sum",
      "type": "number",
      "values": [1520, 3, 1489]
    }
  ],
  "meta": {
    "executedQueryString": "metrics query"
  }
}
```

### Aggregating metrics with group by

Calculate aggregated statistics over time. This example computes the average and maximum response duration grouped by minute and app using the `aggregations` and `group_by` fields.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/metrics/{accountName}/query`

**Request body:**

```json
{
  "page": 1,
  "pageSize": 100,
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
      "value": "http_server_request_duration"
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
    },
    {
      "function": "max",
      "column": "Value",
      "alias": "max_duration"
    }
  ],
  "group_by": {
    "columns": ["TimestampTime", "app"]
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
      "name": "avg_duration",
      "type": "number",
      "values": [0.245, 0.312, 0.198]
    },
    {
      "name": "max_duration",
      "type": "number",
      "values": [1.876, 2.541, 0.943]
    }
  ],
  "meta": {
    "executedQueryString": "metrics query"
  }
}
```

### Summing counter metrics with group by

Calculate total request counts grouped by metric name using the `sum` aggregation. This is suitable for counter-type (`sum`) metrics such as request totals.

**Endpoint:** `POST` `https://{accountName}.vtexcommercebeta.com.br/api/extensions/observability/metrics/{accountName}/query`

**Request body:**

```json
{
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
      "values": [58320, 42150, 15780]
    },
    {
      "name": "total_count",
      "type": "number",
      "values": [58320, 42150, 15780]
    }
  ],
  "meta": {
    "executedQueryString": "metrics query"
  }
}
```

### Using direct merge functions in columns

For advanced use cases, you can use ClickHouse merge functions directly in the `columns` array instead of the `aggregations` field. This gives you more explicit control over how pre-aggregated metric data is merged.

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
  "pageSize": 100,
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
      "values": [892, 1045, 763]
    },
    {
      "name": "average",
      "type": "number",
      "values": [0.342, 0.401, 0.289]
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
        "http_server_request_duration",
        "http_server_request_duration"
      ]
    },
    {
      "name": "MetricType",
      "type": "string",
      "values": ["histogram", "histogram"]
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
      "values": [1523, 1487]
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
      "column": "production",
      "operator": "=",
      "type": "boolean",
      "value": true
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
      "values": [
        "{\"message\":\"Payment gateway returned HTTP 503\",\"gateway\":\"braintree\"}"
      ]
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
      "values": ["error", "error"]
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

- **Always filter by time:** Include `TimestampTime` filters to limit the amount of data scanned in every query.
- **Be specific with filters:** Filter by `app` and `MetricName` whenever possible to narrow results efficiently.
- **Request only needed columns:** Specify only the columns you need in the `columns` array instead of returning all columns.
- **Paginate large results:** Use `page` and `pageSize` to fetch results in manageable chunks instead of requesting large datasets at once.
- **Match aggregation columns to metric types:** Use the `Sum` column for counter and histogram metrics and the `Value` column for gauge metrics.

## Data retention

Logs and metrics are retained for three days. To request higher limits for your account, contact [VTEX Support](https://help.vtex.com/en/support).

>ℹ️ Metrics are pre-aggregated to 1-minute intervals for efficient storage and querying.

## Error codes

The following errors may appear as a message in the response body.

### 400 - Bad Request

- **Message error example**: `"invalid request body"`. The JSON in the request body is malformed or contains invalid fields.

    ```json
    {
      "error": {
        "message": "invalid request body",
        "code": 400
      },
      "timestamp": "2025-01-15T10:00:00Z"
    }
    ```

- **Message error example**: `"column 'X' is not allowed"`. The specified column does not exist or is not available for the query type.

    ```json
    {
      "error": {
        "message": "column 'invalidColumn' is not allowed",
        "code": 400
      },
      "timestamp": "2025-01-15T10:00:00Z"
    }
    ```

### 401 - Unauthorized

- **Message error example**: `"Missing app key or token"`. The authentication headers are missing from the request.

    ```json
    {
      "error": {
        "message": "Missing app key or token",
        "code": 401
      },
      "timestamp": "2025-01-15T10:00:00Z"
    }
    ```

- **Message error example**: `"Invalid token"`. The provided application key or token is incorrect.

    ```json
    {
      "error": {
        "message": "Invalid token",
        "code": 401
      },
      "timestamp": "2025-01-15T10:00:00Z"
    }
    ```

### 403 - Forbidden

**Message error example**: `"Tenant in URL path does not match authenticated tenant"`. The `{accountName}` in the application key does not match the `tenant` in the request URL.

```json
{
  "error": {
    "message": "Tenant in URL path does not match authenticated tenant",
    "code": 403
  },
  "timestamp": "2025-01-15T10:00:00Z"
}
```

### 408 - Request Timeout

**Message error example**: `"Query timeout"`. The query exceeded the 30-second timeout. Try narrowing your filters or reducing the time range.

```json
{
  "error": {
    "message": "Query timeout",
    "code": 408
  },
  "timestamp": "2025-01-15T10:00:00Z"
}
```

### 429 - Too Many Requests

**Message error example**: `"quota exceeded"`. You have exceeded the rate limit for your account. Wait before retrying or contact VTEX support to upgrade your plan.

```json
{
  "error": {
    "message": "quota exceeded",
    "code": 429
  },
  "timestamp": "2025-01-15T10:00:00Z"
}
```
