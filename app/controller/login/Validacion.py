# # from ...DB.config.Connection import Connection
# # from ...DB.config.db_config import config


# class Validacion:
#     '''Esta clase crea un objeto de sesion válida o inválida'''
#     usuario: str
#     password: str
    

#     def encriptar(self):
#         return encrypt(self.password)
    
#     # # CLARAMENTE DEBO MODIFICAR ESO PARA QUE USE EL MODULO DB, PERO ESTÁ ASI PARA PRUEBAS
#     # def consulta_credenciales(self):
#     #     try:
#     #         sql = "select * from usuarios where nombre (%s)"
#     #         conn = Connection(config)
#     #         cursor = conn.cursor()
#     #         query = cursor.execute(sql, (self.usuario, ))
#     #         self.query = query
#     #         conn.commit()
#     #         conn.close()
#     #         return query
#     #     except Exception as e:
#     #         print(e)
#     #         return None
    
#     def validar_password(password, query):
#         if password in query:
#             return True
#         else:
#             return False