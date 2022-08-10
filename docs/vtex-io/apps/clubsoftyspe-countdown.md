---
title: "CountDown App"
slug: "clubsoftyspe-countdown"
excerpt: "clubsoftyspe.countdown@0.0.4"
hidden: true
createdAt: "2022-07-04T22:26:28.154Z"
updatedAt: "2022-08-08T16:11:41.426Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

Countdown counter where the user defines the month, day, year and time to end. Example: "Nov 7,2021 15:00:00" and once the countdown counter is configured, the countdown begins from the current time to the time limit already configured. it has the functionality of hiding when the end date arrives or of showing some code block defined in the JSON.

## Configuration

1. Add the app as a dependency in your store theme

```
"batacl.countdown": "0.x"
```

2. Declare the app block in your store inside your porduct display page.

Note:
The format to define the date and time is as follows:
![DateTime](https://i.ibb.co/Qpq9C5T/count-Down-Documentation.png)

```
{
   ...
   "countdown#imagen":{
       "children":[], // Acá se define el componente que queremos que se muestre cuando se finalice el contador, dejar en blanco si no queremos que aparezca un componente cuando el mismo finalice solo se dejaría de mostrar.
       "props":{
         "setDate":"Sept 21,2021 13:20:00", //Definir la fecha a finalizar el evento tiene un formato a seguir
         "textBefore": "", //Texto a visualizar antes del contador dejar en blanco si no aplica
         "textAfter": "", //Texto a visualizar despues del contador dejar en blanco si no aplica
         "imageWidth": "30%", //Width del contenedor de la imagen
         "imageHeight": "80px", //Height del contenedor de la imagen
         "marginImageConteiner":"auto", //Margen del contenedor de la imagen
         "imageBackgroundImage": "https://i.ibb.co/2nXq1wn/oferta-countdown.png", //Definir la URL de la imagen a mostar en el contenedor
         "mouseCursor":"default", //Se define la propiedad del cursor del mouse, definir "true" para "default" para cuando es solo texto o "false" para "pointer" cuando definimos una imagen con un enlace
         "backgroundRepeat": "no-repeat", //Propiedad para que la imagen no se repita en el contenedor 
         "backgroundColor": "#313135", //Color del contenedor del contador, para cuando colocamos texto se vea como una huincha
         "urlContent": "#", //URL de la redireccion de la imagen o del contenedor de texto si aplica el caso
         "pointerEvents": "none", // none para cuando no queremos que se puede seleccionar nada
         "blockClass": "Contador-regresivo-imagen"
       }
     },
}

{
   ...
   "countdown#regresivo":{
      "children":[], // Acá se define el componente que queremos que se muestre cuando finalice el contador, dejar en blanco si no queremos que aparezca un componente cuando el mismo finalice solo se dejaría de mostrar.
      "props":{
         "setDate":"Ene 11,2022 18:00:00", // Definir la fecha a finalizar el evento tiene un formato a seguir
         "textBefore": " FALTAN", // Texto a visualizar antes del contador dejar en blanco si no aplica
         "textAfter": "PARA LA ENTREGA DEL CONTADOR", //Texto a visualizar despues del contador dejar en blanco si no aplica
         "backgroundColorClock": "#ff0000", //Definir el color del contenedor del reloj
         "urlContent": "", //URL de la redireccion de la imagen o del contenedor de texto si aplica el caso, dejar en blanco si no queremos que redireccione a un enlace
         "imageDisplay": "none", // se le coloca none para que no muestre el contenedor de la imagen
         "imageWidth": "",
         "imageHeight": "",
         "imageBackgroundImage": "",
         "mouseCursor":"default",
         "pointerEvents": "none", // "none" para cuando no queremos que se puede seleccionar nada, se deshabilite el que redireccione si no aplica
         "blockClass": "Contador-regresivo-promocion"
      }
   } 
 
```

3. Screenshot

### Image

![CountDown](https://i.ibb.co/chrcw1K/imagen-1-countdown.png)

### Lineal

![CountDown](https://i.ibb.co/h8JR7Z0/imagen-2-countdown.png)


<!-- DOCS-IGNORE:start -->

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- Duglas Medina
- Jose Martinez

<!-- DOCS-IGNORE:end -->