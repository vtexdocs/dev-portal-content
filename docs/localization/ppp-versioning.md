---
title: "PPP Versioning"
slug: "ppp-versioning"
hidden: false
createdAt: "2025-12-01T00:00:00.00Z"
---

O [Payment Provider Protocol (PPP)](https://newhelp.vtex.com/pt/docs/tutorials/payment-provider-protocol) é o protocolo de integração entre a VTEX e parceiros que realizam o processamento de pagamentos. Para permitir a adoção de novas funcionalidades sem impactar os padrões operacionais existentes, a VTEX oferece o versionamento do PPP, garantindo aos provedores de pagamento flexibilidade para configurar seus conectores de acordo com as soluções que desejam disponibilizar aos clientes.

> ⚠️ Esta funcionalidade está em fase de testes (Closed Beta), o que significa que apenas clientes específicos podem acessá-la agora. Caso queira implementá-lo no futuro, entre em contato com nosso [Suporte](https://support.vtex.com/hc/pt-br/).

## Configurando o PPP Versioning

Siga as etapas abaixo para definir a versão do PPP utilizada nas transações do conector de pagamento:

1. Atualize o manifesto do conector, adicionando o campo `version` com o número da versão desejada, por exemplo, `2.0.0`.
2. Solicite a atualização do manifesto na VTEX junto ao [Suporte Técnico da VTEX](https://help.vtex.com/pt/docs/tutorials/abrir-chamados-para-o-suporte-vtex).

> ⚠️ Antes de atualizar o manifesto para uma nova versão do PPP, verifique os requisitos adicionais associados à versão. Algumas versões podem exigir a inclusão de novos campos em endpoints específicos para suportar funcionalidades extras.

Exemplo de manifesto configurado para a versão `2.0.0`:

```json
{
…
  "version": "2.0.0",
…
}
```

> ⚠️ Todos os conectores de pagamento são homologados automaticamente na VTEX utilizando a  versão `1.0.0` do PPP. Se o provedor de pagamento não tiver interesse em oferecer funcionalidades adicionais, não é necessário incluir o campo `version` no manifesto. Caso o conector já tenha sido atualizado (por exemplo, para a versão: `2.0.0`) e o provedor deseje retornar ao comportamento padrão do PPP, basta alterar o valor do campo `version` para `1.0.0` e solicitar ao suporte técnico da VTEX uma nova atualização do conector.

## Configurando o PPP Versioning

A tabela abaixo apresenta as funcionalidades adicionais disponíveis em cada versão do PPP configurada no conector de pagamento:

| **PPP Versioning** | **Funcionalidade** | **Descrição** |
| --- | --- | --- |
| 2.0.0 | [Tokenização de pagamentos](TBD) | Permite gerenciar informações de tokens de cartões de crédito, aumentando a segurança no armazenamento e na transmissão de dados sensíveis de pagamento. |