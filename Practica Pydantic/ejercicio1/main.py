from pydantic import ValidationError
from estudiante import Estudiante


casos = [
    {
        "nombre": "Legajo inválido",
        "datos": {
            "legajo": 0,
            "nombre_completo": "Lucas Lefipan",
            "email": "lucas@gmail.com",
            "promedio": 8.5
        }
    },
    {
        "nombre": "Nombre demasiado corto",
        "datos": {
            "legajo": 123,
            "nombre_completo": "Ana",
            "email": "ana@gmail.com",
            "promedio": 8.5
        }
    },
    {
        "nombre": "Email inválido",
        "datos": {
            "legajo": 123,
            "nombre_completo": "Ana Perez",
            "email": "correo-invalido",
            "promedio": 8.5
        }
    },
    {
        "nombre": "Promedio fuera de rango",
        "datos": {
            "legajo": 123,
            "nombre_completo": "Ana Perez",
            "email": "ana@gmail.com",
            "promedio": 11.0
        }
    }
]


for caso in casos:
    print(f"\n--- {caso['nombre']} ---")

    try:
        estudiante = Estudiante(**caso["datos"])
        print(estudiante)
    except ValidationError as error:
        print(error)