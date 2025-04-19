from dataclasses import dataclass
from ..config.Connection import Connection
from ..config.db_config import config
from ..models.PerfilDTO import Perfil

@dataclass
class PerfilDAO:
    '''Esta clase controla las consultas que podemos hacer a la tabla Perfiles y maneja sus restricciones'''
    perfil: Perfil

    def insertar_perfil(self, perfil):
        try:
            sql = "insert into perfiles (nombre) values (%s);"
            conn = Connection(config)
            cursor = conn.cursor()
            cursor.execute(sql, (perfil.nombre, ))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False
    

    
    # def buscar_perfil(self, perfil):
    #     try:
    #         sql = "select * from perfiles where rut = %s;"
    #         conn = conexion()
    #         cursor = conn.cursor()
    #         cursor.execute(sql,[rut])
    #         fila = cursor.fetchone()
    #         per = Perfil(fila[0],fila[1],fila[2],fila[3], 
    #                         fila[4],fila[5])
    #         conn.close()
    #         return per
    #     except:
    #         return False
    # def actualizar_perfil(self, perfil):
    #     try:
    #         sql = "update perfiles set nombre = %s where id = %s;"
    #         conn = connection()
    #         cursor = conn.cursor()
    #         cursor.execute(sql,(perfil.nombre,perfil.id, ))
    #         conn.commit()
    #         conn.close()
    #         return True
    #     except:
    #         return False















    
        
    # def eliminarPerfil(self, per: Perfil):
    #     try:
    #         sql = "delete from perfil where rut = %s;"
    #         conn = conexion()
    #         cursor = conn.cursor()
    #         cursor.execute(sql,[per.rut])
    #         conn.commit()
    #         conn.close()
    #         return True
    #     except:
    #         return False
        
    # def listarPerfil(self):
    #     try:
    #         sql = "select * from perfil;"
    #         conn = conexion()
    #         cursor = conn.cursor()
    #         cursor.execute(sql)
    #         filas = cursor.fetchall()
    #         resultados = list()
    #         for fila in filas:
    #             per = Perfil(fila[0],fila[1],fila[2],fila[3], 
    #                           fila[4],fila[5])
    #             resultados.append(per)
    #         conn.close()
    #         return resultados
    #     except:
    #         return False
        