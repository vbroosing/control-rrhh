from .models.PerfilDTO import Perfil
from .models.UsuarioDTO import Usuario
from .models.AreaDTO import Area
from .models.DepartamentoDTO import Departamento

from .DAO.PerfilDAO import PerfilDAO
from .DAO.UsuarioDAO import UsuarioDAO
from .DAO.AreaDAO import AreaDAO
from .DAO.DepartamentoDAO import DepartamentoDAO

def crear_perfil(nombre):
    perfil = Perfil(nombre)
    dao = PerfilDAO(perfil)
    print(dao.insertar_perfil(perfil))

def crear_usuario(usuario, **args):
    usuario = Usuario(**args)
    dao = UsuarioDAO(usuario)
    print(dao.insertar_usuario(usuario))

def crear_area(nombre):
    area = Area(nombre)
    dao = AreaDAO(area)
    print(area)
    print(dao.insertar_area(area))
    
def crear_departamento(area_id, nombre):
    departamento = Departamento(area_id, nombre)
    dao = DepartamentoDAO(departamento)
    print(departamento)
    print(dao.insertar_departamento(departamento))

def leer_usuario(credenciales):
    usuario = Usuario(0,0,credenciales['nombre'], credenciales['contrasenna'], 0)   
    dao = UsuarioDAO(usuario)
    response = dao.buscar_usuario(usuario)
    # print(response)

    if response:
        return response
    else:
        return "aaaaaaaaaaaaaaaaaaaaaa"
    
def actualizar_estado_sesion(usuario):
    dao = UsuarioDAO(usuario)
    usuario = dao.actualizar_sesion_usuario(usuario)
    return usuario



# from datetime import date

#for per in dao.listarPersona():
#    print(per)
#    print("========================")
#print(dao.actualizarPersona(p1))
#print(dao.eliminarPersona(p1))
# print(dao.buscarPersona("111111-1"))