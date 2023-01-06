# Change chain orders in external marketplaces

>ℹ️ This feature works exclusively for VTEX stores with **Multilevel Omnichannel Inventory** chain orders made in external marketplaces. The external marketplace must be responsible for the payment and be able to support the [Change order](https://developers.vtex.com/vtex-rest-api/docs/change-order) feature.

<br>

[Multilevel Omnichannel Inventory](https://developers.vtex.com/vtex-rest-api/docs/multilevel-omnichannel-inventory) is the VTEX setting that allows franchise accounts or white label sellers' inventory to be sold in marketplaces connected to the main account. This article explains how to use the [Change order](https://developers.vtex.com/vtex-rest-api/docs/change-order) while performing Multilevel Omnichannel Inventory operations in [external marketplaces](https://developers.vtex.com/vtex-rest-api/docs/external-marketplace-integration-guide).                                                                  

By configuring this feature, your VTEX store will be able to have orders' items or prices changed when selling products that belong to a franchise account in orders made in external marketplaces. This happens due to a new endpoint is created to receive change order’s notifications sent by a VTEX seller in a Multilevel Omnichannel Inventory operation. 

The image below shows how the process occurs, in more detail:

<br>
