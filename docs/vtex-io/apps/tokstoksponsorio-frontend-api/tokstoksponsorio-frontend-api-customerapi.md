---
title: "Customer API"
slug: "tokstoksponsorio-frontend-api-customerapi"
excerpt: "tokstoksponsorio.frontend-api@0.20.2"
hidden: true
createdAt: "2022-07-18T11:36:17.415Z"
updatedAt: "2022-08-01T14:03:46.980Z"
---
## Endpoints

- `/customer-api/orders`
  - Endpoint responsavel por obter todos os pedidos do Cliente referente ao Cookie "VtexIdclientAutCookie_tokstok"
- `/customer-api/order/:orderId`
  - Endpoint responsavel por buscar um pedido (parametro de URL: `orderId`) do Cliente referente ao Cookie "VtexIdclientAutCookie_tokstok"
- `/customer-api/order/:orderId/cancel`
  - Variação do ednpoint de busca de pedido, responsavel por verificar se o pedido pode ser cancelado e se sim cancela-lo(parametro de URL: `orderId`) do Cliente referente ao Cookie "VtexIdclientAutCookie_tokstok"

#### [Docs](https://documenter.getpostman.com/view/9420029/SW18vEXR?version=latest#8816657c-79a2-4896-b04e-bbdc208fa019)