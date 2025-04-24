'''Este modulo valida el ingresaro '''
def captura_datos():
    while True:
    
        usuario = input("Usuario: ")
        password = input("Password: ")

        print("Presiona enter para continuar,")
        opcion = input("ó ingresa ingresa cualquier tecla para reintentar.. .")

        if opcion == "":
            return usuario, password
                
        else:
            print("\nReingresar datos!\n")
