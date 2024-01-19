"""
IMPORTANTE
Para contornar o problema de não encontrar a definição da classe a que o relacionamento
definido nas clausulas relationship(...), Cada classe do mapeamento deve ser declarada
na inicialização do módulo inteiro do Models.

Ref: https://stackoverflow.com/questions/9088957/sqlalchemy-cannot-find-a-class-name
"""

from models.concursos import Concursos  # noqa F401
from models.mega_models import MegaSena  # noqa F401
