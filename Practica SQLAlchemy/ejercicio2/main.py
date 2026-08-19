from datetime import datetime

from database import engine, Base, SessionLocal
from departamento import Departamento
from profesor import Profesor


# Crear las tablas
Base.metadata.create_all(engine)

# Crear una sesión
session = SessionLocal()


# Crear departamentos
informatica = Departamento(nombre="Informática")
matematica = Departamento(nombre="Matemática")

session.add(informatica)
session.add(matematica)

session.commit()


# Crear profesores
profesor1 = Profesor(
    nombre="Lucas Fernández",
    email="lucas@email.com",
    fecha_ingreso=datetime(2026, 8, 19),
    departamento=informatica
)

profesor2 = Profesor(
    nombre="Ana López",
    email="ana@email.com",
    fecha_ingreso=datetime(2025, 3, 10),
    departamento=informatica
)

profesor3 = Profesor(
    nombre="Carlos Gómez",
    email="carlos@email.com",
    fecha_ingreso=datetime(2024, 11, 5),
    departamento=matematica
)

session.add_all([profesor1, profesor2, profesor3])

session.commit()


# Mostrar departamentos y sus profesores
departamentos = session.query(Departamento).all()

for departamento in departamentos:
    print(f"\nDepartamento: {departamento.nombre}")

    for profesor in departamento.profesores:
        print(f" - {profesor.nombre} ({profesor.email})")


session.close()