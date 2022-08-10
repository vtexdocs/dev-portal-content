---
title: "Click & collect"
slug: "tommymx-axo-clickncollectorders-readmees-4"
excerpt: "tommymx.axo-clickncollectorders@3.1.3"
hidden: true
createdAt: "2022-08-06T00:02:24.181Z"
updatedAt: "2022-08-06T00:02:24.181Z"
---
Esta aplicación le permite a los usuarios ver y hacer seguimiento a las ordenes que están *en tienda*, esta aplicación búsca las ordenes en la tienda específica y muestra esas ordenes con algunos filtros por estatus (cancelado, pendiente, entregado o en tienda).

![image](https://user-images.githubusercontent.com/60228986/170093863-0d4d6c33-952f-453a-abf2-9e7eef358aec.png)


# ¿Cómo funciona?

Básicamente [una vez instalada]() la aplicación de "click and collect" está disponible en el panel de administración, esta trabaja basada en dos principales fuentes de información:

1. Ordenes almacenadas en el white label en el que está [registrado el usuario]() que está haciendo uso del módulo
2. Ordenes almacenadas en master data su "*acronym*" debe ser 'EN' para que la aplicación la reconozca

La lógica principal toma estas dos fuentes de información y aplica un filtro para obtener las ordenes de estado *"en tienda"*, esto lo hace búscando las ordenes principales del seller dentro de las ordenes almacenadas en master data que cumplan con las siguientes condiciones:

1. El nombre de la *sucursal* debe ser el mismo en la cual se está llevando a cabo la sesión
2. El estado de la ordén en master data debe ser "R"

Una vez filrtradas las ordenes se les aplica el estado correspondiente, adicionalmente si una orden esta en tienda, se calculan los días que esta lleva allí, a partir de un campo en la tabla de master data llamado **Fecha**, estos días tienen un código de color que indica si el pedido ha excedido los días en tienda, de 0 a 9 días el color será negro, entre 10 y 15 será amarillo, 15 o mas el color será rojo.

> **Nota:** Es importante que el campo fecha tenga el formato ```Día Mes Año (24 Mayo 2022)``` para que la lógica pueda calcular los días en tienda.

### Detalle de las ordenes

La página de detalle de las ordenes incluye información detallada del pedido, están en desarrollo algunas de las funcionalidades de esta vista.

![order-detail](https://user-images.githubusercontent.com/60228986/170093824-9475e894-b2a0-4fa9-880c-8eb0cfd4f522.png)