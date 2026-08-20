from datetime import date

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
    nombre="Lucas Lefipan",
    legajo=1001
)

estudiante2 = Estudiante(
    nombre="Leandro Paredes",
    legajo=1002
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


# Crear inscripciones
inscripcion1 = Inscripcion(
    estudiante=estudiante1,
    curso=curso1,
    fecha_inscripcion=date(2026, 8, 20),
    calificacion_final=8.5
)

inscripcion2 = Inscripcion(
    estudiante=estudiante1,
    curso=curso2,
    fecha_inscripcion=date(2026, 8, 20),
    calificacion_final=9.0
)

inscripcion3 = Inscripcion(
    estudiante=estudiante2,
    curso=curso1,
    fecha_inscripcion=date(2026, 8, 21),
    calificacion_final=7.5
)


# Guardar los registros
session.add_all([
    estudiante1,
    estudiante2,
    curso1,
    curso2,
    inscripcion1,
    inscripcion2,
    inscripcion3
])

session.commit()


# Mostrar las inscripciones
print("=== Inscripciones ===")

inscripciones = session.query(Inscripcion).all()

for inscripcion in inscripciones:
    print(
        f"Estudiante: {inscripcion.estudiante.nombre} | "
        f"Curso: {inscripcion.curso.titulo} | "
        f"Fecha: {inscripcion.fecha_inscripcion} | "
        f"Calificación: {inscripcion.calificacion_final}"
    )


session.close()