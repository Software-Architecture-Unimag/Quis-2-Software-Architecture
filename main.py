#!/usr/bin/env python
import usuario
import administrador
import vendedor
import cliente
import producto

cliente = cliente.Cliente("Pedro Pineda", "1234456", "pedro", "pedro@gmail.com", "1234", "Cliente")
vendedor = vendedor.Vendedor("Jose Pineda", "1234456", "jose", "jose@gmail.com", "1234", "Vendedor", "Frutas")
usuarios = []
usuarios.append(cliente)
usuarios.append(vendedor)

vendedores = []
vendedores.append(vendedor)
admin = administrador.Administrador("Juan Perez", "1234567", "juan", "juanito@gmail.com", "1234", "Administrador", vendedores)
usuarios.append(admin)

producto1 = producto.Producto("Manzana", 12, 12, "fruta")

admin.login(usuarios)
cliente.login(usuarios)
vendedor.login(usuarios)

cliente.comprar(vendedor, producto1, 10)

cliente.logout()
cliente.comprar(vendedor, producto1, 3)
cliente.login(usuarios)
cliente.comprar(vendedor, producto1, 3)
