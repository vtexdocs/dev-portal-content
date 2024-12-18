---
title: "SEO"
slug: "storefront-seo"
hidden: false
createdAt: "2024-09-26T14:09:58.908Z"
updatedAt: ""
excerpt: "Discover strategies to improve your ecommerce SEO."
---

Search Engine Optimization (SEO) is a set of strategies to enhance the performance of websites, blogs, and web pages. The primary goal is to achieve higher rankings in organic search results, driving more traffic and boosting the site's authority.

In ecommerce, a well-implemented SEO strategy enhances visibility, attracts organic traffic, and improves user experience. By elevating search engine rankings, SEO provides a competitive edge, reduces customer acquisition costs, and ensures long-term results.

To learn more about SEO strategies, check Google’s documentation resource [Explore Google Search documentation to improve your site's SEO](https://developers.google.com/search/docs).

VTEX offers a set of tools and settings that allow you to optimize your store for search engines, making your products more discoverable and improving site performance.

In this guide, you will learn some best practices for implementing strategies to improve SEO in your VTEX store.

## Store settings

Properly configuring the elements of your ecommerce store, such as titles, descriptions, media, and URLs may significantly impact how search engines index and rank your pages.

### Titles and descriptions

When setting up your store, consider how title tags and descriptions affect your store’s SEO:

- **Title tags:** Use primary keywords at the beginning of the title and ensure titles are concise (50-60 characters). The value assigned to this tag is displayed at the top of the browser's title bar when someone visits your website. It can be configured for home, [product](https://help.vtex.com/en/tutorial/product-registration-fields--4dYXWIK3zyS8IceKkQseke), [category](https://help.vtex.com/en/tutorial/category-registration-fields--5Z7RrvW41yumyQCmk2iqoG), and [brand](https://help.vtex.com/en/tutorial/brand-registration-fields--37Ky7lTbEkiWIAYA80EMyI) pages.

> ℹ️ For stores developed with Store Framework, you can customize Department, Category, and Subcategory titles using [VTEX Intelligent Search app](https://developers.vtex.com/docs/apps/vtex.search@1.0.8). This allows your store to display different titles for each category level within the search navigation bar. Learn more in [Intelligent Search](https://help.vtex.com/tracks/vtex-intelligent-search).

- **Meta descriptions:** Include relevant keywords, limit them to 140-160 characters, and provide a compelling reason for users to click, which will help improve organic traffic. Meta descriptions are crucial for SEO because they appear in search engine results pages (SERPs) as snippets under the page title, giving users an idea of what they can find on the site. They can be configured for home, product, category, and brand pages in the same setup page where you configure the title tags, directly in the VTEX Admin.
- **Unique content:** Avoid duplication across pages. Make sure titles and descriptions are unique for each page to improve search visibility and prevent keyword cannibalization, where multiple pages compete for the same search terms.
- **Robots.txt:** Edit or customize your `robots.txt`, which is a text file that search engines use to define site scanning rules for crawlers based on your business needs. Learn more in [Google Search Console Tracking - robots.txt](https://help.vtex.com/en/tutorial/google-search-console-tracking-robots-txt--tutorials_574).

In Legacy CMS Portal stores, the SEO settings for the home page, such as `meta tag description` and `robots.txt` file are configured through *Store Settings > Storefront > Settings* in the VTEX Admin. Learn more in [Settings](https://help.vtex.com/en/tracks/cms--2YcpgIljVaLVQYMzxQbc3z/1oN446gRGcR2s70RvBCAmj#settings). To improve SEO on other pages of your site, you can leverage **meta tags control**. Learn more in [How to use the meta tags control](https://help.vtex.com/en/tutorial/how-to-use-the-meta-tags-control--2OPiSPubgcEqIikAWsCouk).

For stores developed with Store Framework, the SEO settings for the home page are configured through *Store Settings > Storefront > Store*. Learn more in [Configuring SEO in your Store Framework store](https://help.vtex.com/pt/tutorial/configuring-seo-in-your-store--1sKskEsjUSvgHyqM8oknVR). To enhance SEO for product listing pages, see [Improving the SEO of Product Listing Pages](https://help.vtex.com/en/tutorial/improving-the-seo-of-product-listing-pages--UrQtlKAMuSaLBP5wG9ftG).

For FastStore stores, see [Configuration options for faststore.config.js](https://developers.vtex.com/docs/guides/faststore/project-structure-config-options).

### Images and videos

When adding images or videos to your store, whether for SKUs, banners, or any other page on your site, follow these guidelines:

- **Media file name:** Rename media files used in your store with descriptive keywords, avoiding generic names such as `image1.png`.
- **`alt text`:** Use clear `alt text` with relevant keywords to describe the media content accurately. Search engines don't read images and videos, so each media piece should have personalized alternative text (`alt text`). Moreover, the `alt text` promotes [Accessibility](LINK) by helping visually impaired users understand the content on the page.
- **Image optimization:** Compress images to improve page load speed without sacrificing quality. Learn more in [Image compression](https://help.vtex.com/tutorial/image-compression--4klbgpsPksq44KcwqKeye8).

### URLs

When defining the URLs for your site, keep in mind the following best practices:

- **Keyword-friendly URLs:** Incorporate primary keywords into short, clean, and descriptive URLs. Use hyphens to separate words in URLs, enhancing readability and clarity for users and search engines. For product pages, the URL is defined by the `textLink` field in the product settings, as outlined in the guide [Filling in the category registration fields](https://help.vtex.com/en/tutorial/category-registration-fields--5Z7RrvW41yumyQCmk2iqoG).
- **Canonical tags:** Use canonical tags on your site to indicate the preferred version of a URL when there are multiple pages with similar content. This prevents duplicate content issues by consolidating ranking signals and ensuring search engines index the correct page. On VTEX, the canonical tag is generated automatically for all store pages, such as product, category, brand, and custom.

> ⚠ In cross-border stores, you must configure the canonical tag for each binding, as they have different canonical base addresses. For example: `store.com/en` and `store.com/pt`. Learn more in [Cross-border store content internationalization](https://developers.vtex.com/docs/guides/cross-border-custom-urls-1).

## Monitoring and analysis

Effective monitoring and analysis are crucial for understanding the impact of your SEO efforts and making data-driven decisions:

- **Implement schema markup:** Structured data (schema markup) helps search engines better understand the content and enhance rich snippets in search results. Learn more in [Structured data through Google Search Console Data Markers](https://help.vtex.com/en/tutorial/structured-data-through-google-search-console-data-markers--tutorials_560).
- **Track keyword rankings:** Use tools such as [Google Search Console](https://search.google.com/search-console/about) to monitor the rankings of your target keywords over time and identify trends and fluctuations, which will help you understand what is working and where improvements are needed.
- **Analyze website traffic:** Use [Google Analytics](https://analytics.google.com/) or your preferred tool to track organic traffic, page views, and user behavior on your site.
- **Evaluate on-page performance:** Analyze page load times, mobile usability, and overall user experience with tools such as [PageSpeed Insights](https://pagespeed.web.dev/). Review on-page metrics such as bounce rate, time on page, and conversion rates to assess content effectiveness.

Learn more in [Integration with monitoring tools](https://help.vtex.com/subcategory/tracking-integration--1luKrYptdi8WoMYckakUaM).
