from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Clase(Base):
    __tablename__ = "clases"

    id = Column(Integer, primary_key=True)
    tema = Column(String, nullable=False)
    duracion_minutos = Column(Integer, nullable=False)

    curso_id = Column(Integer, ForeignKey("cursos.id"))

    curso = relationship(
        "Curso",
        back_populates="clases"
    )