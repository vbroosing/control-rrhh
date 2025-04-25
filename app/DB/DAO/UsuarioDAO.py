from dataclasses import dataclass
from ..config.Connection import Connection
from ..config.db_config import config
from ..models.UsuarioDTO import Usuario

@dataclass
class UsuarioDAO:
    '''Esta clase controla las consultas que podemos hacer a la tabla Usuarios y maneja sus restricciones'''
    usuario: Usuario

    def insertar_usuario(self, usuario):
        # try:
        #     sql = "insert into perfiles (nombre) values (%s);"
        #     conn = Connection(config)
        #     cursor = conn.cursor()
        #     cursor.execute(sql, (usuario.nombre, ))
        #     conn.commit()
        #     conn.close()
        #     return True
        # except Exception as e:
        #     print(e)
            # return False
        pass
            
    def buscar_usuario(self, usuario):
        try:
            sql = "select * from usuarios where nombre = %s;"
            conn = Connection(config)
            cursor = conn.cursor()
            cursor.execute(sql,[usuario.nombre], )
            fila = cursor.fetchone()
            # for element in fila:
            #     print(element)
            #     print(type(element))
            #### No entregamos la primera posición porque es el id del usuario 
            User = Usuario(fila[1], fila[2], fila[3], fila[4], fila[5])
            conn.close()
            return User
        except Exception as e:
            print(e)
            return False

    def actualizar_sesion_usuario(self, usuario):
        try:
            sql = "set sesion = (%s where nombre = %s"
            conn = Connection(config)
            cursor = conn.cursor()
            cursor.execute(sql, (usuario.sesion, usuario.nombre))
            usuario = cursor.fetchone()
            for element in usuario:
                print(element)
            usuario = Usuario(usuario[1], usuario[2], usuario[3], usuario[4], usuario[5])
            print(usuario)
            conn.close
            return usuario
        except Exception as e:
            print("error")
            print(e)

# SET sesion = FALSE where usuario_id = 1;
# UPDATE usuarios
# SET sesion = TRUE where usuario_id = 1;
# select * from usuarios;	