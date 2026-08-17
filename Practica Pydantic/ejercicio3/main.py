from typing import Annotated
from pydantic import BaseModel, Field, ValidationError


CoordenadaGPS = Annotated[
    float,
    Field(ge=-90.0, le=90.0)
]


class Ubicacion(BaseModel):
    longitud: CoordenadaGPS
    latitud: CoordenadaGPS
    etiqueta: str | None = None


# Instancia válida
ubicacion = Ubicacion(
    longitud=-58.3816,
    latitud=-34.6037,
    etiqueta="Buenos Aires"
)

print("--- Ubicación válida ---")
print(ubicacion)


# Instancia inválida
try:
    ubicacion_invalida = Ubicacion(
        longitud=120.0,
        latitud=-100.0,
        etiqueta="Ubicación inválida"
    )
except ValidationError as error:
    print("\n--- Error de validación ---")
    print(error)