# Monitor de Clima Local

Projeto desenvolvido com o objetivo de aprender na prática o consumo de APIs externas e a persistência de dados com banco de dados relacional. Utiliza a API do OpenWeatherMap para buscar dados climáticos em tempo real e os armazena localmente em um banco SQLite.

## O que o projeto faz

- Busca temperatura, umidade e condição do tempo de uma cidade via API
- Salva cada leitura no banco de dados local `clima.db`
- Exibe o histórico completo de registros salvos

## Tecnologias utilizadas

- Python 3
- `requests` para consumo da API
- `sqlite3` para o banco de dados (nativo do Python)
- `python-dotenv` para gerenciamento de variáveis de ambiente

## Pré-requisitos

- Python 3 instalado
- Conta gratuita no [OpenWeatherMap](https://openweathermap.org/) para obter uma chave de API

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/josuejro/clima.git
cd clima
```

2. Instale as dependências:
```bash
python -m pip install requests python-dotenv
```

3. Crie um arquivo `.env` na raiz do projeto com sua chave de API:
```
CHAVE_API=sua_chave_aqui
```

> O arquivo `.env.example` já está disponível no repositório como referência.

## Como usar

Execute o script principal:
```bash
python main.py
```

O programa irá buscar os dados climáticos atuais, salvar no banco e exibir o histórico de registros.

## Cidade configurada

O projeto está configurado para monitorar **Imperatriz, BR** por padrão. Para trocar a cidade, abra o `main.py` e altere a linha:

```python
CIDADE = 'Imperatriz,BR'
```

Substitua pelo nome da cidade desejada seguido da sigla do país, por exemplo:

```python
CIDADE = 'Sao Paulo,BR'
CIDADE = 'Fortaleza,BR'
CIDADE = 'Lisboa,PT'
```

> Cidades com nomes acentuados podem não ser reconhecidas pela API. Se isso ocorrer, use o nome sem acentos ou substitua pela abordagem de coordenadas geográficas (`lat` e `lon`), que é mais confiável para cidades menores.

## Estrutura do projeto

```
clima/
├── main.py          # Script principal
├── clima.db         # Banco de dados local (gerado automaticamente)
├── .env             # Chave da API (não versionado)
├── .env.example     # Exemplo de configuração do .env
├── .gitignore
└── README.md
```

## Aprendizados

Este projeto foi desenvolvido como exercício introdutório para entender:

- Como funciona uma requisição HTTP com `requests.get()`
- Como interpretar e extrair dados de uma resposta JSON
- Como criar tabelas e inserir registros com `sqlite3`
- Como proteger credenciais sensíveis com `python-dotenv`