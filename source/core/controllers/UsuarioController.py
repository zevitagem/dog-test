from ast import arg
from core.services.UsuarioService import UsuarioService


class UsuarioController():

    def __init__(self):
        self.service = UsuarioService()

    def index(self, args):
        return 'Hello World!'
