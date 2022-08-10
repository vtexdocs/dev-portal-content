---
title: "Rossetti"
slug: "rossettiar-store-theme"
excerpt: "rossettiar.store-theme@2.0.12"
hidden: true
createdAt: "2022-07-14T20:58:02.194Z"
updatedAt: "2022-07-14T21:07:33.954Z"
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