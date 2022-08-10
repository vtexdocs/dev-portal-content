---
title: "CUSTOM NEWSLETTER"
slug: "micocacola-custom-newsletter"
excerpt: "micocacola.custom-newsletter@0.0.13"
hidden: true
createdAt: "2022-07-29T17:38:59.459Z"
updatedAt: "2022-07-29T17:38:59.459Z"
---
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

Personalized newsletter that sends customer data to Master Data using Axios. 

![Media Placeholder](./custom-newsletter.jpg)

## Installation 
1. Clone the repository and change the app manifest:
```
{
  "vendor": "<your-vendor>",
  "name": "custom-newsletter",
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
<your-vendor>.custom-newsletter: "0.x"
```
2. Create a new file named `<your-vendor> .custom-newsletter.css` in the css folder and add the following styles.
```
.container{
  background-color: black;
  color: white;
  padding: 25px;
}

.title {
  font-family: gothamboldregular;
}

.textContainer {
  max-width: 40%
}

.textContent, .inputLabel {
    color: white;
    cursor: pointer;
    font-size: 0.875rem;
    font-weight: normal;
    line-height: 1.5;
    margin-bottom: 0;
}

.formContainer{
  max-width: 60%;
  color: white;
  width: 100%;
  height: max-content;
}

.form {
  width: 100%;
  height: 100%;
  color: white;
}

.inputContainer{
  width: 32%;
}

.inputForm {
  width: 100%;
  height: 40px;
  border-radius: 0.4rem;
  border: none;
  color: #e61d2b;
  outline-width: 0;
  font-size: 0.875rem;
}

.buttonContainer{
  height: max-content;
  width: 100%;
}


.btnSuscribe {
  text-transform: none;
  width: 100%;
  border: none;
  font-weight: 500;
  font-size: .9rem;
  transition: 200ms ease-in-out;
  border-radius: 0.4rem;
  background-color: white;
  color: #f40009;
  max-width: -webkit-fill-available;
  height: 40px;
}

.btnSuscribe:hover {
  background-color: #f40009;
  color: white;
  cursor: pointer;
}

@media (min-width: 0px) and (max-width: 1025px) {

  .form{
    flex-flow: column wrap;
  }

  .inputContainer{
    margin: 5px 0px;
    width: 100%;
  }

  .textContainer{
    width: 100%;
    max-width: 100%;
  }
  
  .formContainer{
    max-width: 100%;
  }

  .buttonContainer{
    width: 100%;
  }
}

```
3. Declare the main application block in a given theme template or within another theme block. For example:
```
{
  "flex-layout.row#newsletter": {
        "children": [
            "custom-newsletter"
        ],
        "props": {
            "preventHorizontalStretch": true,
            "horizontalAlign": "center",
            "blockClass": "custom-newsletter"
        }
    }
}
```

## Props

| Prop name    | Type            | Description    | Default value                                                                                                                               |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `title` | `String` |  Left Title text  | `¡DESPACHO GRATIS!`   |
| `text`      | `String` |  Left content text   | `Recibe un cupón al registrarte para conocer nuestras increíbles promociones.`       |

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

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- **Fabian Toro**