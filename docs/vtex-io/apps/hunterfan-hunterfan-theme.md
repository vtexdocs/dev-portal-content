---
title: "Wedigi.tech - Tema mínimo para inicialização do VTEX IO em novos projetos"
slug: "hunterfan-hunterfan-theme"
excerpt: "hunterfan.hunterfan-theme@1.0.50"
hidden: true
createdAt: "2022-07-26T13:33:38.003Z"
updatedAt: "2022-07-26T13:33:38.003Z"
---
## Configurações iniciais

### Passo 1

Inserir comandos no terminal: 
```json
  vtex install vtex.store vtex.search vtex.store-sitemap vtex.admin-pages vtex.admin-search vtex.search-resolver@1.x
```

## Procedimento para inicializar o React no projeto:

```json
  mkdir react ; cd /react //dentro do projeto
  yarn init
```
Inserir a dependencia em package.json:
```json
  "react": "^16.13.1"
  yarn install
```
Inserir em "Builders" no manifest.json:
```json
  "react": "3.x"
```

## Procedimento para publicar um projeto IO:

No manifest alterar a versão em "version" e aí seguir a seguinte cadeia de comandos:
```json
  vtex use prod --production //Migrar para uma WS produção
  vtex publish ; vtex deploy //Publicar e fazer deploy do código na WS em produção
  vtex promote //Promover o código para Master
  vtex install vendor.name@major.minor.patch //Instalar o tema na Master por ex: hunterfan.hunterfan-theme@1.0.0
```

## Instalações para performance

```json
  vtex install vtex.google-tag-manager@2.x
  vtex install vtex.facebook-pixel@2.x
  vtex install vtex.facebook-domain-verification@1.x
  vtex install vtex.google-adwords@1.x
```

## Boas Práticas para a utilização do Site Editor