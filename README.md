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

# mega-cena:
- `scrape_mega_sena_num()`: Esta função retorna uma lista dos números da Mega Sena do último concurso.
- `scrape_concurso_mega_sena()`: Esta função retorna o título e o número do último concurso da Mega Sena.


# mega-cena-virada:
- `scrape_mega_sena_num_virada()`: Esta função retorna uma lista dos números da Mega Sena do último concurso da mega cena da virada.
- `scrape_concurso_mega_sena_virada()`: Esta função retorna o título e o número do último concurso da Mega Sena da virada.


