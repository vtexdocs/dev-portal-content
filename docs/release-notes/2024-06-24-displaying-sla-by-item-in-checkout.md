---
title: "Enhanced shipping estimate display in Checkout"
slug: "2024-06-24-displaying-sla-by-item-in-checkout"
type: "added"
hidden: true
createdAt: ""
updatedAt: ""
excerpt: "Introducing the useIndividualShippingEstimates variable in the Checkout API to display specific shipping dates for each item in the cart."
---

To enhance the customer experience, we have introduced a new feature in the [Checkout API](https://developers.vtex.com/docs/api-reference/checkout-api). The addition of the `useIndividualShippingEstimates` variable allows for displaying precise shipping estimates for each item in the customer's cart. This feature populates the `shippingEstimateDate` with a specific delivery date, such as `"2023-07-12T14:52:00+00:00"`, instead of just providing an estimate in business days.

For detailed instructions on implementing this feature, please refer to the [Displaying SLA by item in Checkout](https://developers.vtex.com/docs/guides/displaying-sla-by-item-in-checkout) guide.
