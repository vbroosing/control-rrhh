from dataclasses import dataclass
from ..config.Connection import Connection
from ..config.db_config import config
from ..models.AreaDTO import Area

@dataclass
class AreaDAO:
    '''Esta clase controla las consultas que podemos hacer a la tabla Areas y maneja sus restricciones'''
    area: Area

    def insertar_area(self, area):
        try:
            sql = "insert into areas (nombre) values (%s)"
            conn = Connection(config)
            cursor = conn.cursor()
            cursor.execute(sql, (area.nombre, ))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False
