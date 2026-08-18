from datetime import datetime

from database import engine, Base, SessionLocal
from profesor import Profesor


# Crear las tablas
Base.metadata.create_all(engine)

# Crear una sesión
session = SessionLocal()

# Crear profesores de prueba
profesor1 = Profesor(
    nombre="Pepito Fernandez",
    email="pepito10@gmail.com",
    fecha_ingreso=datetime(2026, 8, 18, 9, 0)
)

profesor2 = Profesor(
    nombre="Rufina Diaz",
    email="rufus@gmail.com",
    fecha_ingreso=datetime(2026, 8, 18, 10, 30)
)

# Agregar los profesores a la sesión
session.add(profesor1)
session.add(profesor2)

# Guardar los cambios en la base de datos
session.commit()

# Consultar todos los profesores
profesores = session.query(Profesor).all()

# Mostrar los profesores por consola
for profesor in profesores:
    print(
        f"ID: {profesor.id} | "
        f"Nombre: {profesor.nombre} | "
        f"Email: {profesor.email} | "
        f"Fecha de ingreso: {profesor.fecha_ingreso}"
    )

# Cerrar la sesión
session.close()