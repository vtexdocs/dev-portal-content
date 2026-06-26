---
title: "Exporting ads reports"
slug: "exporting-ads-reports"
excerpt: "Access and download platform data automatically through API endpoints with JSON or XLSX export options."
hidden: false
createdAt: "2026-06-18T00:00:00.000Z"
updatedAt: "2026-06-18T00:00:00.000Z"
---
Report export allows you to access and download platform information automatically, without the need for manual extraction through the interface. All report routes return data in JSON format by default, but can be exported as XLSX files by including the `download=true` parameter in the query.

> ℹ️ API Authentication
> To access the endpoints, users must be authenticated. See the [VTEX Ads API overview](https://developers.vtex.com/docs/api-reference/vtex-ads-api) for more details.

> ⚠️ Limited availability of some reports
> Export of certain reports may be restricted based on the account type associated with the authentication. Not all users will have access to all available reports.

## Reports

### Advertisers

This endpoint allows you to search for information from all advertisers associated with a publisher account. Data is returned in JSON format by default, but can be exported as XLSX by adding the `download=true` parameter to the query string.

> ℹ️ Only available in publisher view.

#### Request

```http
GET https://api-retail-media.newtail.com.br/report/v2/advertisers?start_date=2025-01-01&end_date=2025-01-01 HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>
```

For the query parameters and response schema, see [Get advertisers report](https://developers.vtex.com/docs/api-reference/vtex-ads-api#get-/report/v2/advertisers) in the API Reference.

### Publishers

This endpoint allows you to search for publisher information. Data is returned in JSON format by default, but can be exported as XLSX by including the `download=true` parameter in the query string.

> ℹ️ Only available in advertiser view.

#### Request

```http
GET https://api-retail-media.newtail.com.br/report/v2/publishers?start_date=2025-01-01&end_date=2025-01-01 HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>
```

For the query parameters and response schema, see [Get publishers report](https://developers.vtex.com/docs/api-reference/vtex-ads-api#get-/report/v2/publishers) in the API Reference.

### Network publishers

This endpoint allows you to search for information about publishers associated with a **Network** type Publisher account. Data is returned in JSON format by default, but can be exported as XLSX by including the `download=true` parameter in the query string.

> ℹ️ Only publishers operating in Network format have permission to access this report.

#### Request

```http
GET https://api-retail-media.newtail.com.br/report/network/publishers?start_date=2025-01-01&end_date=2025-01-01 HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>
```

For the query parameters and response schema, see [Get network publishers report](https://developers.vtex.com/docs/api-reference/vtex-ads-api#get-/report/network/publishers) in the API Reference.

### Campaigns

This endpoint allows you to search for all available campaigns, applying filters as needed. Data is returned in JSON format by default, but can be exported as XLSX by including the `download=true` parameter in the query string.

#### Request

```http
GET https://api-retail-media.newtail.com.br/campaign/v2?start_date=2025-01-01&end_date=2025-01-01 HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>
```

For the query parameters and response schema, see [List campaigns](https://developers.vtex.com/docs/api-reference/vtex-ads-api#get-/campaign/v2) in the API Reference.

### Ads

This endpoint allows you to search for all available ads, applying filters as needed. Data is returned in JSON format by default, but can be exported as XLSX by including the `download=true` parameter in the query string.

#### Request

```http
GET https://api-retail-media.newtail.com.br/ad/results/v2?start_date=2025-01-01&end_date=2025-01-01 HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>
```

For the query parameters and response schema, see [Get ads performance report](https://developers.vtex.com/docs/api-reference/vtex-ads-api#get-/ad/results/v2) in the API Reference.
