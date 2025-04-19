from dataclasses import dataclass
from .connector import connection
from ..models.DepartamentoDTO import Departamento

@dataclass
class DepartamentoDAO:
    departamento: Departamento

    def insertar_departamento(self, departamento):
        try:
            sql = "insert into perfiles (area_id, nombre) values (%s, %s);"
            print(sql, (departamento.area_id, departamento.nombre, ))
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(sql, (departamento.area_id, departamento.nombre, ))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False
        