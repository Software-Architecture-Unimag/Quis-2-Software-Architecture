#!/usr/bin/env python
import usuario

class Vendedor (usuario.Usuario):
    def __init__(self, nombre, cedula, username, email, password, tipoUsuario, departamento):
        usuario.Usuario.__init__(self, nombre, cedula, username, email, password, tipoUsuario)
        self.departamento = departamento
        self.nVentas = 0

    def vender(self, producto, cantidadAComprar):

        if producto.cantidad >= cantidadAComprar :
            self.nVentas = self.nVentas + 1
            producto.venta(cantidadAComprar)
            print ("Venta exitosa")
            return True
        else:
            print ("No tenemos sufientes unidades")
            return False
