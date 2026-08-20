from database import engine, Base, SessionLocal
from estudiante import Estudiante
from curso import Curso
from inscripcion import Inscripcion


# Crear las tablas
Base.metadata.create_all(engine)

# Crear sesión
session = SessionLocal()


# Crear estudiantes
estudiante1 = Estudiante(
    nombre="Juan Pérez",
    legajo=1001
)

estudiante2 = Estudiante(
    nombre="Ana López",
    legajo=1002
)

estudiante3 = Estudiante(
    nombre="Carlos Gómez",
    legajo=1003
)


# Crear cursos
curso1 = Curso(
    titulo="Python",
    creditos=6
)

curso2 = Curso(
    titulo="Bases de Datos",
    creditos=5
)

curso3 = Curso(
    titulo="Ingeniería de Software",
    creditos=4
)


# Crear inscripciones
inscripcion1 = Inscripcion(
    estudiante=estudiante1,
    curso=curso1
)

inscripcion2 = Inscripcion(
    estudiante=estudiante1,
    curso=curso2
)

inscripcion3 = Inscripcion(
    estudiante=estudiante2,
    curso=curso1
)

inscripcion4 = Inscripcion(
    estudiante=estudiante2,
    curso=curso3
)

inscripcion5 = Inscripcion(
    estudiante=estudiante3,
    curso=curso2
)

inscripcion6 = Inscripcion(
    estudiante=estudiante3,
    curso=curso3
)


# Guardar todos los registros
session.add_all([
    estudiante1,
    estudiante2,
    estudiante3,
    curso1,
    curso2,
    curso3,
    inscripcion1,
    inscripcion2,
    inscripcion3,
    inscripcion4,
    inscripcion5,
    inscripcion6
])

session.commit()


# Mostrar las inscripciones
print("=== Inscripciones ===")

inscripciones = session.query(Inscripcion).all()

for inscripcion in inscripciones:
    print(
        f"{inscripcion.estudiante.nombre} "
        f"→ {inscripcion.curso.titulo}"
    )


session.close()