from dataclasses import dataclass

@dataclass
class Usuario:
    '''Esta clase es el modelo de cada registro de la tabla Usuarios, para cumplir el contrato del dato en bd.'''
    trabajador_id:int
    perfil_id: int
    nombre:str
    contrasenna: str
    sesion: bool

    def __str__(self) -> str:
        texto = f"Usuario: {self.trabajador_id, self.perfil_id, self.nombre, self.contrasenna, self.sesion}"
        return texto

    