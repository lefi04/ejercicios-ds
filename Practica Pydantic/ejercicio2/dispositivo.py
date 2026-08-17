from typing import Union, Literal
from pydantic import BaseModel


class Dispositivo(BaseModel):
    id_dispositivo: Union[int, str]
    tipo: Literal["sensor", "actuador", "gateway"]