from dataclasses import dataclass
from .connector import connection
from ..models.PerfilDTO import Perfil

@dataclass
class PerfilDAO:

    perfil: Perfil

    def insertar_perfil(self, perfil):
        try:
            sql = "insert into perfiles (nombre) values (%s);"
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(sql, (perfil.nombre, ))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False
    










    
    # def actualizarPerfil(self, per: Perfil):
    #     try:
    #         sql = "update perfil set nombre = %s, direccion = %s, fecha_nacimiento = %s, sexo = %s, codigo_postal = %s where rut = %s;"
    #         conn = conexion()
    #         cursor = conn.cursor()
    #         cursor.execute(sql,(per.nombre,per.direccion, 
    #                             per.fecha_nacimiento, per.sexo,
    #                             per.codigo_postal,per.rut))
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
        
    # def buscarPerfil(self, rut:str):
    #     try:
    #         sql = "select * from perfil where rut = %s;"
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