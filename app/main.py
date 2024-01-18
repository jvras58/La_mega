from mega_da_virada.raspagem import scrape_concurso_mega_sena_virada, scrape_mega_sena_num_virada
from concursos.raspagem import scrape_mega_sena_num, scrape_concurso_mega_sena


# mega sena
concurso = scrape_concurso_mega_sena()
print(concurso)

numeros = scrape_mega_sena_num()
print(numeros)


# mega da virada
concurso = scrape_concurso_mega_sena_virada()
print(concurso)

numeros = scrape_mega_sena_num_virada()
print(numeros)