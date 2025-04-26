from dataclasses import dataclass
from ..config.Connection import Connection
from ..config.db_config import config
from ..models.UsuarioDTO import Usuario

@dataclass
class UsuarioDAO:
    '''Esta clase controla las consultas que podemos hacer a la tabla Usuarios'''
    usuario: Usuario

    def insertar_usuario(self, usuario):
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
            
    def buscar_usuario(self, usuario):
        try:
            sql = "select * from usuarios where nombre = %s;"
            conn = Connection(config)
            cursor = conn.cursor()
            cursor.execute(sql,[usuario.nombre], )
            fila = cursor.fetchone()
            User = Usuario(fila[1], fila[2], fila[3], fila[4], fila[5])
            del cursor
            return User
        except Exception as e:
            print(e)
            return False

    def actualizar_sesion_usuario(self, usuario):
        try:
            if usuario.sesion == 0:
                usuario.sesion = False
            else:
                usuario.sesion = True

            print(f'DESDE EL DAO {usuario}')
            sql = "update usuarios set sesion = %s where nombre = %s;"
            conn = Connection(config)
            cursor = conn.cursor()
            print('CURSOR??')
            cursor.execute(sql, (usuario.sesion, usuario.nombre))
            print('EJECUCION?')
            conn.commit()
            return usuario
        except Exception as e:
            print("error")
            print(e)