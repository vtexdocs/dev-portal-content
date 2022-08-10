---
title: "Policy Engine API - Overview"
slug: "policy-engine-api-overview"
hidden: false
createdAt: "2021-05-05T15:16:38.051Z"
updatedAt: "2022-02-07T20:48:00.755Z"
---
This API will create promotion alarms when selling products with undesired prices and promotions. It will create conditions that will check if the prices and the promotions are correct. If not, the system will alarm the store with information about the product sold at unexpected prices.
[block:api-header]
{
  "title": "Index"
}
[/block]
<span class="api"><span class="pg-type type-get">get</span> [Get Policy List](SkuServiceTypeId)
<span class="api"><span class="pg-type type-post">post</span> [Evaluate Policies](https://developers.vtex.com/vtex-rest-api/reference/policy_evaluate)
<span class="api"><span class="pg-type type-get">get</span> [Get Policy by ID](https://developers.vtex.com/vtex-rest-api/reference/policy_get)
<span class="api"><span class="pg-type type-post">post</span> [Create Policy](https://developers.vtex.com/vtex-rest-api/reference/policy_createorupdate)
<span class="api"><span class="pg-type type-put">put</span> [Update Policy](https://developers.vtex.com/vtex-rest-api/reference/put_api-policy-engine-policies-id)
<span class="api"><span class="pg-type type-delete">delete</span> [Delete Policy by ID](https://developers.vtex.com/vtex-rest-api/reference/policy_delete)