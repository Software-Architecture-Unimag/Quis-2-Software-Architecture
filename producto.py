#!/usr/bin/env python

class Producto :
    def __init__(self, nombre, precio, cantidad, categoria):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def venta(self, cantidaVendida):
        self.cantidad = self.cantidad - cantidaVendida