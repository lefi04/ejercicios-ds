from datetime import datetime, date
from database import engine, Base, SessionLocal
from profesor import Profesor
from curso import Curso
from estudiante import Estudiante
from inscripcion import Inscripcion


Base.metadata.create_all(engine)

session = SessionLocal()

# Crear profesores
profesor1 = Profesor(
    nombre="Juan Pérez",
    email="juan@email.com",
    fecha_ingreso=datetime(2024, 3, 1)
)

profesor2 = Profesor(
    nombre="Ana López",
    email="ana@email.com",
    fecha_ingreso=datetime(2025, 2, 15)
)

session.add_all([profesor1, profesor2])
session.commit()


# Crear cursos
curso1 = Curso(
    titulo="Python",
    creditos=6,
    profesor=profesor1
)

curso2 = Curso(
    titulo="Bases de Datos",
    creditos=5,
    profesor=profesor1
)

curso3 = Curso(
    titulo="Programación",
    creditos=4,
    profesor=profesor2
)

session.add_all([curso1, curso2, curso3])
session.commit()


# Crear estudiantes
estudiante1 = Estudiante(
    nombre="Lucas Fernández",
    legajo=1001
)

estudiante2 = Estudiante(
    nombre="María González",
    legajo=1002
)

estudiante3 = Estudiante(
    nombre="Carlos Gómez",
    legajo=1003
)

session.add_all([estudiante1, estudiante2, estudiante3])
session.commit()


# Crear inscripciones
inscripciones = [
    Inscripcion(
        estudiante_id=estudiante1.id,
        curso_id=curso1.id,
        fecha_inscripcion=date(2026, 3, 1),
        calificacion_final=8.5
    ),
    Inscripcion(
        estudiante_id=estudiante1.id,
        curso_id=curso2.id,
        fecha_inscripcion=date(2026, 3, 2),
        calificacion_final=9.0
    ),
    Inscripcion(
        estudiante_id=estudiante2.id,
        curso_id=curso1.id,
        fecha_inscripcion=date(2026, 3, 1),
        calificacion_final=7.5
    ),
    Inscripcion(
        estudiante_id=estudiante2.id,
        curso_id=curso3.id,
        fecha_inscripcion=date(2026, 3, 3),
        calificacion_final=8.0
    ),
    Inscripcion(
        estudiante_id=estudiante3.id,
        curso_id=curso1.id,
        fecha_inscripcion=date(2026, 3, 1),
        calificacion_final=6.5
    )
]

session.add_all(inscripciones)
session.commit()


# -------------------------------------------------
# REPORTE 1
# Cursos que dicta un profesor específico
# utilizando JOIN
# -------------------------------------------------

cursos = (
    session.query(Curso)
    .join(Profesor)
    .filter(Profesor.nombre == "Juan Pérez")
    .all()
)

print("=== Cursos de Juan Pérez ===")

for curso in cursos:
    print(f"- {curso.titulo}")


# -------------------------------------------------
# REPORTE 2
# Promedio de calificaciones de un estudiante
# -------------------------------------------------

from sqlalchemy import func

promedio = (
    session.query(func.avg(Inscripcion.calificacion_final))
    .join(Estudiante)
    .filter(Estudiante.nombre == "Lucas Fernández")
    .scalar()
)

print("\n=== Promedio de Lucas Fernández ===")
print(f"Promedio: {promedio:.2f}")


# -------------------------------------------------
# REPORTE 3
# Cantidad de estudiantes por curso
# -------------------------------------------------

resultados = (
    session.query(
        Curso.titulo,
        func.count(Inscripcion.estudiante_id)
    )
    .outerjoin(Inscripcion)
    .group_by(Curso.id)
    .all()
)

print("\n=== Estudiantes inscriptos por curso ===")

for titulo, cantidad in resultados:
    print(f"- {titulo}: {cantidad} estudiantes")


session.close()