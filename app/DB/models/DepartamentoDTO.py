from dataclasses import dataclass

@dataclass
class Departamento:
    '''Esta clase es el modelo de cada registro de la tabla Depaartamentos, para cumplir el contrato del dato en bd.'''
    area_id: int
    nombre: str

    def __str__(self) -> str:
        texto = f"Departamento: {self.nombre}"
        return texto
        