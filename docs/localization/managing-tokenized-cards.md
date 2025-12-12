---
title: "Managing tokenized cards"
slug: "managing-tokenized-cards"
hidden: false
createdAt: "2025-12-12T01:00:00.00Z"
---

A gestão de cartões tokenizados é um componente essencial em integrações de pagamento que exigem migração, verificação ou sincronização de dados entre sistemas. Para atender a esses cenários, a VTEX oferece os seguintes recursos:

   - Consulta a dados de cartões tokenizados
   - Importação de tokens externos na Card Token Vault (CTV)

> ⚠️ A tokenização de cartões está em fase de testes (Closed Beta), o que significa que apenas clientes específicos podem acessá-la no momento. Caso queira implementá-lo no futuro, entre em contato com nosso [Suporte](https://support.vtex.com/hc/pt-br/).

## Consultar informações de um cartão tokenizado

O gateway de pagamentos da VTEX disponibiliza um endpoint que permite recuperar informações não sensíveis dos cartões cadastrados de um cliente. A resposta a essa chamada inclui dados padrão do cartão, como bandeira, data de expiração e identificadores básicos e, caso o cartão possua um token previamente associado, também retorna os metadados relacionados a esse token.

Para consultar essas informações, utilize o endpoint [Get card data](https://developers.vtex.com/docs/api-reference/payments-gateway-api#get-/api/payments/pvt/account/-cardId-).

## Importar tokens na Card Token Vault (CTV)

A importação de tokens para a CTV é indicada em cenários de migração, quando tokens gerados e armazenados em um sistema externo precisam ser replicados no ambiente VTEX de forma estruturada e segura.

### Pré-requisitos

Antes de iniciar o processo de importação, verifique se você possui os itens abaixo:

   - Credenciais de autenticação válidas para acesso aos endpoints da [Card Token Vault API](https://developers.vtex.com/docs/api-reference/card-token-vault-api).
   - Arquivo `.XLSX` com tamanho máximo de 20 MB, contendo os dados necessários para cadastro do token. A primeira linha do arquivo `.XLSX` deve estar preenchida com os seguintes cabeçalhos:

| `accountName` | `providerId` | `profileId` | `paymentSystemName` | `cardFirstDigits` | `cardLastDigits` | `cardAddressType` | `cardAddressPostalCode` | `cardAddressStreet` | `cardAddressNeighborhood` | `cardAddressCity` | `cardAddressState` | `cardAddressCountry` | `cardAddressNumber` | `cardAddressComplement` | `cardHolderName` | `tokenType` | `tokenValue` | `tokenExpiration` | `tokenLabel` | `tokenProviderCardTokenId` | `tokenUseCvvForAuthorization` | `tokenHref` | `extraData` | `email` | `shopperId` |

> ℹ️ A coluna `extraData` deve conter informações no formato JSON ou conter um JSON vazio (`{}`).

> ⚠️ Cada conta pode realizar apenas uma importação por vez. Se um processo estiver em andamento, aguarde sua conclusão antes de iniciar uma nova importação.


## Realizando a importação

Siga as etapas abaixo para importar tokens na [Card Token Vault (CTV)](https://developers.vtex.com/docs/api-reference/card-token-vault-api):

1. Salve o arquivo `.XLSX` em um repositório local.
2. Envie as informações do arquivo `.XLSX` para a CTV utilizando o endpoint [Import card tokens](https://developers.vtex.com/docs/api-reference/card-token-vault-api#post-/api/card-token-vault/tokens/import). O retorno do campo `id` e do status code `202 Accepted` no response body da chamada indica que o arquivo foi recebido com sucesso.
3. Utilizando o `id` obtido no passo anterior, use o endpoint [Get card token import status](https://developers.vtex.com/docs/api-reference/card-token-vault-api#get-/api/card-token-vault/tokens/import/-importId-) para consultar o status de processamento dos dados do arquivo. Os possíveis valores de status são:
   - `CREATED`
   - `RUNNING`
   - `FAILED`
   - `DONE`

4. Repita as chamadas ao endpoint [Get card token import status](https://developers.vtex.com/docs/api-reference/card-token-vault-api#get-/api/card-token-vault/tokens/import/-importId-) até o status retornar a informação `DONE` ou `FAILED`.
   - Se o status retornar `FAILED`, obtenha o relatório de erros por meio do endpoint [Get card token import report](https://developers.vtex.com/docs/api-reference/card-token-vault-api#get-/api/card-token-vault/tokens/import/-importId-/report), corrija as informações no arquivo `.XLSX` e reinicie o processo de importação.
   - Se o status retornar `DONE`, a importação foi concluída com sucesso e nenhuma ação é necessária.