from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from parsel import Selector

def scrape_mega_sena_num_virada()->list:
    """
    Raspa os números da Mega Sena do site oficial.

    Returns:
        list: Uma lista dos números da Mega Sena.
    """
    # Configura o driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Vá para a página da web
    driver.get('https://www.caixa.gov.br/Paginas/mega-da-virada.aspx')

    # Espere até que os números da Mega Sena estejam presentes na página
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.resultado-loteria li')))

    # Obtenha o HTML da página
    html = driver.page_source

    # Feche o navegador
    driver.quit()

    # Crie um seletor Parsel com o HTML
    sel = Selector(text=html)

    # Extraia os números
    numeros = sel.css('ul.resultado-loteria li::text').getall()

    return numeros

def scrape_concurso_mega_sena_virada()->str:
    """
    Raspa o título e o número do concurso da Mega Sena do site oficial.

    Returns:
        str: O título e o número do concurso da Mega Sena.
    """
    # Configura o driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Vá para a página da web
    driver.get('https://www.caixa.gov.br/Paginas/mega-da-virada.aspx')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.sorteio-loteria.clearfix div.nome-loteria.megasena.megasenadavirada p')))

    # Obtenha o HTML da página
    html = driver.page_source

    # Feche o navegador
    driver.quit()

    # Crie um seletor Parsel com o HTML
    sel = Selector(text=html)

    # Extraia o título e o número do concurso
    titulo = sel.css('div.sorteio-loteria.clearfix div.nome-loteria.megasena.megasenadavirada p::text').getall()[0]
    concurso = sel.css('div.sorteio-loteria.clearfix div.nome-loteria.megasena.megasenadavirada p.description::text').get()

    return f"{titulo} {concurso}"



