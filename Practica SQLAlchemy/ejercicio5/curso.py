from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    creditos = Column(Integer, nullable=False)

    clases = relationship(
        "Clase",
        back_populates="curso"
    )