from dataclasses import dataclass

@dataclass
class Perfil:
    nombre:str

    def __str__(self) -> str:
        texto = f"Perfil: {self.nombre}"
        return texto