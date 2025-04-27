from dataclasses import dataclass
from ..config.Connection import Connection
from ..config.db_config import config
from ..models.Carga_familiarDTO import Carga_familiar

@dataclass
class Carga_familiarDAO:

    carga_familiar: Carga_familiar

    def insertar_carga_familiar(self, carga_familiar):
        try:
            sql = "insert into cargas_familiares (trabajador_id, rut, nombre, apellido, parentesco, sexo) values (%s, %s, %s, %s, %s, %s);"
            conn = Connection(config)
            cursor = conn.cursor()
            cursor.execute()
            conn.commit()
        except Exception as e:
            print(e)
            