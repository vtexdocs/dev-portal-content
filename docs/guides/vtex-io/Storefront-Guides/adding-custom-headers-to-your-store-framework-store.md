---
title: "Adding custom headers to your Store Framework store"
slug: "adding-custom-headers-to-your-store-framework-store"
hidden: false
createdAt: "2024-11-25T18:10:16.429Z"
updatedAt: ""
excerpt: "Discover how to configure custom headers in your store"
---

In this guide, you'll learn how to configure custom response headers in your Store Framework store. HTTP headers play a key role in communication between the user's browser and the server, providing additional information about the request in progress. There are two main types of headers:
- **Request Headers:** Sent by the client to the server. They contain information about the request made, such as the type of HTTP method used, the type of accepted content, cookies, among others.
- **Response Headers:** Sent by the server to the client. They provide information about the sent response, such as the response status, type of returned content, cookies, among others.
>ℹ For more information, check the MDN guide [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) and the related documentation.
## Security Response Headers
Here are the headers that accept editing:

- [**X-Frame-Options**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options): Allows the control of how websites can be incorporated into other ones through the use of frames. This header is a security measure to protect users against [click-jacking](https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks#click-jacking) attacks, which occur when an attacker tricks users into clicking something on a web page without their consent.
- [**X-Content-Type-Options**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options): Protects against [MIME](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) vulnerabilities, which can occur when a website allows users to upload content.
- [**Content-Security-Policy (CSP)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy): Allows to control the resources a user agent can load on a given page, preventing [cross-site scripting](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting) attacks.
- [**Strict-Transport-Security (HSTS)**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security): Informs browsers that the site should only be accessed using HTTPS.
- [**X-XSS-Protection**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection): Instructs browsers on how to handle cross-site scripting (XSS) attacks, activating the integrated filter to block malicious scripts from executing in the user's browser.
- [**Referrer-Policy**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy): Determines which origin page information is shared with the destination page in HTTP requests, essential to protect user privacy and website security.
## Instructions
You can configure a custom header, a value that is not standardized and is tailored to the specific requirements or features of your store.
To add a custom heading, follow the instructions below:
1. In the VTEX Admin, go to **Store Settings > Storefront > Store**.
2. Click the Advanced tab.
3. Scroll down to the **Custom Header** section.
4. Click **Add**.

![custom-header-flow-en](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/custom-header-flow-en.gif)
5. Complete the fields based on the [Security Response Headers](#security-response-headers) and the following guidelines:
   - **Header ID:** ID that identifies your custom header.
   - **Key:** Header key, following HTTP standards.
   - **Value:** Header value, following HTTP standards.

   >ℹ For more information on HTTP headers, see the MDN documentation on [headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers).

See the example below:
![custom-header-setup](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/docs/guides/vtex-io/Storefront-Guides/images/custom-header-setup.png)
In the example above, the value `max-age=31536000; includeSubdomains` in the `Strict-Transport-Security` (HSTS) header defines the maximum duration in seconds that the HSTS policy should be applied by the browser for a specific domain and its subdomains. The `preload` directive indicates that the domain should be included in the HSTS preload list, which ensures that compliant browsers will only connect via HTTPS, even for the initial request.
6. Click **Apply** to apply the settings. The update can take up to a day to reflect due to caching.
### Best practices
- When adding new headers to your account, always check the [official MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP).
- When using the `frame-ancestors` header, remember to add the `self` parameter, which indicates that the page can only be embedded in iframes on the domain itself. Without this setting, the Site Editor content may be blocked, as iframes can be used to load and display parts of the store.
- When using the `X-Frame-Options` header, remember to add the `SAMEORIGIN` parameter, which allows the page to be loaded in iframes only when the origin (domain) of the iframe is the same as the main page. Without this setting, the Site Editor content may be blocked, as the header restricts the site display within any iframe.
- Always run tests in a [development workspace](https://developers.vtex.com/docs/guides/vtex-io-documentation-creating-a-development-workspace) before making the configuration available in production stores.
