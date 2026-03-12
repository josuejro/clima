import sqlite3
import requests

CHAVE_API = 'a7e25bc4dc88ccf5508d9026485bf539'
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
            
            print(f'O registro climático de {CIDADE} foi criado com sucesso!')

        else:
            print('Erro: não foi possível obter os dados. Verifique a chave da API')

    except ConnectionError:
        print('Erro de conexão: Verifique sua internet ou a URL.')
    
def ler_historico():
    clima = sqlite3.connect('clima.db')
    cursor = clima.cursor()

    leitura = 'SELECT * FROM registro_clima'
    cursor.execute(leitura)

    lista_resultados = cursor.fetchall()

    for linha in lista_resultados:
        print(linha)
    
    clima.close()

registrar_clima()
ler_historico()