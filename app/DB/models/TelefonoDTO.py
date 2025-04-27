from dataclasses import dataclass

@dataclass
class Telefono:

    telefono: int

    def __str__(self) -> str:
        texto = f"teléfono: {self.telefono}"
        return texto