from dataclasses import dataclass

@dataclass
class Area:
    '''Esta clase es el modelo de cada registro de la tabla Areas, para cumplir el contrato del dato en bd.'''
    nombre: str
    
    def __str__(self) -> str:
        texto = f"Area: {self.nombre}"
        return texto