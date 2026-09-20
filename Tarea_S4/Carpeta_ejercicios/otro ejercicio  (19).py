#Ejercicio: Biblioteca de libros
class Biblioteca:
    def __init__(self):
        self.libros = {}
    def agregar_libros(self, titulo, cantidad):
        if titulo in self.libros:
            self.libros[titulo] += cantidad
        else:
            self.libros[titulo] = cantidad
    def prestar_libros(self, titulo, cantidad):
        if titulo in self.libros and self.libros[titulo] >= cantidad:
            self.libros[titulo] -= cantidad
            return True
        return False
    def libros_bajo_stock(self, minimo):
        resultado = []
        for titulo, cantidad in self.libros.items():
            if cantidad < minimo:
                resultado.append(titulo)
        return resultado
x = Biblioteca()
x.agregar_libros("Python", 20)
x.agregar_libros("Java", 5)
print(x.prestar_libros("Python", 8))
print(x.prestar_libros("Java", 10))
print(x.libros_bajo_stock(10))
