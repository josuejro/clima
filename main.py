import sqlite3
import requests
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_API = os.getenv('CHAVE_API')
CIDADE = 'Imperatriz,BR'
URL_BASE = 'https://api.openweathermap.org/data/2.5/weather'

def registrar_clima():
    params = {
        'q': CIDADE,
        'appid': CHAVE_API,
        'units': 'metric',
        'lang': 'pt_br'
    }

    resposta = requests.get(URL_BASE, params=params)

    try:
        resposta = requests.get(URL_BASE, params=params)

        if resposta.status_code == 200:
            dados_brutos = resposta.json()

            temperatura = dados_brutos['main']['temp']
            umidade = dados_brutos['main']['humidity']
            descricao = dados_brutos['weather'][0]['description']

            print(f'Neste momento, em {CIDADE}, faz {temperatura}°C, com {umidade}% de umidade e tempo {descricao}.')

            clima = sqlite3.connect('clima.db')
            cursor = clima.cursor()

            tabela_criacao = '''
            CREATE TABLE IF NOT EXISTS registro_clima(
                id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                cidade TEXT NOT NULL,
                temperatura REAL,
                umidade INTEGER,
                descricao
            )
            '''

            cursor.execute(tabela_criacao)

            tabela_insercao = '''
                INSERT INTO registro_clima (cidade, temperatura, umidade, descricao)
                VALUES (?, ?, ?, ?)
            '''

            valores = (CIDADE, temperatura, umidade, descricao)
            cursor.execute(tabela_insercao, valores)

            clima.commit()
            clima.close()
            
            print(f'\nO registro climático de {CIDADE} foi criado com sucesso!')

        else:
            print('\nErro: não foi possível obter os dados. Verifique a chave da API')

    except ConnectionError:
        print('\nErro de conexão: Verifique sua internet ou a URL.')
    
def ler_historico():
    clima = sqlite3.connect('clima.db')
    cursor = clima.cursor()

    leitura = 'SELECT * FROM registro_clima'
    cursor.execute(leitura)

    lista_resultados = cursor.fetchall()

    print()
    for registro in lista_resultados:
        print(f'{registro[1]} | {registro[2]}°C | {registro[3]}% umidade | {registro[4]}')
    
    clima.close()

registrar_clima()
ler_historico()