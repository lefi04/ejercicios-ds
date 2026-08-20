from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    creditos = Column(Integer, nullable=False)

    profesor_id = Column(
        Integer,
        ForeignKey("profesores.id")
    )

    profesor = relationship(
        "Profesor",
        back_populates="cursos"
    )

    inscripciones = relationship(
        "Inscripcion",
        back_populates="curso"
    )