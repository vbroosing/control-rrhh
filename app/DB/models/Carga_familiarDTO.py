from dataclasses import dataclass

@dataclass
class Carga_familiar:
    '''Modelo de carga familiar - 
    trabajador_id: int -
    rut: str -
    nombre: str -
    apellido: str -
    parentesco: str -
    sexo: bool'''
    trabajador_id: int
    rut: str
    nombre: str
    apellido: str
    parentesco: str
    sexo: bool
    
    def __str__(self) -> str:
        texto = f"Area: {self.nombre}"
        return texto