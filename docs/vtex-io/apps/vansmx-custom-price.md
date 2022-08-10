---
title: "Instagram Lightbox"
slug: "vansmx-custom-price"
excerpt: "vansmx.custom-price@0.1.4"
hidden: true
createdAt: "2022-07-18T16:00:55.015Z"
updatedAt: "2022-07-18T16:00:55.015Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

For use inside the Store theme.
Show the latest posts from your instagram account in a customizable slider-lightbox

![IMG1](acctxt1.png)
![IMG2](acctxt2.png)


## Configuration

1. Add the app as a dependency in your store theme

```
"account.instagram-lightbox": "0.x"
```

2. Declare the app block in your store inside your page

```
{
   ...
   "children":[
      "instagram-lightbox"
   ]
}
```

3. Change the content in Vtex Admin.
   Go to `Store Setup > CMS > Site Editor` and navigate to a page that contains this block.
   You will find it under the name `Lightbox properties`.

   You may able to set number of slides, number of slides per page, add or remove dots and header, and set your facebook developer token 


<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- Eduardo Cervantes

<!-- DOCS-IGNORE:end -->

# Licence

MIT License

Copyright (c) 2020 Ecomsur

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.