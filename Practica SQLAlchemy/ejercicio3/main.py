from datetime import datetime

from database import engine, Base, SessionLocal
from departamento import Departamento
from profesor import Profesor


# Crear las tablas
Base.metadata.create_all(engine)

# Crear una sesión
session = SessionLocal()

# Crear un departamento
departamento = Departamento(nombre="Informática")

# Crear tres profesores asociados al departamento
profesor1 = Profesor(
    nombre="Pepito Pérez",
    email="pepito@gmail.com",
    fecha_ingreso=datetime(2026, 1, 10),
    departamento=departamento
)

profesor2 = Profesor(
    nombre="Marcelo Lopez",
    email="marlo10@gmail.com",
    fecha_ingreso=datetime(2026, 2, 15),
    departamento=departamento
)

profesor3 = Profesor(
    nombre="Carlos Gómez",
    email="carlos@gmail.com",
    fecha_ingreso=datetime(2026, 3, 20),
    departamento=departamento
)

# Agregar los registros
session.add(departamento)
session.add_all([profesor1, profesor2, profesor3])

# Guardar los cambios
session.commit()


# Navegación desde Departamento hacia sus profesores
print("=== Desde Departamento hacia Profesores ===")
print(f"Departamento: {departamento.nombre}")

for profesor in departamento.profesores:
    print(f"- {profesor.nombre} ({profesor.email})")


# Navegación desde Profesor hacia su departamento
print("\n=== Desde Profesor hacia Departamento ===")

print(f"{profesor1.nombre} pertenece a {profesor1.departamento.nombre}")
print(f"{profesor2.nombre} pertenece a {profesor2.departamento.nombre}")
print(f"{profesor3.nombre} pertenece a {profesor3.departamento.nombre}")


# Cerrar la sesión
session.close()