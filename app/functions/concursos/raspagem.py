from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from parsel import Selector

def scrape_mega_sena_num()->list:
    """
    Raspa os números da Mega Sena do site oficial.

    Returns:
        list: Uma lista dos números da Mega Sena.
    """
    # Configura o driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Vá para a página da web
    driver.get('https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx')

    # Espere até que os números da Mega Sena estejam presentes na página
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.numbers.megasena li')))

    # Obtenha o HTML da página
    html = driver.page_source

    # Feche o navegador
    driver.quit()

    # Crie um seletor Parsel com o HTML
    sel = Selector(text=html)

    # Extraia os números
    numeros = sel.css('ul.numbers.megasena li::text').getall()

    return numeros

#TODO: TEM ALGO DE ERRADO QUE CONSEGUE OU NÃO PEGAR O CONCURSO E O TÍTULO
def scrape_concurso_mega_sena()->str:
    """
    Raspa o título e o número do concurso da Mega Sena do site oficial.

    Returns:
        str: O título e o número do concurso da Mega Sena.
    """
    # Configura o driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Vá para a página da web
    driver.get('https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.title-bar.clearfix h2 span.ng-binding')))

    # Obtenha o HTML da página
    html = driver.page_source

    # Feche o navegador
    driver.quit()

    # Crie um seletor Parsel com o HTML
    sel = Selector(text=html)

    # Extraia o título e o número do concurso
    titulo = sel.css('div.title-bar.clearfix h2::text').get()
    concurso = sel.css('div.title-bar.clearfix h2 span.ng-binding::text').get()


    return f"{titulo} {concurso}"



