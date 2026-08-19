from datetime import datetime

from database import engine, Base, SessionLocal
from profesor import Profesor
from curso import Curso


# Crear las tablas
Base.metadata.create_all(engine)

# Crear una sesión
session = SessionLocal()

# Crear un profesor
profesor = Profesor(
    nombre="Alejandro Gallardo",
    email="ale2000@gmail.com",
    fecha_ingreso=datetime(2026, 1, 10)
)

# Crear tres cursos asociados al profesor
curso1 = Curso(
    titulo="Programación I",
    creditos=6,
    profesor=profesor
)

curso2 = Curso(
    titulo="Bases de Datos",
    creditos=5,
    profesor=profesor
)

curso3 = Curso(
    titulo="Ingeniería de Software",
    creditos=4,
    profesor=profesor
)

# Guardar los registros
session.add(profesor)
session.add_all([curso1, curso2, curso3])

session.commit()


# Profesor → Cursos
print("=== Cursos dictados por el profesor ===")
print(f"Profesor: {profesor.nombre}")

for curso in profesor.cursos:
    print(f"- {curso.titulo} ({curso.creditos} créditos)")


# Curso → Profesor
print("\n=== Profesor de cada curso ===")

print(f"{curso1.titulo} → {curso1.profesor.nombre}")
print(f"{curso2.titulo} → {curso2.profesor.nombre}")
print(f"{curso3.titulo} → {curso3.profesor.nombre}")


# Cerrar sesión
session.close()