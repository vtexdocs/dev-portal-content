---
title: "VTEX Shield: New SSL Certificates API"
slug: "2025-06-03-vtex-shield-new-ssl-certificates-api"
hidden: false
type: "added"
createdAt: "2025-06-03T00:00:00.219Z"
updatedAt: "2025-06-03T00:00:00.219Z"
excerpt: "VTEX Shield now offers an API to manage custom SSL certificates."
---

> ℹ️ This feature is part of [VTEX Shield](https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh). If you are already a VTEX customer and want to adopt VTEX Shield for your business, please contact [Commercial Support](https://help.vtex.com/en/tracks/support-at-vtex--4AXsGdGHqExp9ZkiNq9eMy/3KQWGgkPOwbFTPfBxL7YwZ). Additional fees may apply. If you are not yet a customer but are interested in this solution, please complete our [contact form](https://vtex.com/br-pt/contato/).

The new **SSL Certificates API** allows merchants using [VTEX Shield](https://help.vtex.com/en/tutorial/vtex-shield--2CVk6H9eY2CBtHjtDI7BFh) to manage [custom SSL certificates](https://help.vtex.com/en/tutorial/custom-ssl-certificates--1hoaDEbU50PDZSe6AYep9q) directly on VTEX infrastructure. This feature is designed for businesses with specific compliance or security requirements.

The SSL Certificates API includes the following endpoints:

* GET [List SSL certificates](https://developers.vtex.com/docs/api-reference/ssl-certificates-api#get-/api/edge/certificates): List all custom SSL certificates installed in their store.  
* GET [Get SSL certificate by ID](https://developers.vtex.com/docs/api-reference/ssl-certificates-api#get-/api/edge/certificates/-certificateId-): Retrieve details of a specific certificate by its ID.  
* PUT [Install or renew SSL certificate](https://developers.vtex.com/docs/api-reference/ssl-certificates-api#put-/api/edge/certificates): Install or renew certificates by uploading their contents using either JSON or multipart/form-data formats.

Learn more in the [Managing SSL certificates guide](https://help.vtex.com/tutorial/custom-ssl-certificates--1hoaDEbU50PDZSe6AYep9q) or explore the [API reference](https://developers.vtex.com/docs/api-reference/ssl-certificates-api).
