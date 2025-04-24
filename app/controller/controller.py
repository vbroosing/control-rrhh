from .login.login import captura_datos
# from ..DB.models import UsuarioDTO

def login_captura():
    return captura_datos()

def sesion(usuario): 
    if usuario.sesion == 0:
        usuario.sesion = 1
        return usuario
    else:
        usuario.sesion = 0
        return usuario


