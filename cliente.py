#!/usr/bin/env python
import usuario

class Cliente (usuario.Usuario):
    def __init__(self, nombre, cedula, username, email, password, tipoUsuario):
        usuario.Usuario.__init__(self, nombre, cedula, username, email, password, tipoUsuario)
    

    def comprar(self, vendedor, producto, cantidadAComprar):

        if self.logeado is True & vendedor.logeado is True :
                if vendedor.vender(producto, cantidadAComprar) == True :
                    print ("Compra exitosa")
                else:
                    print ("Compra anulada")
        else : 
            print ("Ambas partes deben logearse")
