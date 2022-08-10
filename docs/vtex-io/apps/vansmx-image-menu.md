---
title: "Image Menu"
slug: "vansmx-image-menu"
excerpt: "vansmx.image-menu@0.1.30"
hidden: true
createdAt: "2022-07-25T22:41:11.743Z"
updatedAt: "2022-07-25T22:59:30.851Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

This repository contains 3 custom applications:
1. CustomInfoCard
![IMG1](./docs/custom-info-card.png)

2. ImageMenu
![IMG1](./docs/image-menu.png)

3. ShoeMenu / ShoeMenuMobile
![IMG1](./docs/shoe-menu.png)


## Configuration

1. Add the app as a dependency in your store theme

```
"dependencies": {
   ...
   "vansmx.image-menu": "0.x"
}
```

2. Declare the app as children in your store inside your page


- To show CustomInfoCard
```
{
    ...
    "children": ["custom-info-card"]
}
```
```
{
   "custom-info-card" : {
        "props": {
            "imageUrl": "",
            "head": "",
            "text": "",
            "callToAction": "",
            "textButton": "",
            "blockClass": ""
        }
    }
}
```

- To show ImageMenu
```
{
    ...
   "children": [ "image-menu" ]
}
```

- To show ShoeMenu / ShoeMenuMobile
```
{
   ...
   "children": [ "shoe-menu" ]

   ...
   "children": ["shoe-menu-mobile"]
}
```



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