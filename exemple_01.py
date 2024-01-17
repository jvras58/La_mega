from parsel import Selector
from httpx import get

response = get('https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx').content

selector = Selector(text=response.decode('utf-8', errors='ignore'))
print(selector)

dezenas = selector.css('')

# teste = selector.css('a').get()
# print(teste)

# links = selector.css('a::attr(href)').getall()
# for link in links:
#     print(link)

# teste = selector.css('a::attr(href)').getall()
# print(teste)
