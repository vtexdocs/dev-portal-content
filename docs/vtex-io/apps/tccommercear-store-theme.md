---
title: "Philips Argentina"
slug: "tccommercear-store-theme"
excerpt: "tccommercear.store-theme@1.0.4"
hidden: true
createdAt: "2022-07-06T20:05:52.417Z"
updatedAt: "2022-08-05T13:31:57.628Z"
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