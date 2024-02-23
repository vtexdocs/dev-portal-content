---
title: "Setting up the SPF"
slug: "setting-up-the-spf"
hidden: false
createdAt: "2021-05-19T19:35:16.057Z"
updatedAt: "2021-05-28T18:40:04.171Z"
---
The [SPF (Sender Policy Framework)](http://www.open-spf.org/Introduction/) is a standard that specifies how to prevent unauthorized servers from sending emails on behalf of your domain. This framework implements rules that verify if the server has a particular policy set up by the domain’s admin.

## Editing the SPF

To understand SPF syntax, we recommend reading [SPF Record Syntax](http://www.open-spf.org/SPF_Record_Syntax/).

VTEX uses `include:amazonses.com`, Amazon's transactional email sending service, used in the default sender of Message Center.

Here is an example of an SPF on VTEX:

```spf
v=spf1 include:server.com include:amazonses.com ~all
```

All `include` mechanisms should be set up to add a new SPF. See the example below to understand how to add `include:amazonses.com` if there is already another `include` mechanism:

| Before | After |
|-|-|
| `v=spf1 include:websitewelcome.com include:_spf.google.com ~all` | `v=spf1 include:websitewelcome.com include:_spf.google.com include:amazonses.com ~all` |

>⚠️ Do not create duplicated entries or entries mixed with other values to avoid possible validation errors.

## Verifying the SPF

To verify the SPF entries on your domain, we recommend using the [DIG](https://www.digwebinterface.com) tool. Follow the steps below:

1. On the [DIG tool website](https://www.digwebinterface.com/), fill your root domain (e.g. `vtex.com`) in **Hostnames or IP addresses**.
2. Select **TXT** as **Type**.
3. Click on **Dig**.

> ℹ️️ The modifications are impacted by the domain propagation time. It can take between 24 or 48 hours for DIG to reflect changes.

Below, check a [consult example using the VTEX domain](https://www.digwebinterface.com/?hostnames=vtex.com&type=TXT&ns=resolver&useresolver=8.8.4.4&nameservers=):

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/setting-up-the-spf-0.png)
