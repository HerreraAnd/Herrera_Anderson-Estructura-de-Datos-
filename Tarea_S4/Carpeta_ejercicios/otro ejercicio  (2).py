##registro producto unico
class Registro_producto:
    def __init__(self):
        self.productos=[]
        self.producto_unico=set()
    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.producto_unico.add(producto)
        return self.producto_unico
    def contar_producto(self):
        return len(self.producto_unico)
    def agregar_multiples(self, *args):
        for producto in args:
            self.agregar_producto(producto)
        return self.productos
c=Registro_producto()
print(c.agregar_multiples("Producto_1", "Producto_2", "Producto_1"))
print(c.contar_producto())