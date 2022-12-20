---
slug: "new-sku-service-endpoints"
title: "New SKU Service endpoints"
createdAt: 2020-06-05T15:39:43.412Z
hidden: false
type: "added"
---

SKU Service actions can now be accessed using the [Catalog API](https://developers.vtex.com/reference/catalog-api-overview), allowing you to create and edit SKU Service types, values and attachments. These are the new endpoints:

- [[POST] Create SKU Service Type](https://developers.vtex.com/reference/sku-service#post_api-catalog-pvt-skuservicetype)
- [[PUT] Update SKU Service Type](https://developers.vtex.com/reference/sku-service#put_api-catalog-pvt-skuservicetype-skuservicetypeid)
- [[DELETE] Delete SKU Service Type](https://developers.vtex.com/reference/sku-service#delete_api-catalog-pvt-skuservicetype-skuservicetypeid)
- [[POST] Create SKU Service Value](https://developers.vtex.com/reference/sku-service#post_api-catalog-pvt-skuservicevalue)
- [[PUT] Update SKU Service Value](https://developers.vtex.com/reference/sku-service#put_api-catalog-pvt-skuservicevalue-skuservicevalueid)
- [[DELETE] Delete SKU Service Value](https://developers.vtex.com/reference/sku-service#delete_api-catalog-pvt-skuservicevalue-skuservicevalueid)
- [[POST] Associate SKU Service Attachment](https://developers.vtex.com/reference/sku-service#post_api-catalog-pvt-skuservicetypeattachment)
- [[DELETE] Dissociate Attachment from SKU Service Type](https://developers.vtex.com/reference/sku-service#delete_api-catalog-pvt-skuservicetypeattachment-skuservicetypeattachmentid)
- [[DELETE] Dissociate Attachment by Attachment ID or SKU Service Type ID](https://developers.vtex.com/reference/sku-service#delete_api-catalog-pvt-skuservicetypeattachment)
- [[POST] Associate SKU Service](https://developers.vtex.com/reference/sku-service#post_api-catalog-pvt-skuservice)
- [[PUT] Update SKU Service](https://developers.vtex.com/reference/sku-service#post_api-catalog-pvt-skuservice-skuserviceid)
- [[DELETE] Dissociate SKU Service](https://developers.vtex.com/reference/sku-service#delete_api-catalog-pvt-skuservice-skuserviceid)

This means the following [Webservice](https://assets.ctfassets.net/alneenqid6w5/4OdeCFbcVQtEgkuWsuuidl/80b79448cf2b327e07b567a8411afaa0/vtex_WebServiceGuide.pdf) methods have been incorporated into the Catalog API:

- StockKeepingUnitServiceGet
- StockKeepingUnitServiceInsertUpdate
- StockKeepingUnitServiceList
