from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.base_model import Base

class MegaSena(Base):
    """
    Representa a tabela relacionada a mega-sena no banco de dados.
    """

    __tablename__ = 'MegaSena'

    id: Mapped[int] = mapped_column(primary_key=True, name='id')
    concurso_id: Mapped[int] = mapped_column(ForeignKey('concursos.id'), name='concursos_id')
    virada: Mapped[bool] = mapped_column(name='MegaSena_virada')
    concurso = relationship("Concursos", back_populates="megasena")
