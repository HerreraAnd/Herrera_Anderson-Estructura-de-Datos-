class InversorSecuencia:
    def invertir_lista(self, lista):
        lista_invertida=[]
        for i in range (len(lista) -1, -1, -1):
            lista_invertida.append(lista[i])
        return lista_invertida
    def invertir_multiple(self, *listas):
        resultado = {}

        for lista in listas:
            original = tuple(lista)
            invertida= self.invertir_lista(lista)
            resultado[original]=invertida
        return resultado
invertir=InversorSecuencia()
print(invertir.invertir_lista([5,6,7]))
print(invertir.invertir_multiple([4,6,7], [8,9,10]))