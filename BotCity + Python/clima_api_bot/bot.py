from botcity.web import WebBot, Browser, By

from botcity.maestro import *

from webdriver_manager.chrome import ChromeDriverManager

from botcity.plugins.http import BotHttpPlugin


BotMaestroSDK.RAISE_NOT_CONNECTED = False

def pesquisar_cidade(bot, cidade):
    bot.browse("https://www.google.com")
    bot.wait(2000)
    while len(bot.find_elements('//*[@id="APjFqb"]', By.XPATH))<1:
        bot.wait(1000)
        print('carrengado.')
    bot.find_element('//*[@id="APjFqb"]', By.XPATH).send_keys(cidade)
    bot.wait(1000)
    bot.enter()



def main():
    
    maestro = BotMaestroSDK.from_sys_args()
    
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    bot.headless = False

    bot.browser = Browser.FIREFOX

    bot.browse("https://www.botcity.dev")


    bot.wait(3000)


    bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
