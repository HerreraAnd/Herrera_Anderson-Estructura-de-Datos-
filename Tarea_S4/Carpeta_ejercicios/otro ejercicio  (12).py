class Selector_pares:
    def crear_rango(self, inicio, fin):
        pares = []
        for numero in range(inicio, fin + 1):
            if numero % 2 == 0:
                pares.append(numero)
        return tuple(pares)
    def pares_en_multiples_rangos(self, *args):
        elementos = set()
        for inicio, fin in args:
            elementos.update(self.crear_rango(inicio, fin))
        return sorted(elementos)
x = Selector_pares()
print(x.crear_rango(1, 6))
print(x.pares_en_multiples_rangos((1, 6), (4, 10)))
