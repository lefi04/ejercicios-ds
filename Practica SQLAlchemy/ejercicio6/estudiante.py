from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    legajo = Column(Integer, nullable=False)

    inscripciones = relationship(
        "Inscripcion",
        back_populates="estudiante"
    )