from dataclasses import dataclass
from ..config.Connection import Connection
from ..config.db_config import config
from ..models.DepartamentoDTO import Departamento

@dataclass
class DepartamentoDAO:
    '''Esta clase controla las consultas que podemos hacer a la tabla Departamentos y maneja sus restricciones'''
    departamento: Departamento

    def insertar_departamento(self, departamento):
        try:
            sql = "insert into perfiles (area_id, nombre) values (%s, %s);"
            # print(sql, (departamento.area_id, departamento.nombre, ))
            conn = Connection(config)
            cursor = conn.cursor()
            cursor.execute(sql, (departamento.area_id, departamento.nombre, ))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False
        