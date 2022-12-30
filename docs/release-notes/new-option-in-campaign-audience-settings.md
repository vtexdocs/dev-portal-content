---
title: "New option in Campaign Audience settings"
slug: "new-option-in-campaign-audience-settings"
type: "added"
createdAt: "2022-07-22T13:48:52.370Z"
hidden: false
excerpt: "It is now possible to use multiple target audiences in a [campaign audience](https://help.vtex.com/en/tutorial/campaign-audiences--3o7lhpNseXY2WmjZO0gQ6m) simultaneously, instead of applying either one target audience or another, when using the Promotions & Taxes API."
---
It is now possible to use multiple target audiences in a [campaign audience](https://help.vtex.com/en/tutorial/campaign-audiences--3o7lhpNseXY2WmjZO0gQ6m) simultaneously, instead of applying either one target audience or another, when using the Promotions & Taxes API.

Previously it was only possible to use the “or” operator in this scenario, which means a campaign audience would be composed of customers that fit any of the selected target audiences.

Now you can choose to use the “and” operator instead, if you wish to restrict the campaign audience to customers who fit both or more defined target audiences. Choosing “and” will combine the criteria set for more than one target audience.

To make this possible, we have added the following property to Campaign Audience endpoints:

|Field|Type|Description|Endpoints|
|-----|----|-----------|---------|
|`isAndOperator`|boolean|When `true`, it determines that all the `targetConfigurations` need to be valid for the campaign audience to be active.\n\nWhen `false`, it determines that if at least one of the `targetConfigurations` is valid, the campaign audience will be active.| <ul><li>get [Get campaign audience configuration](https://developers.vtex.com/vtex-rest-api/reference/getcampaignconfiguration)</li> <li>get [Get all campaign audiences](https://developers.vtex.com/vtex-rest-api/reference/getcampaignaudiences)</li> <li>post [Create campaign audience](https://developers.vtex.com/vtex-rest-api/reference/setcampaignconfiguration)</li></ul>

We have also updated the VTEX Admin **Campaign Audiences** interface to include this option. Read our Help Center [announcement](https://help.vtex.com/en/announcements/campaign-promotions-new-option-when-configuring-target-audience--UJOyf1nYJ0xHXl88RytJ5) and our user documentation [Creating a campaign audience](https://help.vtex.com/en/tutorial/creating-campaign-audiences--6cnuDZJzIkIeocewAQQK4K) to find out more.
