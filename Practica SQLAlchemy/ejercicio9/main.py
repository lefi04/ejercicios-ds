from datetime import date

from sqlalchemy.exc import IntegrityError

from database import engine, Base, SessionLocal
from profesor import Profesor
from curso import Curso
from estudiante import Estudiante
from inscripcion import Inscripcion


Base.metadata.create_all(engine)

session = SessionLocal()


def matricular_alumno(estudiante, curso):
    try:
        inscripcion = Inscripcion(
            estudiante=estudiante,
            curso=curso,
            fecha_inscripcion=date.today(),
            calificacion_final=None
        )

        session.add(inscripcion)
        session.commit()

        print(f"Alumno {estudiante.nombre} matriculado en {curso.titulo}")

    except IntegrityError:
        session.rollback()

        print(
            f"Error: {estudiante.nombre} ya está "
            f"matriculado en {curso.titulo}"
        )


# Crear profesor
profesor = Profesor(
    nombre="Pepito Lopez",
    email="peplo@gmail.com",
    fecha_ingreso=date(2026, 3, 1)
)

# Crear curso
curso = Curso(
    titulo="Python",
    creditos=6,
    profesor=profesor
)

# Crear estudiante
estudiante = Estudiante(
    nombre="Lucas Ruiz",
    legajo=1001
)

session.add_all([profesor, curso, estudiante])
session.commit()


# Primera inscripción: debe funcionar
matricular_alumno(estudiante, curso)


# Segunda inscripción: debe provocar el error
matricular_alumno(estudiante, curso)


# Verificar que el rollback ocurrió
inscripciones = (
    session.query(Inscripcion)
    .filter(Inscripcion.estudiante_id == estudiante.id)
    .all()
)

print("\n=== Verificación del rollback ===")
print(f"Cantidad de inscripciones: {len(inscripciones)}")

for inscripcion in inscripciones:
    print(
        f"- {inscripcion.estudiante.nombre} "
        f"-> {inscripcion.curso.titulo}"
    )


session.close()