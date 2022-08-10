---
title: "Whirlpool Chile"
slug: "whirlpoolcl-store-theme"
excerpt: "whirlpoolcl.store-theme@2.0.13"
hidden: true
createdAt: "2022-07-08T19:53:53.439Z"
updatedAt: "2022-07-28T19:29:13.477Z"
---
## Yarn x npm

__Use Yarn not npm.__
VTEX IO expects a yarn.lock file in some cases and mixing Yarn's and npm's lock files can lead to problems.
It is thus safer to only use Yarn.
Don't forget to commit your changes to yarn.lock.

## Styles

`npm run sass` can be used to compile all the Sass files in the styles/scss folder to the corresponding ones in styles/css. It will keep watching the styles/scss folder for changes in the background.
__All styles should be handled with Sass.__
Notice also that the .css files are in .gitignore.

If you wish to just compile the files once, without watching later, the command is `npm run sass:once`.

__Don't forget to compile the styles before attempting to publish/release the app!__