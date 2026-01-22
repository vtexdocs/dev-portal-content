---
title: "Exporting aggregated data from VTEX Ads"
slug: "exporting-aggregated-data-from-vtex-ads"
excerpt: "Export pre-processed performance metrics and campaign statistics for business intelligence and reporting purposes."
hidden: false
createdAt: "2025-10-13T00:00:00.000Z"
updatedAt: "2025-10-14T00:00:00.000Z"
---
Aggregated data export enables systematic and periodic integration of pre-processed advertising performance metrics for business intelligence and reporting purposes.

## Integration connection

See more about the connection in [Exporting data from VTEX Ads](https://developers.vtex.com/docs/guides/exporting-data-from-vtex-ads).

## Integration format

- Data sent is always D-1 (previous day)
- Data is always sent D-1 with the publisher's timezone
- Files are sent in CSV format:
  - UTF-8 encoding
  - Comma-separated values
  - All numbers follow American format with decimal point (".")
- Files are always sent in a daily path format: `TYPE_REPORT/YYYY/MM/DD/TIMESTAMP_NS/RANDOM_FILE_NAMES.csv` (one or more files may be sent)

## Data to be exported

> 📘 File examples
> 
> Examples of files that will be sent:
> 
> <https://cdn.newtail.com.br/retail-media/docs/export-reports/ads.csv>  
> <https://cdn.newtail.com.br/retail-media/docs/export-reports/campaigns.csv>  
> <https://cdn.newtail.com.br/retail-media/docs/export-reports/advertisers.csv>

### Advertisers

`advertisers/YYYY/MM/DD/CURRENT_DELIVERY_TIME/RANDOM_FILE_NAME.csv`

| Column         | Type   | Description                                              |
| :------------- | :----- | :------------------------------------------------------- |
| advertiser     | String | Advertiser name                                          |
| advertiser_id  | String | Unique advertiser identifier                             |
| seller_id      | String | Seller identifier                                        |
| wallet_balance | Float  | Current balance in the advertiser's wallet               |
| daily_budget   | Float  | Total daily budget sum of all active campaigns          |
| currency       | String | Currency format the advertiser is operating in (e.g., BRL, USD) |

### Campaigns

`campaigns/YYYY/MM/DD/CURRENT_DELIVERY_TIME/RANDOM_FILE_NAME.csv`

| Column            | Type              | Description                                              |
| :---------------- | :---------------- | :------------------------------------------------------- |
| day               | date YYYY-DD-MM   | Day is always sent in the publisher's timezone          |
| name              | String            | Campaign name                                            |
| campaign_id       | String            | Unique campaign identifier                               |
| campaign_type     | String            | Campaign type: `product`, `banner`, `sponsored_brands`, `video` |
| campaign_status   | String            | Campaign operating status                                |
| impressions_total | int               | Total impressions                                        |
| clicks_total      | int               | Total clicks                                             |
| ctr               | float             | Campaign CTR                                             |
| ad_revenue        | Float             | Ad revenue                                               |
| conversions_total | int               | Total conversions                                        |
| conversion_rate   | float             | Order conversion rate                                    |
| sales_revenue     | float             | Revenue from sold items                                  |
| start_date        | date YYYY-DD-MM   | Campaign start date                                      |
| end_date          | date YYYY-DD-MM   | Campaign end date                                        |
| advertiser_id     | String            | Unique advertiser identifier                             |

### Ads

`ads/YYYY/MM/DD/CURRENT_DELIVERY_TIME/RANDOM_FILE_NAME.csv`

| Column            | Type              | Description                                              |
| :---------------- | :---------------- | :------------------------------------------------------- |
| day               | date YYYY-DD-MM   | Day is always sent in the publisher's timezone          |
| ad_id             | String            | Unique ad identifier                                     |
| campaign_id       | String            | Unique campaign identifier                               |
| ad_status         | String            | Ad operating status                                      |
| ad_media_url      | String            | Ad media URL                                             |
| cpm               | float             | CPM value                                                |
| cpc               | float             | CPC value                                                |
| impressions_total | int               | Total impressions                                        |
| clicks_total      | int               | Total clicks                                             |
| ctr               | float             | Ad CTR                                                   |
| ad_revenue        | float             | Ad revenue                                               |
| conversions_total | int               | Total conversions generated by the ad                    |
| conversion_rate   | float             | Conversion rate                                          |
| sales_revenue     | float             | Revenue from product sales                               |
| product_sku       | String            | List of SKUs separated by semicolon. Note: Product campaigns always have only 1 product per ad |

### Product ads

`product_ads/YYYY/MM/DD/CURRENT_DELIVERY_TIME/RANDOM_FILE_NAME.csv`

| Column            | Type              | Description                                              |
| :---------------- | :---------------- | :------------------------------------------------------- |
| day               | date YYYY-DD-MM   | Day is always sent in the publisher's timezone          |
| ad_id             | String            | Unique ad identifier                                     |
| campaign_id       | String            | Unique campaign identifier                               |
| advertiser_id     | String            | Unique advertiser identifier                             |
| product_sku       | String            | Product SKU                                              |
| ad_type           | String            | Ad type                                                  |
| ad_media_url      | String            | Ad media URL                                             |
| cpm               | float             | CPM value                                                |
| cpc               | float             | CPC value                                                |
| impressions_total | int               | Total impressions                                        |
| clicks_total      | int               | Total clicks                                             |
| ctr               | float             | Ad CTR                                                   |
| ad_revenue        | float             | Ad revenue                                               |
| conversions_total | int               | Total conversions generated by the ad                    |
| conversion_rate   | float             | Conversion rate                                          |
| sales_revenue     | float             | Revenue from product sales                               |

### Catalog

`catalog/YYYY/MM/DD/CURRENT_DELIVERY_TIME/RANDOM_FILE_NAME.csv`

| Column      | Type   | Description                                              |
| :---------- | :----- | :------------------------------------------------------- |
| product_sku | String | Product SKU                                              |
| name        | String | Product name                                             |
| categories  | String | List of product categories separated by semicolon (e.g., Cat1 > Cat2; ...) |
| image_url   | String | Product image URL                                        |
