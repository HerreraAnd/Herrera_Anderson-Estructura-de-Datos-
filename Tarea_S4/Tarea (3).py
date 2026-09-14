class CarroCompras:
    def __init__(self):
        self.precios=[]
    def agregar_articulo(self, precio):
        self.precios.append(precio)
    def total_carrito(self):
        return sum(self.precios)
total=CarroCompras()
total.agregar_articulo("Pan", 2.10)
total.agregar_articulo("queso", 3.30)
total.agregar_articulo("leche", 5)

print(total.total_carrito())