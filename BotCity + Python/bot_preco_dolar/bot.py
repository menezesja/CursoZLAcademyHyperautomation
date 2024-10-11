from botcity.web import WebBot, Browser
from botcity.plugins.http import BotHttpPlugin
from webdriver_manager.chrome import ChromeDriverManager
from botcity.maestro import *
import requests

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def insert_produtos():

    http_plugin = BotHttpPlugin() 
    # Inicializa o plugin HTTP com a URL base
    url = 'http://127.0.0.1:5000/produto'

    # Lista de produtos a serem enviados no corpo da requisição POST
    payload = {
        {
            "descricao": "Acai",
            "unidade": "Litro",
            "quantidade": 10,
            "preco_real": 12.50,
            "preco_dolar": 0.0
        },
        {
            "descricao": "Tucuma",
            "unidade": "Kg",
            "quantidade": 30,
            "preco_real": 17.30,
            "preco_dolar": 0.0
        },
        {
            "descricao": "Tapioca",
            "unidade": "Unid",
            "quantidade": 5,
            "preco_real": 4.70,
            "preco_dolar": 0.0
        }
    }

    # Envia cada produto individualmente para a API
    headers = {
        "Content-Type": "application/json"
    }


    # Faz a requisição POST para incluir o produto
    response = requests.post(url, json=payload, headers=headers)

    # Verifica o status da resposta
    if response.status_code == 200:
        print(f"Produto {produto['descricao']} inserido com sucesso!")
        print("Resposta:", response.json())
    else:
        print(f"Falha ao inserir o produto {produto['descricao']}. Status: {response.status_code}")
        print(f"Erro: {response.text}")

def main():
    # Inicializa o Maestro
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    bot.headless = False

    bot.browser = Browser.CHROME

    bot.driver_path = ChromeDriverManager().install()
    
    # Chama a função para inserir produtos
    insert_produtos()

if __name__ == '__main__':
    main()