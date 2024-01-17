# Projeto de Raspagem de Dados da Mega Sena

Este projeto é um script Python que raspa os números da Mega Sena e o título e número do concurso do site oficial da Caixa Econômica Federal.

## Dependências

Este projeto depende das seguintes bibliotecas Python:

- selenium
- webdriver_manager
- parsel

Você pode instalar todas as dependências com o seguinte comando:

```bash
poetry add selenium webdriver_manager parsel
```

## Como usar

O script contém duas funções principais:

- `scrape_mega_sena_num()`: Esta função retorna uma lista dos números da Mega Sena do último concurso.
- `scrape_concurso_mega_sena()`: Esta função retorna o título e o número do último concurso da Mega Sena.

Para usar essas funções, você pode importá-las em seu próprio script Python da seguinte maneira:

```python
from raspagem import scrape_mega_sena_num, scrape_concurso_mega_sena

numeros = scrape_mega_sena_num()
print(numeros)

concurso = scrape_concurso_mega_sena()
print(concurso)
```


