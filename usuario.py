#!/usr/bin/env python

class Usuario:
    
    def __init__(self, nombre, cedula, username, email, password, tipoUsuario):
        self.nombre = nombre
        self.cedula = cedula
        self.username = username
        self.email = email
        self.password = password
        self.tipoUsuario = tipoUsuario
        self.logeado = False

    def login(self, usuarios):
        finded = False
        for usuario in usuarios:
            if usuario.username == self.username:
                finded = True
                if usuario.password == self.password:
                    self.logeado = True
                    print ("Se ha iniciado sesion como "+self.username)
                else:
                    print ("Your password is wrong")

        if finded is False:
            print ("Usuario no registrado")       

    def logout(self):
        self.logeado = False
        print ("Se ha cerrado la sesion de " + self.username)

                

