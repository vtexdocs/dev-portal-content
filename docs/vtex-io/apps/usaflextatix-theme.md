---
title: "usaflex.store-theme"
slug: "usaflextatix-theme"
excerpt: "usaflextatix.theme@2.0.10"
hidden: true
createdAt: "2022-07-05T14:55:02.399Z"
updatedAt: "2022-08-05T19:17:20.914Z"
---
This is the main Usaflex storefront app, where all the pages are assembled.

To contribute to this app pay attention to these points:
- Use of yarn is mandatory. Do not use npm and remember to commit your changed yarn.lock file
- The styles are managed with Sass and the .css files are in the gitignore. Therefore, remember to always compile all styles before releasing the code.

## Commands
- `npm run sass`: compiles all Sass files from styles/sass and place the compiled css files on styles/css
- `npm run sass:watch`: similar to `npm run sass` except that it doesn't exit after it finishes compiling, but remains listening to new content on the Sass files and recompiles the css automatically when there are such changes.