from dataclasses import dataclass

@dataclass
class Usuario:
    trabajador_id:int
    perfil_id: int
    nombre:str
    contrasenna: str

    def __str__(self) -> str:
        texto = f"Perfil: {self.trabajador_id, self.perfil_id, self.nombre, self.contrasenna}"
        return texto