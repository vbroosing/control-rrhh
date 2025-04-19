from ...modules.hashlib import encrypt
from ...DB.config.Connection import Connection
from ...DB.config.db_config import config


class Validacion:
    '''Esta clase crea un objeto de sesion válida o inválida'''
    usuario: str
    password: str

    def encriptar(password):
        return encrypt(password)
    
    # CLARAMENTE DEBO MODIFICAR ESO PARA QUE USE EL MODULO DB, PERO ESTÁ ASI PARA PRUEBAS
    def consulta_credenciales(usuario):
        try:
            sql = "select * from usuarios where nombre (%s)"
            conn = Connection(config)
            cursor = conn.cursor()
            query = cursor.execute(sql, (usuario.nombre, ))
            conn.commit()
            conn.close()
            return query
        except Exception as e:
            print(e)
            return None
    
    def validar_password(password, query):
        if password in query:
            return True
        else:
            return False