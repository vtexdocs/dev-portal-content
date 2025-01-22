---
title: "I can't complete a purchase on a FastStore website"
slug: "i-cant-complete-a-purchase-on-a-faststore-website"
hidden: false
createdAt: "2024-06-06T10:17:18.615Z"
updatedAt: "2024-06-06T14:00:00.615Z"
excerpt: "While trying to checkout on a FastStore website, you might see a 'This Connection Is Not Private' error."
tags:
    - faststore
    - checkout
    - dns
---

**Keywords:** FastStore | Checkout | DNS | SSL

When trying to complete a purchase on your FastStore website, you may receive the following error message: `This Connection Is Not Private`

![not-secure-faststore](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/store-performance/not-secure-faststore.png)

This error occurs when your browser cannot verify whether a website is safe to visit. It usually happens when the browser notices a problem while creating an SSL connection or cannot verify the certificate.

## Solution

To solve this problem, there are two troubleshooting checks and instructions you can follow:

- [Configuring an external DNS](#step-1-configuring-an-external-dns): Ensure your FastStore website is accessible via a custom domain and that the checkout works properly.
- [Check the `secure` subdomain pointing](#step-2-check-the-secure-subdomain-pointing): If the error persists after configuring an external DNS, check if the `secure` subdomain is pointing to VTEX.

### Step 1 - Configuring an external DNS

Configure an external DNS to allow customers to access your FastStore website through your chosen domain and enable features like VTEX Checkout. See the [Configuring external DNS](https://developers.vtex.com/docs/guides/faststore/go-live-1-configuring-external-dns) guide for more information.

### Step 2 - Check the `secure` subdomain pointing

If the error continues, check if your website's `secure` subdomain is pointing to `secure.{hostname}.cdn.vtex.com`, where `hostname` is the complete address of your store. To check, follow these steps:

1. Go to your preferred tool, such as the [DNS Checker](https://dnschecker.org/), to check DNS records for a given domain name.
2. Enter `secure.{hostname}` in the search bar.
3. Choose `CNAME` in the dropdown menu.
4. Check if the `secure` subdomain is pointing to the `secure.{hostname}.cdn.vtex.com`, as in the example below:

   ![dns-checker](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/troubleshooting/store-performance/secure-hostname-2.png)
   
If the `secure` subdomain is pointing to `secure.{hostname}.cdn.vtex.com` but the problem continues, open a ticket with [VTEX Support](https://help.vtex.com/en/support).