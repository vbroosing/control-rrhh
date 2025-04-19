from dataclasses import dataclass
from ..config.Connection import Connection
from ..config.db_config import config
from ..models.UsuarioDTO import Usuario

@dataclass
class UsuarioDAO:
    '''Esta clase controla las consultas que podemos hacer a la tabla Usuarios y maneja sus restricciones'''
    usuario: Usuario

    def insertarPerfil(self, usuario):
        try:
            sql = "insert into perfiles (nombre) values (%s);"
            conn = Connection(config)
            cursor = conn.cursor()
            cursor.execute(sql, (usuario.nombre, ))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False