---
title: "Bringeri"
slug: "bringerihogarar-store-theme"
excerpt: "bringerihogarar.store-theme@3.0.6"
hidden: true
createdAt: "2022-07-07T21:16:30.218Z"
updatedAt: "2022-08-05T17:39:25.837Z"
---
## Yarn x npm

**Use Yarn not npm.**
VTEX IO expects a yarn.lock file in some cases and mixing Yarn's and npm's lock files can lead to problems.
It is thus safer to only use Yarn.
Don't forget to commit your changes to yarn.lock.

## Styles

`npm run sass` can be used to compile all the Sass files in the styles/scss folder to the corresponding ones in styles/css. It will keep watching the styles/scss folder for changes in the background.
**All styles should be handled with Sass.**
Notice also that the .css files are in .gitignore.

If you wish to just compile the files once, without watching later, the command is `npm run sass:once`.

**Don't forget to compile the styles before attempting to publish/release the app!**