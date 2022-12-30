---
title: "Get Product Indexed Information"
slug: "catalog-api-get-product-indexed"
excerpt: "Retrieve details of a Product's Indexed Information in XML format. \r\n## Response body example\r\n\r\n```xml\r\n\"\r\n<?xml version=\\\"1.0\\\" encoding=\\\"UTF-8\\\"?>\\n\r\n<response>\\n\r\n    <lst name=\\\"responseHeader\\\">\r\n        <bool name=\\\"zkConnected\\\">true</bool>\r\n        <int name=\\\"status\\\">0</int>\r\n        <int name=\\\"QTime\\\">2</int>\r\n        <lst name=\\\"params\\\">\r\n            <str name=\\\"fl\\\">*</str>\r\n            <arr name=\\\"fq\\\">\r\n                <str>instanceId:394dbdc8-b1f4-4dea-adfa-1ec104f3bfe1</str>\r\n                <str>productId:1</str>\r\n            </arr>\r\n        </lst>\r\n    </lst>\r\n    <result name=\\\"response\\\" numFound=\\\"0\\\" start=\\\"0\\\" maxScore=\\\"0.0\\\"></result>\r\n    <lst name=\\\"facet_counts\\\">\r\n        <lst name=\\\"facet_queries\\\"/>\r\n        <lst name=\\\"facet_fields\\\"/>\r\n        <lst name=\\\"facet_ranges\\\"/>\r\n        <lst name=\\\"facet_intervals\\\"/>\r\n        <lst name=\\\"facet_heatmaps\\\"/></lst>\\n\r\n</response>\\n\"\r\n```"
hidden: false
createdAt: "2020-02-05T23:07:29.210Z"
updatedAt: "2022-12-02T21:20:29.542Z"
---
