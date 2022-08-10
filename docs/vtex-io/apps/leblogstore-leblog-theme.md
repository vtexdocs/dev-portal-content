---
title: "Leblog Store"
slug: "leblogstore-leblog-theme"
excerpt: "leblogstore.leblog-theme@1.4.8"
hidden: true
createdAt: "2022-07-08T19:48:55.677Z"
updatedAt: "2022-07-28T13:26:41.710Z"
---
![](https://img.shields.io/badge/-Mago%20Io%20LTDA-E43A65?style=flat&logo=cnpj) ![](https://img.shields.io/badge/platform-VTEX-E43A65)

Este é um repositório **Tema** para o [Store Framework](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-what-is-vtex-store-framework) do [VTEX IO](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-what-is-vtex-io).

Essas são as contas que utilizam o conteúdo desse repositório:

- [leblogio](https://leblogio.myvtex.com/)

### Requisitos

- [Git](https://git-scm.com/) - `latest`
- [Node](https://nodejs.org/en/) >= `16.13.2` (Dê preferência a uma versão **LTS**)
- [NPM](https://docs.npmjs.com/cli/npm) >= `6.14.15`
- [Yarn](https://yarnpkg.com/lang/en/) >= `1.22.18`
- [VTEX CLI](https://npmjs.com/package/vtex) - `latest`

## Guia de Começo

1. Clone este projeto

   ```bash
   git clone https://bitbucket.org/mago-io/leblogio/src/master/
   ```

2. Acesse a pasta

   ```bash
   cd leblogio
   ```

3. Instale as dependências do projeto

   ```bash
   yarn install
   ```

4. Instale o [Vtex Toolbelt](https://npmjs.com/package/vtex):

   ```bash
   npm i -g vtex
   ```

   Pode também ser instalado através do `yarn`:

   ```bash
   yarn global add vtex
   ```

5. Faça a autenticação através do comando:

   ```bash
   vtex login leblogstore
   ```

---

## Iniciando uma task

1. Entre na branch homolog

   ```bash
   git checkout homolog 
   ```

2. Atualize a branch local

   ```bash
   git pull
   ```

3. Crie sua branch a partir da homolog

   Utilizar o padrão de tipo semântico de commit com camelCase "**tipoDeAtualizacao/descricaoDaTask**" ou "**tipoDeAtualizacao/idDaTarefa**"

   ```bash
   git checkout -b "feat/updateHome"
   ```

4. Caso não esteja autenticado faça a autenticação através do comando:

   ```
   vtex login
   ```

5. Crie um novo workspace com um nome curto e descritivo da tarefa:

   ```
   vtex workspace create <nome>
   ```

6. Utilize o workspace criado:

   ```
   vtex workspace use <nome>
   ```

7. Faça o link para ficar **assistindo** os arquivos locais e enviá-los ao servidor remoto:

   ```
   vtex link
   ```

8. Utilize o comando em um terminal separado para abrir o link do seu workspace:

   ```bash
   vtex browse
   ```

   Será aberto um link com o seguinte padrão: `https://{NOME_DO_WORKSPACE}--{ACCOUNT}.myvtex.com`.

   Nele você poderá visualizar as modificações em tempo real.

## Boas Práticas

- CSS
  - [Breakpoints](https://styleguide.vtex.com/#/Styles?id=section-breakpoints)
- [Conventional commits](https://blog.cubos.io/que-tal-comecar-a-usar-commits-semanticos/#)
  - O repositório utiliza ferramentas como [commitlint](https://commitlint.js.org/#/), [husky](https://commitlint.js.org/#/) e [commitizen](https://commitizen-tools.github.io/commitizen/) para auxiliar e manter o padrão.
  - Referência: [Padronização de commit com (Commitlint, Husky e Commitizen)](https://dev.to/vitordevsp/padronizacao-de-commit-com-commitlint-husky-e-commitizen-3g1n)

## Concluindo uma task

Após a task ser homologada diretamente na sua workspace e estar pronta para deploy, o processo é o seguinte:

1. Navegue até a branch homolog

   ```bash
   git checkout homolog
   ```

2. Atualize a branch local, faça o merge e envie suas alterações para o repositório remoto

   ```bash
   git pull
   git merge feat/updateHome
   git push
   ```

---

## Processo de pré-deploy

Agora, realizaremos o processo da criação do pacote de instalação do VTEX IO, para que as alterações passem a fazer parte do código em produção. Dentro do Git Bash ou do Prompt de Comando (CMD), siga instruções a seguir.

Antes de inserir o conteúdo da branch homolog na branch premaster, é necessário realizar testes preventivos, para que possamos garantir que não haverá erros no site em produção, e faremos isso dessa forma:

1. Após estar na branch de homolog atualizada, acesse a workspace de homologação

   ```bash
   vtex use homolog
   ```

2. Limpe a workspace para teste(caso tenha muitas alterações antigas na workspace)

   ```bash
   vtex workspace reset 
   ```

3. Linke o repositório na workspace

   ```bash
   vtex link 
   ```

---

## Deploy

Após realizar todos os testes na workspace homolog, siga essas instruções para realizar o deploy:

1. Acesse a branch premaster

    ```bash
    git checkout premaster
    ```

2. Atualize a branch local e remota

   ```bash
   git checkout premaster
   git fetch
   git pull
   git merge homolog
   git push
   ```

Agora, deve-se ter em mente o nível de complexidade do que está sendo feito deploy. Caso seja uma quebra/atualização de API ou instalação de um APP que requer uma release major:

   ```bash
   vtex release major stable
   ```

   **Observação**: Para releases major é necessário uma outra step de migração dos dados do CMS para não perder o conteúdo cadastrado segundo a [documentação da vtex](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-migrating-cms-settings-after-major-update)

---
Caso seja algo muito complexo:

   ```bash
   vtex release minor stable
   ```

---
Caso seja apenas uma correção, com pouco impacto:

   ```bash
   vtex release patch stable
   ```

---
**Referência**: [**Documentação de deploy VTEX**](https://developers.vtex.com/vtex-developer-docs/docs/vtex-io-documentation-creating-a-production-workspace)

E continue seguindo o fluxo normalmente:

3. Crie uma workspace de produção para instalar o tema da loja

   ```bash
   vtex use premaster --production
   vtex install
   ```

Após instalar o tema é necessário esperar os 7 minutos de teste impostos pela VTEX, para dar prosseguimento

4. Depois dos 7 minutos, é possível realizar o deploy do tema

   ```bash
   #exemplo de nome do pacote: leblogio.leblog-theme@1.0.1
   vtex deploy <nome-do-pacote-gerado> 
   ```

5. E para finalizar o processo de deploy, é feito o promote da workspace

   ```bash
   vtex workspace promote
   ```

Após o processo de deploy, e validar em produção durante algum tempo o comportamento esperado, atualizar a branch master e a branch homolog com as novas features

   ```bash
   git checkout master
   git merge premaster
   git checkout homolog
   git merge master
   ```