---
title: "After Sales Service API"
slug: "tokstoksponsorio-frontend-api-aftersalesserviceapi"
excerpt: "tokstoksponsorio.frontend-api@0.20.2"
hidden: true
createdAt: "2022-07-18T11:36:17.438Z"
updatedAt: "2022-08-01T14:03:46.867Z"
---
## Buscar Datas Disponíveis para Serviço Pós-Venda

**GET** `/api/io/after-sales-api/delivery-time/search?document={{document}}&orderId={{orderId}}`

### Parâmetros:
- *document:* CPF
- *orderId:* ID Pedido

### Response:
```json
{
    "data": [
        {
            "dataEntrega": "string",
            "ordemSite": 0,
            "faixa": "string",
            "idCGCE": 0
        }
    ],
	"nomeTipoSpv": "string",
	"scheduledDate": "string", 
    "spv": 0
}
```

## Atualiza a Data do Serviço Pós-Venda

**POST** `/api/io/after-sales-api/delivery-time/update`

### Body:
```json
{
    "spv": 0,
    "idCGCE": 0,
    "numeroItem": 0
}
```

**Obs.:** `numeroItem` é opcional.