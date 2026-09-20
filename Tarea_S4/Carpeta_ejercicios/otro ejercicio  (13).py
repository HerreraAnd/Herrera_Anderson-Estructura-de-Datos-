class Combinador_de_listas:
    def intercalar(self, lista1, lista2):
        resultado=[]
        i=0
        while i<len(lista1) or i<len(lista2):
            if i <len(lista1):
                resultado.  append(lista1[i])
            if i <len(lista2):
                resultado.append(lista2[i])
            i+=1
        return resultado
    def intercalar_multiples(self, *args):
        resultado=[]
        i=0
        while True:
            agregado=False
            for lista in args:
                if i <len(lista):
                    resultado.append(lista[i])
                    agregado=True
            if not agregado:
                break
            i+=1
        return resultado
x=Combinador_de_listas()
print(x.intercalar_multiples(
    [1, 2], 
    ["b","c"], 
     ["X","Y"]
))
