from dataclasses import dataclass

@dataclass
class Cargo:

    departamento_id: int
    nombre: str

    def __str__(self) -> str:
        texto = f"Cargo: {self.nombre}"
        return texto