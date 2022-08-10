---
title: "Backend App - Hiring Coders #3 - Casa Atmosphere 03"
slug: "atmosphere-orderhook-atmosphere-03"
excerpt: "atmosphere.orderhook-atmosphere-03@0.0.2"
hidden: true
createdAt: "2022-07-18T22:45:18.151Z"
updatedAt: "2022-07-21T01:30:04.434Z"
---
Aplicação responsável por observar novos pedidos, calcular quantos pontos de recompensa o cliente receberá e consumir uma API para atualizar este valor no Master Data da VTEX.

**O app já está instalado no workspace `squad3`, não sendo necessário rodar `vtex link` na pasta backend separadamente.**

Aguarde de 10 a 15 segundos após o fechamento de um pedido para que o pagamento seja autorizado.
**Por não ser uma loja real, recomendamos pagar via "Promissória"**, configurada para autorizar o pagamento automaticamente.

Dito isso, para fins de desenvolvimento, segue abaixo o passo a passo:

### Executando o app

1. Acesse a pasta 'backend' pelo terminal/console.
2. `$ vtex login atmosphere`
3. `$ vtex use squad3`
4. `$ vtex link`
5. Abra outro terminal, mantendo o anterior aberto
6. Acesse a pasta raíz do repositório ('hiring-coders-atmosphere-03' por padrão)
7. `$ vtex link`