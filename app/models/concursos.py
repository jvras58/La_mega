from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base_model import Base


class Concursos(Base):
    """
    Representa a tabela relacionada aos concursos no banco de dados.
    """

    __tablename__ = 'concursos'

    id: Mapped[int] = mapped_column(primary_key=True, name='id')
    concurso: Mapped[int] = mapped_column(name='concurso')
    data_sorteio: Mapped[str] = mapped_column(name='data_sorteio')
    megasena = relationship("MegaSena", back_populates="concurso")
