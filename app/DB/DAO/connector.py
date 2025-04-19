from mysql.connector import connect

@staticmethod
def connection():
    return connect(user="root", 
                             password="abcABC123*-3",
                             database="el_correo_de_yuri")