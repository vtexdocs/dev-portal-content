---
title: "CUSTOM NEWSLETTER"
slug: "victoriassecretcl-contact-us-form"
excerpt: "victoriassecretcl.contact-us-form@0.0.2"
hidden: true
createdAt: "2022-08-05T18:14:28.549Z"
updatedAt: "2022-08-05T18:14:28.549Z"
---
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

custom form that sends customer data to Master Data using Axios. 

![Media Placeholder](./contact-us-form.png)

## Installation 
1. Clone the repository and change the app manifest:
```
{
  "vendor": "<your-vendor>",
  "name": "contact-us-form",
  "version": "0.0.0",
  .
  .
  .
}
```
2. Login to your vtex account:
```
> vtex login <development-environment>
```
3. Select your workspace and use `vtex link`:
```
> vtex use <workspace>
> vtex link
```

## Block ⚙
1. Adding the app as a theme dependency in the `manifest.json` file:
```
<your-vendor>.contact-un-form: "0.x"
```

```
2. Declare the main application block in a given theme template or within another theme block. For example:
```
```
{
  "flex-layout.row#contact-us-form": {
        "children": [
            "contact-us-form"
        ],
        "props": {
            "horizontalAlign": "center",
            "blockClass": "contact-us-form"
        }
    }
}
```

## Modus Operandi

The component receives the title and text from the left container.
 
A form is rendered that uses axios to POST to masterData adding a client validating the following data: name, email and date of birth.

 ** The app can be edited from the site editor. **

## Customization

| CSS Handles |
| ----------- |
| `container` |
| `textContainer` |
| `textContent` |
| `title` |
| `formContainer` |
| `form` |
| `inputContainer` |
| `inputForm` |
| `inputLabel` |
| `buttonContainer` |
| `btnSuscribe` |
| `selectContainer` |
| `selectContent` |
| `inputAreaForm` |
| `submitButton` |

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- **Gabriela Montes**