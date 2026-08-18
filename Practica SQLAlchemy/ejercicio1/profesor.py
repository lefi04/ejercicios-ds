from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class Profesor(Base):
    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)
    fecha_ingreso = Column(DateTime, nullable=False)