---
title: "Casa & video - Squad Rocket"
slug: "casaevideonewio-store-theme"
excerpt: "casaevideonewio.store-theme@2.5.26"
hidden: true
createdAt: "2022-07-06T11:00:30.429Z"
updatedAt: "2022-08-05T20:33:47.442Z"
---
_Plataforma: VTEX IO_

### First steps

- Clone this repository
- Run `yarn` on the root folder to install dependencies

## Regras básicas

- Utilizar sempre o **Prettier** para manter o código padronizado para facilitar a leitura e entedimento do mesmo.

- Manter os ambientes **sempre equalizados**. Ou seja, em caso de alterações emergenciais que pulem etapas de desenvolvimento, após a publicação em produção, equalizar os outros ambientes com as atualizações emergenciais realizadas;

- **Não** trabalhar sem uma tarefa correspondente, pois as hotfixes **obrigatoriamente** devem ser atreladas a uma tarefa;

## Setup de trabalho

- **Step 1:** Checkout do repositório remoto:

  ```
  $ git clone https://github.com/corebiz-global/casa-e-video.git
  ```

**Ao iniciar uma tarefa:**

- **Step 1:** Crie uma branch a partir da `develop` para manter todos os componentes e estilos que estão na master

  - Utilizamos do Git Flow para criar as branchs (feature/nome-da-feature, bugfix/nome-do-fix, Hotfix/versão-do-hotfix).

  - Caso sua demanda tenha um prioridade sobre outras que estão sendo executadas e precise fazer uma release exclusivamente para ela, crie a branch a partir da `master`, desta forma caso alguem tenha realiado um merge na branch `develop` não tera impacto na demanda que você está executando.

- **Step 2:** Ao finalizar a tarefa atualizar o `CHANGELOG` e abrir um PR para a `develop` e pedir a aprovação de um desenvolvedor que participa do projeto:

  - É importante manter o CHANGELOG sempre atualizado, pois desta forma facilitamos o entendimento do que foi executado na branch.

  - Deve ser criado um Pull Request para cada branch, dessa forma evitamos conflitos de código e mantemos o código sempre limpo.

- **Step 3:** Criar uma release:

  - Com todas as demandas finalizadas e a branch `develop` atualizada criar uma `Release/v0.0.0` onde `0.0.0` é a nova versão da release que está sendo publicada e deve possuir o mesmo valor da versão do manifest. Lembrando que utlizamos de versionamento semântico - https://semver.org/lang/pt-BR/

  - Criar um PR com a branch `Release/v0.0.0` apontando para a `master` e pedir aprovação de um dos Devs responsaveis pelo projeto.

  - Após a aprovação atualizar a tag no com o comando `git tag -a v0.0.0 -m "Release/v0.0.0"`, em seguida fazer um `git push` na tag, exemplo: `git push origin v0.0.0`

  - O último passo é acessa a `develop` e realizar um `git pull origin Master` na branch `develop`, desta forma atualizando a mesma com o conteudo da master, e em seguida um `git push origin develop` para atulizar a branch develop.

- **Step 4:** Caso exista a necessidade de fazer um `Hotfix`, ou seja, algum bug que não pode esperar o processo da release:

  - O `Hotfix` precisa ter um versionamento, exemplo: `Hotfix/0.0.1`, lembrando que hotfix são sempre algum ajuste de bug, desta forma seu versionamento sempre vai ser de nivel `PATCH` e deve alterar somente o ultimo numero da versão

  - Criar um PR com a branch `Hotfix/0.0.1` apontando para a `master` e pedir aprovação de um dos Devs responsaveis pelo projeto.

  - Após a aprovação atualizar a tag no com o comando `git tag -a v0.0.0 -m "Hotfix/v0.0.0"`, em seguida fazer um `git push` na tag, exemplo: `git push origin v0.0.0`

  - O último passo é acessa a `develop` e realizar um `git pull origin Master` na branch `develop`, desta forma atualizando a mesma com o conteudo da master, e em seguida um `git push origin develop` para atulizar a branch develop.

## Comandos Úteis

    $ vtex login

Faz login no ambiente da Vtex, passar a conta que irá usar no 'Account' e usar o e-mail de acesso.

    $ vtex workspace list

Lista todos os workspaces

    $ vtex workspace create nome-repositorio

Cria um workspace

    $ vtex workspace delete nome-repositorio

Apaga um workspace

    $ vtex workspace reset nome-repositorio

Apaga e recria o repositório (usar quando estiver tendo problemas de compilação)

    $ vtex workspace use nome-repositorio

Usar um workspace existente

    $ vtex link"

Faz link do workspace (componente local)

    $ vtex unlink vtex.service-example@0.x

Desvincula o componente local do workspace

    $ vtex browse

Abre uma aba no navegador do workspace linkado

    $ vtex whoami

Visualizar status atual (account, email, workspace)

## Requisitos do projeto:

- Git e GitFlow
  =- NPM _Versão: 3+_
- Node _Versão: 8+_
- Acesso ao ambiente [Casa&video](https://casaevideodigital.myvtex.com/)

## Links Úteis:

- [Instalação do Vtex CLI](https://vtex.io/docs/recipes/development/vtex-io-cli-installation-and-command-reference/)

- [Treinamento Vtex CoreBiz](https://www.youtube.com/watch?v=nH16vQvD0Mg) (Precisa estar logado no e-mail da empresa)

- [Treinamento de componentes](https://lab.github.com/vtex-trainings/store-framework)

- [Documentação Vtex](https://developers.vtex.com/docs)

- [Componentes de apoio da Vtex](https://github.com/vtex-apps)