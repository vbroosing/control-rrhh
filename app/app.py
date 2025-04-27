from DB import db
from controller import controller
from modules.modules import hash_password 
from DB.models.UsuarioDTO import Usuario
from DB.models.TrabajadorDTO import Trabajador
from datetime import date

# SE MUESTRA PANTALLA DE INICIO
def main():
    print("inicio main")
    # # USUARIO INGRESA SUS CREDENCIALES
    # captura = controller.login_captura()
    # # print(captura)
    # nombre, contrasenna = captura
    # contrasenna = hash_password(contrasenna)
    # print(nombre, contrasenna)
    # credenciales = {'nombre': nombre, 'contrasenna': contrasenna}
    credenciales = {'nombre':'jperez', 'contrasenna':'b0449274d1f88c60a759409bd3f3931c'}
    
    retorno_db = db.leer_usuario(credenciales)
    # print('', retorno_db)

    sesion_activa = controller.sesion(retorno_db)
    # print(sesion_activa)
    
    usuario = db.actualizar_estado_sesion(sesion_activa)
    # print(usuario)

    if usuario.sesion:

        # REDIRIGE A FUNCIONES PROPIAS DEL PERFIL
        if usuario.perfil_id == 1:
            pass
        elif usuario.perfil_id == 2:
            pass
        elif usuario.perfil_id == 3:
            sesion_jefe_RRHH(usuario)

        db.actualizar_estado_sesion(usuario)
    else:
        print('Sesion iniciada en otro dispositivo !')    

    print('Hasta luego!')
    print("fin main")
    

# # PERFIL TRABAJADOR
# SE MUESTRA INICIO DEL TRABAJADOR CON EL MENU DE OPCIONES:
    # MOSTRAR/MODIFICAR DATOS PERSONALES
    # MOSTRAR DATOS LABORALES
def sesion_trabajador(usuario: Usuario):
    pass

def sesion_RRHH(usuario: Usuario):
    pass

# # PERFIL JEFE RRHH
# SE MUESTRA EL INICIO DEL JEFE DE RRHH
def sesion_jefe_RRHH(usuario: Usuario):
    while True:
        print('sesion jefe RRHH\n')
        try:
            print(f'''Bienvenido {usuario.nombre}
========================
Ingresa una opción del menú para listar:
1) Por Sexo
2) Por cargo
3) Por área y departamento''')
            opcion_menu = input("\n ó escribe 0 para cerrar sesión: ")
            opcion_menu = int(opcion_menu)

            if opcion_menu == 0:
                usuario = controller.sesion(usuario)
                return usuario
            
            elif opcion_menu == 1:
                while True:
                    sexo = input("Ingresa M(Masculino), F(Femenino) ó U(undefined)")
                    if sexo.upper() == "M" or sexo.upper() == "F" or sexo.upper() == "U":
                        lista_filtrada_por_sexo = db.leer_trabajadores_por_condicion(usuario, sexo)
                        break
                    else:
                        print("Escoja una opción de la lista")
                
                input('\nPresiona enter para regresar al menu\n')

            elif opcion_menu == 2:
                print("\nFiltro por Cargo\n")
                input('Presiona enter para regresar al menu')
            elif opcion_menu == 3:
                print("\nFiltro por Área\n")
                input('Presiona enter para regresar al menu')
            else:
                print("\nDebes ingresar una opcion del menú!!\n")
                input('Presiona enter para regresar al menu')                
        except:
            print('error')


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
