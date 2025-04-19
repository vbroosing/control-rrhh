from dataclasses import dataclass

@dataclass
class Perfil:
    '''Esta clase es el modelo de cada registro de la tabla Perfiles, para cumplir el contrato del dato en bd.'''
    nombre:str

    def __str__(self) -> str:
        texto = f"Perfil: {self.nombre}"
        return texto