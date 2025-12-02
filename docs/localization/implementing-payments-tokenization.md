---
title: "Implementing payments tokenization"
slug: "implementing-payments-tokenization"
hidden: false
createdAt: "2025-12-01T00:00:00.00Z"
---

A tokenização de pagamentos é a solução da VTEX que permite aos provedores realizar transações de pagamento utilizando [tokens](https://help.vtex.com/docs/tutorials/dpan-and-fpan-understanding-security-in-the-online-tokenized-payment-flow) em vez de dados reais de cartão de crédito. Essa abordagem adiciona uma camada de segurança ao processo, reduzindo a exposição de informações sensíveis e o risco de fraudes ou ataques.

> ⚠️ Esta funcionalidade está em fase de testes (Closed Beta), o que significa que apenas clientes específicos podem acessá-la agora. Caso queira implementá-lo no futuro, entre em contato com nosso [Suporte](https://support.vtex.com/hc/pt-br/).

## Benefícios e funcionalidades

A tokenização possibilita:

- **Integrar sistemas PCI e não-PCI:** permite importar ou exportar cartões tokenizados entre ambientes compatíveis com PCI (como o gateway VTEX) e sistemas não-PCI de clientes, como ERPs ou plataformas corporativas de compras (B2B).
- **Atualização automática de tokens:** atribui automaticamente novos tokens quando um cartão de crédito expira e é substituído por outro, melhorando a experiência do cliente, especialmente em cenários específicos de compras recorrentes, como as de assinaturas.

> ℹ️ A VTEX não gera nem solicita tokens de outros serviços, apenas armazena tokens importados diretamente na Card Token Vault (CTV) ou retornados por um provedor de pagamentos na resposta de uma autorização.

> ⚠️ A tokenização de pagamento está disponível somente para lojas com checkout na arquitetura [Headless](https://developers.vtex.com/docs/guides/store-architecture#headless) e [FastCheckout](https://newhelp.vtex.com/en/announcements/2024-04-03-fastcheckout-boost-your-conversion-with-the-new-checkout). O recurso foi projetado para suportar tokens proprietários de provedores de pagamento, permitindo também o uso de Network Tokens quando o conector opera como Token Requester e envia o token de volta à VTEX.

## Etapas de implementação

Para disponibilizar a funcionalidade de tokenização aos seus clientes, o provedor de pagamento deve executar as seguintes etapas:

1. [Atualizar o manifesto do conector](#atualizando-o-manifesto-do-conector)
2. [Configurar o envio de informações tokenizadas](#configurando-o-envio-de-informacoes-tokenizadas)
3. [Integrar o sistema da Card Token Vault (CTV)](#integrando-o-sistema-card-token-vault-ctv)
4. [Validar a implementação da tokenização](#validando-a-implementacao-da-tokenizacao-de-pagamentos)

### Atualizando o manifesto do conector

O provedor de pagamento deve incluir os seguintes campos no manifesto do conector:

| **Campo** | **Mandatório** | **Tipo** | **Descrição** |
| --- | --- | --- | --- |
| `version` | Yes | string | Indicates the version of the [Payment Provider Protocol (PPP)](https://help.vtex.com/pt/docs/tutorials/payment-provider-protocol) to be used in requests. The default value is `1.0.0`. For card tokenization operations, use the value `2.0.0`. |
| `cardToken` | No | object | Object containing information required for card tokenization operations. This object and all its nested fields are mandatory only when the `version` field is set to `2.0.0`. |
| `canAcceptCardToken` | No | boolean | Indicates whether the payment provider can process tokenized cards. |
| `cardTokenAcceptedTypes` | No | array | Indicates the types of tokens accepted by the payment provider. Possible values are: `TOKEN_FILE`, `TOKEN_CLIENT_ID`, and `TOKEN_VALUE`. |
| `cardGenerateCardToken` | No | boolean | Indicates whether the payment provider can generate a new card after processing a PAN card. |

Exemplo de manifesto com tokenização habilitada:

```json
{
…
  "version": "2.0.0",
  "cardToken": {
    "canAcceptCardToken": true,
    "cardTokenAcceptedTypes": ["TOKEN_VALUE"],
    "canGenerateCardToken": true
  }
…
}
```

> ⚠️ Após revisar o manifesto, [abra um chamado](https://newhelp.vtex.com/pt/docs/tutorials/abrir-chamados-para-o-suporte-vtex) no Suporte Técnico da VTEX para solicitar a atualização do conector.

### Configurando o envio de informações tokenizadas

Além da atualização do manifesto, é necessário incluir campos específicos em endpoints do [Payment Gateway](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments) e do ´[Payment Provider Protocol](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments), conforme o tipo de cartão de crédito utilizado na transação tokenizada.
Os tipos de cartões são classificados da seguinte forma:

- **Cartões com PAN ([Primary Account Number](https://en.wikipedia.org/wiki/Payment_card_number)):** cartões ainda não tokenizados na Card Token Vault (CTV).
- **Cartões tokenizados salvos na VTEX:** cartões já armazenados na CTV e que estão sendo utilizados novamente em uma transação de pagamento.
- **Cartões tokenizados externos:** cartões tokenizados e armazenados em sistemas externos, que podem ou não ser posteriormente salvos na VTEX.

A seguir, são apresentados exemplos de requisições e respostas para cada cenário de transação de pagamento.

#### 1º Cenário: transação com cartão de crédito com PAN

- Payment Gateway ([Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments))

     - **Request body:** não envia campos específicos para tokenização.

     - **Request body:** campos recebidos sobre a tokenização.

```json
[
…
"fields": [{
    "name": "accountId",
    "value": "string"
	}
     …
    ]
…
]
```

- Payment Provider Protocol ([Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments))

     - **Request body:** campos enviados para tokenização.

```json
{
…
    "saveCreditCard": true,
    "useCardToken": true
…
}
```

     - **Response body:** campos recebidos sobre a tokenização.

```json
{
…
    "isNewTokenization": true,
    "generatedCardToken": {
        "cardTokenType": "TOKEN_VALUE",
        "cardTokenHref": "string",
        "tokenExtraData": {
            "extraData1": "string",
            "extraData2": "string"
       },
       "useCvvForAuthorization": true
   }
…
}
```

> ℹ️ Quando o campo `saveCreditCard` é enviado com o valor `false` no request body do [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments?endpoint=post-/payments) endpoint, as informações do cartão de crédito não são armazenadas na VTEX e o response body não retorna dados relacionados à tokenização.

#### 2º Cenário: transação com cartão de crédito tokenizado salvo na VTEX

- Payment Gateway ([Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments))

     - **Request body:** campos enviados para tokenização.

```json
[
…
"fields": {
      "accountId": "string"
    }
…
]
```

     - **Response body:** campos recebidos sobre a tokenização.

```json
[
…
"fields": {
    "name": "accountId",
    "value": "string"
	}
     …
    ]
…
]
```

- Payment Provider Protocol ([Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments))

     - **Request body:** campos enviados para tokenização.

```json
{
…
    "saveCreditCard": false,
    "useCardToken": true
…
}
```

     - **Response body:** campos recebidos sobre a tokenização.

```json
{
…
    "isNewTokenization": false,
    "generatedCardToken": {
        "cardTokenType": "TOKEN_VALUE",
        "cardTokenHref": "string",
        "tokenExtraData": {
            "extraData1": "string",
            "extraData2": "string"
       }
     "useCvvForAuthorization": true
   }
…
}
```

#### 3º Cenário: transação com cartão de crédito tokenizado externo (não será salvo na VTEX)

- Payment Gateway ([Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments))

     - **Request body:** campos enviados para tokenização.

```json
[
…
"fields": [{
    "accountId": "null",
    "cardTokenData": {
        "cardTokenType": "TOKEN_FILE",
        "cardTokenHref":
            "https://linktothetokenfile.com",
        "tokenExtraData": {
            "extraData1": "string",
            "extraData2": "string"
        },
        "useCvvForAuthorization": "boolean",
        "cardTokenCvv": "string",
}
    }]
…
]
```

     - **Response body:** campos recebidos sobre a tokenização.

```json
[
…
"fields": [{
    "name": "isCardToken",
    "value": "true"
	},
    {
    "name": "accountId",
    "value": "string"
	}
     …
    ]
…
]
```

- Payment Provider Protocol ([Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments))

     - **Request body:** campos enviados para tokenização.

```json
{
…
    "saveCreditCard": false,
    "useCardToken": true,
    "cardTokenData": {
        "cardTokenType": "TOKEN_VALUE",
        "cardTokenValue": "string",
        "tokenExtraData": {
           "extraData1": "string",
           "extraData2": "string"
        },
        "useCvvForAuthorization": true,
        "cardTokenCvv": "string"
    },
    "shopperInteration": "string",
…
}
```

     - **Response body:** campos recebidos sobre a tokenização.

```json
{
…
    "isNewTokenization": true,
    "generatedCardToken": {
        "cardTokenType": "TOKEN_VALUE",
        "cardTokenHref": "string",
        "tokenExtraData": {
            "extraData1": "string",
            "extraData2": "string"
        },
        "useCvvForAuthorization": true
   }
…
}
```

#### 4º Cenário: transação com cartão de crédito tokenizado externo (será salvo na VTEX)

- Payment Gateway ([Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments))

     - **Request body:** campos enviados para tokenização.

```json
[
…
"fields": {
    "accountId": "null",
    "savePaymentData": true,
    "cardData": {
        "cardLabel": "string",
        "paymentName": "enum",
        "bin": "string",
        "lastDigits": "string",
    },
    "cardTokenData": {
        "cardTokenType": "TOKEN_FILE",
        "cardTokenHref":
            "https://linktothetokenfile.com",
        "tokenExtraData": {
            "extraData1": "string",
            "extraData2": "string"
        },
        "useCvvForAuthorization": "boolean",
        "cardTokenCvv": "string",
    }
}
…
```

     - **Response body:** campos recebidos sobre a tokenização.

```json
[
…
"fields": [{
    "name": "isCardToken",
    "value": "true"
	},
    {
    "name": "accountId",
    "value": "string"
	}
     …
]
…
]

```

- Payment Provider Protocol ([Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments))

     - **Request body:** campos enviados para tokenização.

```json
{
…
    "saveCreditCard": true,
    "useCardToken": true,
    "cardTokenData": {
        "cardTokenType": "TOKEN_VALUE",
        "cardTokenValue": "string",
        "tokenExtraData": {
            "extraData1": "string",
            "extraData2": "string"
        },
        "useCvvForAuthorization": true,
        "cardTokenCvv": "string"
    },
    "shopperInteration": "string",
…
}
```

     - **Response body:** campos recebidos sobre a tokenização.

```json
{
…
    "isNewTokenization": true,
    "generatedCardToken": {
        "cardTokenType": "TOKEN_VALUE",
        "cardTokenHref": "string",
        "tokenExtraData": {
            "extraData1": "string",
            "extraData2": "string"
       },
        "useCvvForAuthorization": true
   }
…
}
```

> ⚠️ Para mais informações sobre os payload completos das requisições, acesse as documentações dos endpoints [Send payments information](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/payments/transactions/-transactionId-/payments) e [Create payment](https://developers.vtex.com/docs/api-reference/payment-provider-protocol#post-/payments?endpoint=post-/payments).

### Integrando o sistema Card Token Vault (CTV)

A **Card Token Vault (CTV)** é o sistema da VTEX responsável por armazenar e gerenciar as informações de tokens de cartão de crédito. As suas principais funcionalidades são:

- CRUD completo de tokens (criar, ler, atualizar e deletar).
- Importação em massa de tokens via arquivo .XLSX.
- Armazenamento seguro com [criptografia AES](https://pt.wikipedia.org/wiki/Advanced_Encryption_Standard).
- Rastreamento de atividades com suporte à auditoria completa.

Veja abaixo os tipos de informações registradas para cada token armazenado na CTV:

| **Campo** | **Mandatório** | **Tipo** | **Descrição** |
| --- | --- | --- | --- |
| `id` | Yes | string | Token ID in the system. |
| `accountName` | Yes | string | VTEX account name in the License Manager (e.g., carrefourbr, cea). |
| `providerId` | Yes | string | Name of the owner account of the connector used to create the token (ex: worldpay). |
| `profileId` | No | string | Profile ID in the Profile System. |
| `orderGroup` | No | string | Order identifier. |
| `email` | No | string | Email is used only if neither `profileId` nor `orderGroup` is provided (rare use). |
| `shopperId` | No | string | ShopperId is used only if neither `profileId` nor `orderGroup` nor email are provided. |
| `card.paymentSystemId` | No | string | Payment system ID in the Payment Gateway. |
| `card.paymentSystemName` | Yes | string | Card brand (e.g., Visa, Mastercard). |
| `card.firstDigits` | Yes | string | Card BIN (first six digits). |
| `card.lastDigits` | Yes | string | The last four digits of the card. |
| `card.address.addressType` | No | string | Address type. For example, Residential or Pickup. |
| `card.address.addressId` | No | string | Address identifier. |
| `card.address.postalCode` | No | string | Postal code (ZIP/CEP). |
| `card.address.street` | No | string | Street name. |
| `card.address.neighborhood` | No | string | Neighborhood name. |
| `card.address.city` | No | string | City name. |
| `card.address.state` | No | string | State name. |
| `card.address.country` | No | string | Country name. |
| `card.address.number` | No | string | Street number. |
| `card.address.complement` | No | string | Address complement (e.g., apartment, building). |
| `card.holderName` | No | string | Name of the cardholder as printed on the card. |
| `cardTokenData.type` | Yes | string | Type of token (e.g., `FILE`, `TOKEN_CLIENT_ID`, `TOKEN_VALUE`). |
| `cardTokenData.value` | No | string | The token value to be used in transactions. |
| `cardTokenData.expiration` | Yes | string | Token expiration date in YYYY-MM format. |
| `cardTokenData.label` | No | string | Token alias (used instead of lastDigits in UI). |
| `cardTokenData.providerCardTokenId` | No | string | Client ID used to retrieve the token from the provider. |
| `cardTokenData.useCvvForAuthorization` | No | boolean | Flag indicating if CVV is required (default: true). |
| `cardTokenData.href` | No | string | URL of the token file stored by the provider. |
| `extraData` | No | object | Dictionary <string, string> for additional data. |

A integração com a CTV deve ser feita por meio da [Card Token Vault API](https://developers.vtex.com/docs/api-reference/card-token-vault-api), disponível no Developer Portal.

Para mais detalhes sobre a importação de tokens, acesse o guia [Importando tokens na Card Token Vault](TBD).

### Validando a implementação da tokenização de pagamentos


Antes de iniciar a validação da implementação da tokenização no provedor, confirme que tenha à disposição uma conta configurada para compras headless (sem o uso da interface do Admin VTEX).  Em seguida, realize testes de compra conforme descrito no guia [Creating a regular order with the Checkout API](https://developers.vtex.com/docs/guides/creating-a-regular-order-with-the-checkout-api).


Após os testes de compras headless, realize as ações abaixo para validar a correta operação da tokenização de pagamentos:

1. [Configurar a conta](#configurando-a-conta)
2. [Simular uma compra com cartão de crédito](#simulando-uma-compra-com-cartao-de-credito)
3. [Confirmar a tokenização de dados](#confirmando-a-tokenizacao-de-dados)

#### Configurando a conta

Habilite a tokenização na conta headless conforme os passos abaixo:

1. Solicite ao time de pagamentos da VTEX a ativação da funcionalidade de tokenização.
2. Instale na conta o conector de pagamentos que irá suportar as operações de tokenização.

> ℹ️ Caso deseje, você também pode utilizar um conector de testes da VTEX para realizar simulações de operações de tokenização. Para isso, execute a instalação do conector por meio do comando `vtex install vtex.fake-pay-io-connector@3.0.3` no [VTEX IO CLI](https://developers.vtex.com/docs/guides/vtex-io-documentation-vtex-io-cli-usage).

3. No Admin VTEX, acesse **Configurações da loja > Pagamentos > Provedores** ou digite **Provedores** na barra de busca no topo da página.
4. Na tela de provedores, clique no botão `Novo provedor`.
5. Na barra de busca, digite o nome do conector instalado e clique sobre ele.
6. Preencha as informações solicitadas na tela de configuração e clique em `Salvar`.
7. [Configure uma condição de pagamento](https://help.vtex.com/pt/docs/tutorials/condicoes-de-pagamento) com cartão de crédito.

#### Simulando uma compra com cartão de crédito

Realize uma compra utilizando o cartão de crédito conforme descrito a seguir:

1. Realize os passos da compra até a seção **Placing the order** do guia [Creating a regular order with the Checkout API](https://developers.vtex.com/docs/guides/creating-a-regular-order-with-the-checkout-api).
2. Envie as informações de pagamento por meio do endpoint [Send Payments](https://developers.vtex.com/docs/api-reference/payments-gateway-api#post-/api/pub/transactions/-transactionId-/payments) (conforme descrito na seção **Resolving the order payment**), incluindo o campo `savePaymentData` na chamada.

```json

[
    {
        ...
        "fields": {
            "savePaymentData": true,
            "holderName": "John Doe",
        ...
        }
    }
]
```

#### Confirmando a tokenização de dados


Para confirmar se os dados do cartão foram tokenizados e salvos corretamente, siga os passos abaixo:

1. No Admin VTEX, acesse **Pedidos > Transações**, ou digite **Provedores** na barra de busca no topo da página.
2. Clique na transação de pagamento referente à compra realizada na seção anterior.
3. Na página **Eventos da transação**, localize o evento de resposta de autorização do conector e confirme se o conjunto de dados `generatedCardToken` está presente, conforme o exemplo a seguir:

```
Authorization response received: [200 OK] {"status":"approved","authorizationId":"AC97443800154CA8950FA49DB8271EB4","nsu":null,"tid":"40b73bc2-ed66-4118-a6b6-1726c16332a6","acquirer":null,"delayToAutoSettle":3600,"isNewTokenization":true,"generatedCardToken":{"cardTokenType":"TOKEN_VALUE","cardTokenValue":"******","cardTokenExpiryMonth":"08","cardTokenExpiryYear":"2037","cardTokenHref":null,"cardTokenClientId":null,"tokenExtraData":null,"useCvvForAuthorization":false,"cardTokenCvv":null},"paymentId":"DA4B34B82A76497D86F69F2951F6C306","code":null,"message":"Card token payment has been approved"}
```

4. Acesse o endpoint [Get client profile by email](https://developers.vtex.com/docs/api-reference/checkout-api#get-/api/checkout/pub/profiles) e confirme se o campo `accountId` está retornando corretamente, conforme o exemplo abaixo:

```json
{
    ...
    "availableAccounts": [
        {
            "accountId": "ADA70C8D7321403510535172A6EFC3C5",
            "paymentSystem": "4",
            "paymentSystemName": "Mastercard",
            "cardNumber": "************1111",
            "bin": "111111",
            ...
        }
    ],
    "availableAddresses": ...
}
```

> ℹ️ A presença do conjunto de dados `generatedCardToken` e do `accountId` confirma que o conector processou a tokenização corretamente e que o token foi atribuído ao perfil do comprador.