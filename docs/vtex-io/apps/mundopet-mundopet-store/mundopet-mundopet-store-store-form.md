---
title: "Store Form com Master Data v2 e Vtable"
slug: "mundopet-mundopet-store-store-form"
excerpt: "mundopet.mundopet-store@0.43.7"
hidden: true
createdAt: "2022-07-04T22:14:39.854Z"
updatedAt: "2022-08-09T14:48:44.543Z"
---
Esse artigo explica como utilizar o componente *store form* com a entidade de dados no master data v2. E como usar a interface vtable para visualizar os dados.

## Master Data v2

Antes de desenvolver os blocos do componente, precisamos criar a entidade e esquema json no master data v2, utilizando a ferramenta [postman](https://www.postman.com/).

Se adicionar os blocos do componente *store form* antes de ter a entidade(MDv2), será renderizado o seguinte erro:
[Erro](https://i.ibb.co/Xt2GrWb/erro1.png)

Logo devemos criar o esquema json de acordo com a [documentação](https://vtex.io/docs/recipes/templates/creating-a-native-form-for-your-store-users/).

[Esquema JSON](https://i.ibb.co/6F5w669/exemplo-esquema.png)

Na ferramenta postman basta adicionar a seguinte rota:
```curl
  curl --request PUT \
  --url https://account_name.myvtex.com/api/dataentities/data_entity_name/schemas/schema_name \
  --header 'content-type: application/json'
```

Pontos importantes na configuração da [API Save schema by name](https://developers.vtex.com/reference/schemas#saveschemabyname):
- account_name
- data_entity_name
- schema_name
- x-vtex-api-appKey
- x-vtex-api-appToken	

[Import](https://i.ibb.co/82MY9xj/import.png)
[Send](https://i.ibb.co/WDzmbFz/send.png)

Conforme realizamos todos os passos basta clicar em **Send**. 🚀

## Aplicativo Store Form

Com a entidade criada no master data v2 podemos implementar o formulário. Portanto temos que criar os blocos conforme a [documentação](https://github.com/vtex-apps/store-form/blob/master/docs/README.md).

![Form](https://i.ibb.co/CKTp2BF/form.png)

Onde o documento será salvo:
- entity
- schema

## Interface VTable

Podemos utilizar a interface vtable para renderizar os dados do master data. Para criar o aplicativo temos que montar o seguinte esquema json:

[Configurações de esquema JSON](https://help.vtex.com/tutorial/vtable--35ygHE0Ohaw46Si2MSEAE4)

[Validação dos objetos](https://i.ibb.co/jyK44Zj/valida-o.png)

[JSON VTable](https://i.ibb.co/qMkmmXN/vtable.png)

[Exemplo](https://ibb.co/86NDfwQ)

Considerações importantes:
- entity 
- model
- fields
- list
- editor

> Em **entity** temos que adicionar o nome da entidade que contém os dados. Enquanto em **model** é o esquema relacionado à entidade... 

Desse modo precisamos salvar o aplicativo na seguinte rota:

```url
https: // {{AccountName}} .vtexcommercestable.com.br / api / dataentities / vtable / documents / {{app-name}}? _schema = app
```

O **app-name** é o nome que está no código json do seu aplicativo. 

Agora precisamos **Send** via postman, conforme realizamos no início do artigo. 🚀

- Devemos importa a url na ferramenta postman
- Adicionar o código json no body
- x-vtex-api-appKey
- x-vtex-api-appToken	

## Menu da plataforma VTEX

Como adicionar seu aplicativo Vtable no menu da plataforma. 

- [Admin-navigation](https://github.com/vtex/admin-navigation) 
- [Admin-example](https://github.com/vtex-apps/admin-example).

Antes de criar os arquivos de acordo com à documentação, você deve preencher esse formulário da VTEX, para adquirir as permissões necessárias.

[Formulário para adquirir permissões de builders](https://docs.google.com/forms/d/e/1FAIpQLSfhuhFxvezMhPEoFlN9yFEkUifGQlGP4HmJQgx6GP32WZchBw/viewform)

Depois de **um dia** você estará com as permissões de builders

![Builders](https://i.ibb.co/Scm9C0m/builders.png)

**Possíveis erros**

Caso apresente esse erro no seu terminal é porque você ainda não recebeu a confirmação da VTEX:

`
00:00:04.812 - error: API: 403 Forbidden  
00:00:04.813 - error: Source: https://app.io.vtex.com/vtex.builder-hub/v0/mundopet/scroll/_v/builder/0/link/mundopet.x-mundopet-store@0.17.1  
00:00:04.814 - error: Method: post  
00:00:04.814 - error: Message: Account mundopet is not allowed for developing app "x-mundopet-store" in major 0.
You can request access by going to https://forms.gle/f7bYdTA7tfdfB5tt7 .
Find further info at https://vtex.io/docs/releases/2020-02/vtex-io-closed-beta-list  
00:00:04.817 - error: ErrorID: a927c15c0d489e3796f48104a4581280  
`

Se você preencher os dados do formulário com os campos incorretos, vai ter que entrar em contato com à VTEX novamente. É necessário adicionar exatamente os nomes que estão no arquivo **manisfest**.

Erro de **app build**:
`
00:31:17.640 - info: Build accepted for mundopet.mundopet-store@0.17.1 at mundopet/scroll vtex.builder-hub@0.264.4  
00:31:17.729 - error: App build failed with message: Builder "admin" at version range 1.x is not supported by vtex.builder-hub@0.264.4  
`

Solução:
`
 "builders": {
    "admin": "0.x"
  }
`

Depois de tudo estar configurado devemos seguir a documentação e adicionar os arquivos na pasta **admin**:
- navigation
- routes


Navigation:
`
{
    "section": "accountSettings",
    "titleId": "admin.navigation.label-vtable",
    "subSectionItems": [
        {
          "labelId": "admin.navigation.vtable",
          "path": "/admin/vtable/{entity_interface_vtable}"
        }
    ]
}
`

Routes:
`
  "admin.app.vtable": {
    "component": "Vtable",
    "path": "/admin/app/vtable/:type"
  }
}
`

Agora devemos adicionar na pasta **messages** os arquivos **en.json** e **pt.json**:

{
    "admin.navigation.label-vtable": "Interface VTable",
    "admin.navigation.vtable": "Dúvidas"
}

![Menu](https://i.ibb.co/ByS3HRM/duvida.png)
[Vtable](https://i.ibb.co/0Vz8jgH/resultado.png)