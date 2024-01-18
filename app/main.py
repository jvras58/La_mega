from functions.concursos.raspagem import scrape_concurso_mega_sena, scrape_mega_sena_num
from functions.mega_da_virada.raspagem import scrape_concurso_mega_sena_virada, scrape_mega_sena_num_virada

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
