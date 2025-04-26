from .login.login import captura_datos
from .sesion.Sesion import Sesion

def login_captura():
    return captura_datos()

def sesion(usuario): 
    sesion = Sesion()
    usuario = sesion.controlar_sesion(usuario)
    return usuario

