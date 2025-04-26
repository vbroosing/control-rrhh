from mysql.connector import connect, Error

class Connection:
    '''Esta clase crea un singleton de la conexión a la base de datos.'''
    _instance = None

    def __new__(self, config):
        if self._instance is None:
            try:
                self._instance = connect(**config)

                if self._instance.is_connected():
                   print("Conexión establecida")

            except Error as e:
                print(f"Error al conectar la BD {e}")
                # self._instance = None
                raise

        return self._instance




















# from mysql.connector import connect, Error

# class Connection:
#     '''Singleton mejorado para conexión a la base de datos.'''
#     _instance = None

#     @classmethod
#     def get_instance(self, config):
#         if self._instance is None or not self._instance.is_connected():
#             try:
#                 self._instance = connect(**config)
#                 print("Conexión establecida")
#             except Error as e:
#                 print(f"Error al conectar la BD: {e}")
#                 raise  # Lanza la excepción para manejarla externamente
        
#         return self._instance