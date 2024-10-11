
from botcity.web import WebBot, Browser, By

from botcity.maestro import *

from webdriver_manager.chrome import ChromeDriverManager

from botcity.plugins.http import BotHttpPlugin

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def acessar_amazon(bot, produto):
    bot.browse("https://www.amazon.com")
    bot.wait(2000)
    while len(bot.find_elements('//*[@id="twotabsearchtextbox"]', By.XPATH))<1:
        bot.wait(1000)
        print('carregado.')
    bot.find_element('//*[@id="twotabsearchtextbox"]', By.XPATH).send_keys(produto)
    bot.wait(1000)
    bot.enter()

def extrair_dados_produto(bot):
    count = 1
    while True:
        count += 1
        try:
            # Tenta encontrar o nome do produto
            nome_produto = bot.find_element(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{count}]/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span', By.XPATH).text
        except Exception:
            #print(f"Produto não encontrado na posição {count}, ignorando...")
            continue  # Pula para a próxima iteração se o produto não for encontrado
        
        try:
            # Tenta encontrar o valor do produto
            valor_dolar = bot.find_element(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{count}]/div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div[1]/a/span/span[2]/span[2]', By.XPATH).text
            valor_centavos = bot.find_element(f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{count}]/div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div[1]/a/span/span[2]/span[3]', By.XPATH).text
            valor_produto = f"{valor_dolar},{valor_centavos}"
        except Exception:
            #print(f"Valor do produto não encontrado na posição {count}, ignorando...")
            continue  # Pula para a próxima iteração se o valor não for encontrado

        print(f'Nome do Produto: {nome_produto}\n Valor: {valor_produto}')
        
        if count == 10:
            break

def executar_api():
    http=BotHttpPlugin('https://economia.awesomeapi.com.br/last/USD-BRL')
    return http.get_as_json()

def main():
 
    maestro = BotMaestroSDK.from_sys_args()

    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()


    bot.headless = True

    bot.browser = Browser.CHROME

    bot.driver_path = ChromeDriverManager().install()

    try:
        acessar_amazon(bot, 'Kindle')
        extrair_dados_produto(bot)

        retornoJSON = executar_api()
        for item in retornoJSON:
            for m in item['moeda']:
                print(m['Máximo'])

    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')

    finally:
        bot.wait(2000)
        bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
