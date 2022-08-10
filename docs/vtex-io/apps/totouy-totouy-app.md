---
title: "Realizar cambios en TOTO.UY"
slug: "totouy-totouy-app"
excerpt: "totouy.totouy-app@1.1.8"
hidden: true
createdAt: "2022-07-12T11:54:16.413Z"
updatedAt: "2022-07-13T11:53:03.311Z"
---
## Clonando el repositorio

## [Repositorio en GitHub](https://github.com/V473r10/totouy)

El proyecto utiliza GitFlow para el manejo de branches y SASS para compilar las hojas de estilo a CSS.

Una vez clonado el repositorio, en el directorio raíz, se debe ejecutar los siguiente comandos:

+ Git flow init  
  + (Aceptando todas las branches por defecto).
+ Npm i
  + Para instalar las dependencias.
+ Npm i -g sass  
  + Para instalar SASS globalmente.

Las hojas de estilos de react/ y react/components/ están en react/styles y react/styles/components respectivamente en archivos .scss.

Los estilos globales están en styles/scss.

### Importante:

Luego de instalar las dependencias, se debe ejecutar el comando:

+ Npm run sass
  + Dejarlo corriendo en segundo plano durante la edición para que se compilen en tiempo real los cambios en los SCSS.

<br/>

## Entendiendo el flujo de VTEX

Al clonar el proyecto, podremos ver que no es un proyecto con la estructura de React de toda la vida. No hay punto de inicio ni index.html.
El proyecto utiliza componentes de React, pero corre en el entorno de VTEX IO. Para manejarlo hay que aprender sobre el CLI de VTEX.

### Instalando el CLI de VTEX:

[VTEXCLI.EXE](https://vtex.io/vtexcli/install/win-x64)

Chequear la instalación con el comando VTEX

![VTEX Command](./img/VTEX.png)

Si el comando responde, iniciar sesión con el comando VTEX login.  
Cuando pida la cuenta, ingresar totouy. Esto abrirá el navegador para ingresar las credenciales.
Una vez ingresadas, el comando VTEX login responderá con un mensaje de bienvenida y podremos cerrar la pestaña del navegador.

![VTEX Login](./img/Login.png)

Chequear sesión con el comando VTEX whoami

![VTEX Whoami](./img/Whoami.png)

Con esto el CLI nos devuelve la cuental, el usuario y el workspace donde se está trabajando.

<span style="color: red; font-size: 24px; font-weight: 700; ">
¡PELIGRO!
</span>

<br/>

Por defecto, al iniciar sesión en VTEX, el CLI nos situa en el workspace Master de producción. Los cambios manuales en los workspaces de producción están PROHIBIDOS.  
Hay que cambiar a un workspace de desarrollo para realizar cambios. Para esto, se ejecuta el comando VTEX workspace use {nombre del workspace}. Indicando el nombre del workspace sin los corchetes, si el workspace seteado no existe, se crea automáticamente.

![Workspace](./img/Workspace.png)

Para estar seguros del cambio siempre se puede ejecutar el comando VTEX whoami

<br/>

## Sincronizar el proyecto local con el workspace de desarrollo.

Desde la consola, se debe navegar hasta el directorio raíz del proyecto que clonamos al comienzo. Una vez allí, se ejecuta el comando: VTEX link. 

![VTEX LinkResponsability](./img/Responsability.png)

El CLI nos pedirá que confirmemos un descargo de responsabilidad, es crucial que estemos seguros de que estamos en el workspace de desarrollo.

<br/>

Si el comando se ejecuta correctamente veremos un PipeLine como el siguiente y el proyecto será visible en la URL:

## '{workspace}--totouy.myvtex.com'

![Linked](./img/Linked.png)

<br/>

Se debe dejar corriendo esta tarea mientras se efectuan cambios para que sean visibles en la URL, junto con el watcher de SASS.  

<br/>
<br/>
<br/>

# Pasando a producción

Estando en el entorno de desarrollo con los cambios deseados listos para publicar, debemos actualizar la versión de la app del front con el comando VTEX release {tipo de actualización} {tipo de release}.

Antes de continuar, asegurarse de comitear todos los cambios, si el CLI detecta que hay cambios en sin comitear, aunque estén unstaged, devolverá error.

+ Tipos de actualización:
  De acuerdo a las convenciones del SemVer (Semantic Versioning), se puede actualizar la versión de la app con los siguientes tipos:
  + Major: Se debe utilizar solo cuando se realizan cambios incompatibles con la versión actual. Cambia el número de más a la izquierda. x.0.0.  
  + Minor: Se utilizan para cambiar o agregar funcionalidades que no afecten al funcionamiento de la versión actual. Cambia el número del medio. 1.x.0.  
  + Patch: Se utiliza, mayormente para corregir errores. Cambia el número del parche. 1.0.x.

+ Tipos de release:
  + Stable
  + Beta

Este comando lee el valor de la clave "version" del ~manifest.json~ e incrementa su valor de acuerdo al tipo de actualización indicado.

![SemVer](./img/SemVer.png)

El CLI pedirá que comfirmemos el release.

![Releasing](./img/Releasing.png)

En la documentación de VTEX, se detalla que luego de un release se debe publicar el mismo, con el comando VTEX publish. Sin embargo, el CLI lo hace automaticamente.

![Released](./img/Released.png)

Ahora se debe cambiar a un entorno de produccion que será el que promoverá los cambios al master.

Para crear uno nuevo, utilizar el comando VTEX use {nombre del workspace} --production.

![ProdWSpace](./img/ProdWSpace.png)

Instalar la versión de la app publicada anteriormente con el comando:
VTEX Install totouy.totouy-app@{version}

![Install](./img/Install.png)

Desplegarla
VTEX deploy totouy.totouy-app@{version}


![Deploy](./img/Deploy.png)

Una vez en este punto, el workspace está pronto para ser promovido al master, 
chequear que todo esté correcto en la URL:
{workspace}--totouy.myvtex.com

Y ejecutar el comando VTEX workspace promote.

![Promote](./img/Promote.png)