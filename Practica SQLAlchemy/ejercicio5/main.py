from database import engine, Base, SessionLocal
from curso import Curso
from clase import Clase


# Crear las tablas
Base.metadata.create_all(engine)

# Crear una sesión
session = SessionLocal()

# Crear un curso
curso = Curso(
    titulo="Python",
    creditos=6
)

# Crear clases para el curso
clase1 = Clase(
    tema="Introducción a Python",
    duracion_minutos=60,
    curso=curso
)

clase2 = Clase(
    tema="Variables y tipos de datos",
    duracion_minutos=90,
    curso=curso
)

clase3 = Clase(
    tema="Funciones",
    duracion_minutos=75,
    curso=curso
)

# Guardar los registros
session.add(curso)
session.add_all([clase1, clase2, clase3])

session.commit()


# Consulta ORM: obtener todas las clases del curso
clases = session.query(Clase).filter(
    Clase.curso_id == curso.id
).all()


# Mostrar las clases
print(f"Clases del curso: {curso.titulo}")

for clase in clases:
    print(
        f"- {clase.tema} "
        f"({clase.duracion_minutos} minutos)"
    )


# Cerrar sesión
session.close()