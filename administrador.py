#!/usr/bin/env python
import usuario

class Administrador (usuario.Usuario):
    def __init__(self, nombre, cedula, username, email, password, tipoUsuario, vendedores):
        usuario.Usuario.__init__(self, nombre, cedula, username, email, password, tipoUsuario)
        self.vendedores = vendedores

    def getVendores(self):
        print ("Tus vendedores son:")
        for vendedor in self.vendedores:
            print (vendedor+" ha realizado "+vendedor.nVentas)
