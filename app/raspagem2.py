from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape_mega_sena_num()->list:
    """
    Raspa os números da Mega Sena do site oficial.

    Returns:
        list: Uma lista dos números da Mega Sena.
    """
    # Configura o driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Vai para a página da Mega Sena
    driver.get('https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx')

    # Espere até que os números da Mega Sena estejam presentes na página
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.numbers.megasena li')))

    # Aguarda o JavaScript ser executado e busca os números
    numbers = driver.find_elements(By.CSS_SELECTOR, 'ul.numbers.megasena li')

    # Extrai o texto dos elementos
    numbers = [number.text for number in numbers]

    # Fecha o navegador
    driver.quit()

    return numbers

print(scrape_mega_sena_num())
