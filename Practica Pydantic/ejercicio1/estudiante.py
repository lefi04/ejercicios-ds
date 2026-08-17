from pydantic import BaseModel, Field, EmailStr


class Estudiante(BaseModel):
    legajo: int = Field(gt=0)
    nombre_completo: str = Field(min_length=5)
    email: EmailStr
    promedio: float = Field(default=0.0, ge=0.0, le=10.0)