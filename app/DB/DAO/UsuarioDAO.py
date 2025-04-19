from dataclasses import dataclass
from .connector import connection
from ..models.UsuarioDTO import Usuario

@dataclass
class UsuarioDAO:

    
    usuario: Usuario

    def insertarPerfil(self, usuario):
        try:
            sql = "insert into perfiles (nombre) values (%s);"
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(sql, (usuario.nombre, ))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False