from dataclasses import dataclass
from ..config.Connection import Connection
from ..config.db_config import config
from ..models.TrabajadorDTO import Trabajador

@dataclass
class TrabajadorDAO:

    trabajador: Trabajador

    def leer_trabajadores(self, sexo):
        try:
            sql = "select * from trabajadores where sexo = %s"
            conn = Connection(config)
            cursor = conn.cursor()
            response = cursor.execute(sql, (sexo, ))

            conn.commit()
            return response
        except Exception as e:
            print(f"error de tipo {e}")