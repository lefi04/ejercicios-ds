from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Departamento(Base):
    __tablename__ = "departamentos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    profesores = relationship("Profesor", back_populates="departamento")