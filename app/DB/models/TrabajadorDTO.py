from dataclasses import dataclass
from datetime import date

@dataclass
class Trabajador:

    cargo_id: int
    rut: str
    primer_nombre: str
    segundo_nombre: str
    apellido_paterno: str
    apellido_materno: str
    direccion: str
    sexo: str
    fecha_ingreso: date
    
    def __str__(self) -> str:
        texto = f'''Rut: {self.rut}
Nombre: {self.primer_nombre} {self.segundo_nombre} {self.apellido_materno} {self.apellido_paterno}
Dirección: {self.direccion}
Sexo: {self.sexo}
Fecha de ingreso: {self.fecha_ingreso}'''
        return texto

