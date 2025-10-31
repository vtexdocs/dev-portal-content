---
title: "Exporting ads events"
slug: "exporting-ads-events"
excerpt: "Export raw advertising event data including impressions, clicks, views, and conversions for detailed analysis."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2025-10-14T00:00:00.000Z"
---
Event data export enables systematic and periodic integration of raw advertising events for detailed analysis and custom reporting.

## Integration connection

See more about the connection in [Exporting data from VTEX Ads](https://developers.vtex.com/docs/guides/exporting-data-from-vtex-ads).

## Integration format

- Data sent is always D-1 (previous day)
- Files are in [Parquet](https://parquet.apache.org/docs/overview/) format with [Snappy](https://parquet.apache.org/docs/file-format/data-pages/compression/) compression
- Files are always sent in a daily path format: `TYPE_REPORT/YYYY/MM/DD/TIMESTAMP_NS/RANDOM_FILE_NAMES.snappy.parquet` (one or more files may be sent)

> 🚧 Event deduplication
> 
> All events are guaranteed to be sent, but there is no guarantee that an event will be sent only once. Therefore, events must always be deduplicated.

## Event data

### Impressions

| Attribute      | Type          | Description                                                     |
| :------------- | :------------ | :-------------------------------------------------------------- |
| event_id       | String        | Unique event identifier **(deduplication key)**                 |
| session_id     | String        | Unique user session identifier                                  |
| user_id        | String        | Unique user identifier                                          |
| ad_id          | String        | Advertisement identifier                                        |
| campaign_id    | String        | Unique campaign identifier                                      |
| request_id     | String        | Unique ad query request identifier                              |
| ad_type        | String        | Type of advertisement that generated the event                  |
| placement_name | String        | Name of the placement where the ad was displayed                |
| context        | String        | Context in which the ad was displayed                           |
| created_at     | Timestamp UTC | Timestamp of when the event occurred                            |
| site           | String        | Site brand identifier                                           |

### Views

| Attribute      | Type          | Description                                                     |
| :------------- | :------------ | :-------------------------------------------------------------- |
| event_id       | String        | Unique event identifier **(deduplication key)**                 |
| session_id     | String        | Unique user session identifier                                  |
| user_id        | String        | Unique user identifier                                          |
| ad_id          | String        | Advertisement identifier                                        |
| campaign_id    | String        | Unique campaign identifier                                      |
| request_id     | String        | Unique ad query request identifier                              |
| ad_type        | String        | Type of advertisement that generated the event                  |
| placement_name | String        | Name of the placement where the ad was displayed                |
| context        | String        | Context in which the ad was displayed                           |
| created_at     | Timestamp UTC | Timestamp of when the event occurred                            |
| site           | String        | Site brand identifier                                           |

### Clicks

| Attribute      | Type          | Description                                                     |
| :------------- | :------------ | :-------------------------------------------------------------- |
| event_id       | String        | Unique event identifier **(deduplication key)**                 |
| session_id     | String        | Unique user session identifier                                  |
| user_id        | String        | Unique user identifier                                          |
| ad_id          | String        | Advertisement identifier                                        |
| campaign_id    | String        | Unique campaign identifier                                      |
| request_id     | String        | Unique ad query request identifier                              |
| ad_type        | String        | Type of advertisement that generated the event                  |
| placement_name | String        | Name of the placement where the ad was displayed                |
| context        | String        | Context in which the ad was displayed                           |
| created_at     | Timestamp UTC | Timestamp of when the event occurred                            |
| site           | String        | Site brand identifier                                           |

### Conversions

| Attribute  | Type          | Description                                            |
| :--------- | :------------ | :----------------------------------------------------- |
| event_id   | String        | Unique conversion event identifier                     |
| session_id | String        | Unique user session identifier                         |
| user_id    | String        | Unique user identifier                                 |
| order_id   | String        | Unique retail order identifier **(deduplication key)** |
| channel    | String        | Channel identifier                                     |
| placed_at  | Timestamp UTC | Order timestamp                                        |
| site       | String        | Site brand identifier                                  |

### Conversion items

| Attribute         | Type      | Description                                                     |
| :---------------- | :-------- | :-------------------------------------------------------------- |
| event_id          | String    | Unique identifier of the event that generated the conversion (view or click) |
| session_id        | String    | Unique user session identifier                                  |
| user_id           | String    | Unique user identifier                                          |
| order_id          | String    | Unique retail order identifier **(deduplication key)**          |
| product_sku       | String    | Product identifier **(deduplication key)**                      |
| ad_id             | String    | Unique advertisement identifier                                 |
| campaign_id       | String    | Unique campaign identifier                                      |
| request_id        | String    | Unique ad query request identifier                              |
| ad_size           | String    | Size of the media used in the advertisement                     |
| ad_type           | String    | Type of advertisement that generated the conversion             |
| placement_name    | String    | Name of the placement where the ad was displayed                |
| context           | String    | Context in which the ad was displayed                           |
| event_created_at  | Timestamp | Timestamp of when the event occurred                            |
| price             | Float     | Product price (regular)                                         |
| promotional_price | Float     | Product promotional price                                       |
| quantity          | Int       | Quantity of items sold                                          |
| total_value       | Float     | Total item value (quantity * min(price, promotional_price))     |
