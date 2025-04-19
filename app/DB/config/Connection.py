from mysql.connector import connect, Error

class Connection:
    _instance = None

    def __new__(cls, config):
        if cls._instance is None:
            try:
                cls._instance = connect(**config)

                if cls._instance.is_connected():
                   print("Conexión establecida")

            except Error as e:
                print(f"Error al conectar la BD {e}")
                cls._instance = None

        return cls._instance



