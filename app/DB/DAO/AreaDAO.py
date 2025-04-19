from dataclasses import dataclass
from .connector import connection
from ..models.AreaDTO import Area

@dataclass
class AreaDAO:

    area: Area

    def insertar_area(self, area):
        try:
            sql = "insert into areas (nombre) values (%s)"
            conn = connection()
            cursor = conn.cursor()
            cursor.execute(sql, (area.nombre, ))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False
