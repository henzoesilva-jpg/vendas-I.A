# vendas.py — Agente de IA para Análise de Vendas

## Descrição

Aplicação desenvolvida em Python com Streamlit para permitir o carregamento e a visualização de planilhas de vendas no formato Excel, com estrutura para integração com inteligência artificial.

O projeto utiliza bibliotecas de manipulação de dados e a API Gemini.

## Requisitos

* Python
* Streamlit
* Pandas
* OpenPyXL
* Google GenAI

### Instalação das dependências

```bash
pip install streamlit pandas openpyxl google-genai
```

## Configuração da API

Para utilizar a integração com o Gemini, crie manualmente um arquivo chamado `token.json` na mesma pasta do arquivo `vendas.py`.

### Exemplo de estrutura do arquivo token.json:

```json
{
    "api_key": "SUA_CHAVE_DA_API_GEMINI"
}
```

Substitua o valor de exemplo pela sua chave de API do Google AI Studio.

**Importante:** Não compartilhe o arquivo `token.json`, pois ele contém informações privadas de autenticação.

## Como executar

No terminal, execute:

```bash
streamlit run vendas.py
```

A aplicação será aberta no navegador.

## Funcionalidades

* Interface web utilizando Streamlit.
* Upload de planilhas Excel (`.xlsx`).
* Leitura dos dados utilizando Pandas.
* Exibição dos dados em formato de tabela.
* Campo para inserir perguntas relacionadas às vendas.

## Tecnologias utilizadas

* Python
* Streamlit
* Pandas
* Google Gemini API
* JSON
* Excel

## Objetivo

Desenvolver uma aplicação para facilitar a visualização e futura análise de dados comerciais utilizando recursos de inteligência artificial.
