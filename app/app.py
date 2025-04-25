from DB import db
from controller import controller
from modules.modules import hash_password 

# SE MUESTRA PANTALLA DE INICIO
def main():
    print("inicio main")
    # USUARIO INGRESA SUS CREDENCIALES
    # captura = controller.login_captura()
    # # print(captura)
    # nombre, contrasenna = captura
    # contrasenna = hash_password(contrasenna)
    # print(nombre, contrasenna)
    credenciales = {'nombre':'jperez', 'contrasenna':'b0449274d1f88c60a759409bd3f3931c'}
    
    retorno_db = db.leer_usuario(credenciales)
    print(retorno_db)

    sesion_activa = controller.sesion(retorno_db)
    print(sesion_activa)
    usuario = db.actualizar_estado_sesion(sesion_activa)
    print(usuario)


    print("fin main")
    
# REDIRIGE A FUNCIONES PROPIAS DEL PERFIL

# # PERFIL TRABAJADOR
# SE MUESTRA INICIO DEL TRABAJADOR CON EL MENU DE OPCIONES:
    # MOSTRAR/MODIFICAR DATOS PERSONALES
    # MOSTRAR DATOS LABORALES

main()















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
