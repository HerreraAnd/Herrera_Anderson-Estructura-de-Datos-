class combinadorlistas():
    def intercalar(self, lista1, lista2):
        resultado=[]
        for i in range (max(len(lista1), len(lista2))):
            if i<len(lista1):
                resultado.append(lista1[i])

            if i<len(lista2):
                resultado.append(lista2[i])
        return resultado
    def intercalar_multiple(self, *listas):
        resultado=[]
        for lista in listas:
            resultado=self.intercalar(resultado, lista)
        return resultado

combinacion=combinadorlistas()
respuesta=combinacion.intercalar([3,4], [5,7])
print(respuesta)