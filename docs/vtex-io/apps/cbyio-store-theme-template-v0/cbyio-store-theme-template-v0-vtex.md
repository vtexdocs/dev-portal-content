---
title: "Passo 1: Instalar o CLI e baixar o template"
slug: "cbyio-store-theme-template-v0-vtex"
excerpt: "cbyio.store-theme-template@0.1.2"
hidden: true
createdAt: "2022-07-07T02:36:30.811Z"
updatedAt: "2022-07-07T02:36:30.811Z"
---
Comece instalando o cli da vtex em sua maquina.

```
yarn global add vtex
```

Faça o download do repositório do `StoreIO Boilerplate`.

```
git clone https://github.com/codeby-global/codeby.store-theme-template.git
```

## Passo 2 - Editando o `Manifest.json`

Uma vez que temos o repositório baixado, vamos editar o `Manifest.json` para que ele seja compatível com o StoreIO.

Quando estiver no arquivo voce deve trocar os valores do `vendor` e o `account`.

- `vendor`: E o nome da conta do cliente sendo o ambiente vtex
- `account`: Seria o nome do theme podendo ser o de sua escolha

```json
{
  "vendor": "storecomponents",
  "name": "my-test-theme"
}
```

## Passo 3 - Instalando o `apps` necessários

Para usar o `StoreIO Boilerplate`, é necessário instalar os apps padrões que serão utilizados no projeto.

```
vtex install
```

## Passo 4 - Desinstalando qual quer tema existente

Ao rodar o `vtex list`, voce pode verificar se existe algum tema ja instalado.

E comum ja conter algum instalando dentro da loja do seu cliente sendo ele `vtex.store-theme`

Caso seja encontrado na lista, desinstale-o, copiando seu nome da lista e utilizando o comando `vtex uninstall`. Segue o exemplo.

```
vtex uninstall vtex.store-theme
```

## Passo 5 - Rodando sua loja

Chegou a hora de rodar a sua loja com isso voce deve seguir os seguintes passos.

Na pasta raiz do seu projeto execute o comando `yarn install`, para que ele instale as dependências do seu projeto. Sendo que ao executar esse comando ele já ira instalar os pacotes da `StoreIO`, `React` e o seu `Checkout`. Também ja gerando a build do seus arquivos de `estilo` e do seu `checkout`.

Dentro do seu projeto voce tera dois comandos principais para seguir seu desenvolvimento, sendo eles:

- `yarn dev`: Roda a sua loja em modo de desenvolvimento compilando seus arquivos de estilos automaticamente
- `yarn dev:checkout`: Roda a sua loja com as mesma configurações que o `yarn dev`, mas so que também compilando o checkout-ui-custom

```
yarn dev
# or
yarn dev:checkout
```

Utilizando os comandos acima as suas alterações serão automaticamente compiladas e a sua loja rodará em modo de desenvolvimento.