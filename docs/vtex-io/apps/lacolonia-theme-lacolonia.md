---
title: "Lacolonia - Squad Evolutivo Corebiz"
slug: "lacolonia-theme-lacolonia"
excerpt: "lacolonia.theme-lacolonia@0.1.45"
hidden: true
createdAt: "2022-07-21T23:49:21.341Z"
updatedAt: "2022-07-21T23:49:21.341Z"
---
*Plataforma: VTEX IO*




# Fluxo de trabalho

- Este repositório usa o [GitFlow](https://danielkummer.github.io/git-flow-cheatsheet/index.html) como apoio ao fluxo de criação de branches. Porém deste, utilizaremos apenas os **hotfixes** **feature** e **fix**.

## Regras básicas

- Manter os ambientes **sempre equalizados**. Ou seja, em caso de alterações emergenciais que pulem etapas de desenvolvimento, após a publicação em produção, equalizar os outros ambientes com as atualizações emergenciais realizadas;

- **Não** trabalhar sem uma tarefa correspondente, pois as hotfixes **obrigatoriamente** devem ser atreladas a uma tarefa;

- A branch **master** existirá apenas no repositório local. Ou seja, não deverá ser executado o comando **git push** na branch **master** ;

	- ***Nota:*** Em caso de uma publicação acidental desta branch, executar o comando a seguir imediatamente:
		
		```
		$ git push --delete origin develop
		```


- Sempre atualizar as branches antes de iniciar ou finalizar o trabalho. Ou seja:
	- Antes de iniciar um **hotfix** (feature/fix), atualizar a branch **develop**;
	- Antes de continuar o trabalho em um **hotfix**, atualizar a branch do **hotfix** em questão;
	- Antes de finalizar para produção um **hotfix**, atualizar a branch **master**;

- Se, porventura, houver alguma dúvida sobre as alterações feitas pelos comandos do GitFlow, **não** realizar o comando *git push* até que as dúvidas tenham sido sanadas;

	- ***Nota:*** Caso aconteça algo incorreto, ainda teremos a versão no **remote repository** intacta.

## Setup de trabalho

- **Step 1**: Checkout do repositório remoto:
	
	```
	$ git clone https://github.com/corebiz-global/Big-Supermercados.git
	```

- **Step 2**: GitFlow init:
	
	```
	$ git flow init -d
	```

	
	```
	$ git checkout master
	```

	- ***Nota:*** Após o init, a branch atual será a **develop**. Lembrando que, como definido nas regras, **não faremos commits e pushes** nesta branch, por isso o git checkout master.



Ao iniciar uma tarefa:

- **Step 1:** Verificar se o hotfix desta tarefa já não foi criado anteriormente e fazer o checkout + pull deste hotfix. Ou criar o hotfix com o comando:

	```
	$ git flow feature start {{nome_descritivo_em_snake_case}}
	```
	Ou no caso de um ajuste:
	```
	$ git flow fix start {{nome_descritivo_em_snake_case}}
	```

- **Step 2:** Publicar imediatamente a feature/fix:

	```
	$ git flow feature publish
	```
	Ou no caso de um ajuste:

	```
	$ git flow fix publish
	```

- ***Dica:*** Caso não se lembre quais os arquivos alterados na branch no momento da publicação. Use o seguinte comando na branch hotfix para obter essa listagem:
	
		```
		$ git diff master...HEAD --name-status .
		```

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
- Conhecimento em [ReactJS](https://pt-br.reactjs.org/docs/getting-started.html)
- NPM *Versão: 3+*
- Node *Versão: 8+*
- Acesso ao ambiente [Teste](https://bigqa.myvtex.com)

## Links Úteis:

- [Instalação do Vtex CLI](https://vtex.io/docs/recipes/development/vtex-io-cli-installation-and-command-reference/)

- [Treinamento Vtex CoreBiz](https://www.youtube.com/watch?v=nH16vQvD0Mg) (Precisa estar logado no e-mail da empresa)

- [Treinamento de componentes](https://lab.github.com/vtex-trainings/store-framework)

- [Documentação Vtex](https://developers.vtex.com/docs)

- [Componentes de apoio da Vtex](https://github.com/vtex-apps)

Redator: [Matheus Guerra de Andrade](https://github.com/matandwar) e [David Bitencourt](https://github.com/DavidBitencourt)