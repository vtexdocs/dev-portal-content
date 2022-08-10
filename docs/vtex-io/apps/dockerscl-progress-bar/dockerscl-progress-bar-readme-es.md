---
title: "Progress Bar"
slug: "dockerscl-progress-bar-readme-es"
excerpt: "dockerscl.progress-bar@0.0.10"
hidden: true
createdAt: "2022-07-29T20:22:26.999Z"
updatedAt: "2022-07-29T20:22:26.999Z"
---
<!-- DOCS-IGNORE:start -->
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
<!-- DOCS-IGNORE:end -->

Barra de progreso, su funcionalidad se basa en obtener el valor total a pagar del o los productos en el carrito de compra y ver si ese monto cumple o no con la condición para obtener el beneficio del envío gratis del producto donde se muestra el progreso del mismo en una barra progresiva.

## Configuración en el Store - theme 

1. Agregar la dependencia en tu store-theme en el archivo manifest.json

```
"dockersecl.progress-bar": "0.x"
```

2. Declara el block dentro del archivo del minicart.jsonc para que la barra progresiva se muestre en el mismo Ejemplo:

```
{
   ...
   "children":[
      "progressbar"
   ]
},


"progressbar":{
    "props":{
      "setFreeShipping": 40000
    }
}
```
![Progress Bar in MiniCart](https://i.ibb.co/KrHJDk8/progressbar-in-minicart.png)

3. Screenshot

### Vista en el sitio

![Progress Bar](https://i.ibb.co/HY2XGQ4/Screenshot-2.png)

<!-- DOCS-IGNORE:start -->

### Ajustes en la App

En el siguiente directorio de la raiz de la app: ./react/Progressbar.jsx se encuentra el componente de la funcionalidad del progress-bar, en el se trabaja con el contexto del orderForm de vtex para poder obtener los datos necesarios para el funcionamiento de la app, donde dentro del contexto nos referimos al  
${orderForm.value} para obtener el monto total a pagar del producto y del ${orderForm.totalizers[1].id==="Shipping"} para conocer si esa variable trae o no el valor del costo del envio, en caso de ser positivo se genera una funcion aritmetica para conocer el monto total a pagar sin el valor del costo de envio y así conocer si el usuario logra o no el monto para el envío gratuito.

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- Duglas Medina

<!-- DOCS-IGNORE:end -->