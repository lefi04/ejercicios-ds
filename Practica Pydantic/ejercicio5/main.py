from pydantic import BaseModel, Field, HttpUrl


class PerfilUsuario(BaseModel):
    username: str = Field(pattern=r"^[a-z0-9_]{3,20}$")
    biografia: str | None = Field(default=None, max_length=200)
    redes_sociales: list[HttpUrl] | None = None


usuario = PerfilUsuario(
    username="lefi04",
    biografia="Una máquina",
    redes_sociales=[
        "https://instagram.com/lefi04",
        "https://github.com/lefi04",
    ]
)

print(usuario)