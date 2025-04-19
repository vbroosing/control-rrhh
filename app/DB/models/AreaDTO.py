from dataclasses import dataclass

@dataclass
class Area:
    nombre: str
    
    def __str__(self) -> str:
        texto = f"Area: {self.nombre}"
        return texto