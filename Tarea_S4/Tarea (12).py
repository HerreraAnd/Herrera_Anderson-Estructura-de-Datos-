class Selector_rango:
    def crear_rango(self, inicio, final):
        return tuple(range(inicio, final+1))
    def elementos_en_diferentes_rangos(self, *rangos):
        elementos=set()
        for inicio, final in rangos:
            elementos.update(self.crear_rango(inicio, final))
            return sorted(elementos)
selector=Selector_rango()
respuesta=selector.elementos_en_diferentes_rangos((1,5), (2,4))
print(respuesta)