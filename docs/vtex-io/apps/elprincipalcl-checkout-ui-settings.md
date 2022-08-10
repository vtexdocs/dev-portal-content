---
title: "Checkout UI Settings"
slug: "elprincipalcl-checkout-ui-settings"
excerpt: "elprincipalcl.checkout-ui-settings@0.7.6"
hidden: true
createdAt: "2022-07-19T23:41:16.157Z"
updatedAt: "2022-07-21T21:42:14.476Z"
---
Los ajustes de la aplicación Checkout UI son responsables de **personalizar el Checkout UI de tu tienda a través de scripts**.

La principal ventaja de usar esta aplicación en lugar de [store's admin](https://help.vtex.com/tutorial/configure-template-in-smartcheckout-update--ToTE5XB39t0SwtHgpgwSv?locale=en) para esta personalización es que tus scripts Checkout se comportarán como configuraciones para aplicaciones de plataformas.

En la practica, eso significa que los ajustes del Checkout UI permiten Testeo A/B in los scripts de la tienda, en adición a la posibilidad de rápidos retrocesos a escripts antiguos (i.e. scripts pertenecientes a versiones mas antiguas de la aplicación Checkout UI Settings)

## Configuración

1.  Usando tu terminal y el [VTEX IO Toolbelt](https://vtex.io/docs/recipes/development/vtex-io-cli-installment-and-command-reference), ingresa dentro de la cuenta deseada;
2.  Corre `vtex list` para acceder a la lista de aplicaciones de aplicaciones que estan ya instaladas en la cuenta en la que estás trabajando. Si la opción Checkout UI Settings ya existe, puedes saltarte al paso 7 de es paso a paso
3. Si la aplicacion Checkout UI Settings no se encuentra en la lista de aplicaciones instaladas, corre el comando `vtex init`;
4. Selecciona la opción `checkout-ui-settings`;
5.  Abre la aplicación `checkout-ui-settings` en el editor de codigo de tu preferencia;
6.  En el archivo  `manifest.json`, cambia el valor predefinido por defecto `vendor` al nombre de la cuenta en la cual quieres instalar la aplicación;
7.  En la carpeta `checkout-ui-settings`, crea los archivos en los cuales serán incluidos los scripts, tal como lo harías en el [admin's interface](https://help.vtex.com/tutorial/configure-template-in-smartcheckout-update--ToTE5XB39t0SwtHgpgwSv?locale=en#configure-code). observa que algunos archivos por defecto ya existen en la carpeta `checkout-ui-custom`, archivos los cuales puedes usar para insertar los scripts.
8. De acuerdo a la personalización del Checkout que estés buscando, abre el archivo más apropiado para insertar los scripts deseados;
9.  Guarda tus cambios. Luego, [publica](https://vtex.io/docs/recipes/development/publishing-an-app) la nueva versión de la aplicación
10. Todavía ingresado dentro de la cuenta deseada, [Crea un espacio de trabajo de producción](https://vtex.io/docs/recipes/development/creating-a-production-workspace) e [instala la aplicación](https://vtex.io/docs/recipes/development/installing-an-app);
11. Si todo está trabajando como lo esperado, [pasa el espacio de trabajo a master](https://vtex.io/docs/recipes/development/promoting-a-workspace-to-master).

## Modus Operandi 

Una vez la aplicación es desplegada e instalada en la cuenta, cada script contenido en ella será automaticamente enlazado a tu tienda y se utiliza para [construir las plantillas](https://help.vtex.com/tutorial/configure-template-in-smartcheckout-update--ToTE5XB39t0SwtHgpgwSv?locale=en#configuring-templates-from-the-code-menu) para personalizar tu checkout.

:Advertencia: **Los scripts usados en el Checkout serán enlazados al versión de Checkout UI Settings instalada en tu tienda**. Si una versión previa de la aplación fué instalada y quieres cambiar los scripts enlazados, necesitarás repetir el codigo existente y después de eso lazar la nueva versión de la aplicación que contiene solo los cambios que hiciste. El administrador es responsable de actualizar las versiones de la aplicación en las cuentas en donde esté instalada.