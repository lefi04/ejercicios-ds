from typing import Union, Literal
from pydantic import BaseModel, ValidationError


class Dispositivo(BaseModel):
    id_dispositivo: Union[int, str]
    tipo: Literal["sensor", "actuador", "gateway"]


dispositivo1 = Dispositivo(
    id_dispositivo=123,
    tipo="sensor"
)

dispositivo2 = Dispositivo(
    id_dispositivo="ABC-123",
    tipo="gateway"
)

print(dispositivo1)
print(dispositivo2)


try:
    dispositivo_invalido = Dispositivo(
        id_dispositivo=456,
        tipo="camara"
    )
except ValidationError as error:
    print("\n--- Error de validación ---")
    print(error)