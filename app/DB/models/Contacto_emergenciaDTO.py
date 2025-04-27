from dataclasses import dataclass

@dataclass
class Contacto_emergencia:

    nombre: str
    relacion: str

    def __str__(self) -> str:
        texto = f"Nombre contacto: {self.nombre}\nRelación con el trabajador: {self.relacion}"
        return texto