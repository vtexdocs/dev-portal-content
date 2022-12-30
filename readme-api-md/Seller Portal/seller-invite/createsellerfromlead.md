---
title: "Create Seller From Lead"
slug: "createsellerfromlead"
excerpt: "This endpoint is used by marketplace operators to Create Seller Portal accounts. The request will only accept Seller Leads whose status is `accepted`. If they are already `connected` or `invited`, the call will not be fulfilled. \n\nThe creation of the account at VTEX is done by an internal Billing service. There is no Seller Portal account and marketplace affiliation if you do not go through this step. \n\nNote that there's no specific API call that allows status changes. The operations only allow the seller lead to move forward: \n\n From `invite` > to `Accept` > closing on `Create Seller`.  \n\nIf you want to change the status, you can start the process again, by deleting that lead through the *Delete Seller Lead* endpoint, and resending the invite through the *Resend Seller Lead's Invite* endpoint."
hidden: true
createdAt: "2021-04-28T18:30:37.177Z"
updatedAt: "2021-04-28T18:30:37.177Z"
---
