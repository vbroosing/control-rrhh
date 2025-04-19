from dataclasses import dataclass

@dataclass
class Departamento:
    area_id: int
    nombre: str

    def __str__(self) -> str:
        texto = f"Departamento: {self.nombre}"
        return texto
        