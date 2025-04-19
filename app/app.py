from DB import db
from controller.login import Validacion

# # CREAR PERFILES
# db.crear_perfil("Trabajador")
# db.crear_perfil("RRHH")
# db.crear_perfil("Jefe de RRHH")
# db.crear_perfil("Gerente General")
# db.crear_perfil("Developer")

# # CREAR AREAS
# db.crear_area("RRHH")
# db.crear_area("Administración y finanzas")
# db.crear_area("TI")
# db.crear_area("Logística y cadena de suministros")

# CREAR DEPARTAMENTOS
# db.crear_departamento("1", "Desarrollo organizacional")

print("Bienvenido")
print("==========")

usuario = input("Usuario: ")
password = input("Contraseña: ")

validacion = Validacion(usuario, password)