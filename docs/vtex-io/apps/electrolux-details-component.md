---
title: "Main"
slug: "electrolux-details-component"
excerpt: "electrolux.details-component@0.2.1"
hidden: true
createdAt: "2022-08-01T16:52:37.408Z"
updatedAt: "2022-08-01T16:52:37.408Z"
---
Component to create FAQs, initially displays questions with closed answers, to open or close you need to click on the question.
The component allows the use of markdown, but it is recommended that the links are inserted using the HTML `<a>` tag to receive the attribute settings as a target.

Limit of 10 FAQs

## CSS Hanldes
Use these classes to configure the component inside the theme.
| Class                   |
| ----------------------- |
| title                   |
| container               |
| description             |
| hidden                  |
| textContent             |
| paragraph               |
| caretIcon               |
| link                    |

## Configuration on admin
Through the site editor, you can enter the following contents in the fields:
| Parameter                | Description                                                  |
| ------------------------ | -------------------------------------------------------------|
| Title                    | Add a Title to FAQ                                           |
| Question                 | Add a Question to FAQ                                        |
| Answer                   | Add a Answer for Question                                    |
## Tecnologies
Used TACHYONS for CSS settings and also CSS-HANDLES for necessary customizations.
- [Doc TACHYONS](https://tachyons.io/)
- [Doc CSSHandles](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-contributing-with-new-css-handles)

## Configuration
1. On your store-theme app, add details-component as a dependency in the `manifest.json` file: `"electrolux.details-component": "0.x"`.
2. Install the app in your store using the command `vtex install electrolux.details-component@0.x`.
3. Declare the `"details-component"` application block inside the desired block.
4. Customize elements in `electrolux.details-component.css` file inside the theme.
5. To configure the links insert the class `"electrolux-details-component-0-x-link"` in the tag HTML.