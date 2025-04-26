
class Sesion:

    usuario: any

    def controlar_sesion(self, usuario):
        # print(usuario.sesion)
        # print(type(usuario.sesion))

        if usuario.sesion == 0:
            print("iniciando sesion")
            usuario.sesion = 1
        else:
            if usuario.sesion == 1:
                usuario.sesion = 0 

        return usuario