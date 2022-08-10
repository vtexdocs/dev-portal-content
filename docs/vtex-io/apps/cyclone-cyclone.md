---
title: "Store theme"
slug: "cyclone-cyclone"
excerpt: "cyclone.cyclone@0.1.7"
hidden: true
createdAt: "2022-07-05T19:51:49.762Z"
updatedAt: "2022-07-21T19:04:30.038Z"
---
Our boilerplate theme to create stores in the VTEX IO platform.

## Setting up the development environment

To understand how things work check the tutorial [Set up the development environment](https://vtex.io/docs/getting-started/build-stores-with-store-framework/1/)

## Dependencies

All store components that you see on this document are open source too. Production ready, you can found those apps in this GitHub organization.

## VTEX Documentations

-   [VTEX Docs](https://developers.vtex.com/vtex-developer-docs/docs/welcome)

Store GraphQL is a middleware to access all VTEX APIs.

-   [Store GraphQL](https://github.com/vtex-apps/store-graphql/blob/master/docs/README.md)

## Getting Started

-   First create a branch for the feature you are developing with `git checkout -b task-number/name-of-the-feature`, **always make sure you are updated with the master branch with `git pull origin master`**. After this you can start making changes to the code.

-   After you login into VTEX environment, you will need to create a workspace to develop. To do this run `vtex use {workspacename}`. As pattern for development workspaces we use the workspace name as "task(task-number)" like "task7119". After creating your workspace link it using `vtex link` on your terminal. **Important: the changes you make in a development workspace won't be kept when you switch to production workspace**

-   Once you are satisfied with all changes, you can make a release to install your app in a production workspace. For this run `vtex use {workspacename} --production`. As pattern for production workspaces we use "task(task-number)p" like "task7119p". **Always commit and push your changes into the branch you are working before making a release**. After this, you can follow this instructions [Releasing an app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-releasing-a-new-app-version#step-by-step). Once you are done with the release, install the app at the production workspace. The changes you make in the VTEX admin will be kept. Once you are allowed to promote the production workspace to the store run `vtex promote`.

-   Once your work is done, merge the branch you worked into the master branch through pull request, don't forgetting to delete the remote branch on the request. After your work has been merge into the master branch run `git checkout master` and then `git pull origin master` to update the master branch on your computer.

-   After this process you will need to run `git branch --list` to locate the branch you have worked on and then delete it with `git branch -D name-of-the-branch`.

-   Also delete the development workspace on vtex you have worked in to keep it cleaner. Run `vtex workspace list` to locate the development workspace you have worked, also make sure you are not using this workspace, otherwise you won't be able to delete it. To delete a workspace run `vtex workspace delete {workspacename}`.

## Project patterns

-   For every feature or component, create a corresponding folder inside the areas of the projects they belong. It means, for example, if you need to create a banner or
    a similar feature for the Home area of the website, you will make a folder inside the "home" folder and declare the main block of code inside the home.jsonc in the order it needs to appear, and inside the folder you've created for your banner you'll create a file that declares what this block is responsible to do. This way the code gets more cleaner and more sustainable.

-   For SCSS for every feature/component you will create a folder inside "components" folder at SCSS folder, that is contained at styles folder, where you will develop your SCSS code. The files for you SCSS needs to be written with an "_" before the name. For example: _newsletter-flex (for flex-layout). Then, inside the file vtex.flex-layout you will import this file with a comment up and above the import, and inside this comment you will need to declare the name of the feature you are importing and the end of the import. To import use @include "./components/.....". Example on vtex.flex-layout.scss:

-   When creating a block of code, you need to specify the block of code and make sure it doesn't repeat itself in other areas, as well as the blockClass. For that use "#" after the component name as the example:

```
"flex-layout.col#name-i-desire":{
    "props":{
      "blockClass": "classname-i-desire"
    },
    "children": []
}
```

**IT'S VERY IMPORTANT TO DECLARE THE BLOCKCLASS TO STYLE IN VTEX-IO**

```
/******* Newsletter ******/

@include './components/newsletter-flex'

/******* End of Newsletter ******/
```

Also, when you have repeated classes such as flexRow, flexCol or other classes from vtex write your code following this pattern:

```
flexCol{
  &--name-of-the-blockclass{
  // your css code here

    // when you have other descendents:
    &:hover{

    }

    &:first-child{
      // when you have code and/or media queries
        // your css code here
        @media .....{ 

        }
    } 
  
  // when you have media queries
    @media .....{

    }
  }
  
  &--name-of-the-other-blockclass{
    // your css code here
    // when you have media queries
    @media .....{

    }
  }
}
```

**IMPORTANT: NEVER use :global(.vtex....) outside a blockclass and nested classes, this can break the code through the whole page**

-   Avoid files with too many lines, to keep the code sustainable. If necessary create more files inside their respective folder.

-   To run your SCSS you need to install gulp globally (for this run `npm i -g gulp`), and run `gulp` at the command line, so it can watch changes at the SCSS files. If you have imported your files correctly it will compile them into css, that will be seen at the linked store.

-   Images: place them inside the assets folder located at the root of the project in their respective place. To use them on your project use `assets/path-to-the-image/image-name.*`. To use them inside your SCSS use `url(assets/path-to-the-image/image-name.*)`.

## Custom components

-   For custom components you will develop them at the react folder, using typescript to code them. If you need inputs comming from the admin area, you will need to create a schema to export the data of your component to the site-editor panel.

-   To style you component, avoid using css. Use styled components instead. You will need to install styled components as a dev dependency. To do this, navigate to your react folder and run `npm install --save styled-components` and then you will need to import it on your component in order for it to work. If you don't know how to use this library go to: [Styled Components Docs](https://styled-components.com/docs).

-   Don't forget to run `npm i` to install all the dependencies and run `vtex setup --typings` to set up your typescript correctly. **Make sure you are in the react folder while running this commands**. After this refresh your code editor.

**IMPORTANT: The name you chose exporting your component will be the same one to import it into interfaces.json, where first you will declare the name of the component to use it in your jsonc files and inside this declaration the component prop that you will declare must be exactly the name you have exported your custom component. ALWAYS export components in camel case, with the first letter in uppercase.**

-   This is an example of how to export custom components to the site editor:

```
FalarComSuporte.schema = {
  title: 'Fale com o suporte',
  description: 'Componente para abrir o chat do suporte ao cliente',
  type: 'object',
  properties: {
    href: {
      title: 'Link para redirecionar ao suporte',
      description: 'Endereço para o suporte ao cliente',
      type: 'string',
      default: "/"
    }
  }
};

```

-   Images: Import them using the relative path to the assets folder, located at the root of the project. Place your images according to it's functions on the store. Example: ``Import cartao from '../../../assets/icons/cartao.svg` and use them like `<img src={cartao}>`

### Partner's Apps

-   [Facebook Pixel](https://github.com/vtex-apps/facebook-pixel/blob/master/docs/README.md)
-   [Google Tag Manager](https://github.com/vtex-apps/google-tag-manager/blob/master/docs/README.md)

---

# Store theme

Nosso boilerplate para desenvolver lojas em VTEX IO

## Ajustando o ambiente de desenvolvimento

Para entender como funciona o ambiente de desenvolvimento siga este link [Ajustando o ambiente de desenvolvimento](https://vtex.io/docs/getting-started/build-stores-with-store-framework/1/)

## Dependencias

Todos os componentes desse documento são open source. Você pode encontrá-los no github.

## Documentação VTEX IO

-   [VTEX Docs](https://developers.vtex.com/vtex-developer-docs/docs/welcome)

Store GraphQL is a middleware to access all VTEX APIs.

-   [Store GraphQL](https://github.com/vtex-apps/store-graphql/blob/master/docs/README.md)

## Iniciando

-   Primeiro crie uma branch para a feature que está desenvolvendo com `git checkout -b numero-da-task/nome-da-feature`, **sempre tenha certeza de que sua branch está atualizada comm a branch master, para isso execute `git pull origin master`**. Depois desse processo você já poderá trabalhar com código.

-   Depois de efetuar login na VTEX, você precisará criar um workspace de desenvolvimento. Para isso execute `vtex use {workspacename}`. Como padrão para workspaces de desenvolvimento utilizamos "task(numero-da-task)" como "task7119". Depois de ter criado seu workspace, faça o link do seu projeto com `vtex link` no seu terminal. **Importante: as mudanças feitas em ambiente de desenvolvimento não irão para o ambiente de produção**

-   Uma vez que esteja satisfeito com as alterações, você pode fazer um release da app para instalar em um ambiente de produção, onde não será mais possível linkar. Para criar um ambiente de produção execute `vtex use {workspacename} --production`. Como padrão para workspaces de produção utilizamos "task(numero-da-task)p" como "task7119p". **Sempre faça commit and push das alterações antes de fazer o release**. Depois de ter criado seu workspace, siga essas instruções [Releasing an app](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-releasing-a-new-app-version#step-by-step). Feito o release, instale a app no workspace de produção. As mudanças feitas pelo admin desse workspace serão mantidas, e uma vez que você estiver autorizado a lançar as mudanças para a loja (workspace master) execute `vtex promote`.

-   Depois de ter promovido o seu ambiente de produção para a loja, junte sua branch com a master do repositório via pull request, não esquecendo de marcar a opção de deletar a branch remota. Depois de unificar a branch no repositório remoto execute `git checkout master` e `git pull origin master` para atualizar a branch master na sua máquina.

-   Depois deste processo execute `git branch --list` para localizar a branch que você trabalhou e deletá-la com `git branch -D name-of-the-branch`.

-   Também delete o workspace de desenvolvimento na vtex, para que sempre esteja o mais limpo possível. Para isso execute `vtex workspace list` para localizar o seu workspace de desenvolvimento, garantindo que ele não esteja sendo utilizado, caso contrário você não conseguirá deletá-lo. Para deletar um workspace execute `vtex workspace delete {workspacename}`.

## Padrão de projeto

-   Para cada feature ou componente, cria uma pasta dentro da área a qual ela pertence. Por exemplo, se você precisa criar um banner ou outro componente para área de home do website, você criará uma pasta dentro da pasta "home", contendo o nome da feature e um arquivo .jsonc para seu desenvolvimento, que detalhará o que você declarou no arquivo home.json. Você precisará inserir dentro deste arquivo a parte inicial da feature na ordem correta de renderização.

-   SCSS: para cada componente ou feature você criar uma pasta dentro de "components" localizada na pasta styles/scss. Os arquivos que você escreverá deverão ter o nome iniciado por "_" Por exemplo: _newsletter-flex (for flex-layout). Então dentro vtex.flex-layout você importará o arquivo com comentários com o nome da feature/componente acima e abaixo da importação. Para importar um arquivo _nome.scss use @include "./components/nome-da-feature/nome.scss". Exemplo em vtex.flex-layout.scss:

-   Quando criar um bloco de código, você precisa garantir que ele não se repita em outras áreas do código, bem como sua blockClass, a menos que deseje o mesmo estilo em outros lugares. Para isso você usar "#", seguido do nome desejado, e para o blockClass será declarado dentro das props do componente. Exemplo:

```
"flex-layout.col#nome-de-sua-escolha":{
    "props":{
      "blockClass": "nome-da-classe-de-sua-escolha"
    },
    "children": []
}
```

**É DE SUMA IMPORTÂNCIA DECLARAR BLOCKCLASS POIS ELE É O QUE DIFERENCIA O CSS DE UM COMPONENTE PARA OUTRO**

```
/******* Newsletter ******/

@include './components/newsletter-flex'

/****** End of Newsletter ******/
```

Também, quando ocorrem repetições de classes da vtex como flexRow, flexCol ou outras classes escreva o código no seguinte padrão:

```
flexCol{
  &--name-of-the-blockclass{
  // seu código css 

    // outros descendentes da mesma classe
    &:hover{

    }

    &:first-child{
    // código e/ou media queries
      // seu código css
      @media ...
    }

  // media queries
    @media ... {

    }
  }

  &--name-of-the-other-blockclass{
    // seu código css aqui
  }
}
```

**IMPORTANTE: NUNCA use :global(.vtex....) fora de uma blockclass ou classes aninhadas, isso pode gerar quebrar por toda a página**

-   Evite arquivos com muitas linhas, mantenha o código sustentável. Caso haja necessidade, quebre o código em mais arquivos dentro da mesma pasta.

-   Para compilar os arquivos SCSS instale o gulp globalmente (para isso execute `npm i -g gulp`), e execute `gulp` na linha de comando para que ele observe e compile as alterações quando salvas. Se você importou corretamente seu arquivos para os arquivos vtex.....scss, você verá as alterações na loja após o estabelecimento do link.

-   Imagens: coloque as imagens na pasta assets, localizada na raiz do projeto, em seus respectivos lugares. Para usá-las em seu projeto use `assets/path-to-the-image/image-name.*` e para usá-las em seu SCSS use `url(assets/path-to-the-image/image-name.*)`.

## Componentes customizáveis

-   Os componentes customizáveis são desenvolvidos dentro da pasta react, com o uso de typescript. Se você precisar de dados de entrada vindos do admin, você precisará criar um schema para que possa ser incluído no site-editor.

-   Para estilizar um componente, evite usar css. Use styled components. Você precisará instalar o styled-components como dependencia de desenvolvimento. Para isso navegue até sua pasta react e execute `npm install --save styled-components`. Para utilizar o componente será necessário que você importe a biblioteca no seu componente react.
    Para dúvidas acesse a documentação da biblioteca [Styled Components Docs](https://styled-components.com/docs).

-   Não esqueça de executar `npm i` para instalar todas dependencias e execute `vtex setup --typings` para rodar o setup do typescript. **Garanta que você está na pasta react ao executar estes comandos**. Após isso recarregue a janela do seu editor de código.

**IMPORTANTE: O nome que você escolheu ao exportar o componente será o mesmo para importá-lo no interfaces.json, onde primeiro você declarará o nome do bloco customizado a ser utilizado nos arquivos jsonc e após na prop "component" você declarará o componente exatamente como exportou. SEMPRE exporte componentes em camel case, com a primeira letra em maiúsculo**

-   Esse é um exemplo de como exportar componentes para o site editor (schema):

```
FalarComSuporte.schema = {
  title: 'Fale com o suporte',
  description: 'Componente para abrir o chat do suporte ao cliente',
  type: 'object',
  properties: {
    href: {
      title: 'Link para redirecionar ao suporte',
      description: 'Endereço para o suporte ao cliente',
      type: 'string',
      default: "/"
    }
  }
};
```

-   Imagens: Importe-as utilizando o caminho relativo para a pasta assets, localizada na raiz do projeto. Salve as imagens em suas áreas correspondentes. Exemplo de importação: `Import cartao from '../../../assets/icons/cartao.svg` Exemplo de uso: `<img src={cartao}>`

### Apps de parceiros

-   [Facebook Pixel](https://github.com/vtex-apps/facebook-pixel/blob/master/docs/README.md)
-   [Google Tag Manager](https://github.com/vtex-apps/google-tag-manager/blob/master/docs/README.md)