---
title: "Control to disable the canonical tag"
slug: "control-to-disable-the-canonical-tag"
hidden: false
createdAt: "2022-09-13T15:25:41.097Z"
updatedAt: "2022-09-13T15:25:41.097Z"
---
## What is the canonical tag

When using the meta tags control, explained in the article [How to use the meta tags control](how-to-use-the-meta-tags-control), one of the tags inserted in the head of the page is the __canonical tag__:

`<link rel="canonical" href="http://{AccountName}.com.br/{page}">`

The canonical tag allows you to avoid __duplicate content__, that is, scenarios where two pages of the site display identical or almost identical content. An example are the following three URLs:
- {AccountName}.com
- {AccountName}.com.br
- {AccountName}.com/

All of the above URLs display the same content, but for search engines, simply adding a forward slash to the end of the address may characterize a different page, which is bad for __SEO__ purposes.

To avoid scenarios like that, the canonical tag informs search engines what is the preferred version of a web page.

So a search engine can decide whether two pages have duplicate content and, if it decides they do, transfer the indexing merits to the preferred version.

## Disabling the canonical tag for a page

While the canonical tag is useful for SEO purposes, you may not want to use it for specific pages.

Because it's inserted automatically by the meta tag control, if you are using this control, you must inform the system that it should exclude only the canonical tag. This is done through the following control:

`<vtex.cmc:canonicalPage disable="true"/>`