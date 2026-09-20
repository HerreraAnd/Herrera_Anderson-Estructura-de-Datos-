class RegistroPrecios:
    def __init__(self):
        self.productos={}
    def registrar(self, producto, precio):
        self.productos[producto]=precio
    def productos_baratos(self, precio_maximo):
        resultado=[]
        for producto, precio in self.productos.items():
            if precio<=precio_maximo:
                resultado.append(producto)
        return resultado
    def producto_mas_caro(self):
        producto_mayor=None
        precio_mayor=0
        for producto, precio in self.productos.items():
            if precio>precio_mayor:
                precio_mayor=precio
                producto_mayor=producto
        return (producto_mayor, precio_mayor)
x=RegistroPrecios()
x.registrar("Pan", 1.50)
x.registrar("Leche", 2.00)
x.registrar("Cafe", 5.00)
print(x.productos_baratos(2.00))
print(x.producto_mas_caro())