---
title: "Data residency"
slug: "data-residency"
hidden: true
createdAt: "2023-05-16T09:38:36.446Z"
updatedAt: "2023-05-16T09:38:36.446Z"
---
The VTEX data residency feature enables stores to select the specific geographic region where their shoppers' information is stored.

When your VTEX account is created under the PII data architecture, you may choose your residency location from two available options:
- **AWS us-east-1:** located in Virginia, USA.
- **AWS eu-west-1:** located in Ireland.

This feature applies to all data saved in the [Profile System](https://developers.vtex.com/docs/guides/profile-system), such as name, email, and shipping address, among others. 

>ℹ️ Learn more about the [PII data architecture](https://developers.vtex.com/docs/guides/pii-data-architecture)

There are two instances of the [Profile System](https://developers.vtex.com/docs/guides/profile-system) running in parallel, each based in different locations: US (Virginia) and EU (Ireland). These instances are identical in terms of their functioning. However, each instance only holds and processes data associated with stores that selected that location as their accounts' PII data residency.

In practice, when data is requested from the [Profile System](https://developers.vtex.com/docs/guides/profile-system), the VTEX edge layer directs the request to the appropriate Profile System location based on the data residency location selected by the account.

```mermaid
%%{ init: { 'flowchart': { 'curve': 'linear' } } }%%
flowchart LR
    subgraph us [AWS us-east-1]
        A[VTEX service] --> B[Router]
        B -->C(Storage entity)
        C -->E[(Database)]
    end
    style us fill:#FFFFFF
    subgraph eu [AWS eu-west-1]
        D -->F[(Database)]
    end
    style eu fill:#FFFFFF
        B -->D(Storage entity)
```

>ℹ️ The [Profile System](https://developers.vtex.com/docs/guides/profile-system) is the VTEX module responsible for keeping Shopper Profile PII at rest.
