from pydantic import BaseModel, EmailStr, Field, ValidationError


class UsuarioSistema(BaseModel):
    email: EmailStr
    nivel_acceso: int = Field(ge=1, le=5)


# Intenta con estos datos
try: 
    usuario = UsuarioSistema(
        email="correo-invalido",
        nivel_acceso=10
    )

    print(usuario)

#Si ocurre ValidationError, mostrá esto
except ValidationError as error:
    print("--- Errores de validación ---")
    print(error)