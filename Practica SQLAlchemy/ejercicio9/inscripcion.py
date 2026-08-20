from sqlalchemy import Column, Integer, Date, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from database import Base


class Inscripcion(Base):
    __tablename__ = "inscripciones"

    id = Column(Integer, primary_key=True)

    estudiante_id = Column(Integer, ForeignKey("estudiantes.id"))
    curso_id = Column(Integer, ForeignKey("cursos.id"))

    fecha_inscripcion = Column(Date, nullable=False)
    calificacion_final = Column(Float)

    estudiante = relationship(
        "Estudiante",
        back_populates="inscripciones"
    )

    curso = relationship(
        "Curso",
        back_populates="inscripciones"
    )

    __table_args__ = (
        UniqueConstraint(
            "estudiante_id",
            "curso_id",
            name="uq_estudiante_curso"
        ),
    )