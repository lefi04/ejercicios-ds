from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Inscripcion(Base):
    __tablename__ = "inscripciones"

    id = Column(Integer, primary_key=True)

    estudiante_id = Column(
        Integer,
        ForeignKey("estudiantes.id")
    )

    curso_id = Column(
        Integer,
        ForeignKey("cursos.id")
    )

    estudiante = relationship(
        "Estudiante",
        back_populates="inscripciones"
    )

    curso = relationship(
        "Curso",
        back_populates="inscripciones"
    )