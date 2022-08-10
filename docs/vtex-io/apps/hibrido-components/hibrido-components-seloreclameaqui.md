---
title: "SeloReclameAqui"
slug: "hibrido-components-seloreclameaqui"
excerpt: "hibrido.components@0.0.8"
hidden: true
createdAt: "2022-07-14T18:53:08.426Z"
updatedAt: "2022-07-29T12:20:11.782Z"
---
Bloco responsável por exibir o Selo do Reclame Aqui

## Exemplo:

```json
"reclame-aqui": {
    "props": {
        "id": "id-da-empresa"
    }
}
```

## Propriedades:

| Nome         | Tipo            | Descrição    | Valor padrão |
| ------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | 
| `id`        | `string`      | ID Do reclame aqui, pode ser obtido no painel | `null` |
| `env`        | `"development" \| "staging" \| "homolog" \| "evolucao" \| "production" \| null`      | Ambiente do Reclame Aqui | `"production"` |
| `orientation`      | `"vertical" \| "horizontal"`      | Orientação do Selo | `"horizontal"` |