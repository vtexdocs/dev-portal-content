---
title: "Exporting ads reports"
slug: "exporting-ads-reports"
excerpt: "Access and download platform data automatically through API endpoints with JSON or XLSX export options."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2025-10-14T00:00:00.000Z"
---
Report export allows you to access and download platform information automatically, without the need for manual extraction through the interface. All report routes return data in JSON format by default, but can be exported as XLSX files by including the `download=true` parameter in the query.

> ℹ️ API Authentication
> 
> To access the routes, users must be authenticated. See the [authentication documentation](https://newtail-media.readme.io/reference/autenticacao) for more details.

> ⚠️ Limited availability of some reports
> 
> Export of certain reports may be restricted based on the account type associated with the authentication. Not all users will have access to all available reports.

## Reports

### Advertisers

This endpoint allows you to search for information from all advertisers associated with a publisher account. Data is returned in JSON format by default, but can be exported as XLSX by adding the `download=true` parameter to the query string.

> ℹ️ Only available in publisher view.

#### Request

```
GET https://api-retail-media.newtail.com.br/report/v2/advertisers?start_date=2025-01-01&end_date=2025-01-01 HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>
```

#### Query parameters

| Parameter    | Required | Description                                                                       |
| :----------- | :------- | :-------------------------------------------------------------------------------- |
| start_date   | Yes      | Metrics start date in `YYYY-MM-DD` format                                        |
| end_date     | Yes      | Metrics end date in `YYYY-MM-DD` format                                          |
| account_info | No       | If true, includes detailed account information in the result. Default is `false` |
| page         | No       | Page number of results. Default is `1`                                           |
| quantity     | No       | Number of items per page. Default is `100`                                       |
| count        | No       | If `true`, returns the total number of available records. Default is `false`     |
| download     | No       | If `true`, returns an XLSX file buffer ready for download instead of JSON        |

### Publishers

This endpoint allows you to search for publisher information. Data is returned in JSON format by default, but can be exported as XLSX by including the `download=true` parameter in the query string.

> ℹ️ Only available in advertiser view.

#### Request

```
GET https://api-retail-media.newtail.com.br/report/v2/publishers?start_date=2025-01-01&end_date=2025-01-01 HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>
```

#### Query parameters

| Parameter       | Required | Description                                                                                                                                                                                              |
| :-------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start_date      | Yes      | Metrics start date in `YYYY-MM-DD` format                                                                                                                                                               |
| end_date        | Yes      | Metrics end date in `YYYY-MM-DD` format                                                                                                                                                                 |
| publisher_name  | No       | Filters results by publisher name                                                                                                                                                                        |
| account_info    | No       | If true, includes detailed account information in the result. Default is `false`                                                                                                                         |
| page            | No       | Page number of results. Default is `1`                                                                                                                                                                  |
| quantity        | No       | Number of items per page. Default is `100`                                                                                                                                                              |
| count           | No       | If `true`, returns the total number of available records. Default is `false`                                                                                                                            |
| order_by        | No       | Defines the field for sorting results. Possible values: `name, balance, total_daily_budget, total_campaigns, impressions, clicks, ctr, total_spent, conversions, conversion_rate, income, roas`      |
| order_direction | No       | Defines the sorting direction. Possible values: `asc` (ascending) or `desc` (descending)                                                                                                                |
| download        | No       | If `true`, returns an XLSX file buffer ready for download instead of JSON                                                                                                                                |

### Network publishers

This endpoint allows you to search for information about publishers associated with a **Network** type Publisher account. Data is returned in JSON format by default, but can be exported as XLSX by including the `download=true` parameter in the query string.

> ℹ️ Only publishers operating in Network format have permission to access this report.

#### Request

```
GET https://api-retail-media.newtail.com.br/report/network/publishers?start_date=2025-01-01&end_date=2025-01-01 HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>
```

#### Query parameters

| Parameter       | Required | Description                                                                                                                                              |
| :-------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start_date      | Yes      | Metrics start date in `YYYY-MM-DD` format                                                                                                               |
| end_date        | Yes      | Metrics end date in `YYYY-MM-DD` format                                                                                                                 |
| publisher_name  | No       | Filters results by publisher name                                                                                                                        |
| account_info    | No       | If true, includes detailed account information in the result. Default is `false`                                                                         |
| page            | No       | Page number of results. Default is `1`                                                                                                                  |
| quantity        | No       | Number of items per page. Default is `100`                                                                                                              |
| count           | No       | If `true`, returns the total number of available records. Default is `false`                                                                            |
| order_by        | No       | Defines the field for sorting results. Possible values: `name, impressions, clicks, ctr, conversions, conversion_rate, income, roas, requests`        |
| order_direction | No       | Defines the sorting direction. Possible values: `asc` (ascending) or `desc` (descending)                                                                |
| download        | No       | If `true`, returns an XLSX file buffer ready for download instead of JSON                                                                                |

### Campaigns

This endpoint allows you to search for all available campaigns, applying filters as needed. Data is returned in JSON format by default, but can be exported as XLSX by including the `download=true` parameter in the query string.

#### Request

```
GET https://api-retail-media.newtail.com.br/campaign/v2?start_date=2025-01-01&end_date=2025-01-01 HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>
```

#### Query parameters

| Parameter       | Required | Description                                                                                                                                                                                                        |
| :-------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start_date      | Yes      | Metrics start date in `YYYY-MM-DD` format                                                                                                                                                                         |
| end_date        | Yes      | Metrics end date in `YYYY-MM-DD` format                                                                                                                                                                           |
| status          | No       | Filters by campaign status                                                                                                                                                                                         |
| advertiser_id   | No       | Filters campaigns by advertiser ID                                                                                                                                                                                 |
| ad_type         | No       | Filters by ad type                                                                                                                                                                                                 |
| name            | No       | Searches campaigns by name                                                                                                                                                                                         |
| account_info    | No       | If true, includes detailed account information in the result. Default is `false`                                                                                                                                   |
| page            | No       | Page number of results. Default is `1`                                                                                                                                                                            |
| quantity        | No       | Number of items per page. Default is `100`                                                                                                                                                                        |
| count           | No       | If `true`, returns the total number of available records. Default is `false`                                                                                                                                      |
| order_by        | No       | Defines the field for sorting results. Possible values: `name, impressions, clicks, ctr, conversions, conversion_rate, income, roas, created_at, start_at, daily_budget, ad_type, advertiser_name, status`    |
| order_direction | No       | Defines the sorting direction. Possible values: `asc` (ascending) or `desc` (descending)                                                                                                                          |
| download        | No       | If `true`, returns an XLSX file buffer ready for download instead of JSON                                                                                                                                          |

### Ads

This endpoint allows you to search for all available ads, applying filters as needed. Data is returned in JSON format by default, but can be exported as XLSX by including the `download=true` parameter in the query string.

#### Request

```
GET https://api-retail-media.newtail.com.br/ad/results/v2?start_date=2025-01-01&end_date=2025-01-01 HTTP/1.1
accept: application/json
content-type: application/json
x-app-id: <PUBLISHER_APP_ID>
x-api-key: <API_KEY>
```

#### Query parameters

| Parameter       | Required | Description                                                                                                                                                                                      |
| :-------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start_date      | Yes      | Metrics start date in `YYYY-MM-DD` format                                                                                                                                                       |
| end_date        | Yes      | Metrics end date in `YYYY-MM-DD` format                                                                                                                                                         |
| campaign_name   | No       | Filters ads by campaign name                                                                                                                                                                     |
| campaign_id     | No       | Filters ads by campaign ID                                                                                                                                                                       |
| advertiser_id   | No       | Filters ads by advertiser ID                                                                                                                                                                     |
| product_sku     | No       | Filters ads by product SKU                                                                                                                                                                       |
| ad_status       | No       | Filters ads by status                                                                                                                                                                            |
| ad_type         | No       | Filters by ad type                                                                                                                                                                               |
| targeting_type  | No       | Filters by targeting type                                                                                                                                                                        |
| show_inactive   | No       | If `true`, includes paused ads                                                                                                                                                                   |
| account_info    | No       | If `true`, includes detailed account information in the result. Default is `false`                                                                                                               |
| page            | No       | Page number of results. Default is `1`                                                                                                                                                          |
| quantity        | No       | Number of items per page. Default is `100`                                                                                                                                                      |
| count           | No       | If `true`, returns the total number of available records. Default is `false`                                                                                                                    |
| order_by        | No       | Defines the field for sorting results. Possible values: `ad_type, ad_status, impressions, conversion_rate, ctr, income, total_spent, roas, conversions, total_conversions_item_quantity`     |
| order_direction | No       | Defines the sorting direction. Possible values: `asc` (ascending) or `desc` (descending)                                                                                                        |
| download        | No       | If `true`, returns an XLSX file buffer ready for download instead of JSON                                                                                                                        |
