from database.session import get_session
from functions.concursos.raspagem import scrape_concurso_mega_sena, scrape_mega_sena_num


from models.concursos import Concursos
from models.mega_models import MegaSena

# Raspagem dos dados
numeros = scrape_mega_sena_num()
concurso_info = scrape_concurso_mega_sena()

# Separação do título e número do concurso
titulo, numero_concurso = concurso_info.split(maxsplit=1)

# Criação das instâncias dos modelos
concurso = Concursos(concurso=numero_concurso, data_sorteio=titulo)
megasena = MegaSena(concurso_id=concurso.id, virada=False)

# Adição das instâncias à sessão do banco de dados
# FIXME: gerador como um gerenciador de contexto ERROR
with get_session() as session:
    session.add(concurso)
    session.add(megasena)
    session.commit()
