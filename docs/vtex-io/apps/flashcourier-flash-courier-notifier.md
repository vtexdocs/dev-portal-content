---
title: "Flash Courier"
slug: "flashcourier-flash-courier-notifier"
excerpt: "flashcourier.flash-courier-notifier@0.1.22"
hidden: true
createdAt: "2022-07-04T21:34:48.817Z"
updatedAt: "2022-07-12T23:23:21.921Z"
---
O app Flash Courier foi desenvolvido para integrar a loja com o os serviços da transportadora de mesmo nome.<br>
O aplicativo pode ser facilmente integrado a loja, precisando apenas de instalar e preencher os campos com os dados fornecidos pela Flash Courier.<br>
Para obter os dados de configuração, favor entrar em contato com a transportadora.

## Configuração

1. Acesse a seção **Apps(Aplicativos)** na página de administração da sua conta, **App Store(Loja de aplicativos)**, e procure por **Flash Courier**;
2. Em seguida clique em **Install(Instalar)**;
3. Em **My Apps(Meus aplicativos)** encontrará **Flash Courier**. Clique em **Settings(Configurações)** e preencha os campos com os dados fornecidos pela Flash Courier. Todos os campos são obrigatórios;
4. Em seguida clique em **Save(Salvar)**.

## Descrição dos campos

- **Identificador do cliente**: ID único na Flash correspondente ao cliente cadastrado em sistema;
- **ID do CTT**: ID referente ao contrato (tipo de serviço) do cliente na Flash, para a Vtex, tbm será único;
- **Identificador do Produto Flash**: Nome do produto contratado pelo cliente junto ao setor comercial da Flash para tarifas de frete;
- **Identificador da Franquia Recebedora**: Sigla da franquia filiada à Flash que fará a coleta e processo logístico de encomendas desse cliente;
- **Identificador do Centro de Custo**: ID referente ao Centro de Custo no sistema da Flash, campo necessário para parametrizações operacionais na Flash. Para Vtex, sempre será único para determinado cliente;
- **Identificador do Tipo de Encomenda**: ID referente ao tipo de encomenda do cliente, se mercadoria, cartão etc, além de possuir especificações como se o mesmo terá ou redespacho via correios, dimensão da mercadoria etc, tbm não se repete para outros clientes;
- **Identificador do Local Remetente**: ID necessário para que o sistema encontra o endereço sede do cliente, cadastrado no sistema Flash, único para cada cliente;
- **DNA Hawb**: Código sistêmico da Flash para especificações operacionais (por ex. se o cliente terá ou não o serviço de custódia);
- **Usuário**: Criado no sistema da Flash para que possa se autenticar à API de Consulta e de Importação;
- **Senha**: Criado no sistema da Flash para que possa se autenticar à API de Consulta e de Importação.