from dataclasses import dataclass

@dataclass
class Carga_familiar:
    '''Esta clase es el modelo de cada registro de la tabla Areas, para cumplir el contrato del dato en bd.'''
    trabajador_id: int
    rut: str
    nombre: str
    apellido: str
    parentesco: str
    sexo: bool
    
    def __str__(self) -> str:
        texto = f"Area: {self.nombre}"
        return texto