---
title: "Configuración Woowup en VTEX APP."
slug: "woowup-woowup"
excerpt: "woowup.woowup@3.1.0"
hidden: true
createdAt: "2022-07-15T17:25:02.624Z"
updatedAt: "2022-07-26T16:42:49.161Z"
---
En esta guía se te detallará paso a paso como configurar la aplicación de Woowup en VTEX

>Previamente, tenemos que haber instalado la aplicación de Woowup en la Store de VTEX. 
En caso de no haberla instalado, puede acceder a nuestra [guía de instalación](https://docs.woowup.com/vtex/vtex-app-instalacion) de la aplicación.


1. Entrar al panel de administración de la tienda e ingresar en **Apps instaladas** en la opción **Woowup**

![](https://i.postimg.cc/qvw8h8MN/1.png)

2. Aparecerá un formulario con distintos campos. Se debe completar con la siguiente información.

![](https://i.postimg.cc/7LQ0XwzD/2.png)

**URL**: Ingresamos la dirección web de tu tienda. 

**Estados de venta para descargar**: Si conoce los estados de las facturas 
puede ingresarlo en el campo "Estados de ventas para descargar" 
(separados por "," y sin espacios)
Estos son los estados por defecto disponibles para descargar:
* waiting-for-sellers-confirmation
* payment-pending
* payment-approved
* ready-for-handling
* handling
* invoiced
* canceled

> Puede darse el caso que estos campos estén modificados. En caso de que sea así, modificar segun corresponda.

**Nombre de la tienda**: Aquí ingresamos el nombre de la tienda según lo pusiste en una tienda VTEX. Viene dado como prefijo en los dominios `.vtexcommercestable.com.br` 

**Seller**: Opcional. Ingresamos el nombre del seller. 

**App Key/App Token**: Estas claves las obtenemos siguiendo [esta guía](https://docs.woowup.com/vtex/vtex-connect-account).

**Descarga de categorias**: Elegimos si activamos o desactivamos esta opción.

**Sales Channel**: Opcional. Ingresamos el canal de ventas si es que existiese.

**Woowup VTEX Token**: Este campo lo obtenemos ingresando a Woowup, ir a configuración, 
ir a la sección integraciones y seleccionar la integración VTEX. 
Copiar el código VTEX Token provisto.

![](https://i.postimg.cc/fbbYxJJB/3.png)

Una vez completado el formulario. Hacemos click en Guardar y esto se integrará con Woowup.