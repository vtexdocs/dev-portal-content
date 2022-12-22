---
title: "Setting up the SPF"
slug: "setting-up-the-spf"
hidden: false
createdAt: "2021-05-19T19:35:16.057Z"
updatedAt: "2021-05-28T18:40:04.171Z"
---
The SPF (Sender Policy Framework) is a system used to avoid not allowed servers to send emails on behalf of your domain. This system implements rules that verify if the server has a particular policy set up by the domain’s admin.

Check for more information on [the Sender Policy Framework Introduction](https://web.archive.org/web/20080510142749/http://www.openspf.org/Introduction).

## Editing the SPF

All `includes` should be set up to add a new SPF. Here is an example of an SPF on VTEX:
[block:code]
{
  "codes": [
    {
      "code": "v=spf1 a mx ip4:192.0.2.32/27 include:server.com include:amazonses.com -all",
      "language": "erlang"
    }
  ]
}
[/block]
See the example below to understand the change:

**Before**
[block:code]
{
  "codes": [
    {
      "code": "v=spf1 include:websitewelcome.com include:_spf.google.com ~all",
      "language": "erlang"
    }
  ]
}
[/block]
**After**
[block:code]
{
  "codes": [
    {
      "code": "v=spf1 include:websitewelcome.com include:_spf.google.com include:amazonses.com ~all",
      "language": "erlang"
    }
  ]
}
[/block]

[block:callout]
{
  "type": "warning",
  "body": "It should not exist duplicated entries, or even mixed with other values, to avoid possible validation errors."
}
[/block]

## Verifying the SPF

To verify the SPF entries on your domain, we recommend using the DIG tool. You can check the online version on [the Dig web interface](http://www.digwebinterface.com).

To consult the verification, you need to:

1. Fill your domain in **hostnames or IP addresses**.
2. Select **TXT** as **Type**.
3. Click on **Dig**.
[block:callout]
{
  "type": "info",
  "body": "The modifications are impacted by the domain propagation time. This can take between 24 or 48 hours to reflect the changes."
}
[/block]
Here is a [consult example using the VTEX domain](https://www.digwebinterface.com/?hostnames=vtex.com&type=TXT&ns=resolver&useresolver=8.8.4.4&nameservers=):

![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@readme-docs/docs/guides/Integration%20Guides/api-guides/c9a066c-Screenshot_2021-05-19_Boas_prticas_de_SPF_Sender_Policy_Framework_73.png)
