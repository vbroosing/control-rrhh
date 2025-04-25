class Sesion:

    def iniciar_sesion(self, usuario):
        if usuario.sesion == 0:
            print("iniciando sesion")
            usuario.sesion = 1
            return usuario
        else:
            return usuario
        
    def finalizar_sesion(self, usuario):
        print("finalizando sesion")
        usuario.sesion = 0
        return usuario
    