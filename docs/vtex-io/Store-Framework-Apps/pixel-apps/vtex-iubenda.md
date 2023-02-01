---
title: "Iubenda"
slug: "vtex-iubenda"
hidden: false
createdAt: "2020-06-03T15:19:48.350Z"
updatedAt: "2020-11-10T14:41:34.438Z"
---

This is a Iubenda first party integration app. The [solution](https://www.iubenda.com/en/?utm_source=adwords&utm_medium=ppc&utm_campaign=aw_brand_global_exact&utm_term=iubenda&utm_content=336331123145&gclid=EAIaIQobChMI38Tz0Jqg6QIVlwyRCh3KoQtkEAAYASAAEgKtK_D_BwE) is integrated with the IAB TCF and US Privacy Framework and it is responsible for managing consent preferences for the ePrivacy, GDPR, and CCPAntegrated.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-iubenda-0.png)

## Configuration

1. [Install](https://vtex.io/docs/recipes/development/installing-an-app/) the `vtex.iubenda` app;
2. In your VTEX account's admin, open the **App** section and select the Iubenda App box;
3. Add the Site ID and the Cookie Policy ID in the respective fields;
4. Save your changes.

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-iubenda-1.png)

> ℹ️ *The Site ID and the Cookie Policy ID are provided by Iubenda*.

### Recommended Iubenda configuration

![image](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/vtex-iubenda-2.png)

Iubenda also provides a store component to let visitors update their advertising tracking preferences even after closing the cookie banner. Use the [Iubenda Components app](https://github.com/vtex-apps/iubenda-components) for that.
